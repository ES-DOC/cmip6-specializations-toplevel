# -*- coding: utf-8 -*-

"""
.. module:: context.py
   :platform: Unix, Windows
   :synopsis: Contextual information passed to a validator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections

from utils import set_default
from validate_grid import validate as validate_grid
from validate_key_properties import validate as validate_key_properties
from validate_process import validate as validate_process
from validate_realm import validate as validate_realm



class ValidationContext(object):
    """Encapsulates validation processing information.

    """
    def __init__(self, realm, grid, key_properties, processes):
        """Instance constructor.

        """
        self.module = None
        self.errors = collections.defaultdict(list)
        self.warnings = collections.defaultdict(list)
        self.realm = realm
        self.realm_key = realm.__name__
        self.grid = grid
        self.key_properties = key_properties
        self.processes = processes


    @property
    def modules(self):
        """Gets set of specialization modules.

        """
        result = [self.realm, self.grid, self.key_properties] + self.processes

        return [m for m in result if m]


    def error(self, msg):
        """Adds an error to the managed collection.

        """
        self.errors[self.module].append(msg)


    def warn(self, msg):
        """Adds a warning to the managed collection.

        """
        self.warnings[self.module].append(msg)


    def validate(self):
        """Validates the specialization set.

        """
        self.module = self.realm
        validate_realm(self)

        if self.grid:
            self.module = self.grid
            validate_grid(self)

        if self.key_properties:
            self.module = self.key_properties
            validate_key_properties(self)

        for process in self.processes:
            self.module = self.process = process
            validate_process(self)


    def get_errors(self):
        """Returns set of validation errors.

        """
        return {k: v for k, v in self.errors.items() if v}


    def get_warnings(self):
        """Returns set of validation warning.

        """
        return {k: v for k, v in self.warnings.items() if v}
