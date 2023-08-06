# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""type_via() member type utility."""

from importlib import import_module

from .._plum import Plum
from ._member import Member


class Varies(Plum):

    """Variably typed member."""

    __member__ = None

    def __new__(cls, value):
        return value

    @classmethod
    def __touchup__(cls, value, parent):
        member = cls.__member__
        type_member = getattr(parent, member.type_member)
        member_cls = member.mapping[type_member]
        return member_cls(value)

    @classmethod
    def __unpack__(cls, buffer, offset, limit, dump, parent):
        member = cls.__member__
        type_member = getattr(parent, member.type_member)
        member_cls = member.mapping[type_member]
        item, offset, limit = member_cls.__unpack__(buffer, offset, limit, dump, parent)
        if not isinstance(item, member_cls):
            # always create instance so that it may be re-packed (e.g. don't let
            # both UInt8 and UInt16 types produce int ... coerce into Plum type)
            item = member_cls(item)
        return item, offset, limit

    @classmethod
    def __pack__(cls, buffer, offset, value, dump):
        return value.__pack__(buffer, offset, value, dump)

    __baserepr__ = object.__repr__


class VariablyTypedMember(Member):

    """Variably typed member definition."""

    __slots__ = [
        'name',
        'cls',
        'mapping',
        'type_member',
    ]

    def __init__(self, type_member, mapping):
        # pylint: disable=super-init-not-called
        self.type_member = type_member
        self.mapping = mapping
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
        type_of = import_module('._type_of', 'plum.structure')
        super().adjust_members(
            members, name=self.type_member, cls=type_of.TypeMember,
            kwargs={'mapping': self.mapping})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        self.cls = type('Varies', (Varies,), {'__member__': self})


def type_via(member, mapping):
    """Configure member's type to follow that specified by associated member.

    :param str member: variably typed member name
    :param dict mapping: type member value (key) to Plum type (value) mapping
    :returns: structure member definition
    :rtype: VariablyTypedMember

    """
    return VariablyTypedMember(member, mapping)
