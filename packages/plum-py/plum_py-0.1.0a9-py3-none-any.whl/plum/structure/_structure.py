# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure type."""

from .._plum import Plum
from ._structuretype import StructureType
from ._structureview import StructureView


class Structure(list, Plum, metaclass=StructureType):

    """Interpret bytes as a list of uniquely typed items.

    :param iterable iterable: items

    """

    # filled in by metaclass
    __plum_internals__ = (), (), False  # names, types, has_touchups
    __nbytes__ = 0
    __plum_names__ = []

    def __init__(self, *args, **kwargs):
        # pylint: disable=super-init-not-called

        # initializer for anonymous structure (metaclass overrides this
        # implementation when creating subclasses with pre-defined members)
        self.extend(args)
        names = [None] * len(args)
        if kwargs:
            self.extend(kwargs.values())
            names.extend(kwargs.keys())
        object.__setattr__(self, '__plum_names__', names)

    @classmethod
    def __pack__(cls, buffer, offset, value, dump):
        # metaclass installs a proper __pack__, this placeholder keeps pylint happy
        pass

    @classmethod
    def __unpack__(cls, buffer, offset, limit, dump, parent):
        # pylint: disable=too-many-locals
        names, types, _has_touchups = cls.__plum_internals__

        self = list.__new__(cls)
        append = self.append

        if dump:
            dump.cls = cls

            for i, (name, item_cls) in enumerate(zip(names, types)):
                subdump = dump.add_level(access=f'[{i}] (.{name})')
                item, offset, limit = item_cls.__unpack__(buffer, offset, limit, subdump, self)
                append(item)
        else:
            for item_cls in types:
                item, offset, limit = item_cls.__unpack__(buffer, offset, limit, None, self)
                append(item)

        return self, offset, limit

    def __str__(self):
        lst = []
        for name, value in zip(self.__plum_names__, self):
            try:
                rpr = value.__baserepr__()
            except AttributeError:
                rpr = value.__repr__()
            if name is not None:
                rpr = name + '=' + rpr
            lst.append(rpr)

        return f"{type(self).__name__}({', '.join(lst)})"

    __baserepr__ = __str__

    __repr__ = __str__

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        """
        if not cls.__nbytes__:
            raise TypeError(f"cannot create view for structure {cls.__name__!r} "
                            "with variable size")

        if cls.__plum_internals__[2]:  # has_touchups flags
            raise TypeError(f"cannot create view for structure {cls.__name__!r} "
                            "with member protocol touch-ups")

        return StructureView(cls, buffer, offset)

    # __getattr__ injected into class namespace by metaclass for anonymous structure subclass
    # __setattr__ injected into class namespace by metaclass for anonymous structure subclass
