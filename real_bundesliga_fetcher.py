#!/usr/bin/env python3
"""
🇩🇪 REAL BUNDESLIGA FETCHER - ESPN API INTEGRATION 🇩🇪

REVOLUTIONARY GERMAN FOOTBALL DATA SYSTEM
Fetches TODAY'S REAL games from ESPN API for Bundesliga.

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨

🏆 BUNDESLIGA - GERMAN EXCELLENCE:
- 🇩🇪 German Bundesliga (deu.1)

Created: September 15, 2025
Based on: Serie A real data success methodology
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Import the Universal Prediction Engine for 8D analysis
from real_agents.universal_prediction_engine import UniversalPredictionEngine

# Import the REAL BUNDESLIGA ALGORITHM! 🇩🇪⚽🔥 (DATA-DRIVEN)
from bundesliga_real_algorithm import RealBundesligaAlgorithm

logger = logging.getLogger(__name__)

class RealBundesligaFetcher:
    """
    🇩🇪⚽ REAL Bundesliga Data Fetcher
    
    Fetches authentic German football data from ESPN API.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        self.bundesliga_league_id = 'ger.1'  # ESPN's Bundesliga league ID
        
        # Initialize Universal Prediction Engine for 8D analysis
        self.prediction_engine = UniversalPredictionEngine()
        
        # 🇩🇪⚽ INITIALIZE REAL BUNDESLIGA ALGORITHM! 🔥💀🔥 (DATA-DRIVEN)
        self.bundesliga_real = RealBundesligaAlgorithm()
        
    async def fetch_todays_real_bundesliga_games(self) -> List[Dict[str, Any]]:
        """
        🔥 Fetch TODAY'S REAL Bundesliga games from ESPN API
        
        Returns ONLY real data from ESPN API.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        try:
            logger.info("🇩🇪 Fetching REAL Bundesliga games from ESPN API...")
            
            async with aiohttp.ClientSession() as session:
                url = f"{self.espn_api_base}/{self.bundesliga_league_id}/scoreboard"
                
                async with session.get(url, timeout=10) as response:
                    if response.status != 200:
                        logger.warning(f"💀 Bundesliga ESPN API failed with status {response.status}")
                        return []
                    
                    data = await response.json()
                    events = data.get('events', [])
                    
                    if not events:
                        logger.info(f"🇩🇪 No Bundesliga games today - next games Sep 19+")
                        return []
                    
                    games = []
                    for event in events:
                        try:
                            game = await self._parse_espn_game(event)
                            if game:
                                games.append(game)
                        except Exception as e:
                            logger.error(f"💀 Error parsing Bundesliga game: {e}")
                            continue
                    
                    logger.info(f"🇩🇪 Found {len(games)} REAL Bundesliga games from ESPN API")
                    return games
                    
        except Exception as e:
            logger.error(f"💀 Bundesliga fetch error: {e}")
            return []

    async def _parse_espn_game(self, event: Dict) -> Dict[str, Any]:
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
                'id': f"BUNDESLIGA_{game_id}",
                'sport': 'BUNDESLIGA',
                'league': 'BUNDESLIGA',
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
                'real_espn_data': True,  # Mark as real ESPN data
                'data_source': f'ESPN_BUNDESLIGA_API',
                'country_code': '🇩🇪',
                'league_code': self.bundesliga_league_id,
                'original_event': event  # Keep original for debugging
            }
            
            # 🔥💀🔥 BUNDESLIGA PHASE 2 LEGENDARY ALGORITHM! 💀🔥💀
            try:
                # Apply Liga MX Phase 2 legendary optimization to Bundesliga
                legendary_result = await self._apply_bundesliga_legendary_algorithm(event)
                
                if legendary_result.get('enhancement_applied'):
                    game['pick'] = legendary_result['pick']
                    game['prediction'] = legendary_result['prediction']
                    game['confidence'] = legendary_result['confidence']
                    game['enhanced_analysis'] = legendary_result['analysis']
                    
                    # 🔥💀 CHECK FOR UNDECUPLE THREAT ACTIVATION! 💀🔥
                    if legendary_result.get('undecuple_threat_activated', False):
                        game['enhancement_version'] = legendary_result.get('enhancement_version', 'UNDECUPLE THREAT - Bundesliga Hybrid Active')
                        game['algorithm'] = 'BUNDESLIGA_UNDECUPLE_THREAT'
                        logger.info(f"🚀💀 UNDECUPLE THREAT ACTIVATED for {game['matchup']}! 💀🚀")
                    else:
                        game['algorithm'] = 'BUNDESLIGA_LEGENDARY_PHASE2'
                        game['enhancement_version'] = 'Phase 2 - Bundesliga Legendary'
                    
                    logger.info(f"🇩🇪💀🇩🇪 BUNDESLIGA LEGENDARY: {game['matchup']} → {legendary_result['prediction']} ({legendary_result['confidence']:.1f}% confidence)")
                else:
                    # Fallback to basic prediction
                    game['pick'] = f"🏠 {home_team}"
                    game['prediction'] = f"🏠 {home_team}"
                    game['confidence'] = 60.0
                    game['algorithm'] = 'Fallback - Simple Home Advantage'
                    game['enhancement_version'] = 'Fallback - Simple Home Advantage'
                
            except Exception as e:
                logger.error(f"💀 Bundesliga Legendary analysis failed for {game['matchup']}: {e}")
                # Fallback to basic prediction
                game['pick'] = f"🏠 {home_team}"  # Default home advantage
                game['prediction'] = f"🏠 {home_team}"
                game['confidence'] = 60.0
                game['algorithm'] = 'Fallback - Simple Home Advantage'
                game['enhancement_version'] = 'Fallback - Simple Home Advantage'
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN Bundesliga game: {e}")
            return None

    def _format_time(self, date_str: str) -> str:
        """Format ESPN date string to readable time"""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return 'TBD'

    async def fetch_bundesliga_standings(self) -> Dict[str, Any]:
        """
        🏆 Fetch REAL Bundesliga standings from ESPN API
        """
        try:
            standings = {}
            
            async with aiohttp.ClientSession() as session:
                url = f"{self.espn_api_base}/{self.bundesliga_league_id}/standings"
                
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        standings['BUNDESLIGA'] = data
                        logger.info(f"🏆 Bundesliga standings fetched")
                    else:
                        logger.warning(f"💀 Bundesliga standings failed: {response.status}")
            
            return standings
            
        except Exception as e:
            logger.error(f"💀 Bundesliga standings error: {e}")
            return {}

    async def _apply_bundesliga_legendary_algorithm(self, event: Dict) -> Dict[str, Any]:
        """
        🔥💀🔥 BUNDESLIGA PHASE 2 LEGENDARY ALGORITHM! 💀🔥💀
        
        Implements Liga MX Phase 2 optimization adapted for German football:
        1. Recent form analysis (35% weight - GERMAN EFFICIENCY EMPHASIS)
        2. Market efficiency analysis (30% weight - GERMAN FOOTBALL MONEY FLOW)
        3. Season record integration (15% weight)
        4. Key players impact (15% weight - GERMAN TACTICAL DISCIPLINE)
        5. Home advantage (5% weight - REDUCED FOR GERMAN TACTICAL BALANCE)
        """
        try:
            competition = event['competitions'][0]
            competitors = competition['competitors']
            
            if len(competitors) != 2:
                return {'prediction': 'TBD', 'confidence': 50.0, 'analysis': 'Insufficient team data', 'enhancement_applied': False}
            
            home_competitor = next((c for c in competitors if c['homeAway'] == 'home'), competitors[0])
            away_competitor = next((c for c in competitors if c['homeAway'] == 'away'), competitors[1])
            
            home_team = home_competitor['team']['displayName']
            away_team = away_competitor['team']['displayName']
            
            # 🔥💀🔥 BUNDESLIGA UNDECUPLE THREAT INTEGRATION! 💀🔥💀
            base_confidence = 70.0  # Base confidence for hybrid engine
            try:
                # Import and use the Bundesliga Real Algorithm with UNDECUPLE THREAT
                from bundesliga_real_algorithm import RealBundesligaAlgorithm
                bundesliga_algo = RealBundesligaAlgorithm()
                
                # Create game data for the algorithm
                game_data = {
                    'home_team': home_team,
                    'away_team': away_team,
                    'venue': f'{home_team} Stadium',
                    'competition': 'Bundesliga'
                }
                
                # Apply the UNDECUPLE THREAT enhanced algorithm
                enhanced_result = await bundesliga_algo.apply_real_bundesliga_algorithm(game_data)
                
                if enhanced_result.get('undecuple_threat_activated', False):
                    logger.info(f"🚀💀 UNDECUPLE THREAT SUCCESS: {enhanced_result['prediction']} ({enhanced_result['confidence']:.1f}%)")
                    return {
                        'prediction': enhanced_result['prediction'],
                        'confidence': enhanced_result['confidence'],
                        'analysis': enhanced_result.get('enhanced_analysis', {}),
                        'enhancement_applied': True,
                        'undecuple_threat_activated': True,
                        'enhancement_version': 'UNDECUPLE THREAT - Bundesliga Hybrid Engine Active'
                    }
            except Exception as e:
                logger.warning(f"💀 UNDECUPLE THREAT failed, using Phase 2: {e}")
            
            # 🎯 PHASE 2: BUNDESLIGA LEGENDARY OPTIMIZATION! (35% weight - GERMAN EFFICIENCY)
            home_form_strength = self._calculate_form_strength(home_competitor.get('form', 'DDDDD'))
            away_form_strength = self._calculate_form_strength(away_competitor.get('form', 'DDDDD'))
            form_advantage = (home_form_strength - away_form_strength) * 0.35
            
            # 🏠 PHASE 2: GERMAN HOME ADVANTAGE (5% boost - TACTICAL BALANCE)
            home_advantage = 0.05  # 5% boost for German football (tactical discipline reduces home bias)
            
            # 📊 PHASE 2: SEASON RECORDS (15% weight - EFFICIENCY FOCUS)
            home_record_strength = self._calculate_record_strength(home_competitor.get('records', []))
            away_record_strength = self._calculate_record_strength(away_competitor.get('records', []))
            record_advantage = (home_record_strength - away_record_strength) * 0.15
            
            # 💰 PHASE 2: GERMAN MARKET EFFICIENCY (30% weight - BUNDESLIGA MONEY FLOW!)
            market_efficiency_advantage = self._analyze_bundesliga_market_efficiency(event) * 0.30
            
            # 👨‍⚕️ PHASE 2: KEY PLAYERS IMPACT (15% weight - GERMAN TACTICAL DISCIPLINE!)
            key_players_advantage = self._analyze_bundesliga_key_players_impact(event) * 0.15
            
            # 🔥💀🔥 BUNDESLIGA PHASE 2 LEGENDARY COMBINATION! 💀🔥💀
            home_total_advantage = form_advantage + home_advantage + record_advantage + market_efficiency_advantage + key_players_advantage
            away_total_advantage = -form_advantage + 0.0 + (-record_advantage) + (-market_efficiency_advantage) + (-key_players_advantage)  # Away gets no home boost
            
            # 📈 LEGENDARY CONFIDENCE CALCULATION
            advantage_gap = abs(home_total_advantage - away_total_advantage)
            base_confidence = 50.0
            legendary_confidence = min(95.0, base_confidence + (advantage_gap * 100))
            
            # 🎯 MAKE LEGENDARY PREDICTION (5% THRESHOLD FOR GERMAN PRECISION)
            if home_total_advantage > away_total_advantage + 0.05:  # Need 5% edge
                prediction = f"🏠 {home_team}"
                pick = home_team
            elif away_total_advantage > home_total_advantage + 0.05:
                prediction = f"✈️ {away_team}"  
                pick = away_team
            else:
                prediction = "🤝 DRAW"
                pick = "DRAW"
            
            # 📊 BUNDESLIGA LEGENDARY ANALYSIS BREAKDOWN  
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
                'enhancement_version': 'Phase 2 - Bundesliga Legendary',
                'legendary_factors_active': True
            }
            
            logger.info(f"🔥💀🔥 BUNDESLIGA LEGENDARY PREDICTION: {away_team} @ {home_team} → {prediction} ({legendary_confidence:.1f}% confidence)")
            
            return {
                'prediction': prediction,
                'pick': pick,
                'confidence': legendary_confidence,
                'analysis': analysis,
                'enhancement_applied': True
            }
            
        except Exception as e:
            logger.error(f"💀 Bundesliga legendary analysis error: {e}")
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

    def _analyze_bundesliga_market_efficiency(self, event: Dict) -> float:
        """💰 GERMAN MARKET EFFICIENCY - Bundesliga specific money flow analysis"""
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
            
            if home_favorite:
                return 0.10  # 10% advantage for home favorite (reduced for German efficiency)
            elif away_favorite:
                return -0.10  # 10% advantage for away favorite
            
            # Use record-based market simulation for Bundesliga
            home_record = self._calculate_record_strength(home_competitor.get('records', []))
            away_record = self._calculate_record_strength(away_competitor.get('records', []))
            
            record_diff = home_record - away_record
            market_efficiency = record_diff * 0.20  # Scale for German market efficiency
            
            return max(-0.12, min(0.12, market_efficiency))  # Cap at ±12%
            
        except Exception as e:
            logger.warning(f"💰 Bundesliga market efficiency analysis error: {e}")
            return 0.0

    def _analyze_bundesliga_key_players_impact(self, event: Dict) -> float:
        """👨‍⚕️ GERMAN KEY PLAYERS IMPACT - Bundesliga tactical discipline analysis"""
        try:
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return 0.0
            
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            # Use form consistency as proxy for tactical discipline
            home_form = home_competitor.get('form', 'DDDDD')
            away_form = away_competitor.get('form', 'DDDDD')
            
            home_consistency = self._calculate_form_consistency(home_form)
            away_consistency = self._calculate_form_consistency(away_form)
            
            # More consistent team gets advantage (tactical discipline)
            consistency_diff = home_consistency - away_consistency
            key_players_advantage = consistency_diff * 0.06  # Scale for German tactical discipline
            
            return max(-0.10, min(0.10, key_players_advantage))  # Cap at ±10%
            
        except Exception as e:
            logger.warning(f"👨‍⚕️ Bundesliga key players analysis error: {e}")
            return 0.0

    def _calculate_form_consistency(self, form_string: str) -> float:
        """Calculate team consistency from form string"""
        if not form_string or len(form_string) < 2:
            return 0.5
        
        form_values = []
        for result in form_string[-5:]:
            if result.upper() == 'W':
                form_values.append(3)
            elif result.upper() == 'D':
                form_values.append(1)
            else:
                form_values.append(0)
        
        if len(form_values) < 2:
            return 0.5
        
        # Calculate variance (lower variance = more consistent)
        mean_value = sum(form_values) / len(form_values)
        variance = sum((x - mean_value) ** 2 for x in form_values) / len(form_values)
        
        # Convert variance to consistency score
        max_variance = 2.25
        consistency = 1.0 - (variance / max_variance)
        
        return max(0.0, min(1.0, consistency))

async def test_real_bundesliga_fetcher():
    """Test the real Bundesliga fetcher"""
    fetcher = RealBundesligaFetcher()
    
    print("🇩🇪 Testing REAL Bundesliga Data Fetcher...")
    games = await fetcher.fetch_todays_real_bundesliga_games()
    
    print(f"\n🎯 Found {len(games)} REAL Bundesliga games:")
    if games:
        for game in games:
            country = game.get('country_code', '🇩🇪')
            league = game.get('league', 'Unknown')
            matchup = game.get('matchup', 'Unknown')
            status = game.get('status', 'Unknown')
            time = game.get('time', 'Unknown')
            print(f"{country} {league}: {matchup} - {status} at {time}")
    else:
        print("🇩🇪 No Bundesliga games today - season break until Sep 19+")
        print("🔥 System READY for when games resume!")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_bundesliga_fetcher())