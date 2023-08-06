# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a string."""

import codecs

from .._plumtype import PlumType


class StrType(PlumType):

    """Str type metaclass.

    Create custom |Str| subclass.

    :param str encoding: encoding name (see :mod:`codecs` standard encodings)
    :param str errors: error handling (e.g. ``'string'``, ``'ignore'``, ``'replace'``)
    :param int nbytes: size in number of bytes
    :param bytes pad: pad value, len(pad) must equal 1

    For example:

        >>> from plum.str import Str
        >>> class MyStr(Str, encoding='ascii', nbytes=4):
        ...     pass
        ...
        >>>

    """

    def __new__(mcs, name, bases, namespace, encoding=None, errors=None, nbytes=None,
                pad=None, zero_termination=None):
        # pylint: disable=too-many-arguments, unused-argument
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, encoding=None, errors=None, nbytes=None,
                 pad=None, zero_termination=None):
        # pylint: disable=too-many-arguments
        super().__init__(name, bases, namespace)

        if encoding is None:
            encoding = cls._codecs_info.name

        if errors is None:
            errors = cls._errors

        if nbytes is None:
            nbytes = cls.__nbytes__
        else:
            assert nbytes > 0

        if pad is None:
            pad = cls._pad
        else:
            pad = bytes(pad)
            assert len(pad) == 1

        if zero_termination is None:
            zero_termination = cls._zero_termination

        cls._codecs_info = codecs.lookup(encoding)
        cls._errors = errors
        cls.__nbytes__ = nbytes
        cls._pad = pad
        cls._zero_termination = zero_termination
