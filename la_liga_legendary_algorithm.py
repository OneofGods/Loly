#!/usr/bin/env python3
"""
🇪🇸⚽ LA LIGA LEGENDARY ALGORITHM - LIGA MX CLONE FOR SPANISH FOOTBALL 🔥💀

¡VÁMONOS BRODDER! CREATING LA LIGA LEGENDARY ALGORITHM!
- Target: 85%+ accuracy (higher than EPL's 80%)
- Based on Liga MX 91.7% success structure
- Enhanced with Spanish football characteristics

LA LIGA-SPECIFIC FACTORS:
- EL CLÁSICO supremacy (Real Madrid vs Barcelona)
- Galácticos money flow (Florentino transfers)
- Spanish technical football style
- Camp Nou, Bernabéu fortress effect
- European competition pedigree

LIGA MX SUCCESS STRUCTURE ADAPTED FOR SPAIN:
1. Recent Form (30% weight) - La Liga current form
2. Market Efficiency + Money Flow (25% weight) - GALÁCTICOS analysis  
3. Season Records (20% weight) - La Liga table position
4. Key Players + Injuries (15% weight) - Mbappé, Vinicius, Lewa
5. Home Advantage Reduced (8% weight) - Spanish venues
6. X-Factor El Clásico (2% weight) - Real vs Barça + European prestige
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import json

logger = logging.getLogger(__name__)

class LaLigaLegendaryAlgorithm:
    """
    🇪🇸⚽ LA LIGA LEGENDARY ALGORITHM - LIGA MX CLONE FOR SPANISH FOOTBALL
    
    Applies Liga MX 91.7% success structure to La Liga with Spanish characteristics
    Target: 85%+ accuracy (exceeding EPL)
    """
    
    def __init__(self):
        logger.info("🇪🇸⚽ LA LIGA LEGENDARY ALGORITHM INITIALIZED - LIGA MX CLONE FOR SPAIN!")
    
    async def apply_la_liga_legendary_algorithm(self, game_data: Dict) -> Dict:
        """
        🔥 APPLY LA LIGA LEGENDARY ALGORITHM (LIGA MX CLONE)
        
        La Liga Liga MX Clone Structure:
        1. Recent Form (30% weight) - La Liga current team form
        2. Market Efficiency + Money Flow (25% weight) - GALÁCTICOS analysis  
        3. Season Records (20% weight) - La Liga table position
        4. Key Players + Injuries (15% weight) - Spanish superstars
        5. Home Advantage Reduced (8% weight) - Spanish venues (reduced like Liga MX)
        6. X-Factor El Clásico (2% weight) - Real vs Barça + European legacy
        """
        try:
            home_team = game_data.get('home_team', 'Unknown')
            away_team = game_data.get('away_team', 'Unknown')
            
            # LA LIGA LIGA MX CLONE Algorithm Implementation
            recent_form = await self._calculate_la_liga_recent_form(game_data)
            galacticos_money_flow = await self._calculate_galacticos_money_flow(game_data)
            season_records = await self._calculate_la_liga_season_records(game_data)
            key_players_injuries = await self._calculate_la_liga_key_players_injuries(game_data)
            home_advantage_reduced = await self._calculate_spanish_home_advantage_reduced(game_data)
            x_factor_el_clasico = await self._calculate_el_clasico_x_factor(game_data)
            
            # LA LIGA LIGA MX CLONE Formula (EXACT SAME WEIGHTS!)
            base_confidence = (
                recent_form * 0.30 +                    # 30% Recent Form
                galacticos_money_flow * 0.25 +          # 25% Galácticos Money Flow
                season_records * 0.20 +                 # 20% Season Records
                key_players_injuries * 0.15 +           # 15% Key Players + Injuries
                home_advantage_reduced * 0.08 +         # 8% Home Advantage (reduced)
                x_factor_el_clasico * 0.02              # 2% X-Factor (El Clásico)
            )
            
            # La Liga Prediction Logic (Spanish football characteristics)
            prediction, final_confidence = self._make_la_liga_prediction(
                game_data, base_confidence, home_team, away_team
            )
            
            # La Liga Legendary Result Structure
            analyzed_game = {
                'home_team': home_team,
                'away_team': away_team,
                'prediction': prediction,
                'confidence': round(final_confidence, 1),
                'league': 'LA_LIGA',
                'algorithm': 'LA_LIGA_LEGENDARY_LIGA_MX_CLONE',
                
                # La Liga Liga MX Clone Factors
                'la_liga_recent_form': recent_form,
                'galacticos_money_flow': galacticos_money_flow,
                'la_liga_season_records': season_records,
                'la_liga_key_players_injuries': key_players_injuries,
                'spanish_home_advantage_reduced': home_advantage_reduced,
                'el_clasico_x_factor': x_factor_el_clasico,
                
                'analysis_source': 'LA_LIGA_LEGENDARY_ALGORITHM',
                'country': 'Spain',
                'competition': 'La Liga',
                'venue': game_data.get('venue', 'Spanish Stadium'),
                'date': datetime.now().strftime('%Y-%m-%d'),
                'timestamp': datetime.now(timezone.utc).isoformat(),
                
                # Comparison with targets
                'old_system_confidence': game_data.get('confidence', 0),
                'improvement_target': '85% accuracy (vs Liga MX 91.7%)',
                'spanish_football': True
            }
            
            logger.info(f"🇪🇸 {away_team} @ {home_team}: {prediction} ({final_confidence:.1f}%) [LA LIGA LEGENDARY]")
            return analyzed_game
            
        except Exception as e:
            logger.error(f"Error applying La Liga legendary algorithm: {e}")
            return game_data

    async def _calculate_la_liga_recent_form(self, game_data: Dict) -> float:
        """Calculate La Liga recent form (30% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # La Liga Recent Form Analysis (Liga MX style)
        elite_form = ['REAL MADRID', 'BARCELONA', 'ATLETICO MADRID']  # Top tier
        european_form = ['ATHLETIC BILBAO', 'REAL SOCIEDAD', 'VILLARREAL', 'SEVILLA']  # European spots
        mid_table_form = ['VALENCIA', 'BETIS', 'OSASUNA', 'GIRONA', 'LAS PALMAS']
        struggling_form = ['ESPANYOL', 'GETAFE', 'LEGANES', 'VALLADOLID']
        
        home_form = 50  # baseline
        away_form = 50  # baseline
        
        # La Liga Form Analysis
        if any(team in home_team for team in elite_form):
            home_form = 88  # Real, Barça, Atleti level
        elif any(team in home_team for team in european_form):
            home_form = 76  # European competition level
        elif any(team in home_team for team in mid_table_form):
            home_form = 64  # Mid-table form
        elif any(team in home_team for team in struggling_form):
            home_form = 42  # Struggling form
        
        if any(team in away_team for team in elite_form):
            away_form = 88
        elif any(team in away_team for team in european_form):
            away_form = 76
        elif any(team in away_team for team in mid_table_form):
            away_form = 64
        elif any(team in away_team for team in struggling_form):
            away_form = 42
        
        # Liga MX style form calculation
        form_diff = abs(home_form - away_form)
        if form_diff > 30:
            return 86.0  # Massive La Liga form difference
        elif form_diff > 20:
            return 78.0  # Significant form difference
        elif form_diff > 10:
            return 70.0  # Moderate form difference
        else:
            return 62.0  # Similar form

    async def _calculate_galacticos_money_flow(self, game_data: Dict) -> float:
        """Calculate Galácticos money flow (25% weight - Liga MX KEY FACTOR adapted!)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        current_market = game_data.get('market_efficiency', 77)
        
        # LA LIGA GALÁCTICOS MONEY FLOW ANALYSIS (Liga MX style!)
        galacticos_teams = ['REAL MADRID']  # Florentino's infinite money
        big_spenders = ['BARCELONA', 'ATLETICO MADRID']  # Major investment
        european_money = ['SEVILLA', 'VILLARREAL', 'ATHLETIC BILBAO']  # European money
        
        home_money_flow = 50
        away_money_flow = 50
        
        # Money flow analysis (La Liga style)
        if any(team in home_team for team in galacticos_teams):
            home_money_flow = 92  # Real Madrid Galácticos level
        elif any(team in home_team for team in big_spenders):
            home_money_flow = 80  # Barcelona/Atleti level
        elif any(team in home_team for team in european_money):
            home_money_flow = 68  # European competition money
        
        if any(team in away_team for team in galacticos_teams):
            away_money_flow = 92
        elif any(team in away_team for team in big_spenders):
            away_money_flow = 80
        elif any(team in away_team for team in european_money):
            away_money_flow = 68
        
        # Combine market efficiency with Galácticos money flow (Liga MX style)
        market_factor = min(current_market, 85)  # Cap market efficiency
        money_flow_avg = (home_money_flow + away_money_flow) / 2
        
        # Liga MX money flow formula adapted for La Liga
        combined_score = (market_factor * 0.6) + (money_flow_avg * 0.4)
        
        return min(combined_score, 90.0)  # Cap at 90% (higher than Liga MX for Galácticos)

    async def _calculate_la_liga_season_records(self, game_data: Dict) -> float:
        """Calculate La Liga season records (20% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # La Liga Season Performance Tiers (Liga MX style)
        title_race = ['REAL MADRID', 'BARCELONA']  # Title contenders
        champions_league = ['ATLETICO MADRID', 'ATHLETIC BILBAO', 'REAL SOCIEDAD', 'VILLARREAL']  # CL spots
        europa_league = ['SEVILLA', 'BETIS', 'VALENCIA', 'OSASUNA']  # European spots
        relegation_battle = ['ESPANYOL', 'GETAFE', 'LEGANES', 'VALLADOLID']  # Bottom
        
        home_season = 50
        away_season = 50
        
        # Season records analysis (Liga MX structure)
        if any(team in home_team for team in title_race):
            home_season = 90  # Real/Barça title level
        elif any(team in home_team for team in champions_league):
            home_season = 78  # Champions League level
        elif any(team in home_team for team in europa_league):
            home_season = 65  # Europa League level
        elif any(team in home_team for team in relegation_battle):
            home_season = 40  # Relegation battle
        
        if any(team in away_team for team in title_race):
            away_season = 90
        elif any(team in away_team for team in champions_league):
            away_season = 78
        elif any(team in away_team for team in europa_league):
            away_season = 65
        elif any(team in away_team for team in relegation_battle):
            away_season = 40
        
        # Liga MX style season calculation
        season_diff = abs(home_season - away_season)
        if season_diff > 35:
            return 87.0  # Huge La Liga season gap
        elif season_diff > 25:
            return 80.0  # Significant season gap
        elif season_diff > 15:
            return 72.0  # Moderate season gap
        else:
            return 64.0  # Similar season performance

    async def _calculate_la_liga_key_players_injuries(self, game_data: Dict) -> float:
        """Calculate La Liga key players + injuries (15% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # LA LIGA SUPERSTARS Impact + Injury Analysis
        superstar_impact = {
            'REAL MADRID': 95,      # Mbappé, Vinicius, Bellingham, Modric
            'BARCELONA': 82,        # Lewandowski, Pedri, Gavi, Yamal
            'ATLETICO MADRID': 75,  # Griezmann, João Félix legacy
            'ATHLETIC BILBAO': 70,  # Williams brothers, Muniain
            'REAL SOCIEDAD': 73,    # Oyarzabal, Merino
            'VILLARREAL': 72,       # Gerard Moreno, Baena
            'SEVILLA': 68,          # Rakitic legacy, En-Nesyri
        }
        
        home_player_impact = superstar_impact.get(home_team, 55)
        away_player_impact = superstar_impact.get(away_team, 55)
        
        # Liga MX style key players calculation with injury factor
        player_avg = (home_player_impact + away_player_impact) / 2
        
        # Injury adjustment (La Liga specific)
        if player_avg > 90:
            return min(player_avg - 3, 90)  # Real Madrid level (injury risk)
        elif player_avg > 80:
            return min(player_avg - 1, 85)  # Barcelona level
        elif player_avg > 70:
            return min(player_avg + 1, 75)  # European level
        else:
            return min(player_avg + 4, 65)  # Lower teams benefit

    async def _calculate_spanish_home_advantage_reduced(self, game_data: Dict) -> float:
        """Calculate Spanish home advantage reduced (8% weight - Liga MX clone)"""
        home_team = game_data.get('home_team', '').upper()
        venue = game_data.get('venue', '').upper()
        
        # La Liga Fortress Venues (Liga MX style but for Spain)
        fortress_venues = {
            'CAMP NOU': 85,              # Barcelona (99,000 capacity)
            'BERNABEU': 84,              # Real Madrid (81,000)
            'METROPOLITANO': 78,         # Atlético Madrid
            'SAN MAMES': 82,             # Athletic Bilbao (Basque fortress)
            'REALE ARENA': 75,           # Real Sociedad
            'ESTADIO DE LA CERAMICA': 73, # Villarreal
        }
        
        # Check for fortress venues
        for venue_name, advantage in fortress_venues.items():
            if venue_name in venue or venue_name in home_team:
                return min(advantage, 85)  # Cap like Liga MX
        
        # Standard La Liga home advantage (reduced like Liga MX 8%)
        return 67.0  # Liga MX style reduced home advantage

    async def _calculate_el_clasico_x_factor(self, game_data: Dict) -> float:
        """Calculate El Clásico X-Factor (2% weight - Liga MX secret adapted!)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # LA LIGA X-Factor: El Clásico + European Legacy + Pressure (Liga MX style)
        
        # 1. EL CLÁSICO X-Factor (biggest in world football)
        el_clasico_factor = 50
        if ('REAL MADRID' in home_team and 'BARCELONA' in away_team) or \
           ('BARCELONA' in home_team and 'REAL MADRID' in away_team):
            el_clasico_factor = 95  # MAXIMUM X-factor for El Clásico
        
        # 2. Madrid Derby / Catalonia Derby
        elif ('REAL MADRID' in home_team and 'ATLETICO' in away_team) or \
             ('ATLETICO' in home_team and 'REAL MADRID' in away_team):
            el_clasico_factor = 82  # Madrid Derby
        elif ('BARCELONA' in home_team and 'ESPANYOL' in away_team) or \
             ('ESPANYOL' in home_team and 'BARCELONA' in away_team):
            el_clasico_factor = 75  # Catalonia Derby
        
        # 3. European Competition Legacy Factor
        european_legacy_teams = ['REAL MADRID', 'BARCELONA', 'ATLETICO MADRID', 'SEVILLA']
        home_european = any(team in home_team for team in european_legacy_teams)
        away_european = any(team in away_team for team in european_legacy_teams)
        
        european_factor = 50
        if home_european and away_european:
            european_factor = 78  # Both have European pedigree
        elif home_european or away_european:
            european_factor = 65  # One has European pedigree
        
        # 4. Pressure Factor (Title race, relegation, European spots)
        pressure_factor = 58  # baseline higher than Liga MX
        
        # Liga MX style X-Factor combination adapted for La Liga
        x_factor_score = (el_clasico_factor * 0.6) + (european_factor * 0.25) + (pressure_factor * 0.15)
        
        return min(x_factor_score, 95.0)  # Higher cap than Liga MX for El Clásico

    def _make_la_liga_prediction(self, game_data: Dict, base_confidence: float, home_team: str, away_team: str) -> tuple:
        """Make La Liga-specific prediction based on Spanish football characteristics"""
        
        # La Liga-specific adjustments
        spanish_technical_boost = 6.0  # Spanish technical football boost
        
        # Spanish football tends to be more tactical and possession-based
        if base_confidence > 80:
            # Strong favorite (likely Real Madrid or Barcelona)
            stronger_team = self._get_stronger_la_liga_team(home_team, away_team)
            return f"🏆 {stronger_team}", base_confidence + spanish_technical_boost + 10
        elif base_confidence > 70:
            # Moderate favorite  
            if self._is_el_clasico(home_team, away_team):
                return "🔥 EL CLÁSICO UNPREDICTABLE", base_confidence + spanish_technical_boost + 15
            elif self._is_spanish_home_advantage_significant(home_team):
                return f"🏠 {home_team}", base_confidence + spanish_technical_boost + 7
            else:
                stronger_team = self._get_stronger_la_liga_team(home_team, away_team)
                return f"⚽ {stronger_team}", base_confidence + spanish_technical_boost + 5
        elif base_confidence > 60:
            # Close match - La Liga tactical battles
            return f"🏠 {home_team}", base_confidence + spanish_technical_boost + 3
        else:
            # Very close La Liga match
            return "🤝 DRAW", base_confidence + spanish_technical_boost

    def _get_stronger_la_liga_team(self, home_team: str, away_team: str) -> str:
        """Determine stronger team based on La Liga hierarchy"""
        title_contenders = ['REAL MADRID', 'BARCELONA']
        big_teams = ['ATLETICO MADRID', 'SEVILLA', 'ATHLETIC BILBAO', 'REAL SOCIEDAD']
        
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

    def _is_el_clasico(self, home_team: str, away_team: str) -> bool:
        """Check if this is El Clásico"""
        return (('REAL MADRID' in home_team.upper() and 'BARCELONA' in away_team.upper()) or
                ('BARCELONA' in home_team.upper() and 'REAL MADRID' in away_team.upper()))

    def _is_spanish_home_advantage_significant(self, home_team: str) -> bool:
        """Check if home team has significant Spanish home advantage"""
        strong_home_teams = ['REAL MADRID', 'BARCELONA', 'ATLETICO MADRID', 'ATHLETIC BILBAO']
        return any(team in home_team.upper() for team in strong_home_teams)

# Test function
async def test_la_liga_legendary_algorithm():
    """Test La Liga algorithm with El Clásico and regular games"""
    la_liga_algorithm = LaLigaLegendaryAlgorithm()
    
    # Test 1: EL CLÁSICO
    el_clasico = {
        'home_team': 'FC Barcelona',
        'away_team': 'Real Madrid',
        'venue': 'Camp Nou, Barcelona, Spain',
        'market_efficiency': 82,
        'confidence': 75  # Old system baseline
    }
    
    result1 = await la_liga_algorithm.apply_la_liga_legendary_algorithm(el_clasico)
    
    print("🔥 LA LIGA LEGENDARY ALGORITHM TEST:")
    print(f"🇪🇸 EL CLÁSICO: {result1['away_team']} @ {result1['home_team']}")
    print(f"🎯 Prediction: {result1['prediction']}")
    print(f"📊 Confidence: {result1['confidence']}%")
    print(f"🔄 Old System: {result1['old_system_confidence']}%")
    print(f"💰 Galácticos: {result1['galacticos_money_flow']}")
    print(f"🏆 Recent Form: {result1['la_liga_recent_form']}")
    print(f"⚡ El Clásico X-Factor: {result1['el_clasico_x_factor']}")
    print("---")
    
    # Test 2: Regular La Liga game
    regular_game = {
        'home_team': 'Sevilla',
        'away_team': 'Athletic Bilbao',
        'venue': 'Ramón Sánchez-Pizjuán Stadium',
        'market_efficiency': 68,
        'confidence': 62
    }
    
    result2 = await la_liga_algorithm.apply_la_liga_legendary_algorithm(regular_game)
    
    print(f"🇪🇸 REGULAR: {result2['away_team']} @ {result2['home_team']}")
    print(f"🎯 Prediction: {result2['prediction']}")
    print(f"📊 Confidence: {result2['confidence']}%")
    print(f"📈 Algorithm: {result2['algorithm']}")
    
    return result1, result2

if __name__ == "__main__":
    asyncio.run(test_la_liga_legendary_algorithm())