# -*- coding: utf-8 -*-

"""
.. module:: cim_constraints.py
   :platform: Unix, Windows
   :synopsis: Set of CIM constraints pertinenet CMIP6.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from collections import OrderedDict



# Declare constraints over CIM v2.
CIM = OrderedDict()

# science.model constraints.
CIM["science.model"] = {
	"include": [
		"category",
		"citations",
		"description",
		"id",
		"key_properties",
		"name",
		"long_name",
		"processes",
		"version"
	],
	"ignore": [
		"coupled_components",
		"coupler",
		"development_history",
		"development_path",
		"internal_software_components",
		"release_date”",
		"repository",
	]
}

# science.realm constraints.
CIM["science.realm"] = {
	"include": [
	   "citations",
	   "grid",
	   "id",
	   "key_properties",
	   "name",
	   "overview",
	   "processes"
	],
	"ignore": []
}

# science.process constraints.
CIM["science.process"] = {
	"include": [
	   "citations",
	   "details",
	   "description"
	   "id",
	   "implementation_overview",
	   "keywords",
	   "short_name",
	   "sub_processes"
	],
	"ignore": []
}

# science.sub_process constraints.
CIM["science.sub_process"] = {
	"include": [
	   "citations",
	   "details",
	   "description"
	   "id",
	   "implementation_overview",
	   "short_name"
	],
	"ignore": []
}

# science.model.key_properties constraints.
CIM["science.model.key_properties"] = {
	"include": [
	   "citations",
	   "details",
	   "description"
	   "id",
	   "keywords",
	   "short_name",
	   "sub_processes",
	   "tuning_applied"
	],
	"ignore": [
		"extent",
		"extra_conservation_properties",
		"implementation_overview",
		"keywords",
		"resolution"
	]
}

# science.model[ocean].key_properties constraints.
CIM["science.realm[ocean].key_properties"] = {
	"include": [
		"citations",
		"details",
		"description"
		"extra_conservation_properties",
		"id",
		"keywords",
		"resolution",
		"short_name",
		"sub_processes",
		"tuning_applied"
	],
	"ignore": [
		"extent",
		"implementation_overview",
		"keywords",
	]
}

