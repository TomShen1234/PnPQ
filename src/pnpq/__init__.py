"""Python library to control hardware used in quantum optical testbeds."""

from pathlib import Path
from typing import Optional


def get_version() -> Optional[str]:
    """Get the version number from version.txt."""
    version_file = Path(__file__).parent / "version.txt"
    if version_file.exists():
        with open(version_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None


__version__ = get_version()
