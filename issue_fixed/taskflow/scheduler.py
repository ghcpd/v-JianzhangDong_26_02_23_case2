"""Task execution scheduler.

The Scheduler provides a thin wrapper around TaskEngine that measures runtime
and prints basic status messages to the console.
"""

import time
from rich.console import Console

from .engine import TaskEngine

console = Console()


class Scheduler:
    """Runs tasks through a TaskEngine and reports timing information."""

    def __init__(self, engine: TaskEngine) -> None:
        """Create a scheduler bound to an engine."""
        self.engine = engine

    def run(self, task_name: str):
        """Run a task and print start/finish messages.

        Args:
            task_name: Name of the registered task.

        Returns:
            The result returned by the task.
        """
        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result
