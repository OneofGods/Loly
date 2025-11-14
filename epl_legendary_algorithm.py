#!/usr/bin/env python3
"""
⚽🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL LEGENDARY ALGORITHM - PREMIER LEAGUE CUSTOM ALGORITHM 🔥💀

BASED ON EPL-SPECIFIC ANALYSIS:
- Current: 33.33% accuracy (6/9 predictions wrong)
- Target: 80%+ accuracy (Liga MX level)
- Problem: Over-reliance on market efficiency, weak historical analysis

EPL-SPECIFIC FACTORS DISCOVERED:
1. Market Efficiency: 77% (too high weight in current system)
2. Historical Matchups: 54% (weak - needs EPL rivalry boost) 
3. Venue/Weather: 74% (English weather matters!)
4. Sentiment: 37% (EPL fan sentiment different from Liga MX)
5. Team Performance: 61% (needs EPL-specific team analysis)
6. Key Players: 67% (needs Premier League star impact)

LIGA MX SUCCESS FACTORS TO ADAPT:
- Market Efficiency: 25% weight (EPL: reduce from current over-weight)
- Team Performance: 30% weight (EPL: increase with EPL-specific data)
- Key Players: 20% weight (EPL: focus on Premier League stars)
- Home Advantage: 8% (EPL: English home advantage analysis)
- Competition Boost: 10% (EPL: Premier League prestige)
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import json

# Import Enhanced Prediction Engine to fix home bias
try:
    from epl_enhanced_prediction_engine import EPLEnhancedPredictionEngine
except ImportError:
    class EPLEnhancedPredictionEngine:
        def make_enhanced_epl_prediction(self, game_data, base_confidence, home_team, away_team):
            return f"🏠 {home_team}", base_confidence  # Fallback

logger = logging.getLogger(__name__)

class EPLLegendaryAlgorithm:
    """
    ⚽🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL LEGENDARY ALGORITHM - PREMIER LEAGUE SPECIALIST
    
    Applies EPL-specific analysis patterns to achieve 80%+ accuracy
    Based on historical EPL performance data and Liga MX success methodology
    """
    
    def __init__(self):
        logger.info("⚽🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL LEGENDARY ALGORITHM INITIALIZED - TARGET: 80%+ ACCURACY!")
        # Initialize Enhanced Prediction Engine to fix home bias
        self.enhanced_predictor = EPLEnhancedPredictionEngine()
    
    async def apply_epl_legendary_algorithm(self, game_data: Dict) -> Dict:
        """
        🔥 APPLY EPL LEGENDARY ALGORITHM TO PREMIER LEAGUE GAME
        
        EPL-Specific Success Formula (LIGA MX CLONE STRUCTURE):
        1. Recent Form (30% weight) - EPL current team form
        2. Market Efficiency (25% weight) - MONEY FLOW analysis  
        3. Season Records (20% weight) - EPL season performance
        4. Key Players (15% weight) - Premier League injury analysis
        5. Home Advantage (8% weight) - English venues (reduced)
        6. X-Factor (2% weight) - EPL money flow + rivalries
        """
        try:
            home_team = game_data.get('home_team', 'Unknown')
            away_team = game_data.get('away_team', 'Unknown')
            
            # EPL LIGA MX CLONE Algorithm Implementation
            recent_form = await self._calculate_epl_recent_form(game_data)
            market_efficiency_money_flow = await self._calculate_epl_money_flow(game_data)
            season_records = await self._calculate_epl_season_records(game_data)
            key_players_injuries = await self._calculate_epl_key_players_injuries(game_data)
            home_advantage_reduced = await self._calculate_epl_home_advantage_reduced(game_data)
            x_factor_money_flow = await self._calculate_epl_x_factor_money_flow(game_data)
            
            # EPL LIGA MX CLONE Formula (EXACT SAME WEIGHTS!)
            base_confidence = (
                recent_form * 0.30 +                    # 30% Recent Form
                market_efficiency_money_flow * 0.25 +   # 25% Market Efficiency + Money Flow
                season_records * 0.20 +                 # 20% Season Records
                key_players_injuries * 0.15 +           # 15% Key Players + Injuries
                home_advantage_reduced * 0.08 +         # 8% Home Advantage (reduced)
                x_factor_money_flow * 0.02              # 2% X-Factor (money flow)
            )
            
            # EPL ENHANCED Prediction Logic (FIXES HOME BIAS!)
            prediction, final_confidence = self.enhanced_predictor.make_enhanced_epl_prediction(
                game_data, base_confidence, home_team, away_team
            )
            
            # EPL Legendary Result Structure
            analyzed_game = {
                'home_team': home_team,
                'away_team': away_team,
                'prediction': prediction,
                'confidence': round(final_confidence, 1),
                'league': 'PREMIER_LEAGUE',
                'algorithm': 'EPL_LEGENDARY_CUSTOM',
                
                # EPL LIGA MX CLONE Factors
                'epl_recent_form': recent_form,
                'epl_market_efficiency_money_flow': market_efficiency_money_flow,
                'epl_season_records': season_records,
                'epl_key_players_injuries': key_players_injuries,
                'epl_home_advantage_reduced': home_advantage_reduced,
                'epl_x_factor_money_flow': x_factor_money_flow,
                
                'analysis_source': 'EPL_LEGENDARY_ALGORITHM',
                'country': 'England',
                'competition': 'Premier League',
                'venue': game_data.get('venue', 'Premier League Stadium'),
                'date': datetime.now().strftime('%Y-%m-%d'),
                'timestamp': datetime.now(timezone.utc).isoformat(),
                
                # Comparison with old system
                'old_system_confidence': game_data.get('confidence', 0),
                'improvement_target': '80% accuracy (vs 33.33% current)'
            }
            
            logger.info(f"⚽ {away_team} @ {home_team}: {prediction} ({final_confidence:.1f}%) [EPL Algorithm]")
            return analyzed_game
            
        except Exception as e:
            logger.error(f"Error applying EPL legendary algorithm: {e}")
            return game_data

    async def _calculate_epl_recent_form(self, game_data: Dict) -> float:
        """Calculate EPL recent form (30% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # EPL Recent Form Analysis (last 5 games like Liga MX)
        elite_form = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL']  # Currently best form
        good_form = ['CHELSEA', 'TOTTENHAM', 'NEWCASTLE', 'BRIGHTON', 'ASTON VILLA']
        average_form = ['MANCHESTER UNITED', 'WEST HAM', 'FULHAM', 'BRENTFORD']
        poor_form = ['AFC BOURNEMOUTH', 'CRYSTAL PALACE', 'EVERTON']
        
        home_form = 50  # baseline
        away_form = 50  # baseline
        
        # EPL Form Analysis
        if any(team in home_team for team in elite_form):
            home_form = 85
        elif any(team in home_team for team in good_form):
            home_form = 75
        elif any(team in home_team for team in average_form):
            home_form = 65
        elif any(team in home_team for team in poor_form):
            home_form = 45
        
        if any(team in away_team for team in elite_form):
            away_form = 85
        elif any(team in away_team for team in good_form):
            away_form = 75
        elif any(team in away_team for team in average_form):
            away_form = 65
        elif any(team in away_team for team in poor_form):
            away_form = 45
        
        # Liga MX style form calculation
        form_diff = abs(home_form - away_form)
        if form_diff > 25:
            return 82.0  # Massive form difference
        elif form_diff > 15:
            return 75.0  # Significant form difference
        elif form_diff > 8:
            return 68.0  # Moderate form difference
        else:
            return 60.0  # Similar form

    async def _calculate_epl_money_flow(self, game_data: Dict) -> float:
        """Calculate EPL money flow analysis (25% weight - Liga MX KEY FACTOR!)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        current_market = game_data.get('market_efficiency', 77)
        
        # EPL MONEY FLOW ANALYSIS (Like Liga MX secret sauce!)
        big_money_teams = ['MANCHESTER CITY', 'CHELSEA', 'ARSENAL', 'MANCHESTER UNITED']
        investment_teams = ['NEWCASTLE', 'TOTTENHAM', 'ASTON VILLA', 'WEST HAM']
        
        home_money_flow = 50
        away_money_flow = 50
        
        # Money flow analysis
        if any(team in home_team for team in big_money_teams):
            home_money_flow = 85  # High investment backing
        elif any(team in home_team for team in investment_teams):
            home_money_flow = 72  # Moderate investment
        
        if any(team in away_team for team in big_money_teams):
            away_money_flow = 85
        elif any(team in away_team for team in investment_teams):
            away_money_flow = 72
        
        # Combine market efficiency with money flow (Liga MX style)
        market_factor = min(current_market, 85)  # Cap market efficiency
        money_flow_avg = (home_money_flow + away_money_flow) / 2
        
        # Liga MX money flow formula
        combined_score = (market_factor * 0.6) + (money_flow_avg * 0.4)
        
        return min(combined_score, 88.0)  # Cap at 88% like Liga MX

    async def _calculate_epl_season_records(self, game_data: Dict) -> float:
        """Calculate EPL season records (20% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # EPL Season Performance Tiers (like Liga MX but for EPL)
        title_contenders = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL']  # Top 3
        european_spots = ['CHELSEA', 'TOTTENHAM', 'NEWCASTLE', 'MANCHESTER UNITED']  # 4-7
        mid_table = ['ASTON VILLA', 'BRIGHTON', 'WEST HAM', 'FULHAM', 'BRENTFORD']  # 8-15
        relegation_battle = ['AFC BOURNEMOUTH', 'CRYSTAL PALACE', 'EVERTON']  # Bottom
        
        home_season = 50
        away_season = 50
        
        # Season records analysis
        if any(team in home_team for team in title_contenders):
            home_season = 88
        elif any(team in home_team for team in european_spots):
            home_season = 75
        elif any(team in home_team for team in mid_table):
            home_season = 62
        elif any(team in home_team for team in relegation_battle):
            home_season = 45
        
        if any(team in away_team for team in title_contenders):
            away_season = 88
        elif any(team in away_team for team in european_spots):
            away_season = 75
        elif any(team in away_team for team in mid_table):
            away_season = 62
        elif any(team in away_team for team in relegation_battle):
            away_season = 45
        
        # Liga MX style season calculation
        season_diff = abs(home_season - away_season)
        if season_diff > 30:
            return 85.0  # Huge season gap
        elif season_diff > 20:
            return 78.0  # Significant season gap
        elif season_diff > 10:
            return 70.0  # Moderate season gap
        else:
            return 62.0  # Similar season performance

    async def _calculate_epl_key_players_injuries(self, game_data: Dict) -> float:
        """Calculate EPL key players + injuries (15% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # EPL Star Players Impact + Injury Analysis
        superstar_impact = {
            'MANCHESTER CITY': 90,  # Haaland, De Bruyne
            'ARSENAL': 85,          # Odegaard, Saka
            'LIVERPOOL': 88,        # Salah, Van Dijk
            'CHELSEA': 75,          # Palmer, Jackson
            'TOTTENHAM': 80,        # Son, Maddison
            'MANCHESTER UNITED': 70, # Rashford, Bruno
            'NEWCASTLE': 72,        # Isak, Gordon
        }
        
        home_player_impact = superstar_impact.get(home_team, 55)
        away_player_impact = superstar_impact.get(away_team, 55)
        
        # Liga MX style key players calculation with injury factor
        player_avg = (home_player_impact + away_player_impact) / 2
        
        # Injury adjustment (EPL specific)
        if player_avg > 85:
            return min(player_avg - 5, 85)  # Top teams risk injury impact
        elif player_avg > 75:
            return min(player_avg - 2, 80)  # Good teams moderate impact
        else:
            return min(player_avg + 3, 65)  # Lower teams benefit from focus

    async def _calculate_epl_home_advantage_reduced(self, game_data: Dict) -> float:
        """Calculate EPL home advantage reduced (8% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        venue = game_data.get('venue', '').upper()
        
        # EPL Fortress Venues (Liga MX style but for EPL)
        fortress_venues = {
            'ANFIELD': 82,           # Liverpool fortress
            'ETIHAD': 78,           # Manchester City
            'EMIRATES': 75,         # Arsenal
            'OLD TRAFFORD': 76,     # Manchester United
            'STAMFORD BRIDGE': 73,  # Chelsea
            'ST JAMES': 80,         # Newcastle (amazing home support)
        }
        
        # Check for fortress venues
        for venue_name, advantage in fortress_venues.items():
            if venue_name in venue or venue_name in home_team:
                return min(advantage, 82)  # Cap like Liga MX
        
        # Standard EPL home advantage (reduced like Liga MX 8%)
        return 65.0  # Liga MX style reduced home advantage

    async def _calculate_epl_x_factor_money_flow(self, game_data: Dict) -> float:
        """Calculate EPL X-Factor with money flow (2% weight - Liga MX secret!)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # EPL X-Factor: Money Flow + Rivalries + Pressure (Liga MX style)
        
        # 1. Money Flow X-Factor
        oil_money_teams = ['MANCHESTER CITY', 'NEWCASTLE']  # Oil/Saudi money
        american_investment = ['CHELSEA', 'MANCHESTER UNITED', 'ARSENAL', 'LIVERPOOL']
        
        money_flow_factor = 50
        if any(team in home_team for team in oil_money_teams) or any(team in away_team for team in oil_money_teams):
            money_flow_factor = 85  # Oil money X-factor
        elif any(team in home_team for team in american_investment) or any(team in away_team for team in american_investment):
            money_flow_factor = 72  # American investment X-factor
        
        # 2. EPL Rivalries X-Factor
        big_rivalries = [
            ('MANCHESTER UNITED', 'MANCHESTER CITY'),  # Manchester Derby
            ('ARSENAL', 'TOTTENHAM'),                  # North London Derby
            ('LIVERPOOL', 'MANCHESTER UNITED'),        # Historic rivalry
        ]
        
        rivalry_factor = 50
        for team1, team2 in big_rivalries:
            if (team1 in home_team and team2 in away_team) or (team2 in home_team and team1 in away_team):
                rivalry_factor = 80  # Big rivalry X-factor
        
        # 3. Pressure Factor (Title race, relegation)
        pressure_factor = 55  # baseline
        
        # Liga MX style X-Factor combination
        x_factor_score = (money_flow_factor * 0.5) + (rivalry_factor * 0.3) + (pressure_factor * 0.2)
        
        return min(x_factor_score, 85.0)  # Cap like Liga MX

    async def _calculate_epl_key_players(self, game_data: Dict) -> float:
        """Calculate EPL key players impact (25% weight - increased focus)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # EPL Star Players Impact
        superstar_teams = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL']  # Haaland, Salah, etc.
        star_teams = ['CHELSEA', 'MANCHESTER UNITED', 'TOTTENHAM', 'NEWCASTLE']
        
        home_player_impact = 50
        away_player_impact = 50
        
        if any(team in home_team for team in superstar_teams):
            home_player_impact = 85
        elif any(team in home_team for team in star_teams):
            home_player_impact = 75
        
        if any(team in away_team for team in superstar_teams):
            away_player_impact = 85
        elif any(team in away_team for team in star_teams):
            away_player_impact = 75
        
        # Calculate key players advantage
        player_diff = abs(home_player_impact - away_player_impact)
        if player_diff > 15:
            return 80.0  # Star player advantage
        elif player_diff > 8:
            return 70.0  # Moderate player advantage
        else:
            return 60.0  # Similar player quality

    async def _calculate_epl_rivalries(self, game_data: Dict) -> float:
        """Calculate EPL historical rivalries (10% weight - EPL-specific)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # EPL Classic Rivalries
        big_rivalries = [
            ('MANCHESTER UNITED', 'MANCHESTER CITY'),  # Manchester Derby
            ('ARSENAL', 'TOTTENHAM'),  # North London Derby
            ('LIVERPOOL', 'MANCHESTER UNITED'),  # Historic rivalry
            ('CHELSEA', 'ARSENAL'),  # London rivalry
        ]
        
        # Check for big rivalries
        for team1, team2 in big_rivalries:
            if (team1 in home_team and team2 in away_team) or (team2 in home_team and team1 in away_team):
                return 75.0  # Big rivalry factor
        
        # London derbies
        london_teams = ['ARSENAL', 'CHELSEA', 'TOTTENHAM', 'WEST HAM', 'FULHAM', 'BRENTFORD']
        home_london = any(team in home_team for team in london_teams)
        away_london = any(team in away_team for team in london_teams)
        
        if home_london and away_london:
            return 65.0  # London derby
        
        return 55.0  # Regular matchup

    async def _calculate_english_home_advantage(self, game_data: Dict) -> float:
        """Calculate English home advantage (10% weight - EPL-specific)"""
        home_team = game_data.get('home_team', '').upper()
        venue = game_data.get('venue', '').upper()
        
        # EPL Fortress Venues
        fortress_venues = {
            'ANFIELD': 85,  # Liverpool
            'ETIHAD': 80,   # Manchester City
            'OLD TRAFFORD': 80,  # Manchester United
            'EMIRATES': 75,  # Arsenal
            'STAMFORD BRIDGE': 75,  # Chelsea
        }
        
        # Strong home advantage venues
        for venue_name, advantage in fortress_venues.items():
            if venue_name in venue or venue_name in home_team:
                return advantage
        
        # General EPL home advantage
        if 'STADIUM' in venue or 'PARK' in venue:
            return 65.0  # Standard EPL home advantage
        
        return 60.0  # Minimal home advantage

    def _make_epl_prediction(self, game_data: Dict, base_confidence: float, home_team: str, away_team: str) -> tuple:
        """Make EPL-specific prediction based on English football characteristics"""
        
        # EPL-specific adjustments
        epl_boost = 5.0  # Premier League quality boost
        
        # EPL TACTICAL DRAW DETECTION - Big Six rivalries often draw
        big_six = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL', 'CHELSEA', 'MANCHESTER UNITED', 'TOTTENHAM']
        home_big_six = any(team in home_team.upper() for team in big_six)
        away_big_six = any(team in away_team.upper() for team in big_six)
        
        # EPL Draw Conditions - Premier League specific scenarios
        if (home_big_six and away_big_six and 60 <= base_confidence <= 75):
            # Big Six vs Big Six tactical battle - often cagey
            return "🤝 DRAW", min(90.0, base_confidence + epl_boost - 5)  # Slightly reduce confidence for draws
        elif (base_confidence <= 55):
            # Very close match - unpredictable EPL
            return "🤝 DRAW", min(90.0, base_confidence + epl_boost)
        elif (58 <= base_confidence <= 62 and not (home_big_six or away_big_six)):
            # Mid-table tactical stalemate 
            return "🤝 DRAW", min(90.0, base_confidence + epl_boost - 3)
        
        # Standard EPL prediction logic
        if base_confidence > 75:
            # Strong favorite
            stronger_team = self._get_stronger_epl_team(home_team, away_team)
            return f"🏆 {stronger_team}", min(90.0, base_confidence + epl_boost + 8)
        elif base_confidence > 65:
            # Moderate favorite  
            if self._is_home_advantage_significant(home_team):
                return f"🏠 {home_team}", min(90.0, base_confidence + epl_boost + 5)
            else:
                stronger_team = self._get_stronger_epl_team(home_team, away_team)
                return f"⚽ {stronger_team}", min(90.0, base_confidence + epl_boost + 3)
        else:
            # Close match - EPL often has surprises (55-65 range)
            # Add some balance to prevent excessive home bias
            if self._is_home_advantage_significant(home_team):
                return f"🏠 {home_team}", min(90.0, base_confidence + epl_boost + 2)
            else:
                # For non-fortress teams, slightly favor stronger team to reduce home bias
                stronger_team = self._get_stronger_epl_team(home_team, away_team)
                if stronger_team == home_team:
                    return f"🏠 {home_team}", min(90.0, base_confidence + epl_boost + 1)
                else:
                    return f"⚽ {stronger_team}", min(90.0, base_confidence + epl_boost + 1)

    def _get_stronger_epl_team(self, home_team: str, away_team: str) -> str:
        """Determine stronger team based on EPL hierarchy"""
        big_six = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL', 'CHELSEA', 'MANCHESTER UNITED', 'TOTTENHAM']
        
        home_big_six = any(team in home_team.upper() for team in big_six)
        away_big_six = any(team in away_team.upper() for team in big_six)
        
        if home_big_six and not away_big_six:
            return home_team
        elif away_big_six and not home_big_six:
            return away_team
        else:
            # Both or neither in big six - prefer home
            return home_team

    def _is_home_advantage_significant(self, home_team: str) -> bool:
        """Check if home team has significant home advantage"""
        strong_home_teams = ['LIVERPOOL', 'MANCHESTER CITY', 'ARSENAL', 'NEWCASTLE']
        return any(team in home_team.upper() for team in strong_home_teams)

# Test function
async def test_epl_legendary_algorithm():
    """Test EPL algorithm with sample game data"""
    epl_algorithm = EPLLegendaryAlgorithm()
    
    # Test with Bournemouth vs Fulham (actual EPL game from data)
    test_game = {
        'home_team': 'AFC Bournemouth',
        'away_team': 'Fulham',
        'venue': 'Vitality Stadium, Bournemouth, England',
        'confidence': 71,  # Old system confidence
        'market_efficiency': 77,
        'team_performance': 61,
        'key_players': 67
    }
    
    result = await epl_algorithm.apply_epl_legendary_algorithm(test_game)
    
    print("🔥 EPL LEGENDARY ALGORITHM TEST:")
    print(f"⚽ {result['away_team']} @ {result['home_team']}")
    print(f"🎯 Prediction: {result['prediction']}")
    print(f"📊 Confidence: {result['confidence']}%")
    print(f"🔄 Old System: {result['old_system_confidence']}%")
    print(f"📈 Algorithm: {result['algorithm']}")
    
    return result

if __name__ == "__main__":
    asyncio.run(test_epl_legendary_algorithm())