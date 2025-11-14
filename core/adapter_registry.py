#!/usr/bin/env python3
"""
Adapter registry and normalization helper.

This lets consumers request canonical matches for any supported league
without worrying about the underlying data structure.
"""

from typing import Any, Dict, List, Optional, Type

from core.structure_adapter import CanonicalMatch, LeagueAdapter
from adapters.progol_adapter import ProgolAdapter
from adapters.liga_mx_adapter import LigaMXAdapter


ADAPTERS: Dict[str, Type[LeagueAdapter]] = {
    # Mexican Government Lottery
    "PROGOL_FULLWEEK": ProgolAdapter,
    "PROGOL_MIDWEEK": ProgolAdapter,
    # Mexican Football
    "LIGA_MX": LigaMXAdapter,
}


def get_adapter(league_id: str) -> Optional[LeagueAdapter]:
    cls = ADAPTERS.get(league_id.upper()) or ADAPTERS.get(league_id)
    return cls() if cls else None


def normalize_games(league_id: str, games: List[Dict[str, Any]]) -> List[CanonicalMatch]:
    adapter = get_adapter(league_id)
    if not adapter:
        # Fall back: wrap raw payload minimally so downstream consumers can still iterate
        return [
            CanonicalMatch(
                league_id=league_id,
                match_id=str(g.get("game_id") or g.get("id") or f"{league_id}:{i}"),
                home_team=g.get("home_team") or g.get("home") or "TBD",
                away_team=g.get("away_team") or g.get("away") or "TBD",
                date=g.get("date"),
                time=g.get("time"),
                venue=g.get("venue"),
                country_code=g.get("country_code") or None,
                status=g.get("status") or "scheduled",
                completed=bool(g.get("completed")) if g.get("completed") is not None else False,
                source=g.get("data_source") or "UNKNOWN_SOURCE",
                raw=g,
            )
            for i, g in enumerate(games or [])
        ]
    return adapter.adapt(league_id, games)