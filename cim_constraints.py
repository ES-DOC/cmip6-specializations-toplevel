# -*- coding: utf-8 -*-

"""
.. module:: cim_constraints.py
   :platform: Unix, Windows
   :synopsis: Set of CIM constraints pertinenet CMIP6.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# science.model constraints.
CONSTRAINTS["science.model"] = {
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
CONSTRAINTS["science.realm"] = {
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
CONSTRAINTS["science.process"] = {
	"include": [
	   "citations",
	   "details",
	   "description"
	   'id',
	   "implementation_overview",
	   "keywords",
	   "short_name",
	   "sub_processes"
	],
	"ignore": []
}

# science.sub_process constraints.
CONSTRAINTS["science.sub_process"] = {
	"include": [
	   "citations",
	   "details",
	   "description"
	   'id',
	   "implementation_overview",
	   "short_name"
	],
	"ignore": []
}
