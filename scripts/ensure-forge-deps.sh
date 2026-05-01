#!/bin/bash
# SessionStart hook: ensure forge SPC packages are installed.
# Uses CLAUDE_PLUGIN_DATA for persistent install across updates.

check_and_install() {
    local pkg=$1
    local repo=$2
    if ! python3 -c "import $pkg" 2>/dev/null; then
        echo "Installing $pkg from github.com/ewolters/$repo..." >&2
        pip install --quiet "git+https://github.com/ewolters/${repo}.git" 2>&1 | tail -1 >&2
    fi
}

check_and_install forgespc forgespc
check_and_install forgeviz forgeviz
check_and_install forgestat forgestat

exit 0
