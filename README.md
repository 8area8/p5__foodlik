# Foodlik, an API for good people

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

>**NOTE :** enlarge the window of your SHELL for an optimal result

The application has a large portion of French food listed on OpenFoodFact. It repeats these foods, displays their information and generates substitute foods with a higher nutri-score.

Scrum project made with [Trello](https://trello.com):
[![trello image](https://i.imgur.com/J1aDoxD.jpg "TRELLO's link")](https://trello.com/b/6xV0TMFR/p5-foodlik)

## I - Installation

This UI need some other programs to work well.

### 1.1 - Install Python

Foodlik is based on python, an elegant coding langage.
Get the last Python's version at the [following link](https://www.python.org/).
Be sure you got the 3.6 version (or newer).
Check for "pip" and for the root integration during the installation.

### 1.2 - Install the database

Curently, Foodlik support PostgreSQL and MySQL.

PostgreSQL installation : [follow the link](https://www.postgresql.org/).
MySQL installation : [follow the link](https://www.mysql.com/). Install the MySQL GPL version.

#### 1.2.1 - ID, password and environnment variables

You can create a new file and write your ID and password database.
Create an ```app_env``` file at the root of the project.
insert in:

```bash
export POSTGRES_USER="your_id"
export POSTGRES_PASSWORD="your_password"

export MYSQL_USER="your_id"
export MYSQL_PASSWORD="your_password"
```

Replacing the identifiers and passwords with yours.
Then start the file in your console (```source app_env``` or ```. app_env```).
Environment variables will be loaded at each application launch,
which will save you from having to retype your username and password.

The name "app_env" is automatically ignored by Git.
I advise to enter users who have all access to avoid unpleasant surprises ("postgres" for PostgreSQL and "root" for MySQL).

### 1.3 - Install some Python's librairies

Foodlik uses some third-party Python's librairie.

**Note:** You should set a [new virtual environment](http://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html) before installing.

* ```pip install psycopg2```. Only if you want to use PostgreSQL.
* ```pip install mysql-connector```. Only if you want to use MySQL.
* ```pip install docopt```. Allow you to write a good Shell parser.
* ```pip install prompt-toolkit```. Allow you to use auto-completion.
* ```pip install requests```. Allow you to use the requests easily.
* ```pip install termcolor```. Allow you to display colored texts.

## II - Quickstart

1. Install python 3.6 and PostgreSQL or MySQL.
1. Create a new virtual environment and install the required modules (```pip install -r requirements.txt``` will install all required packages).
1. Launch the chosen server. You can save you ID and password using environnment variables.
1. Open your favorite SHELL at the root of the folder.
1. Type ```python main.py --psql create_database``` and wait few minutes.
1. Type ```python main.py --psql```.
1. Enjoy.

>**Note :** you can type ```--msql```in place of ```--psql``` if you want to use the MySQL database.

## III - Structure

### 3.1 - User Interface

The user interface has Home and two ways with 3 and 2 sections.

The first way is the product selection and contains:

* the categories
* products of a category
* the selected product

The second way is the substitute view and contains:

* the substitutes list
* the substitute page

each section follows the following pattern:

* A header: displays the title of the section.
* a body: displays the contents of the section.
* a footer: displays the possible commands in the section.

**Exemples :**

![home](https://i.imgur.com/SkVUOlE.png)
![categories](https://i.imgur.com/HrqMEJw.png)
![product](https://i.imgur.com/Bi8lDsj.png)

### 3.2 - DATAS

The data in this program is all from the OpenFoodFact API.
The first data are the categories, numbering 234.

next comes the products (about 18,000 products).
Each product has:

* a name (title)
* a description
* some stores
* some categories
* an url to the OpenFoodFact page
* a nutri-score

then substitutes. They simply link the products (they are products).

#### 3.2.1 - Filters

The products have been filtered. Have been set aside:

* those who did not belong to the categories selected
* those who did not have a nutri-score
* duplicate products (a product with a similar name has already been added)

#### 3.2.2 - Substituts

Substitutes follow two algorithms, each of which returns a substitution product.

* The first will look for a product with a better score in the current category.
* The second will look for a product with a higher score in the lowest category of the targeted product (the result is generally more accurate).

## IV - Options

The UI has several options that have passed since the SHELL.

### 4.1 - Load the datas

**Note :** The update is done slowly. Do not be presced.

* Type ```python main.py --load_pages```. This option retrieve data from the OpenFoodFact site.

>**Note :** You can also specify the desired page number by typing ```python main.py --load_pages 1-5```. The pattern is as follows: ```main.py (--load_pages | -l) [<first_page>[-<last_page>]]```

### 4.2 - (Re)create the database

* The data are stored in a json file. Let's go to the Data-base : ```python main.py --create_database```. This will delete and recreate the database foodlik, and add all json datas inside.

>**Note :** Recreate the MySQL database is fifteen times longer than the PosteSQL database. It's due to their respective python module

### 4.3 - the mix of both

* Type ```python main.py --psql --full_install``` to use the mix of the two previous methods.

>**Note :** don't forget you can replace ```--msql``` by ```--psql```.

## V - FAQ

>```could not connect to server: Connection refused``` When i launch the application.

* Be sure the PostgreSQL / MySQL server is running.

>```ERROR:  database "database_name" is being accessed by other users``` When i launch the application.

* Disconnect your pgAdmin connection. A way to solve it is to restarts the server.