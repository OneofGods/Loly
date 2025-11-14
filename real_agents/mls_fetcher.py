#!/usr/bin/env python3
"""
🔥💀🔥 REAL MLS FETCHER - MAJOR LEAGUE SOCCER ESPN INTEGRATION 💀🔥💀

Real MLS (Major League Soccer) games fetcher with ESPN API integration
Provides authentic MLS match data with complete 8D analysis

🌟 Blessed by: Goddess of Syrup
⚡ Powered by: ESPN MLS API + Universal Prediction Engine
"""

import asyncio
import aiohttp
import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# Import the REAL MLS ALGORITHM! 🇺🇸⚽🔥 (TYPE 1 DATA-DRIVEN)
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mls_real_algorithm import RealMLSAlgorithm

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RealMLSFetcher:
    """
    🔥💀🔥 REAL MLS FETCHER - ESPN API INTEGRATION 💀🔥💀
    
    Fetches real MLS games from ESPN API with 8D analysis
    """
    
    def __init__(self):
        """Initialize Real MLS Fetcher"""
        self.espn_api_base = "https://site.api.espn.com/apis/site/v2/sports/soccer"
        self.mls_league_id = "usa.1"  # ESPN league identifier for MLS
        
        # Initialize REAL MLS TYPE 1 ALGORITHM 🇺🇸🔥
        self.mls_real = RealMLSAlgorithm()
        
        logger.info("🔥💀🔥 Real MLS Fetcher initialized with ESPN API integration 💀🔥💀")
    
    async def fetch_todays_real_mls_games(self) -> List[Dict[str, Any]]:
        """
        🎯 MAIN ENDPOINT: Fetch today's real MLS games with 8D analysis
        
        Returns:
            List of MLS games with complete Universal Prediction Engine analysis
        """
        try:
            logger.info("Fetching REAL MLS games from ESPN API")
            
            # Try multiple date strategies for better game coverage
            games = []
            
            # Strategy 1: Default scoreboard (current/upcoming games)
            default_games = await self._fetch_mls_games_by_strategy("default")
            if default_games:
                games.extend(default_games)
                logger.info(f"Found {len(default_games)} MLS games (default)")
            
            # Strategy 2: Date range search if needed
            if len(games) < 5:  # If we need more games
                date_games = await self._fetch_mls_games_by_strategy("date_range")
                if date_games:
                    # Avoid duplicates
                    existing_ids = {game.get('espn_id', '') for game in games}
                    new_games = [g for g in date_games if g.get('espn_id', '') not in existing_ids]
                    games.extend(new_games)
                    logger.info(f"Found {len(new_games)} additional MLS games (date range)")
            
            if not games:
                logger.warning("No MLS games found from ESPN API")
                return []
            
            # Apply Universal Prediction Engine for 8D analysis
            analyzed_games = []
            from real_agents.universal_prediction_engine import UniversalPredictionEngine
            prediction_engine = UniversalPredictionEngine()
            
            for game in games:
                try:
                    # 🔥💀🔥 APPLY REAL MLS TYPE 1 ALGORITHM! 💀🔥💀
                    real_result = await self.mls_real.apply_real_mls_algorithm(game)
                    
                    # Also run 8D analysis for comparison
                    analyzed_game = await prediction_engine.analyze_game(game, 'MLS')
                    
                    # Use Cultural Mastery algorithm results as primary
                    analyzed_game['prediction'] = real_result.get('prediction', analyzed_game.get('prediction', 'TBD'))
                    analyzed_game['confidence'] = real_result.get('confidence', analyzed_game.get('confidence', 50))
                    analyzed_game['algorithm'] = 'MLS_AMERICAN_SOCCER_CULTURAL_MASTERY'
                    analyzed_game['cultural_mastery_version'] = '2.0'
                    analyzed_game['legendary_status'] = True
                    analyzed_game['mls_cultural_data'] = real_result
                    
                    analyzed_games.append(analyzed_game)
                    
                    # Log analysis result
                    home = analyzed_game.get('home_team', 'Unknown')
                    away = analyzed_game.get('away_team', 'Unknown')
                    confidence = analyzed_game.get('confidence', 0)
                    prediction = analyzed_game.get('prediction', 'Unknown')
                    
                    logger.info(f"🇺🇸 MLS CULTURAL MASTERY: {away} @ {home} → {prediction} ({confidence}% confidence)")
                    
                except Exception as e:
                    logger.error(f"❌ MLS Type 1 analysis failed: {e}")
                    analyzed_games.append(game)  # Add without analysis
            
            logger.info(f"✅ Returning {len(analyzed_games)} MLS games with 8D analysis")
            return analyzed_games
            
        except Exception as e:
            logger.error(f"💀 Real MLS fetcher error: {e}")
            return []
    
    async def _fetch_mls_games_by_strategy(self, strategy: str) -> List[Dict[str, Any]]:
        """
        🔍 Fetch MLS games using specific strategy
        """
        try:
            if strategy == "default":
                return await self._fetch_mls_default_scoreboard()
            elif strategy == "date_range":
                return await self._fetch_mls_date_range()
            else:
                logger.warning(f"Unknown MLS fetch strategy: {strategy}")
                return []
                
        except Exception as e:
            logger.error(f"❌ MLS strategy {strategy} failed: {e}")
            return []
    
    async def _fetch_mls_default_scoreboard(self) -> List[Dict[str, Any]]:
        """
        📊 Fetch MLS games from default scoreboard
        """
        try:
            url = f"{self.espn_api_base}/{self.mls_league_id}/scoreboard"
            logger.info(f"Trying MLS endpoint: {self.mls_league_id} (default scoreboard)")
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        games = self._parse_espn_mls_response(data)
                        if games:
                            logger.info(f"Found {len(games)} MLS games at {self.mls_league_id} (default)")
                            return games
                    else:
                        logger.warning(f"⚠️ ESPN MLS API returned status {response.status}")
            
            return []
            
        except Exception as e:
            logger.error(f"❌ MLS default scoreboard error: {e}")
            return []
    
    async def _fetch_mls_date_range(self) -> List[Dict[str, Any]]:
        """
        📅 Fetch MLS games across date range
        """
        try:
            games = []
            
            # Search dates: -3 to +4 days (8 days total)
            for days_offset in range(-3, 5):
                target_date = datetime.now() + timedelta(days=days_offset)
                date_str = target_date.strftime("%Y%m%d")
                
                url = f"{self.espn_api_base}/{self.mls_league_id}/scoreboard?dates={date_str}"
                
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url, timeout=8) as response:
                            if response.status == 200:
                                data = await response.json()
                                date_games = self._parse_espn_mls_response(data)
                                if date_games:
                                    games.extend(date_games)
                                    logger.info(f"Found {len(date_games)} MLS games on {date_str}")
                except Exception as e:
                    logger.debug(f"Date {date_str} error: {e}")
                    continue
            
            return games
            
        except Exception as e:
            logger.error(f"❌ MLS date range error: {e}")
            return []
    
    def _parse_espn_mls_response(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        🔍 Parse ESPN MLS API response into standard game format
        """
        try:
            games = []
            events = data.get('events', [])
            
            for event in events:
                try:
                    # Extract competitors (teams)
                    competitions = event.get('competitions', [{}])
                    if not competitions:
                        continue
                    
                    competition = competitions[0]
                    competitors = competition.get('competitors', [])
                    
                    if len(competitors) != 2:
                        continue
                    
                    # Determine home/away teams
                    home_team = None
                    away_team = None
                    
                    for competitor in competitors:
                        team = competitor.get('team', {})
                        is_home = competitor.get('homeAway') == 'home'
                        
                        team_name = team.get('displayName', team.get('name', 'Unknown'))
                        
                        if is_home:
                            home_team = team_name
                        else:
                            away_team = team_name
                    
                    if not home_team or not away_team:
                        continue
                    
                    # Extract game details
                    game_id = event.get('id', 'unknown')
                    status = event.get('status', {})
                    venue = competition.get('venue', {})
                    
                    # Parse game time
                    game_date = event.get('date', '')
                    try:
                        game_datetime = datetime.fromisoformat(game_date.replace('Z', '+00:00'))
                        game_time = game_datetime.strftime("%I:%M %p")
                    except:
                        game_time = "TBD"
                    
                    # Create game object
                    game = {
                        'espn_id': game_id,
                        'home_team': home_team,
                        'away_team': away_team,
                        'league': 'MLS',
                        'venue': venue.get('fullName', 'TBD'),
                        'game_time': game_time,
                        'status': status.get('type', {}).get('description', 'Scheduled'),
                        'sport': 'SOCCER',
                        
                        # Metadata for 8D analysis
                        'data_source': 'ESPN_MLS_API',
                        'fetcher': 'RealMLSFetcher',
                        'last_updated': datetime.now().isoformat()
                    }
                    
                    games.append(game)
                    
                except Exception as e:
                    logger.debug(f"Error parsing MLS event: {e}")
                    continue
            
            return games
            
        except Exception as e:
            logger.error(f"❌ ESPN MLS response parsing error: {e}")
            return []
    
    async def get_mls_league_info(self) -> Dict[str, Any]:
        """
        📊 Get MLS league information
        """
        return {
            'league_name': 'Major League Soccer',
            'league_code': 'MLS',
            'espn_id': self.mls_league_id,
            'country': 'United States/Canada',
            'founded': 1993,
            'teams': 30,  # 2025 season
            'season': '2025',
            'data_source': 'ESPN_MLS_API'
        }


# Global function for easy import
async def fetch_todays_real_mls_games() -> List[Dict[str, Any]]:
    """
    🔥💀🔥 MAIN MLS ENDPOINT 💀🔥💀
    """
    fetcher = RealMLSFetcher()
    return await fetcher.fetch_todays_real_mls_games()


# Main execution for testing
async def main():
    """Test the Real MLS Fetcher"""
    print("🔥💀🔥 TESTING REAL MLS FETCHER 💀🔥💀")
    print("=" * 60)
    
    try:
        fetcher = RealMLSFetcher()
        
        # Test league info
        league_info = await fetcher.get_mls_league_info()
        print(f"🏆 League: {league_info['league_name']}")
        print(f"📊 Teams: {league_info['teams']}")
        print(f"🌍 Region: {league_info['country']}")
        print()
        
        # Test game fetching
        print("📅 Fetching MLS games...")
        games = await fetcher.fetch_todays_real_mls_games()
        
        print(f"✅ Found {len(games)} MLS games")
        print()
        
        # Show sample games
        for i, game in enumerate(games[:5]):
            home = game.get('home_team', 'Unknown')
            away = game.get('away_team', 'Unknown')
            venue = game.get('venue', 'Unknown')
            time = game.get('game_time', 'TBD')
            confidence = game.get('confidence', 'TBD')
            
            print(f"🎮 Game {i+1}: {away} @ {home}")
            print(f"   🏟️ Venue: {venue}")
            print(f"   ⏰ Time: {time}")
            print(f"   🎯 Confidence: {confidence}%")
            print()
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())