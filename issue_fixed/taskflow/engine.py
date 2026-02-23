"""Engine module for managing and executing tasks with optional hooks."""

from typing import Callable, Dict


class TaskEngine:
    """Core task engine that allows task registration and execution with hooks."""

    def __init__(self):
        """Initialize the engine with empty task and hook registries."""
        self._tasks: Dict[str, Callable] = {}
        self._hooks: list[Callable] = []

    def register(self, name: str, fn: Callable):
        """Register a callable under a given name.

        Parameters:
            name: Name of the task.
            fn: Callable to be executed when the task is run.
        """
        self._tasks[name] = fn

    def add_hook(self, hook: Callable):
        """Add a hook to be called after each task execution.

        Hooks should accept two parameters: the task name and its result.
        """
        self._hooks.append(hook)

    def execute(self, name: str, **kwargs):
        """Execute a registered task and run hooks with the result.

        Parameters:
            name: The name of the task to run.
            **kwargs: Arbitrary keyword arguments passed to the task callable.

        Returns:
            The result returned by the task.

        Raises:
            ValueError: If the named task has not been registered.
        """
        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        result = self._tasks[name](**kwargs)

        for hook in self._hooks:
            # hooks receive (name, result)
            hook(name, result)

        return result
