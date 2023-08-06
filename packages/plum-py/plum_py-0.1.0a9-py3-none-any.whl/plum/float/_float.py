# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a floating point number."""

from struct import Struct

from .._plum import Plum, getbytes
from ._floattype import FloatType
from ._floatview import FloatView


class Float(float, Plum, metaclass=FloatType):

    """Interpret bytes as a floating point number.

    :param x: value
    :type x: number or str

    """

    _byteorder = 'little'
    __nbytes__ = 4
    _pack_with_format = Struct('<f').pack
    _unpack = Struct('<f').unpack

    __equivalent__ = float

    @classmethod
    def __unpack__(cls, buffer, offset, limit, dump, parent):
        chunk, offset, limit = getbytes(buffer, offset, cls.__nbytes__, limit, dump, cls)

        self = cls._unpack(chunk)[0]

        if dump:
            dump.value = self

        return self, offset, limit

    @classmethod
    def __pack__(cls, buffer, offset, value, dump):
        if dump:
            dump.cls = cls

        chunk = cls._pack_with_format(value)

        end = offset + cls.__nbytes__
        buffer[offset:end] = chunk

        if dump:
            dump.value = value
            dump.memory = chunk

        return end

    __baserepr__ = float.__repr__

    __repr__ = Plum.__repr__

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        """
        return FloatView(cls, buffer, offset)
