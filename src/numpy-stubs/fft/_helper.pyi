from typing import Any, Literal as L, TypeVar, overload

from numpy import complexfloating, floating, generic, integer
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ShapeLike,
)

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

_SCT = TypeVar("_SCT", bound=generic)

@overload
def fftshift(x: _ArrayLike[_SCT], axes: None | _ShapeLike = ...) -> NDArray[_SCT]: ...
@overload
def fftshift(x: ArrayLike, axes: None | _ShapeLike = ...) -> NDArray[Any]: ...
@overload
def ifftshift(x: _ArrayLike[_SCT], axes: None | _ShapeLike = ...) -> NDArray[_SCT]: ...
@overload
def ifftshift(x: ArrayLike, axes: None | _ShapeLike = ...) -> NDArray[Any]: ...
@overload
def fftfreq(
    n: int | integer[Any],
    d: _ArrayLikeFloat_co = ...,
    device: None | L["cpu"] = ...,
) -> NDArray[floating[Any]]: ...
@overload
def fftfreq(
    n: int | integer[Any],
    d: _ArrayLikeComplex_co = ...,
    device: None | L["cpu"] = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def rfftfreq(
    n: int | integer[Any],
    d: _ArrayLikeFloat_co = ...,
    device: None | L["cpu"] = ...,
) -> NDArray[floating[Any]]: ...
@overload
def rfftfreq(
    n: int | integer[Any],
    d: _ArrayLikeComplex_co = ...,
    device: None | L["cpu"] = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
