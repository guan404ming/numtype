# @generated 2025-03-06T16:09:38Z
from typing_extensions import assert_type

import numpy as np

###
# scalars

b0: bool
b1: np.bool
u1: np.uint8
u2: np.uint16
u4: np.uint32
u8: np.uint64
i1: np.int8
i2: np.int16
i4: np.int32
i8: np.int64
f2: np.float16
f4: np.float32
f8: np.float64
ld: np.longdouble
c8: np.complex64
c16: np.complex128
cld: np.clongdouble
m8: np.timedelta64
M8: np.datetime64

###
# __[r]add__

assert_type(b1 + b0, np.bool)
assert_type(b1 + b1, np.bool)
assert_type(b1 + u1, np.uint8)
assert_type(b1 + u2, np.uint16)
assert_type(b1 + u4, np.uint32)
assert_type(b1 + u8, np.uint64)
assert_type(b1 + i1, np.int8)
assert_type(b1 + i2, np.int16)
assert_type(b1 + i4, np.int32)
assert_type(b1 + i8, np.int64)
assert_type(b1 + f2, np.float16)
assert_type(b1 + f4, np.float32)
assert_type(b1 + f8, np.float64)
assert_type(b1 + ld, np.longdouble)
assert_type(b1 + c8, np.complex64)
assert_type(b1 + c16, np.complex128)
assert_type(b1 + cld, np.clongdouble)
assert_type(b1 + m8, np.timedelta64)
assert_type(b1 + M8, np.datetime64)

assert_type(u1 + b0, np.uint8)
assert_type(u1 + b1, np.uint8)
assert_type(u1 + u1, np.uint8)
assert_type(u1 + u2, np.uint16)
assert_type(u1 + u4, np.uint32)
assert_type(u1 + u8, np.uint64)
assert_type(u1 + i1, np.int16)
assert_type(u1 + i2, np.int16)
assert_type(u1 + i4, np.int32)
assert_type(u1 + i8, np.int64)
assert_type(u1 + f2, np.float16)
assert_type(u1 + f4, np.float32)
assert_type(u1 + f8, np.float64)
assert_type(u1 + ld, np.longdouble)
assert_type(u1 + c8, np.complex64)
assert_type(u1 + c16, np.complex128)
assert_type(u1 + cld, np.clongdouble)
assert_type(u1 + m8, np.timedelta64)
assert_type(u1 + M8, np.datetime64)

assert_type(u2 + b0, np.uint16)
assert_type(u2 + b1, np.uint16)
assert_type(u2 + u1, np.uint16)
assert_type(u2 + u2, np.uint16)
assert_type(u2 + u4, np.uint32)
assert_type(u2 + u8, np.uint64)
assert_type(u2 + i1, np.int32)
assert_type(u2 + i2, np.int32)
assert_type(u2 + i4, np.int32)
assert_type(u2 + i8, np.int64)
assert_type(u2 + f2, np.float32)
assert_type(u2 + f4, np.float32)
assert_type(u2 + f8, np.float64)
assert_type(u2 + ld, np.longdouble)
assert_type(u2 + c8, np.complex64)
assert_type(u2 + c16, np.complex128)
assert_type(u2 + cld, np.clongdouble)
assert_type(u2 + m8, np.timedelta64)
assert_type(u2 + M8, np.datetime64)

assert_type(u4 + b0, np.uint32)
assert_type(u4 + b1, np.uint32)
assert_type(u4 + u1, np.uint32)
assert_type(u4 + u2, np.uint32)
assert_type(u4 + u4, np.uint32)
assert_type(u4 + u8, np.uint64)
assert_type(u4 + i1, np.int64)
assert_type(u4 + i2, np.int64)
assert_type(u4 + i4, np.int64)
assert_type(u4 + i8, np.int64)
assert_type(u4 + f2, np.float64)
assert_type(u4 + f4, np.float64)
assert_type(u4 + f8, np.float64)
assert_type(u4 + ld, np.longdouble)
assert_type(u4 + c8, np.complex128)
assert_type(u4 + c16, np.complex128)
assert_type(u4 + cld, np.clongdouble)
assert_type(u4 + m8, np.timedelta64)
assert_type(u4 + M8, np.datetime64)

assert_type(u8 + b0, np.uint64)
assert_type(u8 + b1, np.uint64)
assert_type(u8 + u1, np.uint64)
assert_type(u8 + u2, np.uint64)
assert_type(u8 + u4, np.uint64)
assert_type(u8 + u8, np.uint64)
assert_type(u8 + i1, np.float64)
assert_type(u8 + i2, np.float64)
assert_type(u8 + i4, np.float64)
assert_type(u8 + i8, np.float64)
assert_type(u8 + f2, np.float64)
assert_type(u8 + f4, np.float64)
assert_type(u8 + f8, np.float64)
assert_type(u8 + ld, np.longdouble)
assert_type(u8 + c8, np.complex128)
assert_type(u8 + c16, np.complex128)
assert_type(u8 + cld, np.clongdouble)
assert_type(u8 + m8, np.timedelta64)
assert_type(u8 + M8, np.datetime64)

assert_type(i1 + b0, np.int8)
assert_type(i1 + b1, np.int8)
assert_type(i1 + u1, np.int16)
assert_type(i1 + u2, np.int32)
assert_type(i1 + u4, np.int64)
assert_type(i1 + u8, np.float64)
assert_type(i1 + i1, np.int8)
assert_type(i1 + i2, np.int16)
assert_type(i1 + i4, np.int32)
assert_type(i1 + i8, np.int64)
assert_type(i1 + f2, np.float16)
assert_type(i1 + f4, np.float32)
assert_type(i1 + f8, np.float64)
assert_type(i1 + ld, np.longdouble)
assert_type(i1 + c8, np.complex64)
assert_type(i1 + c16, np.complex128)
assert_type(i1 + cld, np.clongdouble)
assert_type(i1 + m8, np.timedelta64)
assert_type(i1 + M8, np.datetime64)

assert_type(i2 + b0, np.int16)
assert_type(i2 + b1, np.int16)
assert_type(i2 + u1, np.int16)
assert_type(i2 + u2, np.int32)
assert_type(i2 + u4, np.int64)
assert_type(i2 + u8, np.float64)
assert_type(i2 + i1, np.int16)
assert_type(i2 + i2, np.int16)
assert_type(i2 + i4, np.int32)
assert_type(i2 + i8, np.int64)
assert_type(i2 + f2, np.float32)
assert_type(i2 + f4, np.float32)
assert_type(i2 + f8, np.float64)
assert_type(i2 + ld, np.longdouble)
assert_type(i2 + c8, np.complex64)
assert_type(i2 + c16, np.complex128)
assert_type(i2 + cld, np.clongdouble)
assert_type(i2 + m8, np.timedelta64)
assert_type(i2 + M8, np.datetime64)

assert_type(i4 + b0, np.int32)
assert_type(i4 + b1, np.int32)
assert_type(i4 + u1, np.int32)
assert_type(i4 + u2, np.int32)
assert_type(i4 + u4, np.int64)
assert_type(i4 + u8, np.float64)
assert_type(i4 + i1, np.int32)
assert_type(i4 + i2, np.int32)
assert_type(i4 + i4, np.int32)
assert_type(i4 + i8, np.int64)
assert_type(i4 + f2, np.float64)
assert_type(i4 + f4, np.float64)
assert_type(i4 + f8, np.float64)
assert_type(i4 + ld, np.longdouble)
assert_type(i4 + c8, np.complex128)
assert_type(i4 + c16, np.complex128)
assert_type(i4 + cld, np.clongdouble)
assert_type(i4 + m8, np.timedelta64)
assert_type(i4 + M8, np.datetime64)

assert_type(i8 + b0, np.int64)
assert_type(i8 + b1, np.int64)
assert_type(i8 + u1, np.int64)
assert_type(i8 + u2, np.int64)
assert_type(i8 + u4, np.int64)
assert_type(i8 + u8, np.float64)
assert_type(i8 + i1, np.int64)
assert_type(i8 + i2, np.int64)
assert_type(i8 + i4, np.int64)
assert_type(i8 + i8, np.int64)
assert_type(i8 + f2, np.float64)
assert_type(i8 + f4, np.float64)
assert_type(i8 + f8, np.float64)
assert_type(i8 + ld, np.longdouble)
assert_type(i8 + c8, np.complex128)
assert_type(i8 + c16, np.complex128)
assert_type(i8 + cld, np.clongdouble)
assert_type(i8 + m8, np.timedelta64)
assert_type(i8 + M8, np.datetime64)

assert_type(f2 + b0, np.float16)
assert_type(f2 + b1, np.float16)
assert_type(f2 + u1, np.float16)
assert_type(f2 + u2, np.float32)
assert_type(f2 + u4, np.float64)
assert_type(f2 + u8, np.float64)
assert_type(f2 + i1, np.float16)
assert_type(f2 + i2, np.float32)
assert_type(f2 + i4, np.float64)
assert_type(f2 + i8, np.float64)
assert_type(f2 + f2, np.float16)
assert_type(f2 + f4, np.float32)
assert_type(f2 + f8, np.float64)
assert_type(f2 + ld, np.longdouble)
assert_type(f2 + c8, np.complex64)
assert_type(f2 + c16, np.complex128)
assert_type(f2 + cld, np.clongdouble)
f2 + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4 + b0, np.float32)
assert_type(f4 + b1, np.float32)
assert_type(f4 + u1, np.float32)
assert_type(f4 + u2, np.float32)
assert_type(f4 + u4, np.float64)
assert_type(f4 + u8, np.float64)
assert_type(f4 + i1, np.float32)
assert_type(f4 + i2, np.float32)
assert_type(f4 + i4, np.float64)
assert_type(f4 + i8, np.float64)
assert_type(f4 + f2, np.float32)
assert_type(f4 + f4, np.float32)
assert_type(f4 + f8, np.float64)
assert_type(f4 + ld, np.longdouble)
assert_type(f4 + c8, np.complex64)
assert_type(f4 + c16, np.complex128)
assert_type(f4 + cld, np.clongdouble)
f4 + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8 + b0, np.float64)
assert_type(f8 + b1, np.float64)
assert_type(f8 + u1, np.float64)
assert_type(f8 + u2, np.float64)
assert_type(f8 + u4, np.float64)
assert_type(f8 + u8, np.float64)
assert_type(f8 + i1, np.float64)
assert_type(f8 + i2, np.float64)
assert_type(f8 + i4, np.float64)
assert_type(f8 + i8, np.float64)
assert_type(f8 + f2, np.float64)
assert_type(f8 + f4, np.float64)
assert_type(f8 + f8, np.float64)
assert_type(f8 + ld, np.longdouble)
assert_type(f8 + c8, np.complex128)
assert_type(f8 + c16, np.complex128)
assert_type(f8 + cld, np.clongdouble)
f8 + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(ld + b0, np.longdouble)
assert_type(ld + b1, np.longdouble)
assert_type(ld + u1, np.longdouble)
assert_type(ld + u2, np.longdouble)
assert_type(ld + u4, np.longdouble)
assert_type(ld + u8, np.longdouble)
assert_type(ld + i1, np.longdouble)
assert_type(ld + i2, np.longdouble)
assert_type(ld + i4, np.longdouble)
assert_type(ld + i8, np.longdouble)
assert_type(ld + f2, np.longdouble)
assert_type(ld + f4, np.longdouble)
assert_type(ld + f8, np.longdouble)
assert_type(ld + ld, np.longdouble)
assert_type(ld + c8, np.clongdouble)
assert_type(ld + c16, np.clongdouble)
assert_type(ld + cld, np.clongdouble)
ld + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c8 + b0, np.complex64)
assert_type(c8 + b1, np.complex64)
assert_type(c8 + u1, np.complex64)
assert_type(c8 + u2, np.complex64)
assert_type(c8 + u4, np.complex128)
assert_type(c8 + u8, np.complex128)
assert_type(c8 + i1, np.complex64)
assert_type(c8 + i2, np.complex64)
assert_type(c8 + i4, np.complex128)
assert_type(c8 + i8, np.complex128)
assert_type(c8 + f2, np.complex64)
assert_type(c8 + f4, np.complex64)
assert_type(c8 + f8, np.complex128)
assert_type(c8 + ld, np.clongdouble)
assert_type(c8 + c8, np.complex64)
assert_type(c8 + c16, np.complex128)
assert_type(c8 + cld, np.clongdouble)
c8 + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16 + b0, np.complex128)
assert_type(c16 + b1, np.complex128)
assert_type(c16 + u1, np.complex128)
assert_type(c16 + u2, np.complex128)
assert_type(c16 + u4, np.complex128)
assert_type(c16 + u8, np.complex128)
assert_type(c16 + i1, np.complex128)
assert_type(c16 + i2, np.complex128)
assert_type(c16 + i4, np.complex128)
assert_type(c16 + i8, np.complex128)
assert_type(c16 + f2, np.complex128)
assert_type(c16 + f4, np.complex128)
assert_type(c16 + f8, np.complex128)
assert_type(c16 + ld, np.clongdouble)
assert_type(c16 + c8, np.complex128)
assert_type(c16 + c16, np.complex128)
assert_type(c16 + cld, np.clongdouble)
c16 + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld + b0, np.clongdouble)
assert_type(cld + b1, np.clongdouble)
assert_type(cld + u1, np.clongdouble)
assert_type(cld + u2, np.clongdouble)
assert_type(cld + u4, np.clongdouble)
assert_type(cld + u8, np.clongdouble)
assert_type(cld + i1, np.clongdouble)
assert_type(cld + i2, np.clongdouble)
assert_type(cld + i4, np.clongdouble)
assert_type(cld + i8, np.clongdouble)
assert_type(cld + f2, np.clongdouble)
assert_type(cld + f4, np.clongdouble)
assert_type(cld + f8, np.clongdouble)
assert_type(cld + ld, np.clongdouble)
assert_type(cld + c8, np.clongdouble)
assert_type(cld + c16, np.clongdouble)
assert_type(cld + cld, np.clongdouble)
cld + m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8 + b0, np.timedelta64)
assert_type(m8 + b1, np.timedelta64)
assert_type(m8 + u1, np.timedelta64)
assert_type(m8 + u2, np.timedelta64)
assert_type(m8 + u4, np.timedelta64)
assert_type(m8 + u8, np.timedelta64)
assert_type(m8 + i1, np.timedelta64)
assert_type(m8 + i2, np.timedelta64)
assert_type(m8 + i4, np.timedelta64)
assert_type(m8 + i8, np.timedelta64)
m8 + f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 + f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 + f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 + ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 + c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 + c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 + cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 + m8, np.timedelta64)
assert_type(m8 + M8, np.datetime64)

