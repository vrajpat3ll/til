# _uv_: The new virtual environment

> [Blog](https://astral.sh/blog/uv-unified-python-packaging)

> [Docs](https://docs.astral.sh/uv/)

- Basically, it is to replace the venv.
- It is a fast python package manager.
- It can manage entire python projects.

## Installation

```sh
pip install uv
```

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage
```sh
uv init example

cd example

uv add ruff

uv run ruff check

uv lock

uv sync
```

## Python versions
- `uv` installs Python and allows quickly switching between versions.

Install multiple Python versions:
```sh
uv python install 3.10 3.11 3.12
```

use 
```sh
uv python pin 3.10
```
To use 3.10 for the current directory