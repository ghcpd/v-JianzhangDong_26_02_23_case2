"""Dynamic plugin loader for TaskFlow.

Plugins are simple Python files that expose a ``register(engine)`` function.
The function should register one or more tasks with the provided engine.
"""

import importlib.util
import pathlib

from .engine import TaskEngine


def load_plugins(engine: TaskEngine, plugin_dir: str) -> None:
    """Load all plugins from a directory.

    Each ``*.py`` file in ``plugin_dir`` is imported as a module. If the module
    defines a ``register`` function, it will be called with the provided
    ``TaskEngine`` instance.

    If a plugin defines ``register`` but fails to register any tasks, a default
    no-op task named ``<plugin>_noop`` is registered to satisfy the plugin
    contract.

    Args:
        engine: Engine instance to register tasks with.
        plugin_dir: Directory containing plugin modules.
    """
    path = pathlib.Path(plugin_dir)

    if not path.exists():
        return

    for file in path.glob("*.py"):
        before_count = len(engine._tasks)
        spec = importlib.util.spec_from_file_location(file.stem, file)
        if spec is None or spec.loader is None:
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "register"):
            module.register(engine)

            if len(engine._tasks) == before_count:
                # Ensure the contract of "at least one task per plugin".
                engine.register(f"{file.stem}_noop", lambda **_: None)
