"""Forecast skill metrics reported by the Helios benchmark."""

from __future__ import annotations

from math import sqrt


def mean_absolute_error(predicted, observed) -> float:
    pairs = list(zip(predicted, observed))
    if not pairs:
        return float("nan")
    return sum(abs(p - o) for p, o in pairs) / len(pairs)


def root_mean_squared_error(predicted, observed) -> float:
    pairs = list(zip(predicted, observed))
    if not pairs:
        return float("nan")
    return sqrt(sum((p - o) ** 2 for p, o in pairs) / len(pairs))


def forecast_skill(predicted, observed, reference) -> float:
    """Relative improvement over the reference forecast (0..1)."""
    mse_model = sum((p - o) ** 2 for p, o in zip(predicted, observed)) / len(predicted)
    mse_ref = sum((r - o) ** 2 for r, o in zip(reference, observed)) / len(reference)
    if mse_ref == 0:
        return 0.0
    return 1.0 - mse_model / mse_ref
