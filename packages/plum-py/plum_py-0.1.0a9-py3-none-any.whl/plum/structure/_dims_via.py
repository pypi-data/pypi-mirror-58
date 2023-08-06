# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized array structure member utility."""

from importlib import import_module

from ..int import Int
from ._member import Member


def __touchup__(cls, value, parent):
    if value is None:
        dims = getattr(parent, cls.__member__.dimsmember)
        try:
            dims = [int(dims)]
        except TypeError:
            dims = list(dims)

        value = cls.__member__.cls.__make_instance__(None, dims)

    return value


def __unpack__(cls, buffer, offset, limit, dump, parent):
    dims = getattr(parent, cls.__member__.dimsmember)

    try:
        dims = (int(dims),)
    except TypeError:
        dims = tuple(int(d) for d in dims)

    return cls.__original_unpack__(buffer, offset, limit, dump, None, dims)


class ArrayMember(Member):

    """Array structure member definition."""

    __slots__ = [
        'name',
        'cls',
        'dimsmember'
    ]

    def __init__(self, dimsmember):
        # pylint: disable=super-init-not-called
        self.dimsmember = dimsmember
        self.name = None  # assigned during structure class construction
        self.cls = None  # assigned during structure class construction

    @property
    def default(self):
        """Member default value to use when value not provided.

        :returns: member value
        :rtype: object

        """
        return None

    @property
    def ignore(self):
        """Member to be ignored during structure comparison.

        :returns: indication
        :rtype: bool

        """
        return False

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        dims_of = import_module('._dims_of', 'plum.structure')
        super().adjust_members(members, name=self.dimsmember, cls=dims_of.DimsMember)

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        dims_cls = members[self.dimsmember].cls

        if issubclass(dims_cls, Int):
            dims = (None,)
        else:
            dims = [None] * dims_cls.__dims__[0]

        namespace = {
            '__member__': self,
            '__touchup__': classmethod(__touchup__),
            '__unpack__': classmethod(__unpack__),
            '__original_unpack__': self.cls.__unpack__,
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace, dims=dims)


def dims_via(dims):
    """Configure array structure member to follow dims structure member.

    :param str dims: array dimensions member name
    :returns: structure member definition
    :rtype: ArrayMember

    """
    return ArrayMember(dims)
