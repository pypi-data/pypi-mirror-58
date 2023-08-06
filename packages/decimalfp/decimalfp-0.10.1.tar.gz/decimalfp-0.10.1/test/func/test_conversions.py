#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Name:        test_properties
# Purpose:     Test driver for package 'decimalfp' (conversions)
#
# Author:      Michael Amrhein (michael@adrhinum.de)
#
# Copyright:   (c) 2019 Michael Amrhein
# ----------------------------------------------------------------------------
# $Source: test/func/test_conversions.py $
# $Revision: 2019-03-17T21:54:25+01:00 $


"""Test driver for package 'decimalfp' (conversions)."""


from fractions import Fraction
import math

import pytest


@pytest.mark.parametrize("value",
                         ("17.8",
                          ".".join(("1" * 3297, "4" * 33)),
                          "0.00014"),
                         ids=("compact", "large", "fraction"))
def test_true(impl, value):
    dec = impl.Decimal(value)
    assert dec


@pytest.mark.parametrize("value", (None, "0.0000"),
                         ids=("None", "0"))
def test_false(impl, value):
    dec = impl.Decimal(value)
    assert not dec


@pytest.mark.parametrize(("num", "den"),
                         ((170, 10),
                          (9 ** 394, 10 ** 247),
                          (-19, 4000)),
                         ids=("compact", "large", "fraction"))
def test_trunc(impl, num, den):
    f = Fraction(num, den)
    dec = impl.Decimal(f, 250)
    assert int(f) == int(dec)
    assert math.trunc(f) == math.trunc(dec)


@pytest.mark.parametrize(("num", "den"),
                         ((170, 10),
                          (9 ** 394, 10 ** 247),
                          (-19, 4000)),
                         ids=("compact", "large", "fraction"))
def test_floor(impl, num, den):
    f = Fraction(num, den)
    dec = impl.Decimal(f, 250)
    assert math.floor(f) == math.floor(dec)


@pytest.mark.parametrize(("num", "den"),
                         ((170, 10),
                          (9 ** 394, 10 ** 247),
                          (-19, 4000)),
                         ids=("compact", "large", "fraction"))
def test_ceil(impl, num, den):
    f = Fraction(num, den)
    dec = impl.Decimal(f, 250)
    assert math.ceil(f) == math.ceil(dec)


@pytest.mark.parametrize(("num", "den"),
                         ((17, 1),
                          (9 ** 394, 10 ** 247),
                          (-190, 400000)),
                         ids=("compact", "large", "fraction"))
def test_to_float(impl, num, den):
    f = Fraction(num, den)
    dec = impl.Decimal(f, 250)
    assert float(f) == float(dec)


@pytest.mark.parametrize("sign", (0, 1), ids=("+", "-"))
@pytest.mark.parametrize("coeff", (178, 9 ** 378), ids=("small", "large"))
@pytest.mark.parametrize("exp", (0, -54, 23), ids=("0", "neg", "pos"))
def test_as_tuple(impl, sign, coeff, exp):
    s = f"{'-' * sign}{coeff}e{exp}"
    dec = impl.Decimal(s)
    assert dec.as_tuple() == (sign, coeff * 10 ** max(0, exp), min(exp, 0))


@pytest.mark.parametrize(("num", "den"),
                         ((17, 1),
                          (9 ** 394, 10 ** 247),
                          (190, 400000)),
                         ids=("compact", "large", "fraction"))
def test_as_integer_ratio(impl, num, den):
    f = Fraction(num, den)
    dec = impl.Decimal(f, 250)
    assert dec.as_integer_ratio() == (f.numerator, f.denominator)


@pytest.mark.parametrize(("value", "prec", "str_"),
                         ((None, None, "0"),
                          (None, 2, "0.00"),
                          ("-20.7e-3", 5, "-0.02070"),
                          ("0.0000000000207", None, "0.0000000000207"),
                          (887 * 10 ** 14, 0, "887" + "0" * 14)))
def test_str(impl, value, prec, str_):
    dec = impl.Decimal(value, prec)
    assert str(dec) == str_


@pytest.mark.parametrize(("value", "prec", "repr_"),
                         ((None, None, "Decimal(0)"),
                          (None, 2, "Decimal(0, 2)"),
                          ("15", 2, "Decimal(15, 2)"),
                          ("15.4", 2, "Decimal('15.4', 2)"),
                          ("-20.7e-3", 5, "Decimal('-0.0207', 5)"),
                          ("0.0000000000207", None,
                           "Decimal('0.0000000000207')"),
                          (887 * 10 ** 14, 0,
                           "Decimal(887" + "0" * 14 + ")")))
def test_repr(impl, value, prec, repr_):
    dec = impl.Decimal(value, prec)
    assert repr(dec) == repr_
