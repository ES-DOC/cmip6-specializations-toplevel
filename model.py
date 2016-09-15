"""A top level model.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

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

# TODO see CIM2 syntax for these properties

# --------------------------------------------------------------------
# MODEL: NAME
#
# Official CMIP model name to allow automated links with data and other documents
# --------------------------------------------------------------------
NAME = ''

# --------------------------------------------------------------------
# MODEL: LONG_NAME
#
# 
# --------------------------------------------------------------------
LONG_NAME = ''


# --------------------------------------------------------------------
# MODEL: CATEGORY
#
# Generic type for this model
# --------------------------------------------------------------------
CATEGORY = ('ENUM:model_types', '1.1',
            "Generic type for this model."),

CITATIONS = ('shared.citation', '0.N',
             "Set of pertinent citations."),

DEVELOPMENT_HISTORY = ('software.development_path', '0.1',
                       "History of the development of this component."),

RELEASE_DATE = ('time.date_time', '0.1',
                "The date of publication of the component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)."),

REPOSITORY = ('shared.online_resource', '0.1',
              "Location of code for this component."),

VERSION = ('str', '0.1',
           "Version identifier.")

COUPLED_COMPONENTS = ('science.model', '0.N',
                      "Software components which are linked together using a coupler to deliver this model."),

COUPLER = ('software.coupling_framework', '0.1',
           "Overarching coupling framework for model."),

INTERNAL_SOFTWARE_COMPONENTS = ('software.software_component', '0.N',
                                "Software modules which together provide the functionality for this model."),

SIMULATES = ['linked_to(science.scientific_realm)', '0.N',
             "The scientific domains which this model simulates.")

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
# File names (without the .py suffix) containing the scientific realms
# which this model simulates.

# Realms simulated by the model
# TODO: included on/off switch to allow for partial configurations (AMIP, AOGCM)
#
# ***
# I am thinking that each realm is nillable with nil reason
# ("nil:inapplicable", "There is no value"),
# [https://github.com/ES-DOC/esdoc-cim/blob/master/v2/schema/shared_classes.py#L200]
# ***
# --------------------------------------------------------------------
REALMS = [
    'atmosphere',
    'ocean',
    'seaice',
    'oceanBGC',
    'landsurface'
    'atmos_chem',
    'aerorols'
    'ETC.'
]

# --------------------------------------------------------------------
# MODEL: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['model_types'] = {
    'description': 'Defines a set of gross model classes.'
    'is_open': True,
    'members': [
        ("Atm Only", "Atmosphere Only"),
        ("Ocean Only", "Ocean Only"),
        ("Regional", "Regional Model"),
        ("GCM", "Global Climate Model (Atmosphere, Ocean, no carbon cycle)"),
        ("IGCM", "Intermediate Complexity GCM"),
        ("GCM-MLO", "GCM with mixed layer ocean"),
        ("Mesoscale", "Mesoscale Model"),
        ("Process", "Limited Area process model"),
        ("Planetary", "Non-Earth model"),
    ]
}
