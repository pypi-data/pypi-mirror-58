#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 lafrite <lafrite@Poivre>
#
# Distributed under terms of the MIT license.

"""
Tokens represents MathObject at API level

"""
from ...core.MO import MO, MOnumber, MOstr, moify
from ...core.MO.fraction import MOFraction
from ...core.MO.monomial import MOstrPower, MOMonomial
from ...core.MO.polynomial import MOpolynomial
from decimal import Decimal as _Decimal
from functools import wraps
from .token import Token

__all__ = ["factory"]


def tokenify(mo, name="", ancestor=None):
    """ Transform a MO or a python builtin to the appropriate token 

    :param mo: the thing to turn into a Token
    :param name: a virtual name of the toke
    :param ancestor: its ancestor

    :example:
    >>> a = MOnumber(2)
    >>> tokenify(a)
    <Integer 2>
    >>> tokenify(2)
    <Integer 2>
    >>> tokenify("x")
    <Linear x>
    >>> tokenify(_Decimal("2.2"))
    <Decimal 2.2>
    >>> tokenify("2.2")
    <Decimal 2.2>
    >>> tokenify(2.2)
    <Decimal 2.20000000000000017763568394002504646778106689453125>

    tokenify is idempotent on "mo" parameter

    >>> a = MOnumber(2)
    >>> ta = tokenify(a)
    >>> ta == tokenify(ta)
    True

    """
    if isinstance(mo, MO):
        return _tokenify(mo, name, ancestor)

    if isinstance(mo, Token):
        if name == "":
            _name = mo.name
        else:
            _name = name
        if ancestor is None:
            _ancestor = mo._ancestor
        else:
            _ancestor = ancestor
        return _tokenify(mo._mo, _name, _ancestor)

    return _tokenify(moify(mo), name, ancestor)


def to_be_token(func):
    """ Decorator to ensure that the return value is a Token """
    @wraps(func)
    def wrapped(*args, **kwds):
        ans = func(*args, **kwds)
        try:
            return [tokenify(t) for t in ans]
        except TypeError:
            return tokenify(ans)
    return wrapped


def _tokenify(mo, name="", ancestor=None):
    """ Transform a MO (from core) to the appropriate token (from API)

    :example:
    >>> a = MOnumber(2)
    >>> _tokenify(a)
    <Integer 2>
    >>> a = MOnumber(2.5)
    >>> _tokenify(a)
    <Decimal 2.5>
    >>> a = MOFraction(2, 5)
    >>> _tokenify(a)
    <Fraction 2 / 5>
    >>> a = MOstr('x')
    >>> _tokenify(a)
    <Linear x>
    >>> a = MOstrPower('x', 2)
    >>> _tokenify(a)
    <Quadratic x^2>
    >>> a = MOstrPower('x', 3)
    >>> _tokenify(a)
    <Polynomial x^3>
    >>> a = MOMonomial(3, 'x', 1)
    >>> _tokenify(a)
    <Linear 3x>
    >>> a = MOMonomial(3, 'x', 2)
    >>> _tokenify(a)
    <Quadratic 3x^2>
    >>> a = MOMonomial(3, 'x', 3)
    >>> _tokenify(a)
    <Polynomial 3x^3>
    """
    if isinstance(mo, MOnumber):
        if isinstance(mo.value, int):
            from .number import Integer

            return Integer.from_mo(mo, name, ancestor)
        elif isinstance(mo.value, _Decimal):
            from .number import Decimal

            return Decimal.from_mo(mo, name, ancestor)

        raise TypeError(f"Can't build from MOnumber ({mo}) neither int nor decimal")

    if isinstance(mo, MOFraction):
        if isinstance(mo._denominator, MOnumber) and isinstance(
            mo._numerator, MOnumber
        ):
            from .number import Fraction

            return Fraction.from_mo(mo, name, ancestor)

        raise TypeError(
            f"Can't build from MOFraction ({mo}) numerator and denominator are not MOnumber"
        )

    if isinstance(mo, (MOstr, MOstrPower, MOMonomial, MOpolynomial)):
        if not isinstance(mo._variable, (MOstr, str)):
            raise TypeError(
                f"Can't build Polynom over something else than a letter (got {mo._variable})"
            )
        if (
            isinstance(mo, MOstr)
            or (isinstance(mo, MOMonomial) and mo.power.value == 1)
            or (isinstance(mo, MOpolynomial) and mo.power.value == 1)
        ):
            from .polynomial import Linear

            return Linear.from_mo(mo, name, ancestor)
        elif (
            (isinstance(mo, MOstrPower) and mo.power.value == 2)
            or (isinstance(mo, MOMonomial) and mo.power.value == 2)
            or (isinstance(mo, MOpolynomial) and mo.power.value == 2)
        ):
            from .polynomial import Quadratic

            return Quadratic.from_mo(mo, name, ancestor)
        else:
            from .polynomial import Polynomial

            return Polynomial.from_mo(mo, name, ancestor)

    raise TypeError(f"{type(mo)} is unknown MathObject")


def factory(exp, name="", ancestor=None):
    """ Transform a Expression with on single MathObject (from core) to a appropriate token (from API)

    :example:
    >>> from ..expression import Expression
    >>> a = Expression(MOnumber(2))
    >>> factory(a)
    <Integer 2>
    >>> a = Expression(MOnumber(2.5))
    >>> factory(a)
    <Decimal 2.5>
    >>> a = Expression(MOFraction(2, 5))
    >>> factory(a)
    <Fraction 2 / 5>
    >>> a = Expression(MOstr('x'))
    >>> factory(a)
    <Linear x>
    >>> a = Expression(MOstrPower('x', 2))
    >>> factory(a)
    <Quadratic x^2>
    >>> a = Expression(MOstrPower('x', 3))
    >>> factory(a)
    <Polynomial x^3>
    >>> a = Expression(MOMonomial(3, 'x', 1))
    >>> factory(a)
    <Linear 3x>
    >>> a = Expression(MOMonomial(3, 'x', 2))
    >>> factory(a)
    <Quadratic 3x^2>
    >>> a = Expression(MOMonomial(3, 'x', 3))
    >>> factory(a)
    <Polynomial 3x^3>
    """
    mo = exp._tree
    if not isinstance(mo, MO):
        raise TypeError(f"Can't build Token from not computed Expression (got {mo})")

    return _tokenify(mo, name, ancestor)


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
