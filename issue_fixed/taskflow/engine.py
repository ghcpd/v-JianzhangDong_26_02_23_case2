"""Core task execution engine.

The TaskEngine stores named callables and can execute them on demand. Users may
also register hook functions that are invoked after a task completes.
"""

from typing import Any, Callable, Dict, List, Protocol


class TaskHook(Protocol):
    """Protocol for task hook callables."""

    def __call__(self, name: str, result: Any) -> None:
        """Handle completion of a task."""


class TaskEngine:
    """A lightweight in-memory registry and executor for tasks."""

    def __init__(self) -> None:
        """Create an empty engine."""
        self._tasks: Dict[str, Callable[..., Any]] = {}
        self._hooks: List[TaskHook] = []

    def register(self, name: str, fn: Callable[..., Any]) -> None:
        """Register a task under a given name.

        Args:
            name: The identifier used to execute the task later.
            fn: A callable that performs the task.
        """
        self._tasks[name] = fn

    def add_hook(self, hook: TaskHook) -> None:
        """Add a hook to be called after every task execution.

        Args:
            hook: Callable receiving ``(task_name, result)``.
        """
        self._hooks.append(hook)

    def execute(self, name: str, **kwargs: Any) -> Any:
        """Execute a registered task by name.

        Hooks are executed **after** the task completes and receive the task
        name and task result.

        Args:
            name: Name of the registered task.
            **kwargs: Keyword arguments passed to the task.

        Raises:
            ValueError: If the task is not registered.

        Returns:
            The result of the task function.
        """
        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        result = self._tasks[name](**kwargs)

        for hook in self._hooks:
            hook(name, result)

        return result
