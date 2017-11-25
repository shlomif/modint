# -*- coding: utf-8 -*-

__author__ = """Shlomi Fish"""
__email__ = 'shlomif@shlomifish.org'
__version__ = '0.1.0'

class ChineseRemainderConstructor:
    def __init__(self, bases):
        """Accepts a list of two integer bases."""
        self._bases = bases
        p = 1
        for x in bases:
            p *= x
        self._prod = p
        self._inverses = [p//x for x in bases]

    def rem(self, mods):
        """Accepts a list of corresponding modulos for the bases and
        returns the accumulated modulo.
        """
        return 1
