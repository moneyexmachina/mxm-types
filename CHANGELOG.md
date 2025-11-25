# Changelog

All notable changes to **mxm-types** will be documented in this file.

This project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**  
and the formatting guidelines of **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**.

---

## [0.1.0] - 2025-11-25

### Added
- Initial stable release of `mxm-types`.
- Canonical JSON type system:
  - `JSONScalar`
  - `JSONValue` (strict)
  - `JSONLike` (permissive)
  - `JSONObj` and `JSONMap`
- Path alias:
  - `StrPath`
- Cross-cutting interfaces:
  - `KVReadable` protocol
  - `CLIFormatOptions` `TypedDict`
- PEP 695 `type` aliases and Python 3.13 compatibility.
- PEP 561 typing support via `py.typed`.
- Complete tooling setup:
  - Ruff, Black, Isort, Pyright, Pytest
  - GitHub Actions CI
  - Makefile (`check`, `test`, `build`)
- Documentation and README with explicit API surface.

---

## [Unreleased]
- No pending changes.

---

<!-- Release links (added once repo is online)
[0.1.0]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.1.0
-->
