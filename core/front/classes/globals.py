#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Globals functions."""


def section_repr(self):
    """Return a CLI representation."""
    return self.header + "\n" + self.content + "\n" + self.footer


class BaseSection():
    """Abstract base for every sections."""

    def __init__(self, str_function=section_repr):
        """Initialize the class."""
        self.__str__ = str_function

    def actions(self):
        """Return the possible actions."""
        raise NotImplementedError