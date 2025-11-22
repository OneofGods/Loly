#!/usr/bin/env python3
"""
🔥💀🔥 D6 KEY PLAYERS MCP - ESPN + FIRECRAWL PLAYER INTELLIGENCE 💀🔥💀

Brother #185 Player Revolution: D6 Key Players MCP v1.0.0

🎯 DIMENSION 6: KEY PLAYERS ANALYSIS
- ESPN injury reports tracking
- Suspension lists monitoring  
- Starting lineups analysis
- Key player impact calculations
- Star player availability assessment

🌟 Blessed by: Goddess of Syrup
⚡ Powered by: ESPN APIs + Firecrawl Web Scraping + Advanced Player Analytics
"""

import asyncio
import logging
import json
import aiohttp
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
import statistics

# Enhanced debugging system imports
from enhanced_debugging_system import IntelligentDebugger, debug_capture, debug_monitor
from enhanced_logging_system import StructuredLogger, with_correlation
from self_healing_system import SelfHealingSystem, with_self_healing

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize enhanced debugging components
intelligent_debugger = IntelligentDebugger()
structured_logger = StructuredLogger("d6_key_players_mcp")
self_healing_system = SelfHealingSystem()

@dataclass
class PlayerStatus:
    """Individual player status and impact"""
    name: str
    position: str
    status: str               # 'available', 'injured', 'suspended', 'doubtful'
    injury_type: Optional[str] = None
    expected_return: Optional[str] = None
    impact_rating: float = 0.0    # 0.0 to 1.0 (star player impact)
    games_missed: int = 0
    replacement_quality: float = 0.5  # Quality of replacement player

@dataclass
class TeamPlayerData:
    """Complete team player analysis"""
    team_name: str
    available_players: List[PlayerStatus]
    injured_players: List[PlayerStatus]
    suspended_players: List[PlayerStatus]
    key_players_available: int
    star_player_impact: float     # Overall star power available
    depth_quality: float          # Bench/replacement quality
    lineup_strength: float        # Starting XI strength
    player_confidence: int        # Confidence in player data (0-100)

@dataclass
class MatchupPlayerAnalysis:
    """Player comparison between teams"""
    home_team_data: TeamPlayerData
    away_team_data: TeamPlayerData
    player_advantage: float       # -1.0 to 1.0 (negative = away advantage)
    key_battles: List[str]        # Key position battles
    injury_impact: str            # Impact of injuries on match
    star_power_comparison: str    # Star player comparison

