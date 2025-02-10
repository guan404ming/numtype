from typing import Any, TypeAlias, overload

import numpy as np
from numpy._typing import (
    NDArray,
    _ArrayLikeAnyString_co as ToAnyStringND,
    _ArrayLikeBytes_co as ToBytesND,
    _ArrayLikeInt_co as ToIntND,
    _ArrayLikeStr_co as ToStrND,
    _ArrayLikeString_co as ToStringND,
    _SupportsArray,
)

_StringArrayLike: TypeAlias = _SupportsArray[np.dtypes.StringDType]

_BoolArray: TypeAlias = NDArray[np.bool]
_IntArray: TypeAlias = NDArray[np.int_]
_StringArray: TypeAlias = np.ndarray[tuple[int, ...], np.dtypes.StringDType]
_StrArray: TypeAlias = NDArray[np.str_]
_BytesArray: TypeAlias = NDArray[np.bytes_]

###

@overload
def equal(x1: ToStrND, x2: ToStrND) -> _BoolArray: ...
@overload
def equal(x1: ToBytesND, x2: ToBytesND) -> _BoolArray: ...
@overload
def equal(x1: ToStringND, x2: ToStringND) -> _BoolArray: ...

#
@overload
def not_equal(x1: ToStrND, x2: ToStrND) -> _BoolArray: ...
@overload
def not_equal(x1: ToBytesND, x2: ToBytesND) -> _BoolArray: ...
@overload
def not_equal(x1: ToStringND, x2: ToStringND) -> _BoolArray: ...

#
@overload
def greater_equal(x1: ToStrND, x2: ToStrND) -> _BoolArray: ...
@overload
def greater_equal(x1: ToBytesND, x2: ToBytesND) -> _BoolArray: ...
@overload
def greater_equal(x1: ToStringND, x2: ToStringND) -> _BoolArray: ...

#
@overload
def less_equal(x1: ToStrND, x2: ToStrND) -> _BoolArray: ...
@overload
def less_equal(x1: ToBytesND, x2: ToBytesND) -> _BoolArray: ...
@overload
def less_equal(x1: ToStringND, x2: ToStringND) -> _BoolArray: ...

#
@overload
def greater(x1: ToStrND, x2: ToStrND) -> _BoolArray: ...
@overload
def greater(x1: ToBytesND, x2: ToBytesND) -> _BoolArray: ...
@overload
def greater(x1: ToStringND, x2: ToStringND) -> _BoolArray: ...

#
@overload
def less(x1: ToStrND, x2: ToStrND) -> _BoolArray: ...
@overload
def less(x1: ToBytesND, x2: ToBytesND) -> _BoolArray: ...
@overload
def less(x1: ToStringND, x2: ToStringND) -> _BoolArray: ...

