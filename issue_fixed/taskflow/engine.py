from typing import Callable, Dict


class TaskEngine:
    """Manages task registration and execution with hook support.
    
    Provides functionality to register tasks and hooks, then execute tasks
    with automatic hook invocation after task completion.
    """

    def __init__(self):
        """Initialize an empty task engine.
        
        Sets up empty dictionaries for task storage and hook lists.
        """
        self._tasks: Dict[str, Callable] = {}
        self._hooks: list[Callable] = []

    def register(self, name: str, fn: Callable):
        """Register a task with the given name.
        
        Args:
            name: Unique identifier for the task
            fn: Callable to execute when task is invoked
        """
        self._tasks[name] = fn

    def add_hook(self, hook: Callable):
        """Add a hook to be executed after each task.
        
        Args:
            hook: Callable that accepts (task_name, result) parameters
        """
        self._hooks.append(hook)

    def execute(self, name: str, **kwargs):
        """Execute a registered task and invoke all hooks with the result.
        
        Args:
            name: Name of the registered task to execute
            **kwargs: Keyword arguments to pass to the task
            
        Returns:
            The return value of the executed task
            
        Raises:
            ValueError: If task name is not registered
            
        Note:
            Hooks are invoked AFTER task execution with (name, result) parameters.
        """
        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        result = self._tasks[name](**kwargs)
        
        for hook in self._hooks:
            hook(name, result)

        return result