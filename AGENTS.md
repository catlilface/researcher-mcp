# Researcher MCP Agent Guidelines

## Project Structure
This is a Python project using FastMCP and pre-commit for development. The main entry point is `main.py`.

## Build/Lint/Test Commands

### Setup
```bash
# Install dependencies (virtual environment is recommended)
pip install -e .
```

### Running Tests
```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_specific.py

# Run a specific test function
pytest tests/test_specific.py::test_function_name

# Run tests with coverage
pytest --cov=src

# Run tests with verbose output
pytest -v
```

### Linting and Formatting
```bash
# Check code style with ruff
ruff check

# Automatically fix fixable issues with ruff
ruff check --fix

# Format code with ruff
ruff format

# Run pre-commit hooks
pre-commit run --all-files
```

### Development Commands
```bash
# Start the main application
python main.py

# Run linter with strict settings
ruff check --select=E,W,F --ignore=N802,N803,N806
```

## Code Style Guidelines

### Imports
- Group imports in order: standard library, third-party, local
- Use explicit relative imports when appropriate
- Import modules, not individual functions/classes when possible
- Sort imports alphabetically within each group

### Formatting
- Follow PEP 8 style guide
- Use 4-space indentation
- Maximum line length of 88 characters (via ruff)
- Add blank lines to separate logical sections
- No trailing whitespace
- Use f-strings for string formatting

### Type Hints
- Always add type hints to function signatures
- Use Optional for nullable types
- Use Union for union types
- Prefer typing.List over list, typing.Dict over dict
- Use typing.TYPE_CHECKING for forward references
- Include docstrings with type annotations

### Naming Conventions
- Use snake_case for variables and functions
- Use PascalCase for classes
- Use UPPER_CASE for constants
- Avoid single letter variable names except for loop counters
- Use descriptive names that indicate purpose

### Error Handling
- Handle exceptions appropriately with try/except blocks
- Log errors with appropriate context information
- Raise specific exceptions when needed
- Use finally blocks for cleanup resources when necessary
- Don't ignore exceptions silently

### Documentation
- Add docstrings to all public functions and classes
- Use Google-style or NumPy-style docstrings consistently
- Document parameters, return values, and exceptions
- Include examples where helpful

## Environment Variables

The project uses environment variables defined in `.env.sample`:
- `ARXIV_BASE_URL`: Base URL for arXiv API
- `PUBMED_BASE_URL`: Base URL for PubMed API

## Dependencies

### Core Dependencies
- fastmcp >= 2.14.5
- pre-commit >= 4.5.1

### Development Dependencies
- pytest for testing
- ruff for linting and formatting
- pre-commit for git hooks

## Pre-commit Hooks

This project uses pre-commit hooks to maintain code quality:
- ruff check and format
- pytest (if applicable)
- Commit message validation

Run `pre-commit install` to set up the hooks locally.