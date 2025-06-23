# twat-mcp: MCP Plugin for twat

[![PyPI version](https://img.shields.io/pypi/v/twat-mcp.svg)](https://pypi.org/project/twat-mcp/)
[![Python versions](https://img.shields.io/pypi/pyversions/twat-mcp.svg)](https://pypi.org/project/twat-mcp/)
[![License](https://img.shields.io/pypi/l/twat-mcp.svg)](https://opensource.org/licenses/MIT)
[![Build status](https://img.shields.io/github/actions/workflow/status/twardoch/twat-mcp/push.yml?branch=main)](https://github.com/twardoch/twat-mcp/actions/workflows/push.yml)
[![Coverage status](https://img.shields.io/codecov/c/github/twardoch/twat-mcp/main.svg?style=flat-square)](https://app.codecov.io/gh/twardoch/twat-mcp)
<!-- TODO: Update badge URLs if necessary, especially for Codecov -->

`twat-mcp` is a plugin for the `twat` application, designed to implement the MUD Client Protocol (MCP). MCP is a protocol that allows MUD clients and servers to exchange structured data, enabling richer interactions than plain telnet.

## Rationale

The `twat` application, a versatile (hypothetical) terminal/text-based interaction tool, can be extended with plugins to support various protocols and functionalities. This plugin, `twat-mcp`, specifically adds support for MCP, enabling `twat` users to connect to MUDs (Multi-User Dungeons) that use MCP for enhanced features like out-of-band communication, client-side UI updates, and more.

The goal is to provide a modern, well-tested, and easy-to-maintain implementation of MCP for the `twat` ecosystem.

## Features

*   **MCP 2.1 Support**: Aims to implement the MUD Client Protocol version 2.1.
*   **Plugin for `twat`**: Seamlessly integrates with the `twat` plugin system.
*   **Modern Python**: Built with Python 3.10+ using modern tooling.
*   **PEP 621 Compliant Packaging**: Uses `pyproject.toml` for packaging.
*   **Automated Versioning**: Versioning is handled automatically from Git tags using `hatch-vcs`.
*   **Type Hinted**: Fully type-hinted for improved code quality and developer experience with Mypy.
*   **Linted and Formatted**: Code quality maintained with Ruff.
*   **Testing**: Comprehensive test suite using Pytest.
*   **CI/CD Ready**: GitHub Actions for continuous integration, testing, and deployment.
*   **Convenience Structures**: Hatch and uv-based tooling for easy development and packaging.

## Installation

You can install `twat-mcp` from PyPI using `uv` (recommended) or `pip`:

```bash
# Using uv (recommended)
uv pip install twat-mcp

# Or using pip
pip install twat-mcp
```

This will install the plugin, and `twat` should be able to discover it if its plugin system is configured to look for entry points.

## Usage

Once installed, `twat-mcp` should be automatically discoverable by `twat` via its plugin entry point. The specifics of how `twat` loads and interacts with plugins would be defined by `twat` itself.

Conceptually, after `twat` loads the `twat-mcp` plugin, MCP capabilities would become available when connecting to a MUD server that supports MCP. The plugin would handle the MCP handshake and subsequent message exchanges.

**Example (Conceptual Python Snippet within `twat`'s context):**

```python
# This is a hypothetical example of how twat might interact with the plugin.
# The actual usage depends on twat's plugin API.

# Assuming 'twat' has a plugin manager
plugin_manager = twat.get_plugin_manager()

# twat-mcp would have registered itself via entry points
mcp_plugin_instance = plugin_manager.get_plugin_by_name("twat-mcp") # Or similar lookup

if mcp_plugin_instance:
    print(f"Loaded {mcp_plugin_instance.name} version {mcp_plugin_instance.__version__}")
    # twat might then delegate MCP handling to this plugin instance
    # during a MUD connection.
    # mcp_plugin_instance.handle_mcp_message(server_message)
else:
    print("twat-mcp plugin not found or loaded.")

```

The primary interface for this plugin is its registration with `twat` and the methods defined in the `TwatMcpPlugin` class (e.g., `load`, `unload`, and any methods `twat` calls for MCP message handling).

## Contribution Guidelines

We welcome contributions to `twat-mcp`! Please follow these guidelines to ensure a smooth development process.

### Development Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/twardoch/twat-mcp.git
    cd twat-mcp
    ```

2.  **Install Hatch:**
    If you don't have Hatch, install it. `uv` is recommended for installing Python tools.
    ```bash
    uv pip install hatch
    ```

3.  **Activate the development environment:**
    Hatch will create and manage a virtual environment for the project.
    ```bash
    hatch shell
    ```
    This command creates a virtual environment (if it doesn't exist), installs all dependencies including `dev` and `test` extras, and activates the environment.

    Alternatively, you can manually create a virtual environment and install dependencies using `uv`:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
    uv pip install -e ".[dev]"
    ```

### Codebase Structure

*   `pyproject.toml`: Defines project metadata, dependencies, and tool configurations (Hatch, Ruff, Mypy, Pytest).
*   `src/twat_mcp/`: Contains the main source code for the plugin.
    *   `__init__.py`: Main entry point for the package, defines the `TwatMcpPlugin` class.
    *   `__version__.py`: Version file automatically generated by `hatch-vcs`.
*   `tests/`: Contains tests for the plugin.
*   `.github/workflows/`: GitHub Actions workflows for CI/CD.
*   `.pre-commit-config.yaml`: Configuration for pre-commit hooks.

### Running Tests

To run the test suite (including coverage):
```bash
hatch run test:test-cov
```
Or, if you activated your environment manually:
```bash
uv run pytest --cov=src/twat_mcp --cov-report=term-missing --cov-config=pyproject.toml tests/
```

### Linting and Formatting

This project uses Ruff for linting and formatting, and Mypy for type checking.

*   **To run all checks (format, lint, type-check, test):**
    ```bash
    hatch run lint-all
    ```
    (Note: `lint-all` script was defined as `["format", "type-check", "test-cov"]`. You might want a script that *just* does linting/formatting if `test-cov` is too slow for quick checks, e.g., `hatch run lint:all` which runs `style` and `typing` from the `lint` env.)

*   **To format the code:**
    ```bash
    hatch run format
    # or directly:
    uv run ruff format .
    ```

*   **To check for linting issues (and auto-fix where possible):**
    ```bash
    hatch run lint:style # (using the lint environment's style script)
    # or directly:
    uv run ruff check . --fix
    ```

*   **To run type checking with Mypy:**
    ```bash
    hatch run type-check
    # or directly:
    uv run mypy src/twat_mcp tests
    ```

### Pre-commit Hooks

This project uses pre-commit hooks to automatically lint and format code before committing. To install the hooks:
```bash
pre-commit install
```
This will ensure that your commits adhere to the project's coding standards. The hooks are defined in `.pre-commit-config.yaml`.

### Versioning and Releases

*   **Versioning**: The project uses semantic versioning (SemVer) based on Git tags. The version is managed automatically by `hatch-vcs`. When a new commit is made, `hatch-vcs` derives the development version (e.g., `0.1.0.post1+g123abc`).
*   **Making a Release**:
    1.  Ensure your `main` branch is up-to-date and all tests are passing.
    2.  Create an annotated Git tag for the new version:
        ```bash
        git tag -a vX.Y.Z -m "Version X.Y.Z"
        ```
    3.  Push the tag to GitHub:
        ```bash
        git push origin vX.Y.Z
        ```
    Pushing a tag matching `v*` (e.g., `v0.1.0`) will trigger the `release.yml` GitHub Actions workflow, which builds the package and publishes it to PyPI. It will also create a GitHub Release.

### Submitting Changes

1.  Fork the repository on GitHub.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes, ensuring they adhere to the coding style and pass all tests and linters.
4.  Add tests for any new functionality.
5.  Update documentation if necessary.
6.  Push your changes to your fork.
7.  Submit a pull request to the `main` branch of the original repository.

## License

`twat-mcp` is licensed under the [MIT License](LICENSE).

## Acknowledgements

*   This plugin is designed for the (hypothetical) `twat` application.
*   Inspired by the MUD Client Protocol (MCP).
