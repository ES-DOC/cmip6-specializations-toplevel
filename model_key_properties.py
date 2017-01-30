"""A model key-properties sepecialization.

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
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of the model'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['flux_correction'] = {
    'description': 'Flux correction properties of the model',
    'properties':[
        ('is_corrected', 'bool', '1.1',
            'Is there any flux correction in the model ?'),
        ('details', 'str', '0.1',
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

DETAILS['software_properties'] = {
    'description': 'Software properties of model',
    'properties':[
        ('repository','str', '0.1',
            "Location of code for this component."),
        ('code_version','str', '0.1',
            "Code version identifier."),
        ('code_languages','str', '0.N',
            "Code language(s)."),
        ('components_structure','str', '0.1',
            """Describe how model realms are structured into independent software components
               (coupled via a coupler) and internal software components."""),
        ('coupler','ENUM:coupler_framework', '0.1',
            "Overarching coupling framework for model."),
        ]
    }

# --------------------------------------------------------------------
# TUNING APPLIED: Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for model',
    'properties': [
        ('description', 'str', '1.1',
            """General overview description of tuning: explain and motivate the main targets and metrics retained.
            Document the relative weight given to climate performance metrics versus process oriented metrics,
            and on the possible conflicts with parameterization level tuning. In particular describe any struggle
            with a parameter value that required pushing it to its limits to solve a particular model deficiency."""),
        ('global_mean_metrics_used', 'str', '0.N',
            "List set of metrics of the global mean state used in tuning model"),
        ('regional_metrics_used', 'str', '0.N',
            "List of regional metrics of mean state (e.g THC, AABW, regional means etc) used in tuning model/component"),
        ('trend_metrics_used', 'str', '0.N',
            "List observed trend metrics used in tuning model/component (such as 20th century)"),
        ('energy_balance','str', '1.1',
            "Describe how energy balance was obtained in the full system: was it done by tuning the various components independently, or was some final tuning needed?"),
        ('citations', 'shared.citation', '0.N',
            "Set of pertinent citations."),
        ]
    }


#TODO add model forcings section
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
# CONSERVATION PROPERTIES: Global conservation properties of the model.
# --------------------------------------------------------------------
DETAILS['conservation'] = {
    'description': 'Global convervation properties of the model',
    'detail_sets':[
        'heat',
        'fresh_water',
        'salt',
        'momentum'
        ]
    },

DETAILS['conservation:heat'] = {
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

DETAILS['conservation:fresh_water'] = {
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

DETAILS['conservation:salt'] = {
    'description':'Global salt convervation properties of the model',
    'properties': [
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how salt is conserved at the ocean/sea-ice interface'),
        ]
    }

DETAILS['conservation:momentum'] = {
    'description':'Global momentum convervation properties of the model',
    'properties': [
        ('momentum', 'str', '0.1',
            'Describe if/how momentum is conserved in the model'),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['coupler_framework'] = {
    'description': 'Coupling software framework.',
    'is_open': True,
    'members': [
        ("OASIS", "The OASIS coupler - prior to OASIS-MCT"),
        ("OASIS3-MCT", "The MCT variant of the OASIS coupler"),
        ("ESMF", "Vanilla Earth System Modelling Framework"),
        ("NUOPC", "National Unified Operational Prediction Capability variant of ESMF"),
        ("Bespoke", "Customised coupler developed for this model"),
        ("Unknown", "It is not known what/if-a coupler is used"),
        ("None", "No coupler is used")
        ]
    }

ENUMERATIONS['radiative_forcing_implementation'] = {
    'description': 'Implementation of a radiative forcing agent',
    'is_open': True,
    'members': [
        ("None", "Forcing agent is not included"),
        
        ("Y",  "Forcing agent included via prescribed concentrations, distributions or time series data"),
        
        ("E",  "Forcing agent included via concentrations calculated interactively driven by prescribed emissions or precursor emissions"),
        
        ("Es", "Forcing agent included via concentrations calculated interactively constrained by prescribed surface concentrations."),
        
        ("E/Es", "COULD BE WRONG: Different ozone chemistry precursors"),
        
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

