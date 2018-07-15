#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Connect to the database for queries."""

from os import listdir
from pathlib import Path
import json

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import core.passwords as db_connect


def init():
    """Initialize the database creation."""
    user = db_connect.DB_USER
    pwd = db_connect.DB_PASSWORD
    print("Wait few minutes...")

    _create_foodlik(user, pwd)

    conn = psycopg2.connect(dbname="foodlik", user=user,
                            host="localhost", password=pwd)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    _create_structure(user, pwd, cur)
    _fill_in_database(cur)

    cur.close()
    conn.close()
    print("database ready for use.")


def _create_foodlik(user, pwd):
    """Create the foodlik database."""
    conn = psycopg2.connect(dbname="postgres", user=user,
                            host="localhost", password=pwd)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(f"ALTER USER {user} CREATEDB;")
    cur.execute("DROP DATABASE IF EXISTS foodlik")
    cur.execute("CREATE DATABASE foodlik")
    cur.close()
    conn.close()
    print("database created.")


def _create_structure(user, pwd, cursor):
    """Create the database structure."""
    path = str(Path().resolve() / "core" / "back" / "database")

    cursor.execute(open(path + "/structure.sql", "r").read())


def _fill_in_database(cursor):
    """Fill in 'foodlik' of datas."""
    datas_path = Path().resolve() / "core" / "back" / "requests"
    datas_path = datas_path / "datas"
    _fill_in_categories(datas_path, cursor)
    _fill_in_products(datas_path, cursor)
    _fill_in_products_number(datas_path, cursor)


def _fill_in_categories(datas_path, cursor):
    """Fill in database of categories."""
    cat_fr = str(datas_path / "categories_fr.json")
    with open(cat_fr, "r", encoding="utf8") as file:
        categories = json.load(file)
    for name in categories:
        cursor.execute(f"INSERT INTO category (title) VALUES ('{name}')")
    print("Categories done.")


def _fill_in_products(datas_path, cursor):
    """Fill in database of products."""
    prod_path = datas_path / "products"
    for index, file in enumerate(listdir(prod_path)):
        with open(str(prod_path / file), "r", encoding='utf8') as product_file:
            datas = json.load(product_file)

        for product in datas:
            _insert_product(product, cursor)
            name = product["name"]

            for ctg in set(product["categories"]):  # lazy set, sorry. :p
                _insert_categorie_per_product(ctg, name, cursor)
        print(f"file {index + 1} done.")


def _insert_product(product, cursor):
    """Insert a product into the database."""
    name = product["name"]
    descr = product["description"]
    stores = product["stores"]
    url = product["site_url"]
    score = product["score"]
    cursor.execute("INSERT INTO product (title, description, "
                   "stores, site_url, score) VALUES "
                   f"('{name}', '{descr}', '{stores}',"
                   f" '{url}', '{score}')")


def _insert_categorie_per_product(ctg, name, cursor):
    """Insert all categories of a product."""
    cursor.execute("INSERT INTO category_per_product "
                   "(category_title, product_title) "
                   f"VALUES ('{ctg}', '{name}')")


def _fill_in_products_number(datas_path, cursor):
    """Insert the products number of each category.

    Remove lines that do not contain products.
    """
    cursor.execute("SELECT title FROM CATEGORY")
    result = [wrd[0] for wrd in cursor.fetchall() if wrd[0]]
    for category in result:
        cursor.execute("UPDATE CATEGORY "
                       "SET product_number = subquery.count "
                       "FROM (SELECT COUNT(*) "
                       "FROM CATEGORY_PER_PRODUCT AS CPP "
                       f"WHERE CPP.category_title='{category}') AS subquery "
                       f"WHERE CATEGORY.title = '{category}'")

    cursor.execute("DELETE FROM CATEGORY "
                   "WHERE product_number = 0")
