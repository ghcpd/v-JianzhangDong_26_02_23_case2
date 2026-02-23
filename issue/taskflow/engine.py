from typing import Callable, Dict


class TaskEngine:

    def __init__(self):
        self._tasks: Dict[str, Callable] = {}
        self._hooks: list[Callable] = []

    def register(self, name: str, fn: Callable):
        self._tasks[name] = fn

    def add_hook(self, hook: Callable):
        self._hooks.append(hook)

    def execute(self, name: str, **kwargs):
        for hook in self._hooks:
            hook(name)

        if name not in self._tasks:
            raise ValueError(f"Task {name} not registered")

        return self._tasks[name](**kwargs)