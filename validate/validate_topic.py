"""
.. module:: validate_topic.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a specialized CMIP6 scientific topic.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from utils import validate_std
from validate_detail_sets import validate as validate_detail_sets
from validate_enum import validate_enumerations



def validate(ctx, topic):
    """Validates a CMIP6 scientific detail topic.

    :param ValidationContext ctx: Validation contextual information.
    :param module detail_topic: A python module containing specializations.

    """
    # Determine whether validating a process or not.
    is_process = not topic.__name__.endswith("grid") and \
                 not topic.__name__.endswith("key_properties")

    # Set expected sections.
    sections = ['ENUMERATIONS', 'DETAILS']
    if not topic.__name__.endswith("grid") and \
       not topic.__name__.endswith("key_properties"):
        sections.append('SUB_PROCESSES')

    # Level-1 validation.
    validate_std(ctx, topic, sections)
    if ctx.errors[topic]:
        return

    # Level-2 validation.
    ctx.errors[topic] += \
        validate_enumerations(topic.ENUMERATIONS)
    for section in sections[1:]:
        ctx.errors[topic] += \
            validate_detail_sets(topic, getattr(topic, section))
