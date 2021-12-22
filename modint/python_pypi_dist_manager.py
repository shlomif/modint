#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.

from pydistman import DistManager


class Derived(DistManager):
    """docstring for Derived"""
    pass


dist_name = "modint"

obj = Derived(
    dist_name=dist_name,
    dist_version="0.4.0",
    project_name="modint",
    project_short_description=(
        "Python implementation of the "
        "Chinese Remainder algorithm"
    ),
    release_date="2021-11-26",
    project_year="2018",
    aur_email="shlomif@cpan.org",
    project_email="shlomif@cpan.org",
    full_name="Shlomi Fish",
    github_username="shlomif",
    filter_test_reqs=True,
)
obj.cli_run()
