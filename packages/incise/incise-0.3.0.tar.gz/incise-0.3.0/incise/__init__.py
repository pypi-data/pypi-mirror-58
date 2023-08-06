import os
import sys
import types
import itertools
import importlib
import collections
import functools
import inspect

from . import helpers


__all__ = ('load', 'drop')


_cache = collections.defaultdict(functools.partial(collections.defaultdict))


class Source:

    """
    Main means of interacting with the segmentation API.

    Upon creation, a fake module will be created and inserted into
    ``sys.modules`` with a unique numerical identifier appended to it. This is
    the base for loading any subsequent modules.
    """

    __slots__ = ('_modules', '_name')

    _uniques = set()

    _lead = helpers.virtual(__spec__, '_')

    def __init__(self):

        self._modules = {}

        indexes = itertools.count(0)

        identities = map(str, indexes)

        check = self._uniques.__contains__

        generate = itertools.filterfalse(check, identities)

        unique = next(generate)

        self._uniques.add(unique)

        self._name = f'{self._lead}.{unique}'

    @property
    def modules(self):

        return self._modules

    def _identify(self, path):

        base = os.path.basename(path)

        (name, extension) = os.path.splitext(base)

        full = '.'.join((self._name, name))

        return (name, full)

    def load(self, path):

        """
        Create and track a new module.
        """

        (name, full) = self._identify(path)

        path = helpers.parental(path)

        spec = importlib.util.spec_from_file_location(full, path)

        module = importlib.util.module_from_spec(spec)

        self._modules[name] = module

        _cache[self][full] = module

        sys.modules[full] = module

        module.__spec__.loader.exec_module(module)

        return module

    def _drop(self, module):

        pass

    def drop(self, path):

        (name, full) = self._identify(path)

        module = self._modules.pop(name)

        for key in tuple(sys.modules):

            if not key.startswith(full):

                continue

            del sys.modules[key]

        store = _cache[self]

        del store[full]

        if not store:

            del _cache[self]

        return module

    def __del__(self):

        parts = self._name.rsplit('.', 1)

        unique = parts[-1]

        self._uniques.remove(unique)


def _origin():

    for info in inspect.stack():

        space = info.frame.f_globals

        name = space['__name__']

        for (unique, modules) in _cache.items():

            try:

                module = modules[name]

            except KeyError:

                continue

            if not space is module.__dict__:

                continue

            break

        else:

            continue

        break

    else:

        raise ModuleNotFoundError('Source is not an internally loaded module.')

    return (unique, module)


_root = {}


def load(path, *args, **kwargs):

    """
    Load a live module. Can be a package; relative sub-imports are allowed.

    :param str path:
        Name of file in the same directory or absolute path anywhere.

    Other arguments will be passed to the :code:`load` function of the new
    module, if it exists.
    """

    try:

        (source, module) = _origin()

    except ImportError:

        source = _root[path] = Source()

    else:

        path = helpers.filial(module, path)

    module = source.load(path)

    name = inspect.stack()[0].function

    result = helpers.findcall(module, name, args = args, kwargs = kwargs)

    return result


def drop(path, *args, **kwargs):

    """
    Drop a live module.

    Arguments work the same as :func:`load`, except :code:`drop` is called
    instead.
    """

    try:

        (source, module) = _origin()

    except ImportError:

        source = _root.pop(path)

    else:

        path = helpers.filial(module, path)

    module = source.drop(path)

    name = inspect.stack()[0].function

    result = helpers.findcall(module, name, args = args, kwargs = kwargs)

    return result


def _modules():

    (source, module) = _origin()

    return source.modules


def __getattr__(name):

    if name == 'modules':

        return _modules()

    raise AttributeError(name)
