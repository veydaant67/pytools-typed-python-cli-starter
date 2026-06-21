"""Top-level Typer application — registers all pytools subcommands."""

from __future__ import annotations

import json as _json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table

from pytools.commands.filestats import compute_stats
from pytools.commands.jsonpretty import load_json

console = Console()
app = typer.Typer(
    name="pytools",
    help="Typed Python CLI utilities: file stats, JSON pretty-print, HTTP ping.",
    no_args_is_help=True,
)


@app.command("filestats")
def filestats_cmd(
    file: Path = typer.Argument(..., help="File to analyse", exists=True),  # type: ignore[assignment]
    json_output: bool = typer.Option(False, "--json", help="Emit JSON instead of a table"),
) -> None:
    """Print line, word, character, and byte counts for FILE."""
    stats = compute_stats(file)
    if json_output:
        typer.echo(_json.dumps(stats))
        return
    table = Table(title=str(file))
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")
    for key, value in stats.items():
        table.add_row(key, str(value))
    console.print(table)


@app.command("json")
def json_cmd(
    file: Optional[Path] = typer.Argument(None, help="JSON file to format (default: stdin)"),
    indent: int = typer.Option(2, "--indent", "-i", help="Indentation width"),
    sort_keys: bool = typer.Option(False, "--sort-keys", help="Sort object keys"),
) -> None:
    """Pretty-print JSON from FILE or stdin, with syntax highlighting."""
    try:
        data = load_json(file)
    except _json.JSONDecodeError as exc:
        typer.echo(f"Invalid JSON: {exc}", err=True)
        raise typer.Exit(1)

    formatted = _json.dumps(data, indent=indent, sort_keys=sort_keys)
    syntax = Syntax(formatted, "json", theme="monokai", line_numbers=False)
    console.print(syntax)


@app.command("ping")
def ping_cmd(
    url: str = typer.Argument(..., help="URL to ping"),
    timeout: float = typer.Option(10.0, "--timeout", "-t", help="Timeout in seconds"),
    count: Optional[int] = typer.Option(None, "--count", "-n", help="Number of pings"),
) -> None:
    """Send HTTP GET requests to URL and report status and latency."""
    typer.echo("ping not yet implemented", err=True)
    raise typer.Exit(1)


def main() -> None:
    """Entry point called by the ``pytools`` console script."""
    app()
