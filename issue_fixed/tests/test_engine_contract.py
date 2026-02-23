import pytest
from taskflow.engine import TaskEngine


def test_hook_execution_order():
    """
    Contract expectation:
    Hooks should run AFTER task execution,
    and receive both task name and result.
    """

    engine = TaskEngine()

    execution_log = []

    def task():
        execution_log.append("task")
        return 42

    def hook(name, result):
        execution_log.append("hook")

    engine.register("demo", task)
    engine.add_hook(hook)

    engine.execute("demo")

    # Expect task first, then hook
    assert execution_log == ["task", "hook"]