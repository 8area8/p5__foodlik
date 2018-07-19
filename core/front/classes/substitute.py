#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Contain the Substitute section."""

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas
from textwrap import wrap


class Substitute(BaseSection):
    """The substitute class."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.name = datas.chosen_product.upper()

        self.c_return_sub = "[return sub]: return to substitutes page."

    @property
    def header(self):
        """Return the header informations."""
        title = f"   {self.name}"
        return colored(title, "yellow") + "\n" + "   " + "-" * 23

    @property
    def content(self):
        """Return the content."""
        content = datas.load_substitute_page()
        text = colored("    SUBSTITUTE:\n", "green")
        for caract in content[0]:
            caract = "\n      ".join(wrap(str(caract), 45))
            text += "    * " + caract + "\n"
        text += colored("\n    PRODUCTS SUBSTITUTED:\n", "green")
        for product in content[1]:
            product = "\n     ".join(wrap(str(product[0]), 45))
            text += "    * " + product + "\n"
        return text + "\n"

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        return (self.comm + self.c_return_sub +
                self.c_quit + "\n") + super().footer

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        return (["return sub"] + super().actions)

    def apply(self, action):
        """Apply an action."""
        if action == "return sub":
            self.change_to = "Substitutes"
