#!/usr/bin/env python3

import sys
import os
import json
from pathlib import Path

def main():
    # Add .claude-plugin to path for lib imports
    plugin_dir = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_dir:
        sys.path.insert(0, plugin_dir)
    else:
        # Project-local mode: hooks/ is at .claude-plugin/hooks/
        plugin_dir = Path(__file__).resolve().parent.parent
        sys.path.insert(0, str(plugin_dir))
    from lib.logger import logger
    logger('SYSTEM', f'PermissionRequest hook started')
    from lib.permission import determine
    result = determine(sys.stdin.read(), caller='PermissionRequest')
    # TODO: It is a bad hack, pass this too determine as an argument later!
    print(json.dumps(result))
    logger('SYSTEM', f'PermissionRequest hook finished: {result}')

if __name__ == "__main__":
    main()
