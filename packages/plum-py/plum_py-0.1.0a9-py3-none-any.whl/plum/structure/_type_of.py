# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""type_of() structure member utility."""

from importlib import import_module

from ._member import Member


def __touchup__(cls, value, parent):
    type_member = cls.__member__
    type_mapping = type_member.mapping

    if value is None:
        variably_typed_object = getattr(parent, type_member.variably_typed_member)

        variable_object_type = type(variably_typed_object)

        for type_value, object_type in type_mapping.items():
            if variable_object_type is object_type:
                value = type_value
                break
        else:
            raise TypeError(
                f'structure member {type_member.variably_typed_member!r} must '
                f'be one of the following types: '
                f'{list(repr(c) for c in type_mapping.values())} not {object_type!r}')

    return value


class TypeMember(Member):

    """Structure variably typed member definition."""

    __slots__ = [
        'name',
        'cls',
        'mapping',
        'variably_typed_member',
    ]

    def __init__(self, variably_typed_member, mapping):
        # pylint: disable=super-init-not-called
        self.variably_typed_member = variably_typed_member
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
        type_via = import_module('._type_via', 'plum.structure')
        super().adjust_members(
            members, name=self.variably_typed_member, cls=type_via.VariablyTypedMember,
            kwargs={'mapping': self.mapping})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__member__': self,
            '__touchup__': classmethod(__touchup__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def type_of(member, mapping):
    """Configure type structure member to follow type of associated structure member.

    :param str member: variably typed member name
    :param dict mapping: type member value (key) to Plum type (value) mapping
    :returns: structure member definition
    :rtype: TypeMember

    """
    return TypeMember(member, mapping)
