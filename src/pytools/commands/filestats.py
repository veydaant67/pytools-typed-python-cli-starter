"""File stats subcommand: line, word, character, and byte counts for a file."""

from pathlib import Path


def compute_stats(path: Path) -> dict[str, int]:
    """Return line, word, character, and byte counts for *path*.

    Args:
        path: Path to the file to analyse.

    Returns:
        Dict with keys ``lines``, ``words``, ``chars``, and ``bytes``.

    Raises:
        FileNotFoundError: If *path* does not exist.
        IsADirectoryError: If *path* is a directory.
    """
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    return {
        "lines": text.count("\n"),
        "words": len(text.split()),
        "chars": len(text),
        "bytes": len(raw),
    }
