import numpy as np

DTYPE_i8: np.dtype[np.int64]

np.mintypecode(DTYPE_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.iscomplexobj(DTYPE_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.isrealobj(DTYPE_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.typename(DTYPE_i8)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.typename("invalid")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.common_type(np.timedelta64())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
