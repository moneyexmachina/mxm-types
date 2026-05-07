# `mxm-types`

![Version](https://img.shields.io/github/v/release/moneyexmachina/mxm-types)
![License](https://img.shields.io/github/license/moneyexmachina/mxm-types)
![Python](https://img.shields.io/badge/python-3.13+-blue)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)

## Purpose

`mxm-types` provides shared foundational types and representation adapters for the Money Ex Machina ecosystem.

It defines a small, stable, representation-focused layer for:

- cross-package type definitions
- canonical data representations
- explicit boundary adapters between representations

The package is intentionally domain-agnostic.  
Domain models and business semantics belong in their respective packages.

## Installation

```bash
pip install mxm-types
```

## Overview

`mxm-types` defines:

- **Strict JSON tree types** for configuration, metadata, requests, and portable data structures
- **Lightweight aliases** for common cross-package patterns such as path-like values and HTTP headers
- **Micro-protocols** for cross-cutting interfaces
- **A canonical MXM timestamp substrate** based on `np.datetime64[ns]`
- **Explicit representation bridges** from canonical MXM timestamps to:
  - integer epoch nanoseconds
  - strict canonical UTC strings
  - pandas `Timestamp` / `DatetimeIndex`
- **PEP 561 typing support** (`py.typed` included in the wheel)

The package is intentionally small and stable, but it is no longer dependency-free:  
the pandas boundary adapter layer depends on `pandas`.

## Public API

The following names form the stable public API of `mxm-types`.  
All other names are private and may change across releases.

### General Types

| Name | Description |
|------|-------------|
| `JSONScalar` | `str \| int \| float \| bool \| None` |
| `JSONValue` | Strict recursive JSON tree |
| `JSONLike` | Permissive tree for accepting general inputs |
| `JSONObj` | `Mapping[str, JSONValue]` |
| `JSONMap` | `dict[str, JSONValue]` |
| `HeadersLike` | Canonical alias for HTTP header mappings |
| `StrPath` | `str \| PathLike[str]` |

### Protocols and TypedDicts

| Name | Description |
|------|-------------|
| `KVReadable` | Minimal protocol for key-value access |
| `CLIFormatOptions` | CLI output formatting hints |

### Canonical Timestamp Substrate

| Name | Description |
|------|-------------|
| `TSNSScalar` | Canonical timestamp scalar (`np.datetime64[ns]`) |
| `TSNSArray` | Canonical timestamp array |
| `Int64Array` | Integer array for epoch nanoseconds |
| `TS_NS_DTYPE` | Canonical timestamp dtype |
| `INT64_DTYPE` | Canonical integer dtype |
| `EPOCH_TS_NS` | Unix epoch constant |
| `NAT_TS_NS` | Canonical `NaT` sentinel |

#### Timestamp Predicates and Assertions

| Name | Description |
|------|-------------|
| `is_ts_ns` | Predicate for canonical timestamp scalars |
| `assert_ts_ns` | Assert canonical timestamp scalar |
| `is_nat` | Predicate for `NaT` |
| `assert_not_nat` | Assert not `NaT` |
| `is_ts_ns_array` | Predicate for timestamp arrays |
| `assert_ts_ns_array` | Assert timestamp array |
| `has_nat` | Detect `NaT` in array |
| `assert_no_nat` | Assert no `NaT` |
| `assert_monotonic_increasing_ts_ns_array` | Assert monotonic timestamps |

#### Timestamp Bridges

| Name | Description |
|------|-------------|
| `ts_ns_from_int` | From integer epoch nanoseconds |
| `ts_ns_to_int` | To integer epoch nanoseconds |
| `ts_ns_from_str` | From canonical string |
| `ts_ns_to_str` | To canonical string |

### Pandas Timestamp Adapters

| Name | Description |
|------|-------------|
| `is_pd_timestamp_for_ts_ns` | Predicate for pandas scalar |
| `assert_pd_timestamp_for_ts_ns` | Assert pandas scalar |
| `is_pd_datetimeindex_for_ts_ns_array` | Predicate for pandas index |
| `assert_pd_datetimeindex_for_ts_ns_array` | Assert pandas index |
| `ts_ns_from_pd_timestamp` | Convert from pandas |
| `ts_ns_to_pd_timestamp` | Convert to pandas |
| `ts_ns_array_from_pd_datetimeindex` | Convert index to array |
| `ts_ns_array_to_pd_datetimeindex` | Convert array to index |

---

## Usage

### General shared types

```python
from mxm.types import JSONObj, StrPath

def load_metadata(path: StrPath) -> JSONObj:
    ...
```

### Canonical timestamp substrate

```python
from mxm.types import TSNSScalar, assert_not_nat, ts_ns_from_str, ts_ns_to_int

def parse_created_ts(text: str) -> int:
    ts: TSNSScalar = ts_ns_from_str(text)
    ts = assert_not_nat(ts)
    return ts_ns_to_int(ts)
```

### Pandas boundary adapter

```python
import pandas as pd
from mxm.types import ts_ns_array_from_pd_datetimeindex, ts_ns_to_pd_timestamp
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

Canonical timestamps:

- are timezone-naive NumPy timestamps interpreted as UTC
- represent instants on a linear time axis
- have nanosecond precision
- use explicit boundary adapters for external systems

Canonical string format:

```text
YYYY-MM-DDTHH:MM:SS.fffffffffZ
```

## Design Principles

- **Single canonical representation**
- **Explicit boundary adapters**
- **Representation-focused scope**
- **Stable cross-package surface**
- **Strict static typing**

## Development

```bash
make check
```

## License

MIT License. See [LICENSE](LICENSE).
