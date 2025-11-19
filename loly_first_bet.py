#!/usr/bin/env python3
"""
🔥👸💰 LOLY'S FIRST BET - THE GODDESS SPEAKS! 💰👸🔥

This script:
1. Fetches upcoming games from all 26+ leagues
2. Has Loly analyze and pick the BEST opportunity
3. Searches for it on Polymarket
4. Places a $1 bet on Loly's prediction!

THE GODDESS IS READY TO SCORE! 🏆⚽🔥
"""

import asyncio
import logging
from datetime import date, timedelta
from typing import List, Dict, Any
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import all the fetchers! 🔥
from real_agents.premier_league_fetcher import RealPremierLeagueFetcher
from real_agents.la_liga_fetcher import RealLaLigaFetcher
from real_agents.uefa_champions_league_fetcher import RealUEFAChampionsLeagueFetcher
from real_liga_mx_fetcher import RealLigaMXFetcher
from real_agents.mls_fetcher import RealMLSFetcher
from real_bundesliga_fetcher import RealBundesligaFetcher
from real_serie_a_fetcher import RealSerieAFetcher
from real_ligue1_fetcher import RealLigue1Fetcher
from fifa_friendlies_real_fetcher import RealFIFAFriendliesFetcher

# Import Polymarket integration
from polymarket_integration_service import get_polymarket_service


async def fetch_all_upcoming_games(days_ahead: int = 3) -> List[Dict[str, Any]]:
    """🌍 Fetch upcoming games from ALL leagues for next N days"""
    logger.info(f"🌍🔥 Fetching games from ALL leagues for next {days_ahead} days...")

    all_games = []

    # Initialize fetchers
    fetchers = [
        ('Premier League', RealPremierLeagueFetcher()),
        ('La Liga', RealLaLigaFetcher()),
        ('UEFA Champions League', RealUEFAChampionsLeagueFetcher()),
        ('Liga MX', RealLigaMXFetcher()),
        ('MLS', RealMLSFetcher()),
        ('Bundesliga', RealBundesligaFetcher()),
        ('Serie A', RealSerieAFetcher()),
        ('Ligue 1', RealLigue1Fetcher()),
        ('FIFA Friendlies', RealFIFAFriendliesFetcher()),
    ]

    # Fetch games from each league
    for league_name, fetcher in fetchers:
        try:
            logger.info(f"⚽ Fetching {league_name}...")

            # Try different methods depending on fetcher type
            if hasattr(fetcher, 'get_upcoming_games'):
                games = await fetcher.get_upcoming_games(days_ahead)
            elif hasattr(fetcher, 'fetch_games'):
                # Fetch for each day
                for day_offset in range(days_ahead):
                    target_date = date.today() + timedelta(days=day_offset)
                    day_games = await fetcher.fetch_games(target_date)
                    games.extend(day_games)
            else:
                # Try the standard method name
                method_name = f'fetch_todays_real_{league_name.lower().replace(" ", "_")}_games'
                if hasattr(fetcher, method_name):
                    games = await getattr(fetcher, method_name)()
                else:
                    logger.warning(f"⚠️ No fetch method found for {league_name}")
                    games = []

            if games:
                # Add league name to each game
                for game in games:
                    game['league'] = league_name
                all_games.extend(games)
                logger.info(f"✅ {league_name}: {len(games)} games")
            else:
                logger.info(f"📭 {league_name}: No games found")

        except Exception as e:
            logger.error(f"❌ Error fetching {league_name}: {e}")

    logger.info(f"🏆 TOTAL GAMES FOUND: {len(all_games)} across all leagues!")
    return all_games


