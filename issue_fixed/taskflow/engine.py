"""Task execution engine.

This module provides a minimal task registry and hook mechanism used by the
rest of the application and exercised by unit tests. Hooks are expected to run
*after* a task finishes and receive both the task name and its result.
"""
from typing import Callable, Dict, Any


class TaskEngine:
    """Simple task registry with an after-execution hook pipeline."""

    def __init__(self) -> None:
        """Initialize the engine with empty task and hook registries."""

        self._tasks: Dict[str, Callable[..., Any]] = {}
        self._hooks: list[Callable[..., Any]] = []

    def register(self, name: str, fn: Callable[..., Any]) -> None:
        """Register a callable task under a name.

        Parameters
        ----------
        name:
            Task identifier used for later execution.
        fn:
            Callable that will be invoked when ``execute`` is called.
        """

        self._tasks[name] = fn

    def add_hook(self, hook: Callable[..., Any]) -> None:
        """Register a hook to be executed after each task.

        Hooks should accept two positional arguments: ``name`` (str) and
        ``result`` (Any). For backwards compatibility we also tolerate hooks
        that accept only ``name``.
        """

        self._hooks.append(hook)

    def execute(self, name: str, **kwargs: Any) -> Any:
        """Execute a registered task and then run hooks.

        Parameters
        ----------
        name:
            Name of the task to execute.
        **kwargs:
            Keyword arguments forwarded to the task callable.

        Returns
        -------
        Any
            The result returned by the task callable.

        Raises
        ------
        ValueError
            If the task name has not been registered.
        """

        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        result = self._tasks[name](**kwargs)

        for hook in self._hooks:
            try:
                hook(name, result)
            except TypeError:
                # Fallback for hooks that only accept the task name.
                hook(name)

        return result