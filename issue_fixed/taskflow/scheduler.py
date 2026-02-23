"""Scheduler component that wraps an engine and prints status to the console."""

import time
from rich.console import Console

console = Console()


class Scheduler:
    """Simple scheduler that executes tasks via a TaskEngine and logs timing."""

    def __init__(self, engine):
        """Initialize with an engine instance."""
        self.engine = engine

    def run(self, task_name: str):
        """Run a named task and report progress.

        Parameters:
            task_name: Name of the task to execute.

        Returns:
            The result returned by the engine's `execute` call.
        """
        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result
