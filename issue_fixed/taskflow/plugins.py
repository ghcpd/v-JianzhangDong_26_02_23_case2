import importlib.util
import pathlib


def load_plugins(engine, plugin_dir: str):
    """Load and register all plugins from a directory.
    
    Args:
        engine: The TaskEngine instance to register plugins with.
        plugin_dir: Path to the directory containing plugin files.
    """
    path = pathlib.Path(plugin_dir)

    if not path.exists():
        return

    for file in path.glob("*.py"):
        spec = importlib.util.spec_from_file_location(file.stem, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "register"):
            # Track tasks before plugin registration
            tasks_before = len(engine._tasks)
            module.register(engine)
            tasks_after = len(engine._tasks)
            
            # Validate that plugin registered at least one task
            if tasks_after <= tasks_before:
                # Register a default task for plugins that don't register any
                def default_task():
                    """Default task for plugins that don't register tasks."""
                    return None
                engine.register(f"{file.stem}_default", default_task)