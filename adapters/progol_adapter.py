#!/usr/bin/env python3
"""
PROGOL adapter: maps Mexican Government lottery game payloads to CanonicalMatch.
"""

from typing import Any, Dict, List

from core.structure_adapter import CanonicalMatch, build_dimensions, STANDARD_DIM_KEYS


class ProgolAdapter:
    """Adapter for PROGOL_FULLWEEK and PROGOL_MIDWEEK game structures."""

    def adapt(self, league_id: str, games: List[Dict[str, Any]]) -> List[CanonicalMatch]:
        canon: List[CanonicalMatch] = []
        for g in games or []:
            home = g.get("home_team") or g.get("home") or g.get("homeName") or "TBD"
            away = g.get("away_team") or g.get("away") or g.get("awayName") or "TBD"
            match_id = (
                str(g.get("game_id")
                    or g.get("id")
                    or g.get("matchId")
                    or f"{league_id}:{home}-{away}")
            )

            # Dimensions may already exist or be spread across keys; normalize gracefully
            dims_raw = g.get("dimensions") or {}
            dims_kwargs: Dict[str, Any] = {}
            for key in STANDARD_DIM_KEYS:
                # Prefer already standardized keys; fall back to common alternates
                if key in dims_raw:
                    dims_kwargs[key] = dims_raw.get(key)
            # Common alternates used in docs
            dims_kwargs.setdefault("polymarket_odds", g.get("polymarket_odds") or (g.get("D0_polymarket") if isinstance(g.get("D0_polymarket"), (int, float)) else 0))
            dims_kwargs.setdefault("historical_matchups", g.get("historical_matchups") or g.get("D1_historical") or 0)
            dims_kwargs.setdefault("weather_venue", g.get("weather_venue") or g.get("D2_venue") or 0)
            dims_kwargs.setdefault("sentiment", g.get("sentiment") or g.get("D3_sentiment") or 0)
            dims_kwargs.setdefault("market_efficiency", g.get("market_efficiency") or g.get("D4_market_efficiency") or 0)
            dims_kwargs.setdefault("team_performance", g.get("team_performance") or g.get("D5_team_performance") or 0)
            dims_kwargs.setdefault("key_players", g.get("key_players") or g.get("D6_key_players") or 0)
            dims_kwargs.setdefault("x_factor", g.get("x_factor") or g.get("D7_x_factor") or 0)

            canon.append(
                CanonicalMatch(
                    league_id=league_id,
                    match_id=match_id,
                    home_team=home,
                    away_team=away,
                    date=g.get("date"),
                    time=g.get("time"),
                    venue=g.get("venue"),
                    country_code=g.get("country_code") or "🇲🇽",
                    status=g.get("status") or "scheduled",
                    completed=bool(g.get("completed")) if g.get("completed") is not None else False,
                    source=g.get("data_source") or "MEXICAN_GOVERNMENT_PROGOL",
                    dimensions=build_dimensions(**dims_kwargs),
                    raw=g,
                )
            )
        return canon