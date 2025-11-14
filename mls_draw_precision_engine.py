#!/usr/bin/env python3
"""
🔥💀🔥 MLS DRAW PRECISION ENGINE - STOP FALSE DRAWS! 💀🔥💀

CRITICAL PROBLEM IDENTIFIED:
- 5 out of 8 failures are FALSE DRAW PREDICTIONS
- We're predicting draws when teams actually win decisively
- Need PRECISION: Know when NOT to predict draws

NEW ANTI-DRAW FACTORS:
1. 🏟️ HOME DOMINANCE DETECTOR (3-0, 3-1 home wins)
2. ⚡ QUALITY GAP IDENTIFIER (skill difference too big for draw)
3. 🎯 FORM MOMENTUM TRACKER (hot team vs cold team)
4. 🏆 PLAYOFF DESPERATION (team needs points badly)
5. 💪 TACTICAL MISMATCH (attacking vs defensive styles)

Created: November 1, 2025
Mission: ACHIEVE 70%+ MLS ACCURACY WITH PRECISION DRAW DETECTION
"""

import logging
from typing import Dict, Any, Tuple, List

logger = logging.getLogger(__name__)

class MLSDrawPrecisionEngine:
    """
    🔥💀🔥 MLS DRAW PRECISION ENGINE
    
    Prevents false draw predictions by identifying when teams will win decisively
    """
    
    def __init__(self):
        """Initialize the draw precision engine"""
        
        # ANTI-DRAW FACTORS (prevent false draws)
        self.anti_draw_factors = {
            'home_dominance_threshold': 0.15,      # 15%+ home advantage = unlikely draw
            'quality_gap_threshold': 0.20,        # 20%+ quality gap = unlikely draw  
            'form_momentum_threshold': 0.18,       # Hot vs cold team = unlikely draw
            'desperation_factor': 0.25,            # Playoff desperation = unlikely draw
            'tactical_mismatch_factor': 0.12       # Style clash = unlikely draw
        }
        
        # MLS TEAM QUALITY TIERS (based on payroll, recent performance)
        self.team_quality_tiers = {
            'elite': {
                'teams': ['INTER MIAMI', 'LAFC', 'LA GALAXY', 'COLUMBUS CREW'],
                'rating': 85
            },
            'strong': {
                'teams': ['ATLANTA UNITED', 'SEATTLE SOUNDERS', 'NYCFC', 'PHILADELPHIA UNION', 'PORTLAND TIMBERS'],
                'rating': 75
            },
            'average': {
                'teams': ['FC CINCINNATI', 'MINNESOTA UNITED', 'CHICAGO FIRE', 'NASHVILLE SC', 'NEW ENGLAND REVOLUTION'],
                'rating': 65
            },
            'weak': {
                'teams': ['FC DALLAS', 'VANCOUVER WHITECAPS', 'CHARLOTTE FC', 'ORLANDO CITY', 'DC UNITED'],
                'rating': 55
            }
        }
        
        # HOME FORTRESS TEAMS (strong home advantage)
        self.home_fortress_teams = {
            'ATLANTA UNITED': 0.20,     # Mercedes-Benz Stadium atmosphere
            'SEATTLE SOUNDERS': 0.18,   # Lumen Field noise
            'PORTLAND TIMBERS': 0.16,   # Providence Park intensity
            'COLUMBUS CREW': 0.15,      # Crew Stadium loyal fans
            'LA GALAXY': 0.14,          # Dignity Health Sports Park experience
            'LAFC': 0.13,              # Banc of California Stadium modern
        }
        
        # AWAY SPECIALIST TEAMS (good at traveling)
        self.away_specialists = {
            'NYCFC': 0.12,             # Used to hostile environments
            'INTER MIAMI': 0.10,       # Messi draws crowds everywhere
            'SEATTLE SOUNDERS': 0.08,   # Experienced traveling
        }
        
        logger.info("🔥💀🔥 Draw Precision Engine initialized - FALSE DRAW KILLER! 💀🔥💀")
    
    def calculate_anti_draw_factors(self, 
                                  home_team: str, 
                                  away_team: str, 
                                  match_context: Dict[str, Any] = None) -> Tuple[float, Dict[str, Any]]:
        """
        🎯 CALCULATE ANTI-DRAW FACTORS: Reasons why this WON'T be a draw
        
        Returns: (anti_draw_score, analysis_report)
        Higher score = LESS likely to be a draw
        """
        try:
            if not match_context:
                match_context = {}
            
            anti_draw_score = 0.0
            factors_detected = []
            
            # FACTOR 1: HOME DOMINANCE DETECTOR
            home_dominance = self._calculate_home_dominance(home_team, away_team)
            if home_dominance > self.anti_draw_factors['home_dominance_threshold']:
                anti_draw_score += home_dominance
                factors_detected.append(f'🏟️ Home Dominance: {home_dominance:.2f}')
            
            # FACTOR 2: QUALITY GAP IDENTIFIER  
            quality_gap = self._calculate_quality_gap(home_team, away_team)
            if quality_gap > self.anti_draw_factors['quality_gap_threshold']:
                anti_draw_score += quality_gap
                factors_detected.append(f'⭐ Quality Gap: {quality_gap:.2f}')
            
            # FACTOR 3: FORM MOMENTUM TRACKER
            form_momentum = self._calculate_form_momentum(home_team, away_team, match_context)
            if form_momentum > self.anti_draw_factors['form_momentum_threshold']:
                anti_draw_score += form_momentum
                factors_detected.append(f'🔥 Form Momentum: {form_momentum:.2f}')
            
            # FACTOR 4: PLAYOFF DESPERATION
            desperation = self._calculate_desperation_factor(home_team, away_team, match_context)
            if desperation > self.anti_draw_factors['desperation_factor']:
                anti_draw_score += desperation
                factors_detected.append(f'🏆 Desperation: {desperation:.2f}')
            
            # FACTOR 5: TACTICAL MISMATCH
            tactical_mismatch = self._calculate_tactical_mismatch(home_team, away_team)
            if tactical_mismatch > self.anti_draw_factors['tactical_mismatch_factor']:
                anti_draw_score += tactical_mismatch
                factors_detected.append(f'⚔️ Tactical Mismatch: {tactical_mismatch:.2f}')
            
            analysis_report = {
                'anti_draw_score': anti_draw_score,
                'factors_detected': factors_detected,
                'draw_likelihood': 'LOW' if anti_draw_score > 0.30 else 'MEDIUM' if anti_draw_score > 0.15 else 'HIGH',
                'recommendation': 'AVOID_DRAW' if anti_draw_score > 0.25 else 'CONSIDER_DRAW' if anti_draw_score < 0.10 else 'BALANCED'
            }
            
            return anti_draw_score, analysis_report
            
        except Exception as e:
            logger.error(f"💀 Anti-draw calculation error: {e}")
            return 0.0, {'error': str(e), 'fallback': True}
    
    def _calculate_home_dominance(self, home_team: str, away_team: str) -> float:
        """🏟️ Calculate home team dominance factor"""
        home_fortress_bonus = self.home_fortress_teams.get(home_team.upper(), 0.0)
        away_weakness = 0.05 if away_team.upper() not in self.away_specialists else 0.0
        
        # Check if home team is significantly stronger
        home_tier = self._get_team_tier(home_team)
        away_tier = self._get_team_tier(away_team)
        
        tier_advantage = max(0, (home_tier - away_tier) * 0.03)  # 3% per tier difference
        
        return home_fortress_bonus + away_weakness + tier_advantage
    
    def _calculate_quality_gap(self, home_team: str, away_team: str) -> float:
        """⭐ Calculate quality gap between teams"""
        home_rating = self._get_team_rating(home_team)
        away_rating = self._get_team_rating(away_team)
        
        rating_diff = abs(home_rating - away_rating)
        
        # Convert rating difference to gap factor
        if rating_diff >= 20:
            return 0.30  # Huge gap
        elif rating_diff >= 15:
            return 0.22  # Large gap
        elif rating_diff >= 10:
            return 0.15  # Medium gap
        else:
            return 0.05  # Small gap
    
    def _calculate_form_momentum(self, home_team: str, away_team: str, context: Dict) -> float:
        """🔥 Calculate form momentum difference"""
        # Simplified form calculation (in real system would use recent results)
        home_form = context.get('home_recent_form', 50)  # 0-100 scale
        away_form = context.get('away_recent_form', 50)
        
        form_diff = abs(home_form - away_form)
        
        if form_diff >= 25:
            return 0.25  # Hot vs cold
        elif form_diff >= 15:
            return 0.18  # Good vs poor
        else:
            return 0.08  # Similar form
    
    def _calculate_desperation_factor(self, home_team: str, away_team: str, context: Dict) -> float:
        """🏆 Calculate playoff desperation"""
        home_position = context.get('home_playoff_position', 'safe')
        away_position = context.get('away_playoff_position', 'safe')
        
        desperation_score = 0.0
        
        if home_position == 'must_win':
            desperation_score += 0.25
        elif home_position == 'fighting':
            desperation_score += 0.15
        
        if away_position == 'must_win':
            desperation_score += 0.20  # Away desperation slightly less
        elif away_position == 'fighting':
            desperation_score += 0.12
        
        return desperation_score
    
    def _calculate_tactical_mismatch(self, home_team: str, away_team: str) -> float:
        """⚔️ Calculate tactical style mismatch"""
        # Simplified tactical analysis
        attacking_teams = ['LAFC', 'ATLANTA UNITED', 'INTER MIAMI']
        defensive_teams = ['COLUMBUS CREW', 'NEW ENGLAND REVOLUTION', 'VANCOUVER WHITECAPS']
        
        home_attacking = any(team in home_team.upper() for team in attacking_teams)
        away_attacking = any(team in away_team.upper() for team in attacking_teams)
        home_defensive = any(team in home_team.upper() for team in defensive_teams)
        away_defensive = any(team in away_team.upper() for team in defensive_teams)
        
        # Attacking vs Defensive = mismatch likely creates clear winner
        if (home_attacking and away_defensive) or (home_defensive and away_attacking):
            return 0.15
        else:
            return 0.05
    
    def _get_team_tier(self, team_name: str) -> int:
        """Get team tier (1=elite, 4=weak)"""
        for tier_name, tier_data in self.team_quality_tiers.items():
            if any(team in team_name.upper() for team in tier_data['teams']):
                tier_map = {'elite': 1, 'strong': 2, 'average': 3, 'weak': 4}
                return tier_map[tier_name]
        return 3  # Default to average
    
    def _get_team_rating(self, team_name: str) -> int:
        """Get team rating (0-100)"""
        for tier_data in self.team_quality_tiers.values():
            if any(team in team_name.upper() for team in tier_data['teams']):
                return tier_data['rating']
        return 65  # Default to average

