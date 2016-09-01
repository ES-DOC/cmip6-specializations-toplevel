"""A model key-properties sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

# --------------------------------------------------------------------
# CONTACT
#
# Set to model co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to model authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# KEY PROPERTIES: DESCRIPTION
#
# Scientific context of the key properties
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of the model'

# --------------------------------------------------------------------
# KEY PROPERTIES: DETAILS
#
# Sets of details for the key properties
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['flux_correction'] = {
    'description': 'Flux correction properties of the model',
    'properties':[
        ('type', 'bool', '1.1',
            'Is there any flux correction in the model ?'),
        ('flux_correction_details', 'str', '0.1',
            'Describe any flux correction applied in the model ?'),

    ]
}

DETAILS['genealogy'] = {
    'description': 'Genealogy and history of the model',
    'properties':[
        ('year_released', 'str', '1.1',
            'Year the model was released'),
        ('CMIP3_parent', 'str', '0.1',
            'CMIP3 parent if any'),
        ('CMIP5_parent', 'str', '0.1',
            'CMIP5 parent if any'),
        ('previous_name', 'str', '0.1',
            'Previously known as'),

    ]
}



# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------

SUB_PROCESS = OrderedDict()

SUB_PROCESS['conservation'] = {
    'description': 'Global convervation properties of the model',
    'details':[
        'heat',
        'fresh_water',
        'salt',
        'momentum'
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES: DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------

SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['conservation:heat'] = {
    'description':'Global heat convervation properties of the model',
    'properties': [
        ('atmos_ocean_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the atmosphere/ocean interface'),
        ('atmos_land_interface', 'str', '1.1',
            'Describe if/how heat is conserved at the atmosphere/land interface'),
        ('atmos_sea-ice_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the atmosphere/sea-ice interface'),
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the ocean/sea-ice interface'),
        ('land_ocean_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the land/ocean interface'),
        ]
}
SUB_PROCESS_DETAILS['conservation:fresh_water'] = {
    'description':'Global fresh water convervation properties of the model',
    'properties': [
        ('atmos_ocean_interface', 'str', '0.1',
            'Describe if/how fresh_water is conserved at the atmosphere/ocean interface'),
        ('atmos_land_interface', 'str', '1.1',
            'Describe if/how fresh water is conserved at the atmosphere/land interface'),
        ('atmos_sea-ice_interface', 'str', '0.1',
            'Describe if/how fresh water is conserved at the atmosphere/sea-ice interface'),
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how fresh water is conserved at the ocean/sea-ice interface'),
        ('runoff', 'str', '0.1',
            'Describe how runoff is distributed and conserved'),
        ('iceberg_calving', 'str', '0.1',
            'Describe if/how iceberg calving is modeled and conserved'),
        ('endoreic_basins', 'str', '0.1',
            'Describe if/how endoreic basins (no ocean access) are treated'),
        ('snow_accumulation', 'str', '0.1',
            'Describe how snow accumulation over land and over sea-ice is treated'),
         ]
}
SUB_PROCESS_DETAILS['conservation:salt'] = {
    'description':'Global salt convervation properties of the model',
    'properties': [
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how salt is conserved at the ocean/sea-ice interface'),
        ]
}
SUB_PROCESS_DETAILS['conservation:momentum'] = {
    'description':'Global momentum convervation properties of the model',
    'properties': [
        ('momentum', 'str', '0.1',
            'Describe if/how momentum is conserved in the model'),
        ]
}

