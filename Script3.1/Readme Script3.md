# Script3.1-Book scrapper
> This script will go through each category in https://books.toscrape.com/ ,collect each book link in a category then collect the data of each book and save them in a separate csv file for each category 

> Ce script collecte les liens de chaque livres présent de chaque catégorie de https://books.toscrape.com/ puis collecte les données de chaque livre et les sauvegardes dans un fichier csv séparé pour chaque catégorie.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)


## General Information
- This script will go through each category in https://books.toscrape.com/ and collect each book links present in that category.Then it will collect a set of data (product page url,universal product code (upc),title,price including tax,price excluding tax,number available,product description,category,review rating,image url) from each book.These data will then be saved in a separate csv file present in a directory created for each category
- Ce script collecte les liens des livres présent sur chaque catégorie de https://books.toscrape.com/ .A partir de ces liens il collecte un enssemble de donnés (page url du produit,code upc,titre,prix avec taxe,prix sans taxe,nombre disponible,description du produit,catégorie,évaluation,url de l'image) pour chaque livres.Les données sont ensuite sauvegardées dans des fichiers csv séparés par catégorie et présent dans un dossier dédié.

- This script is the third step in the creation of a system to collect data from https://books.toscrape.com/ at a given time so we can follow price variation.
- Ce script est la troisième étape dans la création d'un systeme collectant les données de https://books.toscrape.com/ dans l'objectif de suivre la variation des prix.


## Technologies Used
- Tech 1 - requests
- Tech 2 - breautifulsoup4 bs4

## Features
List the ready features here:
- Collect all links from a category page.
- Collecte les liens présent sur la page d'une catégorie

- Use these links to collect data from each book in a category page.
- Utilise ces liens pour collecter les données de la page de chaque livre

- Save the data of each book in a category in a csv file present in a dedicated directory
- Sauvegarde les données de chaque livre dans une catégorie dans un fichier csv présent dans un dossier dédié.

- Save the Picture of each book in a directory linked to the book category
- Sauvegarde les images de chaque livre dans une dossier nommé selon la catégorie du livre.


## Setup
To run this script you will need Python3.8 or above and the package described in the requirements.txt file.You can install them in a separate virtual environment following these step*:
- Navigate to the directory on which the script is present in your terminal.
- Create a new virtual environment using 'python -m venv env'
- Activate your virtual environment using 'env/scripts/activate'
- Install the packages using 'pip install -r requirements.txt'

(The process can differ on OS other than windows)

Pour faire fonctionner ce script,vous aurez besoin d'une version de Python3.8 ou supérieure et des packages décrit dans le fichier requirements.txt.Vous pouvez les installer dans un environement virtuel séparé en suivant ces étapes*:
- Dans votre terminal,naviguez jusqu'au dossier où le script est présent.
- Créez un nouvel environement virtuel en utilisant 'python -m venv env'
- Activez votre environement virtuel avec 'env/scripts/activate'
- Installez les packages nécessaire avec 'pip install -r requirements.txt'

(Les étapes peuvent être différentes sur un OS différent de windows)

## Usage

After installing the required package,to use this script, run the script by typing 'python Script3.1.py' in your terminal.The script will indicate as it goes through each page so that can check it is running correctly.You will need to rename the main directory "Script 3.1 Data" before using the script again.

Après vous êtres assuré que les packages nécessaire sont installés,vous pouvez lancer le script en tappant 'python Script3.1.py" dans votre terminal.Le script indiquera chaque page qu'il vient de parcourir,indiquant ainsi qu'il fonctionne corréctement.Il vous faudra renomer le dossier"Script 3.1 Data" avant de pouvoir relancer le script.

## Project Status
Project is: _completed_