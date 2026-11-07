"""Dataset loading and quality filtering for the Helios benchmark."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List


@dataclass
class Observation:
    station: str
    timestamp: datetime
    ghi: float
    temperature: float


def load_station(path: str | Path, station: str) -> List[Observation]:
    rows: List[Observation] = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["station"] != station:
                continue
            rows.append(
                Observation(
                    station=row["station"],
                    timestamp=datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00")),
                    ghi=float(row["ghi_wm2"]),
                    temperature=float(row["temperature_c"]),
                )
            )
    rows.sort(key=lambda item: item.timestamp)
    return rows


def quality_filter(rows: List[Observation], max_gap_hours: int = 3) -> List[Observation]:
    """Drop rows that follow a gap longer than ``max_gap_hours``."""
    kept: List[Observation] = []
    previous = None
    for row in rows:
        if previous is not None:
            gap = (row.timestamp - previous.timestamp).total_seconds() / 3600.0
            if gap > max_gap_hours:
                previous = row
                continue
        kept.append(row)
        previous = row
    return kept


def station_summary(rows: List[Observation]) -> Dict[str, float]:
    if not rows:
        return {"count": 0}
    return {
        "count": len(rows),
        "ghi_mean": sum(r.ghi for r in rows) / len(rows),
        "ghi_max": max(r.ghi for r in rows),
    }
