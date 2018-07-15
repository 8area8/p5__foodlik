# Foodlik, an API for good people

[TRELLO's link](https://trello.com/b/6xV0TMFR/p5-foodlik)

```ascii
oooooooooooo                           .o8  oooo   o8o  oooo
'888'     '8                          "888  '888   '"'  `888
 888          .ooooo.   .ooooo.   .oooo888   888  oooo   888  oooo
 888oooo8    d88' '88b d88' '88b d88' '888   888  `888   888 .8P'
 888    "    888   888 888   888 888   888   888   888   888888.
 888         888   888 888   888 888   888   888   888   888 `88b.
o888o        'Y8bod8P' 'Y8bod8P' `Y8bod88P" o888o o888o o888o o888o
```

*An elegant UI based on OpenFoodFact.*

>**NOTE :** enlarge the window of your control console for an optimal result

The application has a large portion of French food listed on OpenFoodFact. It repeats these foods, displays their information and generates substitute foods with a higher nutri-score.

## I - Installation

This UI need some other programs to work well.

### 1.1 - Install Python

Foodlik is based on python, an elegant coding langage.
Get the last Python's version at the [following link](https://www.python.org/).
Be sure you got the 3.6 version (or newer).
Check for "pip" and for the root integration in the installation.

### 1.2 - Install the database

Curently, Foodlik support PostgreSQL and MySQL.

PostgreSQL installation : [follow the link](https://www.postgresql.org/).
MySQL installation : [follow the link](https://www.mysql.com/). Install the MySQL GPL version.

#### 1.2.1 - ID, password and environnment variables

You can create a new file and write your ID and password database.

### 1.3 - Install some Python's librairies

Foodlik uses some third-party Python's librairie.

**Note:** You should set a new virtual environment before installing.

* ```pip install terminaltables```. Allow you to display console tables.

**Optionnal:** ```pip install pytest```. For those who want to run the tests.

## II - Quickstart

1. Install python 3.6 and PostgreSQL or MySQL.
1. Create a new virtual environment and install the required modules (```pip install -r requirements.txt``` will install all required packages).
1. Launch the chosen server. You can save you ID and password using environnment variables.
1. Open your favorite SHELL at the root of the folder.
1. Type ```python main.py --mysql create_database``` and wait few minutes.
1. Type ```python main.py --mysql```.
1. Enjoy.

## III - Structure

### 3.1 - User Interface

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

### 3.2 - DATAS

Les données de ce programme viennent toutes de l'API OpenFoodFact.
Les premières données sont les catégories, au nombre de 234 :

* liste
* des
* catégories

vient ensuite les produits, au nombre de **nombre**.
Chaque produit possède :

* a name (title)
* a description
* some stores
* some categories
* an url to the OpenFoodFact page

 >**NOTE** : the substituts are dynamically generated.

#### 3.2.1 - Filters

Les produits ont été filtrés. Ont été mis de côté :

* ceux qui n'appartenaient pas aux catégories retenues
* ceux qui ne possédaient pas de nutri-score
* les produits doublons (un produit au nom similaire a déjà été ajouté)

#### 3.2.2 - Substituts

Les substituts suivent deux algorithmes, qui retournent chacun un produit de substitution.
Le premier va chercher un produit avec un meilleur score dans la catégorie la moins fournie du produit ciblé.
Le deuxième va chercher un produit avec un bien meilleur score dans la 2eme ou 3eme catégorie la moins fournie du produit ciblé.

## IV - Options

The UI has several options that have passed since the SHELL.

### 4.1 - Update the database

**Note:** The update is done slowly. Do not be presced.

* Type ```python main.py --load_pages```. This option retrieve data from the OpenFoodFact site.

>**Note:** You can also specify the desired page number by typing ```python main.py --load_pages 1-5```. The pattern is as follows: ```main.py (--load_pages | -l) [<first_page>[-<last_page>]]```

* The data was stored in a json file. Let's go to the Data-base : ```python main.py --create_database```. This will delete and recreate the database foodlik, and add all json datas inside.

## V - FAQ

>```could not connect to server: Connection refused``` When i launch the application.

* Be sure the PostgreSQL / MySQL server is running.

>```ERROR:  database "database_name" is being accessed by other users``` When i launch the application.

* Disconnect your pgAdmin connection. An way to solve it is to restarts the server.