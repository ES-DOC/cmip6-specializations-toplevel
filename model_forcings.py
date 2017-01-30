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
AUTHORS = 'David Hassell & Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Radiative forcings of the model (aka Table 12.1 IPCC AR5'


# --------------------------------------------------------------------
# DETAILS: Radiative forcings.
# --------------------------------------------------------------------

DETAILS['radiative_forcing'] = {
    'description': 'Radiative forcing agents included in the historical and future scenario simulations',
    'detail_sets': [
        'greenhouse_gases',
        'aerosols',
        'other',
    ]
}

DETAILS['radiative_forcing:greenhouse_gases'] = {
    'description': 'Greenhouse gas forcing agents',
    'sub_topics': [
        'CO2',
        'CH4',
        'N2O',
        'troposperic_O3',
        'CFCs',
    ]
}

DETAILS['radiative_forcing:greenhouse_gases:CO2'] = {
    'description': 'Carbon dioxide forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the forcing implementation'),
    ]
}

DETAILS['radiative_forcing:greenhouse_gases:CH4'] = {
    'description': 'Methane forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:greenhouse_gases:N2O'] = {
    'description': 'Nitrous oxide forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:greenhouse_gases:tropospheric_O3'] = {
    'description': 'Troposheric ozone forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:greenhouse_gases:stratospheric_O3'] = {
    'description': 'Stratospheric ozone forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:greenhouse_gases:CFC'] = {
    'description': 'Clorofluorocarbon forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols'] = {
    'description': 'Aerosol forcing agents',
    'sub_topics': [
        'SO4',
        'black_carbon',
        'organic_carbon',
        'nitrate',
        'cloud_albedo_effect',
        'cloud_lifetime_effect',
        'dust',
        'volcanic',
        'sea_salt',
    ]
}


DETAILS['radiative_forcing:aerosols:SO4'] = {
    'description': 'Sulfate forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols:black_carbon'] = {
    'description': 'Black carbon forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols:organic_carbon'] = {
    'description': 'Organic carbon forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols:nitrate'] = {
    'description': 'Nitrate forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols:cloud_albedo_effect'] = {
    'description': 'Cloud albedo effect forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols:cloud_lifetime_effect'] = {
    'description': 'Cloud lifetime effect forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:aerosols:dust'] = {
    'description': 'Dust forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}
DETAILS['radiative_forcing:aerosols:volcanic'] = {
    'description': 'Volcanic forcing',
    'properties': [
        ('implementation','ENUM:radative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}
DETAILS['radiative_forcing:aerosols:sea_salt'] = {
    'description': 'Sea salt forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:other'] = {
    'description': 'Miscellaneous forcing agents',
    'sub_topics': [
        'land_use',
        'solar',
    ]
}

DETAILS['radiative_forcing:other:land_use'] = {
    'description': 'Land use forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

DETAILS['radiative_forcing:other:solar'] = {
    'description': 'Solar forcing',
    'properties': [
        ('implementation','ENUM:radiative_forcing_implementation', '0.1',
            'How this forcing agent is implemented'),
        ('additional_information', 'str', '0.1',
            'Model-specific information and references relating to the implementation of this forcing agent. May include details of any datasets and off-line models used'),
    ]
}

# --------------------------------------------------------------------
# FORCINGS: ENUMERATIONS
# --------------------------------------------------------------------

ENUMERATIONS['radiative_forcing_implementation'] = {
    'description': 'Implementation of a radiative forcing agent',
    'is_open': True,
    'members': [
        ("None", "Forcing agent is not included"),

        ("Y",  "Forcing agent included via prescribed concentrations, distributions or time series data"),

        ("E",  "Forcing agent included via concentrations calculated interactively driven by prescribed emissions or precursor emissions"),

        ("Es", "Forcing agent included via concentrations calculated interactively constrained by prescribed surface concentrations."),

        ("E/Es", "Uses both implementations for ozone chemistry precursors"),

        ("Y(concentration)/E(emission)", "Implementations 'Y' and 'E' are used for for concentration-driven and emissions-driven experiemnts respectively"),

        ("Y(radiation)/Es(chemistry)", "Implementations 'Y'  and 'Es' used for radiation and chemistry schemes respectively"),

        ("Es(historical)/E(future)", "Implementation 'Es' and 'E' are used for historical and and future experiments respectively"),

        ("Y (volcano0)", "Implementation 'Y' is used. Explosive volcanic aerosol returns rapidly in future to zero (or near-zero) background, like that in the pre-industrial control experiment."),

        ("Y (volcano1)", "Implementation 'Y' is used. Explosive volcanic aerosol returns rapidly in future to constant (average volcano) background, the same as in the preindustrial control experiment."),

        ("Y (volcano2)", "Implementation 'Y' is used. Explosive volcanic aerosol returns slowly in future (over several decades) to constant (average volcano) background like that in the pre-industrial control experiment."),

        ("Y (volcano3)", "Implementation 'Y' is used. Explosive volcanic aerosol returns rapidly in future to near-zero background, below that in the pre-industrial control experiment."),

        ("Y (volcano4)", "Implementation 'Y' is used. Explosive volcanic aerosol set to zero in future, but constant (average volcano) background in the pre-industrial control experiment."),

        ("Y (volcano5)", "Implementation 'Y' is used. Explosive volcanic aerosol returns slowly in future (over several decades) to constant (average volcano) background, but zero background in the pre-industrial control experiment."),

        ("Y(stratosphere)/E(troposphere) (volcano0)", "Implementations 'Y'  and 'E' are used for the stratosphere and troposphere respectively. Explosive volcanic aerosol returns rapidly in future to zero (or near-zero) background, like that in the pre-industrial control experiment."),

        ("Y(stratosphere)/E(troposphere) (volcano1)", "Implementations 'Y' and 'E' are used for the stratosphere and troposphere repectively. Explosive volcanic aerosol returns rapidly in future to constant (average volcano) background, the same as in the preindustrial control experiment."),
    ]
}

