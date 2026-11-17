"""CLI for stitchline: generate and update OpenAPI specifications."""

import argparse


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stitchline",
        description="Generate and keep up-to-date OpenAPI specifications "
        "by statically analyzing TypeScript router code and test suites.",
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Root directory to scan for TypeScript router code and tests "
        "(default: current directory)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path for the generated OpenAPI spec; if not set, "
        "prints to stdout",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose logging",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"stitchline {__import__('stitchline').__version__}",
        help="Show version and exit",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)
    print(f"stitchline scanning {args.path}")
    if args.verbose:
        print("verbose logging enabled")
    if args.output:
        print(f"output will be written to {args.output}")
    else:
        print("output to stdout")


if __name__ == "__main__":
    main()