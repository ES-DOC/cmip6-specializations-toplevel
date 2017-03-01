"""
.. module:: validate_realm.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a CMIP6 scientific model specialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from utils import validate_std



def validate(ctx, root):
    """Validates a scientific model specialization.

    :param ValidationContext ctx: Validation contextual information.

    """
    # Validate standard attributes.
    validate_std(ctx, root)

    # Validate expected fields.
    for name, type_ in {
        ('CONTRIBUTORS', str),
        ('CHANGE_HISTORY', list),
        ('KEY_PROPERTIES', str),
        ('PROCESSES', list)
        }:
        if not hasattr(root, name):
            ctx.error("{} property is missing".format(name))
        elif not isinstance(getattr(root, name), type_):
            ctx.error("{} property must be a string".format(name))

    # Validate CHANGE_HISTORY.
    if [i for i in root.CHANGE_HISTORY if not isinstance(i, tuple) or len(i) != 4]:
        ctx.error("CHANGE_HISTORY entries must be 4 member tuples: (version, date, comment, who)")

    # Validate PROCESSES.
    process_keys = [p.__name__ for p in ctx.processes]
    for process_key in root.PROCESSES:
        if process_key not in process_keys:
            err = "invalid process key: {}".format(process_key)
            ctx.error(err)
