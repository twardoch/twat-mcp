"""Tests for the twat-mcp plugin functionality."""

from pytest import CaptureFixture  # For capsys typing

# Import the module itself to allow patching within it
import twat_mcp
from twat_mcp import TwatMcpPlugin, __version__


def test_plugin_instantiation() -> None:
    """Test that the TwatMcpPlugin can be instantiated."""
    plugin = TwatMcpPlugin()
    assert plugin is not None
    assert plugin.name == "twat-mcp", "Plugin name should be set correctly."


def test_plugin_version_accessible_via_instance() -> None:
    """Test that the version is accessible, e.g. if plugin uses it internally."""
    plugin = TwatMcpPlugin()
    # This test assumes the plugin might expose or use its version.
    # For now, we just check it's the same as the package version.
    # A more direct test would be if plugin.version existed, for example.
    assert plugin.__class__.__module__ == "twat_mcp"  # Ensure it's the correct class
    # No direct version attribute on instance by default, but can check package one
    assert __version__ is not None


def test_plugin_load_prints_message(capsys: CaptureFixture[str]) -> None:
    """Test that the plugin's load() method prints the expected message."""
    plugin = TwatMcpPlugin()  # Using the direct import from the top
    plugin.load()
    captured = capsys.readouterr()
    # Ensure to use the __version__ that the plugin itself would use.
    # If src/twat_mcp/__version__.py doesn't exist, it's the fallback.
    # If it does, it's the generated one. The test should be consistent.
    # twat_mcp.__version__ imported at the top of this test file should be consistent
    # with what the plugin code sees if the __version__.py file is (not) present.
    expected_output = f"Plugin '{plugin.name}' version {twat_mcp.__version__} loaded.\n"
    assert captured.out == expected_output


def test_plugin_unload_prints_message(capsys: CaptureFixture[str]) -> None:
    """Test that the plugin's unload() method prints the expected message."""
    plugin = TwatMcpPlugin()  # Using the direct import
    plugin.unload()
    captured = capsys.readouterr()
    expected_output = f"Plugin '{plugin.name}' unloaded.\n"
    assert captured.out == expected_output


# Example of a more functional test if the plugin had actual logic:
# def test_plugin_handles_mcp_message() -> None:
#     plugin = TwatMcpPlugin()
#     # Assume plugin.handle_mcp_message(some_data) exists
#     # response = plugin.handle_mcp_message({"command": "mcp_negotiate"})
#     # assert response == {"expected_mcp_reply"}
#     pass


# Test for the __version__ in the package itself (already in test_package.py but good for completeness)
def test_package_has_version() -> None:
    """Verify package exposes version directly."""
    assert __version__ is not None
    assert isinstance(__version__, str)
    # A simple check for development version format, adjust if your scheme is different
    assert "dev" in __version__ or "." in __version__


# More tests can be added here as plugin functionality grows.
# For example, testing specific MCP message handling, state changes, etc.
