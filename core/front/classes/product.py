#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""The Product section."""

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas
import textwrap


class Product(BaseSection):
    """The product class."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.name = datas.chosen_product.upper()

        self.c_return_prd = "[retour prod]: retourne à la page produits.\n"
        self.c_save_substitut1 = ("[sauve premier]: sauvegarde le premier"
                                  "substitut.\n")
        self.c_save_substitut2 = ("[sauve second]: sauvegarde le second "
                                  "substitut.\n")
        self.info_msg = ""
        self.substituts = None

    @property
    def header(self):
        """Return the header informations."""
        title = f"   {self.name}"
        return colored(title, "yellow") + "\n" + "   " + "-" * 23

    @property
    def content(self):
        """Return the content."""
        content = datas.load_product()
        self.substituts = datas.load_product_substitutes(content[4],
                                                         content[0])
        text = ""
        titles = ["nom: ", "description: ",
                  "magasins ", "url: ", "nutri-score: "]

        for title, infos in zip(titles, content):
            infos = textwrap.wrap(str(infos), 45)
            infos = "\n     ".join(infos)
            text += ("   * " + colored(title, "yellow") + infos + " \n")

        text += colored("\n\n   SUBSTITUTS TROUVES\n", "green")
        text += "   " + "-" * 23 + "\n\n"
        subst = "   PREMIER SUBSTITUT, DANS LA CATEGORIE COURANTE:\n"
        text += colored(subst, "green")

        titles.insert(3, "catégorie: ")
        for product in self.substituts[0]:
            for title, caract in zip(titles, product):
                caract = textwrap.wrap(str(caract), 45)
                caract = "\n     ".join(caract)
                text += "   * " + colored(title, "green") + caract + "\n"
            text += "\n\n   "
            subst = "SECOND SUBSTITUT, DANS UNE CATEGORIE PLUS CIBLEE:\n"
            text += colored(subst, "green")

        if isinstance(self.substituts[1], str):
            text += "   * " + self.substituts[1] + "\n"
            return text

        for product in self.substituts[1]:
            for title, caract in zip(titles, product):
                caract = textwrap.wrap(str(caract), 45)
                caract = "\n     ".join(caract)
                text += "   * " + colored(title, "green") + caract + "\n"
        return text

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        text = (self.comm + self.c_return_prd + self.c_return_ctgs +
                self.c_quit + self.c_save_substitut1 +
                self.c_return_title +
                self.c_save_substitut2 + "\n" +
                self.info_msg + "\n") + super().footer
        self.info_msg = ""
        return text

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        return (self.a_return_ctgs +
                ["retour prod", "sauve premier", "sauve second"] +
                self.a_return_title +
                super().actions)

    def apply(self, action):
        """Apply an action."""
        if action == "retour cat":
            self.change_to = "Categories"
        if action == "retour prod":
            self.change_to = "Category"
        if action == "sauve premier" and isinstance(self.substituts, tuple):
            self.info_msg = datas.save_substitute(self.substituts[0][0])
        if action == "sauve second" and isinstance(self.substituts, tuple):
            self.info_msg = datas.save_substitute(self.substituts[1][0])
        if action == "retour titre":
            self.change_to = "TitleScreen"
