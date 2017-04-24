# -*- coding: utf-8 -*-

class ChineseRemainderConstructor:
    def __init__(self, bases):
        """Accepts a list of two integer bases."""
        self.bases = bases

    def rem(self, mods):
        """Accepts a list of corresponding modulos for the bases and
        returns the accumulated modulo.
        """
