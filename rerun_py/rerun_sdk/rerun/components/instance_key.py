# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/components/instance_key.fbs".

# You can extend this class by creating a "InstanceKeyExt" class in "instance_key_ext.py".

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Sequence, Union

import numpy as np
import numpy.typing as npt
import pyarrow as pa
from attrs import define, field

from .._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)
from .instance_key_ext import InstanceKeyExt

__all__ = ["InstanceKey", "InstanceKeyArray", "InstanceKeyArrayLike", "InstanceKeyLike", "InstanceKeyType"]


@define
class InstanceKey(InstanceKeyExt):
    """A unique numeric identifier for each individual instance within a batch."""

    # You can define your own __init__ function as a member of InstanceKeyExt in instance_key_ext.py

    value: int = field(converter=int)

    def __array__(self, dtype: npt.DTypeLike = None) -> npt.NDArray[Any]:
        # You can define your own __array__ function as a member of InstanceKeyExt in instance_key_ext.py
        return np.asarray(self.value, dtype=dtype)

    def __int__(self) -> int:
        return int(self.value)


if TYPE_CHECKING:
    InstanceKeyLike = Union[InstanceKey, int]
else:
    InstanceKeyLike = Any

InstanceKeyArrayLike = Union[InstanceKey, Sequence[InstanceKeyLike], int, npt.NDArray[np.uint64]]


# --- Arrow support ---


class InstanceKeyType(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(self, pa.uint64(), "rerun.components.InstanceKey")


class InstanceKeyArray(BaseExtensionArray[InstanceKeyArrayLike]):
    _EXTENSION_NAME = "rerun.components.InstanceKey"
    _EXTENSION_TYPE = InstanceKeyType

    @staticmethod
    def _native_to_pa_array(data: InstanceKeyArrayLike, data_type: pa.DataType) -> pa.Array:
        return InstanceKeyExt.native_to_pa_array_override(data, data_type)


InstanceKeyType._ARRAY_TYPE = InstanceKeyArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(InstanceKeyType())


if hasattr(InstanceKeyExt, "deferred_patch_class"):
    InstanceKeyExt.deferred_patch_class(InstanceKey)
