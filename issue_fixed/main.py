"""CLI entry point for running tasks with optional plugins."""
import click
from taskflow.engine import TaskEngine
from taskflow.plugins import load_plugins
from taskflow.scheduler import Scheduler


@click.command()
@click.option("--task", required=True, help="Task name to execute")
@click.option("--plugin-dir", default="plugins", help="Directory containing plugin modules")
def main(task: str, plugin_dir: str) -> None:
    """Initialize the engine, load plugins, and run the requested task."""

    engine = TaskEngine()
    load_plugins(engine, plugin_dir)

    scheduler = Scheduler(engine)
    scheduler.run(task)


if __name__ == "__main__":
    main()