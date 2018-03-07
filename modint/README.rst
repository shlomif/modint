===============================
ModInt
===============================


.. image:: https://img.shields.io/pypi/v/modint.svg
        :target: https://pypi.python.org/pypi/modint

.. image:: https://img.shields.io/travis/shlomif/modint.svg
        :target: https://travis-ci.org/shlomif/modint

.. image:: https://readthedocs.org/projects/modint/badge/?version=latest
        :target: https://modint.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/shlomif/modint/shield.svg
     :target: https://pyup.io/repos/github/shlomif/modint/
     :alt: Updates


Python implementation of the Chinese Remainder algorithm


* Free software: MIT license
* Documentation: https://modint.readthedocs.io.


Features
--------

A usable implementation of the Chinese Remainder algorithm (see
https://en.wikipedia.org/wiki/Chinese_remainder_theorem ) under the permissive
MIT/Expat licence. Written because none other similarly-licensed ones
could be found.

What this does is given two-or-more pairwise coprime bases integers and their
corresponding moduli, it finds an integer that yields these moduli for all the
bases.

Example
-------

Here is an example::

    from modint import ChineseRemainderConstructor, chinese_remainder

    cr = ChineseRemainderConstructor([2, 5])
    # Because 5 % 2 == 1 and 5 % 5 == 0
    assert cr.rem([1, 0]) == 5
    # Because 8 % 2 == 0 and 8 % 5 == 3
    assert cr.rem([0, 3]) == 8

    # Convenience function
    assert chinese_remainder([2, 3, 7], [1, 2, 3]) == 17

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

