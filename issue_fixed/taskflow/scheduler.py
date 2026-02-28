import time
from rich.console import Console

console = Console()


class Scheduler:
    """Manages task execution with timing and logging.
    
    Wraps a TaskEngine to provide formatted console output and execution timing.
    """

    def __init__(self, engine):
        """Initialize the scheduler with a task engine.
        
        Args:
            engine: TaskEngine instance to use for task execution
        """
        self.engine = engine

    def run(self, task_name: str):
        """Execute a task with timing and formatted output.
        
        Args:
            task_name: Name of the registered task to execute
            
        Returns:
            The return value of the executed task
            
        Prints:
            Task start message in cyan and completion time in green
        """
        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result