"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import stitchline


def test_version_is_set() -> None:
    assert stitchline.__version__
