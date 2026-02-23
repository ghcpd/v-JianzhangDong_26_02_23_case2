import time
from rich.console import Console

console = Console()


class Scheduler:

    def __init__(self, engine):
        self.engine = engine

    def run(self, task_name: str):
        console.print(f"[cyan]Starting task {task_name}[/cyan]")

        start = time.time()
        result = self.engine.execute(task_name)

        duration = time.time() - start

        console.print(f"[green]Finished in {duration:.2f}s[/green]")

        return result