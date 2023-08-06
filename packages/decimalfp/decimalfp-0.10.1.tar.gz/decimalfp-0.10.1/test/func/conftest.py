# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Name:        conftest
# Purpose:     Shared pytest fixtures
#
# Author:      Michael Amrhein (michael@adrhinum.de)
#
# Copyright:   (c) 2019 Michael Amrhein
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source: test/func/conftest.py $
# $Revision: 2019-03-27T17:51:47+01:00 $


"""Shared pytest fixtures."""


# standard library imports

from importlib import import_module
import os

# third-party imports

import pytest

# local imports


if os.getenv('DECIMALFP_FORCE_PYTHON_IMPL'):
    IMPLS = ("decimalfp._pydecimalfp",)
    IDS = ("pydec",)
else:
    IMPLS = ("decimalfp._pydecimalfp", "decimalfp._cdecimalfp")
    IDS = ("pydec", "cydec")


@pytest.fixture(scope="session",
                params=IMPLS,
                ids=IDS)
def impl(request):
    mod = import_module(request.param)
    return mod
