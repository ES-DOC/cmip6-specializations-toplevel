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
NAME = ['']

# --------------------------------------------------------------------
# MODEL: TUNING
#
# Model tuning
# --------------------------------------------------------------------
TUNING = 'tuning'

# --------------------------------------------------------------------
# MODEL: KEY PROPERTIES
#
# Key properties of the top level model
# --------------------------------------------------------------------
KEY_PROPERTIES = 'model_key_properties'

# --------------------------------------------------------------------
# MODEL: REALM
#
# Realms simulated by the model
# TODO: included on/off switch to allow for partial configurations (AMIP, AOGCM)
# --------------------------------------------------------------------
REALMS = [
    'atmosphere',
    'ocean',
    'seaice',
    ]
