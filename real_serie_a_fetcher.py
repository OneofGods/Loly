#!/usr/bin/env python3
"""
🇮🇹 REAL SERIE A FETCHER - ESPN API INTEGRATION 🇮🇹

REVOLUTIONARY ITALIAN FOOTBALL DATA SYSTEM
Fetches TODAY'S REAL games from ESPN API for Serie A.

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨

🏆 SERIE A - ITALIAN EXCELLENCE:
- 🇮🇹 Italian Serie A (ita.1)

Created: September 15, 2025
Based on: SEA League real data success methodology
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Import the REAL SERIE A ALGORITHM! 🇮🇹⚽🔥 (TYPE 1 DATA-DRIVEN)
from serie_a_real_algorithm import RealSerieAAlgorithm

logger = logging.getLogger(__name__)

class RealSerieAFetcher:
    """
    🇮🇹⚽ REAL Serie A Data Fetcher
    
    Fetches authentic Italian football data from ESPN API.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        self.serie_a_league_id = 'ita.1'  # ESPN's Serie A league ID
        
        # Initialize REAL SERIE A TYPE 1 ALGORITHM 🇮🇹🔥
        self.serie_a_real = RealSerieAAlgorithm()
        
    async def fetch_todays_real_serie_a_games(self) -> List[Dict[str, Any]]:
        """
        🔥 Fetch TODAY'S REAL Serie A games from ESPN API
        
        Returns ONLY real data from ESPN API.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        try:
            logger.info("🇮🇹 Fetching REAL Serie A games from ESPN API...")
            
            async with aiohttp.ClientSession() as session:
                url = f"{self.espn_api_base}/{self.serie_a_league_id}/scoreboard"
                
                async with session.get(url, timeout=10) as response:
                    if response.status != 200:
                        logger.warning(f"💀 Serie A ESPN API failed with status {response.status}")
                        return []
                    
                    data = await response.json()
                    events = data.get('events', [])
                    
                    if not events:
                        logger.info(f"🇮🇹 No Serie A games today")
                        return []
                    
                    games = []
                    for event in events:
                        try:
                            game = self._parse_espn_game(event)
                            if game:
                                # 🔥💀🔥 SERIE A UNDECUPLE THREAT v2.0 ALGORITHM! 💀🔥💀
                                real_result = await self.serie_a_real.apply_real_serie_a_algorithm(game)
                                game['prediction'] = real_result.get('prediction', game.get('prediction', 'TBD'))
                                game['confidence'] = real_result.get('confidence', game.get('confidence', 50))
                                game['algorithm'] = real_result.get('algorithm', 'REAL_SERIE_A_DATA_DRIVEN')
                                
                                # Check for UNDECUPLE THREAT activation
                                if real_result.get('undecuple_threat_activated'):
                                    game['undecuple_threat_activated'] = True
                                    game['hybrid_engine_boost'] = real_result.get('hybrid_engine_boost', 0)
                                    game['enhancement_version'] = real_result.get('enhancement_version', 'UNDECUPLE THREAT v2.0')
                                    logger.info(f"🇮🇹💀 UNDECUPLE THREAT v2.0 ACTIVATED for {game.get('matchup', 'Unknown')}!")
                                
                                games.append(game)
                        except Exception as e:
                            logger.error(f"💀 Error parsing Serie A game: {e}")
                            continue
                    
                    logger.info(f"🇮🇹 Found {len(games)} REAL Serie A games from ESPN API")
                    return games
                    
        except Exception as e:
            logger.error(f"💀 Serie A fetch error: {e}")
            return []

    def _parse_espn_game(self, event: Dict) -> Dict[str, Any]:
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
                'id': f"SERIE_A_{game_id}",
                'sport': 'SERIE_A',
                'league': 'SERIE_A',
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
                'data_source': f'ESPN_SERIE_A_API',
                'country_code': '🇮🇹',
                'league_code': self.serie_a_league_id,
                'original_event': event  # Keep original for debugging
            }
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN Serie A game: {e}")
            return None

    def _format_time(self, date_str: str) -> str:
        """Format ESPN date string to readable time"""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return 'TBD'

    async def fetch_serie_a_standings(self) -> Dict[str, Any]:
        """
        🏆 Fetch REAL Serie A standings from ESPN API
        """
        try:
            standings = {}
            
            async with aiohttp.ClientSession() as session:
                url = f"{self.espn_api_base}/{self.serie_a_league_id}/standings"
                
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        standings['SERIE_A'] = data
                        logger.info(f"🏆 Serie A standings fetched")
                    else:
                        logger.warning(f"💀 Serie A standings failed: {response.status}")
            
            return standings
            
        except Exception as e:
            logger.error(f"💀 Serie A standings error: {e}")
            return {}

    def _apply_serie_a_legendary_algorithm(self, event: Dict) -> Dict[str, Any]:
        """
        🇮🇹💀🇮🇹 SERIE A PHASE 2 LEGENDARY ALGORITHM! 🇮🇹💀🇮🇹
        
        Liga MX Phase 2 optimization adapted for ITALIAN FOOTBALL culture:
        
        🏆 TACTICAL ITALIAN WEIGHTS (optimized for Calcio excellence):
        - 🔥 Recent Form Analysis (40%) - Higher due to Italian tactical adaptations
        - 💰 Market Efficiency (25%) - Italian betting market precision
        - 📊 Season Records (15%) - Serie A historical performance
        - ⭐ Key Players Impact (15%) - Stars like Lukaku, Lautaro, Osimhen
        - 🏠 Home Advantage (5%) - Reduced due to tactical football focus
        
        🇮🇹 ITALIAN FOOTBALL CULTURE ADAPTATIONS:
        - Tactical discipline over pure athleticism  
        - Defense-first mentality (Catenaccio legacy)
        - Star player dependency (Juve, Inter, Milan dynasties)
        - Home advantage less critical than tactics
        """
        try:
            logger.info(f"🇮🇹🔥 Applying Serie A Phase 2 Legendary Algorithm...")
            
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return {'prediction': 'TBD', 'confidence': 50.0, 'analysis': 'Insufficient data', 'enhancement_applied': False}
            
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            home_team = home_competitor.get('team', {}).get('displayName', 'Unknown')
            away_team = away_competitor.get('team', {}).get('displayName', 'Unknown')
            
            # 🔥💀🔥 SERIE A LEGENDARY FACTOR ANALYSIS! 💀🔥💀
            
            # 1️⃣ 🔥 RECENT FORM ANALYSIS (40% - Italian tactical adaptations)
            home_form_strength = self._calculate_form_strength(home_competitor.get('form', ''))
            away_form_strength = self._calculate_form_strength(away_competitor.get('form', ''))
            form_advantage = (home_form_strength - away_form_strength) * 0.40
            
            # 2️⃣ 🏠 HOME ADVANTAGE (5% - Tactical focus over stadium advantage)
            home_advantage = 0.05  # Italian football values tactics over crowd
            
            # 3️⃣ 📊 SEASON RECORDS ANALYSIS (15% - Serie A historical performance)
            home_record_strength = self._calculate_record_strength(home_competitor.get('records', []))
            away_record_strength = self._calculate_record_strength(away_competitor.get('records', []))
            record_advantage = (home_record_strength - away_record_strength) * 0.15
            
            # 4️⃣ 💰 MARKET EFFICIENCY ANALYSIS (25% - Italian betting precision)
            market_efficiency_advantage = self._analyze_serie_a_market_efficiency(event) * 0.25
            
            # 5️⃣ ⭐ KEY PLAYERS IMPACT (15% - Serie A star dependency) 
            key_players_advantage = self._analyze_serie_a_key_players_impact(event) * 0.15
            
            # 🔥💀🔥 SERIE A PHASE 2 LEGENDARY COMBINATION! 💀🔥💀
            home_total_advantage = form_advantage + home_advantage + record_advantage + market_efficiency_advantage + key_players_advantage
            away_total_advantage = -form_advantage + 0.0 + (-record_advantage) + (-market_efficiency_advantage) + (-key_players_advantage)  # Away gets no home boost
            
            # 📈 LEGENDARY CONFIDENCE CALCULATION (ITALIAN FOOTBALL MASTERY)
            advantage_gap = abs(home_total_advantage - away_total_advantage)
            base_confidence = 60.0  # Higher Italian base confidence  
            
            # Italian elite team confidence boost
            home_team_lower = home_team.lower()
            away_team_lower = away_team.lower()
            elite_teams = ['juventus', 'inter', 'milan', 'napoli', 'roma', 'lazio', 'atalanta']
            
            elite_boost = 0.0
            if any(team in home_team_lower for team in elite_teams) or any(team in away_team_lower for team in elite_teams):
                elite_boost = 8.0  # 8% boost for elite team involvement
            
            legendary_confidence = min(95.0, base_confidence + elite_boost + (advantage_gap * 180))  # Aggressive Italian multiplier
            
            # 🎯 MAKE LEGENDARY PREDICTION (4% THRESHOLD FOR ITALIAN PRECISION)
            if home_total_advantage > away_total_advantage + 0.04:  # Tight Italian margins
                prediction = f"🏠 {home_team}"
                pick = home_team
            elif away_total_advantage > home_total_advantage + 0.04:
                prediction = f"✈️ {away_team}"  
                pick = away_team
            else:
                prediction = "🤝 PAREGGIO"  # Italian for draw
                pick = "DRAW"
            
            # 📊 SERIE A LEGENDARY ANALYSIS BREAKDOWN  
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
                'enhancement_version': 'Phase 2 - Serie A Legendary',
                'legendary_factors_active': True,
                'italian_tactical_focus': True
            }
            
            logger.info(f"🔥💀🔥 SERIE A LEGENDARY PREDICTION: {away_team} @ {home_team} → {prediction} ({legendary_confidence:.1f}% confidence)")
            
            return {
                'prediction': prediction,
                'pick': pick,
                'confidence': legendary_confidence,
                'analysis': analysis,
                'enhancement_applied': True
            }
            
        except Exception as e:
            logger.error(f"💀 Serie A legendary analysis error: {e}")
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

    def _analyze_serie_a_market_efficiency(self, event: Dict) -> float:
        """💰 ITALIAN MARKET EFFICIENCY - Serie A specific money flow analysis"""
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
            
            # Italian betting market analysis (BOOSTED FOR LEGENDARY)
            if home_favorite and not away_favorite:
                return 0.20  # Home favorite advantage - boosted
            elif away_favorite and not home_favorite:
                return -0.20  # Away favorite advantage - boosted
            else:
                # Check team rankings/quality for market efficiency
                home_team = home_competitor.get('team', {}).get('displayName', '').lower()
                away_team = away_competitor.get('team', {}).get('displayName', '').lower()
                
                # Italian football elite teams
                elite_teams = ['juventus', 'inter', 'milan', 'napoli', 'roma', 'lazio', 'atalanta']
                
                home_elite = any(team in home_team for team in elite_teams)
                away_elite = any(team in away_team for team in elite_teams)
                
                if home_elite and not away_elite:
                    return 0.16  # Home elite advantage - boosted
                elif away_elite and not home_elite:
                    return -0.16  # Away elite advantage - boosted
                else:
                    return 0.0  # Balanced matchup
                    
        except Exception as e:
            logger.warning(f"🇮🇹 Serie A market efficiency error: {e}")
            return 0.0

    def _analyze_serie_a_key_players_impact(self, event: Dict) -> float:
        """⭐ ITALIAN KEY PLAYERS - Serie A star impact analysis"""
        try:
            competition = event.get('competitions', [{}])[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return 0.0
            
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), {})
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), {})
            
            home_team = home_competitor.get('team', {}).get('displayName', '').lower()
            away_team = away_competitor.get('team', {}).get('displayName', '').lower()
            
            # Serie A superstar teams analysis (BOOSTED FOR LEGENDARY PERFORMANCE)
            superstar_teams = {
                'juventus': 0.12,  # Vlahovic, Chiesa - Old Lady power
                'inter': 0.15,    # Lautaro, Lukaku legacy - Nerazzurri dominance
                'milan': 0.14,    # Leao, Pulisic - Rossoneri excellence
                'napoli': 0.16,   # Osimhen, Kvaratskhelia - Partenopei magic
                'roma': 0.11,     # Dybala - Giallorossi creativity
                'lazio': 0.10,    # Immobile - Biancocelesti precision
                'atalanta': 0.13  # Lookman, Hojlund legacy - La Dea tactical mastery
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
            logger.warning(f"🇮🇹 Serie A key players error: {e}")
            return 0.0

async def test_real_serie_a_fetcher():
    """Test the real Serie A fetcher"""
    fetcher = RealSerieAFetcher()
    
    print("🇮🇹 Testing REAL Serie A Data Fetcher...")
    games = await fetcher.fetch_todays_real_serie_a_games()
    
    print(f"\n🎯 Found {len(games)} REAL Serie A games:")
    for game in games:
        country = game.get('country_code', '🇮🇹')
        league = game.get('league', 'Unknown')
        matchup = game.get('matchup', 'Unknown')
        status = game.get('status', 'Unknown')
        time = game.get('time', 'Unknown')
        prediction = game.get('prediction', 'TBD')
        confidence = game.get('confidence', 0)
        algorithm = game.get('algorithm', 'None')
        print(f"{country} {league}: {matchup} - {status} at {time}")
        print(f"   🎯 {prediction} ({confidence}% confidence) [{algorithm}]")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_serie_a_fetcher())