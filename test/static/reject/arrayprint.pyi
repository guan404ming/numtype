from collections.abc import Callable
from typing import Any

import numpy as np
import numpy.typing as npt

AR: npt.NDArray[np.float64]
func1: Callable[[Any], str]
func2: Callable[[np.integer], str]

np.array2string(AR, style=None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.array2string(AR, legacy="1.14")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.array2string(AR, sign="*")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.array2string(AR, floatmode="default")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.array2string(AR, formatter={"A": func1})  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.array2string(AR, formatter={"float": func2})  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
