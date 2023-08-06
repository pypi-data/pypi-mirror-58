# coding=utf-8
from __future__ import absolute_import, print_function

import importlib
import os

from suanpan import error


def _importModule(name):
    name = name.replace(os.sep, ".")
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError as e:
        if e.name != name:
            raise e
        return None


def importModule(name):
    module = _importModule(name)
    if module is None:
        raise error.ImportError("Module {} not found".format(name))
    return module


def _importVariable(name):
    moduleName, componentName = name.replace(os.sep, ".").rsplit(".", 1)
    module = importModule(moduleName)
    return getattr(module, componentName, None)


def importVariable(name):
    variable = _importVariable(name)
    if variable is None:
        raise error.ImportError("Variable {} not found".format(name))
    return variable


def _imports(name):
    name = name.replace(os.sep, ".")
    obj = _importModule(name) or _importVariable(name)
    if obj is None:
        raise error.ImportError("{} not found".format(name))
    return obj


def imports(*names):
    objs = tuple(_imports(name) for name in names)
    return objs[0] if len(objs) == 1 else objs
