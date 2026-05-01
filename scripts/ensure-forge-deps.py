#!/usr/bin/env python3
"""SessionStart hook: ensure forge SPC packages are installed."""

import importlib
import subprocess
import sys

PACKAGES = [
    ("forgespc", "forgespc"),
    ("forgeviz", "forgeviz"),
    ("forgestat", "forgestat"),
]

for module_name, repo_name in PACKAGES:
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"Installing {module_name} from github.com/ewolters/{repo_name}...", file=sys.stderr)
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet",
             f"git+https://github.com/ewolters/{repo_name}.git"],
            stderr=subprocess.DEVNULL,
        )
