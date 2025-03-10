from types import ModuleType

# NOTE: these 5 areonly defined on systems with an intel processor
SSE42: ModuleType | None = ...
FMA3: ModuleType | None = ...
AVX2: ModuleType | None = ...
AVX512F: ModuleType | None = ...
AVX512_SKX: ModuleType | None = ...

baseline: ModuleType | None = ...

# TODO(jorenham): TypedDict
targets: dict[str, ModuleType | None] = ...

def clear_floatstatus() -> None: ...
def get_floatstatus() -> int: ...
