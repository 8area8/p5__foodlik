#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Connect to the database for queries."""

from os import listdir
from pathlib import Path
import getpass
import json

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def init():
    """Initialize the database creation."""
    user = input("PostgreSQL user:")
    pwd = getpass.getpass("PostgreSQL password:")

    _create_foodlik(user, pwd)

    conn = psycopg2.connect(dbname="foodlik", user=user,
                            host="localhost", password=pwd)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    _create_structure(user, pwd, cur)
    _fill_in_database(cur)

    cur.close()
    conn.close()


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
    """Full in top 'foodlik' of datas."""
    datas_path = Path().resolve() / "core" / "back" / "requests"
    datas_path = datas_path / "datas"

    cat_fr = str(datas_path / "categories_fr.json")
    with open(cat_fr, "r", encoding="utf8") as file:
        categories = json.load(file)
    for name in categories:
        cursor.execute(f"""INSERT INTO category (title) VALUES ("{name}")""")
    print("Categories done.")

    for file in listdir(datas_path / "products"):
        with open(file, "r", encoding='utf8') as file:
            datas = json.load(file)

        for product in datas:
            name = product["name"]
            descr = product["description"]
            stores = product["stores"]
            url = product["site_url"]
            score = product["score"]
            cursor.execute("INSERT INTO product (title, description, "
                           "stores, site_url, score) VALUES "
                           f"""("{name}", "{descr}", "{stores}","""
                           f""" "{url}", {score})""")

            for ctg in product["categories"]:
                cursor.execute("INSERT INTO category_per_product "
                               "(category_title, product_title) "
                               f"""VALUES ("{ctg}", "{name}")""")
