"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import stitchline


def test_version_is_set() -> None:
    assert stitchline.__version__


def test_package_is_importable() -> None:
    assert isinstance(stitchline.__name__, str)
    assert stitchline.__name__ == "stitchline"
