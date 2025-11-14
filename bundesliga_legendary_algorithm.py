#!/usr/bin/env python3
"""
🇩🇪⚽ BUNDESLIGA LEGENDARY ALGORITHM - LIGA MX CLONE FOR GERMAN FOOTBALL 🔥💀

¡VÁMONOS BRODDER! CREATING BUNDESLIGA LEGENDARY ALGORITHM!
- Target: 80%+ accuracy (vs Liga MX 91.7%)
- Based on Liga MX proven 5-factor structure
- Enhanced with German football characteristics

BUNDESLIGA-SPECIFIC FACTORS:
- Der Klassiker supremacy (Bayern vs Dortmund)
- German engineering efficiency (tactics & fitness)
- 50+1 ownership rule (fan culture vs commercial power)
- Allianz Arena, Signal Iduna Park fortress effect
- Champions League pedigree (Bayern dominance)

LIGA MX SUCCESS STRUCTURE ADAPTED FOR GERMANY:
1. Recent Form (30% weight) - Bundesliga current form
2. Market Efficiency + Money Flow (25% weight) - BAYERN analysis  
3. Season Records (20% weight) - Bundesliga table position
4. Key Players + Injuries (15% weight) - Kane, Bellingham legacy, Haaland
5. Home Advantage Reduced (8% weight) - German venues
6. X-Factor Der Klassiker (2% weight) - Bayern vs BVB + German efficiency
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import json

logger = logging.getLogger(__name__)

class BundesligaLegendaryAlgorithm:
    """
    🇩🇪⚽ BUNDESLIGA LEGENDARY ALGORITHM - LIGA MX CLONE FOR GERMAN FOOTBALL
    
    Applies Liga MX 91.7% success structure to Bundesliga with German characteristics
    Target: 80%+ accuracy (matching EPL target)
    """
    
    def __init__(self):
        logger.info("🇩🇪⚽ BUNDESLIGA LEGENDARY ALGORITHM INITIALIZED - LIGA MX CLONE FOR GERMANY!")
    
    async def apply_bundesliga_legendary_algorithm(self, game_data: Dict) -> Dict:
        """
        🔥 APPLY BUNDESLIGA LEGENDARY ALGORITHM (LIGA MX CLONE)
        
        Bundesliga Liga MX Clone Structure:
        1. Recent Form (30% weight) - Bundesliga current team form
        2. Market Efficiency + Money Flow (25% weight) - BAYERN analysis  
        3. Season Records (20% weight) - Bundesliga table position
        4. Key Players + Injuries (15% weight) - German superstars
        5. Home Advantage Reduced (8% weight) - German venues (reduced like Liga MX)
        6. X-Factor Der Klassiker (2% weight) - Bayern vs BVB + German efficiency
        """
        try:
            home_team = game_data.get('home_team', 'Unknown')
            away_team = game_data.get('away_team', 'Unknown')
            
            # BUNDESLIGA LIGA MX CLONE Algorithm Implementation
            recent_form = await self._calculate_bundesliga_recent_form(game_data)
            bayern_money_flow = await self._calculate_bayern_money_flow(game_data)
            season_records = await self._calculate_bundesliga_season_records(game_data)
            key_players_injuries = await self._calculate_bundesliga_key_players_injuries(game_data)
            home_advantage_reduced = await self._calculate_german_home_advantage_reduced(game_data)
            x_factor_der_klassiker = await self._calculate_der_klassiker_x_factor(game_data)
            
            # BUNDESLIGA LIGA MX CLONE Formula (EXACT SAME WEIGHTS!)
            base_confidence = (
                recent_form * 0.30 +                    # 30% Recent Form
                bayern_money_flow * 0.25 +              # 25% Bayern Money Flow
                season_records * 0.20 +                 # 20% Season Records
                key_players_injuries * 0.15 +           # 15% Key Players + Injuries
                home_advantage_reduced * 0.08 +         # 8% Home Advantage (reduced)
                x_factor_der_klassiker * 0.02           # 2% X-Factor (Der Klassiker)
            )
            
            # Bundesliga Prediction Logic (German football characteristics)
            prediction, final_confidence = self._make_bundesliga_prediction(
                game_data, base_confidence, home_team, away_team
            )
            
            # Bundesliga Legendary Result Structure
            analyzed_game = {
                'home_team': home_team,
                'away_team': away_team,
                'prediction': prediction,
                'confidence': round(final_confidence, 1),
                'league': 'BUNDESLIGA',
                'algorithm': 'BUNDESLIGA_LEGENDARY_LIGA_MX_CLONE',
                
                # Bundesliga Liga MX Clone Factors
                'bundesliga_recent_form': recent_form,
                'bayern_money_flow': bayern_money_flow,
                'bundesliga_season_records': season_records,
                'bundesliga_key_players_injuries': key_players_injuries,
                'german_home_advantage_reduced': home_advantage_reduced,
                'der_klassiker_x_factor': x_factor_der_klassiker,
                
                'analysis_source': 'BUNDESLIGA_LEGENDARY_ALGORITHM',
                'country': 'Germany',
                'competition': 'Bundesliga',
                'venue': game_data.get('venue', 'German Stadium'),
                'date': datetime.now().strftime('%Y-%m-%d'),
                'timestamp': datetime.now(timezone.utc).isoformat(),
                
                # Comparison with targets
                'old_system_confidence': game_data.get('confidence', 0),
                'improvement_target': '80% accuracy (vs Liga MX 91.7%)',
                'german_football': True
            }
            
            logger.info(f"🇩🇪 {away_team} @ {home_team}: {prediction} ({final_confidence:.1f}%) [BUNDESLIGA LEGENDARY]")
            return analyzed_game
            
        except Exception as e:
            logger.error(f"Error applying Bundesliga legendary algorithm: {e}")
            return game_data

    async def _calculate_bundesliga_recent_form(self, game_data: Dict) -> float:
        """Calculate Bundesliga recent form (30% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # Bundesliga Recent Form Analysis (Liga MX style)
        elite_form = ['BAYERN MUNICH', 'BAYERN MUNCHEN', 'FC BAYERN']  # Bavarian dominance
        top_tier_form = ['BORUSSIA DORTMUND', 'RB LEIPZIG', 'BAYER LEVERKUSEN']  # Title contenders
        european_form = ['EINTRACHT FRANKFURT', 'UNION BERLIN', 'FREIBURG', 'WERDER BREMEN']  # European spots
        mid_table_form = ['BORUSSIA MONCHENGLADBACH', 'WOLFSBURG', 'HOFFENHEIM', 'MAINZ']
        struggling_form = ['SCHALKE', 'HERTHA BERLIN', 'GREUTHER FURTH', 'ARMINIA BIELEFELD']
        
        home_form = 50  # baseline
        away_form = 50  # baseline
        
        # Bundesliga Form Analysis
        if any(team in home_team for team in elite_form):
            home_form = 90  # Bayern level dominance
        elif any(team in home_team for team in top_tier_form):
            home_form = 80  # Dortmund, Leipzig, Leverkusen level
        elif any(team in home_team for team in european_form):
            home_form = 70  # European competition level
        elif any(team in home_team for team in mid_table_form):
            home_form = 60  # Mid-table form
        elif any(team in home_team for team in struggling_form):
            home_form = 40  # Struggling form
        
        if any(team in away_team for team in elite_form):
            away_form = 90
        elif any(team in away_team for team in top_tier_form):
            away_form = 80
        elif any(team in away_team for team in european_form):
            away_form = 70
        elif any(team in away_team for team in mid_table_form):
            away_form = 60
        elif any(team in away_team for team in struggling_form):
            away_form = 40
        
        # Liga MX style form calculation
        form_diff = abs(home_form - away_form)
        if form_diff > 35:
            return 88.0  # Massive Bundesliga form difference (Bayern vs lower)
        elif form_diff > 25:
            return 81.0  # Significant form difference
        elif form_diff > 15:
            return 73.0  # Moderate form difference
        else:
            return 65.0  # Similar form

    async def _calculate_bayern_money_flow(self, game_data: Dict) -> float:
        """Calculate Bayern money flow (25% weight - Liga MX KEY FACTOR adapted!)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        current_market = game_data.get('market_efficiency', 77)
        
        # BUNDESLIGA BAYERN MONEY FLOW ANALYSIS (Liga MX style!)
        bayern_teams = ['BAYERN MUNICH', 'BAYERN MUNCHEN', 'FC BAYERN']  # Financial dominance
        big_spenders = ['BORUSSIA DORTMUND', 'RB LEIPZIG']  # Major investment
        solid_finance = ['BAYER LEVERKUSEN', 'EINTRACHT FRANKFURT', 'WOLFSBURG']  # Stable finance
        
        home_money_flow = 50
        away_money_flow = 50
        
        # Money flow analysis (Bundesliga style)
        if any(team in home_team for team in bayern_teams):
            home_money_flow = 94  # Bayern Munich financial dominance
        elif any(team in home_team for team in big_spenders):
            home_money_flow = 78  # Dortmund/Leipzig level
        elif any(team in home_team for team in solid_finance):
            home_money_flow = 65  # Solid financial backing
        
        if any(team in away_team for team in bayern_teams):
            away_money_flow = 94
        elif any(team in away_team for team in big_spenders):
            away_money_flow = 78
        elif any(team in away_team for team in solid_finance):
            away_money_flow = 65
        
        # Combine market efficiency with Bayern money flow (Liga MX style)
        market_factor = min(current_market, 85)  # Cap market efficiency
        money_flow_avg = (home_money_flow + away_money_flow) / 2
        
        # Liga MX money flow formula adapted for Bundesliga
        combined_score = (market_factor * 0.6) + (money_flow_avg * 0.4)
        
        return min(combined_score, 88.0)  # Cap at 88% (Bayern dominance factor)

    async def _calculate_bundesliga_season_records(self, game_data: Dict) -> float:
        """Calculate Bundesliga season records (20% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # Bundesliga Season Performance Tiers (Liga MX style)
        title_race = ['BAYERN MUNICH', 'BAYERN MUNCHEN', 'FC BAYERN']  # Title favorites
        champions_league = ['BORUSSIA DORTMUND', 'RB LEIPZIG', 'BAYER LEVERKUSEN']  # CL spots
        europa_league = ['EINTRACHT FRANKFURT', 'UNION BERLIN', 'FREIBURG', 'WERDER BREMEN']  # European spots
        relegation_battle = ['SCHALKE', 'HERTHA BERLIN', 'GREUTHER FURTH', 'ARMINIA BIELEFELD']  # Bottom
        
        home_season = 50
        away_season = 50
        
        # Season records analysis (Liga MX structure)
        if any(team in home_team for team in title_race):
            home_season = 92  # Bayern title level
        elif any(team in home_team for team in champions_league):
            home_season = 79  # Champions League level
        elif any(team in home_team for team in europa_league):
            home_season = 67  # Europa League level
        elif any(team in home_team for team in relegation_battle):
            home_season = 38  # Relegation battle
        
        if any(team in away_team for team in title_race):
            away_season = 92
        elif any(team in away_team for team in champions_league):
            away_season = 79
        elif any(team in away_team for team in europa_league):
            away_season = 67
        elif any(team in away_team for team in relegation_battle):
            away_season = 38
        
        # Liga MX style season calculation
        season_diff = abs(home_season - away_season)
        if season_diff > 40:
            return 89.0  # Huge Bundesliga season gap (Bayern vs relegation)
        elif season_diff > 30:
            return 82.0  # Significant season gap
        elif season_diff > 20:
            return 74.0  # Moderate season gap
        else:
            return 66.0  # Similar season performance

    async def _calculate_bundesliga_key_players_injuries(self, game_data: Dict) -> float:
        """Calculate Bundesliga key players + injuries (15% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # BUNDESLIGA SUPERSTARS Impact + Injury Analysis
        superstar_impact = {
            'BAYERN MUNICH': 93,        # Kane, Musiala, Davies, Neuer
            'BORUSSIA DORTMUND': 81,    # Bellingham legacy, Haaland legacy, Reus
            'RB LEIPZIG': 74,           # Werner, Nkunku legacy, Szoboszlai legacy
            'BAYER LEVERKUSEN': 76,     # Wirtz, Diaby, Boniface
            'EINTRACHT FRANKFURT': 69,  # Marmoush, Götze
            'UNION BERLIN': 67,         # Becker, Trimmel
            'FREIBURG': 68,             # Grifo, Günter
            'WOLFSBURG': 66,            # Arnold, Wind
        }
        
        home_player_impact = superstar_impact.get(home_team, 55)
        away_player_impact = superstar_impact.get(away_team, 55)
        
        # Liga MX style key players calculation with injury factor
        player_avg = (home_player_impact + away_player_impact) / 2
        
        # Injury adjustment (Bundesliga specific)
        if player_avg > 90:
            return min(player_avg - 2, 92)  # Bayern level (injury risk)
        elif player_avg > 80:
            return min(player_avg - 1, 83)  # Dortmund level
        elif player_avg > 70:
            return min(player_avg + 1, 77)  # European level
        else:
            return min(player_avg + 3, 67)  # Lower teams benefit

    async def _calculate_german_home_advantage_reduced(self, game_data: Dict) -> float:
        """Calculate German home advantage reduced (8% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        venue = game_data.get('venue', '').upper()
        
        # Bundesliga Fortress Venues (Liga MX style but for Germany)
        fortress_venues = {
            'ALLIANZ ARENA': 87,           # Bayern Munich (75,000 capacity)
            'SIGNAL IDUNA PARK': 86,       # Borussia Dortmund (81,365 - largest)
            'RED BULL ARENA': 76,          # RB Leipzig
            'BAYARENA': 74,                # Bayer Leverkusen
            'COMMERZBANK-ARENA': 78,       # Eintracht Frankfurt
            'ALTE FORSTEREI': 82,          # Union Berlin (famous atmosphere)
            'EUROPA-PARK STADION': 73,     # Freiburg
        }
        
        # Check for fortress venues
        for venue_name, advantage in fortress_venues.items():
            if venue_name in venue or venue_name in home_team:
                return min(advantage, 87)  # Cap like Liga MX
        
        # Standard Bundesliga home advantage (reduced like Liga MX 8%)
        return 69.0  # Liga MX style reduced home advantage

    async def _calculate_der_klassiker_x_factor(self, game_data: Dict) -> float:
        """Calculate Der Klassiker X-Factor (2% weight - Liga MX secret adapted!)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # BUNDESLIGA X-Factor: Der Klassiker + German Efficiency + European Legacy (Liga MX style)
        
        # 1. DER KLASSIKER X-Factor (biggest rivalry in German football)
        der_klassiker_factor = 50
        if (('BAYERN' in home_team and 'DORTMUND' in away_team) or 
            ('DORTMUND' in home_team and 'BAYERN' in away_team)):
            der_klassiker_factor = 92  # MAXIMUM X-factor for Der Klassiker
        
        # 2. Ruhr Derby / Bavaria Derby
        elif (('DORTMUND' in home_team and 'SCHALKE' in away_team) or 
              ('SCHALKE' in home_team and 'DORTMUND' in away_team)):
            der_klassiker_factor = 84  # Ruhr Derby
        elif (('BAYERN' in home_team and 'AUGSBURG' in away_team) or 
              ('AUGSBURG' in home_team and 'BAYERN' in away_team)):
            der_klassiker_factor = 72  # Bavaria Derby
        
        # 3. German Efficiency Factor (tactical discipline)
        german_efficiency_teams = ['BAYERN MUNICH', 'BORUSSIA DORTMUND', 'RB LEIPZIG', 'BAYER LEVERKUSEN']
        home_efficient = any(team in home_team for team in german_efficiency_teams)
        away_efficient = any(team in away_team for team in german_efficiency_teams)
        
        efficiency_factor = 50
        if home_efficient and away_efficient:
            efficiency_factor = 80  # Both have German efficiency
        elif home_efficient or away_efficient:
            efficiency_factor = 67  # One has German efficiency
        
        # 4. European Competition Legacy Factor
        european_legacy_teams = ['BAYERN MUNICH', 'BORUSSIA DORTMUND', 'BAYER LEVERKUSEN', 'EINTRACHT FRANKFURT']
        home_european = any(team in home_team for team in european_legacy_teams)
        away_european = any(team in away_team for team in european_legacy_teams)
        
        european_factor = 50
        if home_european and away_european:
            european_factor = 76  # Both have European pedigree
        elif home_european or away_european:
            european_factor = 63  # One has European pedigree
        
        # Liga MX style X-Factor combination adapted for Bundesliga
        x_factor_score = (der_klassiker_factor * 0.5) + (efficiency_factor * 0.3) + (european_factor * 0.2)
        
        return min(x_factor_score, 92.0)  # High cap for Der Klassiker

    def _make_bundesliga_prediction(self, game_data: Dict, base_confidence: float, home_team: str, away_team: str) -> tuple:
        """Make Bundesliga-specific prediction based on German football characteristics"""
        
        # Bundesliga-specific adjustments
        german_efficiency_boost = 7.0  # German tactical efficiency boost
        
        # German football tends to be more tactical and possession-based
        if base_confidence > 82:
            # Strong favorite (likely Bayern Munich)
            stronger_team = self._get_stronger_bundesliga_team(home_team, away_team)
            return f"🏆 {stronger_team}", base_confidence + german_efficiency_boost + 12
        elif base_confidence > 72:
            # Moderate favorite  
            if self._is_der_klassiker(home_team, away_team):
                return "🔥 DER KLASSIKER BATTLE", base_confidence + german_efficiency_boost + 18
            elif self._is_german_home_advantage_significant(home_team):
                return f"🏠 {home_team}", base_confidence + german_efficiency_boost + 8
            else:
                stronger_team = self._get_stronger_bundesliga_team(home_team, away_team)
                return f"⚽ {stronger_team}", base_confidence + german_efficiency_boost + 6
        elif base_confidence > 62:
            # Close match - Bundesliga tactical battles
            return f"🏠 {home_team}", base_confidence + german_efficiency_boost + 4
        else:
            # Very close Bundesliga match
            return "🤝 UNENTSCHIEDEN", base_confidence + german_efficiency_boost  # German for "DRAW"

    def _get_stronger_bundesliga_team(self, home_team: str, away_team: str) -> str:
        """Determine stronger team based on Bundesliga hierarchy"""
        title_contenders = ['BAYERN MUNICH', 'BAYERN MUNCHEN', 'FC BAYERN']
        big_teams = ['BORUSSIA DORTMUND', 'RB LEIPZIG', 'BAYER LEVERKUSEN', 'EINTRACHT FRANKFURT']
        
        home_title = any(team in home_team.upper() for team in title_contenders)
        away_title = any(team in away_team.upper() for team in title_contenders)
        home_big = any(team in home_team.upper() for team in big_teams)
        away_big = any(team in away_team.upper() for team in big_teams)
        
        if home_title and not away_title:
            return home_team
        elif away_title and not home_title:
            return away_team
        elif home_big and not away_big:
            return home_team
        elif away_big and not home_big:
            return away_team
        else:
            # Similar level - prefer home
            return home_team

    def _is_der_klassiker(self, home_team: str, away_team: str) -> bool:
        """Check if this is Der Klassiker"""
        return (('BAYERN' in home_team.upper() and 'DORTMUND' in away_team.upper()) or
                ('DORTMUND' in home_team.upper() and 'BAYERN' in away_team.upper()))

    def _is_german_home_advantage_significant(self, home_team: str) -> bool:
        """Check if home team has significant German home advantage"""
        strong_home_teams = ['BAYERN MUNICH', 'BORUSSIA DORTMUND', 'RB LEIPZIG', 'UNION BERLIN']
        return any(team in home_team.upper() for team in strong_home_teams)

# Test function
async def test_bundesliga_legendary_algorithm():
    """Test Bundesliga algorithm with Der Klassiker and regular games"""
    bundesliga_algorithm = BundesligaLegendaryAlgorithm()
    
    # Test 1: DER KLASSIKER
    der_klassiker = {
        'home_team': 'Bayern Munich',
        'away_team': 'Borussia Dortmund',
        'venue': 'Allianz Arena, Munich, Germany',
        'market_efficiency': 84,
        'confidence': 78  # Old system baseline
    }
    
    result1 = await bundesliga_algorithm.apply_bundesliga_legendary_algorithm(der_klassiker)
    
    print("🔥 BUNDESLIGA LEGENDARY ALGORITHM TEST:")
    print(f"🇩🇪 DER KLASSIKER: {result1['away_team']} @ {result1['home_team']}")
    print(f"🎯 Prediction: {result1['prediction']}")
    print(f"📊 Confidence: {result1['confidence']}%")
    print(f"🔄 Old System: {result1['old_system_confidence']}%")
    print(f"💰 Bayern Money Flow: {result1['bayern_money_flow']}")
    print(f"🏆 Recent Form: {result1['bundesliga_recent_form']}")
    print(f"⚡ Der Klassiker X-Factor: {result1['der_klassiker_x_factor']}")
    print("---")
    
    # Test 2: Regular Bundesliga game
    regular_game = {
        'home_team': 'Eintracht Frankfurt',
        'away_team': 'RB Leipzig',
        'venue': 'Commerzbank-Arena',
        'market_efficiency': 71,
        'confidence': 64
    }
    
    result2 = await bundesliga_algorithm.apply_bundesliga_legendary_algorithm(regular_game)
    
    print(f"🇩🇪 REGULAR: {result2['away_team']} @ {result2['home_team']}")
    print(f"🎯 Prediction: {result2['prediction']}")
    print(f"📊 Confidence: {result2['confidence']}%")
    print(f"📈 Algorithm: {result2['algorithm']}")
    
    return result1, result2

if __name__ == "__main__":
    asyncio.run(test_bundesliga_legendary_algorithm())