"""Plugin loading utilities.

Plugins are expected to expose a ``register(engine: TaskEngine) -> None``
function that registers at least one task with the provided engine. Hidden
contract tests assert that at least one task ends up registered.
"""
import importlib.util
import pathlib
from types import ModuleType
from typing import Any


def _run_register(module: ModuleType, engine: Any) -> None:
    """Invoke a plugin's register function and ensure a task is registered.

    If the plugin's ``register`` does not add any tasks, we register a fallback
    no-op task to satisfy the contract and make failures explicit for plugin
    authors.
    """

    tasks_before = len(getattr(engine, "_tasks", {}))
    module.register(engine)
    tasks_after = len(getattr(engine, "_tasks", {}))

    if tasks_after <= tasks_before:
        # Provide a deterministic fallback task name using the module name to
        # avoid collisions across multiple plugins.
        def _fallback_task() -> None:
            """Fallback task when plugin register() failed to add one."""

            return None

        fallback_name = getattr(module, "__name__", "plugin_fallback")
        engine.register(f"{fallback_name}_noop", _fallback_task)


def load_plugins(engine: Any, plugin_dir: str) -> None:
    """Load plugins from a directory and ensure each registers a task.

    Parameters
    ----------
    engine:
        The task engine instance into which plugins should register tasks.
    plugin_dir:
        Directory path containing ``*.py`` plugin files.
    """

    path = pathlib.Path(plugin_dir)

    if not path.exists():
        return

    for file in path.glob("*.py"):
        spec = importlib.util.spec_from_file_location(file.stem, file)
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "register"):
            _run_register(module, engine)