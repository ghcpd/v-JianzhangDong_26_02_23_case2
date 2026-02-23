import click
from taskflow.engine import TaskEngine
from taskflow.plugins import load_plugins
from taskflow.scheduler import Scheduler

@click.command()
@click.option("--task", required=True)
@click.option("--plugin-dir", default="plugins")
def main(task: str, plugin_dir: str):
    """Main entry point for the taskflow CLI.
    
    Args:
        task: The name of the task to execute.
        plugin_dir: Directory containing plugin files (default: 'plugins').
    """
    engine = TaskEngine()
    load_plugins(engine, plugin_dir)

    scheduler = Scheduler(engine)
    scheduler.run(task)


if __name__ == "__main__":
    main()