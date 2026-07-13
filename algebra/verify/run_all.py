"""Run every *_verify.py script in this folder and report a combined result.

This is the literal reviewer gate: a PR is not mergeable unless this exits 0.

Usage:
    python3 run_all.py
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent


def main():
    scripts = sorted(p for p in HERE.glob("*_verify.py"))
    if not scripts:
        print("No verify scripts found.")
        return

    failed = []
    for script in scripts:
        print(f"── {script.name} " + "─" * max(0, 50 - len(script.name)), flush=True)
        result = subprocess.run([sys.executable, str(script)])
        if result.returncode != 0:
            failed.append(script.name)
        print(flush=True)

    if failed:
        print(f"FAILED: {', '.join(failed)}")
        raise SystemExit(1)
    print(f"All {len(scripts)} sheet verify scripts passed.")


if __name__ == "__main__":
    main()
