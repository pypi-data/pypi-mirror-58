# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized structure member utility."""

from importlib import import_module

from .._exceptions import ExcessMemoryError
from .._plum import getbytes
from ._member import Member


def __unpack__(cls, buffer, offset, limit, dump, parent):
    # pylint: disable=too-many-locals

    sized_member = cls.__member__

    expected_size_in_bytes = getattr(parent, sized_member.sizemember) * sized_member.ratio

    chunk, offset, limit = getbytes(buffer, offset, expected_size_in_bytes, limit, dump, cls)

    if dump:
        dump.memory = b''

    item, actual_size_in_bytes, _ = cls.__original_unpack__(chunk, 0, None, dump, parent)

    extra_bytes = chunk[actual_size_in_bytes:]

    if extra_bytes:
        if dump:
            value = '<excess bytes>'
            for i in range(0, len(extra_bytes), 16):
                dump.add_row(value=value, memory=extra_bytes[i:i+16])
                value = ''

        raise ExcessMemoryError(f'{len(extra_bytes)} unconsumed bytes', extra_bytes)

    return item, offset, limit


class SizedMember(Member):

    """Sized member definition."""

    __slots__ = [
        'name',
        'cls',
        'sizemember',
        'ratio',
    ]

    def __init__(self, sizemember, ratio):
        # pylint: disable=super-init-not-called
        self.name = None  # assigned during structure class construction
        self.cls = None  # assigned during structure class construction
        self.sizemember = sizemember
        self.ratio = ratio

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
        size_of = import_module('._size_of', 'plum.structure')
        super().adjust_members(
            members, name=self.sizemember, cls=size_of.SizeMember,
            kwargs={'ratio': self.ratio})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__member__': self,
            '__unpack__': classmethod(__unpack__),
            '__original_unpack__': self.cls.__unpack__,
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def size_via(size, ratio=1):
    """Configure structure member to follow size structure member.

    :param str size: size member name
    :param int ratio: number of bytes per increment of size member
    :returns: structure member definition
    :rtype: SizedMember

    """
    return SizedMember(size, ratio)
