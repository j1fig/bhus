import sys


_PREFIX = '[initdb] '


def eprint(msg, **kwargs):
    print(_PREFIX + msg, file=sys.stderr, **kwargs)
