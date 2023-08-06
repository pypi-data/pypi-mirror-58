# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""BitFields type metaclass."""

from enum import IntEnum

from ..._plumtype import PlumType
from ._bitfield import BitField


class MockBitFields:

    """Fake BitFields type for calculating default value."""

    def __init__(self, value):
        self.__value__ = value

    def __int__(self):
        return self.__value__


class BitFieldsType(PlumType):

    """BitFields type metaclass.

    Create custom |BitFields| subclass. For example:

    :param int nbytes: number of bytes
    :param str byteorder: ``'big'`` or ``'little'``
    :param int default: default value (before applying bit field values)
    :param int ignore: mask applied during comparison to ignore bit fields

    For example:

        >>> from plum.int.bitfields import BitFields, bitfield
        >>> class MyBits(BitFields, nbytes=1, byteorder='big', default=0, ignore=0x80):
        ...     nibble: int = bitfield(pos=0, size=4)
        ...     threebits: int = bitfield(pos=4, size=3)
        ...
        >>>

    """

    def __new__(mcs, name, bases, namespace, nbytes=None, byteorder=None,
                default=None, ignore=None):
        # pylint: disable=too-many-arguments,unused-argument
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, nbytes=None, byteorder=None,
                 default=None, ignore=None):
        # pylint: disable=too-many-arguments, too-many-locals
        super().__init__(name, bases, namespace)

        if byteorder is None:
            byteorder = cls.__byteorder__

        assert byteorder in {'big', 'little'}

        if default is None:
            default = cls.__default__
        default = int(default)

        if ignore is None:
            ignore = cls.__ignore__

        fields = dict()
        adjusted_default = MockBitFields(default)
        for fieldname, typ in getattr(cls, '__annotations__', {}).items():
            field = getattr(cls, fieldname, None)
            assert isinstance(field, BitField)
            assert isinstance(typ, BitFieldsType) or issubclass(
                typ, (int, IntEnum))
            field.type = typ
            fields[fieldname] = field
            if field.default is not None:
                field.__set__(adjusted_default, field.default)

        if nbytes is None:
            numbits = max(field.pos + field.size for field in fields.values())
            nbytes = 1
            while numbits > (nbytes * 8):
                nbytes *= 2

        max_ = (1 << (nbytes * 8)) - 1

        for field in fields.values():
            if field.ignore:
                ignore |= field.mask << field.pos
            elif isinstance(field.type, BitFieldsType):
                ignore |= field.type.__ignore__ << field.pos

        assert 0 <= default <= max_, f'default must be: 0 <= number <= 0x{max_:x}'

        cls.__byteorder__ = byteorder
        cls.__compare_mask__ = (max_ ^ ignore) & max_
        cls.__fields__ = fields
        cls.__default__ = int(adjusted_default)
        cls.__fields_with_defaults__ = {
            name for name, field in fields.items() if field.default is not None}
        cls.__ignore__ = ignore
        cls.__max__ = max_
        cls.__nbytes__ = nbytes
