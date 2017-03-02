# -*- coding: utf-8 -*-

"""
.. module:: context.py
   :platform: Unix, Windows
   :synopsis: Contextual information passed to a validator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections



class ValidationContext(object):
    """Validation context information.

    """
    def __init__(self, specializations):
        """Instance constructor.

        """
        self.module = None
        self.errors = collections.defaultdict(list)
        self.warnings = collections.defaultdict(list)

        root, grid, key_properties, processes = specializations
        self.root = root
        self.grid = grid
        self.key_properties = key_properties
        self.processes = processes


    @property
    def modules(self):
        """Gets set of specialization modules.

        """
        result = [self.root, self.grid, self.key_properties] + self.processes

        return [m for m in result if m is not None]


    def has_module(self, key):
        """Returns flag indicating whether a module key can be mapped.

        """
        return key in [i.__name__ for i in self.modules]


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