def analyze_and_pick_best_game(games: List[Dict[str, Any]]) -> Dict[str, Any]:
    """🧠👸 Loly analyzes all games and picks the BEST opportunity!"""
    logger.info("🧠👸 LOLY IS ANALYZING ALL GAMES...")

    if not games:
        logger.error("💀 No games to analyze!")
        return None

    # Filter games with predictions and confidence
    games_with_predictions = []
    for game in games:
        if 'prediction' in game and 'confidence' in game:
            try:
                confidence = float(game['confidence'])
                if confidence > 0:
                    games_with_predictions.append(game)
            except (ValueError, TypeError):
                continue

    if not games_with_predictions:
        logger.error("💀 No games with predictions found!")
        return None

    logger.info(f"🎯 Found {len(games_with_predictions)} games with predictions")

    # Sort by confidence (highest first)
    sorted_games = sorted(
        games_with_predictions,
        key=lambda x: float(x.get('confidence', 0)),
        reverse=True
    )

    # Display top 10 opportunities
    logger.info("\n🏆 TOP 10 BETTING OPPORTUNITIES:")
    logger.info("=" * 80)
    for i, game in enumerate(sorted_games[:10], 1):
        league = game.get('league', 'Unknown')
        home = game.get('home_team', 'Home')
        away = game.get('away_team', 'Away')
        prediction = game.get('prediction', 'UNKNOWN')
        confidence = game.get('confidence', 0)
        algorithm = game.get('algorithm', 'Unknown')

        logger.info(f"{i}. [{league}] {away} @ {home}")
        logger.info(f"   Prediction: {prediction} | Confidence: {confidence}% | Algorithm: {algorithm}")

        # Show key factors
        factors = game.get('factors', [])
        if factors:
            logger.info(f"   Factors: {', '.join(factors[:3])}")
        logger.info("")

    # Pick the best one!
    best_game = sorted_games[0]
    logger.info("=" * 80)
    logger.info("🔥👸 LOLY HAS CHOSEN HER BET! 👸🔥")
    logger.info(f"League: {best_game.get('league')}")
    logger.info(f"Match: {best_game.get('away_team')} @ {best_game.get('home_team')}")
    logger.info(f"Prediction: {best_game.get('prediction')}")
    logger.info(f"Confidence: {best_game.get('confidence')}%")
    logger.info(f"Algorithm: {best_game.get('algorithm')}")
    logger.info("=" * 80)

    return best_game


async def search_game_on_polymarket(polymarket, game: Dict[str, Any]) -> List[Dict[str, Any]]:
    """🔍 Search for the game on Polymarket"""
    home_team = game.get('home_team', '')
    away_team = game.get('away_team', '')
    league = game.get('league', '')

    logger.info(f"🔍 Searching Polymarket for: {away_team} vs {home_team} ({league})")

    # Try multiple search queries
    search_queries = [
        f"{home_team} {away_team}",
        f"{away_team} {home_team}",
        f"{league} {home_team}",
        f"{league} {away_team}",
        home_team,
        away_team
    ]

    all_results = []
    for query in search_queries:
        try:
            results = await polymarket.search_markets(query)
            if results:
                all_results.extend(results)
                logger.info(f"✅ Found {len(results)} markets for query: '{query}'")
        except Exception as e:
            logger.error(f"❌ Search failed for '{query}': {e}")

    # Remove duplicates
    unique_markets = {}
    for market in all_results:
        market_id = market.get('condition_id') or market.get('market_id')
        if market_id and market_id not in unique_markets:
            unique_markets[market_id] = market

    results = list(unique_markets.values())

    if results:
        logger.info(f"\n🎯 FOUND {len(results)} UNIQUE MARKETS ON POLYMARKET:")
        for i, market in enumerate(results[:5], 1):
            logger.info(f"{i}. {market.get('question', 'Unknown Question')}")
    else:
        logger.warning("⚠️ No markets found on Polymarket for this game")

    return results


