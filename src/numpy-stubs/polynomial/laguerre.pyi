from typing import Final, Literal as L

import numpy as np
from _numtype import Array_1d

from ._polybase import ABCPolyBase
from ._polytypes import (
    _FuncBinOp,
    _FuncCompanion,
    _FuncDer,
    _FuncFit,
    _FuncFromRoots,
    _FuncGauss,
    _FuncInteg,
    _FuncLine,
    _FuncPoly2Ortho,
    _FuncPow,
    _FuncRoots,
    _FuncUnOp,
    _FuncVal,
    _FuncVal2D,
    _FuncVal3D,
    _FuncValFromRoots,
    _FuncVander,
    _FuncVander2D,
    _FuncVander3D,
    _FuncWeight,
)
from .polyutils import trimcoef as lagtrim

__all__ = [
    "Laguerre",
    "lag2poly",
    "lagadd",
    "lagcompanion",
    "lagder",
    "lagdiv",
    "lagdomain",
    "lagfit",
    "lagfromroots",
    "laggauss",
    "laggrid2d",
    "laggrid3d",
    "lagint",
    "lagline",
    "lagmul",
    "lagmulx",
    "lagone",
    "lagpow",
    "lagroots",
    "lagsub",
    "lagtrim",
    "lagval",
    "lagval2d",
    "lagval3d",
    "lagvander",
    "lagvander2d",
    "lagvander3d",
    "lagweight",
    "lagx",
    "lagzero",
    "poly2lag",
]

lagdomain: Final[Array_1d[np.float64]] = ...
lagzero: Final[Array_1d[np.int_]] = ...
lagone: Final[Array_1d[np.int_]] = ...
lagx: Final[Array_1d[np.int_]] = ...

poly2lag: Final[_FuncPoly2Ortho[L["poly2lag"]]] = ...
lag2poly: Final[_FuncUnOp[L["lag2poly"]]] = ...
lagline: Final[_FuncLine[L["lagline"]]] = ...
lagfromroots: Final[_FuncFromRoots[L["lagfromroots"]]] = ...
lagadd: Final[_FuncBinOp[L["lagadd"]]] = ...
lagsub: Final[_FuncBinOp[L["lagsub"]]] = ...
lagmulx: Final[_FuncUnOp[L["lagmulx"]]] = ...
lagmul: Final[_FuncBinOp[L["lagmul"]]] = ...
lagdiv: Final[_FuncBinOp[L["lagdiv"]]] = ...
lagpow: Final[_FuncPow[L["lagpow"]]] = ...
lagder: Final[_FuncDer[L["lagder"]]] = ...
lagint: Final[_FuncInteg[L["lagint"]]] = ...
lagval: Final[_FuncVal[L["lagval"]]] = ...
lagval2d: Final[_FuncVal2D[L["lagval2d"]]] = ...
lagval3d: Final[_FuncVal3D[L["lagval3d"]]] = ...
lagvalfromroots: Final[_FuncValFromRoots[L["lagvalfromroots"]]] = ...
laggrid2d: Final[_FuncVal2D[L["laggrid2d"]]] = ...
laggrid3d: Final[_FuncVal3D[L["laggrid3d"]]] = ...
lagvander: Final[_FuncVander[L["lagvander"]]] = ...
lagvander2d: Final[_FuncVander2D[L["lagvander2d"]]] = ...
lagvander3d: Final[_FuncVander3D[L["lagvander3d"]]] = ...
lagfit: Final[_FuncFit[L["lagfit"]]] = ...
lagcompanion: Final[_FuncCompanion[L["lagcompanion"]]] = ...
lagroots: Final[_FuncRoots[L["lagroots"]]] = ...
laggauss: Final[_FuncGauss[L["laggauss"]]] = ...
lagweight: Final[_FuncWeight[L["lagweight"]]] = ...

class Laguerre(ABCPolyBase):
    domain: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["L"] = "L"  # pyright: ignore[reportIncompatibleMethodOverride]
