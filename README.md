# `mxm-types`

![Version](https://img.shields.io/github/v/release/moneyexmachina/mxm-types)
![License](https://img.shields.io/github/license/moneyexmachina/mxm-types)
![Python](https://img.shields.io/badge/python-3.13+-blue)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)

Shared foundational types and representation adapters for the Money Ex Machina ecosystem.

`mxm-types` provides a small, stable package for cross-package MXM type definitions and canonical representation bridges.

It currently includes:

- general shared aliases and micro-protocols
- the canonical MXM timestamp substrate
- explicit pandas boundary adapters for the canonical timestamp model

The package is intentionally representation-focused and domain-agnostic.  
Domain models and business semantics belong in their respective packages.

## Install

```bash
pip install mxm-types
```

## Overview

`mxm-types` defines:

- **Strict JSON tree types** for configuration, metadata, requests, and portable data structures.
- **Lightweight aliases** for common cross-package patterns such as path-like values and HTTP headers.
- **Micro-protocols** for cross-cutting interfaces.
- **A canonical MXM timestamp substrate** based on `np.datetime64[ns]`.
- **Explicit representation bridges** from canonical MXM timestamps to:
  - integer epoch nanoseconds
  - strict canonical UTC strings
  - pandas `Timestamp` / `DatetimeIndex`
- **PEP 561 typing support** (`py.typed` included in the wheel).

The package is intentionally small and stable, but it is no longer dependency-free:  
the pandas boundary adapter layer depends on `pandas`.

## Public API

The following names form the stable public API of `mxm-types`.  
All other names are private and may change across releases.

### General Types

| Name | Description |
|------|-------------|
| `JSONScalar` | `str \| int \| float \| bool \| None` |
| `JSONValue` | Strict recursive JSON tree: scalars, `list[JSONValue]`, `dict[str, JSONValue]` |
| `JSONLike` | Permissive tree for accepting general `Sequence` / `Mapping` inputs |
| `JSONObj` | `Mapping[str, JSONValue]` — preferred for function parameters |
| `JSONMap` | `dict[str, JSONValue]` — preferred for concrete, mutable results |
| `HeadersLike` | Canonical alias for HTTP header mappings |
| `StrPath` | `str \| PathLike[str]` |

### Protocols and TypedDicts

| Name | Description |
|------|-------------|
| `KVReadable` | Minimal protocol for objects exposing `get(key, default)` |
| `CLIFormatOptions` | Optional formatting hints for CLI output (`"plain" \| "rich" \| "json"`) |

### Canonical Timestamp Substrate

| Name | Description |
|------|-------------|
| `TSNSScalar` | Canonical MXM timestamp scalar (`np.datetime64[ns]`) |
| `TSNSArray` | Canonical MXM timestamp array (`ndarray[datetime64[ns]]`) |
| `Int64Array` | `ndarray[int64]` alias used alongside canonical timestamp bridges |
| `TS_NS_DTYPE` | Canonical NumPy timestamp dtype constant |
| `INT64_DTYPE` | Canonical integer dtype constant for epoch nanoseconds |
| `EPOCH_TS_NS` | Unix epoch constant in canonical MXM timestamp form |
| `NAT_TS_NS` | Canonical NumPy `NaT` sentinel in `datetime64[ns]` form |

#### Timestamp Predicates and Assertions

| Name | Description |
|------|-------------|
| `is_ts_ns` | Predicate for canonical timestamp scalars |
| `assert_ts_ns` | Assert and return canonical timestamp scalar |
| `is_nat` | Predicate for canonical `NaT` scalar |
| `assert_not_nat` | Assert scalar is not `NaT` |
| `is_ts_ns_array` | Predicate for canonical timestamp arrays |
| `assert_ts_ns_array` | Assert and return canonical timestamp array |
| `has_nat` | Detect `NaT` in a canonical timestamp array |
| `assert_no_nat` | Assert canonical timestamp array contains no `NaT` |
| `assert_monotonic_increasing_ts_ns_array` | Assert 1D, non-`NaT`, monotonic-increasing canonical timestamp array |

#### Timestamp Bridges

| Name | Description |
|------|-------------|
| `ts_ns_from_int` | Construct canonical timestamp from integer epoch nanoseconds |
| `ts_ns_to_int` | Convert canonical timestamp to integer epoch nanoseconds |
| `ts_ns_from_str` | Parse canonical UTC string into canonical timestamp |
| `ts_ns_to_str` | Format canonical timestamp as canonical UTC string |

### Pandas Timestamp Adapters

| Name | Description |
|------|-------------|
| `is_pd_timestamp_for_ts_ns` | Predicate for approved pandas scalar normal form |
| `assert_pd_timestamp_for_ts_ns` | Assert pandas scalar normal form |
| `is_pd_datetimeindex_for_ts_ns_array` | Predicate for approved pandas array normal form |
| `assert_pd_datetimeindex_for_ts_ns_array` | Assert pandas array normal form |
| `ts_ns_from_pd_timestamp` | Convert pandas `Timestamp` to canonical timestamp |
| `ts_ns_to_pd_timestamp` | Convert canonical timestamp to UTC pandas `Timestamp` |
| `ts_ns_array_from_pd_datetimeindex` | Convert pandas `DatetimeIndex` to canonical timestamp array |
| `ts_ns_array_to_pd_datetimeindex` | Convert canonical timestamp array to UTC pandas `DatetimeIndex` |

---

## Usage

### General shared types

```python
from mxm.types import (
    JSONLike,
    JSONObj,
    JSONValue,
    StrPath,
)

def load_metadata(path: StrPath) -> JSONObj:
    ...
```

### Canonical timestamp substrate

```python
from mxm.types import (
    TSNSScalar,
    assert_not_nat,
    ts_ns_from_str,
    ts_ns_to_int,
)

def parse_created_ts(text: str) -> int:
    ts: TSNSScalar = ts_ns_from_str(text)
    ts = assert_not_nat(ts)
    return ts_ns_to_int(ts)
```

### Pandas boundary adapter

```python
import pandas as pd

from mxm.types import (
    ts_ns_array_from_pd_datetimeindex,
    ts_ns_to_pd_timestamp,
)
from mxm.types.timestamps import ts_ns_from_str

idx = pd.DatetimeIndex(
    ["2026-03-25 10:14:03.123456789", "2026-03-25 10:14:04.123456789"],
    tz="Europe/Amsterdam",
)

arr = ts_ns_array_from_pd_datetimeindex(idx)

ts = ts_ns_from_str("2026-03-25T10:14:03.123456789Z")
pd_ts = ts_ns_to_pd_timestamp(ts)
```

## Timestamp Design

MXM adopts a single canonical internal timestamp representation:

```python
np.datetime64[ns]
```

Under MXM policy, canonical timestamps:

- are timezone-naive NumPy timestamps interpreted strictly as UTC
- represent instants on a POSIX-style linear time axis
- have nanosecond precision
- use explicit boundary adapters for pandas and other external systems

The canonical textual bridge format is:

```text
YYYY-MM-DDTHH:MM:SS.fffffffffZ
```

with exactly 9 fractional digits and mandatory trailing `Z`.

## Design Principles

- **One canonical timestamp model**: shared across MXM packages.
- **Explicit representation bridges**: conversions to strings, integers, and pandas stay visible.
- **Representation-focused scope**: this package owns types and adapters, not domain semantics.
- **Stable cross-package surface**: suitable for low-level shared usage.
- **Strict static typing**: Pyright-clean, test-covered, and PEP 561 compliant.

## Development

```bash
poetry install
poetry run ruff check .
poetry run black --check .
poetry run pyright
poetry run pytest -q
poetry build
```

## License

MIT License. See [LICENSE](LICENSE).

