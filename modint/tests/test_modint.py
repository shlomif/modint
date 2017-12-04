#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_modint
----------------------------------

Tests for `modint` module.
"""

import pytest

from modint import ChineseRemainderConstructor


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_modint():
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    cr = ChineseRemainderConstructor([3, 5])
    assert cr.rem([1, 1]) == 1

    cr = ChineseRemainderConstructor([2, 5])
    assert cr.rem([1, 0]) == 5
