"""Test suite for twat_mcp."""

import twat_mcp  # Moved to top level


def test_version() -> None:
    """Verify package exposes version."""
    assert twat_mcp.__version__