#
@overload
def add(x1: ToStrND, x2: ToStrND) -> _StrArray: ...
@overload
def add(x1: ToBytesND, x2: ToBytesND) -> _BytesArray: ...
@overload
def add(x1: _StringArrayLike, x2: _StringArrayLike) -> _StringArray: ...
@overload
def add(x1: ToStringND, x2: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def multiply(a: ToStrND, i: ToIntND) -> _StrArray: ...
@overload
def multiply(a: ToBytesND, i: ToIntND) -> _BytesArray: ...
@overload
def multiply(a: _StringArrayLike, i: ToIntND) -> _StringArray: ...
@overload
def multiply(a: ToStringND, i: ToIntND) -> _StrArray | _StringArray: ...

#
@overload
def mod(a: ToStrND, value: Any) -> _StrArray: ...
@overload
def mod(a: ToBytesND, value: Any) -> _BytesArray: ...
@overload
def mod(a: _StringArrayLike, value: Any) -> _StringArray: ...
@overload
def mod(a: ToStringND, value: Any) -> _StrArray | _StringArray: ...

#
def isalpha(x: ToAnyStringND) -> _BoolArray: ...
def isalnum(a: ToAnyStringND) -> _BoolArray: ...
def isdigit(x: ToAnyStringND) -> _BoolArray: ...
def isspace(x: ToAnyStringND) -> _BoolArray: ...
def isdecimal(x: ToStrND | ToStringND) -> _BoolArray: ...
def isnumeric(x: ToStrND | ToStringND) -> _BoolArray: ...
def islower(a: ToAnyStringND) -> _BoolArray: ...
def istitle(a: ToAnyStringND) -> _BoolArray: ...
def isupper(a: ToAnyStringND) -> _BoolArray: ...
def str_len(x: ToAnyStringND) -> _IntArray: ...

#
@overload
def find(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def find(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def find(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def rfind(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rfind(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rfind(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def index(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def index(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def index(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def rindex(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rindex(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rindex(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def count(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def count(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def count(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def startswith(a: ToStrND, prefix: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def startswith(a: ToBytesND, prefix: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def startswith(a: ToStringND, suffix: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...

#
@overload
def endswith(a: ToStrND, suffix: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def endswith(a: ToBytesND, suffix: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def endswith(a: ToStringND, suffix: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...

#
def decode(a: ToBytesND, encoding: str | None = None, errors: str | None = None) -> _StrArray: ...
def encode(a: ToStrND | ToStringND, encoding: str | None = None, errors: str | None = None) -> _BytesArray: ...

#
@overload
def expandtabs(a: ToStrND, tabsize: ToIntND = 8) -> _StrArray: ...
@overload
def expandtabs(a: ToBytesND, tabsize: ToIntND = 8) -> _BytesArray: ...
@overload
def expandtabs(a: _StringArrayLike, tabsize: ToIntND = 8) -> _StringArray: ...
@overload
def expandtabs(a: ToStringND, tabsize: ToIntND = 8) -> _StrArray | _StringArray: ...

#
@overload
def center(a: ToStrND, width: ToIntND, fillchar: ToStrND = ...) -> _StrArray: ...
@overload
def center(a: ToBytesND, width: ToIntND, fillchar: ToBytesND = ...) -> _BytesArray: ...
@overload
def center(a: _StringArrayLike, width: ToIntND, fillchar: _StringArrayLike = ...) -> _StringArray: ...
@overload
def center(a: ToStringND, width: ToIntND, fillchar: ToStringND = ...) -> _StrArray | _StringArray: ...

#
@overload
def ljust(a: ToStrND, width: ToIntND, fillchar: ToStrND = ...) -> _StrArray: ...
@overload
def ljust(a: ToBytesND, width: ToIntND, fillchar: ToBytesND = ...) -> _BytesArray: ...
@overload
def ljust(a: _StringArrayLike, width: ToIntND, fillchar: _StringArrayLike = ...) -> _StringArray: ...
@overload
def ljust(a: ToStringND, width: ToIntND, fillchar: ToStringND = ...) -> _StrArray | _StringArray: ...

#
@overload
def rjust(a: ToStrND, width: ToIntND, fillchar: ToStrND = ...) -> _StrArray: ...
@overload
def rjust(a: ToBytesND, width: ToIntND, fillchar: ToBytesND = ...) -> _BytesArray: ...
@overload
def rjust(a: _StringArrayLike, width: ToIntND, fillchar: _StringArrayLike = ...) -> _StringArray: ...
@overload
def rjust(a: ToStringND, width: ToIntND, fillchar: ToStringND = ...) -> _StrArray | _StringArray: ...

#
@overload
def lstrip(a: ToStrND, chars: ToStrND | None = None) -> _StrArray: ...
@overload
def lstrip(a: ToBytesND, chars: ToBytesND | None = None) -> _BytesArray: ...
@overload
def lstrip(a: _StringArrayLike, chars: _StringArrayLike | None = None) -> _StringArray: ...
@overload
def lstrip(a: ToStringND, chars: ToStringND | None = None) -> _StrArray | _StringArray: ...

#
@overload
def rstrip(a: ToStrND, char: ToStrND | None = None) -> _StrArray: ...
@overload
def rstrip(a: ToBytesND, char: ToBytesND | None = None) -> _BytesArray: ...
@overload
def rstrip(a: _StringArrayLike, chars: _StringArrayLike | None = None) -> _StringArray: ...
@overload
def rstrip(a: ToStringND, chars: ToStringND | None = None) -> _StrArray | _StringArray: ...

#
@overload
def strip(a: ToStrND, chars: ToStrND | None = None) -> _StrArray: ...
@overload
def strip(a: ToBytesND, chars: ToBytesND | None = None) -> _BytesArray: ...
@overload
def strip(a: _StringArrayLike, chars: _StringArrayLike | None = None) -> _StringArray: ...
@overload
def strip(a: ToStringND, chars: ToStringND | None = None) -> _StrArray | _StringArray: ...

#
@overload
def zfill(a: ToStrND, width: ToIntND) -> _StrArray: ...
@overload
def zfill(a: ToBytesND, width: ToIntND) -> _BytesArray: ...
@overload
def zfill(a: _StringArrayLike, width: ToIntND) -> _StringArray: ...
@overload
def zfill(a: ToStringND, width: ToIntND) -> _StrArray | _StringArray: ...

#
@overload
def upper(a: ToStrND) -> _StrArray: ...
@overload
def upper(a: ToBytesND) -> _BytesArray: ...
@overload
def upper(a: _StringArrayLike) -> _StringArray: ...
@overload
def upper(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def lower(a: ToStrND) -> _StrArray: ...
@overload
def lower(a: ToBytesND) -> _BytesArray: ...
@overload
def lower(a: _StringArrayLike) -> _StringArray: ...
@overload
def lower(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def swapcase(a: ToStrND) -> _StrArray: ...
@overload
def swapcase(a: ToBytesND) -> _BytesArray: ...
@overload
def swapcase(a: _StringArrayLike) -> _StringArray: ...
@overload
def swapcase(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def capitalize(a: ToStrND) -> _StrArray: ...
@overload
def capitalize(a: ToBytesND) -> _BytesArray: ...
@overload
def capitalize(a: _StringArrayLike) -> _StringArray: ...
@overload
def capitalize(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def title(a: ToStrND) -> _StrArray: ...
@overload
def title(a: ToBytesND) -> _BytesArray: ...
@overload
def title(a: _StringArrayLike) -> _StringArray: ...
@overload
def title(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def replace(a: ToStrND, old: ToStrND, new: ToStrND, count: ToIntND = -1) -> _StrArray: ...
@overload
def replace(a: ToBytesND, old: ToBytesND, new: ToBytesND, count: ToIntND = -1) -> _BytesArray: ...
@overload
def replace(a: _StringArrayLike, old: _StringArrayLike, new: _StringArrayLike, count: ToIntND = -1) -> _StringArray: ...
@overload
def replace(a: ToStringND, old: ToStringND, new: ToStringND, count: ToIntND = -1) -> _StrArray | _StringArray: ...

#
@overload
def join(sep: ToStrND, seq: ToStrND) -> _StrArray: ...
@overload
def join(sep: ToBytesND, seq: ToBytesND) -> _BytesArray: ...
@overload
def join(sep: _StringArrayLike, seq: _StringArrayLike) -> _StringArray: ...
@overload
def join(sep: ToStringND, seq: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def partition(a: ToStrND, sep: ToStrND) -> _StrArray: ...
@overload
def partition(a: ToBytesND, sep: ToBytesND) -> _BytesArray: ...
@overload
def partition(a: _StringArrayLike, sep: _StringArrayLike) -> _StringArray: ...
@overload
def partition(a: ToStringND, sep: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def rpartition(a: ToStrND, sep: ToStrND) -> _StrArray: ...
@overload
def rpartition(a: ToBytesND, sep: ToBytesND) -> _BytesArray: ...
@overload
def rpartition(a: _StringArrayLike, sep: _StringArrayLike) -> _StringArray: ...
@overload
def rpartition(a: ToStringND, sep: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def translate(a: ToStrND, table: str, deletechars: str | None = None) -> _StrArray: ...
@overload
def translate(a: ToBytesND, table: str, deletechars: str | None = None) -> _BytesArray: ...
@overload
def translate(a: _StringArrayLike, table: str, deletechars: str | None = None) -> _StringArray: ...
@overload
def translate(a: ToStringND, table: str, deletechars: str | None = None) -> _StrArray | _StringArray: ...
