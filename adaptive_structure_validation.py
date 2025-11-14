#!/usr/bin/env python3
"""
🔥💀🔥 ADAPTIVE STRUCTURE VALIDATION - LOLY PIVOT POWER 💀🔥💀

Quick demo that Loly can pivot across different league structures
by normalizing games into a single CanonicalMatch format.
"""

import asyncio
from typing import List

from core.adapter_registry import normalize_games
from live_progol_fetcher import AuthenticProgolFetcher
from real_mediotiempo_liga_mx_fetcher import RealMedioTiempoLigaMXFetcher


async def fetch_and_normalize(league_id: str) -> List:
    if league_id.upper() in ("PROGOL_FULLWEEK", "PROGOL_MIDWEEK"):
        fetcher = AuthenticProgolFetcher()
        games = await fetcher.get_fullweek_games() if league_id.upper() == "PROGOL_FULLWEEK" else await fetcher.get_midweek_games()  # type: ignore[attr-defined]
    elif league_id.upper() == "LIGA_MX":
        fetcher = RealMedioTiempoLigaMXFetcher()
        games = await fetcher.get_todays_games()
    else:
        games = []

    return normalize_games(league_id, games)


async def main():
    print("🔥💀🔥 TESTING LOLY'S ADAPTIVE STRUCTURE LEARNING 💀🔥💀")
    leagues = ["PROGOL_FULLWEEK", "PROGOL_MIDWEEK", "LIGA_MX"]
    for lid in leagues:
        try:
            canon = await fetch_and_normalize(lid)
            print(f"\n🎯 League: {lid} → Canonical matches: {len(canon)}")
            # Show a tiny sample for confidence
            for m in canon[:3]:
                print(
                    f"  • {m.away_team} @ {m.home_team} | id={m.match_id} | status={m.status} | completed={m.completed}"
                )
                # Show a subset of dimensions for proof of normalization
                dims = m.dimensions or {}
                subset_keys = ["market_efficiency", "team_performance", "key_players"]
                subset_view = {k: round(dims.get(k, 0.0), 1) for k in subset_keys}
                print(f"    dims: {subset_view}")
        except Exception as e:
            print(f"⚠️ {lid} normalization error: {e}")

    print("\n🎉💀🎉 ULTIMATE LEGENDARY VICTORY CELEBRATION! LOLY IS UNSTOPPABLE! 💀🎉💀")


if __name__ == "__main__":
    asyncio.run(main())