#!/usr/bin/env python3
"""
🌏 REAL SEA LEAGUE FETCHER - ESPN API INTEGRATION 🌏

REVOLUTIONARY SOUTHEAST ASIAN FOOTBALL DATA SYSTEM
Fetches TODAY'S REAL games from ESPN API for all Southeast Asian leagues.

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨

🏆 SUPPORTED LEAGUES:
- 🇮🇩 Indonesian Super League (idn.1)
- 🇲🇾 Malaysian Super League (mys.1) 
- 🇹🇭 Thai League 1 (tha.1)
- 🇸🇬 Singapore Premier League (sgp.1)

Created: September 15, 2025
Based on: La Liga real data success methodology
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class RealSEALeagueFetcher:
    """
    🌏⚽ REAL SEA League Data Fetcher
    
    Fetches authentic Southeast Asian football data from ESPN API.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        
        # Real ESPN league IDs for Southeast Asian football
        self.sea_league_ids = {
            'AFF_CHAMPIONSHIP': 'aff.championship', # AFF Championship (main SEA tournament)
            'INDONESIAN_SUPER_LEAGUE': 'idn.1',     # Indonesian Super League
            'MALAYSIAN_SUPER_LEAGUE': 'mys.1',      # Malaysian Super League  
            'THAI_LEAGUE_1': 'tha.1',               # Thai League 1
            'SINGAPORE_PREMIER_LEAGUE': 'sgp.1'     # Singapore Premier League
        }
        
    async def fetch_todays_real_sea_league_games(self) -> List[Dict[str, Any]]:
        """
        🔥 Fetch TODAY'S REAL SEA League games from ESPN API
        
        Returns ONLY real data from ESPN API across all Southeast Asian leagues.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        try:
            logger.info("🌏 Fetching REAL SEA League games from ESPN API...")
            
            all_games = []
            
            async with aiohttp.ClientSession() as session:
                # Fetch from all SEA leagues in parallel
                tasks = []
                for league_name, league_id in self.sea_league_ids.items():
                    task = self._fetch_league_games(session, league_name, league_id)
                    tasks.append(task)
                
                # Wait for all leagues to complete
                league_results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # Combine results from all leagues
                for result in league_results:
                    if isinstance(result, list):
                        all_games.extend(result)
                    elif isinstance(result, Exception):
                        logger.error(f"🚨 League fetch error: {result}")
            
            logger.info(f"🌏 Found {len(all_games)} REAL SEA League games from ESPN API")
            return all_games
            
        except Exception as e:
            logger.error(f"💀 SEA League fetch error: {e}")
            return []

    async def _fetch_league_games(self, session: aiohttp.ClientSession, 
                                 league_name: str, league_id: str) -> List[Dict[str, Any]]:
        """
        Fetch games from a specific SEA league
        """
        try:
            url = f"{self.espn_api_base}/{league_id}/scoreboard"
            
            async with session.get(url, timeout=10) as response:
                if response.status != 200:
                    logger.warning(f"💀 {league_name} ESPN API failed with status {response.status}")
                    return []
                
                data = await response.json()
                events = data.get('events', [])
                
                if not events:
                    logger.info(f"🌏 No games today for {league_name}")
                    return []
                
                games = []
                for event in events:
                    try:
                        game = self._parse_espn_game(event, league_name, league_id)
                        if game:
                            games.append(game)
                    except Exception as e:
                        logger.error(f"💀 Error parsing {league_name} game: {e}")
                        continue
                
                logger.info(f"🌏 {league_name}: {len(games)} real games fetched")
                return games
                
        except Exception as e:
            logger.error(f"💀 {league_name} fetch error: {e}")
            return []

    def _parse_espn_game(self, event: Dict, league_name: str, league_id: str) -> Dict[str, Any]:
        """
        Parse ESPN game data into our format
        """
        try:
            # Get basic game info
            game_id = event.get('id', '')
            game_name = event.get('name', '')
            short_name = event.get('shortName', '')
            game_date = event.get('date', '')
            
            # Get competition data
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return None
            
            # Parse teams
            home_team_data = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_team_data = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            home_team = home_team_data.get('team', {}).get('displayName', 'Unknown')
            away_team = away_team_data.get('team', {}).get('displayName', 'Unknown')
            home_score = home_team_data.get('score', '0')
            away_score = away_team_data.get('score', '0')
            
            # Get status
            status = competition.get('status', {})
            status_type = status.get('type', {})
            game_status = status_type.get('name', 'UNKNOWN')
            is_completed = status_type.get('completed', False)
            
            # Get venue
            venue = competition.get('venue', {})
            venue_name = venue.get('fullName', 'Unknown Stadium')
            
            # Create our game object
            game = {
                'id': f"SEA_{league_id}_{game_id}",
                'sport': 'SEA_LEAGUE',
                'league': league_name,
                'home_team': home_team,
                'away_team': away_team,
                'home_score': int(home_score) if home_score.isdigit() else 0,
                'away_score': int(away_score) if away_score.isdigit() else 0,
                'status': game_status,
                'completed': is_completed,
                'matchup': f"{home_team} vs {away_team}",
                'venue': venue_name,
                'date': game_date,
                'time': self._format_time(game_date),
                'real_espn_data': True,  # Mark as real ESPN data
                'data_source': f'ESPN_SEA_LEAGUE_{league_id.upper()}',
                'country_code': self._get_country_code(league_id),
                'league_code': league_id,
                'original_event': event  # Keep original for debugging
            }
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN game: {e}")
            return None

    def _format_time(self, date_str: str) -> str:
        """Format ESPN date string to readable time"""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return 'TBD'

    def _get_country_code(self, league_id: str) -> str:
        """Get country code from league ID"""
        country_map = {
            'idn.1': '🇮🇩',
            'mys.1': '🇲🇾', 
            'tha.1': '🇹🇭',
            'sgp.1': '🇸🇬'
        }
        return country_map.get(league_id, '🌏')

    async def fetch_sea_league_standings(self) -> Dict[str, Any]:
        """
        🏆 Fetch REAL SEA League standings from ESPN API
        """
        try:
            standings = {}
            
            async with aiohttp.ClientSession() as session:
                for league_name, league_id in self.sea_league_ids.items():
                    try:
                        url = f"{self.espn_api_base}/{league_id}/standings"
                        
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                standings[league_name] = data
                                logger.info(f"🏆 {league_name} standings fetched")
                            else:
                                logger.warning(f"💀 {league_name} standings failed: {response.status}")
                                
                    except Exception as e:
                        logger.error(f"💀 {league_name} standings error: {e}")
                        continue
            
            return standings
            
        except Exception as e:
            logger.error(f"💀 SEA League standings error: {e}")
            return {}

async def test_real_sea_league_fetcher():
    """Test the real SEA League fetcher"""
    fetcher = RealSEALeagueFetcher()
    
    print("🌏 Testing REAL SEA League Data Fetcher...")
    games = await fetcher.fetch_todays_real_sea_league_games()
    
    print(f"\n🎯 Found {len(games)} REAL SEA League games:")
    for game in games:
        country = game.get('country_code', '🌏')
        league = game.get('league', 'Unknown')
        matchup = game.get('matchup', 'Unknown')
        status = game.get('status', 'Unknown')
        print(f"{country} {league}: {matchup} - {status}")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_sea_league_fetcher())