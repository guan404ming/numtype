from typing import Final, Literal as L
from typing_extensions import TypeVar

import numpy as np
from _numtype import Array, Array_1d

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
from .polyutils import trimcoef as hermtrim

__all__ = [
    "Hermite",
    "herm2poly",
    "hermadd",
    "hermcompanion",
    "hermder",
    "hermdiv",
    "hermdomain",
    "hermfit",
    "hermfromroots",
    "hermgauss",
    "hermgrid2d",
    "hermgrid3d",
    "hermint",
    "hermline",
    "hermmul",
    "hermmulx",
    "hermone",
    "hermpow",
    "hermroots",
    "hermsub",
    "hermtrim",
    "hermval",
    "hermval2d",
    "hermval3d",
    "hermvander",
    "hermvander2d",
    "hermvander3d",
    "hermweight",
    "hermx",
    "hermzero",
    "poly2herm",
]

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])

hermdomain: Final[Array_1d[np.float64]] = ...
hermzero: Final[Array_1d[np.int_]] = ...
hermone: Final[Array_1d[np.int_]] = ...
hermx: Final[Array_1d[np.int_]] = ...

poly2herm: Final[_FuncPoly2Ortho[L["poly2herm"]]] = ...
herm2poly: Final[_FuncUnOp[L["herm2poly"]]] = ...
hermline: Final[_FuncLine[L["hermline"]]] = ...
hermfromroots: Final[_FuncFromRoots[L["hermfromroots"]]] = ...
hermadd: Final[_FuncBinOp[L["hermadd"]]] = ...
hermsub: Final[_FuncBinOp[L["hermsub"]]] = ...
hermmulx: Final[_FuncUnOp[L["hermmulx"]]] = ...
hermmul: Final[_FuncBinOp[L["hermmul"]]] = ...
hermdiv: Final[_FuncBinOp[L["hermdiv"]]] = ...
hermpow: Final[_FuncPow[L["hermpow"]]] = ...
hermder: Final[_FuncDer[L["hermder"]]] = ...
hermint: Final[_FuncInteg[L["hermint"]]] = ...
hermval: Final[_FuncVal[L["hermval"]]] = ...
hermval2d: Final[_FuncVal2D[L["hermval2d"]]] = ...
hermval3d: Final[_FuncVal3D[L["hermval3d"]]] = ...
hermvalfromroots: Final[_FuncValFromRoots[L["hermvalfromroots"]]] = ...
hermgrid2d: Final[_FuncVal2D[L["hermgrid2d"]]] = ...
hermgrid3d: Final[_FuncVal3D[L["hermgrid3d"]]] = ...
hermvander: Final[_FuncVander[L["hermvander"]]] = ...
hermvander2d: Final[_FuncVander2D[L["hermvander2d"]]] = ...
hermvander3d: Final[_FuncVander3D[L["hermvander3d"]]] = ...
hermfit: Final[_FuncFit[L["hermfit"]]] = ...
hermcompanion: Final[_FuncCompanion[L["hermcompanion"]]] = ...
hermroots: Final[_FuncRoots[L["hermroots"]]] = ...
hermgauss: Final[_FuncGauss[L["hermgauss"]]] = ...
hermweight: Final[_FuncWeight[L["hermweight"]]] = ...

def _normed_hermite_n(x: Array[np.float64, _ShapeT], n: int | np.intp) -> Array[np.float64, _ShapeT]: ...

class Hermite(ABCPolyBase):
    domain: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["H"] = "H"  # pyright: ignore[reportIncompatibleMethodOverride]
