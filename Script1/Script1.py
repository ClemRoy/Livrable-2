#packages
import csv
import requests
from bs4 import BeautifulSoup
import re

#Url

url = ""

#Transforme page en objet bs4

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#Emptylist

Lpageurlsls = [ url ]
Lupcs = []
Ltitres = []
LpriceITs = []
LpriceETs = []
Lnumbavais = []
Lproddescrs = []
Lcategs = []
LReview = []
LImagesLink = []

#scrap upc, priceit, priceet, avail

data = []
table = soup.find('table', attrs={'class':'table table-striped'})

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
Lupcs.append(upc)
LpriceETs.append(pricExT)
LpriceITs.append(pricInTr)
Lnumbavais.append(avail)

#Scrap produc descr.

descr = soup.find_all('p', str)[3].get_text()
Lproddescrs.append(descr)

#Scrap titre

titre_bs = soup.find("h1")
Ltitres.append(titre_bs.text)

#scrap image url

Images = soup.find(class_="item active").find('img').get('src').replace("../", "")
#link= Images.find('img')
#img = link.get('src')

LImagesLink.append("http://books.toscrape.com/" + Images)

#Scrap review

review = soup.find("p", class_="star-rating")["class"][1]
LReview.append(review)

#Scrap category

Cat = soup.select('a[href]')[3].text
Lcategs.append(Cat)

#Création fichier csv

en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax_in£", "price_excluding_tax_in£", "number_available", "product_description", "category", "review_rating", "image_url"]

pageurlsls = [ Lpageurlsls ]
upcs = [ Lupcs ]
titres = [ Ltitres ]
priceITs = [ LpriceITs ]
priceETs = [ LpriceETs ]
numbavais = [ Lnumbavais ]
proddescrs = [ Lproddescrs ]
categs = [ Lcategs ]
reviews = [LReview ]
imgurls = [ LImagesLink ]

file_name = ''.join(e for e in Ltitres[0] if e.isalnum())

with open(file_name[:30]+ '.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    for pageurl, upc, titre, priceIT, priceET, numbavai, proddescr, categ, review, imgurl in zip(pageurlsls ,upcs ,titres ,priceITs ,priceETs, numbavais, proddescrs, categs, reviews, imgurls):
        ligne = [pageurl, upc, titre, priceIT, priceET, numbavai, proddescr, categ, review, imgurl]
        writer.writerow(ligne)