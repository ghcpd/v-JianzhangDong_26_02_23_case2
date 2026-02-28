import importlib.util
import pathlib


def load_plugins(engine, plugin_dir: str):
    """Load and initialize plugins from a directory.
    
    Discovers Python files in the given directory and calls their
    register(engine) function if present. Plugins are expected to
    register tasks with the engine via engine.register().
    
    Args:
        engine: TaskEngine instance to pass to plugins for registration
        plugin_dir: Directory path to search for .py plugin files
        
    Expected plugin protocol:
        Plugins must expose: register(engine: TaskEngine) -> None
        Plugins should register at least one task during initialization
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