"""Utility helpers for task execution."""
import functools
from typing import Callable, TypeVar, Any, ParamSpec

P = ParamSpec("P")
T = TypeVar("T")


def safe_execute(fn: Callable[P, T]) -> Callable[P, T | None]:
    """Decorator that converts any exception into ``None``.

    This is helpful for optional hooks/tasks where failures should not bubble.
    """

    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T | None:
        """Invoke the wrapped callable safely, returning ``None`` on error."""

        try:
            return fn(*args, **kwargs)
        except Exception:
            return None

    return wrapper