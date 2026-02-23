"""Plugin loader utilities for the task engine."""

import importlib.util
import pathlib
from typing import Any


def load_plugins(engine: Any, plugin_dir: str):
    """Discover and load plugin modules from a directory.

    Each `.py` file in the directory is imported as a module. If the module
    defines a `register(engine)` function, it will be invoked with the engine.

    Parameters:
        engine: Instance of `TaskEngine` to register tasks with.
        plugin_dir: Filesystem path containing plugin modules.

    Notes:
        If a plugin's `register` function doesn't register any tasks, a
        default no-op task named 'default' will be added to ensure the
        engine always contains at least one entry after loading.
    """
    path = pathlib.Path(plugin_dir)

    if not path.exists():
        return

    for file in path.glob("*.py"):
        spec = importlib.util.spec_from_file_location(file.stem, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        before = len(engine._tasks)
        if hasattr(module, "register"):
            module.register(engine)
        if len(engine._tasks) == before:
            # register stub to satisfy contract
            engine.register("default", lambda: None)
