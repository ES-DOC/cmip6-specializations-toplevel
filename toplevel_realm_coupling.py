"""A model radiative forcings sepecialization.

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
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell, Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Coupling between model realms'

# --------------------------------------------------------------------
# TOPLEVEL: 
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': '',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of coupling in the model'),
        ('atmosphere_double_flux', 'bool', '1.1',
             'Is the atmosphere passing a double flux to the ocean and sea ice (as opposed to a single one)?'),
        ('atmosphere_fluxes_calculation_grid', 'ENUM:atmosphere_fluxes_calculation_grid', '0.1',
             'Where are the air-sea fluxes calculated'), #: on the atmospheric, the oceanic or a specific coupler grid?'),  OPEN enum
        ('atmosphere_relative_winds', 'bool', '1.1',
            'Are relative or absolute winds used to compute the flux? I.e. do ocean surface currents enter the wind stress calculation?'),
    ]
}


_fields = 'Enter the coupled fields, their coupling frequency and any coupling details as a comma seperated list. E.g. temperature, daily, area-weighted interpolotaion'

# --------------------------------------------------------------------
# Coupling from OCEAN to other realms
# --------------------------------------------------------------------
_from = 'ocean'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'ocean'
_to   = 'seaice'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'ocean'
_to   = 'ocean_biogeochemistry'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from ATMOSPHERE to other realms
# --------------------------------------------------------------------
_from = 'atmosphere'
_to   = 'ocean'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmosphere'
_to   = 'seaice'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmosphere'
_to   = 'land'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmosphere'
_to   = 'aerosols'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmosphere'
_to   = 'amospheric_chemistry'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }


_from = 'atmosphere'
_to   = 'ocean_biogeochemistry'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from SEAICE to other realms
# --------------------------------------------------------------------
_from = 'seaice'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'seaice'
_to   = 'ocean'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'seaice'
_to   = 'ocean_biogeochemistry'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from LAND to other realms
# --------------------------------------------------------------------
_from = 'land'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'land'
_to   = 'ocean_biogeochemistry'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'land'
_to   = 'atmospheric_chemistry'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from AEROSOLS to other realms
# --------------------------------------------------------------------
_from = 'aerosols'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from ATMOSPHERIC CHEMISTRY to other realms
# --------------------------------------------------------------------
_from = 'atmospheric_chemistry'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmospheric_chemistry'
_to   = 'land'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmospheric_chemistry'
_to   = 'land_ice'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'atmospheric_chemistry'
_to   = 'sea_ice'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from OCEAN BIOGEOCHEMISTRY to other realms
# --------------------------------------------------------------------
_from = 'ocean_biogeochemistry'
_to   = 'ocean'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'ocean_biogeochemistry'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'ocean_biogeochemistry'
_to   = 'seaice'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# Coupling from LAND ICE to other realms
# --------------------------------------------------------------------
_from = 'land_ice'
_to   = 'ocean'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

_from = 'land_ice'
_to   = 'atmosphere'
DETAILS[_from+'_to_'+_to] = {
    'description': _from.replace('_', ' ').capitalize()+' to '+_to.replace('_', ' ')+' interface couplings',
    'properties':[
        ('overview', 'str', '1.1',
            'Overview of '+_from.replace('_', ' ')+' to '+_to.replace('_', ' ')+' coupling interface'),
        ('fields', 'str', '0.N',
             _fields),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['atmosphere_fluxes_calculation_grid'] = {
    'description': 'Where are the air-sea fluxes calculated',
    'is_open': True,
    'members': [
        ("atmospheric grid", None),
        ("oceanic grid", None),
        ("specific coupler grid", None,),
    ]
}

