#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Load the categories from OpenFoodFact."""


import requests
import json
import unicodedata as unic


def init(max_categories=4000):
    """Launch the script."""
    url = "https://fr.openfoodfacts.org/categories.json"
    resp = requests.get(url)

    datas = filtered_categories(resp.json(), max_categories)
    file_path = "datas/categories.json"

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
        max_categories = len(datas)

    for index in range(0, len(datas)):
        name = datas[index]["name"]
        if not name or ":" in name:
            continue
        if not only_roman_chars(name):
            continue

        categories.append(name)

    categories.sort()
    return categories


def is_latin(uchr):
    """Return True if "uchr" is a latin letter."""
    latin_letters = {}
    try:
        return latin_letters[uchr]
    except KeyError:
        return latin_letters.setdefault(uchr, 'LATIN' in unic.name(uchr))


def only_roman_chars(unistr):
    """Return True if "uchr" contains only latin letters."""
    return all(is_latin(uchr)
               for uchr in unistr
               if uchr.isalpha())  # isalpha suggested by John Machin


if __name__ == "__main__":
    init()
