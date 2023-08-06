#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 lafrite <lafrite@Poivre>
#
# Distributed under terms of the MIT license.

from mapytex.calculus.core.tree import Tree
from .mo import Molecule, MO
from .atoms import MOnumber

__all__ = ["MOFraction"]


class MOFraction(Molecule):

    """ Fraction math object"""

    MAINOP = "/"

    def __init__(self, numerator, denominator, negative=False):
        """ Initiate the MOFraction

        It can't be indempotent.

        :param numerator: Numerator of the Fraction
        :param denominator: Denominator of the Fraction
        :param negative: Is the fraction negative (not concidering sign of
        numerator or denominator.

        >>> f = MOFraction(2, 3)
        >>> f
        <MOFraction 2 / 3>
        >>> print(f.__txt__)
        2 / 3
        >>> print(f.__tex__)
        \\dfrac{2}{3}
        >>> print(f)
        2 / 3
        >>> f = MOFraction(2, 3, negative = True)
        >>> f
        <MOFraction - 2 / 3>
        """
        _numerator = MO.factory(numerator)
        _denominator = MO.factory(denominator)
        base_tree = Tree("/", _numerator, _denominator)
        if negative:
            tree = Tree("-", None, base_tree)
        else:
            tree = base_tree
        Molecule.__init__(self, tree)

        self._numerator = _numerator
        self._denominator = _denominator
        self.negative = negative

    @property
    def numerator(self):
        """ Get the numerator. If self is negative, getting the opposite of the _numerator
        """
        if self.negative:
            return Tree("-", None, self._numerator)

        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def inverse(self):
        """ return the inverse fraction """
        return MOFraction(self._denominator, self._numerator, self.negative)

    def differentiate(self):
        """ differentiate a fraction and get something!

        :example:
        >>> a = MOFraction(2, 3)
        >>> a.differentiate()
        <MOnumber 0>
        """
        d_num = self.numerator.differentiate()
        d_denom = self.denominator.differentiate()

        if d_num == 0 and d_denom == 0:
            return MOnumber(0)
        else:
            raise NotImplementedError


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
