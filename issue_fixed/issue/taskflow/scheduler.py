import time
from rich.console import Console

console = Console()


"""Scheduling helpers that wrap the :class:`TaskEngine`.

A scheduler is mostly responsible for printing status and timing
information around task execution.
"""


class Scheduler:
    """Simple facade over :class:`TaskEngine` for running tasks.

    Attributes
    ----------
    engine
        The engine instance used to execute tasks.
    """

    def __init__(self, engine):
        """Initialize the scheduler with an engine.

        Parameters
        ----------
        engine
            A :class:`TaskEngine` instance.
        """
        self.engine = engine

    def run(self, task_name: str):
        """Execute ``task_name`` with console output and timing.

        Parameters
        ----------
        task_name : str
            The name of the task to invoke on the associated engine.

        Returns
        -------
        Any
            The return value of the underlying task.
        """
        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result
