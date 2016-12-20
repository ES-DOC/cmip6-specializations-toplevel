"""A top level model.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to top-level specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to top-level specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Roland Seferian (CNRM)'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-09-01", "Initialised", "Eric Guilyardi"),
    ("0.2.0", "2016-11-08", "Changed syntax to simplify and remove CIM2 dependencies", "Eric Guilyardi et al."),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific top-level
# --------------------------------------------------------------------
DESCRIPTION = 'Top level model'

# --------------------------------------------------------------------
# KEY PROPERTIES: File name (without the .py suffix) containing key properties of the top level model.
# --------------------------------------------------------------------
KEY_PROPERTIES = 'model_key_properties'

# --------------------------------------------------------------------
# SIMULATES: Realms simulated by the model
# N.B. Official realms names are from https://github.com/WCRP-CMIP/CMIP6_CVs/blob/master/CMIP6_realm.json
# N.B. Creation tool should include an on/off switch to allow for partial configurations (AMIP, AOGCM)
# --------------------------------------------------------------------
SIMULATES = [
        "aerosol",
        "atmos",
        "atmosChem",
        "land",
        "landIce",
        "ocean",
        "ocnBgchem",
        "seaIce",
]

# --------------------------------------------------------------------
# DETAILS: top level details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# ENUMERATIONS: top level enumerations
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
