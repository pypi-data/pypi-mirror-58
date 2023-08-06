#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 lafrite <lafrite@Poivre>
#
# Distributed under terms of the MIT license.

"""
Tokens representing polynomials functions 

"""
from ..expression import Expression
from .token import Token
from . import to_be_token
from ...core.MO import MO
from ...core.MO.atoms import moify

__all__ = ["Polynomial", "Quadratic", "Linear"]


class Polynomial(Token):

    """ Token representing a polynomial 

    :examples:
    >>> from ...core.MO.polynomial import MOpolynomial
    >>> P = Polynomial(MOpolynomial('x', [1, 2, 3]))
    >>> P
    <Polynomial 3x^2 + 2x + 1>
    """

    def __init__(self, a, name="", ancestor=None):
        """ Initiate Polynomial with a MO"""
        if not isinstance(a, MO):
            raise TypeError

        Token.__init__(self, a, name, ancestor)
        self._mathtype = "polynome"

    @classmethod
    def from_mo(cls, mo, name="", ancestor=None):

        return cls(mo, name, ancestor)

    @classmethod
    def from_coefficients(cls, coefficients):
        """ Initiate polynomial from list of coefficients """
        pass

    @classmethod
    def random(cls):
        raise NotImplementedError

    @property
    def raw(self):
        raise NotImplementedError("Polynomial does not exists in python")

    def __setitem__(self, key, item):
        """ Use Polynomial like if they were a dictionnary to set coefficients """
        raise NotImplementedError("Can't set coefficient of a polynomial")

    @to_be_token
    def __getitem__(self, key):
        """ Use Polynomial like if they were a dictionnary to get coefficients 

        :examples:
        >>> from ...core.MO.polynomial import MOpolynomial
        >>> P = Polynomial(MOpolynomial('x', [1, 2, 3]))
        >>> P[0]
        <Integer 1>
        >>> P[1]
        <Integer 2>
        >>> P[2]
        <Integer 3>
        >>> P[3]
        Traceback (most recent call last):
            ...
        KeyError: 3
        """
        return self._mo.coefficients[key]

    def __call__(self, value):
        """ Call a Polynomial to evaluate itself on value 

        :examples:
        >>> from ...core.MO.polynomial import MOpolynomial
        >>> P = Polynomial(MOpolynomial('x', [1, 2, 3]))
        >>> for s in P(2).explain():
        ...     print(s)
        3 * 2^2 + 2 * 2 + 1
        3 * 4 + 4 + 1
        12 + 5
        17
        """
        return Expression(self._mo.tree)(value)

    def differentiate(self):
        """ Differentiate a polynome

        :example:
        >>> from ...core.MO.polynomial import MOpolynomial
        >>> P = Polynomial(MOpolynomial('x', [1, 2, 3]))
        >>> P
        <Polynomial 3x^2 + 2x + 1>
        >>> P.differentiate()
        <Linear 6x + 2>
        >>> for s in P.differentiate().explain():
        ...     print(s)
        0 + 2 + 3 * 2x
        2 + 3 * 2 * x
        6x + 2
        """
        return Expression(self._mo.differentiate()).simplify()

    @property
    def roots(self):
        """ Get roots of the Polynomial """
        raise NotImplementedError("Can't compute roots not specific polynomial")


