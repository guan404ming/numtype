from collections.abc import Iterable
from typing import Any, Literal, TypeAlias, TypeVar, overload

from numpy._typing import DTypeLike, NDArray, _SupportsArrayFunc

_ArrayType = TypeVar("_ArrayType", bound=NDArray[Any])

_Requirements: TypeAlias = Literal[
    "C", "C_CONTIGUOUS", "CONTIGUOUS", "F", "F_CONTIGUOUS", "FORTRAN", "A", "ALIGNED", "W", "WRITEABLE", "O", "OWNDATA"
]
_E: TypeAlias = Literal["E", "ENSUREARRAY"]
_RequirementsWithE: TypeAlias = _Requirements | _E

@overload
def require(
    a: _ArrayType,
    dtype: None = ...,
    requirements: _Requirements | Iterable[_Requirements] | None = ...,
    *,
    like: _SupportsArrayFunc = ...,
) -> _ArrayType: ...
@overload
def require(
    a: object, dtype: DTypeLike = ..., requirements: _E | Iterable[_RequirementsWithE] = ..., *, like: _SupportsArrayFunc = ...
) -> NDArray[Any]: ...
@overload
def require(
    a: object,
    dtype: DTypeLike = ...,
    requirements: _Requirements | Iterable[_Requirements] | None = ...,
    *,
    like: _SupportsArrayFunc = ...,
) -> NDArray[Any]: ...
