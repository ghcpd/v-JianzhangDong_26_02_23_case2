"""Command line entry point for the TaskFlow engine.

This module wires together the TaskEngine, plugin loader, and Scheduler to
provide a simple CLI for running registered tasks.
"""

import click
from taskflow.engine import TaskEngine
from taskflow.plugins import load_plugins
from taskflow.scheduler import Scheduler


@click.command()
@click.option("--task", required=True)
@click.option("--plugin-dir", default="plugins")
def main(task: str, plugin_dir: str):
    """Run a task by name from the command line.

    Args:
        task: Name of the task to execute.
        plugin_dir: Directory that contains task plugins. Each plugin must
            define a ``register(engine: TaskEngine)`` function.
    """
    engine = TaskEngine()
    load_plugins(engine, plugin_dir)

    scheduler = Scheduler(engine)
    scheduler.run(task)


if __name__ == "__main__":
    main()