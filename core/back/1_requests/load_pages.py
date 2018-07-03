#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Load the OpenFoodFact datas page per page."""

import requests
import json


with open("datas/categories.json") as file:
    CATEGORIES = json.load(file)


def init(start=1, end=2):
    """Load the products from OpenFoodFact."""
    try:
        assert 0 < start <= end
    except Exception as error:
        raise error

    _load_pages(start, end + 1)


def _load_pages(start, end):
    """Create or overwrite the datas file."""
    base_url = ("https://world.openfoodfacts.org/cgi/search.pl?"
                "action=process&tagtype_0=categories&tagtype_1=countries"
                "&tag_contains_1=france&page_size=1000&json=1")
    mode = "w"

    for index in range(start, end):
        url = base_url + f"&page={index}"
        resp = requests.get(url)

        datas = _filtered_datas(resp.json())
        file_path = "datas/products.json"

        with open(file_path, mode, encoding='utf8') as file:
            json.dump(datas, file, indent=4, ensure_ascii=False)

        print(f"page {index}/{end - 1} done.")
        mode = "a"


def _filtered_datas(datas):
    """Filter the datas."""
    datas = datas["products"]
    filtered = []

    for product in datas:
        categories = product.get("categories_tags", [])
        categories = (elem[3:] for elem in categories if elem[:2] == "fr")
        stores = product.get("stores", "").split(",")

        product = {
            "name": product.get('product_name', None),
            "description": product.get("generic_name", None),
            "categories": [elem for elem in categories if elem in CATEGORIES],
            "stores": stores,
            "site_url": product.get("url", None),
            "score": int(product["nutriments"].get("nutrition-score-fr", 100))
        }
        if not product["categories"]:
            continue
        if not product["score"]:
            continue

        filtered.append(product)
    return filtered


if __name__ == "__main__":
    init()
