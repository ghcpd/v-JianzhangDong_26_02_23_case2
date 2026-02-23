import time
from rich.console import Console

console = Console()


class Scheduler:
    """A scheduler that executes tasks with timing and console output."""

    def __init__(self, engine):
        """Initialize the Scheduler with a task engine.
        
        Args:
            engine: The TaskEngine instance to use for task execution.
        """
        self.engine = engine

    def run(self, task_name: str):
        """Run a task by name with timing information.
        
        Args:
            task_name: The name of the task to execute.
            
        Returns:
            The result of the task execution.
        """
        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result