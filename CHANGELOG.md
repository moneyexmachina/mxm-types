# Changelog

All notable changes to **mxm-types** will be documented in this file.

This project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**  
and the formatting guidelines of **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**.

---

## Unreleased
- No pending changes.

## [0.3.0] - 2026-06-04

### Added
- Added `RuntimeIdentity` as the canonical shared runtime identity model.
- Added typed runtime identity field aliases for app, environment, machine, substrate, and role.
- Added documentation for the MXM runtime identity model.

### Changed
- Expanded package scope from representation-focused types to shared foundational vocabulary.

## [0.2.2] - 2026-05-12

### Changed

- Relaxed pandas dependency constraint from:
  ```toml
  pandas = ">=3.0.2,<4.0.0"
  ```
  to:
  ```toml
  pandas = ">=2.3.3,<4.0.0"
  ```

### Fixed

- Restored compatibility with the current MXM package ecosystem, including:
  - `mxm-refdata`
  - `mxm-v1`
- Eliminated transitive dependency conflicts during Poetry resolution across MXM packages.

### Notes

- The previous pandas constraint was unnecessarily restrictive and forced ecosystem-wide upgrades to pandas 3.x before downstream packages were ready.
- This release restores compatibility while preserving forward compatibility with future pandas 3.x adoption.
- The issue highlighted the need for centralized dependency governance and synchronized dependency baselines across MXM packages.
## [0.2.1] - 2026-05-07

### Fixed
- Updated `pyproject.toml` to use MXM namespace package declaration:
  - `packages = [{ include = "mxm", from = "src" }]`
- Removed non-canonical Ruff configuration (`exclude`) to match MXM tooling policy.
- Simplified `isort` configuration to canonical MXM defaults.

### Changed
- Aligned project structure and configuration with `mxm-foundry` policy:
  - Enforced PEP 420 namespace package model (`src/mxm` without `__init__.py`)
  - Ensured package directory matches distribution name (`mxm-types` → `mxm/types`)
- Updated `README.md` to conform to MXM documentation policy:
  - Added required `## Purpose` and `## Installation` sections
  - Standardized development workflow to use `make check`

### Notes
- This release introduces no changes to the public API.
- Changes are structural and ensure full compliance with the MXM package standard enforced by `mxm-foundry`.

## [0.2.0] - 2026-04-16
### Added
- Added the canonical MXM timestamp substrate in `mxm.types.timestamps`.
- Added canonical timestamp type aliases and dtype constants:
  - `TSNSScalar`
  - `TSNSArray`
  - `Int64Array`
  - `TS_NS_DTYPE`
  - `INT64_DTYPE`
- Added canonical timestamp constants:
  - `EPOCH_TS_NS`
  - `NAT_TS_NS`
- Added canonical timestamp predicates and assertions:
  - `is_ts_ns`
  - `assert_ts_ns`
  - `is_nat`
  - `assert_not_nat`
  - `is_ts_ns_array`
  - `assert_ts_ns_array`
  - `has_nat`
  - `assert_no_nat`
  - `assert_monotonic_increasing_ts_ns_array`
- Added canonical bridge conversions between:
  - `np.datetime64[ns]` and integer epoch nanoseconds
  - `np.datetime64[ns]` and strict canonical UTC strings
- Added the canonical pandas boundary adapter layer in `mxm.types.pandas_timestamps`.
- Added pandas-side normal-form predicates and assertions for canonical MXM timestamps:
  - `is_pd_timestamp_for_ts_ns`
  - `assert_pd_timestamp_for_ts_ns`
  - `is_pd_datetimeindex_for_ts_ns_array`
  - `assert_pd_datetimeindex_for_ts_ns_array`
- Added explicit pandas bridge conversions between:
  - canonical MXM timestamps and `pd.Timestamp`
  - canonical MXM timestamp arrays and `pd.DatetimeIndex`
- Added test coverage for:
  - canonical timestamp substrate behavior
  - pandas timestamp boundary adapters
  - NaT handling
  - monotonicity checks
  - integer and string round-trips
  - UTC normalization across pandas conversions

### Changed
- Expanded `mxm-types` from a small shared alias package into a broader foundational package for shared MXM representation types and adapters.
- Moved the original general aliases and micro-protocol definitions out of `__init__.py` into `mxm.types.general`.
- Updated `mxm.types.__init__` to re-export the public surface from:
  - `general`
  - `timestamps`
  - `pandas_timestamps`
- Updated package-level documentation to reflect the broader scope of `mxm-types`.

## [0.1.1] - 2025-12-08

### Added
- Introduced `HeadersLike` as a canonical shared alias for HTTP header mappings.

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

[0.3.0]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.3.0
[0.2.2]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.2.2
[0.2.1]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.2.1
[0.2.0]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.2.0
[0.1.1]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.1.1
[0.1.0]: https://github.com/moneyexmachina/mxm-types/releases/tag/v0.1.0
