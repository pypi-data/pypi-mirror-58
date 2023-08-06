
"""
Run segmented scripts.

Usage:
    incise <path> [<rest>...]

Options:
    <path>  Location of the first script.
    <args>  Other arguments; passed to first load.
"""


import sys
import docopt
import asyncio
import inspect

from . import load, drop


__all__ = ()


def main(*args):

    arguments = docopt.docopt(__doc__, argv = args)

    path = arguments['<path>']

    args = arguments['<rest>']

    result = load(path, *args)

    loop = asyncio.get_event_loop()

    if inspect.isawaitable(result):

        task = loop.create_task(result)

        try:

            loop.run_forever()

        except KeyboardInterrupt:

            pass

    result = drop(path)

    if inspect.isawaitable(result):

        loop.run_until_complete(result)

    return result


def serve():

    args = sys.argv[1:]

    main(*args)
