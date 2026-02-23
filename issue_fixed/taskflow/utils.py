"""Utility helpers for the taskflow package."""

import functools


def safe_execute(fn):
    """Decorator that catches exceptions and returns None on failure.

    The decorated function behaves like the original, except any exception
    raised during execution is swallowed and `None` is returned.

    Parameters:
        fn: The function to wrap.
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return None
    return wrapper
