"""
.. module:: validate_root.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a CMIP6 scientific root specialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from utils import validate_field



def validate(ctx):
    """Validates a scientific root specialization.

    :param DefinitionsValidationContext ctx: Validation contextual information.

    """
    # Set current module.
    ctx.module = ctx.root

    # Validate fields.
    for name, typeof in {
        ('AUTHORS', str),
        ('CONTACT', str),
        ('CONTRIBUTORS', str),
        ('CHANGE_HISTORY', list),
        ('DESCRIPTION', str),
        ('GRID', (str, type(None))),
        ('KEY_PROPERTIES', str),
        ('PROCESSES', list),
        }:
        validate_field(ctx, ctx.root, name, typeof)

    # Validate CHANGE_HISTORY.
    if [i for i in ctx.root.CHANGE_HISTORY if not isinstance(i, tuple) or len(i) != 4]:
        ctx.error("CHANGE_HISTORY entries must be 4 member tuples: (version, date, comment, who)")

    # Validate module keys.
    module_keys = [ctx.root.GRID, ctx.root.KEY_PROPERTIES] + ctx.root.PROCESSES
    module_keys = [i for i in module_keys if i is not None]
    for module_key in module_keys:
        if not ctx.has_module(module_key):
            ctx.error("{0} is an invalid key - no matching {0}.py file can be found".format(module_key))
