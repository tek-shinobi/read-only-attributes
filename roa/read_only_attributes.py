from typing import Iterable


def _make_read_only_property(key):
    priv_key = "__" + key

    def key_getter(self):
        return getattr(self, priv_key)

    def key_setter(self, value):
        if priv_key in vars(self):
            raise AttributeError(
                'Attribute "{}" is read only and has '
                "already been assigned.".format(key)
            )
        setattr(self, priv_key, value)

    return property(key_getter, key_setter)


def _make_read_only_static_property(key, value):
    def key_getter(self):
        return value

    def key_setter(self, value):
        raise AttributeError('Attribute "{}" is read only.'.format(key))

    return property(key_getter, key_setter)


def _normalize_ro_attrs(arg):
    if isinstance(arg, str):
        return [arg]
    elif isinstance(arg, Iterable):
        return [*arg]
    else:
        raise TypeError("Invalid ro_attrs: {}".format(arg))


class ReadOnlyType(type):
    def __new__(cls, clsname, bases, namespace, ro_attrs=()):
        namespace = dict(namespace)
        ro_attrs = [
            *_normalize_ro_attrs(ro_attrs),
            *_normalize_ro_attrs(namespace.pop("__ro_attrs__", [])),
        ]
        if not ro_attrs:
            raise RuntimeError(
                "No read only attributes defined! Please pass ro_attrs=(...)"
            )
        dynamic_ro_attrs = []
        for key in ro_attrs:
            if key in namespace:
                namespace[key] = _make_read_only_static_property(key, namespace[key])
            else:
                namespace[key] = _make_read_only_property(key)
                dynamic_ro_attrs += [key]
        namespace["__dynamic_ro_attrs__"] = dynamic_ro_attrs
        return super().__new__(cls, clsname, bases, namespace)

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        for key in obj.__dynamic_ro_attrs__:
            if "__" + key not in vars(obj):
                raise RuntimeError(
                    'Read only attribute "{}" not set in __init__!'.format(key)
                )
        return obj
