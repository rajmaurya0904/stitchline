"""CLI tests for stitchline."""

import subprocess
import sys


def test_version_flag() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "stitchline.cli", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "stitchline" in result.stdout


def test_help_flag() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "stitchline.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "usage:" in result.stdout


def test_path_flag() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "stitchline.cli", "--path", "/tmp"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "scanning /tmp" in result.stdout


def test_output_flag() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "stitchline.cli", "--output", "/tmp/out.yaml"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "output will be written to /tmp/out.yaml" in result.stdout


def test_verbose_flag() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "stitchline.cli", "--verbose"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "verbose logging enabled" in result.stdout


def test_combined_flags() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "stitchline.cli",
            "--path",
            "/tmp",
            "--output",
            "/tmp/out.yaml",
            "--verbose",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "scanning /tmp" in result.stdout
    assert "verbose logging enabled" in result.stdout
    assert "output will be written to /tmp/out.yaml" in result.stdout


def test_invalid_flag() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "stitchline.cli", "--invalid"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "unrecognized arguments" in result.stderr or "error:" in result.stderr