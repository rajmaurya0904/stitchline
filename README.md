# Stitchline

**Automatically generates and keeps up-to-date OpenAPI specifications by statically analyzing TypeScript router code and test suites.**

When API contracts drift, developers manually sync specs, wasting hours chasing down undocumented route changes and test discrepancies. Stitchline parses TypeScript ASTs and test assertions directly, eliminating manual spec maintenance entirely.

## Example

```bash
$ stitchline --path . --output openapi.yaml
stitchline scanning .
output will be written to openapi.yaml
```

## Install

Clone the repository and install in editable mode:

```bash
pip install -e .
```

## Usage

Stitchline provides a single command-line tool with configuration flags:

- `stitchline`: Generates the OpenAPI specification by scanning the current directory and printing to stdout.
- `stitchline --path <dir>`: Scans a specified directory for TypeScript router code and test suites.
- `stitchline --output <file>`: Writes the generated OpenAPI specification to the specified file path instead of stdout.
- `stitchline --verbose`: Enables verbose logging during analysis and generation.

## How it works

- Parses TypeScript Abstract Syntax Trees (ASTs) for route definitions and HTTP methods.
- Extracts request/response schemas and validation rules from source and test assertions.
- Computes endpoint parameter types, query parameters, and status codes.
- Emits fully compliant OpenAPI specifications in YAML or JSON format.

## Limitations

- Supports common TypeScript router patterns but does not evaluate arbitrary dynamic runtime routing logic.
- Does not automatically push generated specs to remote API gateways or developer portals.
- Experimental support for complex nested middleware chains.