assert_type(M8 + b0, np.datetime64)
assert_type(M8 + b1, np.datetime64)
assert_type(M8 + u1, np.datetime64)
assert_type(M8 + u2, np.datetime64)
assert_type(M8 + u4, np.datetime64)
assert_type(M8 + u8, np.datetime64)
assert_type(M8 + i1, np.datetime64)
assert_type(M8 + i2, np.datetime64)
assert_type(M8 + i4, np.datetime64)
assert_type(M8 + i8, np.datetime64)
M8 + f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 + f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 + f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 + ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 + c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 + c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 + cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8 + m8, np.datetime64)
M8 + M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]sub__

b1 - b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 - u1, np.uint8)
assert_type(b1 - u2, np.uint16)
assert_type(b1 - u4, np.uint32)
assert_type(b1 - u8, np.uint64)
assert_type(b1 - i1, np.int8)
assert_type(b1 - i2, np.int16)
assert_type(b1 - i4, np.int32)
assert_type(b1 - i8, np.int64)
assert_type(b1 - f2, np.float16)
assert_type(b1 - f4, np.float32)
assert_type(b1 - f8, np.float64)
assert_type(b1 - ld, np.longdouble)
assert_type(b1 - c8, np.complex64)
assert_type(b1 - c16, np.complex128)
assert_type(b1 - cld, np.clongdouble)
assert_type(b1 - m8, np.timedelta64)
b1 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1 - b0, np.uint8)
assert_type(u1 - b1, np.uint8)
assert_type(u1 - u1, np.uint8)
assert_type(u1 - u2, np.uint16)
assert_type(u1 - u4, np.uint32)
assert_type(u1 - u8, np.uint64)
assert_type(u1 - i1, np.int16)
assert_type(u1 - i2, np.int16)
assert_type(u1 - i4, np.int32)
assert_type(u1 - i8, np.int64)
assert_type(u1 - f2, np.float16)
assert_type(u1 - f4, np.float32)
assert_type(u1 - f8, np.float64)
assert_type(u1 - ld, np.longdouble)
assert_type(u1 - c8, np.complex64)
assert_type(u1 - c16, np.complex128)
assert_type(u1 - cld, np.clongdouble)
assert_type(u1 - m8, np.timedelta64)
u1 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2 - b0, np.uint16)
assert_type(u2 - b1, np.uint16)
assert_type(u2 - u1, np.uint16)
assert_type(u2 - u2, np.uint16)
assert_type(u2 - u4, np.uint32)
assert_type(u2 - u8, np.uint64)
assert_type(u2 - i1, np.int32)
assert_type(u2 - i2, np.int32)
assert_type(u2 - i4, np.int32)
assert_type(u2 - i8, np.int64)
assert_type(u2 - f2, np.float32)
assert_type(u2 - f4, np.float32)
assert_type(u2 - f8, np.float64)
assert_type(u2 - ld, np.longdouble)
assert_type(u2 - c8, np.complex64)
assert_type(u2 - c16, np.complex128)
assert_type(u2 - cld, np.clongdouble)
assert_type(u2 - m8, np.timedelta64)
u2 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4 - b0, np.uint32)
assert_type(u4 - b1, np.uint32)
assert_type(u4 - u1, np.uint32)
assert_type(u4 - u2, np.uint32)
assert_type(u4 - u4, np.uint32)
assert_type(u4 - u8, np.uint64)
assert_type(u4 - i1, np.int64)
assert_type(u4 - i2, np.int64)
assert_type(u4 - i4, np.int64)
assert_type(u4 - i8, np.int64)
assert_type(u4 - f2, np.float64)
assert_type(u4 - f4, np.float64)
assert_type(u4 - f8, np.float64)
assert_type(u4 - ld, np.longdouble)
assert_type(u4 - c8, np.complex128)
assert_type(u4 - c16, np.complex128)
assert_type(u4 - cld, np.clongdouble)
assert_type(u4 - m8, np.timedelta64)
u4 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 - b0, np.uint64)
assert_type(u8 - b1, np.uint64)
assert_type(u8 - u1, np.uint64)
assert_type(u8 - u2, np.uint64)
assert_type(u8 - u4, np.uint64)
assert_type(u8 - u8, np.uint64)
assert_type(u8 - i1, np.float64)
assert_type(u8 - i2, np.float64)
assert_type(u8 - i4, np.float64)
assert_type(u8 - i8, np.float64)
assert_type(u8 - f2, np.float64)
assert_type(u8 - f4, np.float64)
assert_type(u8 - f8, np.float64)
assert_type(u8 - ld, np.longdouble)
assert_type(u8 - c8, np.complex128)
assert_type(u8 - c16, np.complex128)
assert_type(u8 - cld, np.clongdouble)
assert_type(u8 - m8, np.timedelta64)
u8 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 - b0, np.int8)
assert_type(i1 - b1, np.int8)
assert_type(i1 - u1, np.int16)
assert_type(i1 - u2, np.int32)
assert_type(i1 - u4, np.int64)
assert_type(i1 - u8, np.float64)
assert_type(i1 - i1, np.int8)
assert_type(i1 - i2, np.int16)
assert_type(i1 - i4, np.int32)
assert_type(i1 - i8, np.int64)
assert_type(i1 - f2, np.float16)
assert_type(i1 - f4, np.float32)
assert_type(i1 - f8, np.float64)
assert_type(i1 - ld, np.longdouble)
assert_type(i1 - c8, np.complex64)
assert_type(i1 - c16, np.complex128)
assert_type(i1 - cld, np.clongdouble)
assert_type(i1 - m8, np.timedelta64)
i1 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2 - b0, np.int16)
assert_type(i2 - b1, np.int16)
assert_type(i2 - u1, np.int16)
assert_type(i2 - u2, np.int32)
assert_type(i2 - u4, np.int64)
assert_type(i2 - u8, np.float64)
assert_type(i2 - i1, np.int16)
assert_type(i2 - i2, np.int16)
assert_type(i2 - i4, np.int32)
assert_type(i2 - i8, np.int64)
assert_type(i2 - f2, np.float32)
assert_type(i2 - f4, np.float32)
assert_type(i2 - f8, np.float64)
assert_type(i2 - ld, np.longdouble)
assert_type(i2 - c8, np.complex64)
assert_type(i2 - c16, np.complex128)
assert_type(i2 - cld, np.clongdouble)
assert_type(i2 - m8, np.timedelta64)
i2 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4 - b0, np.int32)
assert_type(i4 - b1, np.int32)
assert_type(i4 - u1, np.int32)
assert_type(i4 - u2, np.int32)
assert_type(i4 - u4, np.int64)
assert_type(i4 - u8, np.float64)
assert_type(i4 - i1, np.int32)
assert_type(i4 - i2, np.int32)
assert_type(i4 - i4, np.int32)
assert_type(i4 - i8, np.int64)
assert_type(i4 - f2, np.float64)
assert_type(i4 - f4, np.float64)
assert_type(i4 - f8, np.float64)
assert_type(i4 - ld, np.longdouble)
assert_type(i4 - c8, np.complex128)
assert_type(i4 - c16, np.complex128)
assert_type(i4 - cld, np.clongdouble)
assert_type(i4 - m8, np.timedelta64)
i4 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 - b0, np.int64)
assert_type(i8 - b1, np.int64)
assert_type(i8 - u1, np.int64)
assert_type(i8 - u2, np.int64)
assert_type(i8 - u4, np.int64)
assert_type(i8 - u8, np.float64)
assert_type(i8 - i1, np.int64)
assert_type(i8 - i2, np.int64)
assert_type(i8 - i4, np.int64)
assert_type(i8 - i8, np.int64)
assert_type(i8 - f2, np.float64)
assert_type(i8 - f4, np.float64)
assert_type(i8 - f8, np.float64)
assert_type(i8 - ld, np.longdouble)
assert_type(i8 - c8, np.complex128)
assert_type(i8 - c16, np.complex128)
assert_type(i8 - cld, np.clongdouble)
assert_type(i8 - m8, np.timedelta64)
i8 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2 - b0, np.float16)
assert_type(f2 - b1, np.float16)
assert_type(f2 - u1, np.float16)
assert_type(f2 - u2, np.float32)
assert_type(f2 - u4, np.float64)
assert_type(f2 - u8, np.float64)
assert_type(f2 - i1, np.float16)
assert_type(f2 - i2, np.float32)
assert_type(f2 - i4, np.float64)
assert_type(f2 - i8, np.float64)
assert_type(f2 - f2, np.float16)
assert_type(f2 - f4, np.float32)
assert_type(f2 - f8, np.float64)
assert_type(f2 - ld, np.longdouble)
assert_type(f2 - c8, np.complex64)
assert_type(f2 - c16, np.complex128)
assert_type(f2 - cld, np.clongdouble)
f2 - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4 - b0, np.float32)
assert_type(f4 - b1, np.float32)
assert_type(f4 - u1, np.float32)
assert_type(f4 - u2, np.float32)
assert_type(f4 - u4, np.float64)
assert_type(f4 - u8, np.float64)
assert_type(f4 - i1, np.float32)
assert_type(f4 - i2, np.float32)
assert_type(f4 - i4, np.float64)
assert_type(f4 - i8, np.float64)
assert_type(f4 - f2, np.float32)
assert_type(f4 - f4, np.float32)
assert_type(f4 - f8, np.float64)
assert_type(f4 - ld, np.longdouble)
assert_type(f4 - c8, np.complex64)
assert_type(f4 - c16, np.complex128)
assert_type(f4 - cld, np.clongdouble)
f4 - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8 - b0, np.float64)
assert_type(f8 - b1, np.float64)
assert_type(f8 - u1, np.float64)
assert_type(f8 - u2, np.float64)
assert_type(f8 - u4, np.float64)
assert_type(f8 - u8, np.float64)
assert_type(f8 - i1, np.float64)
assert_type(f8 - i2, np.float64)
assert_type(f8 - i4, np.float64)
assert_type(f8 - i8, np.float64)
assert_type(f8 - f2, np.float64)
assert_type(f8 - f4, np.float64)
assert_type(f8 - f8, np.float64)
assert_type(f8 - ld, np.longdouble)
assert_type(f8 - c8, np.complex128)
assert_type(f8 - c16, np.complex128)
assert_type(f8 - cld, np.clongdouble)
f8 - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(ld - b0, np.longdouble)
assert_type(ld - b1, np.longdouble)
assert_type(ld - u1, np.longdouble)
assert_type(ld - u2, np.longdouble)
assert_type(ld - u4, np.longdouble)
assert_type(ld - u8, np.longdouble)
assert_type(ld - i1, np.longdouble)
assert_type(ld - i2, np.longdouble)
assert_type(ld - i4, np.longdouble)
assert_type(ld - i8, np.longdouble)
assert_type(ld - f2, np.longdouble)
assert_type(ld - f4, np.longdouble)
assert_type(ld - f8, np.longdouble)
assert_type(ld - ld, np.longdouble)
assert_type(ld - c8, np.clongdouble)
assert_type(ld - c16, np.clongdouble)
assert_type(ld - cld, np.clongdouble)
ld - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c8 - b0, np.complex64)
assert_type(c8 - b1, np.complex64)
assert_type(c8 - u1, np.complex64)
assert_type(c8 - u2, np.complex64)
assert_type(c8 - u4, np.complex128)
assert_type(c8 - u8, np.complex128)
assert_type(c8 - i1, np.complex64)
assert_type(c8 - i2, np.complex64)
assert_type(c8 - i4, np.complex128)
assert_type(c8 - i8, np.complex128)
assert_type(c8 - f2, np.complex64)
assert_type(c8 - f4, np.complex64)
assert_type(c8 - f8, np.complex128)
assert_type(c8 - ld, np.clongdouble)
assert_type(c8 - c8, np.complex64)
assert_type(c8 - c16, np.complex128)
assert_type(c8 - cld, np.clongdouble)
c8 - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16 - b0, np.complex128)
assert_type(c16 - b1, np.complex128)
assert_type(c16 - u1, np.complex128)
assert_type(c16 - u2, np.complex128)
assert_type(c16 - u4, np.complex128)
assert_type(c16 - u8, np.complex128)
assert_type(c16 - i1, np.complex128)
assert_type(c16 - i2, np.complex128)
assert_type(c16 - i4, np.complex128)
assert_type(c16 - i8, np.complex128)
assert_type(c16 - f2, np.complex128)
assert_type(c16 - f4, np.complex128)
assert_type(c16 - f8, np.complex128)
assert_type(c16 - ld, np.clongdouble)
assert_type(c16 - c8, np.complex128)
assert_type(c16 - c16, np.complex128)
assert_type(c16 - cld, np.clongdouble)
c16 - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld - b0, np.clongdouble)
assert_type(cld - b1, np.clongdouble)
assert_type(cld - u1, np.clongdouble)
assert_type(cld - u2, np.clongdouble)
assert_type(cld - u4, np.clongdouble)
assert_type(cld - u8, np.clongdouble)
assert_type(cld - i1, np.clongdouble)
assert_type(cld - i2, np.clongdouble)
assert_type(cld - i4, np.clongdouble)
assert_type(cld - i8, np.clongdouble)
assert_type(cld - f2, np.clongdouble)
assert_type(cld - f4, np.clongdouble)
assert_type(cld - f8, np.clongdouble)
assert_type(cld - ld, np.clongdouble)
assert_type(cld - c8, np.clongdouble)
assert_type(cld - c16, np.clongdouble)
assert_type(cld - cld, np.clongdouble)
cld - m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8 - b0, np.timedelta64)
assert_type(m8 - b1, np.timedelta64)
assert_type(m8 - u1, np.timedelta64)
assert_type(m8 - u2, np.timedelta64)
assert_type(m8 - u4, np.timedelta64)
assert_type(m8 - u8, np.timedelta64)
assert_type(m8 - i1, np.timedelta64)
assert_type(m8 - i2, np.timedelta64)
assert_type(m8 - i4, np.timedelta64)
assert_type(m8 - i8, np.timedelta64)
m8 - f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 - f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 - f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 - ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 - c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 - c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 - cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 - m8, np.timedelta64)
m8 - M8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(M8 - b0, np.datetime64)
assert_type(M8 - b1, np.datetime64)
assert_type(M8 - u1, np.datetime64)
assert_type(M8 - u2, np.datetime64)
assert_type(M8 - u4, np.datetime64)
assert_type(M8 - u8, np.datetime64)
assert_type(M8 - i1, np.datetime64)
assert_type(M8 - i2, np.datetime64)
assert_type(M8 - i4, np.datetime64)
assert_type(M8 - i8, np.datetime64)
M8 - f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 - f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 - f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 - ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 - c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 - c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8 - cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8 - m8, np.datetime64)
assert_type(M8 - M8, np.timedelta64)

