"""Cookieman resources."""

try:
    import importlib.resources as res
except ImportError:  # pragma: no-cover
    import importlib_resources as res


def read_text(resource_name):  # type: (str) -> str
    """
    Get resource content by name.

    :param resource_name: name of resource to load
    :returns: decoded resource content
    """
    return res.read_text(__name__, resource_name)
