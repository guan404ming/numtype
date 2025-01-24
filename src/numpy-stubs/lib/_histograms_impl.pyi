from collections.abc import Sequence
from typing import (
    Any,
    Literal as L,
    SupportsIndex,
    TypeAlias,
)

from numpy._typing import (
    ArrayLike,
    NDArray,
)

__all__ = ["histogram", "histogram_bin_edges", "histogramdd"]

_BinKind: TypeAlias = L[
    "stone",
    "auto",
    "doane",
    "fd",
    "rice",
    "scott",
    "sqrt",
    "sturges",
]

def histogram_bin_edges(
    a: ArrayLike,
    bins: _BinKind | SupportsIndex | ArrayLike = ...,
    range: None | tuple[float, float] = ...,
    weights: None | ArrayLike = ...,
) -> NDArray[Any]: ...
def histogram(
    a: ArrayLike,
    bins: _BinKind | SupportsIndex | ArrayLike = ...,
    range: None | tuple[float, float] = ...,
    density: bool = ...,
    weights: None | ArrayLike = ...,
) -> tuple[NDArray[Any], NDArray[Any]]: ...
def histogramdd(
    sample: ArrayLike,
    bins: SupportsIndex | ArrayLike = ...,
    range: Sequence[tuple[float, float]] = ...,
    density: None | bool = ...,
    weights: None | ArrayLike = ...,
) -> tuple[NDArray[Any], tuple[NDArray[Any], ...]]: ...
