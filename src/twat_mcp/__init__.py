"""twat-mcp: Model Context Protocol (MCP) plugin for the twat ecosystem.

MCP (Model Context Protocol) is Anthropic's open standard for connecting AI
models to external tools and data sources. An MCP server exposes callable
tools; an MCP client (such as Claude Code or any AI assistant) discovers and
invokes them.

This plugin registers as a twat extension via the ``twat.plugins`` entry
point, allowing twat to discover and expose MCP tool servers to compatible
AI clients. Once installed, twat can act as an MCP host: it loads this plugin,
which in turn manages connections to MCP servers defined in your configuration.

Key components:
- ``mcp_search.py``: discovers and queries MCP tool servers
- Entry point: ``twat.plugins -> mcp = twat_mcp:TwatMcpPlugin``

Dependencies: ``mcp[cli]>=1.2.1``, ``mcp-openapi-proxy``
"""

try:
    from .__version__ import __version__  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    # Package not installed, or version file not generated yet.
    # Provide a fallback version or handle appropriately.
    __version__ = "0.0.0.dev0+unknown"  # Placeholder version

__version__ = metadata.version(__name__)
