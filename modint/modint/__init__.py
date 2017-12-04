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
        ret = 0
        for base, inv, mod in zip(self._bases, self._inverses, mods):
            ret += mod * inv * self.mul_inv(inv, base)
        return ret % self._prod

    def mul_inv(self, a, b):
        """Internal method that implements Euclid's modified gcd algorithm.
        """
        initial_b = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            div, mod = divmod(a, b)
            a, b = b, mod
            x0, x1 = x1 - div * x0, x0
        return (x1 if x1 >= 0 else x1 + initial_b)
