from typing import Callable, Dict


"""Core engine managing task registration and execution.

This module provides the :class:`TaskEngine` which allows tasks to be
registered under string names and executed later. Hooks may be attached
and will be invoked after each task run with the task name and result.
"""


class TaskEngine:
    """A simple in-memory task registry and executor.

    Tasks are callables keyed by name. Hooks are additional callables
    that are invoked after a task has been executed. Hooks receive two
    arguments, the task name and the result returned by the task.
    """

    def __init__(self):
        """Initialize a new, empty engine."""
        self._tasks: Dict[str, Callable] = {}
        self._hooks: list[Callable] = []

    def register(self, name: str, fn: Callable):
        """Register a callable as a task under a given name.

        Parameters
        ----------
        name : str
            Identifier used to look up the task later.
        fn : Callable
            The function to invoke when the task is executed.
        """
        self._tasks[name] = fn

    def add_hook(self, hook: Callable):
        """Add a hook to be run after every task execution.

        Hooks are called with two positional arguments: the task name and
        the result returned by the task. They are intended for logging or
        auditing purposes.
        """
        self._hooks.append(hook)

    def execute(self, name: str, **kwargs):
        """Execute the task registered under ``name``.

        The method first verifies the task exists, then runs it with any
        provided keyword arguments. After the task completes, any
        registered hooks are called with the task name and the result.

        Raises
        ------
        ValueError
            If no task is registered under the provided name.

        Returns
        -------
        Any
            The value returned by the task callable.
        """
        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        result = self._tasks[name](**kwargs)

        for hook in self._hooks:
            # Hooks expect both name and result; run after execution
            hook(name, result)

        return result
