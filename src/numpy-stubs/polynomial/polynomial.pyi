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
    _FuncInteg,
    _FuncLine,
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
)
from .polyutils import trimcoef as polytrim

__all__ = [
    "Polynomial",
    "polyadd",
    "polycompanion",
    "polyder",
    "polydiv",
    "polydomain",
    "polyfit",
    "polyfromroots",
    "polygrid2d",
    "polygrid3d",
    "polyint",
    "polyline",
    "polymul",
    "polymulx",
    "polyone",
    "polypow",
    "polyroots",
    "polysub",
    "polytrim",
    "polyval",
    "polyval2d",
    "polyval3d",
    "polyvalfromroots",
    "polyvander",
    "polyvander2d",
    "polyvander3d",
    "polyx",
    "polyzero",
]

polydomain: Final[Array_1d[np.float64]] = ...
polyzero: Final[Array_1d[np.int_]] = ...
polyone: Final[Array_1d[np.int_]] = ...
polyx: Final[Array_1d[np.int_]] = ...

polyline: Final[_FuncLine[L["Polyline"]]] = ...
polyfromroots: Final[_FuncFromRoots[L["polyfromroots"]]] = ...
polyadd: Final[_FuncBinOp[L["polyadd"]]] = ...
polysub: Final[_FuncBinOp[L["polysub"]]] = ...
polymulx: Final[_FuncUnOp[L["polymulx"]]] = ...
polymul: Final[_FuncBinOp[L["polymul"]]] = ...
polydiv: Final[_FuncBinOp[L["polydiv"]]] = ...
polypow: Final[_FuncPow[L["polypow"]]] = ...
polyder: Final[_FuncDer[L["polyder"]]] = ...
polyint: Final[_FuncInteg[L["polyint"]]] = ...
polyval: Final[_FuncVal[L["polyval"]]] = ...
polyval2d: Final[_FuncVal2D[L["polyval2d"]]] = ...
polyval3d: Final[_FuncVal3D[L["polyval3d"]]] = ...
polyvalfromroots: Final[_FuncValFromRoots[L["polyvalfromroots"]]] = ...
polygrid2d: Final[_FuncVal2D[L["polygrid2d"]]] = ...
polygrid3d: Final[_FuncVal3D[L["polygrid3d"]]] = ...
polyvander: Final[_FuncVander[L["polyvander"]]] = ...
polyvander2d: Final[_FuncVander2D[L["polyvander2d"]]] = ...
polyvander3d: Final[_FuncVander3D[L["polyvander3d"]]] = ...
polyfit: Final[_FuncFit[L["polyfit"]]] = ...
polycompanion: Final[_FuncCompanion[L["polycompanion"]]] = ...
polyroots: Final[_FuncRoots[L["polyroots"]]] = ...

class Polynomial(ABCPolyBase):
    domain: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: None = None  # pyright: ignore[reportIncompatibleMethodOverride]