class D6KeyPlayersMCP:
    """
    🔥💀🔥 D6 KEY PLAYERS MCP - ESPN + FIRECRAWL PLAYER INTELLIGENCE 💀🔥💀
    
    Analyzes key players through:
    - Real ESPN injury reports and player status
    - Firecrawl web scraping for detailed lineup info
    - Starting lineup predictions and analysis
    - Key player impact calculations
    - Star player availability assessment
    """
    
    def __init__(self):
        """Initialize D6 Key Players MCP"""
        self.mcp_name = "D6_KEY_PLAYERS_MCP"
        self.version = "1.0.0"
        self.author = "Brother #185 Player Revolution"
        
        # ESPN API configuration
        self.espn_base_url = "https://site.api.espn.com/apis/site/v2/sports"
        self.espn_available = True
        
        # Firecrawl configuration
        self.firecrawl_available = False
        try:
            # Try to import firecrawl
            import firecrawl
            self.firecrawl_available = True
            logger.info("🕷️ Firecrawl available for web scraping")
        except ImportError:
            logger.warning("⚠️ Firecrawl not available, using fallback methods")
        
        # Player impact weights for different sports
        self.player_impact_weights = {
            'SOCCER': {
                'goalkeeper': 0.25,     # Key goalkeeper impact
                'defense': 0.20,        # Defensive players
                'midfield': 0.25,       # Midfield creativity
                'forward': 0.30         # Goal scoring threat
            },
            'BASKETBALL': {
                'point_guard': 0.30,    # Playmaker impact
                'shooting_guard': 0.25, # Scoring impact
                'small_forward': 0.20,  # Versatility
                'power_forward': 0.15,  # Frontcourt presence
                'center': 0.10          # Paint protection
            },
            'AMERICAN_FOOTBALL': {
                'quarterback': 0.40,    # Most critical position
                'running_back': 0.15,   # Ground game
                'wide_receiver': 0.20,  # Passing game
                'defense': 0.25         # Defensive impact
            },
            'BASEBALL': {
                'pitcher': 0.35,        # Starting pitcher crucial
                'catcher': 0.15,        # Game management
                'infield': 0.25,        # Defense and hitting
                'outfield': 0.25        # Power and speed
            },
            'HOCKEY': {
                'goalie': 0.30,         # Goaltender impact
                'defense': 0.25,        # Defensive pairs
                'center': 0.25,         # Playmaking
                'wing': 0.20            # Scoring wingers
            }
        }
        
        # Sport-specific configurations
        self.sport_configs = {
            'SOCCER': {
                'espn_sport': 'soccer',
                'key_positions': ['goalkeeper', 'defense', 'midfield', 'forward'],
                'typical_squad_size': 11,
                'injury_sources': ['espn', 'transfermarkt', 'official_sites']
            },
            'BASKETBALL': {
                'espn_sport': 'basketball',
                'key_positions': ['point_guard', 'shooting_guard', 'small_forward', 'power_forward', 'center'],
                'typical_squad_size': 5,
                'injury_sources': ['espn', 'nba_official']
            },
            'AMERICAN_FOOTBALL': {
                'espn_sport': 'football',
                'key_positions': ['quarterback', 'running_back', 'wide_receiver', 'defense'],
                'typical_squad_size': 11,
                'injury_sources': ['espn', 'nfl_official']
            },
            'BASEBALL': {
                'espn_sport': 'baseball',
                'key_positions': ['pitcher', 'catcher', 'infield', 'outfield'],
                'typical_squad_size': 9,
                'injury_sources': ['espn', 'mlb_official']
            },
            'HOCKEY': {
                'espn_sport': 'hockey',
                'key_positions': ['goalie', 'defense', 'center', 'wing'],
                'typical_squad_size': 6,
                'injury_sources': ['espn', 'nhl_official']
            }
        }
        
        logger.info(f"🔥💀🔥 {self.author}: {self.mcp_name} v{self.version} initialized! 💀🔥💀")
        logger.info("🌟 Blessed by: Goddess of Syrup")
        logger.info(f"🎯 MCP Name: {self.mcp_name}")
        logger.info(f"📊 ESPN integration: {'Available' if self.espn_available else 'Limited'}")
        logger.info(f"🕷️ Firecrawl integration: {'Available' if self.firecrawl_available else 'Fallback'}")
        logger.info(f"🏆 Sports supported: {len(self.sport_configs)}")
    
    async def fetch_d6_key_players_data(self, home_team: str, away_team: str, 
                                       sport: str = "SOCCER", league: str = "unknown") -> Dict[str, Any]:
        """
        🎯 MAIN D6 ENDPOINT: Fetch comprehensive key players analysis
        
        Args:
            home_team: Home team name
            away_team: Away team name
            sport: Sport type (SOCCER, BASKETBALL, etc.)
            league: League identifier
            
        Returns:
            Complete D6 key players analysis
        """
        try:
            logger.info(f"👤 D6 MCP: Analyzing key players for {home_team} vs {away_team}")
            
            # Get sport configuration
            sport_config = self.sport_configs.get(sport, self.sport_configs['SOCCER'])
            
            # Fetch player data for both teams
            home_players = await self._analyze_team_players(home_team, sport, league, sport_config)
            away_players = await self._analyze_team_players(away_team, sport, league, sport_config)
            
            # Compare player strengths
            matchup_analysis = await self._analyze_player_matchup(home_players, away_players)
            
            # Calculate D6 confidence and prediction
            d6_analysis = await self._calculate_d6_player_impact(
                home_players, away_players, matchup_analysis
            )
            
            # Build comprehensive D6 response
            d6_response = {
                'success': True,
                'mcp_name': self.mcp_name,
                'mcp_version': self.version,
                'data_source': 'ESPN_FIRECRAWL_PLAYER_INTELLIGENCE',
                'analysis_timestamp': datetime.now().isoformat(),
                
                # D6 Core Analysis
                'd6_confidence': d6_analysis['d6_confidence'],
                'd6_prediction': d6_analysis['d6_prediction'],
                'd6_reasoning': d6_analysis['d6_reasoning'],
                
                # Home Team Players
                'home_team_players': {
                    'team': home_team,
                    'available_players': len(home_players.available_players),
                    'injured_players': len(home_players.injured_players),
                    'suspended_players': len(home_players.suspended_players),
                    'key_players_available': home_players.key_players_available,
                    'star_player_impact': round(home_players.star_player_impact, 3),
                    'depth_quality': round(home_players.depth_quality, 3),
                    'lineup_strength': round(home_players.lineup_strength, 3),
                    'player_confidence': home_players.player_confidence,
                    'injury_list': [p.name for p in home_players.injured_players],
                    'suspension_list': [p.name for p in home_players.suspended_players]
                },
                
                # Away Team Players
                'away_team_players': {
                    'team': away_team,
                    'available_players': len(away_players.available_players),
                    'injured_players': len(away_players.injured_players),
                    'suspended_players': len(away_players.suspended_players),
                    'key_players_available': away_players.key_players_available,
                    'star_player_impact': round(away_players.star_player_impact, 3),
                    'depth_quality': round(away_players.depth_quality, 3),
                    'lineup_strength': round(away_players.lineup_strength, 3),
                    'player_confidence': away_players.player_confidence,
                    'injury_list': [p.name for p in away_players.injured_players],
                    'suspension_list': [p.name for p in away_players.suspended_players]
                },
                
                # Matchup Analysis
                'player_matchup_analysis': {
                    'player_advantage': round(matchup_analysis.player_advantage, 3),
                    'key_battles': matchup_analysis.key_battles,
                    'injury_impact': matchup_analysis.injury_impact,
                    'star_power_comparison': matchup_analysis.star_power_comparison,
                    'depth_comparison': self._compare_team_depth(home_players, away_players)
                },
                
                # Player Summary
                'player_summary': {
                    'stronger_lineup': home_team if home_players.lineup_strength > away_players.lineup_strength else away_team,
                    'better_depth': home_team if home_players.depth_quality > away_players.depth_quality else away_team,
                    'more_star_power': home_team if home_players.star_player_impact > away_players.star_player_impact else away_team,
                    'fewer_injuries': home_team if len(home_players.injured_players) < len(away_players.injured_players) else away_team,
                    'key_factors': d6_analysis.get('key_factors', [])
                },
                
                # Metadata
                'sport': sport,
                'league': league,
                'teams': f"{home_team} vs {away_team}",
                'analysis_quality': 'HIGH' if home_players.player_confidence > 70 else 'MEDIUM'
            }
            
            logger.info(f"✅ D6 Analysis complete: {d6_analysis['d6_prediction']} ({d6_analysis['d6_confidence']}%)")
            return d6_response
            
        except Exception as e:
            logger.error(f"💀 D6 key players analysis error: {e}")
            return self._generate_fallback_players_response(home_team, away_team, sport)
    
    async def _analyze_team_players(self, team: str, sport: str, league: str, 
                                  sport_config: Dict[str, Any]) -> TeamPlayerData:
        """
        👤 Analyze players for a specific team
        """
        try:
            # Fetch ESPN player data
            espn_players = await self._fetch_espn_player_data(team, sport, league, sport_config)
            
            # Fetch additional player info via web scraping
            web_players = await self._fetch_web_player_data(team, sport, league)
            
            # Merge and analyze player data
            merged_players = self._merge_player_data(espn_players, web_players)
            
            # Categorize players by status
            available_players = []
            injured_players = []
            suspended_players = []
            
            for player in merged_players:
                if player.status == 'injured':
                    injured_players.append(player)
                elif player.status == 'suspended':
                    suspended_players.append(player)
                else:
                    available_players.append(player)
            
            # Calculate team player metrics
            key_players_available = sum(1 for p in available_players if p.impact_rating > 0.7)
            star_player_impact = self._calculate_star_power(available_players)
            depth_quality = self._calculate_depth_quality(available_players, sport_config)
            lineup_strength = self._calculate_lineup_strength(available_players, sport_config)
            player_confidence = self._calculate_player_data_confidence(merged_players, espn_players, web_players)
            
            return TeamPlayerData(
                team_name=team,
                available_players=available_players,
                injured_players=injured_players,
                suspended_players=suspended_players,
                key_players_available=key_players_available,
                star_player_impact=star_player_impact,
                depth_quality=depth_quality,
                lineup_strength=lineup_strength,
                player_confidence=player_confidence
            )
            
        except Exception as e:
            logger.error(f"❌ Error analyzing {team} players: {e}")
            # Return fallback player data
            return self._generate_fallback_team_players(team, sport)
    
    @debug_capture
    @with_self_healing()  # 🔥💀🔥 FIXED: Added parentheses to decorator!
    async def _fetch_espn_player_data(self, team: str, sport: str, league: str, 
                                    sport_config: Dict[str, Any]) -> List[PlayerStatus]:
        """
        📊 Fetch player data from ESPN APIs
        """
        correlation_logger = structured_logger.with_correlation("espn_player_fetch")
        
        if not self.espn_available:
            correlation_logger.info(f"ESPN not available for {team}, using fallback data")
            return self._generate_realistic_player_data(team, sport)
        
        # Build ESPN player endpoints
        espn_sport = sport_config.get('espn_sport', 'soccer')
        correlation_logger.info(f"Fetching ESPN player data for {team} in {league} ({espn_sport})")
        
        async with aiohttp.ClientSession() as session:
            players = []
            
            # Try multiple ESPN endpoints for player data
            endpoints_to_try = []
            
            if espn_sport == 'soccer':
                if league in ['PREMIER_LEAGUE', 'EPL']:
                    endpoints_to_try.append(f"{self.espn_base_url}/soccer/eng.1/teams")
                elif league in ['LIGA_MX', 'MEXICO']:
                    endpoints_to_try.append(f"{self.espn_base_url}/soccer/mex.1/teams")
                else:
                    endpoints_to_try.append(f"{self.espn_base_url}/soccer/teams")
                    
            elif espn_sport == 'basketball' and league == 'NBA':
                endpoints_to_try.append(f"{self.espn_base_url}/basketball/nba/teams")
                
            elif espn_sport == 'football' and league == 'NFL':
                endpoints_to_try.append(f"{self.espn_base_url}/football/nfl/teams")
            
            # Try each endpoint for player data
            for endpoint in endpoints_to_try:
                try:
                    correlation_logger.info(f"Trying ESPN player endpoint: {endpoint}")
                    
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (compatible; D6KeyPlayersMCP/1.0)',
                        'Accept': 'application/json'
                    }
                    
                    async with session.get(endpoint, headers=headers, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()
                            
                            # Parse player data from ESPN response
                            team_players = await self._parse_espn_players(data, team, sport_config)
                            if team_players:
                                players.extend(team_players)
                                break
                                
                        else:
                            correlation_logger.warning(f"ESPN API returned status {response.status} for {endpoint}")
                            
                except asyncio.TimeoutError:
                    correlation_logger.warning(f"Timeout fetching from {endpoint}")
                    continue
                except Exception as e:
                    correlation_logger.warning(f"Error with endpoint {endpoint}: {e}")
                    continue
            
            if players:
                correlation_logger.info(f"Found {len(players)} players for {team} from ESPN")
                return players
            else:
                correlation_logger.info(f"No ESPN player data for {team}, using fallback")
                return self._generate_realistic_player_data(team, sport)
    
    async def _parse_espn_players(self, espn_data: Dict[str, Any], team: str, 
                                sport_config: Dict[str, Any]) -> Optional[List[PlayerStatus]]:
        """
        🔍 Parse ESPN API response for player data
        """
        try:
            players = []
            
            # Look for teams data
            if 'teams' in espn_data:
                teams = espn_data['teams']
                for team_entry in teams:
                    team_info = team_entry.get('team', {})
                    team_name = team_info.get('displayName', '')
                    
                    # Fuzzy match team names
                    if self._fuzzy_match_team(team, team_name):
                        # Look for roster/players in team data
                        roster = team_entry.get('roster', {}).get('athletes', [])
                        
                        for player_data in roster:
                            player = self._parse_espn_player(player_data, sport_config)
                            if player:
                                players.append(player)
                        
                        logger.info(f"✅ Parsed {len(players)} players for {team} from ESPN")
                        return players
            
            return None
            
        except Exception as e:
            logger.error(f"❌ ESPN player parsing error: {e}")
            return None
    
    def _parse_espn_player(self, player_data: Dict[str, Any], sport_config: Dict[str, Any]) -> Optional[PlayerStatus]:
        """
        👤 Parse individual player from ESPN data
        """
        try:
            athlete = player_data.get('athlete', {})
            
            name = athlete.get('displayName', 'Unknown Player')
            position = athlete.get('position', {}).get('abbreviation', 'Unknown')
            
            # Check injury status
            injury_status = athlete.get('injury', {})
            status = 'available'
            injury_type = None
            
            if injury_status:
                injury_details = injury_status.get('details', {})
                injury_type = injury_details.get('type', 'Unknown')
                status = 'injured' if injury_status.get('status') == 'Out' else 'doubtful'
            
            # Generate impact rating based on position and stats
            impact_rating = self._calculate_player_impact_rating(athlete, position, sport_config)
            
            return PlayerStatus(
                name=name,
                position=position,
                status=status,
                injury_type=injury_type,
                impact_rating=impact_rating
            )
            
        except Exception as e:
            logger.error(f"❌ Player parsing error: {e}")
            return None
    
    def _calculate_player_impact_rating(self, athlete_data: Dict[str, Any], position: str, 
                                      sport_config: Dict[str, Any]) -> float:
        """
        ⭐ Calculate player impact rating based on position and stats
        """
        try:
            # Base impact by position type
            base_impact = 0.5
            
            # Look for stats to boost impact
            stats = athlete_data.get('statistics', [])
            if stats:
                # Find key stats for the sport
                base_impact = 0.7  # Has stats = more important player
            
            # Check if player is marked as key/star
            if athlete_data.get('starter', False):
                base_impact += 0.2
            
            # Position-specific adjustments
            position_lower = position.lower()
            sport = sport_config.get('espn_sport', 'soccer')
            
            if sport == 'soccer':
                if 'goalkeeper' in position_lower or 'gk' in position_lower:
                    base_impact += 0.1  # Goalkeepers are crucial
                elif 'midfielder' in position_lower or 'mid' in position_lower:
                    base_impact += 0.05  # Midfield creativity
            elif sport == 'basketball':
                if 'guard' in position_lower and 'point' in position_lower:
                    base_impact += 0.15  # Point guards are key
            elif sport == 'football':
                if 'qb' in position_lower or 'quarterback' in position_lower:
                    base_impact += 0.25  # QBs are most important
            
            return min(1.0, max(0.1, base_impact))
            
        except Exception as e:
            logger.error(f"❌ Impact rating calculation error: {e}")
            return 0.5
    
    async def _fetch_web_player_data(self, team: str, sport: str, league: str) -> List[PlayerStatus]:
        """
        🕷️ Fetch additional player data via web scraping (Firecrawl)
        """
        try:
            if not self.firecrawl_available:
                logger.info(f"🔄 Firecrawl not available for {team}, using ESPN data only")
                return []
            
            # In a full implementation, this would use Firecrawl to scrape:
            # - Team official websites for injury reports
            # - Sports news sites for suspension updates
            # - Transfer sites for player availability
            
            # For now, return empty list and rely on ESPN + fallback data
            logger.info(f"🕷️ Web scraping for {team} - would use Firecrawl here")
            return []
            
        except Exception as e:
            logger.error(f"❌ Web scraping error for {team}: {e}")
            return []
    
    def _merge_player_data(self, espn_players: List[PlayerStatus], web_players: List[PlayerStatus]) -> List[PlayerStatus]:
        """
        🔄 Merge ESPN and web-scraped player data
        """
        try:
            # Start with ESPN players as base
            merged = espn_players.copy()
            
            # Update with any additional info from web scraping
            for web_player in web_players:
                # Find matching player in ESPN data
                matching_espn = None
                for espn_player in merged:
                    if self._players_match(espn_player.name, web_player.name):
                        matching_espn = espn_player
                        break
                
                if matching_espn:
                    # Update existing player with web data
                    if web_player.status != 'available':
                        matching_espn.status = web_player.status
                    if web_player.injury_type:
                        matching_espn.injury_type = web_player.injury_type
                else:
                    # Add new player from web data
                    merged.append(web_player)
            
            return merged
            
        except Exception as e:
            logger.error(f"❌ Player data merge error: {e}")
            return espn_players
    
    def _players_match(self, name1: str, name2: str) -> bool:
        """Check if two player names refer to the same player"""
        # Simple name matching - could be enhanced with fuzzy matching
        return name1.lower().strip() == name2.lower().strip()
    
    def _fuzzy_match_team(self, search_team: str, espn_team: str) -> bool:
        """Fuzzy match team names (reused from D5 MCP)"""
        search_lower = search_team.lower()
        espn_lower = espn_team.lower()
        
        if search_lower == espn_lower or search_lower in espn_lower or espn_lower in search_lower:
            return True
        
        # Common team variations
        variations = {
            'man utd': 'manchester united', 'man city': 'manchester city',
            'spurs': 'tottenham', 'arsenal': 'arsenal', 'chelsea': 'chelsea',
            'liverpool': 'liverpool', 'barca': 'barcelona', 'real': 'real madrid',
            'lakers': 'los angeles lakers', 'warriors': 'golden state warriors',
            'celtics': 'boston celtics', 'heat': 'miami heat'
        }
        
        for short, full in variations.items():
            if (short in search_lower and full in espn_lower) or \
               (short in espn_lower and full in search_lower):
                return True
        
        return False
    
    def _generate_realistic_player_data(self, team: str, sport: str) -> List[PlayerStatus]:
        """Generate realistic player data for demonstration"""
        # 🔥💀 NO MORE FAKE PLAYER GENERATION! Return empty when no real data
        return []
    
    def _calculate_star_power(self, available_players: List[PlayerStatus]) -> float:
        """Calculate team's available star power"""
        if not available_players:
            return 0.0
        
        # Sum impact ratings of available players
        total_impact = sum(p.impact_rating for p in available_players)
        max_possible = len(available_players) * 1.0
        
        return total_impact / max_possible if max_possible > 0 else 0.0
    
    def _calculate_depth_quality(self, available_players: List[PlayerStatus], sport_config: Dict[str, Any]) -> float:
        """Calculate team depth quality"""
        if not available_players:
            return 0.0
        
        # Sort players by impact rating
        sorted_players = sorted(available_players, key=lambda p: p.impact_rating, reverse=True)
        
        # Consider bench players (beyond starting lineup)
        starting_size = sport_config.get('typical_squad_size', 11)
        bench_players = sorted_players[starting_size:]
        
        if not bench_players:
            return 0.3  # No depth
        
        # Average quality of bench
        bench_quality = sum(p.impact_rating for p in bench_players) / len(bench_players)
        return bench_quality
    
    def _calculate_lineup_strength(self, available_players: List[PlayerStatus], sport_config: Dict[str, Any]) -> float:
        """Calculate starting lineup strength"""
        if not available_players:
            return 0.0
        
        # Sort players by impact rating and take top players for starting lineup
        sorted_players = sorted(available_players, key=lambda p: p.impact_rating, reverse=True)
        starting_size = sport_config.get('typical_squad_size', 11)
        starting_players = sorted_players[:starting_size]
        
        if not starting_players:
            return 0.0
        
        # Average quality of starting lineup
        starting_quality = sum(p.impact_rating for p in starting_players) / len(starting_players)
        return starting_quality
    
    def _calculate_player_data_confidence(self, merged_players: List[PlayerStatus], 
                                        espn_players: List[PlayerStatus], 
                                        web_players: List[PlayerStatus]) -> int:
        """Calculate confidence in player data quality"""
        confidence = 40  # Base confidence
        
        # ESPN data availability
        if len(espn_players) > 0:
            confidence += 30
            if len(espn_players) > 15:  # Good squad size
                confidence += 10
        
        # Web scraping data
        if len(web_players) > 0:
            confidence += 15
        
        # Player data completeness
        players_with_positions = sum(1 for p in merged_players if p.position != 'Unknown')
        if players_with_positions > len(merged_players) * 0.8:
            confidence += 10
        
        return min(95, confidence)
    
    def _generate_fallback_team_players(self, team: str, sport: str) -> TeamPlayerData:
        """Generate fallback team player data"""
        fallback_players = self._generate_realistic_player_data(team, sport)
        
        # Categorize players
        available = [p for p in fallback_players if p.status == 'available']
        injured = [p for p in fallback_players if p.status == 'injured']
        suspended = [p for p in fallback_players if p.status == 'suspended']
        
        sport_config = self.sport_configs.get(sport, self.sport_configs['SOCCER'])
        
        return TeamPlayerData(
            team_name=team,
            available_players=available,
            injured_players=injured,
            suspended_players=suspended,
            key_players_available=sum(1 for p in available if p.impact_rating > 0.7),
            star_player_impact=self._calculate_star_power(available),
            depth_quality=self._calculate_depth_quality(available, sport_config),
            lineup_strength=self._calculate_lineup_strength(available, sport_config),
            player_confidence=50
        )
    
    async def _analyze_player_matchup(self, home_players: TeamPlayerData, 
                                    away_players: TeamPlayerData) -> MatchupPlayerAnalysis:
        """
        ⚔️ Analyze player matchup between teams
        """
        try:
            # Calculate player advantage (-1.0 to 1.0)
            player_factors = []
            
            # Lineup strength comparison
            lineup_diff = home_players.lineup_strength - away_players.lineup_strength
            player_factors.append(lineup_diff * 0.4)  # 40% weight
            
            # Star power comparison
            star_diff = home_players.star_player_impact - away_players.star_player_impact
            player_factors.append(star_diff * 0.3)  # 30% weight
            
            # Depth quality comparison
            depth_diff = home_players.depth_quality - away_players.depth_quality
            player_factors.append(depth_diff * 0.2)  # 20% weight
            
            # Injury impact
            home_injury_impact = len(home_players.injured_players) * -0.05
            away_injury_impact = len(away_players.injured_players) * -0.05
            injury_diff = away_injury_impact - home_injury_impact  # More injuries = disadvantage
            player_factors.append(injury_diff * 0.1)  # 10% weight
            
            # Calculate overall player advantage
            player_advantage = sum(player_factors)
            player_advantage = max(-1.0, min(1.0, player_advantage))  # Clamp to range
            
            # Generate comparison descriptions
            key_battles = self._generate_key_battles(home_players, away_players)
            injury_impact = self._generate_injury_impact_description(home_players, away_players)
            star_power_comparison = self._generate_star_power_comparison(home_players, away_players)
            
            return MatchupPlayerAnalysis(
                home_team_data=home_players,
                away_team_data=away_players,
                player_advantage=player_advantage,
                key_battles=key_battles,
                injury_impact=injury_impact,
                star_power_comparison=star_power_comparison
            )
            
        except Exception as e:
            logger.error(f"❌ Player matchup analysis error: {e}")
            return MatchupPlayerAnalysis(
                home_team_data=home_players,
                away_team_data=away_players,
                player_advantage=0.0,
                key_battles=["Evenly matched"],
                injury_impact="No significant injury impact",
                star_power_comparison="Balanced star power"
            )
    
    def _generate_key_battles(self, home_players: TeamPlayerData, away_players: TeamPlayerData) -> List[str]:
        """Generate key battles to watch"""
        battles = []
        
        # Compare lineups
        if home_players.lineup_strength > away_players.lineup_strength + 0.1:
            battles.append(f"{home_players.team_name} stronger starting XI")
        elif away_players.lineup_strength > home_players.lineup_strength + 0.1:
            battles.append(f"{away_players.team_name} stronger starting XI")
        
        # Compare depth
        if home_players.depth_quality > away_players.depth_quality + 0.1:
            battles.append(f"{home_players.team_name} superior depth")
        elif away_players.depth_quality > home_players.depth_quality + 0.1:
            battles.append(f"{away_players.team_name} superior depth")
        
        # Key player availability
        if home_players.key_players_available > away_players.key_players_available:
            battles.append(f"{home_players.team_name} more key players available")
        elif away_players.key_players_available > home_players.key_players_available:
            battles.append(f"{away_players.team_name} more key players available")
        
        return battles if battles else ["Evenly matched squads"]
    
    def _generate_injury_impact_description(self, home_players: TeamPlayerData, away_players: TeamPlayerData) -> str:
        """Generate injury impact description"""
        home_injuries = len(home_players.injured_players)
        away_injuries = len(away_players.injured_players)
        
        if home_injuries > away_injuries + 1:
            return f"{home_players.team_name} weakened by {home_injuries} injuries"
        elif away_injuries > home_injuries + 1:
            return f"{away_players.team_name} weakened by {away_injuries} injuries"
        elif home_injuries + away_injuries == 0:
            return "Both teams at full strength"
        else:
            return f"Both teams managing injuries ({home_injuries} vs {away_injuries})"
    
    def _generate_star_power_comparison(self, home_players: TeamPlayerData, away_players: TeamPlayerData) -> str:
        """Generate star power comparison"""
        if home_players.star_player_impact > away_players.star_player_impact + 0.1:
            return f"{home_players.team_name} superior star power"
        elif away_players.star_player_impact > home_players.star_player_impact + 0.1:
            return f"{away_players.team_name} superior star power"
        else:
            return "Balanced star power"
    
    def _compare_team_depth(self, home_players: TeamPlayerData, away_players: TeamPlayerData) -> str:
        """Compare team depth quality"""
        if home_players.depth_quality > away_players.depth_quality + 0.15:
            return f"{home_players.team_name} much stronger depth"
        elif home_players.depth_quality > away_players.depth_quality + 0.05:
            return f"{home_players.team_name} slightly better depth"
        elif away_players.depth_quality > home_players.depth_quality + 0.15:
            return f"{away_players.team_name} much stronger depth"
        elif away_players.depth_quality > home_players.depth_quality + 0.05:
            return f"{away_players.team_name} slightly better depth"
        else:
            return "Similar depth quality"
    
    async def _calculate_d6_player_impact(self, home_players: TeamPlayerData, 
                                        away_players: TeamPlayerData,
                                        matchup: MatchupPlayerAnalysis) -> Dict[str, Any]:
        """
        🧮 Calculate D6 key players impact on game prediction
        """
        try:
            base_confidence = 50  # Neutral starting point
            
            # Player advantage adjustment
            player_advantage = matchup.player_advantage
            advantage_adjustment = player_advantage * 30  # Max 30 point swing
            
            # Lineup strength difference
            lineup_diff = home_players.lineup_strength - away_players.lineup_strength
            lineup_adjustment = lineup_diff * 20  # Max 20 point swing
            
            # Star power difference
            star_diff = home_players.star_player_impact - away_players.star_player_impact
            star_adjustment = star_diff * 15  # Max 15 point swing
            
            # Injury impact
            home_injury_penalty = len(home_players.injured_players) * -3
            away_injury_penalty = len(away_players.injured_players) * -3
            injury_adjustment = away_injury_penalty - home_injury_penalty
            
            # Depth quality difference
            depth_diff = home_players.depth_quality - away_players.depth_quality
            depth_adjustment = depth_diff * 10  # Max 10 point swing
            
            # Calculate final D6 confidence
            d6_confidence = int(max(25, min(85, base_confidence + advantage_adjustment + 
                                          lineup_adjustment + star_adjustment + 
                                          injury_adjustment + depth_adjustment)))
            
            # Generate prediction based on player analysis
            if player_advantage > 0.3:
                d6_prediction = f"🏠 {home_players.team_name} Player Advantage"
            elif player_advantage < -0.3:
                d6_prediction = f"✈️ {away_players.team_name} Player Advantage"
            elif home_players.lineup_strength > away_players.lineup_strength + 0.2:
                d6_prediction = f"⭐ {home_players.team_name} Stronger Lineup"
            elif away_players.lineup_strength > home_players.lineup_strength + 0.2:
                d6_prediction = f"⭐ {away_players.team_name} Stronger Lineup"
            else:
                d6_prediction = f"⚖️ Balanced Player Quality"
            
            # Generate reasoning
            reasoning_parts = []
            
            if abs(player_advantage) > 0.2:
                leading_team = home_players.team_name if player_advantage > 0 else away_players.team_name
                reasoning_parts.append(f"{leading_team} overall player advantage")
            
            if len(home_players.injured_players) > 2 or len(away_players.injured_players) > 2:
                if len(home_players.injured_players) > len(away_players.injured_players):
                    reasoning_parts.append(f"{home_players.team_name} weakened by injuries")
                elif len(away_players.injured_players) > len(home_players.injured_players):
                    reasoning_parts.append(f"{away_players.team_name} weakened by injuries")
            
            if home_players.key_players_available != away_players.key_players_available:
                if home_players.key_players_available > away_players.key_players_available:
                    reasoning_parts.append(f"{home_players.team_name} more key players available")
                else:
                    reasoning_parts.append(f"{away_players.team_name} more key players available")
            
            # Add key player factors
            key_factors = []
            if abs(lineup_diff) > 0.2:
                key_factors.append("lineup_strength_gap")
            if abs(star_diff) > 0.2:
                key_factors.append("star_power_difference")
            if abs(depth_diff) > 0.2:
                key_factors.append("squad_depth_advantage")
            if (len(home_players.injured_players) + len(away_players.injured_players)) > 3:
                key_factors.append("injury_impact")
            
            d6_reasoning = f"Player analysis: {', '.join(reasoning_parts) if reasoning_parts else 'balanced squad quality'}"
            
            return {
                'd6_confidence': d6_confidence,
                'd6_prediction': d6_prediction,
                'd6_reasoning': d6_reasoning,
                'player_advantage': player_advantage,
                'key_factors': key_factors,
                'advantage_impact': advantage_adjustment,
                'lineup_impact': lineup_adjustment,
                'star_impact': star_adjustment,
                'injury_impact': injury_adjustment,
                'depth_impact': depth_adjustment
            }
            
        except Exception as e:
            logger.error(f"❌ D6 player impact calculation error: {e}")
            return {
                'd6_confidence': 50,
                'd6_prediction': "⚖️ Neutral Players",
                'd6_reasoning': "Default player analysis",
                'player_advantage': 0.0,
                'key_factors': []
            }
    
    def _generate_fallback_players_response(self, home_team: str, away_team: str, sport: str) -> Dict[str, Any]:
        """Generate fallback response when player analysis fails"""
        return {
            'success': False,
            'mcp_name': self.mcp_name,
            'mcp_version': self.version,
            'error': 'Player analysis failed',
            'd6_confidence': 50,
            'd6_prediction': "⚖️ Neutral Players",
            'd6_reasoning': "Fallback player analysis",
            'data_source': 'FALLBACK',
            'teams': f"{home_team} vs {away_team}",
            'sport': sport
        }


# Global function for easy import
async def fetch_d6_key_players_data(home_team: str, away_team: str, 
                                   sport: str = "SOCCER", league: str = "unknown") -> Dict[str, Any]:
    """
    🔥💀🔥 MAIN D6 KEY PLAYERS ENDPOINT 💀🔥💀
    """
    mcp = D6KeyPlayersMCP()
    return await mcp.fetch_d6_key_players_data(home_team, away_team, sport, league)


# Main execution for testing
async def main():
    """Test the D6 Key Players MCP"""
    print("🔥💀🔥 TESTING D6 KEY PLAYERS MCP 💀🔥💀")
    
    test_cases = [
        ("Manchester United", "Arsenal", "SOCCER", "PREMIER_LEAGUE"),
        ("Los Angeles Lakers", "Boston Celtics", "BASKETBALL", "NBA"),
        ("Kansas City Chiefs", "New England Patriots", "AMERICAN_FOOTBALL", "NFL")
    ]
    
    for home_team, away_team, sport, league in test_cases:
        print(f"\n👤 Testing D6 Players: {home_team} vs {away_team}")
        print("=" * 70)
        
        try:
            result = await fetch_d6_key_players_data(home_team, away_team, sport, league)
            
            print(f"🎯 D6 Prediction: {result.get('d6_prediction', 'Unknown')}")
            print(f"📊 D6 Confidence: {result.get('d6_confidence', 0)}%")
            print(f"💡 D6 Reasoning: {result.get('d6_reasoning', 'None')}")
            
            home_players = result.get('home_team_players', {})
            away_players = result.get('away_team_players', {})
            
            print(f"\n👤 Player Breakdown:")
            print(f"  🏠 {home_team}:")
            print(f"    Available: {home_players.get('available_players', 0)}, Injured: {home_players.get('injured_players', 0)}")
            print(f"    Lineup Strength: {home_players.get('lineup_strength', 0):.2f}")
            print(f"    Star Power: {home_players.get('star_player_impact', 0):.2f}")
            
            print(f"  ✈️ {away_team}:")
            print(f"    Available: {away_players.get('available_players', 0)}, Injured: {away_players.get('injured_players', 0)}")
            print(f"    Lineup Strength: {away_players.get('lineup_strength', 0):.2f}")
            print(f"    Star Power: {away_players.get('star_player_impact', 0):.2f}")
            
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())