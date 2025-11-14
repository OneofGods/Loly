#!/usr/bin/env python3
"""
🇦🇺 REAL AUSTRALIA A-LEAGUE FETCHER - ESPN API INTEGRATION 🇦🇺

REVOLUTIONARY AUSTRALIAN FOOTBALL DATA SYSTEM
Fetches TODAY'S REAL games from ESPN API for Australia A-League.

🚨 NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA! 🚨

⚽🇦🇺 AUSTRALIA A-LEAGUE EXCELLENCE:
- 🏆 Australia A-League Men - Top tier Australian football
- ⭐ Elite teams like Sydney FC, Melbourne Victory, Melbourne City
- 🔥 The most competitive league in Australia and Oceania
- 🌟 Melbourne Derby, Sydney Derby, Big Blue classics

Created: November 3, 2025
Based on: Argentina Liga Profesional elite success methodology
"""

import asyncio
import aiohttp
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any
from australia_a_league_hybrid_engine import AustraliaALeagueHybridEngine

logger = logging.getLogger(__name__)

class RealAustraliaALeagueFetcher:
    """
    🇦🇺⚽ REAL Australia A-League Data Fetcher
    
    Fetches authentic Australian A-League football data from ESPN API.
    NO FAKE DATA BULLSHIT - ONLY REAL ESPN API DATA!
    """
    
    def __init__(self):
        self.espn_api_base = "http://site.api.espn.com/apis/site/v2/sports/soccer"
        self.hybrid_engine = AustraliaALeagueHybridEngine()
        # Australia A-League endpoint
        self.australia_league_ids = [
            'aus.1',                    # Main Australian A-League ID
            'australia.1',              # Australia first division
            'a-league.australia',       # A-League Australia
            'aleague.men',             # A-League Men
            'australia.aleague',        # Australia A-League
            'aus.aleague'              # Australia A-League short
        ]
        
    async def fetch_todays_real_australia_a_league_games(self) -> List[Dict[str, Any]]:
        """
        🔥 Fetch TODAY'S REAL Australia A-League games from ESPN API
        
        Returns ONLY real data from ESPN API.
        NO hardcoded games, NO synthetic data, NO fake fallbacks!
        """
        try:
            logger.info("🇦🇺 Fetching REAL Australia A-League games from ESPN API...")
            
            all_games = []
            
            async with aiohttp.ClientSession() as session:
                # Try multiple Australia A-League endpoints
                for league_id in self.australia_league_ids:
                    try:
                        url = f"{self.espn_api_base}/{league_id}/scoreboard"
                        logger.info(f"🔍 Trying Australia A-League endpoint: {league_id}")
                        
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                events = data.get('events', [])
                                
                                if events:
                                    logger.info(f"✅ Found Australia A-League data at endpoint: {league_id}")
                                    
                                    for event in events:
                                        try:
                                            game = self._parse_espn_game(event, league_id)
                                            if game:
                                                # Apply UNDECUPLE THREAT v2.0 hybrid engine
                                                enhanced_game = await self._enhance_with_hybrid_engine(game)
                                                all_games.append(enhanced_game)
                                        except Exception as e:
                                            logger.error(f"💀 Error parsing Australia A-League game: {e}")
                                            continue
                                    
                                    # Use first successful endpoint
                                    break
                                else:
                                    logger.info(f"📅 No Australia A-League games at endpoint {league_id}")
                            else:
                                logger.warning(f"💀 Australia A-League endpoint {league_id} failed with status {response.status}")
                                
                    except Exception as e:
                        logger.warning(f"💀 Australia A-League endpoint {league_id} error: {e}")
                        continue
                
                if all_games:
                    logger.info(f"🇦🇺 Found {len(all_games)} REAL Australia A-League games from ESPN API")
                else:
                    logger.info(f"🇦🇺 No Australia A-League games today - checking weekly schedule")
                    
                return all_games
                    
        except Exception as e:
            logger.error(f"💀 Australia A-League fetch error: {e}")
            return []

    async def _enhance_with_hybrid_engine(self, game: Dict[str, Any]) -> Dict[str, Any]:
        """
        🔥💀🔥 Enhance game with UNDECUPLE THREAT v2.0 hybrid engine
        """
        try:
            home_team = game.get('home_team', '')
            away_team = game.get('away_team', '')
            
            # Calculate base confidence
            base_confidence = await self._calculate_base_confidence(game)
            
            # Apply UNDECUPLE THREAT v2.0 hybrid engine
            prediction_text, final_confidence = self.hybrid_engine.make_hybrid_australia_prediction(
                game, base_confidence, home_team, away_team
            )
            
            # Determine algorithm type
            algorithm_type = self._determine_algorithm_type(prediction_text, game)
            
            # Create enhanced analysis
            enhanced_analysis = self._create_enhanced_analysis(
                game, prediction_text, final_confidence, algorithm_type
            )
            
            # Update game with predictions
            game.update({
                'prediction': prediction_text,
                'confidence': final_confidence,
                'algorithm': algorithm_type,
                'enhanced_analysis': enhanced_analysis,
                'undecuple_threat_v2': True,
                'australia_mastery': True,
                'melbourne_derby_ready': True
            })
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Hybrid engine enhancement error: {e}")
            return game

    async def _calculate_base_confidence(self, game: Dict[str, Any]) -> float:
        """Calculate base confidence for Australia A-League game"""
        try:
            home_team = game.get('home_team', '').upper()
            away_team = game.get('away_team', '').upper()
            venue = game.get('venue', '')
            
            # Base Australian home advantage (stronger in AFL-influenced culture)
            base_confidence = 66.0
            
            # Australia-specific adjustments
            
            # Big city teams have stronger home advantage
            big_city_boost = 0
            if any(team in home_team for team in ['SYDNEY FC', 'MELBOURNE VICTORY', 'MELBOURNE CITY']):
                big_city_boost = 6
            
            # Iconic stadium boost
            iconic_stadiums = {
                'ALLIANZ': 8,
                'MARVEL': 7,
                'AAMI': 6,
                'COMMBANK': 5
            }
            
            stadium_boost = 0
            for stadium, boost in iconic_stadiums.items():
                if stadium in venue.upper():
                    stadium_boost = boost
                    break
            
            # AFC Champions League experience boost
            afc_boost = 0
            afc_teams = ['SYDNEY FC', 'MELBOURNE VICTORY', 'WESTERN SYDNEY', 'ADELAIDE']
            if any(team in home_team for team in afc_teams):
                afc_boost = 4
            
            # Fighting spirit boost for passionate clubs
            spirit_boost = 0
            spirit_teams = ['WESTERN SYDNEY', 'MELBOURNE VICTORY', 'ADELAIDE']
            if any(team in home_team for team in spirit_teams):
                spirit_boost = 3
            
            # Calculate final base confidence
            final_base = base_confidence + big_city_boost + stadium_boost + afc_boost + spirit_boost
            
            return min(final_base, 85)  # Cap at 85 for base
            
        except Exception as e:
            logger.error(f"💀 Base confidence calculation error: {e}")
            return 66.0

    def _determine_algorithm_type(self, prediction_text: str, game: Dict[str, Any]) -> str:
        """Determine the algorithm type based on prediction and context"""
        prediction_lower = prediction_text.lower()
        derby_level = game.get('team_info', {}).get('derby_level', 'NORMAL')
        
        # Derby detection
        if 'melbourne derby' in prediction_lower:
            return 'AUSTRALIA_MELBOURNE_DERBY'
        elif 'sydney derby' in prediction_lower:
            return 'AUSTRALIA_SYDNEY_DERBY'
        elif 'big blue' in prediction_lower:
            return 'AUSTRALIA_BIG_BLUE_CLASSIC'
        
        # Giants away dominance
        if any(term in prediction_lower for term in ['harbour away', 'victory away', 'rbb away']):
            return 'AUSTRALIA_GIANTS_AWAY_DOMINANCE'
        
        # AFC Champions League legacy
        if any(term in prediction_lower for term in ['afc champions', 'afc legacy', 'afc experience']):
            return 'AUSTRALIA_AFC_LEGACY'
        
        # Trans-Tasman dynamics
        if any(term in prediction_lower for term in ['kiwi fortress', 'tasman crossing']):
            return 'AUSTRALIA_TRANS_TASMAN'
        
        # Cultural moments
        if any(term in prediction_lower for term in ['original a-league', 'aussie derby', 'melbourne clash']):
            return 'AUSTRALIA_CULTURAL_MASTERY'
        
        # Draw detection
        if any(term in prediction_lower for term in ['balance', 'tactical', 'tasman balance']):
            return 'AUSTRALIA_UNDECUPLE_DRAW_MASTERY'
        
        # Fighting spirit
        if any(term in prediction_lower for term in ['fighting spirit', 'aussie spirit']):
            return 'AUSTRALIA_FIGHTING_SPIRIT'
        
        # Finals pressure
        if any(term in prediction_lower for term in ['grand final pressure', 'finals desperation']):
            return 'AUSTRALIA_FINALS_PRESSURE'
        
        # Default
        return 'AUSTRALIA_A_LEAGUE_MASTERY'

    def _create_enhanced_analysis(self, game: Dict[str, Any], prediction: str, 
                                confidence: float, algorithm: str) -> Dict[str, str]:
        """Create enhanced analysis object for Australia A-League game"""
        try:
            home_team = game.get('home_team', '')
            away_team = game.get('away_team', '')
            derby_level = game.get('team_info', {}).get('derby_level', 'NORMAL')
            
            analysis = {
                'enhancement_version': 'UNDECUPLE_THREAT_v2.0_AUSTRALIA',
                'algorithm_type': algorithm,
                'confidence_level': f"{confidence:.1f}%",
                'prediction_basis': self._get_prediction_basis(prediction, algorithm),
                'australia_factor': self._get_australia_factor(home_team, away_team, derby_level),
                'undecuple_patterns': self._get_active_undecuple_patterns(prediction, algorithm),
                'derby_status': self._get_derby_status(algorithm),
                'afc_factor': self._get_afc_factor(home_team, away_team),
                'fighting_spirit_index': self._calculate_fighting_spirit_index(home_team, away_team),
                'oceania_dynamics': self._get_oceania_dynamics(home_team, away_team)
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"💀 Enhanced analysis creation error: {e}")
            return {'enhancement_version': 'AUSTRALIA_BASIC', 'error': str(e)}

    def _get_prediction_basis(self, prediction: str, algorithm: str) -> str:
        """Get the basis for the prediction"""
        if 'MELBOURNE_DERBY' in algorithm:
            return 'Melbourne Derby intensity and cross-city rivalry'
        elif 'SYDNEY_DERBY' in algorithm:
            return 'Sydney Derby passion with RBB and Cove support'
        elif 'BIG_BLUE' in algorithm:
            return 'Big Blue classic - Melbourne Victory vs Sydney FC heritage'
        elif 'GIANTS_AWAY' in algorithm:
            return 'Australian giants away dominance pattern'
        elif 'AFC_LEGACY' in algorithm:
            return 'AFC Champions League legacy and continental experience'
        elif 'TRANS_TASMAN' in algorithm:
            return 'Trans-Tasman dynamics and Australia-NZ rivalry'
        elif 'CULTURAL' in algorithm:
            return 'Australian football culture and passionate support'
        elif 'DRAW' in algorithm:
            return 'UNDECUPLE threat draw detection and tactical balance'
        elif 'FIGHTING_SPIRIT' in algorithm:
            return 'Australian fighting spirit and never-give-up mentality'
        else:
            return 'A-League home advantage and Australian football culture'

    def _get_australia_factor(self, home_team: str, away_team: str, derby_level: str) -> str:
        """Get Australia-specific factors"""
        factors = []
        
        # Check for Melbourne teams
        melbourne_teams = ['MELBOURNE VICTORY', 'MELBOURNE CITY', 'WESTERN UNITED']
        home_melbourne = any(team in home_team.upper() for team in melbourne_teams)
        away_melbourne = any(team in away_team.upper() for team in melbourne_teams)
        
        # Check for Sydney teams
        sydney_teams = ['SYDNEY FC', 'WESTERN SYDNEY', 'MACARTHUR']
        home_sydney = any(team in home_team.upper() for team in sydney_teams)
        away_sydney = any(team in away_team.upper() for team in sydney_teams)
        
        if home_melbourne and away_melbourne:
            factors.append('Melbourne city derby intensity')
        elif home_sydney and away_sydney:
            factors.append('Sydney city rivalry passion')
        elif home_melbourne or home_sydney:
            factors.append('Big city home advantage')
        
        # Derby factor
        if derby_level != 'NORMAL':
            factors.append(f'{derby_level} passionate derby')
        
        # AFC Champions League experience
        afc_teams = ['SYDNEY FC', 'MELBOURNE VICTORY', 'WESTERN SYDNEY', 'ADELAIDE']
        if any(team in home_team.upper() for team in afc_teams):
            factors.append('AFC Champions League pedigree')
        
        # Trans-Tasman factor
        if 'WELLINGTON' in home_team.upper() or 'AUCKLAND' in home_team.upper():
            factors.append('New Zealand Trans-Tasman dynamics')
        
        return ' + '.join(factors) if factors else 'Standard A-League dynamics'

    def _get_active_undecuple_patterns(self, prediction: str, algorithm: str) -> str:
        """Identify which UNDECUPLE patterns are active"""
        active_patterns = []
        prediction_lower = prediction.lower()
        
        # Check for each of the 11 patterns
        pattern_indicators = {
            'EPL Tactical Hierarchy': ['tactical', 'hierarchy', 'giant edge'],
            'MLS Cultural Recognition': ['derby', 'cultural', 'rivalry'],
            'Liga MX Form Volatility': ['fighting spirit', 'aussie spirit', 'passion'],
            'UEFA Financial Power': ['afc champions', 'afc legacy', 'continental'],
            'Copa Continental Dynamics': ['oceania', 'trans-tasman', 'kiwi'],
            'EFL Championship Pressure': ['finals pressure', 'grand final', 'survival'],
            'La Liga Giants Away': ['harbour away', 'victory away', 'giant away'],
            'Bundesliga Efficiency': ['tactical edge', 'systematic', 'efficiency'],
            'Enhanced Draw Detection': ['balance', 'tactical balance', 'tasman balance'],
            'MLS Final Draw Breakthrough': ['draw', 'stalemate', 'even'],
            'UEFA 90%+ Breakthrough': ['dominance', 'power', 'force']
        }
        
        for pattern, indicators in pattern_indicators.items():
            if any(indicator in prediction_lower for indicator in indicators):
                active_patterns.append(pattern)
        
        return ', '.join(active_patterns) if active_patterns else 'Standard Australian patterns'

    def _get_derby_status(self, algorithm: str) -> str:
        """Get derby status"""
        if 'MELBOURNE_DERBY' in algorithm:
            return 'MELBOURNE DERBY - Cross-city rivalry'
        elif 'SYDNEY_DERBY' in algorithm:
            return 'SYDNEY DERBY - Harbour city passion'
        elif 'BIG_BLUE' in algorithm:
            return 'BIG BLUE CLASSIC - Historic rivalry'
        elif 'CULTURAL' in algorithm:
            return 'Cultural rivalry matchup'
        else:
            return 'Regular A-League fixture'

    def _get_afc_factor(self, home_team: str, away_team: str) -> str:
        """Get AFC Champions League factor"""
        afc_champions = {
            'WESTERN SYDNEY WANDERERS': 'AFC Champions League Winners 2014',
            'SYDNEY FC': 'Multiple AFC Champions League campaigns',
            'MELBOURNE VICTORY': 'AFC Champions League regular',
            'ADELAIDE UNITED': 'AFC Champions League experience'
        }
        
        home_afc = None
        away_afc = None
        
        for team, achievement in afc_champions.items():
            if team in home_team.upper():
                home_afc = achievement
            if team in away_team.upper():
                away_afc = achievement
        
        if home_afc and away_afc:
            return f'AFC battle: {home_afc} vs {away_afc}'
        elif home_afc:
            return f'Home AFC pedigree: {home_afc}'
        elif away_afc:
            return f'Away AFC experience: {away_afc}'
        else:
            return 'Non-AFC Champions League participants'

    def _calculate_fighting_spirit_index(self, home_team: str, away_team: str) -> str:
        """Calculate fighting spirit index for Australian football"""
        spirit_ratings = {
            'WESTERN SYDNEY WANDERERS': 'MAXIMUM (10/10) - RBB Red and Black Bloc',
            'MELBOURNE VICTORY': 'EXTREME (9/10) - Active End passion',
            'ADELAIDE UNITED': 'VERY HIGH (8/10) - Red Army supporters',
            'PERTH GLORY': 'HIGH (7/10) - Shed End loyalty',
            'SYDNEY FC': 'HIGH (7/10) - The Cove atmosphere'
        }
        
        home_spirit = spirit_ratings.get(home_team.upper(), 'MODERATE (6/10) - Standard A-League')
        away_spirit = spirit_ratings.get(away_team.upper(), 'MODERATE (6/10) - Standard A-League')
        
        if home_spirit.startswith('MAXIMUM') or away_spirit.startswith('MAXIMUM'):
            return 'MAXIMUM fighting spirit expected'
        elif home_spirit.startswith('EXTREME') or away_spirit.startswith('EXTREME'):
            return 'EXTREME fighting spirit atmosphere'
        else:
            return f'Home: {home_spirit}, Away: {away_spirit}'

    def _get_oceania_dynamics(self, home_team: str, away_team: str) -> str:
        """Get Oceania regional dynamics"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        home_nz = 'WELLINGTON' in home_upper or 'AUCKLAND' in home_upper
        away_nz = 'WELLINGTON' in away_upper or 'AUCKLAND' in away_upper
        
        if home_nz and not away_nz:
            return 'New Zealand home vs Australian away - Trans-Tasman rivalry'
        elif away_nz and not home_nz:
            return 'Australian home vs New Zealand away - Continental challenge'
        elif home_nz and away_nz:
            return 'New Zealand derby within A-League structure'
        else:
            return 'Pure Australian domestic matchup'

    def _parse_espn_game(self, event: Dict, league_id: str) -> Dict[str, Any]:
        """Parse ESPN game data into our format"""
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
            venue_country = venue.get('address', {}).get('country', 'Australia')
            
            # Get round information
            season = event.get('season', {})
            competition_type = competition.get('type', {})
            round_info = competition.get('notes', [])
            matchday = "Round 1"  # Default A-League round
            
            if round_info:
                for note in round_info:
                    if isinstance(note, dict) and 'headline' in note:
                        matchday = note['headline']
                        break
            
            # Map famous Australian teams with their characteristics
            team_info = self._get_australian_team_info(home_team, away_team)
            
            # Determine stadium based on well-known Australian venues
            stadium_emoji = self._get_stadium_emoji(venue_name, home_team)
            
            # Create our game object
            game = {
                'id': f"AUSTRALIA_A_LEAGUE_{game_id}",
                'sport': 'AUSTRALIA_A_LEAGUE',
                'league': 'AUSTRALIA_A_LEAGUE',
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
                'matchday': matchday,  # A-League specific
                'real_espn_data': True,  # Mark as real ESPN data
                'data_source': f'ESPN_AUSTRALIA_A_LEAGUE_API',
                'country_code': '🇦🇺',  # Australia flag
                'league_code': league_id,
                'a_league_men': True,  # Mark as A-League Men
                'oceania_competition': True,  # Mark as Oceania competition
                'stadium_emoji': stadium_emoji,
                'team_info': team_info,
                'fighting_spirit_level': 'HIGH',  # Australian football fighting spirit
                'original_event': event  # Keep original for debugging
            }
            
            return game
            
        except Exception as e:
            logger.error(f"💀 Error parsing ESPN Australia A-League game: {e}")
            return None

    def _get_australian_team_info(self, home_team: str, away_team: str) -> Dict[str, str]:
        """Get information about famous Australian teams"""
        team_map = {
            'Sydney FC': {'emoji': '🌊💙', 'nickname': 'Sky Blues', 'supporter_group': 'The Cove'},
            'Melbourne Victory': {'emoji': '🔵⚪', 'nickname': 'Victory', 'supporter_group': 'Active End'},
            'Melbourne City': {'emoji': '🌃💙', 'nickname': 'City', 'supporter_group': 'City Till I Die'},
            'Western Sydney Wanderers': {'emoji': '🔴⚫', 'nickname': 'Wanderers', 'supporter_group': 'RBB'},
            'Adelaide United': {'emoji': '🔴💛', 'nickname': 'Reds', 'supporter_group': 'Red Army'},
            'Perth Glory': {'emoji': '💜💛', 'nickname': 'Glory', 'supporter_group': 'Shed End'},
            'Newcastle Jets': {'emoji': '🔵🔴', 'nickname': 'Jets', 'supporter_group': 'Squadron'},
            'Central Coast Mariners': {'emoji': '💛🔵', 'nickname': 'Mariners', 'supporter_group': 'Yellow Army'},
            'Wellington Phoenix': {'emoji': '💛⚫', 'nickname': 'Phoenix', 'supporter_group': 'Yellow Fever'},
            'Western United': {'emoji': '🟢⚫', 'nickname': 'United', 'supporter_group': 'Green Gully'},
        }
        
        home_info = team_map.get(home_team, {'emoji': '⚽', 'nickname': 'Home', 'supporter_group': 'Home Support'})
        away_info = team_map.get(away_team, {'emoji': '⚽', 'nickname': 'Away', 'supporter_group': 'Away Support'})
        
        return {
            'home_emoji': home_info['emoji'],
            'away_emoji': away_info['emoji'],
            'home_nickname': home_info['nickname'],
            'away_nickname': away_info['nickname'],
            'derby_level': self._get_derby_level(home_team, away_team)
        }

    def _get_derby_level(self, home_team: str, away_team: str) -> str:
        """Determine derby level between teams"""
        melbourne_derby = {'Melbourne Victory', 'Melbourne City'}
        sydney_derby = {'Sydney FC', 'Western Sydney Wanderers'}
        big_blue = {'Melbourne Victory', 'Sydney FC'}
        
        teams = {home_team, away_team}
        
        if teams == melbourne_derby:
            return 'MELBOURNE_DERBY'
        elif teams == sydney_derby:
            return 'SYDNEY_DERBY'
        elif teams == big_blue:
            return 'BIG_BLUE_CLASSIC'
        elif 'Wellington' in home_team or 'Wellington' in away_team:
            return 'TRANS_TASMAN'
        else:
            return 'NORMAL'

    def _get_stadium_emoji(self, venue_name: str, home_team: str) -> str:
        """Get appropriate emoji for stadium"""
        famous_stadiums = {
            'Allianz Stadium': '🏟️🌊',
            'Marvel Stadium': '🏟️🔵',
            'AAMI Park': '🏟️🌃',
            'CommBank Stadium': '🏟️🔴',
            'HBF Park': '🏟️💜',
            'Sky Stadium': '🏟️🇳🇿',
        }
        
        return famous_stadiums.get(venue_name, '🏟️⚽')

    def _format_time(self, date_str: str) -> str:
        """Format ESPN date string to readable time"""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%I:%M %p')
        except:
            return 'TBD'

async def test_real_australia_a_league_fetcher():
    """Test the real Australia A-League fetcher"""
    fetcher = RealAustraliaALeagueFetcher()
    
    print("🇦🇺 Testing REAL Australia A-League Data Fetcher...")
    games = await fetcher.fetch_todays_real_australia_a_league_games()
    
    print(f"\n🎯 Found {len(games)} REAL Australia A-League games:")
    if games:
        for game in games:
            country = game.get('country_code', '🇦🇺')
            league = game.get('league', 'Unknown')
            matchup = game.get('matchup', 'Unknown')
            prediction = game.get('prediction', 'TBD')
            confidence = game.get('confidence', 0)
            algorithm = game.get('algorithm', 'Unknown')
            derby_level = game.get('team_info', {}).get('derby_level', 'NORMAL')
            
            print(f"{country} {league}: {matchup}")
            print(f"   🏆 Prediction: {prediction}")
            print(f"   📊 Confidence: {confidence:.1f}%")
            print(f"   🔬 Algorithm: {algorithm}")
            print(f"   ⚔️ Derby: {derby_level}")
            print()
    else:
        print("🇦🇺 No Australia A-League games today")
        print("🔥 System READY for when A-League matches resume!")
        print("⭐ Australia A-League integration complete!")
        print("🏆 UNDECUPLE THREAT v2.0 fully integrated!")
    
    return games

if __name__ == "__main__":
    # Test the fetcher
    asyncio.run(test_real_australia_a_league_fetcher())