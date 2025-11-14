#!/usr/bin/env python3
"""
Adaptive League Structure: Canonical schema and adapter interface

Purpose: Give Loly a single, resilient match format that every league can map to.
This enables pivoting across different league structures without breaking pipelines.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Protocol


@dataclass
class CanonicalMatch:
    """Unified representation of a sports match/game across leagues."""
    league_id: str
    match_id: str
    home_team: str
    away_team: str
    date: Optional[str] = None
    time: Optional[str] = None
    venue: Optional[str] = None
    country_code: Optional[str] = None
    status: Optional[str] = None
    completed: Optional[bool] = None
    source: Optional[str] = None
    # Standardized 8D dimensions used by dashboards (values are percentages 0-100)
    dimensions: Dict[str, float] = field(default_factory=dict)
    # Original raw game payload for traceability/debug
    raw: Dict[str, Any] = field(default_factory=dict)


class LeagueAdapter(Protocol):
    """Adapter contract to map arbitrary league game payloads into CanonicalMatch."""

    def adapt(self, league_id: str, games: List[Dict[str, Any]]) -> List[CanonicalMatch]:
        ...


def _safe_pct(value: Any) -> float:
    """Coerce numeric values into a 0-100 float percentage, defaulting safely."""
    try:
        f = float(value)
        # If the value looks like 0-1, convert to 0-100; otherwise clamp to 0-100
        if 0.0 <= f <= 1.0:
            return max(0.0, min(100.0, f * 100.0))
        return max(0.0, min(100.0, f))
    except Exception:
        return 0.0


STANDARD_DIM_KEYS = (
    "polymarket_odds",
    "historical_matchups",
    "weather_venue",
    "sentiment",
    "market_efficiency",
    "team_performance",
    "key_players",
    "x_factor",
)


def build_dimensions(**kwargs: Any) -> Dict[str, float]:
    """Build a dimensions dict with safe defaults and standardized keys."""
    dims: Dict[str, float] = {}
    for key in STANDARD_DIM_KEYS:
        dims[key] = _safe_pct(kwargs.get(key, 0.0))
    return dims