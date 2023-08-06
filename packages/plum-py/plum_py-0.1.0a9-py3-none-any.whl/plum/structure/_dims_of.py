# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized array structure member utility."""

from importlib import import_module

from ._member import Member
from ..int import Int


def __touchup__(cls, value, parent):
    if value is None:
        array = getattr(parent, cls.__member__.arraymember)
        dims_cls = cls.__member__.cls
        if array is None:
            # both dims and array members not provided
            if issubclass(dims_cls, Int):
                value = 0
            else:
                value = [0] * dims_cls.__dims__[0]
        else:
            if issubclass(dims_cls, Int):
                value = len(array)
            else:
                value = []
                for _ in range(dims_cls.__dims__[0]):
                    value.append(len(array))
                    array = array[0]
    return value


class DimsMember(Member):

    """Dimensions structure member."""

    __slots__ = [
        'name',
        'cls',
        'arraymember'
    ]

    def __init__(self, arraymember):
        # pylint: disable=super-init-not-called
        self.arraymember = arraymember
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
        dims_via = import_module('._dims_via', 'plum.structure')
        super().adjust_members(members, name=self.arraymember, cls=dims_via.ArrayMember)

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__member__': self,
            '__touchup__': classmethod(__touchup__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def dims_of(array):
    """Configure dims structure member to follow dims of array structure member.

    :param str array: array member name
    :returns: structure member definition
    :rtype: DimsMember

    """
    return DimsMember(array)
