#packages
import csv
from bs4.element import PageElement
import requests
import re
from bs4 import BeautifulSoup
import os

home_page = 'http://books.toscrape.com/'
home_page_req = requests.get(home_page)
home_page_soup = BeautifulSoup(home_page_req.text, 'html.parser')

#create dictionnary linking category name and category url
side_categ_list_name_and_url = []
categs = home_page_soup.find(class_="side_categories").findAll('a')
for a in categs:
    categ_name_and_url = {}
    categ_name_and_url['book_category'] = a['href'].replace('catalogue/category/books/', '').replace("/index.html", '')
    categ_name_and_url['url'] = home_page + a['href']
    side_categ_list_name_and_url.append(categ_name_and_url)
side_categ_list_name_and_url.pop(0)

#scrap a book data and return it as a list of 10 elements per book

def book_scrapper(book_url):
    book_page = requests.get(book_url)
    book_soup = BeautifulSoup(book_page.text, 'html.parser')
    data = []
    Book_data = []
    table = book_soup.find('table', attrs={'class':'table table-striped'})
    rows = table.find_all('tr')
    THS_TO_IGNORE = ['Number of reviews', 'Product Type', 'Tax']
    for row in rows:
        if row.th.text not in THS_TO_IGNORE:
            cells = row.find_all('td')
            cells = [{row.th.text:ele.text.strip()} for ele in cells]
            data.append([ele for ele in cells if ele]) 
    upc = data[0][0]['UPC']
    pricExTraw = data[1][0]['Price (excl. tax)']
    pricExT = str(re.findall(r"[-+]?\d*\.\d+|\d+", pricExTraw))
    pricInTraw = data[2][0]['Price (incl. tax)']
    pricInTr = str(re.findall(r"[-+]?\d*\.\d+|\d+", pricInTraw))
    availraw = data[3][0]['Availability']
    avail = int(re.search(r'\d+', availraw).group())
    descr = book_soup.find_all('p', str)[3].get_text()
    titre = str(book_soup.find("h1")).strip('<h1>').strip('</')
    Imagesraw = book_soup.find(class_="item active").find('img').get('src').replace("../", "")
    Images = "http://books.toscrape.com/" + Imagesraw
    review = book_soup.find("p", class_="star-rating")["class"][1]
    book_cat = book_soup.select('a[href]')[3].text
    Book_data.append([book_url ,upc,titre,pricInTr,pricExT,avail,descr,book_cat,review,Images])
    return Book_data

#scrap a category page and return all book in page

def scrap_book_links(urltoscrap):
    Links = []
    page = requests.get(urltoscrap)
    soup = BeautifulSoup(page.text, "html.parser")
    urls = soup.find_all("h3")
    for url in urls:
        a = url.find('a')
        linkraw = a['href']
        Linkstr = 'http://books.toscrape.com/catalogue/' + linkraw.replace("../", "")
        Links.append(Linkstr)
    return Links

#scrap through all page in a category and return all book links in a category


def genlinks(url):
    Links = []
    catPage = requests.get(url)
    catSoup = BeautifulSoup(catPage.text, 'html.parser')
    pagenumber = 1
    if catSoup.find("li", class_="next") == None:
            Links += scrap_book_links(url)
            print(url + ' done')
    else:
        while True:
            catPageUrl = url.replace('index.html', '') + 'page-' + str(pagenumber) + '.html'
            catPageM = requests.get(catPageUrl)
            catSoupM = BeautifulSoup(catPageM.text, 'html.parser')
            Links += scrap_book_links(catPageUrl)
            print(catPageUrl + ' done')
            pagenumber += 1
            if catSoupM.find("li", class_="next") == None:
                Links += scrap_book_links(catPageUrl)
                break 
    return Links

#download book img from link

def save_image (path,url):
    resp = requests.get(url)
    with open( path , 'wb') as jpg:
        jpg.write(resp.content)



#collect data from all category and write csv file

def write_to_csv(book_category,Links):
    os.mkdir('Script 3.1 Data/'+book_category)
    dirpath = 'Script 3.1 Data/'+ book_category+ '/'     
    Book_data = []
    for link in Links:
        data = book_scrapper(link)
        for infolink in data:
            image_name = ''.join(e for e in infolink[2] if e.isalnum())
            save_image(dirpath+image_name[:25]+'.jpg',infolink[-1])
        Book_data += book_scrapper(link)
        print(link+ ' done')
    en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    with open(dirpath + book_category+'data.csv' , 'w',  encoding="utf-8") as fichier_csv:
          writer = csv.writer(fichier_csv, delimiter=",")
          writer.writerow(en_tete)
          for book_data in Book_data:
              ligne = book_data
              writer.writerow(ligne)
    print( book_category + 'file done')
        
#Goes through each category in the dictionnary and create a csv file with the data
os.mkdir('Script 3.1 Data/')
for dic in side_categ_list_name_and_url:
    write_to_csv(dic['book_category'],genlinks(dic['url']))
print('Script Done')