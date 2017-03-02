"""
.. module:: validate_topic.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a specialized CMIP6 scientific topic.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import re

import validate_property



# Regular expressions.
_RE_DETAIL_NAME = '^[a-z_]+$'
_RE_DETAILSET_NAME = '^[a-z_]+$'

# Set of valid property cardinalities.
_CARDINALITIES = {'0.1', '1.1', '0.N', '1.N'}

# Set of valid property types.
_TYPES = {'bool', 'float', 'int', 'str'}



def validate(topic, prop_sets):
    """Validates a set of CMIP6 scientific details.

    :param module topic: A specialization topic.
    :param module prop_sets: Topic property sets.

    """
    errors = []

    for name, defn in prop_sets.items():
        _validate_property_set(errors, topic.ENUMERATIONS.keys(), prop_sets, name, defn)

    return errors


def _validate_property_set(errors, enums, associated, name, defn):
    """Validates a single detail set specialization.

    """
    # Verify nesting level.
    if len(name.split(":")) > 2:
        errors.append("{} : property nesting level cannot be > 2".format(name))
        return

    # ... verify hierachical name is correct.
    is_top_level = name.startswith("toplevel")
    if not is_top_level:
        if ":" in name and not ":".join((name.split(":")[0:-1])) in associated:
            errors.append("{}: must be associated with a parent property set".format(name))
            return

    # description = mandatory string.
    if "description" not in defn:
        errors.append("{}: detail set must have a description".format(name))
    elif not isinstance(defn['description'], str):
        errors.append("{}: detail set description must be a string".format(name))

    # properties = collection.
    if "properties" in defn:
        if not isinstance(defn['properties'], list):
            errors.append("{}: properties must defined as a list".format(name))
        elif [p for p in defn['properties'] if not isinstance(p, tuple) or len(p) != 4]:
            errors.append("{}: all properties must be 4 member tuples".format(name))
        else:
            for prop in defn['properties']:
                errors += ["{}.{}".format(name, i) for i in validate_property.validate(prop, enums)]
