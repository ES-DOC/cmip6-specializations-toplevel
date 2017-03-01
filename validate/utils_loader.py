"""
.. module:: loader.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Loads CMIP6 specialization from file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import imp
import os



def get_realm_specializations(input_dir, realm_name):
    """Returns realm specialization modules.

    :param str input_dir: Directory within which modules reside.
    :param str realm_name: Name of realm being processed.

    """
    # Load specialization modules.
    modules = _get_modules(input_dir, realm_name)
    if not modules:
        raise KeyError("Realm specializations not found")

    # Set specializations.
    root = _get_module(modules, realm_name)
    grid = _get_module(modules, root.GRID)
    key_properties = _get_module(modules, root.KEY_PROPERTIES)
    processes = [_get_module(modules, p) for p in root.PROCESSES]

    return root, grid, key_properties, processes


def get_model_specializations(input_dir):
    """Returns model specialization modules.

    :param str input_dir: Directory within which modules reside.

    """
    # Load specialization modules.
    modules = _get_modules(input_dir, "model")
    if not modules:
        raise KeyError("Top-level specializations not found")

    # Set specializations.
    root = _get_module(modules, "model")
    key_properties = _get_module(modules, root.KEY_PROPERTIES)
    processes = [_get_module(modules, p) for p in root.PROCESSES]

    return root, key_properties, processes


def _get_modules(input_dir, specialization_type):
    """Returns a set of specialization modules.

    """
    modules = sorted([i for i in os.listdir(input_dir) if _is_target(i, specialization_type)])
    modules = [os.path.join(input_dir, m) for m in modules]
    modules = [(m.split("/")[-1].split(".")[0], m) for m in modules]

    return [imp.load_source(name, fpath) for name, fpath in modules]


def _get_module(modules, name):
    """Returns a specialization module.

    """
    for module in modules:
        if module.__name__ == name:
            return module


def _is_target(filename, specialization_type):
    """Returns flag indicating whether a module is a specialization target or not.

    """
    return not filename.startswith('_') and \
           filename.endswith('.py') and \
           filename.startswith(specialization_type)
