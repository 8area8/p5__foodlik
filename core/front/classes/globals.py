#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Globals functions."""

from prompt_toolkit.completion import WordCompleter
from termcolor import colored

from core.back.database.data_wrapper import datas_wrapper as datas


def shell_repr(self):
    """Return a Command Line Interface representation."""
    return self.header + ("\n" * 2) + self.content + "\n" + self.footer


class BaseSection():
    """Abstract base for every sections.

    Child classes must contain:
        - self.header
        - self.content
        - self.footer

    These objects can be a string or a property (that returns a string).
    """

    def __init__(self):
        """Initialize the class."""
        self.change_to = ""

        self.comm = "COMMANDES:\n"
        self.c_quit = "[quitter] or [q]: quitter l'application.\n"
        self.c_return_ctgs = "[retour cat]: retourne à la page catégories.\n"
        self.c_return_title = "[retour titre]: retour à l'écran titre.\n"

        self.a_nextbef = ["suivant", "s", "avant", "a"]
        self.a_return_ctgs = ["retour cat"]
        self.a_return_title = ["retour titre"]

        self.action_error = {"text": "", "active": False}

    @property
    def auto_completion(self):
        """Return a list of keys from self.actions for auto-completion.

        This method uses the 'prompt_toolkit' library.
        """
        return WordCompleter(self.actions)

    @property
    def footer(self):
        """Define the footer.

        This footer catches error messages and returns them for child classes.
        """
        if self.action_error["active"]:
            self.action_error["active"] = False
            return colored(self.action_error["text"], "red")
        return ""

    @property
    def actions(self):
        """Return the possible actions.

        NOTE: follow this pattern to use autocompletion properly:
            - each action must be a 'keyboard key' or a word
            - each action must be sperrated by ", "
            - the keyboard keys should be written as follows: key_name keyword
            - the words should be written as follows: 'word_name'
        """
        return ['q', 'quitter']

    def apply(self, action):
        """Apply an action."""
        raise NotImplementedError

    def add_action_error(self, action):
        """Return an error text."""
        error = (f"L'action '{action}' n'est pas une action valide.\n")
        self.action_error["text"] = error
        self.action_error["active"] = True

    def close_connection(self):
        """Close the database connection."""
        return datas.close()


BaseSection.__str__ = shell_repr  # monkey patching.
#                   __
#                  / _,\
#                  \_\
#       ,,,,    _,_)  #      /)
#      (= =)D__/    __/     //
#     C/^__)/     _(    ___//
#       \_,/  -.   '-._/,--'
# _\\_,  /           -//.
#  \_ \_/  -,._ _     ) )
#    \/    /    )    / /
#    \-__,/    (    ( (
#               \.__,-)\_
#                )\_ / -(
#               / -(////
#              ////
