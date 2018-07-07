#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Load the OpenFoodFact datas page per page."""

import requests
import json
import os
from pathlib import Path


with open("datas/categories_fr.json", encoding='utf-8') as file:
    CATEGORIES_FR = json.load(file)
with open("datas/categories_en.json", encoding='utf-8') as file:
    CATEGORIES_EN = json.load(file)
USED_NAMES = []  # Avoid duplicates.


def init(start=1, end=30):
    """Load the products from OpenFoodFact."""
    try:
        assert 0 < start <= end
    except Exception as error:
        raise error
    _load_pages(start, end + 1)


def _load_pages(start, end):
    """Create or overwrite the datas file."""
    _remove_data_files()
    base_url = ("https://world.openfoodfacts.org/cgi/search.pl?"
                "action=process&tagtype_0=categories&tagtype_1=countries"
                "&tag_contains_1=france&page_size=1000&json=1")

    for index in range(start, end):
        url = base_url + f"&page={index}"
        resp = requests.get(url).json()

        datas = _filtered_datas(resp)
        file_path = f"datas/products/products{index}.json"

        with open(file_path, "w", encoding='utf8') as file:
            json.dump(datas, file, indent=4, ensure_ascii=False)

        print(f"page {index}/{end - 1} done.")


def _remove_data_files():  # https: // stackoverflow.com/questions/185936
    """Remove each file from "products folder."""
    folder = Path().resolve() / "core" / "back"
    folder = folder / "requests" / "datas" / "products"

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as error:
            print(error)


def _filtered_datas(datas):
    """Filter the datas."""
    datas = datas["products"]
    filtered = []

    for product in datas:
        categories = product.get("categories_tags", [])
        stores = product.get("stores", "").split(",")

        product = {
            "name": product.get('product_name', None),
            "description": product.get("generic_name", None),
            "categories": _translate_categories(categories),
            "stores": stores,
            "site_url": product.get("url", None),
            "score": int(product["nutriments"].get("nutrition-score-fr", 100))
        }
        if not product["categories"]:
            continue
        if product["score"] == 100:
            continue
        if product["name"] in USED_NAMES:
            continue

        USED_NAMES.append(product["name"])
        filtered.append(product)
    return filtered


def _translate_categories(categories):
    """Translate the english categories to french."""
    french_categories = []
    for name in categories:
        name = name.replace("-", " ")
        name = name[3:].capitalize()

        if name in CATEGORIES_EN:
            index = CATEGORIES_EN.index(name)
            french_categories.append(CATEGORIES_FR[index])
        elif name in CATEGORIES_FR:
            french_categories.append(name)

    return french_categories


if __name__ == "__main__":
    init()