###
# __[r]mul__

assert_type(b1 * b0, np.bool)
assert_type(b1 * b1, np.bool)
assert_type(b1 * u1, np.uint8)
assert_type(b1 * u2, np.uint16)
assert_type(b1 * u4, np.uint32)
assert_type(b1 * u8, np.uint64)
assert_type(b1 * i1, np.int8)
assert_type(b1 * i2, np.int16)
assert_type(b1 * i4, np.int32)
assert_type(b1 * i8, np.int64)
assert_type(b1 * f2, np.float16)
assert_type(b1 * f4, np.float32)
assert_type(b1 * f8, np.float64)
assert_type(b1 * ld, np.longdouble)
assert_type(b1 * c8, np.complex64)
assert_type(b1 * c16, np.complex128)
assert_type(b1 * cld, np.clongdouble)
assert_type(b1 * m8, np.timedelta64)

assert_type(u1 * b0, np.uint8)
assert_type(u1 * b1, np.uint8)
assert_type(u1 * u1, np.uint8)
assert_type(u1 * u2, np.uint16)
assert_type(u1 * u4, np.uint32)
assert_type(u1 * u8, np.uint64)
assert_type(u1 * i1, np.int16)
assert_type(u1 * i2, np.int16)
assert_type(u1 * i4, np.int32)
assert_type(u1 * i8, np.int64)
assert_type(u1 * f2, np.float16)
assert_type(u1 * f4, np.float32)
assert_type(u1 * f8, np.float64)
assert_type(u1 * ld, np.longdouble)
assert_type(u1 * c8, np.complex64)
assert_type(u1 * c16, np.complex128)
assert_type(u1 * cld, np.clongdouble)
assert_type(u1 * m8, np.timedelta64)

assert_type(u2 * b0, np.uint16)
assert_type(u2 * b1, np.uint16)
assert_type(u2 * u1, np.uint16)
assert_type(u2 * u2, np.uint16)
assert_type(u2 * u4, np.uint32)
assert_type(u2 * u8, np.uint64)
assert_type(u2 * i1, np.int32)
assert_type(u2 * i2, np.int32)
assert_type(u2 * i4, np.int32)
assert_type(u2 * i8, np.int64)
assert_type(u2 * f2, np.float32)
assert_type(u2 * f4, np.float32)
assert_type(u2 * f8, np.float64)
assert_type(u2 * ld, np.longdouble)
assert_type(u2 * c8, np.complex64)
assert_type(u2 * c16, np.complex128)
assert_type(u2 * cld, np.clongdouble)
assert_type(u2 * m8, np.timedelta64)

assert_type(u4 * b0, np.uint32)
assert_type(u4 * b1, np.uint32)
assert_type(u4 * u1, np.uint32)
assert_type(u4 * u2, np.uint32)
assert_type(u4 * u4, np.uint32)
assert_type(u4 * u8, np.uint64)
assert_type(u4 * i1, np.int64)
assert_type(u4 * i2, np.int64)
assert_type(u4 * i4, np.int64)
assert_type(u4 * i8, np.int64)
assert_type(u4 * f2, np.float64)
assert_type(u4 * f4, np.float64)
assert_type(u4 * f8, np.float64)
assert_type(u4 * ld, np.longdouble)
assert_type(u4 * c8, np.complex128)
assert_type(u4 * c16, np.complex128)
assert_type(u4 * cld, np.clongdouble)
assert_type(u4 * m8, np.timedelta64)

assert_type(u8 * b0, np.uint64)
assert_type(u8 * b1, np.uint64)
assert_type(u8 * u1, np.uint64)
assert_type(u8 * u2, np.uint64)
assert_type(u8 * u4, np.uint64)
assert_type(u8 * u8, np.uint64)
assert_type(u8 * i1, np.float64)
assert_type(u8 * i2, np.float64)
assert_type(u8 * i4, np.float64)
assert_type(u8 * i8, np.float64)
assert_type(u8 * f2, np.float64)
assert_type(u8 * f4, np.float64)
assert_type(u8 * f8, np.float64)
assert_type(u8 * ld, np.longdouble)
assert_type(u8 * c8, np.complex128)
assert_type(u8 * c16, np.complex128)
assert_type(u8 * cld, np.clongdouble)
assert_type(u8 * m8, np.timedelta64)

assert_type(i1 * b0, np.int8)
assert_type(i1 * b1, np.int8)
assert_type(i1 * u1, np.int16)
assert_type(i1 * u2, np.int32)
assert_type(i1 * u4, np.int64)
assert_type(i1 * u8, np.float64)
assert_type(i1 * i1, np.int8)
assert_type(i1 * i2, np.int16)
assert_type(i1 * i4, np.int32)
assert_type(i1 * i8, np.int64)
assert_type(i1 * f2, np.float16)
assert_type(i1 * f4, np.float32)
assert_type(i1 * f8, np.float64)
assert_type(i1 * ld, np.longdouble)
assert_type(i1 * c8, np.complex64)
assert_type(i1 * c16, np.complex128)
assert_type(i1 * cld, np.clongdouble)
assert_type(i1 * m8, np.timedelta64)

assert_type(i2 * b0, np.int16)
assert_type(i2 * b1, np.int16)
assert_type(i2 * u1, np.int16)
assert_type(i2 * u2, np.int32)
assert_type(i2 * u4, np.int64)
assert_type(i2 * u8, np.float64)
assert_type(i2 * i1, np.int16)
assert_type(i2 * i2, np.int16)
assert_type(i2 * i4, np.int32)
assert_type(i2 * i8, np.int64)
assert_type(i2 * f2, np.float32)
assert_type(i2 * f4, np.float32)
assert_type(i2 * f8, np.float64)
assert_type(i2 * ld, np.longdouble)
assert_type(i2 * c8, np.complex64)
assert_type(i2 * c16, np.complex128)
assert_type(i2 * cld, np.clongdouble)
assert_type(i2 * m8, np.timedelta64)

assert_type(i4 * b0, np.int32)
assert_type(i4 * b1, np.int32)
assert_type(i4 * u1, np.int32)
assert_type(i4 * u2, np.int32)
assert_type(i4 * u4, np.int64)
assert_type(i4 * u8, np.float64)
assert_type(i4 * i1, np.int32)
assert_type(i4 * i2, np.int32)
assert_type(i4 * i4, np.int32)
assert_type(i4 * i8, np.int64)
assert_type(i4 * f2, np.float64)
assert_type(i4 * f4, np.float64)
assert_type(i4 * f8, np.float64)
assert_type(i4 * ld, np.longdouble)
assert_type(i4 * c8, np.complex128)
assert_type(i4 * c16, np.complex128)
assert_type(i4 * cld, np.clongdouble)
assert_type(i4 * m8, np.timedelta64)

assert_type(i8 * b0, np.int64)
assert_type(i8 * b1, np.int64)
assert_type(i8 * u1, np.int64)
assert_type(i8 * u2, np.int64)
assert_type(i8 * u4, np.int64)
assert_type(i8 * u8, np.float64)
assert_type(i8 * i1, np.int64)
assert_type(i8 * i2, np.int64)
assert_type(i8 * i4, np.int64)
assert_type(i8 * i8, np.int64)
assert_type(i8 * f2, np.float64)
assert_type(i8 * f4, np.float64)
assert_type(i8 * f8, np.float64)
assert_type(i8 * ld, np.longdouble)
assert_type(i8 * c8, np.complex128)
assert_type(i8 * c16, np.complex128)
assert_type(i8 * cld, np.clongdouble)
assert_type(i8 * m8, np.timedelta64)

assert_type(f2 * b0, np.float16)
assert_type(f2 * b1, np.float16)
assert_type(f2 * u1, np.float16)
assert_type(f2 * u2, np.float32)
assert_type(f2 * u4, np.float64)
assert_type(f2 * u8, np.float64)
assert_type(f2 * i1, np.float16)
assert_type(f2 * i2, np.float32)
assert_type(f2 * i4, np.float64)
assert_type(f2 * i8, np.float64)
assert_type(f2 * f2, np.float16)
assert_type(f2 * f4, np.float32)
assert_type(f2 * f8, np.float64)
assert_type(f2 * ld, np.longdouble)
assert_type(f2 * c8, np.complex64)
assert_type(f2 * c16, np.complex128)
assert_type(f2 * cld, np.clongdouble)
assert_type(f2 * m8, np.timedelta64)

assert_type(f4 * b0, np.float32)
assert_type(f4 * b1, np.float32)
assert_type(f4 * u1, np.float32)
assert_type(f4 * u2, np.float32)
assert_type(f4 * u4, np.float64)
assert_type(f4 * u8, np.float64)
assert_type(f4 * i1, np.float32)
assert_type(f4 * i2, np.float32)
assert_type(f4 * i4, np.float64)
assert_type(f4 * i8, np.float64)
assert_type(f4 * f2, np.float32)
assert_type(f4 * f4, np.float32)
assert_type(f4 * f8, np.float64)
assert_type(f4 * ld, np.longdouble)
assert_type(f4 * c8, np.complex64)
assert_type(f4 * c16, np.complex128)
assert_type(f4 * cld, np.clongdouble)
assert_type(f4 * m8, np.timedelta64)

assert_type(f8 * b0, np.float64)
assert_type(f8 * b1, np.float64)
assert_type(f8 * u1, np.float64)
assert_type(f8 * u2, np.float64)
assert_type(f8 * u4, np.float64)
assert_type(f8 * u8, np.float64)
assert_type(f8 * i1, np.float64)
assert_type(f8 * i2, np.float64)
assert_type(f8 * i4, np.float64)
assert_type(f8 * i8, np.float64)
assert_type(f8 * f2, np.float64)
assert_type(f8 * f4, np.float64)
assert_type(f8 * f8, np.float64)
assert_type(f8 * ld, np.longdouble)
assert_type(f8 * c8, np.complex128)
assert_type(f8 * c16, np.complex128)
assert_type(f8 * cld, np.clongdouble)
assert_type(f8 * m8, np.timedelta64)

