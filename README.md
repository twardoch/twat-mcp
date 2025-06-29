# twat-mcp: MUD Client Protocol (MCP) Plugin for twat

[![PyPI version](https://img.shields.io/pypi/v/twat-mcp.svg)](https://pypi.org/project/twat-mcp/)
[![Python versions](https://img.shields.io/pypi/pyversions/twat-mcp.svg)](https://pypi.org/project/twat-mcp/)
[![License](https://img.shields.io/pypi/l/twat-mcp.svg)](https://opensource.org/licenses/MIT)
[![Build status](https://img.shields.io/github/actions/workflow/status/twardoch/twat-mcp/push.yml?branch=main)](https://github.com/twardoch/twat-mcp/actions/workflows/push.yml)
[![Coverage status](https://img.shields.io/codecov/c/github/twardoch/twat-mcp/main.svg?style=flat-square)](https://app.codecov.io/gh/twardoch/twat-mcp)

Part of the [**twat**](https://pypi.org/project/twat/) collection of tools.

`twat-mcp` is a plugin for the `twat` application, designed to bring the rich, interactive world of MUDs (Multi-User Dungeons) to your terminal through the power of the MUD Client Protocol (MCP).

## What is a MUD?

A MUD (Multi-User Dungeon) is a text-based online multiplayer game that combines elements of role-playing games, interactive fiction, and online chat. Players connect to a server, typically using a client application, and interact with a virtual world by typing commands. Imagine a vast, descriptive novel where you are the protagonist, and your actions, typed as text, shape your adventure in a world shared with other players. MUDs offer deep, complex gameplay and vibrant communities, existing long before graphical MMORPGs.

## What is MCP? And Why Is It Useful?

The MUD Client Protocol (MCP) is a special communication language that allows MUD servers and MUD clients (like `twat` when equipped with this plugin) to exchange structured information beyond simple text. Think of it as an upgrade to the basic MUD experience:

*   **Plain Telnet:** You send text commands, you get text responses.
*   **With MCP:** The server can send your client data like your character's health points, the items in your inventory, or details about your location. Your client can then display this information in dedicated UI elements (e.g., health bars, inventory lists, dynamic maps) or trigger notifications.

`twat-mcp` implements MCP, specifically targeting version 2.1. This enables `twat` to:

*   **Offer Richer Interactions:** Go beyond basic text with features like clickable links for MUD actions, enhanced character status displays, or even simple graphical elements if `twat` supports them.
*   **Improve User Experience:** Make playing MUDs more intuitive and engaging by providing information in a more organized and accessible way.
*   **Enable Advanced Features:** Support out-of-band communication for things like editing MUD world content directly from the client or secure authentication.

## Who is `twat-mcp` For?

*   **MUD Players using `twat`:** If you use the (hypothetical) `twat` application as your MUD client, `twat-mcp` enhances your gameplay experience on MCP-enabled MUDs.
*   **MUD Administrators and Developers:** If you run or develop a MUD that supports MCP, `twat-mcp` ensures that users connecting via `twat` can take full advantage of your MUD's features.
*   **Developers extending `twat`:** This plugin serves as an example of how to extend `twat` with protocol-specific capabilities.

## Rationale

The `twat` application, a versatile (hypothetical) terminal/text-based interaction tool, can be extended with plugins to support various protocols and functionalities. This plugin, `twat-mcp`, specifically adds support for MCP, enabling `twat` users to connect to MUDs that use MCP for enhanced features.

The goal is to provide a modern, well-tested, and easy-to-maintain implementation of MCP for the `twat` ecosystem.

## Core Features

*   **MCP 2.1 Support**: Implements the MUD Client Protocol version 2.1.
*   **Seamless `twat` Integration**: Designed as a plugin for the `twat` application, discoverable via Python entry points.
*   **Modern Python Stack**: Built with Python 3.10+ using `pyproject.toml` (PEP 621) and Hatch for project management.
*   **Quality Assured**: Fully type-hinted (Mypy), linted and formatted (Ruff), and tested (Pytest).
*   **Automated Processes**: Features automated versioning from Git tags (`hatch-vcs`) and CI/CD via GitHub Actions.

## Installation

To use `twat-mcp`, you'll need Python 3.10 or newer. You can install the plugin using `uv` (a fast Python package installer, recommended) or `pip` (Python's standard package installer).

It's also assumed that you have the main `twat` application installed. If not, please refer to the `twat` installation guide.

```bash
# Using uv (recommended)
uv pip install twat-mcp

# Or using pip
pip install twat-mcp
```

This command installs `twat-mcp` and its dependencies. The `twat` application should then be able to automatically discover and load the plugin if its plugin system is set up to find plugins registered via Python entry points (which `twat-mcp` uses).

## Usage

The `twat-mcp` plugin is designed to integrate seamlessly with the `twat` application. Once installed, `twat` should automatically detect and make MCP capabilities available when you connect to a MUD server that supports MCP.

### Enabling MCP in `twat` (Conceptual)

The exact way to enable or use MCP features will depend on the `twat` application's design. For example, `twat` might:

*   Automatically attempt MCP negotiation when a new MUD connection is established.
*   Provide a command or UI option within `twat` to enable/disable MCP for the current session.
*   Have a configuration setting where you can specify preferred protocols like MCP.

**Example: Connecting to a MUD with `twat` (Conceptual CLI)**

Imagine you're using `twat` from your terminal to connect to a MUD:

```bash
# This is a hypothetical twat CLI command
twat connect mymud.com:4000 --enable-mcp
```

Or, `twat` might have an internal command after connecting:

```
/connect mymud.com:4000
... connected to mymud.com ...
/mcp start
```

During the connection, if the MUD server starts an MCP handshake, `twat-mcp` would handle the communication in the background. You would then see MCP-driven features come to life, such as custom UI elements, status updates, or special MUD-specific commands becoming available.

### Programmatic Interaction (for `twat` or developers)

The `twat-mcp` plugin registers itself using an entry point defined in `pyproject.toml`. The `twat` application would typically use Python's `importlib.metadata` or a similar mechanism to find and load such plugins.

The core of the plugin is the `TwatMcpPlugin` class (expected to be defined in `src/twat_mcp/__init__.py`).

**Conceptual Python Snippet (How `twat` might interact with the plugin):**

```python
# Within the twat application's codebase (hypothetical)

# twat would have a plugin manager or discovery mechanism
# For example, using entry points:
from importlib.metadata import entry_points

def load_twat_plugins():
    loaded_plugins = {}
    try:
        # For Python 3.10+
        discovered_plugins = entry_points(group="twat.plugins")
    except TypeError: # Fallback for older way of calling or if group is not a kwarg
        discovered_plugins = entry_points().select(group="twat.plugins")
    except AttributeError: # Fallback for Python < 3.10 using importlib_metadata
        from importlib_metadata import entry_points
        discovered_plugins = entry_points(group="twat.plugins")

    for entry_point in discovered_plugins:
        if entry_point.name == "mcp": # Name defined in twat-mcp's pyproject.toml
            try:
                plugin_class = entry_point.load()
                # Assuming the plugin class has an __init__ that twat calls,
                # possibly passing some twat-specific context or API.
                # plugin_instance = plugin_class(twat_api_handle=get_twat_api())
                plugin_instance = plugin_class() # Or however twat expects to init
                loaded_plugins[entry_point.name] = plugin_instance
                # Assuming a get_version method or __version__ attribute
                # version = getattr(plugin_instance, "get_version", lambda: getattr(plugin_instance, "__version__", "unknown"))()
                # print(f"Loaded plugin: {entry_point.name} - version {version}")
                print(f"Loaded plugin: {entry_point.name}")


                # twat might then call methods on plugin_instance, e.g.:
                # plugin_instance.initialize_mcp_session(connection_id)
            except Exception as e:
                print(f"Failed to load plugin {entry_point.name}: {e}")
    return loaded_plugins

# Later, when twat receives a message that might be MCP:
# active_mcp_plugin = loaded_plugins.get("mcp")
# if active_mcp_plugin and hasattr(active_mcp_plugin, 'is_mcp_message'):
#     if active_mcp_plugin.is_mcp_message(server_data):
#         mcp_response = active_mcp_plugin.handle_mcp_message(server_data)
#         if mcp_response:
#             send_to_server(mcp_response)

# This is a simplified, conceptual illustration. The actual methods and interaction
# flow would be defined by twat's plugin API. The TwatMcpPlugin class would
# implement the necessary methods to conform to that API, handling MCP negotiation,
# message parsing, and state management.
```

The `TwatMcpPlugin` would be responsible for:

*   Initiating the MCP handshake with the MUD server.
*   Processing incoming MCP messages from the server.
*   Dispatching these messages to appropriate handlers (e.g., for updating UI elements managed by `twat`, or for handling specific MCP packages).
*   Sending MCP messages generated by the client (or by `twat` through the plugin) back to the server.

## How the Code Works (Technical Details)

This section provides a deeper dive into the internal workings of `twat-mcp`.

### Overall Architecture

`twat-mcp` is designed as a plugin for the `twat` application. Its primary responsibility is to manage all aspects of MUD Client Protocol (MCP) communication for `twat`.

1.  **Plugin Discovery and Loading**:
    *   `twat-mcp` registers itself as a plugin using a standard Python entry point: `twat.plugins`. This is defined in the `pyproject.toml` file:
        ```toml
        [project.entry-points."twat.plugins"]
        mcp = "twat_mcp:TwatMcpPlugin"
        ```
    *   The `twat` application is expected to look for entry points in this group. Upon discovering `twat-mcp`, it would load the `TwatMcpPlugin` class from `src/twat_mcp/__init__.py`.

2.  **Main Plugin Class: `TwatMcpPlugin`**:
    *   The `TwatMcpPlugin` class is the central hub of the plugin. An instance of this class will be created by `twat`.
    *   It will hold the state of the MCP connection for a given MUD session.
    *   It will expose methods for `twat` to call, for example, to:
        *   Notify the plugin of new data received from the server.
        *   Request the plugin to send an MCP message to the server.
        *   Query the status of the MCP session.
    *   It will likely interact with a `twat`-provided API to:
        *   Send data back to the MUD server.
        *   Update `twat`'s UI elements based on MCP messages (e.g., display a health bar, update a map).
        *   Log messages or errors.

3.  **Dependencies**:
    *   **`mcp-openapi-proxy`**: This dependency suggests that `twat-mcp` might leverage OpenAPI specifications for MCP messages. It could be used to generate client-side code for message validation, serialization, and deserialization, ensuring that the plugin correctly implements various MCP packages based on a formal specification.
    *   **`mcp[cli]>=1.2.1`**: This indicates a dependency on an MCP library, potentially providing core MCP parsing, state management, or utilities. The `[cli]` extra suggests it might also come with command-line tools useful for debugging or development.
    *   **`twat`**: The plugin naturally depends on the main `twat` application, expecting it to provide the necessary environment and APIs for a plugin to function.

### MCP Protocol Implementation Details

`twat-mcp` aims to implement MCP version 2.1. This involves several key aspects:

1.  **MCP Handshake (Negotiation)**:
    *   When `twat` connects to a MUD, and MCP is enabled, the plugin needs to listen for the server initiating the MCP handshake. This typically starts with the server sending a `#$#mcp version: 2.1 to: 2.1` message.
    *   The `TwatMcpPlugin` will be responsible for recognizing this handshake and responding appropriately to establish an MCP session.
    *   It will also handle the initial exchange of supported MCP packages.

2.  **Message Handling**:
    *   **Parsing**: Incoming data from the MUD server must be inspected for MCP messages. MCP messages are typically prefixed with `#$#`. The plugin will parse these messages to extract the command, arguments, and any key-value pairs.
    *   **Dispatching**: Once an MCP message is parsed (e.g., `#$#dns-com-awns-status-update room_name: "The Grand Hall" room_id: "gh123"`), the plugin will dispatch it to a handler specific to that MCP package and command (e.g., a handler for `dns-com-awns-status-update`).
    *   **State Management**: The plugin will need to maintain state related to the MCP session, such as negotiated packages, authentication status (if using MCP auth), and any data received from the server that needs to be tracked (e.g., current character stats).

3.  **MCP Packages**:
    *   MCP is a framework, and its functionality is extended through various "packages" (e.g., `mcp-negotiate`, `dns-com-awns-status`, `dns-com-awns-display`).
    *   The plugin will need to declare which MCP packages it supports.
    *   Implementation of handlers for specific MCP packages will define the plugin's capabilities. For example:
        *   A handler for `dns-com-awns-status` might update variables in `twat` that display the character's current status.
        *   A handler for `mcp-negotiate` would manage the list of supported packages with the server.
    *   The `mcp-openapi-proxy` dependency suggests that the structure and validation of these packages might be defined by OpenAPI schemas.

4.  **Sending MCP Messages**:
    *   The plugin will provide methods for `twat` (or internal components of the plugin) to construct and send valid MCP messages to the MUD server. This could be in response to server messages or initiated by user actions within `twat`.

### Data Flow

The typical data flow involving `twat-mcp` would be:

**Server to Client (MUD -> `twat` -> `twat-mcp` -> `twat` UI):**

1.  MUD server sends data containing an MCP message (e.g., `#$#char-status-update hp: 100 max_hp: 100`).
2.  `twat` receives this data from the network connection.
3.  `twat` passes the data to the `TwatMcpPlugin` instance.
4.  `TwatMcpPlugin` parses the data, identifies it as an MCP message, and extracts its content.
5.  The plugin processes the message (e.g., notes that HP is 100/100).
6.  The plugin might then use a `twat` API to update a UI element (e.g., set a health bar to full) or store the state internally for other uses.

**Client to Server (`twat` UI/Action -> `twat-mcp` -> `twat` -> MUD):**

1.  A user action in `twat` (e.g., clicking a button defined by an MCP package) or an internal `twat` event triggers the need to send an MCP message.
2.  `twat` calls a method on the `TwatMcpPlugin` instance, requesting it to send a specific MCP message (e.g., `mcp-edit-save` for an object).
3.  `TwatMcpPlugin` constructs the valid MCP message string (e.g., `#$#mcp-edit-save object_name: "sword" content: "A gleaming sword."`).
4.  The plugin passes this string to `twat`'s networking layer.
5.  `twat` sends the message to the MUD server.

### Key Code Components

*   **`pyproject.toml`**:
    *   Defines project metadata, dependencies (including `mcp-openapi-proxy`, `mcp[cli]`, `twat`).
    *   Crucially, contains the `[project.entry-points."twat.plugins"]` definition that allows `twat` to discover `twat-mcp`.
    *   Configures development tools like Hatch, Ruff, Mypy, and Pytest.

*   **`src/twat_mcp/__init__.py`**:
    *   This is the main entry point of the installable package.
    *   It is expected to define the `TwatMcpPlugin` class. This class will encapsulate all MCP logic.
    *   It also includes version information, typically managed by `hatch-vcs` by writing to `src/twat_mcp/__version__.py`.

*   **`src/twat_mcp/mcp_search.py`**:
    *   This file is currently empty. Its intended purpose is not clear from the existing codebase.
    *   Possible uses could have been for implementing client-side discovery of MCP services or packages if a MUD supported such a mechanism (which is not standard MCP 2.1 but could be a custom extension).
    *   Alternatively, it might have been a placeholder for helper functions related to searching or processing MCP data.
    *   For now, its role is undefined in this documentation. If it's developed, this documentation should be updated.

*   **`tests/`**:
    *   Contains Pytest tests for the plugin.
    *   `test_package.py`: Likely contains basic tests confirming package integrity, version, etc.
    *   `test_plugin.py`: Should contain tests for the `TwatMcpPlugin` class, MCP message parsing, state changes, and interaction with a mocked `twat` API.

## Contribution Guidelines

We welcome contributions to `twat-mcp`! Please follow these guidelines to ensure a smooth and effective development process. Our goal is to maintain a high-quality, modern, and robust plugin.

### Guiding Principles

*   **Clarity and Readability**: Write code that is easy to understand and maintain.
*   **Test Coverage**: Aim for comprehensive test coverage for all new features and bug fixes.
*   **Type Safety**: Leverage Python's type hinting system to improve code reliability.
*   **Consistency**: Adhere to the project's coding style and conventions.

### Development Environment Setup

1.  **Prerequisites**:
    *   Git
    *   Python 3.10 or newer
    *   [Hatch](https://hatch.pypa.io/latest/install/): For project and environment management.
    *   [uv](https://github.com/astral-sh/uv): Recommended for fast Python package installation within Hatch environments or standalone.

2.  **Clone the Repository**:
    ```bash
    git clone https://github.com/twardoch/twat-mcp.git
    cd twat-mcp
    ```

3.  **Install Hatch (if not already installed)**:
    ```bash
    # Using uv (recommended)
    uv pip install hatch
    # Or using pip
    pip install hatch
    ```

4.  **Activate the Development Environment with Hatch**:
    Hatch will create and manage a virtual environment for the project, installing all necessary dependencies, including development and testing tools.
    ```bash
    hatch shell
    ```
    This command:
    *   Creates a virtual environment (if it doesn't exist) using the Python version specified in `pyproject.toml` (defaulting to 3.10).
    *   Installs the `twat-mcp` package in editable mode (`-e .`) along with its `dev` and `test` optional dependencies.
    *   Activates the virtual environment, making tools like `pytest`, `ruff`, and `mypy` directly available.

    You can also run commands within the Hatch environment without explicitly activating the shell using `hatch run <script_name>`. For example, `hatch run test`.

5.  **Install Pre-commit Hooks**:
    This project uses pre-commit hooks to automatically check and format your code before each commit. This helps ensure that all committed code adheres to the project's standards.
    ```bash
    # Ensure you are in the hatch shell or your manually activated venv
    pre-commit install
    ```
    The hooks are defined in `.pre-commit-config.yaml`.

### Codebase Structure Overview

*   `pyproject.toml`: Defines project metadata, dependencies, build system (`hatchling`), and configurations for tools like Ruff, Mypy, Pytest, and Hatch environments/scripts.
*   `src/twat_mcp/`: Contains the main source code for the plugin.
    *   `__init__.py`: Main module for the package, expected to define the `TwatMcpPlugin` class.
    *   `__version__.py`: Version file automatically generated/updated by `hatch-vcs`.
    *   `mcp_search.py`: Currently an empty module; its future role will be documented here if developed.
*   `tests/`: Contains the Pytest test suite.
*   `.github/workflows/`: GitHub Actions workflows for Continuous Integration (CI) and releases.
*   `.pre-commit-config.yaml`: Configuration for pre-commit hooks (Ruff, Mypy, etc.).
*   `LICENSE`: The MIT License file.
*   `README.md`: This file – project documentation.

### Coding Standards

*   **Formatting**: Code formatting is enforced by [Ruff](https://docs.astral.sh/ruff/) using the configuration in `pyproject.toml`.
    *   Run `hatch run format` or `ruff format . && ruff check . --fix` to format your code.
    *   The pre-commit hook will also attempt to auto-format changed files.
*   **Linting**: Code quality and style are checked by [Ruff](https://docs.astral.sh/ruff/).
    *   Run `hatch run lint:style` or `ruff check .` to identify and fix linting issues.
*   **Type Checking**: Static type checking is performed by [Mypy](http://mypy-lang.org/) using the configuration in `pyproject.toml`.
    *   Run `hatch run type-check` or `mypy src/twat_mcp tests` to check types.
    *   All new code should include type hints. Aim for `disallow_untyped_defs = true`.

### Running Tests

Comprehensive testing is crucial. This project uses [Pytest](https://docs.pytest.org/).

*   **To run all tests with coverage reporting**:
    ```bash
    hatch run test:test-cov
    ```
    This command (defined in `pyproject.toml` under `tool.hatch.envs.default.scripts`) runs Pytest, measures code coverage, and generates a report.
*   **To run specific tests**:
    ```bash
    hatch run test -- tests/test_plugin.py::TestMyFeature -k "some_test_name"
    ```
    (Arguments after `--` are passed directly to Pytest).
*   Ensure new features are accompanied by tests, and that all tests pass before submitting changes.
*   Maintain or improve the existing code coverage level (see `tool.coverage.report.fail_under` in `pyproject.toml`).

### Versioning and Releases

*   **Versioning Scheme**: The project uses Semantic Versioning (SemVer - `MAJOR.MINOR.PATCH`) based on Git tags.
*   **Automatic Versioning**: The version is managed automatically by `hatch-vcs`.
    *   When a new commit is made on `main` after a release tag, `hatch-vcs` derives a development version (e.g., `0.1.0.post1+g123abc`).
    *   The official version string is written to `src/twat_mcp/__version__.py` at build time.
*   **Making a Release (for maintainers)**:
    1.  Ensure the `main` branch is up-to-date, all tests are passing, and documentation is current.
    2.  Create an annotated Git tag for the new version:
        ```bash
        git tag -a vX.Y.Z -m "Version X.Y.Z Release Notes"
        ```
        (e.g., `git tag -a v0.2.0 -m "Release version 0.2.0: Added feature X and fixed bug Y."`)
    3.  Push the tag to GitHub:
        ```bash
        git push origin vX.Y.Z
        ```
    Pushing a tag matching `v*.*.*` (e.g., `v0.1.0`) will trigger the `release.yml` GitHub Actions workflow. This workflow builds the package (sdist and wheel) and publishes it to PyPI. It also creates a GitHub Release based on the tag.

### Submitting Changes (Pull Requests)

1.  **Fork the Repository**: Create a fork of `twardoch/twat-mcp` on GitHub.
2.  **Create a Feature Branch**:
    ```bash
    git checkout -b your-feature-name main
    ```
    (Choose a descriptive branch name, e.g., `feat/add-mcp-edit-package` or `fix/handle-malformed-input`).
3.  **Implement Your Changes**:
    *   Write clear, maintainable code.
    *   Add comprehensive tests for new functionality or bug fixes.
    *   Ensure your code passes all linting, formatting, and type checks:
        ```bash
        hatch run lint-all
        ```
        (This script typically runs formatting, type checking, and tests with coverage).
    *   Update `README.md` or other documentation if your changes affect usage, architecture, or add new features.
4.  **Commit Your Changes**:
    *   Write clear and concise commit messages. Follow conventional commit message formats if possible (e.g., `feat: Implement MCP package X`, `fix: Resolve issue with Y`).
    *   Ensure pre-commit hooks run successfully.
5.  **Push to Your Fork**:
    ```bash
    git push origin your-feature-name
    ```
6.  **Submit a Pull Request (PR)**:
    *   Open a PR from your feature branch on your fork to the `main` branch of the `twardoch/twat-mcp` repository.
    *   Provide a clear description of your changes in the PR. Reference any relevant issues.
    *   Ensure all automated checks (GitHub Actions CI) pass for your PR.
    *   Be prepared to discuss and iterate on your changes based on feedback.

## License

`twat-mcp` is licensed under the [MIT License](LICENSE). By contributing to `twat-mcp`, you agree that your contributions will be licensed under the same MIT License that covers the project.

## Acknowledgements

*   This plugin is designed for the (hypothetical) `twat` application.
*   Inspired by the MUD Client Protocol (MCP).
*   Utilizes modern Python tooling including Hatch, Ruff, Mypy, and Pytest.
