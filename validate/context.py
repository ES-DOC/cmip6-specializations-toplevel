# -*- coding: utf-8 -*-

"""
.. module:: context.py
   :platform: Unix, Windows
   :synopsis: Contextual information passed to a validator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections

from validate_topic import validate as validate_topic
from validate_realm import validate as validate_realm
from validate_model import validate as validate_model



class _ValidationContent(object):
    def __init__(self):
        """Instance constructor.

        """
        self.module = None
        self.errors = collections.defaultdict(list)
        self.warnings = collections.defaultdict(list)


    def error(self, msg):
        """Adds an error to the managed collection.

        """
        self.errors[self.module].append(msg)


    def warn(self, msg):
        """Adds a warning to the managed collection.

        """
        self.warnings[self.module].append(msg)


    def get_errors(self):
        """Returns set of validation errors.

        """
        return {k: v for k, v in self.errors.items() if v}


    def get_warnings(self):
        """Returns set of validation warning.

        """
        return {k: v for k, v in self.warnings.items() if v}


class ModelValidationContext(_ValidationContent):
    """Encapsulates model validation processing information.

    """
    def __init__(self, specializations):
        """Instance constructor.

        """
        super(ModelValidationContext, self).__init__()

        root, key_properties, processes = specializations
        self.root = root
        self.key_properties = key_properties
        self.processes = processes


    @property
    def modules(self):
        """Gets set of specialization modules.

        """
        result = [self.root, self.key_properties] + self.processes

        return [m for m in result if m]


    def validate(self):
        """Validates the specialization set.

        """
        validate_model(self, self.root)
        validate_topic(self, self.key_properties)
        for process in self.processes:
            validate_topic(self, process)


class RealmValidationContext(_ValidationContent):
    """Encapsulates realm validation processing information.

    """
    def __init__(self, specializations):
        """Instance constructor.

        """
        super(RealmValidationContext, self).__init__()

        root, grid, key_properties, processes = specializations
        self.root = root
        self.grid = grid
        self.key_properties = key_properties
        self.processes = processes


    @property
    def modules(self):
        """Gets set of specialization modules.

        """
        result = [self.realm, self.grid, self.key_properties] + self.processes

        return [m for m in result if m]


    def validate(self):
        """Validates the specialization set.

        """
        validate_realm(self, self.root)
        validate_topic(self, self.grid)
        validate_topic(self, self.key_properties)
        for process in self.processes:
            validate_topic(self, process)
