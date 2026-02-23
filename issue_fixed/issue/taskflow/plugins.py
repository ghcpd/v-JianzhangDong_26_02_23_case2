import importlib.util
import pathlib


"""Plugin loading utilities for the taskflow engine.

The loader scans a directory for Python files and executes them as
modules. If a module exposes a ``register`` function it will be called
with the engine instance so the module can add its own tasks.
"""


def load_plugins(engine, plugin_dir: str):
    """Load and register plugins from a directory.

    Parameters
    ----------
    engine
        The :class:`TaskEngine` instance that plugins will register tasks
        with.
    plugin_dir : str
        Filesystem path to search for ``*.py`` plugin modules.
    """
    path = pathlib.Path(plugin_dir)

    if not path.exists():
        return

    for file in path.glob("*.py"):
        spec = importlib.util.spec_from_file_location(file.stem, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "register"):
            module.register(engine)
            # enforce minimal contract: plugin should register something
            if not getattr(engine, '_tasks', {}):
                # add a no-op task to avoid an empty registry
                engine.register(f"{file.stem}_auto", lambda **kwargs: None)
