# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/components/blob.fbs".

# You can extend this class by creating a "BlobExt" class in "blob_ext.py".

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
from .._converters import (
    to_np_uint8,
)
from .blob_ext import BlobExt

__all__ = ["Blob", "BlobArray", "BlobArrayLike", "BlobLike", "BlobType"]


@define
class Blob(BlobExt):
    # You can define your own __init__ function as a member of BlobExt in blob_ext.py

    data: npt.NDArray[np.uint8] = field(converter=to_np_uint8)

    def __array__(self, dtype: npt.DTypeLike = None) -> npt.NDArray[Any]:
        # You can define your own __array__ function as a member of BlobExt in blob_ext.py
        return np.asarray(self.data, dtype=dtype)


if TYPE_CHECKING:
    BlobLike = Union[Blob, bytes, npt.NDArray[np.uint8]]
else:
    BlobLike = Any

BlobArrayLike = Union[Blob, Sequence[BlobLike], bytes, npt.NDArray[np.uint8]]


# --- Arrow support ---


class BlobType(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self, pa.list_(pa.field("item", pa.uint8(), nullable=False, metadata={})), "rerun.components.Blob"
        )


class BlobArray(BaseExtensionArray[BlobArrayLike]):
    _EXTENSION_NAME = "rerun.components.Blob"
    _EXTENSION_TYPE = BlobType

    @staticmethod
    def _native_to_pa_array(data: BlobArrayLike, data_type: pa.DataType) -> pa.Array:
        return BlobExt.native_to_pa_array_override(data, data_type)


BlobType._ARRAY_TYPE = BlobArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(BlobType())


if hasattr(BlobExt, "deferred_patch_class"):
    BlobExt.deferred_patch_class(Blob)
