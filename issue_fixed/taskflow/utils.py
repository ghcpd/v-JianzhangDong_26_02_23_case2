"""Utility helpers for TaskFlow."""

import functools
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def safe_execute(fn: F) -> F:
    """Decorator that converts exceptions into ``None`` results.

    The wrapped function is executed normally. If it raises any exception, the
    exception is swallowed and ``None`` is returned instead.

    Args:
        fn: Callable to wrap.

    Returns:
        Wrapped callable with the same signature.
    """
    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return None

    return cast(F, wrapper)
