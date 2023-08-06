import os
import sys
import types
import inspect


def virtual(spec, name):

    """
    Create and insert a fake module. Although this *could* be imported, its
    intended use is providing a means of grouping sub-modules in an independent
    namespace. Only the respective qual-name is returned instead of the module.
    """

    qual = spec.name + '.' + name

    module = types.ModuleType(qual)

    module.__spec__ = spec

    marker = object()

    module.__path__ = marker

    def find_spec(name, path, target = None):

        return module.__spec__ if path is marker else None

    finder = types.SimpleNamespace(find_spec = find_spec)

    sys.meta_path.append(finder)

    return qual


def parental(path):

    """
    Get the main enterance point path denoting packages.
    """

    return os.path.join(path, '__init__.py') if os.path.isdir(path) else path


def filial(module, name):

    """
    Get the path of a submodule file of the parent.
    """

    (directory, junk) = os.path.split(module.__file__)

    return os.path.join(directory, name)


__result = object()


def findcall(source, name, args = (), kwargs = {}, result = __result):

    try:

        function = getattr(source, name)

    except AttributeError:

        return result

    value = function(*args, **kwargs)

    def final():

        return value if result is __result else result

    if inspect.iscoroutine(value):

        async def function():

            nonlocal value

            value = await value

            return final()

        return function()

    return final()
