import os
import subprocess


def main():
    # ensure logs directory exists
    root = os.path.dirname(__file__)
    logdir = os.path.join(root, "logs")
    os.makedirs(logdir, exist_ok=True)
    logpath = os.path.join(logdir, "test_run.log")

    env = os.environ.copy()
    # when running from this script, make sure our package is importable
    env["PYTHONPATH"] = root

    with open(logpath, "w", encoding="utf-8") as f:
        proc = subprocess.run(
            ["pytest", "-q"],
            cwd=root,
            stdout=f,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
        )
    return proc.returncode


if __name__ == "__main__":
    exit(main())
