import ast
import sys
import types
import unittest
import warnings
from _typeshed import GenericPath, StrOrBytesPath, StrPath
from collections.abc import Callable, Iterable, Sequence
from contextlib import _GeneratorContextManager
from re import Pattern
from typing import (
    Any,
    AnyStr,
    ClassVar,
    Final,
    Literal as L,
    NoReturn,
    ParamSpec,
    Self,
    SupportsIndex,
    TypeAlias,
    TypeVar,
    overload,
    type_check_only,
)
from unittest.case import SkipTest

import numpy as np
from numpy import _ConvertibleToFloat, number, object_
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLikeDT64_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
)

__all__ = [
    "HAS_LAPACK64",
    "HAS_REFCOUNT",
    "IS_EDITABLE",
    "IS_MUSL",
    "IS_PYPY",
    "IS_PYSTON",
    "IS_WASM",
    "NOGIL_BUILD",
    "IgnoreException",
    "KnownFailureException",
    "SkipTest",
    "assert_",
    "assert_allclose",
    "assert_almost_equal",
    "assert_approx_equal",
    "assert_array_almost_equal",
    "assert_array_almost_equal_nulp",
    "assert_array_compare",
    "assert_array_equal",
    "assert_array_less",
    "assert_array_max_ulp",
    "assert_equal",
    "assert_no_gc_cycles",
    "assert_no_warnings",
    "assert_raises",
    "assert_raises_regex",
    "assert_string_equal",
    "assert_warns",
    "break_cycles",
    "build_err_msg",
    "check_support_sve",
    "clear_and_catch_warnings",
    "decorate_methods",
    "jiffies",
    "measure",
    "memusage",
    "print_assert_equal",
    "run_threaded",
    "rundocs",
    "runstring",
    "suppress_warnings",
    "tempdir",
    "temppath",
    "verbose",
]

_P = ParamSpec("_P")
_T = TypeVar("_T")
_ET = TypeVar("_ET", bound=BaseException)
_FT = TypeVar("_FT", bound=Callable[..., Any])

# Must return a bool or an ndarray/generic type
# that is supported by `np.logical_and.reduce`
_ComparisonFunc: TypeAlias = Callable[
    [NDArray[Any], NDArray[Any]], (bool | np.bool | number[Any] | NDArray[np.bool | number[Any] | object_])
]

class KnownFailureException(Exception): ...
class IgnoreException(Exception): ...

class clear_and_catch_warnings(warnings.catch_warnings[list[warnings.WarningMessage]]):
    class_modules: ClassVar[tuple[types.ModuleType, ...]]
    modules: set[types.ModuleType]
    @overload
    def __new__(
        cls,
        record: L[False] = ...,
        modules: Iterable[types.ModuleType] = ...,
    ) -> _clear_and_catch_warnings_without_records: ...
    @overload
    def __new__(
        cls,
        record: L[True],
        modules: Iterable[types.ModuleType] = ...,
    ) -> _clear_and_catch_warnings_with_records: ...
    @overload
    def __new__(
        cls,
        record: bool,
        modules: Iterable[types.ModuleType] = ...,
    ) -> clear_and_catch_warnings: ...
    def __enter__(self) -> None | list[warnings.WarningMessage]: ...
    def __exit__(
        self,
        __exc_type: None | type[BaseException] = ...,
        __exc_val: None | BaseException = ...,
        __exc_tb: None | types.TracebackType = ...,
    ) -> None: ...

# Type-check only `clear_and_catch_warnings` subclasses for both values of the
# `record` parameter. Copied from the stdlib `warnings` stubs.

@type_check_only
class _clear_and_catch_warnings_with_records(clear_and_catch_warnings):
    def __enter__(self) -> list[warnings.WarningMessage]: ...

@type_check_only
class _clear_and_catch_warnings_without_records(clear_and_catch_warnings):
    def __enter__(self) -> None: ...

class suppress_warnings:
    log: list[warnings.WarningMessage]
    def __init__(
        self,
        forwarding_rule: L["always", "module", "once", "location"] = ...,
    ) -> None: ...
    def filter(
        self,
        category: type[Warning] = ...,
        message: str = ...,
        module: None | types.ModuleType = ...,
    ) -> None: ...
    def record(
        self,
        category: type[Warning] = ...,
        message: str = ...,
        module: None | types.ModuleType = ...,
    ) -> list[warnings.WarningMessage]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        __exc_type: None | type[BaseException] = ...,
        __exc_val: None | BaseException = ...,
        __exc_tb: None | types.TracebackType = ...,
    ) -> None: ...
    def __call__(self, func: _FT) -> _FT: ...

verbose: int
IS_EDITABLE: Final[bool]
IS_MUSL: Final[bool]
IS_PYPY: Final[bool]
IS_PYSTON: Final[bool]
IS_WASM: Final[bool]
HAS_REFCOUNT: Final[bool]
HAS_LAPACK64: Final[bool]
NOGIL_BUILD: Final[bool]

def assert_(val: object, msg: str | Callable[[], str] = ...) -> None: ...

# Contrary to runtime we can't do `os.name` checks while type checking,
# only `sys.platform` checks
if sys.platform == "win32" or sys.platform == "cygwin":
    def memusage(processName: str = ..., instance: int = ...) -> int: ...

elif sys.platform == "linux":
    def memusage(_proc_pid_stat: StrOrBytesPath = ...) -> None | int: ...

else:
    def memusage() -> NoReturn: ...

if sys.platform == "linux":
    def jiffies(
        _proc_pid_stat: StrOrBytesPath = ...,
        _load_time: list[float] = ...,
    ) -> int: ...

