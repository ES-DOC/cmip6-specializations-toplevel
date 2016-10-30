"""A top level model.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
from collections import OrderedDict
# --------------------------------------------------------------------
# CONTACT
#
# Set the top level model co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to top level model authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS
#
# Set to top level contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Roland Seferian (CNRM)'

# --------------------------------------------------------------------
# CHANGE HISTORY
#
# Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2016-09-01", "Initialised", "Eric Guilyardi"),
     ]

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# MODEL: DESCRIPTION
#
# Scientific context of top level model
# --------------------------------------------------------------------
DESCRIPTION = 'Top level model'

CATEGORY = ('ENUM:model_types', '1.1',
            "Generic type for this model."),

CITATIONS = ('shared.citation', '0.N', "Set of pertinent citations."),


# --------------------------------------------------------------------
# MODEL: NAME
#
# Official CMIP model name ('source_id' in netCDF files)
# *KEY* to allow automated links with data and other documents
# --------------------------------------------------------------------
NAME = ''

# --------------------------------------------------------------------
# MODEL: LONG_NAME ('source' in netCDF files)
# --------------------------------------------------------------------
LONG_NAME = ''
#
# --------------------------------------------------------------------
# MODEL: KEY PROPERTIES
#
# File name (without the .py suffix) containing key properties of the
# top level model.
# --------------------------------------------------------------------
KEY_PROPERTIES = 'model_key_properties'

# --------------------------------------------------------------------
# MODEL: SIMULATES
#
# Realms simulated by the model
# Official realms names are from https://github.com/WCRP-CMIP/CMIP6_CVs/blob/master/CMIP6_realm.json
# Creation tool should include an on/off switch to allow for partial configurations (AMIP, AOGCM)
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
# MODEL: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['model_types'] = {
    'description': 'Defines a set of gross model classes.',
    'is_open': True,
    'members': [
        ("Atm Only", "Atmosphere Only"),
        ("Ocean Only", "Ocean Only"),
        ("Regional", "Regional Model"),
        ("ESM", "Earth System Model (Atmosphere, Ocean, Land, Sea-ice and cycles)"),
        ("CGCM", "Global Coupled Climate Model (Atmosphere, Ocean, Land, Sea-ice no carbon cycle)"),
        ("IGCM", "Intermediate Complexity GCM"),
        ("GCM-MLO", "GCM with mixed layer ocean"),
        ("Mesoscale", "Mesoscale Model"),
        ("Process", "Limited Area process model"),
        ("Planetary", "Non-Earth model"),
    ]
}
