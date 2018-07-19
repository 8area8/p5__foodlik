#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Load the categories from OpenFoodFact.

NOTE: this script does not allow to have categories that
correspond to each other. Read 'NOTE.txt' from the 'requests' folder.

For this reason, the files created by this script will not replace
the base category files.
"""


import json
import unicodedata as unic
import requests


def init(max_categories=400):
    """Launch the script."""
    print("Wait few minutes...")
    url_fr = "https://fr.openfoodfacts.org/categories.json"
    url_en = "https://world.openfoodfacts.org/categories.json"
    urls = (url_fr, url_en)
    langages = ["fr", "en"]

    for url in urls:
        resp = requests.get(url)

        datas = filtered_categories(resp.json(), max_categories)
        file_path = f"datas/_categories_{langages.pop(0)}.json"

        with open(file_path, "w", encoding='utf8') as file:
            json.dump(datas, file, indent=4, ensure_ascii=False)

    print("categories loaded.")


def filtered_categories(datas, max_categories):
    """Filter the datas and return a list of categories."""
    datas = datas["tags"]
    categories = []

    try:
        datas[max_categories]
    except IndexError:
        max_categories = 400

    for index in range(0, max_categories):
        name = datas[index]["name"]
        if not name or ":" in name:
            continue
        if not only_roman_chars(name):
            continue

        name = name.replace("-", " ").replace("'", " ")
        categories.append(name)

    return categories


def is_latin(uchr):  # https://stackoverflow.com/questions/3094498
    """Return True if "uchr" is a latin letter."""
    latin_letters = {}
    try:
        return latin_letters[uchr]
    except KeyError:
        return latin_letters.setdefault(uchr, 'LATIN' in unic.name(uchr))


def only_roman_chars(unistr):
    """Return True if "unistr" only contains latin letters."""
    return all(is_latin(uchr)
               for uchr in unistr
               if uchr.isalpha())  # isalpha suggested by John Machin


if __name__ == "__main__":
    init()
