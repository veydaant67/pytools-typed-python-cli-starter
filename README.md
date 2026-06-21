# pytools

A typed Python CLI with three subcommands: `filestats`, `json`, and `ping`.

Built with [Typer](https://typer.tiangolo.com/) and [Rich](https://github.com/Textualize/rich).
Type hints throughout; mypy strict mode and ruff enforced in CI.

## Layout

```
src/pytools/
    cli.py              top-level Typer app
    commands/
        filestats.py    line / word / char / byte counts for a file
        jsonpretty.py   format and syntax-highlight JSON
        ping.py         HTTP GET with status and latency (stub)
tests/                  pytest suite (added in later commits)
pyproject.toml          build config, deps, tool settings
```

## Install

```sh
git clone https://github.com/veydaant67/pytools-typed-python-cli-starter
cd pytools-typed-python-cli-starter
pip install -e ".[dev]"
```

## Usage

```sh
pytools filestats path/to/file.txt
pytools filestats path/to/file.txt --json
pytools json path/to/data.json
pytools json --sort-keys path/to/data.json
pytools ping https://example.com          # not yet implemented
```

## Dev

```sh
ruff check src tests
mypy --strict src
pytest --cov=pytools tests/
```
