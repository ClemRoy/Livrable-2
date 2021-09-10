# Script1-Book scrapper
> This script will collect a set of data from any book page coming from https://books.toscrape.com/ and save it as a csv file.

> Ce script collecte les données d'une page de livre provenant du site https://books.toscrape.com/ et la sauvegarde sous la forme d'un fichier csv.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


## General Information
- This script will collect a set of data (product page url,universal product code (upc),title,price including tax,price excluding tax,number available,product description,category,review rating,image url) from any book page coming from https://books.toscrape.com/ and save it in a csv file named data.
- Ce script collecte un enssemble de données (page url du produit,code upc,titre,prix avec taxe,prix sans taxe,nombre disponible,description du produit,catégorie,évaluation,url de l'image) depuis n'importe quelle page de livre du site https://books.toscrape.com/ et les sauvegarde sous la forme d'un fichier csv appelé data.

- This script is the first step in the creation of a system to collect data from https://books.toscrape.com/ at a given time so we can follow price variation.
- Ce script est la première étape dans la création d'un systeme collectant les données de https://books.toscrape.com/ dans l'objectif de suivre la variation des prix.


## Technologies Used
- Tech 1 - requests
- Tech 2 - breautifulsoup4 bs4

## Features
List the ready features here:
- Collect data from a single book page and save it as a csv file.
- Collecte les données de la page d'un livre et les sauvegarde sous la forme d'un fichier csv.

## Setup
To run this script you will need Python3.8 or above and the package described in the requirements.txt file.You can install them in a separate virtual environment following these step:
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

After installing the required package,to use this script,open it in an editor and modify the url variable by pasting the url of the book page you wich to collect data from inside the "" line 9,make sure to save before you exit the editor.Then run the script by typing 'python Script1.py' in your terminal

Après vous êtres assuré que les packages nécessaire sont installés,ouvrez le script dans un éditeur et modifier la variable située ligne 9 en copiant l'adresse url de la page dont vous souhaitez collecter les données dans les "".Après avoir sauvegardé et quitter l'éditeur,vous pouvez lancer le script en tappant 'python Script1.py" dans votre terminal.

## Project Status
Project is: _in progress_


## Room for Improvement
The scope of this project is to collect all books from each category of the https://books.toscrape.com/ site.Next step should be to collect books data from a category 
L'objectif de ce projet est de collecter les données de tout les livre de chaque catégories du site https://books.toscrape.com/ .La prochaine étape consiste a collecter les données de tout les livres d'une catégorie.

Room for improvement:
- extend the script to each book in a category
- étendre le script a tout les livres d'une catégorie

- extend the script to each category on the site
- étendre le script a toutes les catégories du site

To do:
- create a function to collect all book links in a category then collect data from each book.
- créer une fonction permettant de collecter les liens de chaque livre puis de collecter les données de chaque lien.
