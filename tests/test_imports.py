from __future__ import annotations

from pathlib import Path
from typing import Any

from mxm.types import (
    CLIFormatOptions,
    JSONLike,
    JSONMap,
    JSONObj,
    JSONScalar,
    JSONValue,
    KVReadable,
    StrPath,
)


def test_json_scalar_and_value_nesting() -> None:
    # JSONScalar should accept basic JSON-compatible scalars
    scalars: list[JSONScalar] = ["x", 1, 1.5, True, None]
    assert len(scalars) == 5

    # JSONValue should accept nested list/dict structures
    value: JSONValue = {
        "a": 1,
        "b": [True, None, 3.14],
        "c": {"nested": "ok"},
    }
    assert isinstance(value, dict)
    assert "c" in value


def test_json_obj_and_map_aliases() -> None:
    # JSONObj is a Mapping[str, JSONValue]
    obj: JSONObj = {"foo": 1, "bar": ["x", "y"]}
    assert obj["foo"] == 1

    # JSONMap is a dict[str, JSONValue]
    m: JSONMap = {"x": {"inner": False}}
    assert isinstance(m, dict)
    assert isinstance(m["x"], dict)


def test_json_like_permissive_shapes() -> None:
    # JSONLike can accept general Sequence/Mapping, not just list/dict
    like1: JSONLike = ("tuple", 1, 2)  # type: ignore[assignment]
    like2: JSONLike = {"k": ("v1", "v2")}  # type: ignore[assignment]

    assert isinstance(like1, tuple)
    assert isinstance(like2, dict)


def test_strpath_accepts_str_and_path() -> None:
    def needs_path(p: StrPath) -> str:
        return str(p)

    s = needs_path("/tmp/test")
    p = needs_path(Path("/tmp/other"))

    assert "/tmp" in s
    assert "/tmp" in p


def test_kv_readable_protocol_runtime_check() -> None:
    class DummyStore:
        def __init__(self) -> None:
            self._data: dict[str, Any] = {"a": 1}

        def get(self, key: str, default: Any = None) -> Any:
            return self._data.get(key, default)

    store = DummyStore()

    # Protocol is runtime_checkable, so this should pass
    assert isinstance(store, KVReadable)
    assert store.get("a") == 1
    assert store.get("missing", 42) == 42


def test_cli_format_options_literal_values() -> None:
    opts: CLIFormatOptions = {"format": "json"}
    assert opts["format"] in {"plain", "rich", "json"}
