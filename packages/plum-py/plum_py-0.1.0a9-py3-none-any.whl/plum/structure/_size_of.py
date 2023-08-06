# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized structure member utility."""

from importlib import import_module

from .. import Plum, pack
from ._member import Member


def __touchup__(cls, value, parent):
    size_member = cls.__member__

    if value is None:
        sized_object = getattr(parent, size_member.sizedmember)

        if sized_object is None:
            # both size and sized member not provided
            value = 0

        else:
            if isinstance(sized_object, Plum):
                value = sized_object.nbytes // size_member.ratio
            else:
                names, types, _has_touchups = type(parent).__plum_internals__
                so_cls = types[names.index(size_member.sizedmember)]
                value = len(pack(so_cls, sized_object)) // size_member.ratio

    return value


class SizeMember(Member):

    """Structure size member definition."""

    __slots__ = [
        'name',
        'cls',
        'ratio',
        'sizedmember',
    ]

    def __init__(self, sizedmember, ratio):
        # pylint: disable=super-init-not-called
        self.sizedmember = sizedmember
        self.ratio = ratio
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
        size_via = import_module('._size_via', 'plum.structure')
        super().adjust_members(
            members, name=self.sizedmember, cls=size_via.SizedMember,
            kwargs={'ratio': self.ratio})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__member__': self,
            '__touchup__': classmethod(__touchup__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def size_of(sized, ratio=1):
    """Configure size structure member to follow size of associated structure member.

    :param str sized: sized member name
    :param int ratio: number of bytes per increment of member
    :returns: structure member definition
    :rtype: SizeMember

    """
    return SizeMember(sized, ratio)
