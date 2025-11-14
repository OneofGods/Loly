#!/usr/bin/env python3
"""
⚽🌍 UEFA WORLD CUP QUALIFIERS ALGORITHM - INTERNATIONAL FOOTBALL SPECIALIST 🔥💀

BASED ON INTERNATIONAL FOOTBALL PATTERNS AND ANALYSIS:
- FIFA World Rankings (30% weight) - Elite nations vs developing nations
- World Cup Qualification History (25% weight) - Always qualify vs struggle teams
- International Tournament Experience (20% weight) - Euro, Nations League performance
- Home Nation Support (15% weight) - Passionate crowds for smaller nations
- Current FIFA Form (10% weight) - Recent international results

UEFA WORLD CUP QUALIFICATION FACTORS DISCOVERED:
1. FIFA World Rankings: Elite nations (France, England, Spain) vs developing (Malta, San Marino)
2. World Cup History: Teams like Germany, Italy always qualify vs nations that struggle
3. Tournament Experience: Euro experience, Nations League performance impact
4. Home Support: Smaller nations get massive boost when hosting elite teams
5. Current Form: Recent FIFA window results and momentum

REGIONAL RIVALRY ANALYSIS:
- England vs Scotland: Classic British rivalry intensity
- Spain vs Portugal: Iberian Peninsula battles
- Italy vs France: Mediterranean power struggle
- Germany vs Netherlands: Northern European dominance
- Turkey vs Greece: Eastern Mediterranean tension

WORLD CUP PRESSURE FACTORS:
- Teams close to qualifying vs teams already qualified/eliminated
- Qualification group stage vs playoff rounds
- Must-win scenarios for smaller nations
- Elite teams managing squad rotation

Created: November 11, 2025
Based on: EPL Legendary Algorithm + UEFA Champions League Algorithm patterns
Target Accuracy: 85%+ (International Football Specialist)
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import json
import random

# Import Enhanced Prediction Engine for international football bias fixes
try:
    from ai_enhanced_prediction_engine import AIEnhancedPredictionEngine
except ImportError:
    class AIEnhancedPredictionEngine:
        def make_enhanced_prediction(self, game_data, base_confidence, home_team, away_team):
            return f"🏠 {home_team}", base_confidence  # Fallback

logger = logging.getLogger(__name__)

class UEFAWorldCupQualifiersAlgorithm:
    """
    ⚽🌍 UEFA WORLD CUP QUALIFIERS ALGORITHM - INTERNATIONAL FOOTBALL SPECIALIST
    
    Applies international football-specific analysis patterns to achieve 85%+ accuracy
    Based on FIFA rankings, World Cup history, and European qualification dynamics
    Includes regional rivalries, home nation support, and qualification pressure analysis
    """
    
    def __init__(self):
        logger.info("⚽🌍 UEFA WORLD CUP QUALIFIERS ALGORITHM INITIALIZED - TARGET: 85%+ ACCURACY!")
        
        # Initialize Enhanced Prediction Engine for international football
        self.enhanced_predictor = AIEnhancedPredictionEngine()
        
        # FIFA WORLD RANKINGS TIERS (2024-2025 data)
        self.fifa_elite_nations = [
            'FRANCE', 'ENGLAND', 'SPAIN', 'GERMANY', 'ITALY', 'PORTUGAL', 
            'NETHERLANDS', 'BELGIUM', 'CROATIA', 'DENMARK'
        ]
        
        self.fifa_strong_nations = [
            'SWITZERLAND', 'AUSTRIA', 'POLAND', 'UKRAINE', 'SWEDEN', 
            'NORWAY', 'CZECH REPUBLIC', 'TURKEY', 'RUSSIA', 'SERBIA'
        ]
        
        self.fifa_moderate_nations = [
            'SCOTLAND', 'WALES', 'REPUBLIC OF IRELAND', 'SLOVAKIA', 'SLOVENIA', 
            'FINLAND', 'BOSNIA AND HERZEGOVINA', 'NORTH MACEDONIA', 'ALBANIA', 'MONTENEGRO'
        ]
        
        self.fifa_developing_nations = [
            'MALTA', 'SAN MARINO', 'ANDORRA', 'LIECHTENSTEIN', 'GIBRALTAR',
            'FAROE ISLANDS', 'ESTONIA', 'LATVIA', 'LITHUANIA', 'LUXEMBOURG'
        ]
        
        # WORLD CUP QUALIFICATION HISTORY (1990-2022)
        self.always_qualify_teams = [
            'GERMANY', 'FRANCE', 'SPAIN', 'ENGLAND', 'ITALY', 'NETHERLANDS',
            'PORTUGAL', 'BELGIUM'
        ]
        
        self.regular_qualifiers = [
            'DENMARK', 'SWITZERLAND', 'AUSTRIA', 'POLAND', 'CROATIA',
            'SWEDEN', 'CZECH REPUBLIC', 'NORWAY'
        ]
        
        self.struggle_to_qualify = [
            'SCOTLAND', 'WALES', 'REPUBLIC OF IRELAND', 'TURKEY', 'UKRAINE',
            'SERBIA', 'SLOVAKIA', 'FINLAND'
        ]
        
        self.rarely_qualify = [
            'BOSNIA AND HERZEGOVINA', 'NORTH MACEDONIA', 'ALBANIA', 'MONTENEGRO',
            'SLOVENIA', 'ESTONIA', 'LATVIA', 'LITHUANIA'
        ]
        
        # EUROPEAN TOURNAMENT EXPERIENCE (Euro + Nations League)
        self.tournament_veterans = [
            'FRANCE', 'GERMANY', 'SPAIN', 'ITALY', 'PORTUGAL', 'NETHERLANDS',
            'ENGLAND', 'BELGIUM', 'CROATIA', 'DENMARK'
        ]
        
        self.tournament_regulars = [
            'SWITZERLAND', 'AUSTRIA', 'POLAND', 'CZECH REPUBLIC', 'SWEDEN',
            'UKRAINE', 'TURKEY', 'WALES', 'SCOTLAND'
        ]
        
        # REGIONAL RIVALRIES (High intensity matchups)
        self.major_rivalries = [
            ('ENGLAND', 'SCOTLAND'),  # Classic British rivalry
            ('SPAIN', 'PORTUGAL'),    # Iberian Peninsula
            ('ITALY', 'FRANCE'),      # Mediterranean powers
            ('GERMANY', 'NETHERLANDS'), # Northern European
            ('TURKEY', 'GREECE'),     # Eastern Mediterranean
            ('POLAND', 'RUSSIA'),     # Eastern European tension
            ('SERBIA', 'ALBANIA'),    # Balkan intensity
            ('CROATIA', 'SERBIA'),    # Former Yugoslavia
        ]
        
        # HOME NATION SUPPORT INTENSITY (Crowd impact)
        self.passionate_home_crowds = [
            'TURKEY', 'GREECE', 'SCOTLAND', 'WALES', 'REPUBLIC OF IRELAND',
            'SERBIA', 'ALBANIA', 'BOSNIA AND HERZEGOVINA', 'NORTH MACEDONIA',
            'MONTENEGRO', 'POLAND', 'UKRAINE', 'CROATIA'
        ]
        
        # FORTRESS HOME VENUES (Difficult for visitors)
        self.fortress_venues = {
            'WEMBLEY': 85,          # England - Wembley Stadium
            'STADE DE FRANCE': 82,  # France - Saint-Denis
            'ALLIANZ ARENA': 80,    # Germany - Munich
            'SAN SIRO': 78,         # Italy - Milan
            'ESTADIO DA LUZ': 76,   # Portugal - Lisbon
            'JOHAN CRUIJFF': 75,    # Netherlands - Amsterdam
            'HAMPDEN PARK': 88,     # Scotland - Glasgow (massive home support)
            'MILLENNIUM': 85,       # Wales - Cardiff
            'AVIVA STADIUM': 82,    # Ireland - Dublin
            'SUKRU SARACOGLU': 90,  # Turkey - Istanbul (incredible atmosphere)
        }
    
    async def apply_uefa_wc_qualifiers_algorithm(self, game_data: Dict) -> Dict:
        """
        🔥 APPLY UEFA WORLD CUP QUALIFIERS ALGORITHM TO INTERNATIONAL GAME
        
        UEFA WC Qualifiers Success Formula:
        1. FIFA World Rankings (30% weight) - Elite vs developing nations analysis
        2. World Cup Qualification History (25% weight) - Always qualify vs struggle teams
        3. International Tournament Experience (20% weight) - Euro + Nations League
        4. Home Nation Support (15% weight) - Passionate crowds for smaller nations
        5. Current FIFA Form (10% weight) - Recent international window results
        """
        try:
            home_team = game_data.get('home_team', 'Unknown')
            away_team = game_data.get('away_team', 'Unknown')
            
            # UEFA WORLD CUP QUALIFIERS Algorithm Implementation
            fifa_rankings_factor = await self._calculate_fifa_rankings_factor(game_data)
            wc_qualification_history = await self._calculate_wc_qualification_history(game_data)
            tournament_experience = await self._calculate_tournament_experience(game_data)
            home_nation_support = await self._calculate_home_nation_support(game_data)
            current_fifa_form = await self._calculate_current_fifa_form(game_data)
            
            # UEFA WC Qualifiers Formula (International Football Specialist)
            base_confidence = (
                fifa_rankings_factor * 0.30 +          # 30% FIFA World Rankings
                wc_qualification_history * 0.25 +      # 25% WC Qualification History
                tournament_experience * 0.20 +         # 20% Tournament Experience
                home_nation_support * 0.15 +           # 15% Home Nation Support
                current_fifa_form * 0.10               # 10% Current FIFA Form
            )
            
            # Enhanced Prediction Logic for international football
            # Create base prediction data for AI enhancement
            base_prediction_data = {
                'prediction': f"🏠 {home_team}",  # Default home prediction
                'confidence': base_confidence,
                'reasoning': f'UEFA WC Qualifiers analysis: FIFA({fifa_rankings_factor:.1f}) WC History({wc_qualification_history:.1f}) Tournament Exp({tournament_experience:.1f})',
                'home_team': home_team,
                'away_team': away_team
            }
            
            # Get AI enhanced prediction
            try:
                enhanced_result = await self.enhanced_predictor.enhance_prediction(
                    'UEFA_WORLD_CUP_QUALIFIERS', home_team, away_team, base_prediction_data
                )
                prediction = enhanced_result.get('enhanced_prediction', f"🏠 {home_team}")
                final_confidence = enhanced_result.get('final_confidence', base_confidence)
            except Exception as e:
                logger.warning(f"AI enhancement failed, using base prediction: {e}")
                prediction = f"🏠 {home_team}"
                final_confidence = base_confidence
            
            # Apply international football specific adjustments
            prediction, final_confidence = self._apply_international_adjustments(
                prediction, final_confidence, home_team, away_team, game_data,
                fifa_rankings_factor, wc_qualification_history, home_nation_support
            )
            
            # Cap confidence at 90% (no 95% values as requested)
            final_confidence = min(final_confidence, 90.0)
            
            # UEFA World Cup Qualifiers Result Structure
            analyzed_game = {
                'home_team': home_team,
                'away_team': away_team,
                'prediction': prediction,
                'confidence': round(final_confidence, 1),
                'league': 'UEFA_WORLD_CUP_QUALIFIERS',
                'algorithm': 'UEFA_WC_QUALIFIERS_INTERNATIONAL_SPECIALIST',
                
                # UEFA WC Qualifiers Factors
                'fifa_rankings_factor': fifa_rankings_factor,
                'wc_qualification_history': wc_qualification_history,
                'tournament_experience': tournament_experience,
                'home_nation_support': home_nation_support,
                'current_fifa_form': current_fifa_form,
                
                'analysis_source': 'UEFA_WC_QUALIFIERS_ALGORITHM',
                'country': 'Europe',
                'competition': 'UEFA World Cup Qualifiers',
                'venue': game_data.get('venue', 'International Stadium'),
                'date': datetime.now().strftime('%Y-%m-%d'),
                'timestamp': datetime.now(timezone.utc).isoformat(),
                
                # International football specific data
                'regional_rivalry': self._detect_regional_rivalry(home_team, away_team),
                'qualification_pressure': self._detect_qualification_pressure(game_data),
                'home_crowd_intensity': self._calculate_crowd_intensity(home_team),
                
                'old_system_confidence': game_data.get('confidence', 0),
                'improvement_target': '85% accuracy (International Football Specialist)',
                'international_football': True
            }
            
            logger.info(f"⚽ {away_team} @ {home_team}: {prediction} ({final_confidence:.1f}%) [UEFA WC Qualifiers]")
            return analyzed_game
            
        except Exception as e:
            logger.error(f"Error applying UEFA WC Qualifiers algorithm: {e}")
            return game_data

    async def _calculate_fifa_rankings_factor(self, game_data: Dict) -> float:
        """Calculate FIFA World Rankings factor (30% weight - Elite vs developing nations)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # FIFA Rankings Analysis (Elite nations vs developing)
        home_tier = self._get_fifa_tier(home_team)
        away_tier = self._get_fifa_tier(away_team)
        
        # Calculate ranking advantage
        tier_diff = abs(home_tier - away_tier)
        
        if tier_diff >= 3:
            # Massive FIFA ranking gap (Elite vs Developing)
            return 88.0  # Clear favorite based on FIFA rankings
        elif tier_diff == 2:
            # Significant FIFA ranking gap (Elite vs Moderate, Strong vs Developing)
            return 82.0  # Strong ranking advantage
        elif tier_diff == 1:
            # Moderate FIFA ranking gap (Elite vs Strong, Strong vs Moderate)
            return 75.0  # Moderate ranking advantage
        else:
            # Similar FIFA rankings (same tier teams)
            return 65.0  # Rankings don't provide clear advantage

    def _get_fifa_tier(self, team: str) -> int:
        """Get FIFA tier for team (1=Elite, 2=Strong, 3=Moderate, 4=Developing)"""
        if any(elite in team for elite in self.fifa_elite_nations):
            return 1  # Elite nations
        elif any(strong in team for strong in self.fifa_strong_nations):
            return 2  # Strong nations
        elif any(moderate in team for moderate in self.fifa_moderate_nations):
            return 3  # Moderate nations
        else:
            return 4  # Developing nations

    async def _calculate_wc_qualification_history(self, game_data: Dict) -> float:
        """Calculate World Cup qualification history (25% weight - Always qualify vs struggle)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # World Cup Qualification History Analysis
        home_wc_tier = self._get_wc_qualification_tier(home_team)
        away_wc_tier = self._get_wc_qualification_tier(away_team)
        
        # Calculate WC qualification advantage
        tier_diff = abs(home_wc_tier - away_wc_tier)
        
        if tier_diff >= 3:
            # Always qualify vs rarely qualify
            return 85.0  # Massive WC qualification experience gap
        elif tier_diff == 2:
            # Always qualify vs struggle, or regular vs rarely qualify
            return 78.0  # Significant WC qualification advantage
        elif tier_diff == 1:
            # Adjacent tiers
            return 70.0  # Moderate WC qualification advantage
        else:
            # Same WC qualification tier
            return 62.0  # Similar WC qualification history

    def _get_wc_qualification_tier(self, team: str) -> int:
        """Get WC qualification tier (1=Always, 2=Regular, 3=Struggle, 4=Rarely)"""
        if any(always in team for always in self.always_qualify_teams):
            return 1  # Always qualify for World Cup
        elif any(regular in team for regular in self.regular_qualifiers):
            return 2  # Regular World Cup qualifiers
        elif any(struggle in team for struggle in self.struggle_to_qualify):
            return 3  # Struggle to qualify for World Cup
        else:
            return 4  # Rarely qualify for World Cup

    async def _calculate_tournament_experience(self, game_data: Dict) -> float:
        """Calculate international tournament experience (20% weight - Euro + Nations League)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # Tournament Experience Analysis
        home_tournament_tier = self._get_tournament_experience_tier(home_team)
        away_tournament_tier = self._get_tournament_experience_tier(away_team)
        
        # Calculate tournament experience advantage
        tier_diff = abs(home_tournament_tier - away_tournament_tier)
        
        if tier_diff >= 2:
            # Veterans vs inexperienced
            return 80.0  # Major tournament experience gap
        elif tier_diff == 1:
            # Veterans vs regulars, or regulars vs inexperienced
            return 72.0  # Moderate tournament experience advantage
        else:
            # Similar tournament experience
            return 64.0  # Similar international tournament background

    def _get_tournament_experience_tier(self, team: str) -> int:
        """Get tournament experience tier (1=Veterans, 2=Regulars, 3=Inexperienced)"""
        if any(veteran in team for veteran in self.tournament_veterans):
            return 1  # Tournament veterans (Euro + Nations League regulars)
        elif any(regular in team for regular in self.tournament_regulars):
            return 2  # Tournament regulars (occasional Euro participants)
        else:
            return 3  # Limited tournament experience

    async def _calculate_home_nation_support(self, game_data: Dict) -> float:
        """Calculate home nation support (15% weight - Passionate crowds for smaller nations)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        venue = game_data.get('venue', '').upper()
        
        # Home Nation Support Analysis (Smaller nations get bigger boost vs elite teams)
        home_crowd_intensity = self._calculate_crowd_intensity(home_team)
        
        # Check for fortress venues
        venue_boost = 0
        for venue_name, advantage in self.fortress_venues.items():
            if venue_name in venue:
                venue_boost = (advantage - 70) / 2  # Convert venue advantage to boost
                break
        
        # Elite teams visiting smaller nations face hostile crowds
        home_fifa_tier = self._get_fifa_tier(home_team)
        away_fifa_tier = self._get_fifa_tier(away_team)
        
        if home_fifa_tier > away_fifa_tier:
            # Smaller nation hosting elite team - massive crowd support
            crowd_factor = home_crowd_intensity + (away_fifa_tier - home_fifa_tier) * 8
        else:
            # Elite nation hosting or equal matchup
            crowd_factor = home_crowd_intensity
        
        # Apply venue boost
        total_support = min(crowd_factor + venue_boost, 85.0)
        
        return max(total_support, 55.0)  # Minimum home support

    def _calculate_crowd_intensity(self, team: str) -> float:
        """Calculate crowd intensity for home team"""
        team_upper = team.upper()
        
        if any(passionate in team_upper for passionate in self.passionate_home_crowds):
            return 80.0  # Passionate home crowds (Turkey, Scotland, etc.)
        elif any(elite in team_upper for elite in self.fifa_elite_nations):
            return 68.0  # Elite nations have good but not desperate crowds
        else:
            return 62.0  # Standard home support

    async def _calculate_current_fifa_form(self, game_data: Dict) -> float:
        """Calculate current FIFA form (10% weight - Recent international results)"""
        home_team = game_data.get('home_team', '').upper()
        away_team = game_data.get('away_team', '').upper()
        
        # Current FIFA Form Analysis (based on recent international windows)
        # This would ideally use real recent results, but for now we'll estimate based on team strength
        
        home_tier = self._get_fifa_tier(home_team)
        away_tier = self._get_fifa_tier(away_team)
        
        # Elite teams generally maintain good form
        if home_tier == 1 and away_tier == 1:
            return 72.0  # Elite vs elite - form matters but both strong
        elif home_tier == 1 or away_tier == 1:
            return 75.0  # One elite team likely in better form
        elif home_tier == 2 and away_tier == 2:
            return 68.0  # Strong nations - variable form
        else:
            return 65.0  # Lower tier nations - form less predictable

    def _detect_regional_rivalry(self, home_team: str, away_team: str) -> bool:
        """Detect if this is a regional rivalry matchup"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        for team1, team2 in self.major_rivalries:
            if ((team1 in home_upper and team2 in away_upper) or 
                (team2 in home_upper and team1 in away_upper)):
                return True
        
        return False

    def _detect_qualification_pressure(self, game_data: Dict) -> str:
        """Detect qualification pressure scenario"""
        # This could be enhanced with real group standings data
        # For now, we'll provide general pressure levels
        return "Standard qualifying match pressure"

    def _apply_international_adjustments(self, prediction: str, confidence: float, 
                                       home_team: str, away_team: str, game_data: Dict,
                                       fifa_factor: float, wc_history: float, home_support: float) -> tuple:
        """Apply international football specific adjustments"""
        
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # International draw detection (Elite vs Elite tactical games)
        home_tier = self._get_fifa_tier(home_team)
        away_tier = self._get_fifa_tier(away_team)
        is_rivalry = self._detect_regional_rivalry(home_team, away_team)
        
        # Elite vs Elite matchups often end in draws (tactical defensive games)
        if (home_tier == 1 and away_tier == 1 and 60 <= confidence <= 75):
            return "🤝 EUROPEAN TITANS DRAW", min(confidence - 2, 88.0)
        
        # Regional rivalry intensity can lead to draws
        if (is_rivalry and 55 <= confidence <= 72):
            rivalry_pair = self._get_rivalry_description(home_team, away_team)
            return f"🔥 {rivalry_pair} RIVALRY DRAW", min(confidence, 85.0)
        
        # Competitive international matches (similar tier teams)
        if (abs(home_tier - away_tier) <= 1 and 55 <= confidence <= 68):
            return "🤝 COMPETITIVE NATIONS DRAW", min(confidence - 1, 85.0)
        
        # Massive FIFA ranking gap favors elite team
        if fifa_factor >= 85:
            home_tier = self._get_fifa_tier(home_team)
            away_tier = self._get_fifa_tier(away_team)
            
            if home_tier < away_tier:  # Home team is higher tier (lower number = better)
                return f"👑 {home_team}", min(confidence + 5, 90.0)
            else:  # Away team is higher tier
                return f"✈️ {away_team}", min(confidence + 3, 90.0)
        
        # Small nation with massive home support vs elite team
        if (home_support >= 78 and home_tier > away_tier and confidence >= 70):
            return f"🏠 {home_team}", min(confidence + 4, 90.0)
        
        # Standard international prediction logic
        if confidence >= 85:
            # High confidence - favor stronger team or home advantage
            if fifa_factor >= 80:
                stronger_team = home_team if self._get_fifa_tier(home_team) < self._get_fifa_tier(away_team) else away_team
                return f"⭐ {stronger_team}", min(confidence, 90.0)
            else:
                return f"🏠 {home_team}", min(confidence, 90.0)
        elif confidence >= 75:
            # Moderate confidence
            if home_support >= 75:
                return f"🏠 {home_team}", min(confidence + 2, 90.0)
            else:
                return prediction, min(confidence, 90.0)
        else:
            # Lower confidence - favor home advantage in international football
            return f"🏠 {home_team}", min(confidence + 3, 90.0)

    def _get_rivalry_description(self, home_team: str, away_team: str) -> str:
        """Get description for regional rivalry"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        rivalry_descriptions = {
            ('ENGLAND', 'SCOTLAND'): 'BRITISH ISLES CLASSIC',
            ('SPAIN', 'PORTUGAL'): 'IBERIAN PENINSULA BATTLE',
            ('ITALY', 'FRANCE'): 'MEDITERRANEAN POWERS',
            ('GERMANY', 'NETHERLANDS'): 'NORTHERN EUROPEAN CLASH',
            ('TURKEY', 'GREECE'): 'EASTERN MEDITERRANEAN FIRE',
            ('POLAND', 'RUSSIA'): 'EASTERN EUROPEAN TENSION',
            ('SERBIA', 'ALBANIA'): 'BALKAN INTENSITY',
            ('CROATIA', 'SERBIA'): 'FORMER YUGOSLAVIA BATTLE',
        }
        
        for (team1, team2), description in rivalry_descriptions.items():
            if ((team1 in home_upper and team2 in away_upper) or 
                (team2 in home_upper and team1 in away_upper)):
                return description
        
        return 'REGIONAL RIVALRY'

# Test function
async def test_uefa_wc_qualifiers_algorithm():
    """Test UEFA World Cup Qualifiers algorithm with sample game data"""
    algorithm = UEFAWorldCupQualifiersAlgorithm()
    
    # Test 1: Elite vs Developing nation
    test_game1 = {
        'home_team': 'San Marino',
        'away_team': 'England',
        'venue': 'Stadio Olimpico, San Marino',
        'confidence': 65,
    }
    
    result1 = await algorithm.apply_uefa_wc_qualifiers_algorithm(test_game1)
    
    print("🔥 UEFA WORLD CUP QUALIFIERS ALGORITHM TEST 1:")
    print(f"⚽ {result1['away_team']} @ {result1['home_team']}")
    print(f"🎯 Prediction: {result1['prediction']}")
    print(f"📊 Confidence: {result1['confidence']}%")
    print(f"🌍 FIFA Rankings Factor: {result1['fifa_rankings_factor']}")
    print(f"🏆 WC History: {result1['wc_qualification_history']}")
    print(f"🏠 Home Support: {result1['home_nation_support']}")
    print("---")
    
    # Test 2: Regional rivalry
    test_game2 = {
        'home_team': 'Scotland',
        'away_team': 'England', 
        'venue': 'Hampden Park, Glasgow',
        'confidence': 55,
    }
    
    result2 = await algorithm.apply_uefa_wc_qualifiers_algorithm(test_game2)
    
    print("🔥 UEFA WORLD CUP QUALIFIERS ALGORITHM TEST 2:")
    print(f"⚽ {result2['away_team']} @ {result2['home_team']}")
    print(f"🎯 Prediction: {result2['prediction']}")
    print(f"📊 Confidence: {result2['confidence']}%")
    print(f"🔥 Regional Rivalry: {result2['regional_rivalry']}")
    print(f"📈 Algorithm: {result2['algorithm']}")
    print("---")
    
    # Test 3: Elite vs Elite
    test_game3 = {
        'home_team': 'France',
        'away_team': 'Spain',
        'venue': 'Stade de France, Paris',
        'confidence': 60,
    }
    
    result3 = await algorithm.apply_uefa_wc_qualifiers_algorithm(test_game3)
    
    print("🔥 UEFA WORLD CUP QUALIFIERS ALGORITHM TEST 3:")
    print(f"⚽ {result3['away_team']} @ {result3['home_team']}")
    print(f"🎯 Prediction: {result3['prediction']}")
    print(f"📊 Confidence: {result3['confidence']}%")
    print(f"🏟️ Tournament Experience: {result3['tournament_experience']}")
    
    return [result1, result2, result3]

if __name__ == "__main__":
    asyncio.run(test_uefa_wc_qualifiers_algorithm())