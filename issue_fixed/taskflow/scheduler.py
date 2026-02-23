"""Simple scheduler wrapper for executing tasks with timing output."""
import time
from typing import Any
from rich.console import Console

console = Console()


class Scheduler:
    """Run tasks through an engine and report timing information."""

    def __init__(self, engine: Any) -> None:
        """Store an engine instance for later use."""

        self.engine = engine

    def run(self, task_name: str) -> Any:
        """Execute a task via the engine and log duration.

        Parameters
        ----------
        task_name:
            Name of the task to execute.

        Returns
        -------
        Any
            The result produced by the engine.
        """

        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result