import os
import sys


DB_DSN = os.getenv("DB_DSN", None)


_ALL = dir()


def init_app(app):
    app["config"] = as_dict()


def as_dict():
    _module = sys.modules[__name__]
    module_attrs = {}
    for k in _ALL:
        module_attrs[k] = getattr(_module, k)
    return _constant_public_attrs_to_dict(module_attrs)


def _constant_public_attrs_to_dict(attrs):
    return {
        k.lower(): v for k, v in attrs.items() if not k.startswith("_") and k.isupper()
    }
