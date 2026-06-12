"""
Shared foundational types and vocabulary for Money Ex Machina.

This package provides:

- general shared aliases and micro-protocols
- the canonical MXM timestamp substrate
- explicit pandas boundary adapters for the canonical timestamp model
- shared runtime and infrastructure vocabulary

The package is intentionally small, stable, and dependency-light.

mxm-types owns common representations and cross-package concepts that
must be shared consistently throughout the MXM ecosystem.

Business logic, storage adapters, configuration resolution, secret
management, and runtime construction belong elsewhere.
"""

from __future__ import annotations

from mxm.types.runtime_identity import (
    RuntimeIdentity,
)

from .general import (
    CLIFormatOptions,
    HeadersLike,
    JSONLike,
    JSONMap,
    JSONObj,
    JSONScalar,
    JSONValue,
    KVReadable,
    StrPath,
)
from .pandas_timestamps import (
    assert_pd_datetimeindex_for_ts_ns_array,
    assert_pd_timestamp_for_ts_ns,
    is_pd_datetimeindex_for_ts_ns_array,
    is_pd_timestamp_for_ts_ns,
    ts_ns_array_from_pd_datetimeindex,
    ts_ns_array_to_pd_datetimeindex,
    ts_ns_from_pd_timestamp,
    ts_ns_to_pd_timestamp,
)
from .timestamps import (
    EPOCH_TS_NS,
    INT64_DTYPE,
    NAT_TS_NS,
    TS_NS_DTYPE,
    Int64Array,
    TSNSArray,
    TSNSScalar,
    assert_monotonic_increasing_ts_ns_array,
    assert_no_nat,
    assert_not_nat,
    assert_ts_ns,
    assert_ts_ns_array,
    has_nat,
    is_nat,
    is_ts_ns,
    is_ts_ns_array,
    ts_ns_from_int,
    ts_ns_from_str,
    ts_ns_to_int,
    ts_ns_to_str,
)

__all__ = [
    "EPOCH_TS_NS",
    "INT64_DTYPE",
    "NAT_TS_NS",
    "TS_NS_DTYPE",
    "CLIFormatOptions",
    "HeadersLike",
    "Int64Array",
    "JSONLike",
    "JSONMap",
    "JSONObj",
    "JSONScalar",
    "JSONValue",
    "KVReadable",
    "RuntimeIdentity",
    "StrPath",
    "TSNSArray",
    "TSNSScalar",
    "assert_monotonic_increasing_ts_ns_array",
    "assert_no_nat",
    "assert_not_nat",
    "assert_pd_datetimeindex_for_ts_ns_array",
    "assert_pd_timestamp_for_ts_ns",
    "assert_ts_ns",
    "assert_ts_ns_array",
    "has_nat",
    "is_nat",
    "is_pd_datetimeindex_for_ts_ns_array",
    "is_pd_timestamp_for_ts_ns",
    "is_ts_ns",
    "is_ts_ns_array",
    "ts_ns_array_from_pd_datetimeindex",
    "ts_ns_array_to_pd_datetimeindex",
    "ts_ns_from_int",
    "ts_ns_from_pd_timestamp",
    "ts_ns_from_str",
    "ts_ns_to_int",
    "ts_ns_to_pd_timestamp",
    "ts_ns_to_str",
]
