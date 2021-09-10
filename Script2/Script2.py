#packages
import csv
import requests
import re
from bs4 import BeautifulSoup

#Category to scrap
book_category = ""
book_category_name = book_category.replace('https://books.toscrape.com/catalogue/category/books/','').replace('/index.html','')


#Emptylist

Lbookurls = []
Lupcs = []
Ltitres = []
LpriceITs = []
LpriceETs = []
Lnumbavais = []
Lproddescrs = []
Lbook_categs = []
LReview = []
LImagesLink = []

#function to scrap a category page and get book urls

def scrapBookLinks(urltoscrap):
    page = requests.get(urltoscrap)
    soup = BeautifulSoup(page.text, "html.parser")
    urls = soup.find_all("h3")
    for url in urls:
        a = url.find('a')
        linkraw = a['href']
        Linkstr = 'http://books.toscrape.com/catalogue/' + linkraw.replace("../", "")
        Lbookurls.append(Linkstr)

#Function to scrap book page data

def book_scrapper(book_url):
    book_page = requests.get(book_url)
    book_soup = BeautifulSoup(book_page.text, 'html.parser')
    data = []
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
    pricExT = re.findall(r"[-+]?\d*\.\d+|\d+", pricExTraw)
    pricInTraw = data[2][0]['Price (incl. tax)']
    pricInTr = re.findall(r"[-+]?\d*\.\d+|\d+", pricInTraw)
    availraw = data[3][0]['Availability']
    avail = int(re.search(r'\d+', availraw).group())
    descr = book_soup.find_all('p', str)[3].get_text()
    titre = book_soup.find("h1")
    Images = book_soup.find(class_="item active").find('img').get('src').replace("../", "")
    review = book_soup.find("p", class_="star-rating")["class"][1]
    book_cat = book_soup.select('a[href]')[3].text
    Lupcs.append(upc)
    LpriceETs.append(pricExT)
    LpriceITs.append(pricInTr)
    Lnumbavais.append(avail)
    Lproddescrs.append(descr)
    Ltitres.append(titre.text)
    LImagesLink.append("http://books.toscrape.com/" + Images)
    LReview.append(review)
    Lbook_categs.append(book_cat)
    print(book_url + ' book done')

#Main script

cat_page = requests.get(book_category)
cat_soup = BeautifulSoup(cat_page.text, 'html.parser')
if cat_soup.find("li", class_="next") == None:
    scrapBookLinks(book_category)
    print(book_category +'done')
else:
    pagenumber = 1
    while True:
        book_category_formated = book_category.replace('index.html','page-')+str(pagenumber)+'.html'
        cat_page_formated = requests.get(book_category_formated)
        cat_soup_formated = BeautifulSoup(cat_page_formated.text, 'html.parser')
        scrapBookLinks(book_category_formated)
        pagenumber += 1
        print(book_category_formated + 'category page done')
        if cat_soup_formated.find('li',class_='next') == None:
            scrapBookLinks(book_category_formated)
            break  

for bookurl in Lbookurls:
    book_scrapper(bookurl)
print('Script done')

#Write data in csv

en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax_in£", "price_excluding_tax_in£", "number_available", "product_description", "category", "review_rating", "image_url"]

with open(book_category_name+'data.csv', 'w',  encoding="utf-8") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    for bookurl, upc, titre, priceIT, priceET, numbavai, proddescr, categ, review, imgurl in zip(Lbookurls ,Lupcs ,Ltitres ,LpriceITs ,LpriceETs, Lnumbavais, Lproddescrs, Lbook_categs, LReview, LImagesLink):
        ligne = [bookurl, upc, titre, priceIT, priceET, numbavai, proddescr, categ, review, imgurl]
        writer.writerow(ligne)