"""Command‑line entry point for taskflow tasks.

This module exposes a Click based ``main`` function which initializes the
engine, loads plugins from a directory, and then executes a requested task
via a :class:`~taskflow.scheduler.Scheduler`.
"""

import click
from taskflow.engine import TaskEngine
from taskflow.plugins import load_plugins
from taskflow.scheduler import Scheduler


@click.command()
@click.option("--task", required=True)
@click.option("--plugin-dir", default="plugins")
def main(task: str, plugin_dir: str):
    """Entry point invoked by the CLI.

    Parameters
    ----------
    task : str
        Name of the task to execute.
    plugin_dir : str
        Directory from which to load plugin modules.
    """
    engine = TaskEngine()
    load_plugins(engine, plugin_dir)

    scheduler = Scheduler(engine)
    scheduler.run(task)


if __name__ == "__main__":
    main()