assert_type(ld * b0, np.longdouble)
assert_type(ld * b1, np.longdouble)
assert_type(ld * u1, np.longdouble)
assert_type(ld * u2, np.longdouble)
assert_type(ld * u4, np.longdouble)
assert_type(ld * u8, np.longdouble)
assert_type(ld * i1, np.longdouble)
assert_type(ld * i2, np.longdouble)
assert_type(ld * i4, np.longdouble)
assert_type(ld * i8, np.longdouble)
assert_type(ld * f2, np.longdouble)
assert_type(ld * f4, np.longdouble)
assert_type(ld * f8, np.longdouble)
assert_type(ld * ld, np.longdouble)
assert_type(ld * c8, np.clongdouble)
assert_type(ld * c16, np.clongdouble)
assert_type(ld * cld, np.clongdouble)
assert_type(ld * m8, np.timedelta64)

assert_type(c8 * b0, np.complex64)
assert_type(c8 * b1, np.complex64)
assert_type(c8 * u1, np.complex64)
assert_type(c8 * u2, np.complex64)
assert_type(c8 * u4, np.complex128)
assert_type(c8 * u8, np.complex128)
assert_type(c8 * i1, np.complex64)
assert_type(c8 * i2, np.complex64)
assert_type(c8 * i4, np.complex128)
assert_type(c8 * i8, np.complex128)
assert_type(c8 * f2, np.complex64)
assert_type(c8 * f4, np.complex64)
assert_type(c8 * f8, np.complex128)
assert_type(c8 * ld, np.clongdouble)
assert_type(c8 * c8, np.complex64)
assert_type(c8 * c16, np.complex128)
assert_type(c8 * cld, np.clongdouble)
c8 * m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16 * b0, np.complex128)
assert_type(c16 * b1, np.complex128)
assert_type(c16 * u1, np.complex128)
assert_type(c16 * u2, np.complex128)
assert_type(c16 * u4, np.complex128)
assert_type(c16 * u8, np.complex128)
assert_type(c16 * i1, np.complex128)
assert_type(c16 * i2, np.complex128)
assert_type(c16 * i4, np.complex128)
assert_type(c16 * i8, np.complex128)
assert_type(c16 * f2, np.complex128)
assert_type(c16 * f4, np.complex128)
assert_type(c16 * f8, np.complex128)
assert_type(c16 * ld, np.clongdouble)
assert_type(c16 * c8, np.complex128)
assert_type(c16 * c16, np.complex128)
assert_type(c16 * cld, np.clongdouble)
c16 * m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld * b0, np.clongdouble)
assert_type(cld * b1, np.clongdouble)
assert_type(cld * u1, np.clongdouble)
assert_type(cld * u2, np.clongdouble)
assert_type(cld * u4, np.clongdouble)
assert_type(cld * u8, np.clongdouble)
assert_type(cld * i1, np.clongdouble)
assert_type(cld * i2, np.clongdouble)
assert_type(cld * i4, np.clongdouble)
assert_type(cld * i8, np.clongdouble)
assert_type(cld * f2, np.clongdouble)
assert_type(cld * f4, np.clongdouble)
assert_type(cld * f8, np.clongdouble)
assert_type(cld * ld, np.clongdouble)
assert_type(cld * c8, np.clongdouble)
assert_type(cld * c16, np.clongdouble)
assert_type(cld * cld, np.clongdouble)
cld * m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8 * b0, np.timedelta64)
assert_type(m8 * b1, np.timedelta64)
assert_type(m8 * u1, np.timedelta64)
assert_type(m8 * u2, np.timedelta64)
assert_type(m8 * u4, np.timedelta64)
assert_type(m8 * u8, np.timedelta64)
assert_type(m8 * i1, np.timedelta64)
assert_type(m8 * i2, np.timedelta64)
assert_type(m8 * i4, np.timedelta64)
assert_type(m8 * i8, np.timedelta64)
assert_type(m8 * f2, np.timedelta64)
assert_type(m8 * f4, np.timedelta64)
assert_type(m8 * f8, np.timedelta64)
assert_type(m8 * ld, np.timedelta64)
m8 * c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 * c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 * cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 * m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]pow__

assert_type(b1**b0, np.int8)
assert_type(b1**b1, np.int8)
assert_type(b1**u1, np.uint8)
assert_type(b1**u2, np.uint16)
assert_type(b1**u4, np.uint32)
assert_type(b1**u8, np.uint64)
assert_type(b1**i1, np.int8)
assert_type(b1**i2, np.int16)
assert_type(b1**i4, np.int32)
assert_type(b1**i8, np.int64)
assert_type(b1**f2, np.float16)
assert_type(b1**f4, np.float32)
assert_type(b1**f8, np.float64)
assert_type(b1**ld, np.longdouble)
assert_type(b1**c8, np.complex64)
assert_type(b1**c16, np.complex128)
assert_type(b1**cld, np.clongdouble)

assert_type(u1**b0, np.uint8)
assert_type(u1**b1, np.uint8)
assert_type(u1**u1, np.uint8)
assert_type(u1**u2, np.uint16)
assert_type(u1**u4, np.uint32)
assert_type(u1**u8, np.uint64)
assert_type(u1**i1, np.int16)
assert_type(u1**i2, np.int16)
assert_type(u1**i4, np.int32)
assert_type(u1**i8, np.int64)
assert_type(u1**f2, np.float16)
assert_type(u1**f4, np.float32)
assert_type(u1**f8, np.float64)
assert_type(u1**ld, np.longdouble)
assert_type(u1**c8, np.complex64)
assert_type(u1**c16, np.complex128)
assert_type(u1**cld, np.clongdouble)

assert_type(u2**b0, np.uint16)
assert_type(u2**b1, np.uint16)
assert_type(u2**u1, np.uint16)
assert_type(u2**u2, np.uint16)
assert_type(u2**u4, np.uint32)
assert_type(u2**u8, np.uint64)
assert_type(u2**i1, np.int32)
assert_type(u2**i2, np.int32)
assert_type(u2**i4, np.int32)
assert_type(u2**i8, np.int64)
assert_type(u2**f2, np.float32)
assert_type(u2**f4, np.float32)
assert_type(u2**f8, np.float64)
assert_type(u2**ld, np.longdouble)
assert_type(u2**c8, np.complex64)
assert_type(u2**c16, np.complex128)
assert_type(u2**cld, np.clongdouble)

assert_type(u4**b0, np.uint32)
assert_type(u4**b1, np.uint32)
assert_type(u4**u1, np.uint32)
assert_type(u4**u2, np.uint32)
assert_type(u4**u4, np.uint32)
assert_type(u4**u8, np.uint64)
assert_type(u4**i1, np.int64)
assert_type(u4**i2, np.int64)
assert_type(u4**i4, np.int64)
assert_type(u4**i8, np.int64)
assert_type(u4**f2, np.float64)
assert_type(u4**f4, np.float64)
assert_type(u4**f8, np.float64)
assert_type(u4**ld, np.longdouble)
assert_type(u4**c8, np.complex128)
assert_type(u4**c16, np.complex128)
assert_type(u4**cld, np.clongdouble)

assert_type(u8**b0, np.uint64)
assert_type(u8**b1, np.uint64)
assert_type(u8**u1, np.uint64)
assert_type(u8**u2, np.uint64)
assert_type(u8**u4, np.uint64)
assert_type(u8**u8, np.uint64)
assert_type(u8**i1, np.float64)
assert_type(u8**i2, np.float64)
assert_type(u8**i4, np.float64)
assert_type(u8**i8, np.float64)
assert_type(u8**f2, np.float64)
assert_type(u8**f4, np.float64)
assert_type(u8**f8, np.float64)
assert_type(u8**ld, np.longdouble)
assert_type(u8**c8, np.complex128)
assert_type(u8**c16, np.complex128)
assert_type(u8**cld, np.clongdouble)

assert_type(i1**b0, np.int8)
assert_type(i1**b1, np.int8)
assert_type(i1**u1, np.int16)
assert_type(i1**u2, np.int32)
assert_type(i1**u4, np.int64)
assert_type(i1**u8, np.float64)
assert_type(i1**i1, np.int8)
assert_type(i1**i2, np.int16)
assert_type(i1**i4, np.int32)
assert_type(i1**i8, np.int64)
assert_type(i1**f2, np.float16)
assert_type(i1**f4, np.float32)
assert_type(i1**f8, np.float64)
assert_type(i1**ld, np.longdouble)
assert_type(i1**c8, np.complex64)
assert_type(i1**c16, np.complex128)
assert_type(i1**cld, np.clongdouble)

assert_type(i2**b0, np.int16)
assert_type(i2**b1, np.int16)
assert_type(i2**u1, np.int16)
assert_type(i2**u2, np.int32)
assert_type(i2**u4, np.int64)
assert_type(i2**u8, np.float64)
assert_type(i2**i1, np.int16)
assert_type(i2**i2, np.int16)
assert_type(i2**i4, np.int32)
assert_type(i2**i8, np.int64)
assert_type(i2**f2, np.float32)
assert_type(i2**f4, np.float32)
assert_type(i2**f8, np.float64)
assert_type(i2**ld, np.longdouble)
assert_type(i2**c8, np.complex64)
assert_type(i2**c16, np.complex128)
assert_type(i2**cld, np.clongdouble)

assert_type(i4**b0, np.int32)
assert_type(i4**b1, np.int32)
assert_type(i4**u1, np.int32)
assert_type(i4**u2, np.int32)
assert_type(i4**u4, np.int64)
assert_type(i4**u8, np.float64)
assert_type(i4**i1, np.int32)
assert_type(i4**i2, np.int32)
assert_type(i4**i4, np.int32)
assert_type(i4**i8, np.int64)
assert_type(i4**f2, np.float64)
assert_type(i4**f4, np.float64)
assert_type(i4**f8, np.float64)
assert_type(i4**ld, np.longdouble)
assert_type(i4**c8, np.complex128)
assert_type(i4**c16, np.complex128)
assert_type(i4**cld, np.clongdouble)

assert_type(i8**b0, np.int64)
assert_type(i8**b1, np.int64)
assert_type(i8**u1, np.int64)
assert_type(i8**u2, np.int64)
assert_type(i8**u4, np.int64)
assert_type(i8**u8, np.float64)
assert_type(i8**i1, np.int64)
assert_type(i8**i2, np.int64)
assert_type(i8**i4, np.int64)
assert_type(i8**i8, np.int64)
assert_type(i8**f2, np.float64)
assert_type(i8**f4, np.float64)
assert_type(i8**f8, np.float64)
assert_type(i8**ld, np.longdouble)
assert_type(i8**c8, np.complex128)
assert_type(i8**c16, np.complex128)
assert_type(i8**cld, np.clongdouble)

assert_type(f2**b0, np.float16)
assert_type(f2**b1, np.float16)
assert_type(f2**u1, np.float16)
assert_type(f2**u2, np.float32)
assert_type(f2**u4, np.float64)
assert_type(f2**u8, np.float64)
assert_type(f2**i1, np.float16)
assert_type(f2**i2, np.float32)
assert_type(f2**i4, np.float64)
assert_type(f2**i8, np.float64)
assert_type(f2**f2, np.float16)
assert_type(f2**f4, np.float32)
assert_type(f2**f8, np.float64)
assert_type(f2**ld, np.longdouble)
assert_type(f2**c8, np.complex64)
assert_type(f2**c16, np.complex128)
assert_type(f2**cld, np.clongdouble)

assert_type(f4**b0, np.float32)
assert_type(f4**b1, np.float32)
assert_type(f4**u1, np.float32)
assert_type(f4**u2, np.float32)
assert_type(f4**u4, np.float64)
assert_type(f4**u8, np.float64)
assert_type(f4**i1, np.float32)
assert_type(f4**i2, np.float32)
assert_type(f4**i4, np.float64)
assert_type(f4**i8, np.float64)
assert_type(f4**f2, np.float32)
assert_type(f4**f4, np.float32)
assert_type(f4**f8, np.float64)
assert_type(f4**ld, np.longdouble)
assert_type(f4**c8, np.complex64)
assert_type(f4**c16, np.complex128)
assert_type(f4**cld, np.clongdouble)

assert_type(f8**b0, np.float64)
assert_type(f8**b1, np.float64)
assert_type(f8**u1, np.float64)
assert_type(f8**u2, np.float64)
assert_type(f8**u4, np.float64)
assert_type(f8**u8, np.float64)
assert_type(f8**i1, np.float64)
assert_type(f8**i2, np.float64)
assert_type(f8**i4, np.float64)
assert_type(f8**i8, np.float64)
assert_type(f8**f2, np.float64)
assert_type(f8**f4, np.float64)
assert_type(f8**f8, np.float64)
assert_type(f8**ld, np.longdouble)
assert_type(f8**c8, np.complex128)
assert_type(f8**c16, np.complex128)
assert_type(f8**cld, np.clongdouble)

