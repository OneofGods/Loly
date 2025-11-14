#!/usr/bin/env python3
"""
Liga MX adapter: maps MedioTiempo/ESPN Liga MX payloads to CanonicalMatch.
"""

from typing import Any, Dict, List

from core.structure_adapter import CanonicalMatch, build_dimensions


class LigaMXAdapter:
    """Adapter for LIGA_MX matches from real_mediotiempo_liga_mx_fetcher or espn fetchers."""

    def adapt(self, league_id: str, games: List[Dict[str, Any]]) -> List[CanonicalMatch]:
        canon: List[CanonicalMatch] = []
        for g in games or []:
            home = g.get("home_team") or g.get("home") or "TBD"
            away = g.get("away_team") or g.get("away") or "TBD"
            match_id = (
                str(g.get("game_id") or g.get("id") or f"{league_id}:{home}-{away}")
            )

            dims = build_dimensions(
                polymarket_odds=g.get("polymarket_odds", 0),
                historical_matchups=g.get("historical_matchups", 0),
                weather_venue=g.get("weather_venue", 0),
                sentiment=g.get("sentiment", 0),
                market_efficiency=g.get("market_efficiency", 0),
                team_performance=g.get("team_performance", 0),
                key_players=g.get("key_players", 0),
                x_factor=g.get("x_factor", 0),
            )

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
                    source=g.get("data_source") or (
                        "MEDIOTIEMPO_CESS_API_REAL" if g.get("real_mediotiempo_data") else "ESPN_API_REAL"
                    ),
                    dimensions=dims,
                    raw=g,
                )
            )
        return canon