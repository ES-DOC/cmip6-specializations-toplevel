"""
.. module:: enum_validator.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a CMIP6 enumeration specialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import re



# Regular expressions.
_RE_ENUM_NAME = '^[a-z_]+$'
_RE_ENUM_MEMBER_NAME = '^[a-zA-Z0-9-_ ()/\*\.\,\:+]+$'


def validate_enumerations(enumerations):
    """Validates the module .

    :param dict enumerations: Specialized enumerations.

    """
    errors = []
    for name, value in enumerations.items():
        errors += _validate_enum(name, value)

    return errors


def _validate_enum(name, obj):
    """Validates an enumeration.

    :param str name: Enumeration name.
    :param dict obj: Enumeration definition.

    """
    errors = []

    # Validate name.
    if not re.match(_RE_ENUM_NAME, name):
        errors.append("name is invalid - must be lower_case_underscore")

    # Validate description.
    if "description" not in obj:
        errors.append("description is required")
    elif not isinstance(obj['description'], str):
        errors.append("description must be a string")

    # Validate members.
    if "members" not in obj:
        errors.append("members is required")
    elif not isinstance(obj['members'], list) or \
         not len(obj['members']) or \
         [m for m in obj['members'] if not isinstance(m, tuple) or len(m) != 2]:
        errors.append("members must defined as a list of tuples: (name, description)")
    else:
        for m_obj in obj['members']:
        	errors += _validate_enum_member(m_obj)

    return ["ENUMERATION[{}] :: {}".format(name, e) for e in errors]


def _validate_enum_member(defn):
    """Validates an enum member.

    :param tuple defn: Enum member definition.

    """
    errors = []

    # Name is mandatory.
    name = defn[0]
    if name is None:
        errors.append("name is invalid")

    # Name is mandatory.
    if not re.match(_RE_ENUM_MEMBER_NAME, name):
        err = 'Invalid enum member: {} --> name contain invalid characters'
        err = err.format(name)
        errors.append(err)

    # Description is mandatory.
    description = defn[1]
    if description is None:
        pass
        # errors.append("member description is missing :: member-name={}".format(name))

    return errors
