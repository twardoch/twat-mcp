# twat-mcp: Model Context Protocol plugin for twat

[![PyPI version](https://img.shields.io/pypi/v/twat-mcp.svg)](https://pypi.org/project/twat-mcp/)
[![Python versions](https://img.shields.io/pypi/pyversions/twat-mcp.svg)](https://pypi.org/project/twat-mcp/)
[![License](https://img.shields.io/pypi/l/twat-mcp.svg)](https://opensource.org/licenses/MIT)
[![Build status](https://img.shields.io/github/actions/workflow/status/twardoch/twat-mcp/push.yml?branch=main)](https://github.com/twardoch/twat-mcp/actions/workflows/push.yml)

Part of the [**twat**](https://pypi.org/project/twat/) collection of tools.

`twat-mcp` adds [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) support to the `twat` ecosystem, letting AI assistants (Claude Code, Cursor, etc.) discover and call tools exposed through MCP servers.

## What is MCP?

The **Model Context Protocol** is Anthropic's open standard for connecting AI models to external tools and data sources. It defines a client–server architecture:

- **MCP server**: exposes a set of callable tools (functions, resources, prompts)
- **MCP client / host**: an AI assistant or IDE that discovers those tools and invokes them on the model's behalf

`twat-mcp` turns `twat` into an MCP host. It loads tool servers, handles session negotiation, and routes tool calls between AI clients and the underlying implementations.

## Installation

Requires Python 3.10+. Install with `uv` (recommended) or `pip`:

```bash
uv pip install twat-mcp
# or
pip install twat-mcp
```

The `twat` package must also be installed.

## How it works

`twat-mcp` registers itself as a `twat` plugin via a Python entry point:

```toml
[project.entry-points."twat.plugins"]
mcp = "twat_mcp:TwatMcpPlugin"
```

When `twat` starts, it calls `importlib.metadata.entry_points(group="twat.plugins")`, loads `TwatMcpPlugin`, and delegates MCP lifecycle management to this plugin. The plugin:

1. Reads MCP server configuration (stdio commands, SSE endpoints, or in-process SDK servers)
2. Negotiates capabilities with each server using the MCP handshake
3. Exposes discovered tools to connected AI clients
4. Routes tool call requests and returns results

## Architecture

```
AI client (Claude Code, Cursor, …)
        │  MCP protocol (JSON-RPC over stdio/SSE/HTTP)
        ▼
  TwatMcpPlugin  ←─ loaded by twat via entry_points
        │
        ├── mcp_search.py  (tool discovery and query)
        └── MCP server connections (stdio / SSE / SDK)
```

## Key components

| File | Purpose |
|------|---------|
| `src/twat_mcp/__init__.py` | `TwatMcpPlugin` class; plugin entry point |
| `src/twat_mcp/mcp_search.py` | Discovers and queries MCP tool servers |
| `src/twat_mcp/__version__.py` | Version string (managed by `hatch-vcs`) |

## Development

```bash
git clone https://github.com/twardoch/twat-mcp.git
cd twat-mcp
uv pip install hatch
hatch shell
pre-commit install

# Lint / format / type-check
hatch run lint-all

# Tests
hatch run test:test-cov
```

Versioning uses git tags via `hatch-vcs`. Create an annotated tag and push to trigger a GitHub Actions release.

## License

MIT. Contributions welcome under the same license.
