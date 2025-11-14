#!/usr/bin/env python3
"""
🏆 REAL UEFA EUROPA LEAGUE FETCHER - ESPN API INTEGRATION 🏆

REVOLUTIONARY EUROPEAN FOOTBALL DATA SYSTEM
Fetches TODAY'S REAL games from ESPN API for UEFA Europa League.

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨

⚽🏆 UEFA EUROPA LEAGUE - EUROPEAN FOOTBALL EXCELLENCE:
- 🏆 UEFA Europa League - European Second Division (uefa.europa)
- ⭐ Real Betis, Brighton, Fenerbahce, Feyenoord level elite
- 🔥 The second most prestigious club competition in Europe

Created: October 21, 2025
Based on: UEFA Champions League and EPL elite success methodology
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Import the Universal Prediction Engine for 8D analysis
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from universal_prediction_engine import UniversalPredictionEngine

# Import the REAL UEFA EUROPA LEAGUE ALGORITHM! 🏆⚡🔥 (TYPE 1 DATA-DRIVEN)
from uefa_europa_league_real_algorithm import RealUEFAEuropaLeagueAlgorithm

# Simple logging without broken imports
logger = logging.getLogger(__name__)

class RealUEFAEuropaLeagueFetcher:
    """
    🏆⚽ REAL UEFA Europa League Data Fetcher
    
    Fetches authentic European football data from ESPN API.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        # Try multiple possible UEFA Europa League endpoints
        self.uefa_europa_league_ids = [
            'uefa.europa',      # Main UEFA Europa League ID
            'europa-league',    # Europa League alternative
            'uefa-europa',      # UEFA Europa alternative
            'europa',           # Europa abbreviation
            'uefa.2',           # UEFA second tier
        ]
        
        # Initialize REAL UEFA EUROPA LEAGUE TYPE 1 ALGORITHM 🏆⚡🔥
        self.europa_league_real = RealUEFAEuropaLeagueAlgorithm()
        
        # Initialize Universal Prediction Engine for 8D analysis
        self.prediction_engine = UniversalPredictionEngine()
        
    async def fetch_todays_real_uefa_europa_league_games(self) -> List[Dict[str, Any]]:
        """
        🏆 FETCH TODAY'S REAL UEFA EUROPA LEAGUE GAMES FROM ESPN API 🏆
        
        Returns ONLY real data from ESPN API.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        # Simple logging without broken imports
        logger.info("Fetching REAL UEFA Europa League games from ESPN API")
        
        all_games = []
        
        # Check multiple dates for complete gameweek
        from datetime import datetime, timedelta
        
        async with aiohttp.ClientSession() as session:
            # Try multiple UEFA Europa League endpoints
            for league_id in self.uefa_europa_league_ids:
                try:
                    # FIRST: Try without date parameter (gets current/upcoming games)
                    url = f"{self.espn_api_base}/{league_id}/scoreboard"
                    logger.info(f"Trying UEFA Europa League endpoint: {league_id} (default scoreboard)")
                    
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()
                            events = data.get('events', [])
                            
                            if events:
                                logger.info(f"Found {len(events)} UEFA Europa League games at {league_id} (default)")
                                
                                for event in events:
                                    try:
                                        game = await self._parse_espn_game(event, league_id)
                                        if game:
                                            # Avoid duplicates by checking matchup
                                            matchup = f"{game.get('away_team', '')} @ {game.get('home_team', '')}"
                                            existing = any(f"{g.get('away_team', '')} @ {g.get('home_team', '')}" == matchup for g in all_games)
                                            if not existing:
                                                all_games.append(game)
                                    except Exception as e:
                                        logger.warning(f"Error parsing UEFA Europa League game: {e}")
                                        continue
                                        
                                # If we found games, use this endpoint
                                if all_games:
                                    logger.info(f"Found UEFA Europa League data at endpoint: {league_id}")
                                    break
                            else:
                                logger.info(f"No UEFA Europa League games at {league_id} (default)")
                        else:
                            logger.warning(f"UEFA Europa League endpoint {league_id} failed with status {response.status}")
                    
                    # FALLBACK: If no games found, try with specific dates
                    if not all_games:
                        logger.info(f"Trying {league_id} with specific dates...")
                        # Check current date, previous 4 days, and next 3 days for complete gameweek
                        for days_offset in range(-4, 4):  # -4 to +3 (8 days total)
                            date_to_check = datetime.now() + timedelta(days=days_offset)
                            date_str = date_to_check.strftime('%Y%m%d')
                            
                            url = f"{self.espn_api_base}/{league_id}/scoreboard?dates={date_str}"
                            logger.info(f"Trying UEFA Europa League endpoint: {league_id} for date {date_str}")
                            
                            async with session.get(url, timeout=10) as response:
                                if response.status == 200:
                                    data = await response.json()
                                    events = data.get('events', [])
                                    
                                    if events:
                                        logger.info(f"Found {len(events)} UEFA Europa League games at {league_id} on {date_str}")
                                        
                                        for event in events:
                                            try:
                                                game = await self._parse_espn_game(event, league_id)
                                                if game:
                                                    # Avoid duplicates by checking matchup
                                                    matchup = f"{game.get('away_team', '')} @ {game.get('home_team', '')}"
                                                    existing = any(f"{g.get('away_team', '')} @ {g.get('home_team', '')}" == matchup for g in all_games)
                                                    if not existing:
                                                        all_games.append(game)
                                            except Exception as e:
                                                logger.warning(f"Error parsing UEFA Europa League game: {e}")
                                                continue
                                        
                                        # If we found games, break out of date loop
                                        if all_games:
                                            break
                                    else:
                                        logger.info(f"No UEFA Europa League games at {league_id} on {date_str}")
                                else:
                                    logger.warning(f"UEFA Europa League endpoint {league_id} failed with status {response.status}")
                                    
                    # If we found games, break out of league_id loop
                    if all_games:
                        logger.info(f"Found UEFA Europa League data at endpoint: {league_id}")
                        break
                                
                except Exception as e:
                    logger.warning(f"UEFA Europa League endpoint {league_id} error: {e}")
                    continue
            
            if all_games:
                logger.info(f"Found {len(all_games)} REAL UEFA Europa League games from ESPN API")
                return all_games
            else:
                logger.info("No UEFA Europa League games today - check schedule")
                return []

    async def _parse_espn_game(self, event: Dict, league_id: str) -> Dict[str, Any]:
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
            
            # Get round/week information for UEFA Europa League
            season = event.get('season', {})
            competition_type = competition.get('type', {})
            round_info = competition.get('notes', [])
            week = "Matchday"  # Default English term
            
            if round_info:
                for note in round_info:
                    if isinstance(note, dict) and 'headline' in note:
                        week = note['headline']
                        break
            
            # Create our game object
            game = {
                'id': f"UEFA_EUROPA_{game_id}",
                'sport': 'UEFA_EUROPA_LEAGUE',
                'league': 'UEFA_EUROPA_LEAGUE',
                'home_team': home_team,
                'away_team': away_team,
                'home_score': int(home_score) if home_score.isdigit() else 0,
                'away_score': int(away_score) if away_score.isdigit() else 0,
                'status': game_status,
                'completed': is_completed,
                'matchup': f"{away_team} @ {home_team}",
                'venue': venue_name,
                'date': game_date,
                'time': self._format_time(game_date),
                'week': week,  # UEFA Europa League specific
                'real_espn_data': True,  # Mark as real ESPN data
                'data_source': 'ESPN_UEFA_EUROPA_LEAGUE_API',
                'country_code': '🏆',  # UEFA trophy
                'league_code': league_id,
                'european_football': True,  # Mark as European
                'original_event': event  # Keep original for debugging
            }
            
            # 🔥💀🔥 REAL UEFA EUROPA LEAGUE TYPE 1 ALGORITHM! 💀🔥💀
            try:
                # Apply REAL UEFA EUROPA LEAGUE TYPE 1 ALGORITHM first
                real_result = await self.europa_league_real.apply_real_uefa_europa_league_algorithm(game)
                
                # Also run 8D analysis for comparison
                analyzed_game = await self.prediction_engine.analyze_game(game, 'UEFA_EUROPA_LEAGUE')
                
                # Use LEGENDARY Cultural Mastery algorithm results as primary
                game.update(analyzed_game)
                game['prediction'] = real_result.get('prediction', game.get('prediction', 'TBD'))
                game['confidence'] = real_result.get('confidence', game.get('confidence', 50))
                game['algorithm'] = 'UEFA_EUROPA_LEAGUE_LEGENDARY_EUROPEAN_CULTURAL_MASTERY'
                game['cultural_mastery_version'] = '2.0'
                game['legendary_status'] = True
                game['europa_league_cultural_data'] = real_result
                
                logger.info(f"🏆⚡ UEFA EUROPA LEAGUE TYPE 1: {game['matchup']} → {game.get('prediction', 'TBD')} ({game.get('confidence', 50):.1f}% confidence)")
                
            except Exception as e:
                logger.error(f"💀 UEFA Europa League Type 1 analysis failed for {game['matchup']}: {e}")
                # Fallback to basic prediction
                game['pick'] = f"🏠 {home_team}"  # Default home advantage
                game['prediction'] = f"🏠 {home_team}"
                game['confidence'] = 65.0
                game['algorithm'] = 'Fallback - Simple Home Advantage'
                game['enhancement_version'] = 'Fallback - Simple Home Advantage'
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN UEFA Europa League game: {e}")
            return None

    def _analyze_enhanced_prediction(self, event: Dict) -> Dict[str, Any]:
        """
        🔥💀🔥 ENHANCED UEFA EUROPA LEAGUE PREDICTION ANALYSIS! 💀🔥💀
        
        Implements Phase 1 enhancements:
        1. Recent form analysis (40% weight)
        2. Home advantage detection (15% boost) 
        3. Season record integration (25% weight)
        4. Enhanced confidence scoring
        """
        try:
            competition = event['competitions'][0]
            competitors = competition['competitors']
            
            if len(competitors) != 2:
                return {'prediction': 'TBD', 'confidence': 50.0, 'analysis': 'Insufficient team data'}
            
            home_competitor = next((c for c in competitors if c['homeAway'] == 'home'), competitors[0])
            away_competitor = next((c for c in competitors if c['homeAway'] == 'away'), competitors[1])
            
            home_team = home_competitor['team']['displayName']
            away_team = away_competitor['team']['displayName']
            
            # 🎯 ENHANCEMENT 1: RECENT FORM ANALYSIS (40% weight)
            home_form_strength = self._calculate_form_strength(home_competitor.get('form', 'DDDDD'))
            away_form_strength = self._calculate_form_strength(away_competitor.get('form', 'DDDDD'))
            form_advantage = (home_form_strength - away_form_strength) * 0.4
            
            # 🏠 ENHANCEMENT 2: HOME ADVANTAGE (15% boost)
            home_advantage = 0.15  # 15% boost for home team
            
            # 📊 ENHANCEMENT 3: SEASON RECORDS (25% weight)
            home_record_strength = self._calculate_record_strength(home_competitor.get('records', []))
            away_record_strength = self._calculate_record_strength(away_competitor.get('records', []))
            record_advantage = (home_record_strength - away_record_strength) * 0.25
            
            # 🔥💀🔥 COMBINE ALL FACTORS FOR ENHANCED PREDICTION! 💀🔥💀
            home_total_advantage = form_advantage + home_advantage + record_advantage
            away_total_advantage = -form_advantage + 0.0 + (-record_advantage)  # Away gets no home boost
            
            # 📈 ENHANCED CONFIDENCE CALCULATION
            advantage_gap = abs(home_total_advantage - away_total_advantage)
            base_confidence = 50.0
            enhanced_confidence = min(95.0, base_confidence + (advantage_gap * 100))
            
            # 🎯 MAKE ENHANCED PREDICTION
            if home_total_advantage > away_total_advantage + 0.1:  # Need 10% edge
                prediction = f"🏠 {home_team}"
                pick = home_team
            elif away_total_advantage > home_total_advantage + 0.1:
                prediction = f"✈️ {away_team}"  
                pick = away_team
            else:
                prediction = "🤝 DRAW"
                pick = "DRAW"
            
            # 📊 ENHANCED ANALYSIS BREAKDOWN
            analysis = {
                'home_form': f"{home_competitor.get('form', 'N/A')} ({home_form_strength:.2f})",
                'away_form': f"{away_competitor.get('form', 'N/A')} ({away_form_strength:.2f})",
                'home_advantage': f"+{home_advantage:.1%}",
                'form_edge': f"{form_advantage:+.2f}",
                'record_edge': f"{record_advantage:+.2f}",
                'total_home_score': f"{home_total_advantage:.2f}",
                'total_away_score': f"{away_total_advantage:.2f}",
                'enhancement_version': 'Phase 1 - UEFA Europa League Enhanced'
            }
            
            logger.info(f"🔥💀🔥 ENHANCED PREDICTION: {away_team} @ {home_team} → {prediction} ({enhanced_confidence:.1f}% confidence)")
            
            return {
                'prediction': prediction,
                'pick': pick,
                'confidence': enhanced_confidence,
                'analysis': analysis,
                'enhancement_applied': True
            }
            
        except Exception as e:
            logger.error(f"💀 Enhanced prediction analysis error: {e}")
            return {'prediction': 'TBD', 'confidence': 50.0, 'analysis': 'Analysis failed'}

    def _calculate_form_strength(self, form_string: str) -> float:
        """
        Calculate team strength from recent form (e.g., 'WWDDD' = 60% strength)
        W = 3 points, D = 1 point, L = 0 points. Max = 15 points in 5 games.
        """
        if not form_string or len(form_string) == 0:
            return 0.5  # Neutral if no form data
        
        points = 0
        games = min(len(form_string), 5)  # Max 5 games
        
        for result in form_string[-games:]:  # Take last N games
            if result.upper() == 'W':
                points += 3
            elif result.upper() == 'D':
                points += 1
            # L = 0 points
        
        max_points = games * 3
        return points / max_points if max_points > 0 else 0.5

    def _calculate_record_strength(self, records: List[Dict]) -> float:
        """
        Calculate team strength from season record (e.g., '6-4-1' = 65% strength)
        """
        for record in records:
            if record.get('name') == 'All Splits' or record.get('type') == 'total':
                summary = record.get('summary', '')
                try:
                    # Parse "6-4-1" format (wins-draws-losses)
                    parts = summary.split('-')
                    if len(parts) == 3:
                        wins, draws, losses = map(int, parts)
                        total_games = wins + draws + losses
                        if total_games > 0:
                            points = wins * 3 + draws * 1
                            max_points = total_games * 3
                            return points / max_points
                except ValueError:
                    pass
        
        return 0.5  # Neutral if no record data

    def _format_time(self, date_str: str) -> str:
        """Format ESPN date string to readable time"""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return 'TBD'

    async def fetch_europa_league_standings(self) -> Dict[str, Any]:
        """
        🏆 Fetch REAL UEFA Europa League standings from ESPN API
        """
        try:
            standings = {}
            
            async with aiohttp.ClientSession() as session:
                # Try multiple endpoints for standings
                for league_id in self.uefa_europa_league_ids:
                    try:
                        url = f"{self.espn_api_base}/{league_id}/standings"
                        
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                standings['UEFA_EUROPA_LEAGUE'] = data
                                logger.info(f"🏆 UEFA Europa League standings fetched from {league_id}")
                                break
                            else:
                                logger.warning(f"💀 UEFA Europa League standings failed for {league_id}: {response.status}")
                    except Exception as e:
                        logger.warning(f"💀 UEFA Europa League standings error for {league_id}: {e}")
                        continue
            
            return standings
            
        except Exception as e:
            logger.error(f"💀 UEFA Europa League standings error: {e}")
            return {}

    async def fetch_europa_league_season_games(self, season_year: int = 2025) -> List[Dict[str, Any]]:
        """
        🏆 Fetch UEFA Europa League SEASON games from ESPN API
        
        Fetches historical/season games for accuracy analysis.
        Returns ONLY real season data from ESPN API.
        """
        try:
            logger.info(f"🏆 Fetching UEFA Europa League SEASON {season_year} games from ESPN API...")
            
            all_season_games = []
            
            async with aiohttp.ClientSession() as session:
                # Try multiple UEFA Europa League endpoints for season data
                for league_id in self.uefa_europa_league_ids:
                    try:
                        # Try season scoreboard endpoint (ESPN often has historical data)
                        season_url = f"{self.espn_api_base}/{league_id}/scoreboard?season={season_year}"
                        logger.info(f"🔍 Trying UEFA Europa League season endpoint: {league_id} for {season_year}")
                        
                        async with session.get(season_url, timeout=15) as response:
                            if response.status == 200:
                                data = await response.json()
                                events = data.get('events', [])
                                
                                if events:
                                    logger.info(f"✅ Found UEFA Europa League season data at endpoint: {league_id}")
                                    
                                    for event in events:
                                        try:
                                            game = await self._parse_espn_game(event, league_id)
                                            if game:
                                                # Mark as season game for tracking
                                                game['season_game'] = True
                                                game['season_year'] = season_year
                                                all_season_games.append(game)
                                        except Exception as e:
                                            logger.error(f"💀 Error parsing UEFA Europa League season game: {e}")
                                            continue
                                    
                                    # Use first successful endpoint
                                    break
                                else:
                                    logger.info(f"📅 No UEFA Europa League season games at endpoint {league_id}")
                            else:
                                logger.warning(f"💀 UEFA Europa League season endpoint {league_id} failed with status {response.status}")
                                
                    except Exception as e:
                        logger.warning(f"💀 UEFA Europa League season endpoint {league_id} error: {e}")
                        continue
                
                # If season-specific URL doesn't work, try fetching recent games by date range
                if not all_season_games:
                    logger.info(f"🔄 Trying UEFA Europa League recent games approach for season data...")
                    
                    # Try fetching recent/historical games (UEFA Europa League season runs roughly Aug-May)
                    for league_id in self.uefa_europa_league_ids:
                        try:
                            # ESPN API sometimes accepts date parameters
                            recent_url = f"{self.espn_api_base}/{league_id}/scoreboard?limit=50"
                            logger.info(f"🔍 Trying UEFA Europa League recent games: {league_id}")
                            
                            async with session.get(recent_url, timeout=15) as response:
                                if response.status == 200:
                                    data = await response.json()
                                    events = data.get('events', [])
                                    
                                    if events:
                                        logger.info(f"✅ Found UEFA Europa League recent games at endpoint: {league_id}")
                                        
                                        for event in events:
                                            try:
                                                game = await self._parse_espn_game(event, league_id)
                                                if game:
                                                    game['season_game'] = True
                                                    game['season_year'] = season_year
                                                    all_season_games.append(game)
                                            except Exception as e:
                                                logger.error(f"💀 Error parsing UEFA Europa League recent game: {e}")
                                                continue
                                        
                                        # Use first successful endpoint
                                        break
                                else:
                                    logger.warning(f"💀 UEFA Europa League recent games endpoint {league_id} failed with status {response.status}")
                                    
                        except Exception as e:
                            logger.warning(f"💀 UEFA Europa League recent games endpoint {league_id} error: {e}")
                            continue
                
                if all_season_games and len(all_season_games) >= 10:
                    logger.info(f"🏆 Found {len(all_season_games)} UEFA Europa League season games from ESPN API")
                else:
                    # If we got some games but not enough for season analysis, use simulation
                    if all_season_games:
                        logger.warning(f"💀 Only found {len(all_season_games)} UEFA Europa League games - not enough for season analysis")
                    else:
                        logger.warning(f"💀 No UEFA Europa League season games found for {season_year}")
                    
                    # ABSOLUTELY NO FAKE DATA BULLSHIT!
                    logger.error(f"💀 ZERO TOLERANCE FOR FAKE DATA BULLSHIT!")
                    logger.error(f"💀 Use Official UEFA Europa League API for REAL data instead!")
                    all_season_games = []
                
                return all_season_games
                
        except Exception as e:
            logger.error(f"💀 UEFA Europa League season games error: {e}")
            return []

async def test_real_uefa_europa_league_fetcher():
    """Test the real UEFA Europa League fetcher"""
    fetcher = RealUEFAEuropaLeagueFetcher()
    
    print("🏆 Testing REAL UEFA Europa League Data Fetcher...")
    games = await fetcher.fetch_todays_real_uefa_europa_league_games()
    
    print(f"\n🎯 Found {len(games)} REAL UEFA Europa League games:")
    if games:
        for game in games:
            country = game.get('country_code', '🏆')
            league = game.get('league', 'Unknown')
            matchup = game.get('matchup', 'Unknown')
            status = game.get('status', 'Unknown')
            time = game.get('time', 'Unknown')
            week = game.get('week', 'Unknown Week')
            venue = game.get('venue', 'Unknown Stadium')
            print(f"{country} {league}: {matchup}")
            print(f"   🏟️  {venue} - {week}")
            print(f"   ⏰ {time} - {status}")
            print()
    else:
        print("🏆 No UEFA Europa League games today")
        print("🔥 System READY for when UEFA Europa League matches resume!")
        print("⭐ European football integration complete!")
        print("🏆 Brighton, Real Betis, Fenerbahce, Feyenoord level system ready!")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_uefa_europa_league_fetcher())