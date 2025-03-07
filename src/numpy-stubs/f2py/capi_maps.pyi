from .auxfuncs import _ROut, _Var, process_f2cmap_dict

__all__ = [
    "cb_routsign2map",
    "cb_sign2map",
    "common_sign2map",
    "getarrdims",
    "getarrdocsign",
    "getctype",
    "getinit",
    "getpydocsign",
    "getstrlength",
    "modsign2map",
    "process_f2cmap_dict",
    "routsign2map",
    "sign2map",
]

###

def getctype(var: _Var) -> str: ...
def f2cexpr(expr: str) -> str: ...
def getstrlength(var: _Var) -> str: ...
def getarrdims(a: str, var: _Var, verbose: int = 0) -> dict[str, str]: ...
def getpydocsign(a: str, var: _Var) -> tuple[str, str]: ...
def getarrdocsign(a: str, var: _Var) -> str: ...
def getinit(a: str, var: _Var) -> tuple[str, str]: ...
def sign2map(a: str, var: _Var) -> dict[str, str]: ...
def routsign2map(rout: _ROut) -> dict[str, str]: ...
def modsign2map(m: _ROut) -> dict[str, str]: ...
def cb_sign2map(a: str, var: _Var, index: object | None = None) -> dict[str, str]: ...
def cb_routsign2map(rout: _ROut, um: str) -> dict[str, str]: ...
def common_sign2map(a: str, var: _Var) -> dict[str, str]: ...  # obsolete
