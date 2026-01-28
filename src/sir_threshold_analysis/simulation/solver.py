# src/sir_threshold_analysis/solvers/euler.py
from __future__ import annotations
from typing import Protocol, Tuple, List, runtime_checkable

State = Tuple[float, ...]

@runtime_checkable
class HasDerivatives(Protocol):
    def derivatives(self,
                    t: float,
                    y: State) -> State:
        """Return dy/dt at time t for state y."""

def euler_step(model: HasDerivatives,
               t: float,
               y: State,
               dt: float) -> State:
    """
    One explicit Euler step: y_{n+1} = y_n + dt * f(t_n, y_n)
    """
    if dt <= 0:
        raise ValueError(f"dt must be > 0, got {dt}")

    dydt = model.derivatives(t, y)
    if len(dydt) != len(y):
        raise ValueError(
            f"derivatives() returned length {len(dydt)} but state has length {len(y)}"
        )

    return tuple(yi + dt * dyi for yi, dyi in zip(y, dydt))

def simulate(
        model: HasDerivatives,
        y0: State,
        t_end: float,
        dt: float,
        t0: float = 0.0,
) -> List[Tuple[float, *State]]:  # type: ignore[misc]
    """
    Simulate forward in time using explicit Euler.

    Returns a list of tuples: (t, *state)
    Example: SIR -> (t, S, I, R), SEIR -> (t, S, E, I, R), etc.
    """
    if dt <= 0:
        raise ValueError(f"dt must be > 0, got {dt}")
    if t_end < t0:
        raise ValueError(f"t_end must be >= t0 (t0={t0}), got t_end={t_end}")

    t = float(t0)
    y: State = tuple(float(v) for v in y0)
    history: List[Tuple[float, *State]] = []  # type: ignore[misc]

    # Avoid floating-point “miss the last step by a hair”
    eps = dt * 1e-12

    while t <= t_end + eps:
        history.append((t, *y))
        y = euler_step(model, t, y, dt)
        t += dt

    return history