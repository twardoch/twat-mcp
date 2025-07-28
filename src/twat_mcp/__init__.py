"""twat mcp plugin"""

try:
    from .__version__ import __version__  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    # Package not installed, or version file not generated yet.
    # Provide a fallback version or handle appropriately.
    __version__ = "0.0.0.dev0+unknown"  # Placeholder version

__version__ = metadata.version(__name__)
