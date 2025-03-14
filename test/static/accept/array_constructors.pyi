import sys
from collections import deque
from pathlib import Path
from typing import Any
from typing_extensions import TypeVar, assert_type

import numpy as np
import numpy.typing as npt

_SCT_co = TypeVar("_SCT_co", bound=np.generic, covariant=True)

class MyArray(np.ndarray[tuple[int], np.dtype[_SCT_co]]): ...

i8: np.int64

A: npt.NDArray[np.float64]
B: MyArray[np.float64]
C: list[int]
D: MyArray[np.float64 | np.int64]

def func(i: int, j: int, **kwargs: object) -> MyArray[np.float64]: ...

assert_type(np.array(A), npt.NDArray[np.float64])
assert_type(np.array(B), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.array(D), np.ndarray[tuple[int], np.dtype[np.float64 | np.int64]])
assert_type(np.array([1, 1.0]), npt.NDArray[Any])
assert_type(np.array(deque([1, 2, 3])), npt.NDArray[Any])
assert_type(np.array(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.array(A, dtype="c16"), npt.NDArray[Any])
assert_type(np.array(A, like=A), npt.NDArray[np.float64])
assert_type(np.array(A, subok=True), npt.NDArray[np.float64])
assert_type(np.array(B, subok=True), MyArray[np.float64])
assert_type(np.array(B, subok=True, ndmin=0), MyArray[np.float64])
assert_type(np.array(B, subok=True, ndmin=1), MyArray[np.float64])

assert_type(np.zeros([1, 5, 6]), npt.NDArray[np.float64])
assert_type(np.zeros([1, 5, 6], dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.zeros([1, 5, 6], dtype="c16"), npt.NDArray[Any])

assert_type(np.empty([1, 5, 6]), npt.NDArray[np.float64])
assert_type(np.empty([1, 5, 6], dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.empty([1, 5, 6], dtype="c16"), npt.NDArray[Any])

assert_type(np.concatenate(A), npt.NDArray[np.float64])
assert_type(np.concatenate([A, A]), npt.NDArray[Any])  # pyright: ignore[reportAssertTypeFailure]  # npt.NDArray[np.float64]
assert_type(np.concatenate([[1], A]), npt.NDArray[Any])
assert_type(np.concatenate([[1], [1]]), npt.NDArray[Any])
assert_type(np.concatenate((A, A)), npt.NDArray[np.float64])
assert_type(np.concatenate(([1], [1])), npt.NDArray[Any])
assert_type(np.concatenate([1, 1.0]), npt.NDArray[Any])
assert_type(np.concatenate(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.concatenate(A, dtype="c16"), npt.NDArray[Any])
assert_type(np.concatenate([1, 1.0], out=A), npt.NDArray[np.float64])

assert_type(np.asarray(A), npt.NDArray[np.float64])
assert_type(np.asarray(B), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.asarray([1, 1.0]), npt.NDArray[Any])
assert_type(np.asarray(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.asarray(A, dtype="c16"), npt.NDArray[Any])

assert_type(np.asanyarray(A), npt.NDArray[np.float64])
assert_type(np.asanyarray(B), MyArray[np.float64])
assert_type(np.asanyarray([1, 1.0]), npt.NDArray[Any])
assert_type(np.asanyarray(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.asanyarray(A, dtype="c16"), npt.NDArray[Any])

assert_type(np.ascontiguousarray(A), npt.NDArray[np.float64])
assert_type(np.ascontiguousarray(B), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.ascontiguousarray([1, 1.0]), npt.NDArray[Any])
assert_type(np.ascontiguousarray(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.ascontiguousarray(A, dtype="c16"), npt.NDArray[Any])

assert_type(np.asfortranarray(A), npt.NDArray[np.float64])
assert_type(np.asfortranarray(B), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.asfortranarray([1, 1.0]), npt.NDArray[Any])
assert_type(np.asfortranarray(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.asfortranarray(A, dtype="c16"), npt.NDArray[Any])

assert_type(np.fromstring("1 1 1", sep=" "), npt.NDArray[np.float64])
assert_type(np.fromstring(b"1 1 1", sep=" "), npt.NDArray[np.float64])
assert_type(np.fromstring("1 1 1", dtype=np.int64, sep=" "), npt.NDArray[np.int64])
assert_type(np.fromstring(b"1 1 1", dtype=np.int64, sep=" "), npt.NDArray[np.int64])
assert_type(np.fromstring("1 1 1", dtype="c16", sep=" "), npt.NDArray[Any])
assert_type(np.fromstring(b"1 1 1", dtype="c16", sep=" "), npt.NDArray[Any])

assert_type(np.fromfile("test.txt", sep=" "), npt.NDArray[np.float64])
assert_type(np.fromfile("test.txt", dtype=np.int64, sep=" "), npt.NDArray[np.int64])
assert_type(np.fromfile("test.txt", dtype="c16", sep=" "), npt.NDArray[Any])
with open("test.txt", encoding="utf-8") as f:
    assert_type(np.fromfile(f, sep=" "), npt.NDArray[np.float64])
    assert_type(np.fromfile(b"test.txt", sep=" "), npt.NDArray[np.float64])
    assert_type(np.fromfile(Path("test.txt"), sep=" "), npt.NDArray[np.float64])

assert_type(np.fromiter("12345", np.float64), npt.NDArray[np.float64])
assert_type(np.fromiter("12345", float), npt.NDArray[Any])

assert_type(np.frombuffer(A), npt.NDArray[np.float64])
assert_type(np.frombuffer(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.frombuffer(A, dtype="c16"), npt.NDArray[Any])

assert_type(np.arange(False, True), np.ndarray[tuple[int], np.dtype[np.int_]])
assert_type(np.arange(10), np.ndarray[tuple[int], np.dtype[np.int_]])
assert_type(np.arange(0, 10, step=2), np.ndarray[tuple[int], np.dtype[np.int_]])
assert_type(np.arange(10.0), np.ndarray[tuple[int], np.dtype[np.float64 | np.int_]])
assert_type(np.arange(start=0, stop=10.0), np.ndarray[tuple[int], np.dtype[np.float64 | np.int_]])
assert_type(np.arange(np.timedelta64(0)), np.ndarray[tuple[int], np.dtype[np.timedelta64]])
assert_type(np.arange(0, np.timedelta64(10)), np.ndarray[tuple[int], np.dtype[np.timedelta64]])
assert_type(np.arange(np.datetime64("0"), np.datetime64("10")), np.ndarray[tuple[int], np.dtype[np.datetime64]])
assert_type(np.arange(10, dtype=np.float64), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.arange(0, 10, step=2, dtype=np.int16), np.ndarray[tuple[int], np.dtype[np.int16]])
assert_type(np.arange(10, dtype=int), np.ndarray[tuple[int], np.dtype[np.int_]])
assert_type(np.arange(0, 10, dtype="f8"), np.ndarray[tuple[int], np.dtype[Any]])

assert_type(np.require(A), npt.NDArray[np.float64])
assert_type(np.require(B), MyArray[np.float64])
assert_type(np.require(B, requirements=None), MyArray[np.float64])
assert_type(np.require(B, dtype=int), npt.NDArray[Any])
assert_type(np.require(B, requirements="E"), npt.NDArray[np.float64])
assert_type(np.require(B, requirements=["ENSUREARRAY"]), npt.NDArray[np.float64])
assert_type(np.require(B, requirements={"F", "E"}), npt.NDArray[np.float64])
assert_type(np.require(B, requirements=["C", "OWNDATA"]), MyArray[np.float64])
assert_type(np.require(B, requirements="W"), MyArray[np.float64])
assert_type(np.require(B, requirements="A"), MyArray[np.float64])
assert_type(np.require(C), npt.NDArray[np.intp])

assert_type(np.linspace(0, 10), npt.NDArray[np.floating])
assert_type(np.linspace(0, 10j), npt.NDArray[np.inexact])
assert_type(np.linspace(0, 10, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.linspace(0, 10, dtype=int), npt.NDArray[Any])
assert_type(np.linspace(0, 10, retstep=True), tuple[npt.NDArray[np.floating], np.floating])
assert_type(np.linspace(0j, 10, retstep=True), tuple[npt.NDArray[np.inexact], np.inexact])
assert_type(np.linspace(0, 10, retstep=True, dtype=np.int64), tuple[npt.NDArray[np.int64], np.int64])
assert_type(np.linspace(0j, 10, retstep=True, dtype=int), tuple[npt.NDArray[Any], Any])

assert_type(np.logspace(0, 10), npt.NDArray[np.floating])
assert_type(np.logspace(0, 10j), npt.NDArray[np.inexact])
assert_type(np.logspace(0, 10, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.logspace(0, 10, dtype=int), npt.NDArray[Any])

assert_type(np.geomspace(0, 10), npt.NDArray[np.floating])
assert_type(np.geomspace(0, 10j), npt.NDArray[np.inexact])
assert_type(np.geomspace(0, 10, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.geomspace(0, 10, dtype=int), npt.NDArray[Any])

assert_type(np.empty_like(A), npt.NDArray[np.float64])
assert_type(np.empty_like(A, dtype=float), npt.NDArray[np.float64])
assert_type(np.empty_like(A, shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.empty_like(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.empty_like(A, dtype=np.int64, shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[np.int64]])
assert_type(np.empty_like(A, dtype="c16"), npt.NDArray[Any])
assert_type(np.empty_like(A, dtype="c16", shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[Any]])
assert_type(np.empty_like(B), MyArray[np.float64])
assert_type(np.empty_like(B, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.empty_like(True), np.ndarray[tuple[()], np.dtype[np.bool]])
assert_type(np.empty_like([True]), np.ndarray[tuple[int], np.dtype[np.bool]])
assert_type(np.empty_like([[True]]), np.ndarray[tuple[int, int], np.dtype[np.bool]])
assert_type(np.empty_like([[[True]]]), np.ndarray[tuple[int, int, int], np.dtype[np.bool]])
assert_type(np.empty_like(2), np.ndarray[tuple[()], np.dtype[np.intp]])
assert_type(np.empty_like([2]), np.ndarray[tuple[int], np.dtype[np.intp]])
assert_type(np.empty_like([[2]]), np.ndarray[tuple[int, int], np.dtype[np.intp]])
assert_type(np.empty_like([[[2]]]), np.ndarray[tuple[int, int, int], np.dtype[np.intp]])
assert_type(np.empty_like(0.3), np.ndarray[tuple[()], np.dtype[np.float64]])
assert_type(np.empty_like([0.3]), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.empty_like([[0.3]]), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.empty_like([[[0.3]]]), np.ndarray[tuple[int, int, int], np.dtype[np.float64]])
assert_type(np.empty_like(4j), np.ndarray[tuple[()], np.dtype[np.complex128]])
assert_type(np.empty_like([4j]), np.ndarray[tuple[int], np.dtype[np.complex128]])
assert_type(np.empty_like([[4j]]), np.ndarray[tuple[int, int], np.dtype[np.complex128]])
assert_type(np.empty_like([[[4j]]]), np.ndarray[tuple[int, int, int], np.dtype[np.complex128]])

assert_type(np.zeros_like(A), npt.NDArray[np.float64])
assert_type(np.zeros_like(A, dtype=float), npt.NDArray[np.float64])
assert_type(np.zeros_like(A, shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.zeros_like(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.zeros_like(A, dtype=np.int64, shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[np.int64]])
assert_type(np.zeros_like(A, dtype="c16"), npt.NDArray[Any])
assert_type(np.zeros_like(A, dtype="c16", shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[Any]])
assert_type(np.zeros_like(B), MyArray[np.float64])
assert_type(np.zeros_like(B, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.zeros_like(True), np.ndarray[tuple[()], np.dtype[np.bool]])
assert_type(np.zeros_like([True]), np.ndarray[tuple[int], np.dtype[np.bool]])
assert_type(np.zeros_like([[True]]), np.ndarray[tuple[int, int], np.dtype[np.bool]])
assert_type(np.zeros_like([[[True]]]), np.ndarray[tuple[int, int, int], np.dtype[np.bool]])
assert_type(np.zeros_like(2), np.ndarray[tuple[()], np.dtype[np.intp]])
assert_type(np.zeros_like([2]), np.ndarray[tuple[int], np.dtype[np.intp]])
assert_type(np.zeros_like([[2]]), np.ndarray[tuple[int, int], np.dtype[np.intp]])
assert_type(np.zeros_like([[[2]]]), np.ndarray[tuple[int, int, int], np.dtype[np.intp]])
assert_type(np.zeros_like(0.3), np.ndarray[tuple[()], np.dtype[np.float64]])
assert_type(np.zeros_like([0.3]), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.zeros_like([[0.3]]), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.zeros_like([[[0.3]]]), np.ndarray[tuple[int, int, int], np.dtype[np.float64]])
assert_type(np.zeros_like(4j), np.ndarray[tuple[()], np.dtype[np.complex128]])
assert_type(np.zeros_like([4j]), np.ndarray[tuple[int], np.dtype[np.complex128]])
assert_type(np.zeros_like([[4j]]), np.ndarray[tuple[int, int], np.dtype[np.complex128]])
assert_type(np.zeros_like([[[4j]]]), np.ndarray[tuple[int, int, int], np.dtype[np.complex128]])

assert_type(np.ones_like(A), npt.NDArray[np.float64])
assert_type(np.ones_like(A, dtype=float), npt.NDArray[np.float64])
assert_type(np.ones_like(A, shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.ones_like(A, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.ones_like(A, dtype=np.int64, shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[np.int64]])
assert_type(np.ones_like(A, dtype="c16"), npt.NDArray[Any])
assert_type(np.ones_like(A, dtype="c16", shape=(2, 2)), np.ndarray[tuple[int, int], np.dtype[Any]])
assert_type(np.ones_like(B), MyArray[np.float64])
assert_type(np.ones_like(B, dtype=np.int64), npt.NDArray[np.int64])
assert_type(np.ones_like(True), np.ndarray[tuple[()], np.dtype[np.bool]])
assert_type(np.ones_like([True]), np.ndarray[tuple[int], np.dtype[np.bool]])
assert_type(np.ones_like([[True]]), np.ndarray[tuple[int, int], np.dtype[np.bool]])
assert_type(np.ones_like([[[True]]]), np.ndarray[tuple[int, int, int], np.dtype[np.bool]])
assert_type(np.ones_like(2), np.ndarray[tuple[()], np.dtype[np.intp]])
assert_type(np.ones_like([2]), np.ndarray[tuple[int], np.dtype[np.intp]])
assert_type(np.ones_like([[2]]), np.ndarray[tuple[int, int], np.dtype[np.intp]])
assert_type(np.ones_like([[[2]]]), np.ndarray[tuple[int, int, int], np.dtype[np.intp]])
assert_type(np.ones_like(0.3), np.ndarray[tuple[()], np.dtype[np.float64]])
assert_type(np.ones_like([0.3]), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.ones_like([[0.3]]), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.ones_like([[[0.3]]]), np.ndarray[tuple[int, int, int], np.dtype[np.float64]])
assert_type(np.ones_like(4j), np.ndarray[tuple[()], np.dtype[np.complex128]])
assert_type(np.ones_like([4j]), np.ndarray[tuple[int], np.dtype[np.complex128]])
assert_type(np.ones_like([[4j]]), np.ndarray[tuple[int, int], np.dtype[np.complex128]])
assert_type(np.ones_like([[[4j]]]), np.ndarray[tuple[int, int, int], np.dtype[np.complex128]])

assert_type(np.full_like(A, i8), npt.NDArray[np.float64])
assert_type(np.full_like(C, i8), np.ndarray[tuple[int], np.dtype[np.intp]])
assert_type(np.full_like(A, i8, dtype=int), npt.NDArray[Any])
assert_type(np.full_like(B, i8), MyArray[np.float64])
assert_type(np.full_like(B, i8, dtype=np.int64), npt.NDArray[np.int64])

_size: int
_shape_0d: tuple[()]
_shape_1d: tuple[int]
_shape_2d: tuple[int, int]
_shape_nd: tuple[int, ...]
_shape_like: list[int]

assert_type(np.ones(_shape_0d), np.ndarray[tuple[()], np.dtype[np.float64]])
assert_type(np.ones(_size), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.ones(_shape_2d), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.ones(_shape_nd), np.ndarray[tuple[int, ...], np.dtype[np.float64]])
assert_type(np.ones(_shape_1d, dtype=np.int64), np.ndarray[tuple[int], np.dtype[np.int64]])
assert_type(np.ones(_shape_like), npt.NDArray[np.float64])
assert_type(np.ones(_shape_like, dtype=np.dtypes.StringDType()), np.ndarray[tuple[int, ...], np.dtypes.StringDType])
assert_type(np.ones(_shape_like, dtype=int), npt.NDArray[Any])

assert_type(np.full(_size, i8), np.ndarray[tuple[int], np.dtype[np.int64]])
assert_type(np.full(_shape_2d, i8), np.ndarray[tuple[int, int], np.dtype[np.int64]])
assert_type(np.full(_shape_like, i8), npt.NDArray[np.int64])
assert_type(np.full(_shape_like, True), npt.NDArray[np.bool])
assert_type(np.full(_shape_like, 42), npt.NDArray[np.intp])
assert_type(np.full(_shape_like, 0.3), npt.NDArray[np.float64])
assert_type(np.full(_shape_like, 2j), npt.NDArray[np.complex128])
assert_type(np.full(_size, i8, dtype=np.float64), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.full(_size, i8, dtype=float), np.ndarray[tuple[int], np.dtype[np.float64]])
assert_type(np.full(_shape_like, 42, dtype=float), npt.NDArray[np.float64])
assert_type(np.full(_shape_0d, i8, dtype=object), np.ndarray[tuple[()], np.dtype[Any]])

assert_type(np.indices([1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.indices([1, 2, 3], sparse=True), tuple[npt.NDArray[np.int_], ...])

assert_type(np.fromfunction(func, (3, 5)), MyArray[np.float64])

assert_type(np.identity(10), np.ndarray[tuple[int, int], np.dtype[np.float64]])
assert_type(np.identity(10, dtype=np.int64), np.ndarray[tuple[int, int], np.dtype[np.int64]])
assert_type(np.identity(10, dtype=int), np.ndarray[tuple[int, int], np.dtype[Any]])

assert_type(np.atleast_1d(A), npt.NDArray[np.float64])
assert_type(np.atleast_1d(C), npt.NDArray[Any])
assert_type(np.atleast_1d(A, A), tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]])
assert_type(np.atleast_1d(A, C), tuple[npt.NDArray[Any], npt.NDArray[Any]])
assert_type(np.atleast_1d(C, C), tuple[npt.NDArray[Any], npt.NDArray[Any]])
assert_type(np.atleast_1d(A, A, A), tuple[npt.NDArray[np.float64], ...])
assert_type(np.atleast_1d(C, C, C), tuple[npt.NDArray[Any], ...])

assert_type(np.atleast_2d(A), npt.NDArray[np.float64])
assert_type(np.atleast_2d(A, A), tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]])
assert_type(np.atleast_2d(A, A, A), tuple[npt.NDArray[np.float64], ...])

assert_type(np.atleast_3d(A), npt.NDArray[np.float64])
assert_type(np.atleast_3d(A, A), tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]])
assert_type(np.atleast_3d(A, A, A), tuple[npt.NDArray[np.float64], ...])

assert_type(np.vstack([A, A]), npt.NDArray[np.float64])
assert_type(np.vstack([A, A], dtype=np.float32), npt.NDArray[np.float32])
assert_type(np.vstack([A, C]), npt.NDArray[Any])
assert_type(np.vstack([C, C]), npt.NDArray[Any])

assert_type(np.hstack([A, A]), npt.NDArray[np.float64])
assert_type(np.hstack([A, A], dtype=np.float32), npt.NDArray[np.float32])

assert_type(np.stack([A, A]), npt.NDArray[np.float64])
assert_type(np.stack([A, A], dtype=np.float32), npt.NDArray[np.float32])
assert_type(np.stack([A, C]), npt.NDArray[Any])
assert_type(np.stack([C, C]), npt.NDArray[Any])
assert_type(np.stack([A, A], axis=0), npt.NDArray[np.float64])
assert_type(np.stack([A, A], out=B), MyArray[np.float64])

assert_type(np.block([[A, A], [A, A]]), npt.NDArray[Any])  # pyright: ignore[reportAssertTypeFailure]  # npt.NDArray[np.float64]
assert_type(np.block(C), npt.NDArray[Any])

if sys.version_info >= (3, 12):
    from collections.abc import Buffer

    def create_array(obj: npt.ArrayLike) -> npt.NDArray[Any]: ...

    buffer: Buffer
    assert_type(create_array(buffer), npt.NDArray[Any])