class Linear(Polynomial):

    """ Token representing a linear ax + b

    :examples:
    >>> from ...core.MO.polynomial import MOpolynomial, MOMonomial
    >>> P = Linear(MOpolynomial('x', [1, 2]))
    >>> P
    <Linear 2x + 1>
    >>> P.a
    <Integer 2>
    >>> P.b
    <Integer 1>
    >>> P.differentiate()
    <Integer 2>
    >>> P.roots
    [<Fraction - 2 / 1>]

    """

    def __init__(self, mo, name="", ancestor=None):
        """ Initiate Linear with MO

        :examples:
        >>> from ...core.MO.polynomial import MOpolynomial, MOMonomial
        >>> P = Linear(MOpolynomial('x', [1, 2]))
        >>> P
        <Linear 2x + 1>
        >>> Q = Linear(MOMonomial(3, 'x', 1))
        >>> Q
        <Linear 3x>
        """
        Polynomial.__init__(self, mo, name, ancestor)
        self._mathtype = "affine"

    @classmethod
    def random(cls):
        raise NotImplementedError

    @property
    @to_be_token
    def a(self):
        return self[1]

    @property
    @to_be_token
    def b(self):
        return self[0]

    @property
    @to_be_token
    def roots(self):
        """ Get the root of the polynomial

        :examples:
        >>> from ...core.MO.polynomial import MOpolynomial, MOMonomial
        >>> P = Linear(MOpolynomial('x', [1, 2]))
        >>> P.roots
        [<Fraction - 2 / 1>]
        >>> #P = Linear(MOpolynomial('x', [1, -2]))
        >>> #P.roots
        """

        try:
            return [Expression.from_str(f"-{self.a}/{self.b}").simplify()]
        except AttributeError:
            return [Expression.from_str(f"-{self.a}/{self.b}")]


class Quadratic(Polynomial):

    """ Token representing a quadratic ax^2 + bx + c

    :examples:
    >>> from ...core.MO.polynomial import MOpolynomial
    >>> P = Quadratic(MOpolynomial('x', [1, 2, 3]))
    >>> P
    <Quadratic 3x^2 + 2x + 1>
    >>> P.a
    <Integer 3>
    >>> P.b
    <Integer 2>
    >>> P.c
    <Integer 1>
    >>> P.delta
    <Integer - 8>
    >>> for s in P.delta.explain():
    ...    print(s)
    2^2 - 4 * 3 * 1
    4 - 12 * 1
    4 - 12
    - 8
    >>> P.differentiate()
    <Linear 6x + 2>
    >>> P.roots
    []

    """

    def __init__(self, mo, name="", ancestor=None):
        """ Initiate Quadratic from MO

        >>> from ...core.MO.polynomial import MOpolynomial
        >>> P = Quadratic(MOpolynomial('x', [1, 2, 3]))
        >>> P
        <Quadratic 3x^2 + 2x + 1>
        """

        Polynomial.__init__(self, mo, name, ancestor)
        self._mathtype = "polynome du 2nd degré"

    @classmethod
    def random(cls):
        raise NotImplementedError

    @property
    @to_be_token
    def a(self):
        try:
            return self[2]
        except KeyError:
            return 0

    @property
    @to_be_token
    def b(self):
        try:
            return self[1]
        except KeyError:
            return 0

    @property
    @to_be_token
    def c(self):
        try:
            return self[0]
        except KeyError:
            return 0

    @property
    @to_be_token
    def delta(self):
        return Expression.from_str(f"{self.b}^2-4*{self.a}*{self.c}").simplify()

    @property
    @to_be_token
    def roots(self):
        """ Roots of the polynom

        :example:
        >>> from ...core.MO.polynomial import MOpolynomial
        >>> P = Quadratic(MOpolynomial('x', [1, 0, 1]))
        >>> P.roots
        []
        >>> P = Quadratic(MOpolynomial('x', [4, -4, 1]))
        >>> P.roots
        [<Integer 2>]
        >>> P = Quadratic(MOpolynomial('x', [1, 0, -1]))
        >>> P.roots
        [<Integer - 1>, <Integer 1>]
        """
        if self.delta._mo < 0:
            return []
        elif self.delta._mo == 0:
            # return [Expression.from_str(f"-{self.b}/(2*{self.a})").simplify()]
            return [round(eval(f"-{self.b}/(2*{self.a})"), 2)]
        else:
            from math import sqrt

            roots = [
                str(eval(f"(-{self.b}-sqrt({self.delta}))/(2*{self.a})")),
                str(eval(f"(-{self.b}+sqrt({self.delta}))/(2*{self.a})")),
            ]
            roots.sort()
            return roots


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