assert_type(ld**b0, np.longdouble)
assert_type(ld**b1, np.longdouble)
assert_type(ld**u1, np.longdouble)
assert_type(ld**u2, np.longdouble)
assert_type(ld**u4, np.longdouble)
assert_type(ld**u8, np.longdouble)
assert_type(ld**i1, np.longdouble)
assert_type(ld**i2, np.longdouble)
assert_type(ld**i4, np.longdouble)
assert_type(ld**i8, np.longdouble)
assert_type(ld**f2, np.longdouble)
assert_type(ld**f4, np.longdouble)
assert_type(ld**f8, np.longdouble)
assert_type(ld**ld, np.longdouble)
assert_type(ld**c8, np.clongdouble)
assert_type(ld**c16, np.clongdouble)
assert_type(ld**cld, np.clongdouble)

assert_type(c8**b0, np.complex64)
assert_type(c8**b1, np.complex64)
assert_type(c8**u1, np.complex64)
assert_type(c8**u2, np.complex64)
assert_type(c8**u4, np.complex128)
assert_type(c8**u8, np.complex128)
assert_type(c8**i1, np.complex64)
assert_type(c8**i2, np.complex64)
assert_type(c8**i4, np.complex128)
assert_type(c8**i8, np.complex128)
assert_type(c8**f2, np.complex64)
assert_type(c8**f4, np.complex64)
assert_type(c8**f8, np.complex128)
assert_type(c8**ld, np.clongdouble)
assert_type(c8**c8, np.complex64)
assert_type(c8**c16, np.complex128)
assert_type(c8**cld, np.clongdouble)

assert_type(c16**b0, np.complex128)
assert_type(c16**b1, np.complex128)
assert_type(c16**u1, np.complex128)
assert_type(c16**u2, np.complex128)
assert_type(c16**u4, np.complex128)
assert_type(c16**u8, np.complex128)
assert_type(c16**i1, np.complex128)
assert_type(c16**i2, np.complex128)
assert_type(c16**i4, np.complex128)
assert_type(c16**i8, np.complex128)
assert_type(c16**f2, np.complex128)
assert_type(c16**f4, np.complex128)
assert_type(c16**f8, np.complex128)
assert_type(c16**ld, np.clongdouble)
assert_type(c16**c8, np.complex128)
assert_type(c16**c16, np.complex128)
assert_type(c16**cld, np.clongdouble)

assert_type(cld**b0, np.clongdouble)
assert_type(cld**b1, np.clongdouble)
assert_type(cld**u1, np.clongdouble)
assert_type(cld**u2, np.clongdouble)
assert_type(cld**u4, np.clongdouble)
assert_type(cld**u8, np.clongdouble)
assert_type(cld**i1, np.clongdouble)
assert_type(cld**i2, np.clongdouble)
assert_type(cld**i4, np.clongdouble)
assert_type(cld**i8, np.clongdouble)
assert_type(cld**f2, np.clongdouble)
assert_type(cld**f4, np.clongdouble)
assert_type(cld**f8, np.clongdouble)
assert_type(cld**ld, np.clongdouble)
assert_type(cld**c8, np.clongdouble)
assert_type(cld**c16, np.clongdouble)
assert_type(cld**cld, np.clongdouble)

###
# __[r]truediv__

assert_type(b1 / b0, np.float64)
assert_type(b1 / b1, np.float64)
assert_type(b1 / u1, np.float64)
assert_type(b1 / u2, np.float64)
assert_type(b1 / u4, np.float64)
assert_type(b1 / u8, np.float64)
assert_type(b1 / i1, np.float64)
assert_type(b1 / i2, np.float64)
assert_type(b1 / i4, np.float64)
assert_type(b1 / i8, np.float64)
assert_type(b1 / f2, np.float16)
assert_type(b1 / f4, np.float32)
assert_type(b1 / f8, np.float64)
assert_type(b1 / ld, np.longdouble)
assert_type(b1 / c8, np.complex64)
assert_type(b1 / c16, np.complex128)
assert_type(b1 / cld, np.clongdouble)
b1 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1 / b0, np.float64)
assert_type(u1 / b1, np.float64)
assert_type(u1 / u1, np.float64)
assert_type(u1 / u2, np.float64)
assert_type(u1 / u4, np.float64)
assert_type(u1 / u8, np.float64)
assert_type(u1 / i1, np.float64)
assert_type(u1 / i2, np.float64)
assert_type(u1 / i4, np.float64)
assert_type(u1 / i8, np.float64)
assert_type(u1 / f2, np.float16)
assert_type(u1 / f4, np.float32)
assert_type(u1 / f8, np.float64)
assert_type(u1 / ld, np.longdouble)
assert_type(u1 / c8, np.complex64)
assert_type(u1 / c16, np.complex128)
assert_type(u1 / cld, np.clongdouble)
u1 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2 / b0, np.float64)
assert_type(u2 / b1, np.float64)
assert_type(u2 / u1, np.float64)
assert_type(u2 / u2, np.float64)
assert_type(u2 / u4, np.float64)
assert_type(u2 / u8, np.float64)
assert_type(u2 / i1, np.float64)
assert_type(u2 / i2, np.float64)
assert_type(u2 / i4, np.float64)
assert_type(u2 / i8, np.float64)
assert_type(u2 / f2, np.float32)
assert_type(u2 / f4, np.float32)
assert_type(u2 / f8, np.float64)
assert_type(u2 / ld, np.longdouble)
assert_type(u2 / c8, np.complex64)
assert_type(u2 / c16, np.complex128)
assert_type(u2 / cld, np.clongdouble)
u2 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4 / b0, np.float64)
assert_type(u4 / b1, np.float64)
assert_type(u4 / u1, np.float64)
assert_type(u4 / u2, np.float64)
assert_type(u4 / u4, np.float64)
assert_type(u4 / u8, np.float64)
assert_type(u4 / i1, np.float64)
assert_type(u4 / i2, np.float64)
assert_type(u4 / i4, np.float64)
assert_type(u4 / i8, np.float64)
assert_type(u4 / f2, np.float64)
assert_type(u4 / f4, np.float64)
assert_type(u4 / f8, np.float64)
assert_type(u4 / ld, np.longdouble)
assert_type(u4 / c8, np.complex128)
assert_type(u4 / c16, np.complex128)
assert_type(u4 / cld, np.clongdouble)
u4 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 / b0, np.float64)
assert_type(u8 / b1, np.float64)
assert_type(u8 / u1, np.float64)
assert_type(u8 / u2, np.float64)
assert_type(u8 / u4, np.float64)
assert_type(u8 / u8, np.float64)
assert_type(u8 / i1, np.float64)
assert_type(u8 / i2, np.float64)
assert_type(u8 / i4, np.float64)
assert_type(u8 / i8, np.float64)
assert_type(u8 / f2, np.float64)
assert_type(u8 / f4, np.float64)
assert_type(u8 / f8, np.float64)
assert_type(u8 / ld, np.longdouble)
assert_type(u8 / c8, np.complex128)
assert_type(u8 / c16, np.complex128)
assert_type(u8 / cld, np.clongdouble)
u8 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 / b0, np.float64)
assert_type(i1 / b1, np.float64)
assert_type(i1 / u1, np.float64)
assert_type(i1 / u2, np.float64)
assert_type(i1 / u4, np.float64)
assert_type(i1 / u8, np.float64)
assert_type(i1 / i1, np.float64)
assert_type(i1 / i2, np.float64)
assert_type(i1 / i4, np.float64)
assert_type(i1 / i8, np.float64)
assert_type(i1 / f2, np.float16)
assert_type(i1 / f4, np.float32)
assert_type(i1 / f8, np.float64)
assert_type(i1 / ld, np.longdouble)
assert_type(i1 / c8, np.complex64)
assert_type(i1 / c16, np.complex128)
assert_type(i1 / cld, np.clongdouble)
i1 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2 / b0, np.float64)
assert_type(i2 / b1, np.float64)
assert_type(i2 / u1, np.float64)
assert_type(i2 / u2, np.float64)
assert_type(i2 / u4, np.float64)
assert_type(i2 / u8, np.float64)
assert_type(i2 / i1, np.float64)
assert_type(i2 / i2, np.float64)
assert_type(i2 / i4, np.float64)
assert_type(i2 / i8, np.float64)
assert_type(i2 / f2, np.float32)
assert_type(i2 / f4, np.float32)
assert_type(i2 / f8, np.float64)
assert_type(i2 / ld, np.longdouble)
assert_type(i2 / c8, np.complex64)
assert_type(i2 / c16, np.complex128)
assert_type(i2 / cld, np.clongdouble)
i2 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4 / b0, np.float64)
assert_type(i4 / b1, np.float64)
assert_type(i4 / u1, np.float64)
assert_type(i4 / u2, np.float64)
assert_type(i4 / u4, np.float64)
assert_type(i4 / u8, np.float64)
assert_type(i4 / i1, np.float64)
assert_type(i4 / i2, np.float64)
assert_type(i4 / i4, np.float64)
assert_type(i4 / i8, np.float64)
assert_type(i4 / f2, np.float64)
assert_type(i4 / f4, np.float64)
assert_type(i4 / f8, np.float64)
assert_type(i4 / ld, np.longdouble)
assert_type(i4 / c8, np.complex128)
assert_type(i4 / c16, np.complex128)
assert_type(i4 / cld, np.clongdouble)
i4 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 / b0, np.float64)
assert_type(i8 / b1, np.float64)
assert_type(i8 / u1, np.float64)
assert_type(i8 / u2, np.float64)
assert_type(i8 / u4, np.float64)
assert_type(i8 / u8, np.float64)
assert_type(i8 / i1, np.float64)
assert_type(i8 / i2, np.float64)
assert_type(i8 / i4, np.float64)
assert_type(i8 / i8, np.float64)
assert_type(i8 / f2, np.float64)
assert_type(i8 / f4, np.float64)
assert_type(i8 / f8, np.float64)
assert_type(i8 / ld, np.longdouble)
assert_type(i8 / c8, np.complex128)
assert_type(i8 / c16, np.complex128)
assert_type(i8 / cld, np.clongdouble)
i8 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2 / b0, np.float16)
assert_type(f2 / b1, np.float16)
assert_type(f2 / u1, np.float16)
assert_type(f2 / u2, np.float32)
assert_type(f2 / u4, np.float64)
assert_type(f2 / u8, np.float64)
assert_type(f2 / i1, np.float16)
assert_type(f2 / i2, np.float32)
assert_type(f2 / i4, np.float64)
assert_type(f2 / i8, np.float64)
assert_type(f2 / f2, np.float16)
assert_type(f2 / f4, np.float32)
assert_type(f2 / f8, np.float64)
assert_type(f2 / ld, np.longdouble)
assert_type(f2 / c8, np.complex64)
assert_type(f2 / c16, np.complex128)
assert_type(f2 / cld, np.clongdouble)
f2 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4 / b0, np.float32)
assert_type(f4 / b1, np.float32)
assert_type(f4 / u1, np.float32)
assert_type(f4 / u2, np.float32)
assert_type(f4 / u4, np.float64)
assert_type(f4 / u8, np.float64)
assert_type(f4 / i1, np.float32)
assert_type(f4 / i2, np.float32)
assert_type(f4 / i4, np.float64)
assert_type(f4 / i8, np.float64)
assert_type(f4 / f2, np.float32)
assert_type(f4 / f4, np.float32)
assert_type(f4 / f8, np.float64)
assert_type(f4 / ld, np.longdouble)
assert_type(f4 / c8, np.complex64)
assert_type(f4 / c16, np.complex128)
assert_type(f4 / cld, np.clongdouble)
f4 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8 / b0, np.float64)
assert_type(f8 / b1, np.float64)
assert_type(f8 / u1, np.float64)
assert_type(f8 / u2, np.float64)
assert_type(f8 / u4, np.float64)
assert_type(f8 / u8, np.float64)
assert_type(f8 / i1, np.float64)
assert_type(f8 / i2, np.float64)
assert_type(f8 / i4, np.float64)
assert_type(f8 / i8, np.float64)
assert_type(f8 / f2, np.float64)
assert_type(f8 / f4, np.float64)
assert_type(f8 / f8, np.float64)
assert_type(f8 / ld, np.longdouble)
assert_type(f8 / c8, np.complex128)
assert_type(f8 / c16, np.complex128)
assert_type(f8 / cld, np.clongdouble)
f8 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(ld / b0, np.longdouble)
assert_type(ld / b1, np.longdouble)
assert_type(ld / u1, np.longdouble)
assert_type(ld / u2, np.longdouble)
assert_type(ld / u4, np.longdouble)
assert_type(ld / u8, np.longdouble)
assert_type(ld / i1, np.longdouble)
assert_type(ld / i2, np.longdouble)
assert_type(ld / i4, np.longdouble)
assert_type(ld / i8, np.longdouble)
assert_type(ld / f2, np.longdouble)
assert_type(ld / f4, np.longdouble)
assert_type(ld / f8, np.longdouble)
assert_type(ld / ld, np.longdouble)
assert_type(ld / c8, np.clongdouble)
assert_type(ld / c16, np.clongdouble)
assert_type(ld / cld, np.clongdouble)
ld / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c8 / b0, np.complex64)
assert_type(c8 / b1, np.complex64)
assert_type(c8 / u1, np.complex64)
assert_type(c8 / u2, np.complex64)
assert_type(c8 / u4, np.complex128)
assert_type(c8 / u8, np.complex128)
assert_type(c8 / i1, np.complex64)
assert_type(c8 / i2, np.complex64)
assert_type(c8 / i4, np.complex128)
assert_type(c8 / i8, np.complex128)
assert_type(c8 / f2, np.complex64)
assert_type(c8 / f4, np.complex64)
assert_type(c8 / f8, np.complex128)
assert_type(c8 / ld, np.clongdouble)
assert_type(c8 / c8, np.complex64)
assert_type(c8 / c16, np.complex128)
assert_type(c8 / cld, np.clongdouble)
c8 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16 / b0, np.complex128)
assert_type(c16 / b1, np.complex128)
assert_type(c16 / u1, np.complex128)
assert_type(c16 / u2, np.complex128)
assert_type(c16 / u4, np.complex128)
assert_type(c16 / u8, np.complex128)
assert_type(c16 / i1, np.complex128)
assert_type(c16 / i2, np.complex128)
assert_type(c16 / i4, np.complex128)
assert_type(c16 / i8, np.complex128)
assert_type(c16 / f2, np.complex128)
assert_type(c16 / f4, np.complex128)
assert_type(c16 / f8, np.complex128)
assert_type(c16 / ld, np.clongdouble)
assert_type(c16 / c8, np.complex128)
assert_type(c16 / c16, np.complex128)
assert_type(c16 / cld, np.clongdouble)
c16 / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld / b0, np.clongdouble)
assert_type(cld / b1, np.clongdouble)
assert_type(cld / u1, np.clongdouble)
assert_type(cld / u2, np.clongdouble)
assert_type(cld / u4, np.clongdouble)
assert_type(cld / u8, np.clongdouble)
assert_type(cld / i1, np.clongdouble)
assert_type(cld / i2, np.clongdouble)
assert_type(cld / i4, np.clongdouble)
assert_type(cld / i8, np.clongdouble)
assert_type(cld / f2, np.clongdouble)
assert_type(cld / f4, np.clongdouble)
assert_type(cld / f8, np.clongdouble)
assert_type(cld / ld, np.clongdouble)
assert_type(cld / c8, np.clongdouble)
assert_type(cld / c16, np.clongdouble)
assert_type(cld / cld, np.clongdouble)
cld / m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m8 / b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 / u1, np.timedelta64)
assert_type(m8 / u2, np.timedelta64)
assert_type(m8 / u4, np.timedelta64)
assert_type(m8 / u8, np.timedelta64)
assert_type(m8 / i1, np.timedelta64)
assert_type(m8 / i2, np.timedelta64)
assert_type(m8 / i4, np.timedelta64)
assert_type(m8 / i8, np.timedelta64)
assert_type(m8 / f2, np.timedelta64)
assert_type(m8 / f4, np.timedelta64)
assert_type(m8 / f8, np.timedelta64)
assert_type(m8 / ld, np.timedelta64)
m8 / c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 / c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 / cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 / m8, np.float64)

