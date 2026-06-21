"""JSON pretty-print subcommand: format and syntax-highlight JSON from a file or stdin."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Optional


def load_json(source: Optional[Path]) -> object:
    """Parse JSON from *source* or from stdin if *source* is None.

    Args:
        source: Path to a JSON file, or ``None`` to read from stdin.

    Returns:
        The parsed JSON value (dict, list, str, int, float, bool, or None).

    Raises:
        json.JSONDecodeError: If the input is not valid JSON.
    """
    text = source.read_text(encoding="utf-8") if source else sys.stdin.read()
    return json.loads(text)