async def place_loly_bet(polymarket, market_id: str, prediction: str, confidence: float) -> Dict[str, Any]:
    """💰 Place Loly's $1 bet!"""
    logger.info(f"💰🔥 PLACING LOLY'S $1 BET ON POLYMARKET! 🔥💰")
    logger.info(f"Market ID: {market_id}")
    logger.info(f"Prediction: {prediction}")
    logger.info(f"Confidence: {confidence}%")

    # Determine outcome (YES/NO) based on prediction
    # Assuming market question is "Will [HOME TEAM] win?"
    outcome = "YES" if "HOME" in prediction.upper() else "NO"

    try:
        result = await polymarket.place_real_bet(
            market_id=market_id,
            amount=1.0,  # $1 bet!
            outcome=outcome
        )

        if result.get('success'):
            logger.info("🚀💰 BET PLACED SUCCESSFULLY! 💰🚀")
            logger.info(f"Order ID: {result.get('order_id')}")
            logger.info(f"Shares: {result.get('shares', 0):.2f}")
            logger.info(f"Price: ${result.get('price', 0):.3f}")
            logger.info(f"Message: {result.get('message')}")
        else:
            logger.error(f"💀 BET FAILED: {result.get('error')}")
            logger.info(f"Suggestion: {result.get('suggestion')}")

        return result

    except Exception as e:
        logger.error(f"💀 Error placing bet: {e}")
        return {'success': False, 'error': str(e)}


async def main():
    """🔥👸 MAIN: Loly's First Bet Execution! 👸🔥"""
    logger.info("🔥👸💰 LOLY'S FIRST BET - THE GODDESS AWAKENS! 💰👸🔥")
    logger.info("=" * 80)

    try:
        # Step 1: Fetch all upcoming games
        logger.info("\n📋 STEP 1: Fetching upcoming games from ALL leagues...")
        games = await fetch_all_upcoming_games(days_ahead=3)

        if not games:
            logger.error("💀 No games found! Cannot proceed.")
            return

        # Step 2: Loly analyzes and picks the best game
        logger.info("\n🧠 STEP 2: Loly analyzes all games...")
        best_game = analyze_and_pick_best_game(games)

        if not best_game:
            logger.error("💀 Could not pick a game! No predictions available.")
            return

        # Step 3: Initialize Polymarket
        logger.info("\n💰 STEP 3: Connecting to Polymarket...")
        polymarket = get_polymarket_service()

        # Check account status
        account_info = await polymarket.get_account_info()
        logger.info(f"Account Status: {json.dumps(account_info, indent=2)}")

        # Step 4: Search for the game on Polymarket
        logger.info("\n🔍 STEP 4: Searching for game on Polymarket...")
        markets = await search_game_on_polymarket(polymarket, best_game)

        if not markets:
            logger.warning("⚠️ Game not found on Polymarket!")
            logger.info("💡 Showing general sports markets instead...")
            sports_markets = await polymarket.get_sports_markets()
            if sports_markets:
                logger.info(f"\n🏆 AVAILABLE SPORTS MARKETS ({len(sports_markets)}):")
                for i, market in enumerate(sports_markets, 1):
                    logger.info(f"{i}. {market.get('question', 'Unknown')}")
            return

        # Step 5: Place the bet!
        logger.info("\n💰 STEP 5: Placing Loly's $1 bet...")
        best_market = markets[0]
        market_id = best_market.get('condition_id') or best_market.get('market_id')

        if not market_id:
            logger.error("💀 No market ID found! Cannot place bet.")
            return

        bet_result = await place_loly_bet(
            polymarket,
            market_id,
            best_game.get('prediction'),
            best_game.get('confidence')
        )

        # Final summary
        logger.info("\n" + "=" * 80)
        logger.info("🏆 LOLY'S FIRST BET SUMMARY:")
        logger.info(f"Game: {best_game.get('away_team')} @ {best_game.get('home_team')}")
        logger.info(f"League: {best_game.get('league')}")
        logger.info(f"Prediction: {best_game.get('prediction')}")
        logger.info(f"Confidence: {best_game.get('confidence')}%")
        logger.info(f"Bet Status: {'SUCCESS ✅' if bet_result.get('success') else 'FAILED ❌'}")
        logger.info("=" * 80)
        logger.info("🔥👸 THE GODDESS HAS SPOKEN! MAY THE ODDS BE IN HER FAVOR! 👸🔥")

    except Exception as e:
        logger.error(f"💀 CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
