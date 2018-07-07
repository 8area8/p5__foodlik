# Foodlik, an API for good people

[TRELLO's link](https://trello.com/b/6xV0TMFR/p5-foodlik)

``` acsii
oooooooooooo                           .o8  oooo   o8o  oooo
'888'     '8                          "888  '888   '"'  `888
 888          .ooooo.   .ooooo.   .oooo888   888  oooo   888  oooo
 888oooo8    d88' '88b d88' '88b d88' '888   888  `888   888 .8P'
 888    "    888   888 888   888 888   888   888   888   888888.
 888         888   888 888   888 888   888   888   888   888 `88b.
o888o        'Y8bod8P' 'Y8bod8P' `Y8bod88P" o888o o888o o888o o888o
```

*An elegant UI based on OpenFoodFact.*

The application has a large portion of French food listed on OpenFoodFact. It repeats these foods, displays their information and generates substitute foods with a higher score.

## Installation

This UI need some other programs to work well.

### Install Python

Foodlik is based on python, an elegant coding langage.
Get the last Python's version at the [following link](https://www.python.org/).
Be sure you got the 3.6 version (or newer).
Check for "pip" and for the root integration in the installation.

### Install the database

Curently, Foodlik only support PostgreSQL.
Go to the [following link](https://www.postgresql.org/) and install PostgreSQL on your computer.

#### Why PostgreSQL

C'est un choix arbitraire. J'ai surtout voulu garder la version 3.6 de Python et, il semblait après quelques recherches que seul les extension python pour Postgres supportent la 3.6.

### Install some Python's librairies

Foodlik uses some third-party Python's librairie.

**Note:** You should set a new virtual environment before installing.

* ```pip install terminaltables```. Allow you to display console tables.
* ```pip install pyfiglet```. Allow you to display texts in ASCII art.
* ```pip install termcolor```. Allow you to display colored texts.
* ```pip install colorama```. Allow you to color the text.

**Optionnal:** ```pip install pytest```. For those who want to run the tests.

## Quickstart

1. Create a new virtual environment and install the required programs.
1. Open your favorite SHELL at the root of the folder.
1. Launch postgresql.
1. Type ```python main.py --create_database``` and wait few minutes.
1. Simply type ```python main.py```.
1. Enjoy.

## Structure

### User Interface

L'interface utilisateur possède 4 sections :

* l'acceuil
* les catégories
* les produits d'une catégorie
* le produit séléctionné

chaque section suit le schéma suivant :

* Un header : affiche le titre de la section.
* un corps : affiche le contenu de la section.
* un footer : affiche les commandes possibles dans la section.

**Exemples :**

exemple 1
exemple 2
exemple 3
exemple 4

### DATAS

Les données de ce programme viennent toutes de l'API OpenFoodFact.
Les premières données sont les catégories, au nombre de **nombre** :

* liste
* des
* catégories

vient ensuite les produits, au nombre de **nombre**.
Chaque produit possède :

* liste
* des
* attributs
* des
* produits (et leur clé de base)

#### Filters

Les produits ont été filtrés. Ont été mis de côté :

* ceux qui n'appartenaient pas aux catégories retenues
* ceux qui ne possédaient pas de nutri-score
* les produits doublons (un produit au nom similaire a déjà été ajouté)

#### Substituts

Les substituts suivent deux algorithmes, qui retournent chacun un produit de substitution.
Le premier va chercher un produit avec un meilleur score dans la catégorie la moins fournie du produit ciblé.
Le deuxième va chercher un produit avec un bien meilleur score dans la 2eme ou 3eme catégorie la moins fournie du produit ciblé.

## Options

The UI has several options that have passed since the SHELL.

### Update the database

**Note:** The update is done slowly. Do not be presced.

1. Type ```python main.py --load_pages```. This option retrieve data from the OpenFoodFact site.

**Note:** You can also specify the desired page number by typing ```python main.py --load_pages 1-5```. The pattern is as follows: ```main.py (--load_pages | -l) [<first_page>[-<last_page>]]```

1. The data was stored in a json file. Let's go to the Data-base : ```python main.py --refurbish_database```.

### Advanced management of the database

* ```python main.py --recreate_database``` will delete and recreate the database. Warning: all data will be lost !

## Changelog