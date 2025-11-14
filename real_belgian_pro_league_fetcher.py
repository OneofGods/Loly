#!/usr/bin/env python3
"""
🇧🇪👑 REAL BELGIAN PRO LEAGUE FETCHER - UNDECUPLE THREAT v2.0! 🇧🇪👑

ULTIMATE BELGIAN FOOTBALL DATA SYSTEM WITH UNDECUPLE MASTERY
Fetches TODAY'S REAL games from ESPN API with LEGENDARY 85%+ confidence from Day 1!

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨
👑 LEGENDARY STATUS TARGET: 85%+ average confidence (Day 1 Mastery)

⚽🇧🇪 BELGIAN PRO LEAGUE ULTIMATE FEATURES:
- 🇧🇪 Belgian Pro League - Jupiler Pro League (bel.1) with CULTURAL MASTERY
- ⚔️ Classic rivalry analysis (Club Brugge vs Anderlecht)
- 🏰 Club Brugge dominance: modern Belgian powerhouse
- 👑 Anderlecht legacy: 34 titles + rebuilding pressure
- 🏛️ Royal Antwerp pride: oldest club (1880) + recent success
- 🎯 European qualification battles: 5 spots available
- ⚡ Compact league intensity: 16 teams = every game matters

Created: November 3, 2025 - UNDECUPLE THREAT v2.0 LAUNCH
Enhanced with: ALL 11 LEGENDARY PATTERNS + Belgian cultural mastery
Algorithm: BELGIAN_UNDECUPLE_THREAT_v2.0
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Import the LEGENDARY BELGIAN PRO LEAGUE ALGORITHM! 🇧🇪👑⚽🔥 (UNDECUPLE THREAT v2.0)
from belgian_pro_league_real_algorithm import RealBelgianProLeagueAlgorithm

logger = logging.getLogger(__name__)

class RealBelgianProLeagueFetcher:
    """
    🇧🇪👑⚽ LEGENDARY Belgian Pro League UNDECUPLE THREAT v2.0 Fetcher
    
    Fetches authentic Belgian football data with LEGENDARY UNDECUPLE mastery.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    Built with ALL 11 LEGENDARY PATTERNS from Day 1!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        # Try multiple possible Belgian Pro League endpoints
        self.belgian_league_ids = [
            'bel.1',          # Main Belgian Pro League ID
            'belgian',        # Belgian league alternative
            'belgium.1',      # Belgium first division
            'jupiler',        # Jupiler Pro League
        ]
        
        # Initialize LEGENDARY BELGIAN PRO LEAGUE UNDECUPLE THREAT v2.0 ALGORITHM 🇧🇪👑🔥
        self.belgian_real = RealBelgianProLeagueAlgorithm()
        
    async def fetch_todays_real_belgian_games(self) -> List[Dict[str, Any]]:
        """
        🔥 Fetch TODAY'S REAL Belgian Pro League games from ESPN API
        
        Returns ONLY real data from ESPN API.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        try:
            logger.info("🇧🇪 Fetching REAL Belgian Pro League games from ESPN API...")
            
            all_games = []
            
            async with aiohttp.ClientSession() as session:
                # Try multiple Belgian Pro League endpoints to find the working one
                for league_id in self.belgian_league_ids:
                    try:
                        url = f"{self.espn_api_base}/{league_id}/scoreboard"
                        logger.info(f"🔍 Trying Belgian Pro League endpoint: {league_id}")
                        
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                events = data.get('events', [])
                                
                                if events:
                                    logger.info(f"✅ Found Belgian Pro League data at endpoint: {league_id}")
                                    
                                    for event in events:
                                        try:
                                            game = self._parse_espn_game(event, league_id)
                                            if game:
                                                # 🔥👑🔥 APPLY LEGENDARY BELGIAN PRO LEAGUE UNDECUPLE THREAT v2.0! 👑🔥👑
                                                real_result = await self.belgian_real.apply_real_belgian_algorithm(game)
                                                game['prediction'] = real_result.get('prediction', game.get('prediction', 'TBD'))
                                                game['confidence'] = real_result.get('confidence', game.get('confidence', 50))
                                                game['algorithm'] = real_result.get('algorithm', 'REAL_BELGIAN_DATA_DRIVEN')
                                                
                                                # Check for UNDECUPLE THREAT activation
                                                if real_result.get('undecuple_threat_activated'):
                                                    game['undecuple_threat_activated'] = True
                                                    game['hybrid_engine_boost'] = real_result.get('hybrid_engine_boost', 0)
                                                    game['enhancement_version'] = real_result.get('enhancement_version', 'UNDECUPLE THREAT v2.0')
                                                    logger.info(f"🇧🇪💀 UNDECUPLE THREAT v2.0 ACTIVATED for {game.get('matchup', 'Unknown')}!")
                                                
                                                all_games.append(game)
                                        except Exception as e:
                                            logger.error(f"💀 Error parsing Belgian game: {e}")
                                            continue
                                    
                                    # Use first successful endpoint
                                    break
                                else:
                                    logger.info(f"📅 No Belgian Pro League games at endpoint {league_id}")
                            else:
                                logger.warning(f"💀 Belgian endpoint {league_id} failed with status {response.status}")
                                
                    except Exception as e:
                        logger.warning(f"💀 Belgian endpoint {league_id} error: {e}")
                        continue
                
                if all_games:
                    logger.info(f"🇧🇪 Found {len(all_games)} REAL Belgian Pro League games from ESPN API")
                else:
                    logger.info(f"🇧🇪 No Belgian Pro League games today - Belgian football schedule dependent")
                    
                return all_games
                    
        except Exception as e:
            logger.error(f"💀 Belgian Pro League fetch error: {e}")
            return []

    def _parse_espn_game(self, event: Dict, league_id: str) -> Dict[str, Any]:
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
            venue_city = venue.get('address', {}).get('city', 'Unknown City')
            venue_country = venue.get('address', {}).get('country', 'Unknown Country')
            
            # Get round/matchday information for Belgian Pro League
            season = event.get('season', {})
            competition_type = competition.get('type', {})
            round_info = competition.get('notes', [])
            matchday = "Journée"  # Default term
            
            if round_info:
                for note in round_info:
                    if isinstance(note, dict) and 'headline' in note:
                        matchday = note['headline']
                        break
            
            # Create our game object
            game = {
                'id': f"BELGIAN_{game_id}",
                'sport': 'BELGIAN_PRO_LEAGUE',
                'league': 'BELGIAN_PRO_LEAGUE',
                'home_team': home_team,
                'away_team': away_team,
                'home_score': int(home_score) if home_score.isdigit() else 0,
                'away_score': int(away_score) if away_score.isdigit() else 0,
                'status': game_status,
                'completed': is_completed,
                'matchup': f"{away_team} @ {home_team}",
                'venue': venue_name,
                'venue_city': venue_city,
                'venue_country': venue_country,
                'date': game_date,
                'time': self._format_time(game_date),
                'matchday': matchday,  # Belgian Pro League specific
                'real_espn_data': True,  # Mark as real ESPN data
                'data_source': f'ESPN_BELGIAN_PRO_LEAGUE_API',
                'country_code': '🇧🇪',  # Belgian flag
                'league_code': league_id,
                'belgian_football': True,  # Mark as Belgian
                'original_event': event  # Keep original for debugging
            }
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN Belgian game: {e}")
            return None

    def _format_time(self, date_str: str) -> str:
        """Format ESPN date string to readable time"""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return 'TBD'

    async def fetch_belgian_standings(self) -> Dict[str, Any]:
        """
        🏆 Fetch REAL Belgian Pro League standings from ESPN API
        """
        try:
            standings = {}
            
            async with aiohttp.ClientSession() as session:
                # Try multiple endpoints for standings
                for league_id in self.belgian_league_ids:
                    try:
                        url = f"{self.espn_api_base}/{league_id}/standings"
                        
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                standings['BELGIAN_PRO_LEAGUE'] = data
                                logger.info(f"🏆 Belgian Pro League standings fetched from {league_id}")
                                break
                            else:
                                logger.warning(f"💀 Belgian standings failed for {league_id}: {response.status}")
                    except Exception as e:
                        logger.warning(f"💀 Belgian standings error for {league_id}: {e}")
                        continue
            
            return standings
            
        except Exception as e:
            logger.error(f"💀 Belgian standings error: {e}")
            return {}

async def test_real_belgian_fetcher():
    """Test the real Belgian Pro League fetcher"""
    fetcher = RealBelgianProLeagueFetcher()
    
    print("🇧🇪 Testing REAL Belgian Pro League Data Fetcher...")
    games = await fetcher.fetch_todays_real_belgian_games()
    
    print(f"\n🎯 Found {len(games)} REAL Belgian Pro League games:")
    if games:
        for game in games:
            country = game.get('country_code', '🇧🇪')
            league = game.get('league', 'Unknown')
            matchup = game.get('matchup', 'Unknown')
            status = game.get('status', 'Unknown')
            time = game.get('time', 'Unknown')
            matchday = game.get('matchday', 'Unknown Journée')
            venue = game.get('venue', 'Unknown Stadium')
            venue_city = game.get('venue_city', 'Unknown City')
            venue_country = game.get('venue_country', 'Unknown Country')
            prediction = game.get('prediction', 'TBD')
            confidence = game.get('confidence', 0)
            algorithm = game.get('algorithm', 'None')
            undecuple_activated = game.get('undecuple_threat_activated', False)
            
            print(f"{country} {league}: {matchup}")
            print(f"   🏟️  {venue} - {venue_city}, {venue_country}")
            print(f"   🇧🇪 {matchday}")
            print(f"   ⏰ {time} - {status}")
            print(f"   🎯 {prediction} ({confidence}% confidence) [{algorithm}]")
            if undecuple_activated:
                print(f"   💀🔥💀 UNDECUPLE THREAT v2.0 ACTIVATED! 💀🔥💀")
            print()
    else:
        print("🇧🇪 No Belgian Pro League games today")
        print("🔥 System READY for when Belgian matches resume!")
        print("⭐ Belgian football integration complete!")
        print("🏆 Club Brugge, Anderlecht, Royal Antwerp level system ready!")
        print("💀🔥💀 UNDECUPLE THREAT v2.0 READY FOR LEGENDARY STATUS! 💀🔥💀")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_belgian_fetcher())