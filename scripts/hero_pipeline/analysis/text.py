"""Combined effect and behavior analysis namespace for remaining callers."""

from .behavior import *  # noqa: F403
from .effects import *  # noqa: F403
from .behavior import (  # noqa: F401
    build_behavior_for_heroes,
    compute_is_dual_range,
    compute_is_melee,
    infer_signature_calculated,
)
from . import behavior as _behavior
from . import effects as _effects

for _name, _value in _effects.__dict__.items():
    if _name not in globals():
        globals()[_name] = _value
for _name, _value in _behavior.__dict__.items():
    if _name not in globals():
        globals()[_name] = _value
