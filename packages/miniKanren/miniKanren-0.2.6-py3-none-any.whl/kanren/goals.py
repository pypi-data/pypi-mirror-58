import operator
import collections

from itertools import permutations
from collections.abc import Sequence

from cons import cons
from cons.core import ConsNull
from unification import isvar, var, reify, unify

from .core import (
    eq,
    EarlyGoalError,
    conde,
    condeseq,
    lany,
    lallgreedy,
    lall,
    fail,
    success,
)
from .util import unique


def heado(head, coll):
    """Construct a goal stating that head is the head of coll.

    See Also
    --------
        tailo
        conso
    """
    return eq(cons(head, var()), coll)


def tailo(tail, coll):
    """Construct a goal stating that tail is the tail of coll.

    See Also
    --------
        heado
        conso
    """
    return eq(cons(var(), tail), coll)


def conso(h, t, l):
    """Construct a goal stating that cons h + t == l."""
    return eq(cons(h, t), l)


def nullo(l):
    """Create a goal asserting that a term is a "Lisp-like" null.

    For un-unified logic variables, it unifies with an empty list.
    """

    def _nullo(s):
        l_rf = reify(l, s)
        if isvar(l_rf):
            yield unify(l_rf, [], s)
        elif isinstance(l_rf, ConsNull):
            yield s

    return _nullo


def itero(l):
    """Construct a goal asserting that a term is an iterable type.

    This is a generic version of the standard `listo` that accounts for
    different iterable types supported by `cons` in Python.

    See `nullo`
    """
    c, d = var(), var()
    return (conde, [(nullo, l), success], [(conso, c, d, l), (itero, d)])


def permuteq(a, b, eq2=eq):
    """Construct a goal asserting equality under permutation.

    For example, (1, 2, 2) equates to (2, 1, 2) under permutation
    >>> from kanren import var, run, permuteq
    >>> x = var()
    >>> run(0, x, permuteq(x, (1, 2)))
    ((1, 2), (2, 1))

    >>> run(0, x, permuteq((2, 1, x), (2, 1, 2)))
    (2,)
    """
    if isinstance(a, Sequence) and isinstance(b, Sequence):
        if len(a) != len(b):
            return fail
        elif collections.Counter(a) == collections.Counter(b):
            return success
        else:
            c, d = list(a), list(b)
            for x in list(c):
                # TODO: This is quadratic in the number items in the sequence.
                # Need something like a multiset. Maybe use
                # collections.Counter?
                try:
                    d.remove(x)
                    c.remove(x)
                except ValueError:
                    pass

            if len(c) == 1:
                return (eq2, c[0], d[0])
            return condeseq(
                ((eq2, x, d[0]), (permuteq, c[0:i] + c[i + 1 :], d[1:], eq2))
                for i, x in enumerate(c)
            )
    elif not (isinstance(a, Sequence) or isinstance(b, Sequence)):
        raise ValueError(
            "Neither a nor b is a Sequence: {}, {}".format(type(a), type(b))
        )

    if isvar(a) and isvar(b):
        raise EarlyGoalError()

    if isvar(a) or isvar(b):
        if isinstance(b, Sequence):
            c, d = a, b
        elif isinstance(a, Sequence):
            c, d = b, a

        return (condeseq, ([eq(c, perm)] for perm in unique(permutations(d, len(d)))))


def seteq(a, b, eq2=eq):
    """Construct a goal asserting set equality.

    For example (1, 2, 3) set equates to (2, 1, 3)

    >>> from kanren import var, run, seteq
    >>> x = var()
    >>> run(0, x, seteq(x, (1, 2)))
    ((1, 2), (2, 1))

    >>> run(0, x, seteq((2, 1, x), (3, 1, 2)))
    (3,)
    """
    ts = lambda x: tuple(set(x))
    if not isvar(a) and not isvar(b):
        return permuteq(ts(a), ts(b), eq2)
    elif not isvar(a):
        return permuteq(ts(a), b, eq2)
    else:  # not isvar(b)
        return permuteq(a, ts(b), eq2)


def goalify(func, name=None):
    """Convert Python function into kanren goal.

    >>> from kanren import run, goalify, var, membero
    >>> typo = goalify(type)
    >>> x = var('x')
    >>> run(0, x, membero(x, (1, 'cat', 'hat', 2)), (typo, x, str))
    ('cat', 'hat')

    Goals go both ways.  Here are all of the types in the collection

    >>> typ = var('typ')
    >>> results = run(0, typ, membero(x, (1, 'cat', 'hat', 2)), (typo, x, typ))
    >>> print([result.__name__ for result in results])
    ['int', 'str']
    """

    def funco(inputs, out):
        if isvar(inputs):
            raise EarlyGoalError()
        else:
            if isinstance(inputs, (tuple, list)):
                if any(map(isvar, inputs)):
                    raise EarlyGoalError()
                return (eq, func(*inputs), out)
            else:
                return (eq, func(inputs), out)

    name = name or (func.__name__ + "o")
    funco.__name__ = name

    return funco


def membero(x, coll):
    """Construct a goal stating that x is an item of coll."""
    if not isvar(coll):
        return (lany,) + tuple((eq, x, item) for item in coll)
    raise EarlyGoalError()


typo = goalify(type, name="typo")
isinstanceo = goalify(isinstance, name="isinstanceo")
not_equalo = goalify(operator.ne, name="not_equalo")


def appendo(l, s, ls, base_type=tuple):
    """Construct a goal stating ls = l + s.

    See Byrd thesis pg. 247
    https://scholarworks.iu.edu/dspace/bitstream/handle/2022/8777/Byrd_indiana_0093A_10344.pdf

    Parameters
    ----------
    base_type: type
        The empty collection type to use when all terms are logic variables.
    """
    if all(map(isvar, (l, s, ls))):
        raise EarlyGoalError()
    a, d, res = [var() for i in range(3)]
    return (
        lany,
        (lallgreedy, (eq, l, base_type()), (eq, s, ls)),
        (lall, (conso, a, d, l), (conso, a, res, ls), (appendo, d, s, res)),
    )
