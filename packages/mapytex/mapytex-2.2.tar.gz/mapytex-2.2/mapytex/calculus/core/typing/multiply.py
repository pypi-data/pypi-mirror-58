#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 lafrite <lafrite@Poivre>
#
# Distributed under terms of the MIT license.

"""
Multiply MO with typing
"""

from multipledispatch import Dispatcher
from ..tree import Tree
from ..MO import MO, MOnumber, MOstr
from ..MO.fraction import MOFraction
from ..MO.monomial import MOstrPower, MOMonomial
from ..compute.filters import special_case

multiply_doc = """ Multiply MOs

:param left: left MO
:param right: right MO
:returns: MO

"""

multiply = Dispatcher("multiply", doc=multiply_doc)


def multiply_filter(left, right):
    """ Automatic multiply on MO

    :param left: MO
    :param right: MO
    :returns: MO if it is a special case, nothing other wise
    """
    try:
        if left == 0:
            return left
    except TypeError:
        pass
    try:
        if right == 0:
            return right
    except TypeError:
        pass

    try:
        if left == 1:
            return right
    except TypeError:
        pass
    try:
        if right == 1:
            return left
    except TypeError:
        pass


@multiply.register((MOnumber, MOFraction), MOstr)
@special_case(multiply_filter)
def moscalar_mostr(left, right):
    """ Multiply a scalar with a letter to create a MOMonomial

    >>> a = MOnumber(2)
    >>> b = MOstr('x')
    >>> multiply(a, b)
    <MOMonomial 2x>
    >>> a = MOFraction(1, 5)
    >>> multiply(a, b)
    <MOMonomial 1 / 5 * x>
    """
    return MOMonomial(left, right)


@multiply.register(MOstr, (MOnumber, MOFraction))
@special_case(multiply_filter)
def mostr_moscalar(left, right):
    """ Multiply a scalar with a letter to create a MOMonomial

    >>> a = MOstr('x')
    >>> b = MOnumber(2)
    >>> multiply(a, b)
    <MOMonomial 2x>
    >>> b = MOFraction(1, 5)
    >>> multiply(a, b)
    <MOMonomial 1 / 5 * x>
    """
    return MOMonomial(right, left)


@multiply.register((MOnumber, MOFraction), MOstrPower)
@special_case(multiply_filter)
def moscalar_mostrpower(left, right):
    """ Multiply a scalar with a MOstrPower

    >>> a = MOnumber(4)
    >>> x = MOstrPower('x', 4)
    >>> multiply(a, x)
    <MOMonomial 4x^4>
    >>> a = MOnumber(1)
    >>> x = MOstrPower('x', 4)
    >>> multiply(a, x)
    <MOstrPower x^4>
    """
    # if left == 1:
    #    return right
    return MOMonomial(left, right)


@multiply.register(MOstrPower, (MOnumber, MOFraction))
@special_case(multiply_filter)
def mostrpower_moscalar(left, right):
    """ Multiply a MOstrPower with a scalar

    >>> a = MOnumber(4)
    >>> x = MOstrPower('x', 4)
    >>> multiply(x, a)
    <MOMonomial 4x^4>

    """
    return MOMonomial(right, left)


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
