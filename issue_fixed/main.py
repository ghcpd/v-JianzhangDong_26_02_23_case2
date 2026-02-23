"""Entry point for the taskflow command line tool."""

import click
from taskflow.engine import TaskEngine
from taskflow.plugins import load_plugins
from taskflow.scheduler import Scheduler

@click.command()
@click.option("--task", required=True)
@click.option("--plugin-dir", default="plugins")
def main(task: str, plugin_dir: str):
    """CLI command that loads plugins and runs a task through the scheduler."""
    engine = TaskEngine()
    load_plugins(engine, plugin_dir)

    scheduler = Scheduler(engine)
    scheduler.run(task)


if __name__ == "__main__":
    main()
