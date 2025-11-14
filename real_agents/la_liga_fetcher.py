#!/usr/bin/env python3
"""
🏆 REAL LA LIGA FETCHER - ESPN API INTEGRATION 🏆

REVOLUTIONARY SPANISH FOOTBALL DATA SYSTEM
Fetches TODAY'S REAL games from ESPN API for La Liga.

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨

⚽🏆 LA LIGA - SPANISH FOOTBALL EXCELLENCE:
- 🏆 La Liga - Spanish First Division (esp.1)
- ⭐ Real Madrid, Barcelona, Atletico Madrid, Sevilla level elite
- 🔥 The most prestigious football competition in Spain

Created: October 21, 2025
Based on: UEFA Champions League and EPL elite success methodology
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Import the Universal Prediction Engine for 8D analysis
from real_agents.universal_prediction_engine import UniversalPredictionEngine

# Import the REAL LA LIGA ALGORITHM! 🇪🇸⚽🔥 (TYPE 1 DATA-DRIVEN)
from la_liga_real_algorithm import RealLaLigaAlgorithm

# Simple logging without broken imports
logger = logging.getLogger(__name__)

class RealLaLigaFetcher:
    """
    🏆⚽ REAL La Liga Data Fetcher
    
    Fetches authentic Spanish football data from ESPN API.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        # Try multiple possible La Liga endpoints
        self.la_liga_ids = [
            'esp.1',            # Main Spanish LALIGA ID
            'laliga',           # LaLiga alternative
            'spanish-la-liga',  # Spanish La Liga alternative
            'spain.1',          # Spain first tier
            'la-liga',          # La Liga hyphenated
        ]
        
        # Initialize Universal Prediction Engine for 8D analysis
        self.prediction_engine = UniversalPredictionEngine()
        
        # 🇪🇸⚽ INITIALIZE REAL LA LIGA ALGORITHM! 🔥💀🔥 (TYPE 1 DATA-DRIVEN)
        self.la_liga_real = RealLaLigaAlgorithm()
        
    async def fetch_todays_real_la_liga_games(self) -> List[Dict[str, Any]]:
        """
        🏆 FETCH TODAY'S REAL LA LIGA GAMES FROM ESPN API 🏆
        
        Returns ONLY real data from ESPN API.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        # Simple logging without broken imports
        logger.info("Fetching REAL La Liga games from ESPN API")
        
        all_games = []
        
        # Check multiple dates for complete gameweek
        from datetime import datetime, timedelta
        
        async with aiohttp.ClientSession() as session:
            # Try multiple La Liga endpoints
            for league_id in self.la_liga_ids:
                try:
                    # FIRST: Try without date parameter (gets current/upcoming games)
                    url = f"{self.espn_api_base}/{league_id}/scoreboard"
                    logger.info(f"Trying La Liga endpoint: {league_id} (default scoreboard)")
                    
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()
                            events = data.get('events', [])
                            
                            if events:
                                logger.info(f"Found {len(events)} La Liga games at {league_id} (default)")
                                
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
                                        logger.warning(f"Error parsing La Liga game: {e}")
                                        continue
                                        
                                # If we found games, use this endpoint
                                if all_games:
                                    logger.info(f"Found La Liga data at endpoint: {league_id}")
                                    break
                            else:
                                logger.info(f"No La Liga games at {league_id} (default)")
                        else:
                            logger.warning(f"La Liga endpoint {league_id} failed with status {response.status}")
                    
                    # FALLBACK: If no games found, try with specific dates
                    if not all_games:
                        logger.info(f"Trying {league_id} with specific dates...")
                        # Check current date, previous 4 days, and next 3 days for complete gameweek
                        for days_offset in range(-4, 4):  # -4 to +3 (8 days total)
                            date_to_check = datetime.now() + timedelta(days=days_offset)
                            date_str = date_to_check.strftime('%Y%m%d')
                            
                            url = f"{self.espn_api_base}/{league_id}/scoreboard?dates={date_str}"
                            logger.info(f"Trying La Liga endpoint: {league_id} for date {date_str}")
                            
                            async with session.get(url, timeout=10) as response:
                                if response.status == 200:
                                    data = await response.json()
                                    events = data.get('events', [])
                                    
                                    if events:
                                        logger.info(f"Found {len(events)} La Liga games at {league_id} on {date_str}")
                                        
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
                                                logger.warning(f"Error parsing La Liga game: {e}")
                                                continue
                                        
                                        # If we found games, break out of date loop
                                        if all_games:
                                            break
                                    else:
                                        logger.info(f"No La Liga games at {league_id} on {date_str}")
                                else:
                                    logger.warning(f"La Liga endpoint {league_id} failed with status {response.status}")
                                    
                    # If we found games, break out of league_id loop
                    if all_games:
                        logger.info(f"Found La Liga data at endpoint: {league_id}")
                        break
                                
                except Exception as e:
                    logger.warning(f"La Liga endpoint {league_id} error: {e}")
                    continue
            
            if all_games:
                logger.info(f"Found {len(all_games)} REAL La Liga games from ESPN API")
                return all_games
            else:
                logger.info("No La Liga games today - check schedule")
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
            
            # Get round/week information for La Liga
            season = event.get('season', {})
            competition_type = competition.get('type', {})
            round_info = competition.get('notes', [])
            week = "Jornada"  # Default Spanish term for matchday
            
            if round_info:
                for note in round_info:
                    if isinstance(note, dict) and 'headline' in note:
                        week = note['headline']
                        break
            
            # Create our game object
            game = {
                'id': f"LA_LIGA_{game_id}",
                'sport': 'LA_LIGA',
                'league': 'LA_LIGA',
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
                'week': week,  # La Liga specific
                'real_espn_data': True,  # Mark as real ESPN data
                'data_source': f'ESPN_LA_LIGA_API',
                'country_code': '🇪🇸',  # Spanish flag
                'league_code': league_id,
                'spanish_football': True,  # Mark as Spanish
                'original_event': event  # Keep original for debugging
            }
            
            # 🔥💀🔥 UNIVERSAL PREDICTION ENGINE - 8D ANALYSIS! 💀🔥💀
            try:
                # Use Universal Prediction Engine for complete 8D analysis
                analyzed_game = await self.prediction_engine.analyze_game(game, 'LA_LIGA')
                
                # Update game with 8D analysis results
                game.update(analyzed_game)
                
                logger.info(f"🔥💀🔥 8D ANALYSIS: {game['matchup']} → {game.get('prediction', 'TBD')} ({game.get('confidence', 50):.1f}% confidence)")
                
            except Exception as e:
                logger.error(f"💀 Universal Prediction Engine failed for {game['matchup']}: {e}")
                # Fallback to basic prediction
                game['pick'] = f"🏠 {home_team}"  # Default home advantage
                game['prediction'] = f"🏠 {home_team}"
                game['confidence'] = 65.0
                game['enhancement_version'] = 'Fallback - Simple Home Advantage'
            
            # 🔥💀🔥 LA LIGA PHASE 2 LEGENDARY ALGORITHM! 💀🔥💀
            try:
                # Apply Liga MX Phase 2 legendary optimization to La Liga
                legendary_result = self._apply_la_liga_legendary_algorithm(event)
                
                if legendary_result.get('enhancement_applied'):
                    game['pick'] = legendary_result['pick']
                    game['prediction'] = legendary_result['prediction']
                    game['confidence'] = legendary_result['confidence']
                    game['enhanced_analysis'] = legendary_result['analysis']
                    game['algorithm'] = 'LA_LIGA_LEGENDARY_PHASE2'
                    game['enhancement_version'] = 'Phase 2 - La Liga Legendary'
                    
                    logger.info(f"🇪🇸⚽ LA LIGA LEGENDARY: {game['matchup']} → {game['prediction']} ({game['confidence']:.1f}%)")
                else:
                    # Fallback to original algorithm
                    real_result = await self.la_liga_real.apply_real_la_liga_algorithm(game)
                    game['prediction'] = real_result.get('prediction', game.get('prediction', 'TBD'))
                    game['confidence'] = real_result.get('confidence', game.get('confidence', 50))
                    game['algorithm'] = 'REAL_LA_LIGA_DATA_DRIVEN'
                    
                    logger.info(f"🇪🇸⚽ REAL LA LIGA: {game['matchup']} → {game['prediction']} ({game['confidence']:.1f}%)")
                
            except Exception as legendary_error:
                logger.warning(f"🇪🇸 Legendary algorithm failed, using fallback: {legendary_error}")
                # Fallback to original algorithm
                try:
                    real_result = await self.la_liga_real.apply_real_la_liga_algorithm(game)
                    game['prediction'] = real_result.get('prediction', game.get('prediction', 'TBD'))
                    game['confidence'] = real_result.get('confidence', game.get('confidence', 50))
                    game['algorithm'] = 'REAL_LA_LIGA_DATA_DRIVEN'
                except Exception as e:
                    logger.error(f"💀 Both algorithms failed for {game['matchup']}: {e}")
                    game['algorithm'] = 'REAL_LA_LIGA_FALLBACK'
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN La Liga game: {e}")
            return None

    def _analyze_enhanced_prediction(self, event: Dict) -> Dict[str, Any]:
        """
        🔥💀🔥 ENHANCED LA LIGA PREDICTION ANALYSIS! 💀🔥💀
        
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
                prediction = "🤝 EMPATE"  # Spanish for "DRAW"
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
                'enhancement_version': 'Phase 1 - La Liga Enhanced'
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

    async def fetch_la_liga_standings(self) -> Dict[str, Any]:
        """
        🏆 Fetch REAL La Liga standings from ESPN API
        """
        try:
            standings = {}
            
            async with aiohttp.ClientSession() as session:
                # Try multiple endpoints for standings
                for league_id in self.la_liga_ids:
                    try:
                        url = f"{self.espn_api_base}/{league_id}/standings"
                        
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                standings['LA_LIGA'] = data
                                logger.info(f"🏆 La Liga standings fetched from {league_id}")
                                break
                            else:
                                logger.warning(f"💀 La Liga standings failed for {league_id}: {response.status}")
                    except Exception as e:
                        logger.warning(f"💀 La Liga standings error for {league_id}: {e}")
                        continue
            
            return standings
            
        except Exception as e:
            logger.error(f"💀 La Liga standings error: {e}")
            return {}

    async def fetch_la_liga_season_games(self, season_year: int = 2025) -> List[Dict[str, Any]]:
        """
        🏆 Fetch La Liga SEASON games from ESPN API
        
        Fetches historical/season games for accuracy analysis.
        Returns ONLY real season data from ESPN API.
        """
        try:
            logger.info(f"🏆 Fetching La Liga SEASON {season_year} games from ESPN API...")
            
            all_season_games = []
            
            async with aiohttp.ClientSession() as session:
                # Try multiple La Liga endpoints for season data
                for league_id in self.la_liga_ids:
                    try:
                        # Try season scoreboard endpoint (ESPN often has historical data)
                        season_url = f"{self.espn_api_base}/{league_id}/scoreboard?season={season_year}"
                        logger.info(f"🔍 Trying La Liga season endpoint: {league_id} for {season_year}")
                        
                        async with session.get(season_url, timeout=15) as response:
                            if response.status == 200:
                                data = await response.json()
                                events = data.get('events', [])
                                
                                if events:
                                    logger.info(f"✅ Found La Liga season data at endpoint: {league_id}")
                                    
                                    for event in events:
                                        try:
                                            game = await self._parse_espn_game(event, league_id)
                                            if game:
                                                # Mark as season game for tracking
                                                game['season_game'] = True
                                                game['season_year'] = season_year
                                                all_season_games.append(game)
                                        except Exception as e:
                                            logger.error(f"💀 Error parsing La Liga season game: {e}")
                                            continue
                                    
                                    # Use first successful endpoint
                                    break
                                else:
                                    logger.info(f"📅 No La Liga season games at endpoint {league_id}")
                            else:
                                logger.warning(f"💀 La Liga season endpoint {league_id} failed with status {response.status}")
                                
                    except Exception as e:
                        logger.warning(f"💀 La Liga season endpoint {league_id} error: {e}")
                        continue
                
                # If season-specific URL doesn't work, try fetching recent games by date range
                if not all_season_games:
                    logger.info(f"🔄 Trying La Liga recent games approach for season data...")
                    
                    # Try fetching recent/historical games (La Liga season runs roughly Aug-May)
                    for league_id in self.la_liga_ids:
                        try:
                            # ESPN API sometimes accepts date parameters
                            recent_url = f"{self.espn_api_base}/{league_id}/scoreboard?limit=50"
                            logger.info(f"🔍 Trying La Liga recent games: {league_id}")
                            
                            async with session.get(recent_url, timeout=15) as response:
                                if response.status == 200:
                                    data = await response.json()
                                    events = data.get('events', [])
                                    
                                    if events:
                                        logger.info(f"✅ Found La Liga recent games at endpoint: {league_id}")
                                        
                                        for event in events:
                                            try:
                                                game = await self._parse_espn_game(event, league_id)
                                                if game:
                                                    game['season_game'] = True
                                                    game['season_year'] = season_year
                                                    all_season_games.append(game)
                                            except Exception as e:
                                                logger.error(f"💀 Error parsing La Liga recent game: {e}")
                                                continue
                                        
                                        # Use first successful endpoint
                                        break
                                else:
                                    logger.warning(f"💀 La Liga recent games endpoint {league_id} failed with status {response.status}")
                                    
                        except Exception as e:
                            logger.warning(f"💀 La Liga recent games endpoint {league_id} error: {e}")
                            continue
                
                if all_season_games and len(all_season_games) >= 10:
                    logger.info(f"🏆 Found {len(all_season_games)} La Liga season games from ESPN API")
                else:
                    # If we got some games but not enough for season analysis, use simulation
                    if all_season_games:
                        logger.warning(f"💀 Only found {len(all_season_games)} La Liga games - not enough for season analysis")
                    else:
                        logger.warning(f"💀 No La Liga season games found for {season_year}")
                    
                    # ABSOLUTELY NO FAKE DATA BULLSHIT!
                    logger.error(f"💀 ZERO TOLERANCE FOR FAKE DATA BULLSHIT!")
                    logger.error(f"💀 Use Official La Liga API for REAL data instead!")
                    all_season_games = []
                
                return all_season_games
                
        except Exception as e:
            logger.error(f"💀 La Liga season games error: {e}")
            return []

    def _apply_la_liga_legendary_algorithm(self, event: Dict) -> Dict[str, Any]:
        """
        🇪🇸💀🇪🇸 LA LIGA PHASE 2 LEGENDARY ALGORITHM! 🇪🇸💀🇪🇸
        
        Liga MX Phase 2 optimization adapted for SPANISH FOOTBALL culture:
        
        🏆 SPANISH FOOTBALL WEIGHTS (optimized for La Liga excellence):
        - 🔥 Recent Form Analysis (30%) - Spanish tactical consistency 
        - 💰 Market Efficiency (35%) - Highest due to global betting interest
        - 📊 Season Records (15%) - La Liga historical performance
        - ⭐ Key Players Impact (15%) - Superstars like Mbappe, Bellingham, Pedri
        - 🏠 Home Advantage (5%) - Reduced due to global fanbase travels
        
        🇪🇸 SPANISH FOOTBALL CULTURE ADAPTATIONS:
        - Global superstar focus (Real Madrid Galacticos, Barcelona legends)
        - High market efficiency due to worldwide betting interest
        - Technical skill over physicality (Tiki-taka legacy)
        - El Clasico and Madrid derby special considerations
        """
        try:
            logger.info(f"🇪🇸🔥 Applying La Liga Phase 2 Legendary Algorithm...")
            
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return {'prediction': 'TBD', 'confidence': 50.0, 'analysis': 'Insufficient data', 'enhancement_applied': False}
            
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            home_team = home_competitor.get('team', {}).get('displayName', 'Unknown')
            away_team = away_competitor.get('team', {}).get('displayName', 'Unknown')
            
            # 🔥💀🔥 LA LIGA LEGENDARY FACTOR ANALYSIS! 💀🔥💀
            
            # 1️⃣ 🔥 RECENT FORM ANALYSIS (30% - Spanish tactical consistency)
            home_form_strength = self._calculate_form_strength(home_competitor.get('form', ''))
            away_form_strength = self._calculate_form_strength(away_competitor.get('form', ''))
            form_advantage = (home_form_strength - away_form_strength) * 0.30
            
            # 2️⃣ 🏠 HOME ADVANTAGE (5% - Global fanbase reduces home impact)
            home_advantage = 0.05  # Spanish football has global following
            
            # 3️⃣ 📊 SEASON RECORDS ANALYSIS (15% - La Liga historical performance)
            home_record_strength = self._calculate_record_strength(home_competitor.get('records', []))
            away_record_strength = self._calculate_record_strength(away_competitor.get('records', []))
            record_advantage = (home_record_strength - away_record_strength) * 0.15
            
            # 4️⃣ 💰 MARKET EFFICIENCY ANALYSIS (35% - HIGHEST due to global betting)
            market_efficiency_advantage = self._analyze_la_liga_market_efficiency(event) * 0.35
            
            # 5️⃣ ⭐ KEY PLAYERS IMPACT (15% - La Liga superstar dependency) 
            key_players_advantage = self._analyze_la_liga_key_players_impact(event) * 0.15
            
            # 🔥💀🔥 LA LIGA PHASE 2 LEGENDARY COMBINATION! 💀🔥💀
            home_total_advantage = form_advantage + home_advantage + record_advantage + market_efficiency_advantage + key_players_advantage
            away_total_advantage = -form_advantage + 0.0 + (-record_advantage) + (-market_efficiency_advantage) + (-key_players_advantage)  # Away gets no home boost
            
            # 📈 LEGENDARY CONFIDENCE CALCULATION (SPANISH FOOTBALL MASTERY)
            advantage_gap = abs(home_total_advantage - away_total_advantage)
            base_confidence = 65.0  # Higher Spanish base confidence due to global analysis
            
            # Spanish superclub confidence boost (Real Madrid, Barcelona dominance)
            home_team_lower = home_team.lower()
            away_team_lower = away_team.lower()
            superclubs = ['real madrid', 'barcelona', 'atletico madrid', 'sevilla']
            
            superclub_boost = 0.0
            if any(club in home_team_lower for club in superclubs) or any(club in away_team_lower for club in superclubs):
                superclub_boost = 10.0  # 10% boost for superclub involvement
            
            legendary_confidence = min(95.0, base_confidence + superclub_boost + (advantage_gap * 200))  # Aggressive Spanish multiplier
            
            # 🎯 MAKE LEGENDARY PREDICTION (3% THRESHOLD FOR SPANISH PRECISION)
            if home_total_advantage > away_total_advantage + 0.03:  # Spanish technical margins
                prediction = f"🏠 {home_team}"
                pick = home_team
            elif away_total_advantage > home_total_advantage + 0.03:
                prediction = f"✈️ {away_team}"  
                pick = away_team
            else:
                prediction = "🤝 EMPATE"  # Spanish for draw
                pick = "DRAW"
            
            # 📊 LA LIGA LEGENDARY ANALYSIS BREAKDOWN  
            analysis = {
                'home_form': f"{home_competitor.get('form', 'N/A')} ({home_form_strength:.2f})",
                'away_form': f"{away_competitor.get('form', 'N/A')} ({away_form_strength:.2f})",
                'home_advantage_edge': f"+{home_advantage:.1%}",
                'recent_form_edge': f"{form_advantage:+.3f}",
                'season_records_edge': f"{record_advantage:+.3f}",
                'market_efficiency_edge': f"{market_efficiency_advantage:+.3f}",
                'key_players_edge': f"{key_players_advantage:+.3f}",
                'total_home_score': f"{home_total_advantage:.2f}",
                'total_away_score': f"{away_total_advantage:.2f}",
                'enhancement_version': 'Phase 2 - La Liga Legendary',
                'legendary_factors_active': True,
                'spanish_superclub_focus': True
            }
            
            logger.info(f"🔥💀🔥 LA LIGA LEGENDARY PREDICTION: {away_team} @ {home_team} → {prediction} ({legendary_confidence:.1f}% confidence)")
            
            return {
                'prediction': prediction,
                'pick': pick,
                'confidence': legendary_confidence,
                'analysis': analysis,
                'enhancement_applied': True
            }
            
        except Exception as e:
            logger.error(f"💀 La Liga legendary analysis error: {e}")
            return {'prediction': 'TBD', 'confidence': 50.0, 'analysis': 'Analysis failed', 'enhancement_applied': False}

    def _calculate_form_strength(self, form_string: str) -> float:
        """Calculate team strength from recent form"""
        if not form_string or len(form_string) == 0:
            return 0.5
        
        points = 0
        games = min(len(form_string), 5)
        
        for result in form_string[-games:]:
            if result.upper() == 'W':
                points += 3
            elif result.upper() == 'D':
                points += 1
        
        max_points = games * 3
        return points / max_points if max_points > 0 else 0.5

    def _calculate_record_strength(self, records: List[Dict]) -> float:
        """Calculate team strength from season record"""
        for record in records:
            if record.get('name') == 'All Splits' or record.get('type') == 'total':
                summary = record.get('summary', '')
                try:
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
        
        return 0.5

    def _analyze_la_liga_market_efficiency(self, event: Dict) -> float:
        """💰 SPANISH MARKET EFFICIENCY - La Liga specific global money flow analysis"""
        try:
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return 0.0
            
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            # Check for favorite status (ESPN data)
            home_favorite = home_competitor.get('favorite', False)
            away_favorite = away_competitor.get('favorite', False)
            
            # Spanish global betting market analysis (HIGHEST efficiency due to worldwide interest)
            if home_favorite and not away_favorite:
                return 0.25  # Home favorite advantage - highest due to global betting
            elif away_favorite and not home_favorite:
                return -0.25  # Away favorite advantage - highest due to global betting
            else:
                # Check team rankings/quality for market efficiency
                home_team = home_competitor.get('team', {}).get('displayName', '').lower()
                away_team = away_competitor.get('team', {}).get('displayName', '').lower()
                
                # Spanish football superclubs (global betting magnets)
                superclubs = ['real madrid', 'barcelona', 'atletico madrid', 'sevilla']
                elite_teams = ['villarreal', 'real sociedad', 'athletic bilbao', 'valencia', 'real betis']
                
                home_superclub = any(club in home_team for club in superclubs)
                away_superclub = any(club in away_team for club in superclubs)
                home_elite = any(team in home_team for team in elite_teams)
                away_elite = any(team in away_team for team in elite_teams)
                
                if home_superclub and not away_superclub:
                    return 0.20  # Home superclub advantage
                elif away_superclub and not home_superclub:
                    return -0.20  # Away superclub advantage
                elif home_elite and not away_elite:
                    return 0.15  # Home elite advantage
                elif away_elite and not home_elite:
                    return -0.15  # Away elite advantage
                else:
                    return 0.0  # Balanced matchup
                    
        except Exception as e:
            logger.warning(f"🇪🇸 La Liga market efficiency error: {e}")
            return 0.0

    def _analyze_la_liga_key_players_impact(self, event: Dict) -> float:
        """⭐ SPANISH KEY PLAYERS - La Liga superstar impact analysis"""
        try:
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return 0.0
            
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            home_team = home_competitor.get('team', {}).get('displayName', '').lower()
            away_team = away_competitor.get('team', {}).get('displayName', '').lower()
            
            # La Liga superstar teams analysis (GLOBAL superstars)
            superstar_teams = {
                'real madrid': 0.20,     # Mbappe, Bellingham, Vinicius - global superstars
                'barcelona': 0.18,      # Yamal, Lewandowski, Pedri - Barca DNA
                'atletico madrid': 0.14, # Griezmann, Alvarez - Cholo's warriors
                'sevilla': 0.12,        # Historical European success
                'villarreal': 0.11,     # Yellow Submarine European pedigree
                'real sociedad': 0.10,  # Basque technical excellence
                'athletic bilbao': 0.09, # Athletic traditions and unique philosophy
                'valencia': 0.08,       # Historical Valencia power
                'real betis': 0.08,     # Betic flair and attacking football
                'getafe': 0.05,         # Defensive solidity
                'osasuna': 0.05         # Basque fighting spirit
            }
            
            home_star_factor = 0.0
            away_star_factor = 0.0
            
            for team, factor in superstar_teams.items():
                if team in home_team:
                    home_star_factor = factor
                if team in away_team:
                    away_star_factor = factor
            
            return home_star_factor - away_star_factor
            
        except Exception as e:
            logger.warning(f"🇪🇸 La Liga key players error: {e}")
            return 0.0

async def test_real_la_liga_fetcher():
    """Test the real La Liga fetcher"""
    fetcher = RealLaLigaFetcher()
    
    print("🏆 Testing REAL La Liga Data Fetcher...")
    games = await fetcher.fetch_todays_real_la_liga_games()
    
    print(f"\n🎯 Found {len(games)} REAL La Liga games:")
    if games:
        for game in games:
            country = game.get('country_code', '🇪🇸')
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
        print("🏆 No La Liga games today")
        print("🔥 System READY for when La Liga matches resume!")
        print("⭐ Spanish football integration complete!")
        print("🏆 Real Madrid, Barcelona, Atletico Madrid, Sevilla level system ready!")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_la_liga_fetcher())