else:
    def jiffies(_load_time: list[float] = ...) -> int: ...

def build_err_msg(
    arrays: Iterable[object],
    err_msg: str,
    header: str = ...,
    verbose: bool = ...,
    names: Sequence[str] = ...,
    precision: None | SupportsIndex = ...,
) -> str: ...
def assert_equal(actual: object, desired: object, err_msg: object = ..., verbose: bool = ..., *, strict: bool = ...) -> None: ...
def print_assert_equal(
    test_string: str,
    actual: object,
    desired: object,
) -> None: ...
def assert_almost_equal(
    actual: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    desired: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    decimal: int = ...,
    err_msg: object = ...,
    verbose: bool = ...,
) -> None: ...

# Anything that can be coerced into `builtins.float`
def assert_approx_equal(
    actual: _ConvertibleToFloat,
    desired: _ConvertibleToFloat,
    significant: int = ...,
    err_msg: object = ...,
    verbose: bool = ...,
) -> None: ...
def assert_array_compare(
    comparison: _ComparisonFunc,
    x: ArrayLike,
    y: ArrayLike,
    err_msg: object = ...,
    verbose: bool = ...,
    header: str = ...,
    precision: SupportsIndex = ...,
    equal_nan: bool = ...,
    equal_inf: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
def assert_array_equal(
    x: ArrayLike, y: ArrayLike, /, err_msg: object = ..., verbose: bool = ..., *, strict: bool = ...
) -> None: ...
def assert_array_almost_equal(
    x: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    y: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    /,
    decimal: float = ...,
    err_msg: object = ...,
    verbose: bool = ...,
) -> None: ...
@overload
def assert_array_less(
    x: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    y: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
@overload
def assert_array_less(
    x: _ArrayLikeTD64_co, y: _ArrayLikeTD64_co, err_msg: object = ..., verbose: bool = ..., *, strict: bool = ...
) -> None: ...
@overload
def assert_array_less(
    x: _ArrayLikeDT64_co, y: _ArrayLikeDT64_co, err_msg: object = ..., verbose: bool = ..., *, strict: bool = ...
) -> None: ...
def runstring(
    astr: str | bytes | types.CodeType,
    dict: None | dict[str, Any],
) -> Any: ...
def assert_string_equal(actual: str, desired: str) -> None: ...
def rundocs(
    filename: StrPath | None = ...,
    raise_on_error: bool = ...,
) -> None: ...
def check_support_sve(__cache: list[_T]) -> _T: ...
def raises(*args: type[BaseException]) -> Callable[[_FT], _FT]: ...
@overload
def assert_raises(  # type: ignore
    expected_exception: type[BaseException] | tuple[type[BaseException], ...],
    callable: Callable[_P, Any],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> None: ...
@overload
def assert_raises(
    expected_exception: type[_ET] | tuple[type[_ET], ...],
    *,
    msg: None | str = ...,
) -> unittest.case._AssertRaisesContext[_ET]: ...
@overload
def assert_raises_regex(
    expected_exception: type[BaseException] | tuple[type[BaseException], ...],
    expected_regex: str | bytes | Pattern[Any],
    callable: Callable[_P, Any],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> None: ...
@overload
def assert_raises_regex(
    expected_exception: type[_ET] | tuple[type[_ET], ...],
    expected_regex: str | bytes | Pattern[Any],
    *,
    msg: None | str = ...,
) -> unittest.case._AssertRaisesContext[_ET]: ...
def decorate_methods(
    cls: type[Any],
    decorator: Callable[[Callable[..., Any]], Any],
    testmatch: None | str | bytes | Pattern[Any] = ...,
) -> None: ...
def measure(
    code_str: str | bytes | ast.mod | ast.AST,
    times: int = ...,
    label: None | str = ...,
) -> float: ...
@overload
def assert_allclose(
    actual: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    desired: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
@overload
def assert_allclose(
    actual: _ArrayLikeTD64_co,
    desired: _ArrayLikeTD64_co,
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
def assert_array_almost_equal_nulp(
    x: _ArrayLikeNumber_co,
    y: _ArrayLikeNumber_co,
    nulp: float = ...,
) -> None: ...
def assert_array_max_ulp(
    a: _ArrayLikeNumber_co,
    b: _ArrayLikeNumber_co,
    maxulp: float = ...,
    dtype: DTypeLike = ...,
) -> NDArray[Any]: ...
@overload
def assert_warns(warning_class: type[Warning]) -> _GeneratorContextManager[None]: ...
@overload
def assert_warns(
    warning_class: type[Warning],
    func: Callable[_P, _T],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> _T: ...
@overload
def assert_no_warnings() -> _GeneratorContextManager[None]: ...
@overload
def assert_no_warnings(
    func: Callable[_P, _T],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> _T: ...
@overload
def tempdir(
    suffix: None = ...,
    prefix: None = ...,
    dir: None = ...,
) -> _GeneratorContextManager[str]: ...
@overload
def tempdir(
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: GenericPath[AnyStr] | None = ...,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def temppath(
    suffix: None = ...,
    prefix: None = ...,
    dir: None = ...,
    text: bool = ...,
) -> _GeneratorContextManager[str]: ...
@overload
def temppath(
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: GenericPath[AnyStr] | None = ...,
    text: bool = ...,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def assert_no_gc_cycles() -> _GeneratorContextManager[None]: ...
@overload
def assert_no_gc_cycles(
    func: Callable[_P, Any],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> None: ...
def break_cycles() -> None: ...
def run_threaded(func: Callable[[], None], iters: int, pass_count: bool = False) -> None: ...
