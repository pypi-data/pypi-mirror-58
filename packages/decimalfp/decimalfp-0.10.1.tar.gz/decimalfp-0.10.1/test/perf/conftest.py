# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Name:        conftest
# Purpose:     Shared pytest fixtures (for performance tests)
#
# Author:      Michael Amrhein (michael@adrhinum.de)
#
# Copyright:   (c) 2019 Michael Amrhein
# License:     This program is part of a larger application. For license
#              details please read the file LICENSE.TXT provided together
#              with the application.
# ----------------------------------------------------------------------------
# $Source: test/perf/conftest.py $
# $Revision: 2019-04-08T18:08:34+02:00 $


"""Shared pytest fixtures (for performance tests)."""


# standard library imports

from collections import namedtuple
from importlib import import_module

# third-party imports

import pytest


@pytest.fixture(scope="session",
                params=("decimal", "decimalfp._pydecimalfp",
                        "decimalfp._cdecimalfp"),
                ids=("stdlib", "pydec", "cydec"))
def impl(request):
    """Return Decimal implementation."""
    mod = import_module(request.param)
    return mod


StrVals = namedtuple('StrVals', "compact, small, large")
str_vals = StrVals("+17.4",
                   "-1234567890.12345678901234567890",
                   "9" * 294 + "." + "183" * 81)


@pytest.fixture(scope="session",
                params=str_vals,
                ids=str_vals._fields)
def str_value(request):
    return request.param


@pytest.fixture(scope="session")
def dec_value(impl, str_value):
    return impl.Decimal(str_value)
