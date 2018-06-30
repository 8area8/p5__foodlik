#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Create the food datas from the OpenFoodFact API.

Usage:
    datas_requests.py (-f | --filter_datas)
    datas_requests.py (-c | --create_file)
    datas_requests.py (-h | --help)
    datas_requests.py --version

Options:
    -h --help           Show this screen.
    --version           Show version.
    -c --create_file    Create a new datas file.
    -f --filter_datas   Filter the datas and write them in datas.json.

"""
import json

import requests
from docopt import docopt


def main():
    """Core function."""
    arguments = docopt(__doc__, version='0.1')
    print(arguments)

    if arguments["--create_file"]:
        _create_file()


def _create_file(truc=True):
    """Create or overwrite the datas file."""
    # page_max?
    # pour chaque page jusqu'à page_max
    base_url = ("https://world.openfoodfacts.org/cgi/search.pl?"
                "action=process&tagtype_0=categories&tagtype_1=countries"
                "&tag_contains_1=france&page_size=1000&json=1")
    max_size = 562 + 1
    mode = "w"

    for i in range(1, 3):
        url = base_url + f"&page={i}"
        resp = requests.get(url)

        if truc:
            datas = _filtered_datas(resp.json())
            file_name = "datas.json"
        else:
            datas = resp.json()
            file_name = "test.json"

        with open(file_name, mode, encoding='utf8') as f:
            json.dump(datas, f, indent=4, ensure_ascii=False)

        print(f"page {i} done.")
        mode = "a"


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
            "categories": [x[3:] for x in categories if x[:2] == "fr"],
            "stores": stores,
            "site_url": product.get("url", None),
            "score": int(product["nutriments"].get("nutrition-score-fr", 100))
        }
        if not product["categories"] or not product["score"]:
            continue
        filtered.append(product)
    return filtered


if __name__ == "__main__":
    main()