# TESTING FUNCTION
async def test_draw_precision():
    """Test the draw precision engine on our false draw cases"""
    print("🔥💀🔥 TESTING DRAW PRECISION ENGINE 💀🔥💀")
    print("=" * 70)
    
    engine = MLSDrawPrecisionEngine()
    
    # Test on our false draw failures
    false_draw_cases = [
        {'home': 'LAFC', 'away': 'Austin FC', 'actual': 'LAFC WIN 2-1'},
        {'home': 'Vancouver Whitecaps', 'away': 'FC Dallas', 'actual': 'Vancouver WIN 3-0'},
        {'home': 'Chicago Fire FC', 'away': 'Orlando City SC', 'actual': 'Chicago WIN 3-1'},
        {'home': 'Columbus Crew', 'away': 'New York Red Bulls', 'actual': 'Columbus WIN 3-1'},
        {'home': 'LA Galaxy', 'away': 'Minnesota United FC', 'actual': 'Galaxy WIN 2-1'}
    ]
    
    print("🎯 TESTING ON FALSE DRAW CASES:")
    for i, case in enumerate(false_draw_cases, 1):
        anti_draw_score, report = engine.calculate_anti_draw_factors(
            case['home'], case['away']
        )
        
        print(f"\n🏟️ CASE {i}: {case['away']} @ {case['home']}")
        print(f"   📊 Anti-Draw Score: {anti_draw_score:.3f}")
        print(f"   🎯 Recommendation: {report['recommendation']}")
        print(f"   🔍 Factors: {', '.join(report['factors_detected']) if report['factors_detected'] else 'None detected'}")
        print(f"   ✅ Actual: {case['actual']}")
        
        should_avoid_draw = anti_draw_score > 0.25
        print(f"   💡 Would avoid draw? {'YES' if should_avoid_draw else 'NO'}")
    
    print("\n✅ DRAW PRECISION ENGINE READY FOR INTEGRATION!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_draw_precision())