###
# __[r]floordiv__

assert_type(b1 // b0, np.int8)
assert_type(b1 // b1, np.int8)
assert_type(b1 // u1, np.uint8)
assert_type(b1 // u2, np.uint16)
assert_type(b1 // u4, np.uint32)
assert_type(b1 // u8, np.uint64)
assert_type(b1 // i1, np.int8)
assert_type(b1 // i2, np.int16)
assert_type(b1 // i4, np.int32)
assert_type(b1 // i8, np.int64)
assert_type(b1 // f2, np.float16)
assert_type(b1 // f4, np.float32)
assert_type(b1 // f8, np.float64)
assert_type(b1 // ld, np.longdouble)
b1 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1 // b0, np.uint8)
assert_type(u1 // b1, np.uint8)
assert_type(u1 // u1, np.uint8)
assert_type(u1 // u2, np.uint16)
assert_type(u1 // u4, np.uint32)
assert_type(u1 // u8, np.uint64)
assert_type(u1 // i1, np.int16)
assert_type(u1 // i2, np.int16)
assert_type(u1 // i4, np.int32)
assert_type(u1 // i8, np.int64)
assert_type(u1 // f2, np.float16)
assert_type(u1 // f4, np.float32)
assert_type(u1 // f8, np.float64)
assert_type(u1 // ld, np.longdouble)
u1 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2 // b0, np.uint16)
assert_type(u2 // b1, np.uint16)
assert_type(u2 // u1, np.uint16)
assert_type(u2 // u2, np.uint16)
assert_type(u2 // u4, np.uint32)
assert_type(u2 // u8, np.uint64)
assert_type(u2 // i1, np.int32)
assert_type(u2 // i2, np.int32)
assert_type(u2 // i4, np.int32)
assert_type(u2 // i8, np.int64)
assert_type(u2 // f2, np.float32)
assert_type(u2 // f4, np.float32)
assert_type(u2 // f8, np.float64)
assert_type(u2 // ld, np.longdouble)
u2 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4 // b0, np.uint32)
assert_type(u4 // b1, np.uint32)
assert_type(u4 // u1, np.uint32)
assert_type(u4 // u2, np.uint32)
assert_type(u4 // u4, np.uint32)
assert_type(u4 // u8, np.uint64)
assert_type(u4 // i1, np.int64)
assert_type(u4 // i2, np.int64)
assert_type(u4 // i4, np.int64)
assert_type(u4 // i8, np.int64)
assert_type(u4 // f2, np.float64)
assert_type(u4 // f4, np.float64)
assert_type(u4 // f8, np.float64)
assert_type(u4 // ld, np.longdouble)
u4 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 // b0, np.uint64)
assert_type(u8 // b1, np.uint64)
assert_type(u8 // u1, np.uint64)
assert_type(u8 // u2, np.uint64)
assert_type(u8 // u4, np.uint64)
assert_type(u8 // u8, np.uint64)
assert_type(u8 // i1, np.float64)
assert_type(u8 // i2, np.float64)
assert_type(u8 // i4, np.float64)
assert_type(u8 // i8, np.float64)
assert_type(u8 // f2, np.float64)
assert_type(u8 // f4, np.float64)
assert_type(u8 // f8, np.float64)
assert_type(u8 // ld, np.longdouble)
u8 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 // b0, np.int8)
assert_type(i1 // b1, np.int8)
assert_type(i1 // u1, np.int16)
assert_type(i1 // u2, np.int32)
assert_type(i1 // u4, np.int64)
assert_type(i1 // u8, np.float64)
assert_type(i1 // i1, np.int8)
assert_type(i1 // i2, np.int16)
assert_type(i1 // i4, np.int32)
assert_type(i1 // i8, np.int64)
assert_type(i1 // f2, np.float16)
assert_type(i1 // f4, np.float32)
assert_type(i1 // f8, np.float64)
assert_type(i1 // ld, np.longdouble)
i1 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2 // b0, np.int16)
assert_type(i2 // b1, np.int16)
assert_type(i2 // u1, np.int16)
assert_type(i2 // u2, np.int32)
assert_type(i2 // u4, np.int64)
assert_type(i2 // u8, np.float64)
assert_type(i2 // i1, np.int16)
assert_type(i2 // i2, np.int16)
assert_type(i2 // i4, np.int32)
assert_type(i2 // i8, np.int64)
assert_type(i2 // f2, np.float32)
assert_type(i2 // f4, np.float32)
assert_type(i2 // f8, np.float64)
assert_type(i2 // ld, np.longdouble)
i2 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4 // b0, np.int32)
assert_type(i4 // b1, np.int32)
assert_type(i4 // u1, np.int32)
assert_type(i4 // u2, np.int32)
assert_type(i4 // u4, np.int64)
assert_type(i4 // u8, np.float64)
assert_type(i4 // i1, np.int32)
assert_type(i4 // i2, np.int32)
assert_type(i4 // i4, np.int32)
assert_type(i4 // i8, np.int64)
assert_type(i4 // f2, np.float64)
assert_type(i4 // f4, np.float64)
assert_type(i4 // f8, np.float64)
assert_type(i4 // ld, np.longdouble)
i4 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 // b0, np.int64)
assert_type(i8 // b1, np.int64)
assert_type(i8 // u1, np.int64)
assert_type(i8 // u2, np.int64)
assert_type(i8 // u4, np.int64)
assert_type(i8 // u8, np.float64)
assert_type(i8 // i1, np.int64)
assert_type(i8 // i2, np.int64)
assert_type(i8 // i4, np.int64)
assert_type(i8 // i8, np.int64)
assert_type(i8 // f2, np.float64)
assert_type(i8 // f4, np.float64)
assert_type(i8 // f8, np.float64)
assert_type(i8 // ld, np.longdouble)
i8 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2 // b0, np.float16)
assert_type(f2 // b1, np.float16)
assert_type(f2 // u1, np.float16)
assert_type(f2 // u2, np.float32)
assert_type(f2 // u4, np.float64)
assert_type(f2 // u8, np.float64)
assert_type(f2 // i1, np.float16)
assert_type(f2 // i2, np.float32)
assert_type(f2 // i4, np.float64)
assert_type(f2 // i8, np.float64)
assert_type(f2 // f2, np.float16)
assert_type(f2 // f4, np.float32)
assert_type(f2 // f8, np.float64)
assert_type(f2 // ld, np.longdouble)
f2 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4 // b0, np.float32)
assert_type(f4 // b1, np.float32)
assert_type(f4 // u1, np.float32)
assert_type(f4 // u2, np.float32)
assert_type(f4 // u4, np.float64)
assert_type(f4 // u8, np.float64)
assert_type(f4 // i1, np.float32)
assert_type(f4 // i2, np.float32)
assert_type(f4 // i4, np.float64)
assert_type(f4 // i8, np.float64)
assert_type(f4 // f2, np.float32)
assert_type(f4 // f4, np.float32)
assert_type(f4 // f8, np.float64)
assert_type(f4 // ld, np.longdouble)
f4 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8 // b0, np.float64)
assert_type(f8 // b1, np.float64)
assert_type(f8 // u1, np.float64)
assert_type(f8 // u2, np.float64)
assert_type(f8 // u4, np.float64)
assert_type(f8 // u8, np.float64)
assert_type(f8 // i1, np.float64)
assert_type(f8 // i2, np.float64)
assert_type(f8 // i4, np.float64)
assert_type(f8 // i8, np.float64)
assert_type(f8 // f2, np.float64)
assert_type(f8 // f4, np.float64)
assert_type(f8 // f8, np.float64)
assert_type(f8 // ld, np.longdouble)
f8 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(ld // b0, np.longdouble)
assert_type(ld // b1, np.longdouble)
assert_type(ld // u1, np.longdouble)
assert_type(ld // u2, np.longdouble)
assert_type(ld // u4, np.longdouble)
assert_type(ld // u8, np.longdouble)
assert_type(ld // i1, np.longdouble)
assert_type(ld // i2, np.longdouble)
assert_type(ld // i4, np.longdouble)
assert_type(ld // i8, np.longdouble)
assert_type(ld // f2, np.longdouble)
assert_type(ld // f4, np.longdouble)
assert_type(ld // f8, np.longdouble)
assert_type(ld // ld, np.longdouble)
ld // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c8 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c16 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

cld // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld // m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m8 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 // u1, np.timedelta64)
assert_type(m8 // u2, np.timedelta64)
assert_type(m8 // u4, np.timedelta64)
assert_type(m8 // u8, np.timedelta64)
assert_type(m8 // i1, np.timedelta64)
assert_type(m8 // i2, np.timedelta64)
assert_type(m8 // i4, np.timedelta64)
assert_type(m8 // i8, np.timedelta64)
assert_type(m8 // f2, np.timedelta64)
assert_type(m8 // f4, np.timedelta64)
assert_type(m8 // f8, np.timedelta64)
assert_type(m8 // ld, np.timedelta64)
m8 // c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 // c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 // cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 // m8, np.longlong)

###
# __[r]mod__

assert_type(b1 % b0, np.int8)
assert_type(b1 % b1, np.int8)
assert_type(b1 % u1, np.uint8)
assert_type(b1 % u2, np.uint16)
assert_type(b1 % u4, np.uint32)
assert_type(b1 % u8, np.uint64)
assert_type(b1 % i1, np.int8)
assert_type(b1 % i2, np.int16)
assert_type(b1 % i4, np.int32)
assert_type(b1 % i8, np.int64)
assert_type(b1 % f2, np.float16)
assert_type(b1 % f4, np.float32)
assert_type(b1 % f8, np.float64)
assert_type(b1 % ld, np.longdouble)
b1 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1 % b0, np.uint8)
assert_type(u1 % b1, np.uint8)
assert_type(u1 % u1, np.uint8)
assert_type(u1 % u2, np.uint16)
assert_type(u1 % u4, np.uint32)
assert_type(u1 % u8, np.uint64)
assert_type(u1 % i1, np.int16)
assert_type(u1 % i2, np.int16)
assert_type(u1 % i4, np.int32)
assert_type(u1 % i8, np.int64)
assert_type(u1 % f2, np.float16)
assert_type(u1 % f4, np.float32)
assert_type(u1 % f8, np.float64)
assert_type(u1 % ld, np.longdouble)
u1 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2 % b0, np.uint16)
assert_type(u2 % b1, np.uint16)
assert_type(u2 % u1, np.uint16)
assert_type(u2 % u2, np.uint16)
assert_type(u2 % u4, np.uint32)
assert_type(u2 % u8, np.uint64)
assert_type(u2 % i1, np.int32)
assert_type(u2 % i2, np.int32)
assert_type(u2 % i4, np.int32)
assert_type(u2 % i8, np.int64)
assert_type(u2 % f2, np.float32)
assert_type(u2 % f4, np.float32)
assert_type(u2 % f8, np.float64)
assert_type(u2 % ld, np.longdouble)
u2 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4 % b0, np.uint32)
assert_type(u4 % b1, np.uint32)
assert_type(u4 % u1, np.uint32)
assert_type(u4 % u2, np.uint32)
assert_type(u4 % u4, np.uint32)
assert_type(u4 % u8, np.uint64)
assert_type(u4 % i1, np.int64)
assert_type(u4 % i2, np.int64)
assert_type(u4 % i4, np.int64)
assert_type(u4 % i8, np.int64)
assert_type(u4 % f2, np.float64)
assert_type(u4 % f4, np.float64)
assert_type(u4 % f8, np.float64)
assert_type(u4 % ld, np.longdouble)
u4 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 % b0, np.uint64)
assert_type(u8 % b1, np.uint64)
assert_type(u8 % u1, np.uint64)
assert_type(u8 % u2, np.uint64)
assert_type(u8 % u4, np.uint64)
assert_type(u8 % u8, np.uint64)
assert_type(u8 % i1, np.float64)
assert_type(u8 % i2, np.float64)
assert_type(u8 % i4, np.float64)
assert_type(u8 % i8, np.float64)
assert_type(u8 % f2, np.float64)
assert_type(u8 % f4, np.float64)
assert_type(u8 % f8, np.float64)
assert_type(u8 % ld, np.longdouble)
u8 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 % b0, np.int8)
assert_type(i1 % b1, np.int8)
assert_type(i1 % u1, np.int16)
assert_type(i1 % u2, np.int32)
assert_type(i1 % u4, np.int64)
assert_type(i1 % u8, np.float64)
assert_type(i1 % i1, np.int8)
assert_type(i1 % i2, np.int16)
assert_type(i1 % i4, np.int32)
assert_type(i1 % i8, np.int64)
assert_type(i1 % f2, np.float16)
assert_type(i1 % f4, np.float32)
assert_type(i1 % f8, np.float64)
assert_type(i1 % ld, np.longdouble)
i1 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2 % b0, np.int16)
assert_type(i2 % b1, np.int16)
assert_type(i2 % u1, np.int16)
assert_type(i2 % u2, np.int32)
assert_type(i2 % u4, np.int64)
assert_type(i2 % u8, np.float64)
assert_type(i2 % i1, np.int16)
assert_type(i2 % i2, np.int16)
assert_type(i2 % i4, np.int32)
assert_type(i2 % i8, np.int64)
assert_type(i2 % f2, np.float32)
assert_type(i2 % f4, np.float32)
assert_type(i2 % f8, np.float64)
assert_type(i2 % ld, np.longdouble)
i2 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4 % b0, np.int32)
assert_type(i4 % b1, np.int32)
assert_type(i4 % u1, np.int32)
assert_type(i4 % u2, np.int32)
assert_type(i4 % u4, np.int64)
assert_type(i4 % u8, np.float64)
assert_type(i4 % i1, np.int32)
assert_type(i4 % i2, np.int32)
assert_type(i4 % i4, np.int32)
assert_type(i4 % i8, np.int64)
assert_type(i4 % f2, np.float64)
assert_type(i4 % f4, np.float64)
assert_type(i4 % f8, np.float64)
assert_type(i4 % ld, np.longdouble)
i4 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 % b0, np.int64)
assert_type(i8 % b1, np.int64)
assert_type(i8 % u1, np.int64)
assert_type(i8 % u2, np.int64)
assert_type(i8 % u4, np.int64)
assert_type(i8 % u8, np.float64)
assert_type(i8 % i1, np.int64)
assert_type(i8 % i2, np.int64)
assert_type(i8 % i4, np.int64)
assert_type(i8 % i8, np.int64)
assert_type(i8 % f2, np.float64)
assert_type(i8 % f4, np.float64)
assert_type(i8 % f8, np.float64)
assert_type(i8 % ld, np.longdouble)
i8 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2 % b0, np.float16)
assert_type(f2 % b1, np.float16)
assert_type(f2 % u1, np.float16)
assert_type(f2 % u2, np.float32)
assert_type(f2 % u4, np.float64)
assert_type(f2 % u8, np.float64)
assert_type(f2 % i1, np.float16)
assert_type(f2 % i2, np.float32)
assert_type(f2 % i4, np.float64)
assert_type(f2 % i8, np.float64)
assert_type(f2 % f2, np.float16)
assert_type(f2 % f4, np.float32)
assert_type(f2 % f8, np.float64)
assert_type(f2 % ld, np.longdouble)
f2 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4 % b0, np.float32)
assert_type(f4 % b1, np.float32)
assert_type(f4 % u1, np.float32)
assert_type(f4 % u2, np.float32)
assert_type(f4 % u4, np.float64)
assert_type(f4 % u8, np.float64)
assert_type(f4 % i1, np.float32)
assert_type(f4 % i2, np.float32)
assert_type(f4 % i4, np.float64)
assert_type(f4 % i8, np.float64)
assert_type(f4 % f2, np.float32)
assert_type(f4 % f4, np.float32)
assert_type(f4 % f8, np.float64)
assert_type(f4 % ld, np.longdouble)
f4 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8 % b0, np.float64)
assert_type(f8 % b1, np.float64)
assert_type(f8 % u1, np.float64)
assert_type(f8 % u2, np.float64)
assert_type(f8 % u4, np.float64)
assert_type(f8 % u8, np.float64)
assert_type(f8 % i1, np.float64)
assert_type(f8 % i2, np.float64)
assert_type(f8 % i4, np.float64)
assert_type(f8 % i8, np.float64)
assert_type(f8 % f2, np.float64)
assert_type(f8 % f4, np.float64)
assert_type(f8 % f8, np.float64)
assert_type(f8 % ld, np.longdouble)
f8 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(ld % b0, np.longdouble)
assert_type(ld % b1, np.longdouble)
assert_type(ld % u1, np.longdouble)
assert_type(ld % u2, np.longdouble)
assert_type(ld % u4, np.longdouble)
assert_type(ld % u8, np.longdouble)
assert_type(ld % i1, np.longdouble)
assert_type(ld % i2, np.longdouble)
assert_type(ld % i4, np.longdouble)
assert_type(ld % i8, np.longdouble)
assert_type(ld % f2, np.longdouble)
assert_type(ld % f4, np.longdouble)
assert_type(ld % f8, np.longdouble)
assert_type(ld % ld, np.longdouble)
ld % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
ld % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c8 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c16 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16 % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

cld % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld % m8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m8 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % u1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % u2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % u4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % f2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % f4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % ld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % c8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % c16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8 % cld  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8 % m8, np.timedelta64)

###
# __[r]lshift__

assert_type(b1 << b0, np.int8)
assert_type(b1 << b1, np.int8)
assert_type(b1 << u1, np.uint8)
assert_type(b1 << u2, np.uint16)
assert_type(b1 << u4, np.uint32)
assert_type(b1 << u8, np.uint64)
assert_type(b1 << i1, np.int8)
assert_type(b1 << i2, np.int16)
assert_type(b1 << i4, np.int32)
assert_type(b1 << i8, np.int64)

assert_type(u1 << b0, np.uint8)
assert_type(u1 << b1, np.uint8)
assert_type(u1 << u1, np.uint8)
assert_type(u1 << u2, np.uint16)
assert_type(u1 << u4, np.uint32)
assert_type(u1 << u8, np.uint64)
assert_type(u1 << i1, np.int16)
assert_type(u1 << i2, np.int16)
assert_type(u1 << i4, np.int32)
assert_type(u1 << i8, np.int64)

assert_type(u2 << b0, np.uint16)
assert_type(u2 << b1, np.uint16)
assert_type(u2 << u1, np.uint16)
assert_type(u2 << u2, np.uint16)
assert_type(u2 << u4, np.uint32)
assert_type(u2 << u8, np.uint64)
assert_type(u2 << i1, np.int32)
assert_type(u2 << i2, np.int32)
assert_type(u2 << i4, np.int32)
assert_type(u2 << i8, np.int64)

assert_type(u4 << b0, np.uint32)
assert_type(u4 << b1, np.uint32)
assert_type(u4 << u1, np.uint32)
assert_type(u4 << u2, np.uint32)
assert_type(u4 << u4, np.uint32)
assert_type(u4 << u8, np.uint64)
assert_type(u4 << i1, np.int64)
assert_type(u4 << i2, np.int64)
assert_type(u4 << i4, np.int64)
assert_type(u4 << i8, np.int64)

assert_type(u8 << b0, np.uint64)
assert_type(u8 << b1, np.uint64)
assert_type(u8 << u1, np.uint64)
assert_type(u8 << u2, np.uint64)
assert_type(u8 << u4, np.uint64)
assert_type(u8 << u8, np.uint64)
u8 << i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 << b0, np.int8)
assert_type(i1 << b1, np.int8)
assert_type(i1 << u1, np.int16)
assert_type(i1 << u2, np.int32)
assert_type(i1 << u4, np.int64)
i1 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1 << i1, np.int8)
assert_type(i1 << i2, np.int16)
assert_type(i1 << i4, np.int32)
assert_type(i1 << i8, np.int64)

assert_type(i2 << b0, np.int16)
assert_type(i2 << b1, np.int16)
assert_type(i2 << u1, np.int16)
assert_type(i2 << u2, np.int32)
assert_type(i2 << u4, np.int64)
i2 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2 << i1, np.int16)
assert_type(i2 << i2, np.int16)
assert_type(i2 << i4, np.int32)
assert_type(i2 << i8, np.int64)

assert_type(i4 << b0, np.int32)
assert_type(i4 << b1, np.int32)
assert_type(i4 << u1, np.int32)
assert_type(i4 << u2, np.int32)
assert_type(i4 << u4, np.int64)
i4 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4 << i1, np.int32)
assert_type(i4 << i2, np.int32)
assert_type(i4 << i4, np.int32)
assert_type(i4 << i8, np.int64)

assert_type(i8 << b0, np.int64)
assert_type(i8 << b1, np.int64)
assert_type(i8 << u1, np.int64)
assert_type(i8 << u2, np.int64)
assert_type(i8 << u4, np.int64)
i8 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 << i1, np.int64)
assert_type(i8 << i2, np.int64)
assert_type(i8 << i4, np.int64)
assert_type(i8 << i8, np.int64)

###
# __[r]rshift__

assert_type(b1 >> b0, np.int8)
assert_type(b1 >> b1, np.int8)
assert_type(b1 >> u1, np.uint8)
assert_type(b1 >> u2, np.uint16)
assert_type(b1 >> u4, np.uint32)
assert_type(b1 >> u8, np.uint64)
assert_type(b1 >> i1, np.int8)
assert_type(b1 >> i2, np.int16)
assert_type(b1 >> i4, np.int32)
assert_type(b1 >> i8, np.int64)

assert_type(u1 >> b0, np.uint8)
assert_type(u1 >> b1, np.uint8)
assert_type(u1 >> u1, np.uint8)
assert_type(u1 >> u2, np.uint16)
assert_type(u1 >> u4, np.uint32)
assert_type(u1 >> u8, np.uint64)
assert_type(u1 >> i1, np.int16)
assert_type(u1 >> i2, np.int16)
assert_type(u1 >> i4, np.int32)
assert_type(u1 >> i8, np.int64)

assert_type(u2 >> b0, np.uint16)
assert_type(u2 >> b1, np.uint16)
assert_type(u2 >> u1, np.uint16)
assert_type(u2 >> u2, np.uint16)
assert_type(u2 >> u4, np.uint32)
assert_type(u2 >> u8, np.uint64)
assert_type(u2 >> i1, np.int32)
assert_type(u2 >> i2, np.int32)
assert_type(u2 >> i4, np.int32)
assert_type(u2 >> i8, np.int64)

assert_type(u4 >> b0, np.uint32)
assert_type(u4 >> b1, np.uint32)
assert_type(u4 >> u1, np.uint32)
assert_type(u4 >> u2, np.uint32)
assert_type(u4 >> u4, np.uint32)
assert_type(u4 >> u8, np.uint64)
assert_type(u4 >> i1, np.int64)
assert_type(u4 >> i2, np.int64)
assert_type(u4 >> i4, np.int64)
assert_type(u4 >> i8, np.int64)

assert_type(u8 >> b0, np.uint64)
assert_type(u8 >> b1, np.uint64)
assert_type(u8 >> u1, np.uint64)
assert_type(u8 >> u2, np.uint64)
assert_type(u8 >> u4, np.uint64)
assert_type(u8 >> u8, np.uint64)
u8 >> i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 >> b0, np.int8)
assert_type(i1 >> b1, np.int8)
assert_type(i1 >> u1, np.int16)
assert_type(i1 >> u2, np.int32)
assert_type(i1 >> u4, np.int64)
i1 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1 >> i1, np.int8)
assert_type(i1 >> i2, np.int16)
assert_type(i1 >> i4, np.int32)
assert_type(i1 >> i8, np.int64)

assert_type(i2 >> b0, np.int16)
assert_type(i2 >> b1, np.int16)
assert_type(i2 >> u1, np.int16)
assert_type(i2 >> u2, np.int32)
assert_type(i2 >> u4, np.int64)
i2 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2 >> i1, np.int16)
assert_type(i2 >> i2, np.int16)
assert_type(i2 >> i4, np.int32)
assert_type(i2 >> i8, np.int64)

assert_type(i4 >> b0, np.int32)
assert_type(i4 >> b1, np.int32)
assert_type(i4 >> u1, np.int32)
assert_type(i4 >> u2, np.int32)
assert_type(i4 >> u4, np.int64)
i4 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4 >> i1, np.int32)
assert_type(i4 >> i2, np.int32)
assert_type(i4 >> i4, np.int32)
assert_type(i4 >> i8, np.int64)

assert_type(i8 >> b0, np.int64)
assert_type(i8 >> b1, np.int64)
assert_type(i8 >> u1, np.int64)
assert_type(i8 >> u2, np.int64)
assert_type(i8 >> u4, np.int64)
i8 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 >> i1, np.int64)
assert_type(i8 >> i2, np.int64)
assert_type(i8 >> i4, np.int64)
assert_type(i8 >> i8, np.int64)

###
# __[r]and__

assert_type(b1 & b0, np.bool)
assert_type(b1 & b1, np.bool)
assert_type(b1 & u1, np.uint8)
assert_type(b1 & u2, np.uint16)
assert_type(b1 & u4, np.uint32)
assert_type(b1 & u8, np.uint64)
assert_type(b1 & i1, np.int8)
assert_type(b1 & i2, np.int16)
assert_type(b1 & i4, np.int32)
assert_type(b1 & i8, np.int64)

assert_type(u1 & b0, np.uint8)
assert_type(u1 & b1, np.uint8)
assert_type(u1 & u1, np.uint8)
assert_type(u1 & u2, np.uint16)
assert_type(u1 & u4, np.uint32)
assert_type(u1 & u8, np.uint64)
assert_type(u1 & i1, np.int16)
assert_type(u1 & i2, np.int16)
assert_type(u1 & i4, np.int32)
assert_type(u1 & i8, np.int64)

assert_type(u2 & b0, np.uint16)
assert_type(u2 & b1, np.uint16)
assert_type(u2 & u1, np.uint16)
assert_type(u2 & u2, np.uint16)
assert_type(u2 & u4, np.uint32)
assert_type(u2 & u8, np.uint64)
assert_type(u2 & i1, np.int32)
assert_type(u2 & i2, np.int32)
assert_type(u2 & i4, np.int32)
assert_type(u2 & i8, np.int64)

assert_type(u4 & b0, np.uint32)
assert_type(u4 & b1, np.uint32)
assert_type(u4 & u1, np.uint32)
assert_type(u4 & u2, np.uint32)
assert_type(u4 & u4, np.uint32)
assert_type(u4 & u8, np.uint64)
assert_type(u4 & i1, np.int64)
assert_type(u4 & i2, np.int64)
assert_type(u4 & i4, np.int64)
assert_type(u4 & i8, np.int64)

assert_type(u8 & b0, np.uint64)
assert_type(u8 & b1, np.uint64)
assert_type(u8 & u1, np.uint64)
assert_type(u8 & u2, np.uint64)
assert_type(u8 & u4, np.uint64)
assert_type(u8 & u8, np.uint64)
u8 & i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 & b0, np.int8)
assert_type(i1 & b1, np.int8)
assert_type(i1 & u1, np.int16)
assert_type(i1 & u2, np.int32)
assert_type(i1 & u4, np.int64)
i1 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1 & i1, np.int8)
assert_type(i1 & i2, np.int16)
assert_type(i1 & i4, np.int32)
assert_type(i1 & i8, np.int64)

assert_type(i2 & b0, np.int16)
assert_type(i2 & b1, np.int16)
assert_type(i2 & u1, np.int16)
assert_type(i2 & u2, np.int32)
assert_type(i2 & u4, np.int64)
i2 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2 & i1, np.int16)
assert_type(i2 & i2, np.int16)
assert_type(i2 & i4, np.int32)
assert_type(i2 & i8, np.int64)

assert_type(i4 & b0, np.int32)
assert_type(i4 & b1, np.int32)
assert_type(i4 & u1, np.int32)
assert_type(i4 & u2, np.int32)
assert_type(i4 & u4, np.int64)
i4 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4 & i1, np.int32)
assert_type(i4 & i2, np.int32)
assert_type(i4 & i4, np.int32)
assert_type(i4 & i8, np.int64)

assert_type(i8 & b0, np.int64)
assert_type(i8 & b1, np.int64)
assert_type(i8 & u1, np.int64)
assert_type(i8 & u2, np.int64)
assert_type(i8 & u4, np.int64)
i8 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 & i1, np.int64)
assert_type(i8 & i2, np.int64)
assert_type(i8 & i4, np.int64)
assert_type(i8 & i8, np.int64)

###
# __[r]xor__

assert_type(b1 ^ b0, np.bool)
assert_type(b1 ^ b1, np.bool)
assert_type(b1 ^ u1, np.uint8)
assert_type(b1 ^ u2, np.uint16)
assert_type(b1 ^ u4, np.uint32)
assert_type(b1 ^ u8, np.uint64)
assert_type(b1 ^ i1, np.int8)
assert_type(b1 ^ i2, np.int16)
assert_type(b1 ^ i4, np.int32)
assert_type(b1 ^ i8, np.int64)

assert_type(u1 ^ b0, np.uint8)
assert_type(u1 ^ b1, np.uint8)
assert_type(u1 ^ u1, np.uint8)
assert_type(u1 ^ u2, np.uint16)
assert_type(u1 ^ u4, np.uint32)
assert_type(u1 ^ u8, np.uint64)
assert_type(u1 ^ i1, np.int16)
assert_type(u1 ^ i2, np.int16)
assert_type(u1 ^ i4, np.int32)
assert_type(u1 ^ i8, np.int64)

assert_type(u2 ^ b0, np.uint16)
assert_type(u2 ^ b1, np.uint16)
assert_type(u2 ^ u1, np.uint16)
assert_type(u2 ^ u2, np.uint16)
assert_type(u2 ^ u4, np.uint32)
assert_type(u2 ^ u8, np.uint64)
assert_type(u2 ^ i1, np.int32)
assert_type(u2 ^ i2, np.int32)
assert_type(u2 ^ i4, np.int32)
assert_type(u2 ^ i8, np.int64)

assert_type(u4 ^ b0, np.uint32)
assert_type(u4 ^ b1, np.uint32)
assert_type(u4 ^ u1, np.uint32)
assert_type(u4 ^ u2, np.uint32)
assert_type(u4 ^ u4, np.uint32)
assert_type(u4 ^ u8, np.uint64)
assert_type(u4 ^ i1, np.int64)
assert_type(u4 ^ i2, np.int64)
assert_type(u4 ^ i4, np.int64)
assert_type(u4 ^ i8, np.int64)

assert_type(u8 ^ b0, np.uint64)
assert_type(u8 ^ b1, np.uint64)
assert_type(u8 ^ u1, np.uint64)
assert_type(u8 ^ u2, np.uint64)
assert_type(u8 ^ u4, np.uint64)
assert_type(u8 ^ u8, np.uint64)
u8 ^ i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 ^ b0, np.int8)
assert_type(i1 ^ b1, np.int8)
assert_type(i1 ^ u1, np.int16)
assert_type(i1 ^ u2, np.int32)
assert_type(i1 ^ u4, np.int64)
i1 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1 ^ i1, np.int8)
assert_type(i1 ^ i2, np.int16)
assert_type(i1 ^ i4, np.int32)
assert_type(i1 ^ i8, np.int64)

assert_type(i2 ^ b0, np.int16)
assert_type(i2 ^ b1, np.int16)
assert_type(i2 ^ u1, np.int16)
assert_type(i2 ^ u2, np.int32)
assert_type(i2 ^ u4, np.int64)
i2 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2 ^ i1, np.int16)
assert_type(i2 ^ i2, np.int16)
assert_type(i2 ^ i4, np.int32)
assert_type(i2 ^ i8, np.int64)

assert_type(i4 ^ b0, np.int32)
assert_type(i4 ^ b1, np.int32)
assert_type(i4 ^ u1, np.int32)
assert_type(i4 ^ u2, np.int32)
assert_type(i4 ^ u4, np.int64)
i4 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4 ^ i1, np.int32)
assert_type(i4 ^ i2, np.int32)
assert_type(i4 ^ i4, np.int32)
assert_type(i4 ^ i8, np.int64)

assert_type(i8 ^ b0, np.int64)
assert_type(i8 ^ b1, np.int64)
assert_type(i8 ^ u1, np.int64)
assert_type(i8 ^ u2, np.int64)
assert_type(i8 ^ u4, np.int64)
i8 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 ^ i1, np.int64)
assert_type(i8 ^ i2, np.int64)
assert_type(i8 ^ i4, np.int64)
assert_type(i8 ^ i8, np.int64)

###
# __[r]or__

assert_type(b1 | b0, np.bool)
assert_type(b1 | b1, np.bool)
assert_type(b1 | u1, np.uint8)
assert_type(b1 | u2, np.uint16)
assert_type(b1 | u4, np.uint32)
assert_type(b1 | u8, np.uint64)
assert_type(b1 | i1, np.int8)
assert_type(b1 | i2, np.int16)
assert_type(b1 | i4, np.int32)
assert_type(b1 | i8, np.int64)

assert_type(u1 | b0, np.uint8)
assert_type(u1 | b1, np.uint8)
assert_type(u1 | u1, np.uint8)
assert_type(u1 | u2, np.uint16)
assert_type(u1 | u4, np.uint32)
assert_type(u1 | u8, np.uint64)
assert_type(u1 | i1, np.int16)
assert_type(u1 | i2, np.int16)
assert_type(u1 | i4, np.int32)
assert_type(u1 | i8, np.int64)

assert_type(u2 | b0, np.uint16)
assert_type(u2 | b1, np.uint16)
assert_type(u2 | u1, np.uint16)
assert_type(u2 | u2, np.uint16)
assert_type(u2 | u4, np.uint32)
assert_type(u2 | u8, np.uint64)
assert_type(u2 | i1, np.int32)
assert_type(u2 | i2, np.int32)
assert_type(u2 | i4, np.int32)
assert_type(u2 | i8, np.int64)

assert_type(u4 | b0, np.uint32)
assert_type(u4 | b1, np.uint32)
assert_type(u4 | u1, np.uint32)
assert_type(u4 | u2, np.uint32)
assert_type(u4 | u4, np.uint32)
assert_type(u4 | u8, np.uint64)
assert_type(u4 | i1, np.int64)
assert_type(u4 | i2, np.int64)
assert_type(u4 | i4, np.int64)
assert_type(u4 | i8, np.int64)

assert_type(u8 | b0, np.uint64)
assert_type(u8 | b1, np.uint64)
assert_type(u8 | u1, np.uint64)
assert_type(u8 | u2, np.uint64)
assert_type(u8 | u4, np.uint64)
assert_type(u8 | u8, np.uint64)
u8 | i1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | i2  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | i4  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1 | b0, np.int8)
assert_type(i1 | b1, np.int8)
assert_type(i1 | u1, np.int16)
assert_type(i1 | u2, np.int32)
assert_type(i1 | u4, np.int64)
i1 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1 | i1, np.int8)
assert_type(i1 | i2, np.int16)
assert_type(i1 | i4, np.int32)
assert_type(i1 | i8, np.int64)

assert_type(i2 | b0, np.int16)
assert_type(i2 | b1, np.int16)
assert_type(i2 | u1, np.int16)
assert_type(i2 | u2, np.int32)
assert_type(i2 | u4, np.int64)
i2 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2 | i1, np.int16)
assert_type(i2 | i2, np.int16)
assert_type(i2 | i4, np.int32)
assert_type(i2 | i8, np.int64)

assert_type(i4 | b0, np.int32)
assert_type(i4 | b1, np.int32)
assert_type(i4 | u1, np.int32)
assert_type(i4 | u2, np.int32)
assert_type(i4 | u4, np.int64)
i4 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4 | i1, np.int32)
assert_type(i4 | i2, np.int32)
assert_type(i4 | i4, np.int32)
assert_type(i4 | i8, np.int64)

assert_type(i8 | b0, np.int64)
assert_type(i8 | b1, np.int64)
assert_type(i8 | u1, np.int64)
assert_type(i8 | u2, np.int64)
assert_type(i8 | u4, np.int64)
i8 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 | i1, np.int64)
assert_type(i8 | i2, np.int64)
assert_type(i8 | i4, np.int64)
assert_type(i8 | i8, np.int64)
