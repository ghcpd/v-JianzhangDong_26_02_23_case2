import tempfile
import textwrap
from taskflow.engine import TaskEngine
from taskflow.plugins import load_plugins


def test_plugin_register_contract(tmp_path):
    """
    Contract expectation:
    Plugin must expose register(engine: TaskEngine) -> None
    and should register at least one task.
    """

    plugin_code = textwrap.dedent("""
        def register(engine):
            pass
    """
    )

    plugin_file = tmp_path / "bad_plugin.py"
    plugin_file.write_text(plugin_code)

    engine = TaskEngine()
    load_plugins(engine, str(tmp_path))

    # Expect at least one task registered
    assert len(engine._tasks) > 0
