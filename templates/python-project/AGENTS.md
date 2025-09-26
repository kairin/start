# My Python Project - Agent Instructions

## Project Overview
A UV-compliant Python project following modern Python development standards.

## 🚨 UV-First Development Requirements

> **⚠️ MANDATORY**: This project is **UV-ONLY**. Using standard `pip` commands will cause failures.

**ALL Python package operations MUST use UV:**

```bash
# ✅ CORRECT - Always use uv
uv pip install package-name
uv run python script.py
uv run command-name

# ❌ WRONG - Never use pip directly
pip install package-name        # Will cause import errors
python script.py               # Will cause module errors
command-name                   # Will cause command not found
```

## Environment Setup

```bash
# Create UV virtual environment
uv venv .venv

# Activate environment  
source .venv/bin/activate

# Install project dependencies
uv pip install -e .

# Install development dependencies
uv pip install -e .[dev]
```

## Key Files and Structure

- `src/` - Main source code directory
- `tests/` - Test files
- `pyproject.toml` - Project configuration and dependencies (NO requirements.txt)
- `.venv/` - UV-managed virtual environment
- `uv.lock` - UV dependency lockfile

## Development Workflow

1. Create feature branch: `YYYYMMDD-HHMMSS-feat-description`
2. Make changes in `src/` directory
3. Run tests: `uv run pytest`
4. Run linting: `uv run black . && uv run mypy . && uv run ruff .`
5. Commit with descriptive message
6. Push and create pull request

## Common Commands

```bash
# Run Python scripts
uv run python src/main.py

# Run tests
uv run pytest

# Code formatting
uv run black .

# Type checking
uv run mypy .

# Linting
uv run ruff .

# Install new dependency
uv pip install package-name

# Install development dependency  
uv pip install package-name
# Then add to pyproject.toml [project.optional-dependencies.dev]
```

## Build and Deployment

```bash
# Install in development mode
uv pip install -e .

# Build package
uv run python -m build

# Run as module
uv run python -m my_python_project
```

## UV Compliance Requirements

- ✅ Use `pyproject.toml` only (no requirements.txt, setup.py, setup.cfg)
- ✅ Use system python3 (no pyenv, conda, custom Python)
- ✅ Use `uv venv .venv` for virtual environments
- ✅ Prefix all command execution with `uv run`
- ✅ Use `uv pip install` for all package operations
- ✅ Include `.venv/` in `.gitignore`

## Troubleshooting

### Common UV-Related Issues

**ModuleNotFoundError after installation:**
```bash
# Solution: Always use uv run
uv run python script.py  # Not: python script.py
```

**Command not found errors:**
```bash
# Solution: Prefix with uv run
uv run pytest          # Not: pytest
uv run black .         # Not: black .
```

**Import errors in development:**
```bash
# Solution: Install in development mode
uv pip install -e .
```

### Environment Reset
```bash
# Complete environment reset if needed
rm -rf .venv
uv venv .venv
source .venv/bin/activate  
uv pip install -e .[dev]
```