"""Reference model adapters used by the Helios benchmark."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class PersistenceModel:
    """Naive baseline: the next value equals the last observed value."""

    def predict(self, history: Iterable[float]) -> List[float]:
        values = list(history)
        horizon = len(values) // 2 or 1
        return [values[-1]] * horizon


@dataclass
class ClimatologyModel:
    """Hour-of-day climatology fitted on the training window."""

    hourly_profile: dict

    def predict(self, history: Iterable[float], hours: Iterable[int]) -> List[float]:
        return [self.hourly_profile.get(h, 0.0) for h in hours]


def build_model(name: str, **kwargs):
    name = name.lower()
    if name == "persistence":
        return PersistenceModel()
    if name == "climatology":
        return ClimatologyModel(kwargs["hourly_profile"])
    raise ValueError(f"unknown model: {name}")
