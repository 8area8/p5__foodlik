#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Connect to the database for queries."""

from os import listdir
from pathlib import Path
import json

from core.back.database.databases_wrapper import database_wrapper as database


def init():
    """Initialize the database creation."""
    print("Wait few minutes...")

    _create_foodlik()

    database.connect()

    _create_structure()
    _fill_in_database()

    database.close()
    print("database ready for use.")


def _create_foodlik():
    """Create the foodlik database."""
    database.connect("root")

    database.execute("DROP DATABASE IF EXISTS foodlik")
    database.execute("CREATE DATABASE foodlik")
    database.close()
    print("database created.")


def _create_structure():
    """Create the database structure."""
    path = str(Path().resolve() / "core" / "back" / "database")
    database.execute(open(path + "/structure.sql", "r").read(), multi=True)
    print("structure created.")


def _fill_in_database():
    """Fill in 'foodlik' of datas."""
    datas_path = Path().resolve() / "core" / "back" / "requests"
    datas_path = datas_path / "datas"
    _fill_in_categories(datas_path)
    _fill_in_products(datas_path)
    _fill_in_products_number(datas_path)


def _fill_in_categories(datas_path):
    """Fill in database of categories."""
    cat_fr = str(datas_path / "categories_fr.json")
    with open(cat_fr, "r", encoding="utf8") as file:
        categories = json.load(file)
    for name in categories:
        database.execute(f"INSERT INTO category (title) VALUES ('{name}')")
    print("Categories done.")


def _fill_in_products(datas_path):
    """Fill in database of products."""
    prod_path = datas_path / "products"
    for index, file in enumerate(listdir(prod_path)):
        with open(str(prod_path / file), "r", encoding='utf8') as product_file:
            datas = json.load(product_file)

        for product in datas:
            try:
                _insert_product(product)
                name = product["name"]
                for ctg in set(product["categories"]):  # lazy set, sorry. :p
                    _insert_categorie_per_product(ctg, name)

            except Exception as _:
                pass

        print(f"file {index + 1} done.")


def _insert_product(product):
    """Insert a product into the database."""
    name = product["name"]
    descr = product["description"]
    stores = product["stores"]
    url = product["site_url"]
    score = product["score"]
    database.execute("INSERT INTO product (title, description, "
                     "stores, site_url, score) VALUES "
                     f"('{name}', '{descr}', '{stores}',"
                     f" '{url}', '{score}')")


def _insert_categorie_per_product(ctg, name):
    """Insert all categories of a product."""
    database.execute("INSERT INTO category_per_product "
                     "(category_title, product_title) "
                     f"VALUES ('{ctg}', '{name}')")


def _fill_in_products_number(datas_path):
    """Insert the products number of each category.

    Remove lines that do not contain products.
    """
    database.execute("SELECT title FROM CATEGORY")
    result = [wrd[0] for wrd in database.get_row(True) if wrd[0]]
    for category in result:
        database.execute("SELECT COUNT(*) "
                         "FROM CATEGORY_PER_PRODUCT AS CPP "
                         f"WHERE CPP.category_title='{category}'")
        database.execute("UPDATE CATEGORY "
                         f"SET product_number = {database.get_row()[0]} "
                         f"WHERE CATEGORY.title = '{category}'")

    database.execute("DELETE FROM CATEGORY "
                     "WHERE product_number = 0")
