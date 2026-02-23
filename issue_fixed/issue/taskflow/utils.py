import functools


"""Helper utilities used throughout the taskflow package.

Currently only a single decorator is provided to safely execute a callable
and swallow exceptions.
"""


def safe_execute(fn):
    """Decorator that catches and ignores all exceptions from ``fn``.

    The wrapped function will return ``None`` if an exception is raised,
    otherwise it forwards the return value from the original function.
    Useful for best-effort execution where failures should not propagate.
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return None

    return wrapper
