#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 lafrite <lafrite@Poivre>
#
# Distributed under terms of the MIT license.

"""
Tokens: practical envelop of math object

"""
from ..renders import renders
from ...core.MO.atoms import moify


class Token(object):

    """ Token: practical envelop of an math object """

    RENDER = "txt"

    def __init__(self, mo, name="", ancestor=None):
        self._mo = mo
        self.name = name
        self._mathtype = None
        self._ancestor = ancestor

    @classmethod
    def random(
        cls,
        family="integer",
        **kwds
    ):
        raise NotImplemented

    @classmethod
    def set_render(cls, render):
        """ Define default render function

        :param render: render name (txt or tex)
        """
        cls.RENDER = render

    def explain(self):
        """ Yield every calculus step which have lead to self
        
        :example:
        >>> from mapytex.calculus.API import Expression
        >>> e = Expression.from_str("2+3*4")
        >>> f = e.simplify()
        >>> f
        <Integer 14>
        >>> for s in f.explain():
        ...     print(s)
        2 + 3 * 4
        2 + 12
        14
        """
        try:
            yield from self._ancestor.explain()
            yield self
        except AttributeError:
            yield self

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__txt__}>"

    def __str__(self):
        if self.RENDER == "tex":
            return self.__tex__
        elif self.RENDER == "txt":
            return self.__txt__
        else:
            raise ValueError(f"Unknow render {self.RENDER}")

        # return renders[self.RENDER](self._mo)

    @property
    def __txt__(self):
        return self._mo.__txt__

    @property
    def __tex__(self):
        return self._mo.__tex__

    @property
    def raw(self):
        """ Get python's raw forme of the token  """
        return self._mo.content

    def _operate(self, other, operation):
        """ Make a operation between 2 Tokens """
        from ..expression import Expression
        from ...core import Tree
        from . import factory

        if not isinstance(other, Token):
            try:
                _other = factory(other)
            except AttributeError:
                _other = factory(Expression(moify(other)))
        else:
            _other = other

        if operation == '-':
            tree = Tree("+", self._mo, Tree("-", None,  _other._mo))
        else:
            tree = Tree(operation, self._mo, _other._mo)
        return Expression(tree).simplify()

    def __add__(self, other):
        """ Adding 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> b = Integer(7)
        >>> c = a + b
        >>> c
        <Integer 10>
        >>> for i in c.explain():
        ...    print(i)
        3 + 7
        10
        >>> a = Integer(3)
        >>> c = a + 7
        >>> c
        <Integer 10>
        >>> for i in c.explain():
        ...    print(i)
        3 + 7
        10
        >>> a = Integer(3)
        >>> c = a + "x"
        >>> c
        <Linear x + 3>
        >>> from .number import Fraction 
        >>> a = Fraction("4/3")
        >>> b = Integer(7)
        >>> c = a + b
        >>> c
        <Fraction 25 / 3>
        >>> for i in c.explain():
        ...    print(i)
        4 / 3 + 7
        4 / 3 + 7 / 1
        4 / 3 + (7 * 3) / (1 * 3)
        4 / 3 + 21 / 3
        (4 + 21) / 3
        25 / 3
        """
        return self._operate(other, "+")

    def __sub__(self, other):
        """ Subing 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> b = Integer(7)
        >>> c = a - b
        >>> c
        <Integer - 4>
        >>> for i in c.explain():
        ...    print(i)
        3 - 7
        3 - 7
        - 4
        >>> a = Integer(3)
        >>> c = a - 7
        >>> c
        <Integer - 4>
        >>> a = Integer(3)
        >>> c = a - "x"
        >>> c
        <Linear - x + 3>
        """
        return self._operate(other, "-")

    def __mul__(self, other):
        """ Multiply 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> b = Integer(7)
        >>> c = a * b
        >>> c
        <Integer 21>
        >>> for i in c.explain():
        ...    print(i)
        3 * 7
        21
        >>> c = a * 7
        >>> c
        <Integer 21>
        >>> c = a * "x"
        >>> c
        <Linear 3x>
        >>> from .number import Fraction 
        >>> a = Fraction("4/3")
        >>> b = Integer(7)
        >>> c = a * b
        >>> c
        <Fraction 28 / 3>
        >>> for i in c.explain():
        ...    print(i)
        4 / 3 * 7
        (4 * 7) / 3
        28 / 3
        """
        return self._operate(other, "*")

    def __truediv__(self, other):
        """ Divising 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> b = Integer(7)
        >>> c = a / b
        >>> c
        <Fraction 3 / 7>
        >>> for i in c.explain():
        ...    print(i)
        3 / 7
        >>> c = a / 7
        >>> c
        <Fraction 3 / 7>
        >>> from .number import Fraction 
        >>> a = Fraction("4/3")
        >>> b = Integer(7)
        >>> c = a / b
        >>> c
        <Fraction 4 / 21>
        >>> for i in c.explain():
        ...    print(i)
        4 / 3 / 7
        4 / 3 * 1 / 7
        (4 * 1) / (3 * 7)
        4 / 21
        """
        return self._operate(other, "/")

    def __pow__(self, other):
        """ Token powered by an other

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> b = Integer(7)
        >>> c = a ** b
        >>> c
        <Integer 2187>
        >>> c = a ** 7
        >>> c
        <Integer 2187>
        >>> from .number import Decimal 
        >>> a = Decimal('2.3')
        >>> c = a ** 2
        >>> c
        <Decimal 5.29>

    """
        return self._operate(other, "^")


    def _roperate(self, other, operation):
        """ Make a operation between 2 Tokens """
        from ..expression import Expression
        from ...core import Tree
        from . import factory

        if not isinstance(other, Token):
            try:
                _other = factory(other)
            except AttributeError:
                _other = factory(Expression(moify(other)))
        else:
            _other = other
        if operation == '-':
            tree = Tree("+", _other._mo, Tree("-", None,  self._mo))
        else:
            tree = Tree(operation, _other._mo, self._mo)
        return Expression(tree).simplify()

    def __radd__(self, other):
        """ Adding 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> c = 7 + a
        >>> c
        <Integer 10>
        >>> c = "x" + a
        >>> c
        <Linear x + 3>
        """
        return self._roperate(other, "+")

    def __rsub__(self, other):
        """ Subing 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> c = 7 - a
        >>> c
        <Integer 4>
        >>> a = Integer(3)
        >>> c = "x" - a
        >>> c
        <Linear x - 3>
        """
        return self._roperate(other, "-")
    def __rmul__(self, other):
        """ Multiply 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> c = 7 * a
        >>> c
        <Integer 21>
        >>> c = "x" * a
        >>> c
        <Linear 3x>
        """
        return self._roperate(other, "*")

    def __rtruediv__(self, other):
        """ Divising 2 Tokens or a Token and a Expression

        :example:
        >>> from .number import Integer 
        >>> a = Integer(3)
        >>> c = 7 / a
        >>> c
        <Fraction 7 / 3>
        """
        return self._roperate(other, "/")


    def _get_soul(self, other=None):
        """ Get the builtin soul of self or other """
        if isinstance(other, Token):
            return other._mo._value
        elif not other is None:
            return other
        return self._mo._value

    def __eq__(self, other):
        return self._get_soul() == self._get_soul(other)

    def __gt__(self, other):
        return self._get_soul() > self._get_soul(other)

    def __lt__(self, other):
        return self._get_soul() < self._get_soul(other)

    def __ge__(self, other):
        return self._get_soul() >= self._get_soul(other)

    def __le__(self, other):
        return self._get_soul() <= self._get_soul(other)


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
