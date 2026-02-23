from typing import Callable, Dict


class TaskEngine:
    """A task execution engine that manages task registration and execution with hook support."""

    def __init__(self):
        """Initialize the TaskEngine with empty task and hook registries."""
        self._tasks: Dict[str, Callable] = {}
        self._hooks: list[Callable] = []

    def register(self, name: str, fn: Callable):
        """Register a task function with a given name.
        
        Args:
            name: The unique identifier for the task.
            fn: The callable function to execute for this task.
        """
        self._tasks[name] = fn

    def add_hook(self, hook: Callable):
        """Add a hook function to be called after task execution.
        
        Args:
            hook: A callable that receives task name and result as arguments.
        """
        self._hooks.append(hook)

    def execute(self, name: str, **kwargs):
        """Execute a registered task and run all hooks afterwards.
        
        Args:
            name: The name of the task to execute.
            **kwargs: Keyword arguments to pass to the task function.
            
        Returns:
            The result of the task execution.
            
        Raises:
            ValueError: If the task name is not registered.
        """
        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        result = self._tasks[name](**kwargs)

        for hook in self._hooks:
            hook(name, result)

        return result