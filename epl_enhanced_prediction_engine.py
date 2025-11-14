#!/usr/bin/env python3
"""
🏴󠁧󠁢󠁥󠁮󠁧󠁿💀 EPL ENHANCED PREDICTION ENGINE - FIX HOME BIAS! 💀🏴󠁧󠁢󠁥󠁮󠁧󠁿

CRITICAL FIXES FOR EPL ALGORITHM:
1. Fix extreme home bias (100% home predictions)
2. Add proper away win detection
3. Add tactical draw detection for EPL
4. Balance Big 6 dominance vs home advantage
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class EPLEnhancedPredictionEngine:
    """
    🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥 EPL ENHANCED PREDICTION ENGINE
    
    Fixes the extreme home bias and adds proper away/draw detection
    """
    
    def __init__(self):
        # EPL Big 6 (global powerhouses)
        self.big_6 = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL', 'CHELSEA', 'MANCHESTER UNITED', 'TOTTENHAM']
        
        # EPL Second Tier (European aspirants)
        self.second_tier = ['NEWCASTLE', 'BRIGHTON', 'ASTON VILLA', 'WEST HAM', 'FULHAM']
        
        # EPL Strong Home Advantage Teams
        self.fortress_teams = ['LIVERPOOL', 'MANCHESTER CITY', 'ARSENAL', 'NEWCASTLE', 'BRIGHTON']
        
        # EPL Good Away Teams (travel well)
        self.good_away_teams = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL', 'BRIGHTON', 'ASTON VILLA']
        
        # EPL Tactical/Defensive Teams (draw specialists)
        self.tactical_teams = ['BURNLEY', 'SHEFFIELD UNITED', 'LUTON TOWN', 'CRYSTAL PALACE', 'WOLVERHAMPTON']
    
    def make_enhanced_epl_prediction(self, game_data: Dict, base_confidence: float, 
                                   home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 ENHANCED EPL PREDICTION - FIXES HOME BIAS!
        
        Priority order:
        1. Big 6 Away Dominance (fixes away detection)
        2. Tactical Draws (fixes draw detection) 
        3. Home Advantage (balanced)
        4. Form-based decisions
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # Get team classifications
            home_is_big6 = any(team in home_upper for team in self.big_6)
            away_is_big6 = any(team in away_upper for team in self.big_6)
            home_is_second = any(team in home_upper for team in self.second_tier)
            away_is_second = any(team in away_upper for team in self.second_tier)
            home_is_tactical = any(team in home_upper for team in self.tactical_teams)
            away_is_tactical = any(team in away_upper for team in self.tactical_teams)
            away_travels_well = any(team in away_upper for team in self.good_away_teams)
            
            # 1. BIG 6 AWAY DOMINANCE (highest priority - fixes away detection!)
            if away_is_big6 and not home_is_big6:
                # Big 6 away vs non-Big 6 home
                confidence_boost = self._calculate_big6_away_boost(away_team, home_team)
                return f"✈️ {away_team} DOMINANCE", min(base_confidence + confidence_boost, 90)
            
            # 2. BIG 6 vs BIG 6 (special case)
            if home_is_big6 and away_is_big6:
                return self._handle_big6_clash(home_team, away_team, base_confidence)
            
            # 3. TACTICAL DRAWS (fixes draw detection!)
            if self._is_tactical_draw_likely(home_team, away_team, base_confidence):
                draw_confidence = self._calculate_draw_confidence(home_team, away_team)
                return f"🤝 EPL TACTICAL DRAW", draw_confidence
            
            # 4. AWAY TEAM QUALITY ADVANTAGE (fixes away detection!)
            if away_travels_well and not home_is_big6:
                away_advantage = self._calculate_away_advantage(away_team, home_team)
                if away_advantage > 0.15:  # Significant away advantage
                    return f"⚡ {away_team} AWAY STRENGTH", min(base_confidence + (away_advantage * 40), 85)
            
            # 5. SECOND TIER vs LOWER TEAMS
            if away_is_second and not (home_is_big6 or home_is_second):
                return f"🚀 {away_team} CLASS", min(base_confidence + 12, 80)
            
            # 6. HOME FORTRESS ADVANTAGE (balanced home advantage)
            if any(team in home_upper for team in self.fortress_teams):
                fortress_boost = self._calculate_fortress_boost(home_team)
                return f"🏰 {home_team} FORTRESS", min(base_confidence + fortress_boost, 85)
            
            # 7. STANDARD HOME ADVANTAGE (reduced from original)
            if base_confidence > 60:
                return f"🏠 {home_team}", min(base_confidence + 8, 78)  # Reduced boost
            
            # 8. CLOSE MATCH DEFAULT (was causing home bias)
            elif base_confidence > 50:
                # NEW: Consider both teams equally instead of defaulting to home
                stronger_team = self._determine_stronger_team_fairly(home_team, away_team)
                if stronger_team == home_team:
                    return f"🏠 {home_team}", min(base_confidence + 5, 70)
                elif stronger_team == away_team:
                    return f"⚡ {away_team}", min(base_confidence + 5, 70)
                else:
                    return f"🤝 CLOSE MATCH", min(base_confidence + 3, 65)
            
            # 9. LOW CONFIDENCE DRAW
            else:
                return f"🤝 EPL UNPREDICTABLE", min(base_confidence + 5, 60)
                
        except Exception as e:
            logger.error(f"Enhanced prediction error: {e}")
            # Fallback - but balanced, not home-biased
            if base_confidence > 60:
                return f"🏠 {home_team}", base_confidence
            else:
                return f"🤝 DRAW", base_confidence
    
    def _calculate_big6_away_boost(self, away_team: str, home_team: str) -> float:
        """Calculate confidence boost for Big 6 away games"""
        away_upper = away_team.upper()
        
        # Tier Big 6 teams by current strength (reduced to prevent 95% caps)
        if 'MANCHESTER CITY' in away_upper:
            return 18  # City away is dominant (reduced from 25)
        elif any(team in away_upper for team in ['ARSENAL', 'LIVERPOOL']):
            return 15  # Arsenal/Liverpool strong away (reduced from 20)
        elif any(team in away_upper for team in ['CHELSEA', 'TOTTENHAM']):
            return 12  # Chelsea/Spurs decent away (reduced from 15)
        elif 'MANCHESTER UNITED' in away_upper:
            return 10  # United inconsistent away (reduced from 12)
        else:
            return 8   # Default Big 6 boost (reduced from 10)
    
    def _handle_big6_clash(self, home_team: str, away_team: str, base_confidence: float) -> Tuple[str, float]:
        """Handle Big 6 vs Big 6 matches"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Current form hierarchy
        elite = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL']
        good = ['CHELSEA', 'TOTTENHAM']
        struggling = ['MANCHESTER UNITED']
        
        home_elite = any(team in home_upper for team in elite)
        away_elite = any(team in away_upper for team in elite)
        home_good = any(team in home_upper for team in good)
        away_good = any(team in away_upper for team in good)
        
        if away_elite and not home_elite:
            return f"✈️ {away_team} ELITE", min(base_confidence + 15, 85)
        elif home_elite and not away_elite:
            return f"🏆 {home_team} ELITE", min(base_confidence + 12, 82)
        else:
            # Equal quality - often draws
            return f"🤝 BIG 6 CLASH", min(base_confidence + 8, 75)
    
    def _is_tactical_draw_likely(self, home_team: str, away_team: str, confidence: float) -> bool:
        """Determine if a tactical draw is likely"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        home_tactical = any(team in home_upper for team in self.tactical_teams)
        away_tactical = any(team in away_upper for team in self.tactical_teams)
        
        # Both teams tactical
        if home_tactical and away_tactical:
            return True
        
        # One tactical team vs mid-table (often cancels out)
        mid_table = ['FULHAM', 'BRENTFORD', 'CRYSTAL PALACE', 'EVERTON', 'NOTTINGHAM FOREST']
        home_mid = any(team in home_upper for team in mid_table)
        away_mid = any(team in away_upper for team in mid_table)
        
        if (home_tactical and away_mid) or (away_tactical and home_mid):
            return True
        
        # Close confidence suggests even match
        if 45 <= confidence <= 65:
            return True
        
        return False
    
    def _calculate_draw_confidence(self, home_team: str, away_team: str) -> float:
        """Calculate confidence for draw predictions"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        base_draw_confidence = 55
        
        # Both tactical teams
        if (any(team in home_upper for team in self.tactical_teams) and 
            any(team in away_upper for team in self.tactical_teams)):
            base_draw_confidence += 15
        
        # Relegation battle (often cagey)
        relegation_teams = ['BURNLEY', 'SHEFFIELD UNITED', 'LUTON TOWN']
        home_relegation = any(team in home_upper for team in relegation_teams)
        away_relegation = any(team in away_upper for team in relegation_teams)
        
        if home_relegation and away_relegation:
            base_draw_confidence += 10
        
        return min(base_draw_confidence, 75)
    
    def _calculate_away_advantage(self, away_team: str, home_team: str) -> float:
        """Calculate away team advantage factor"""
        away_upper = away_team.upper()
        home_upper = home_team.upper()
        
        advantage = 0.0
        
        # Away team quality advantage
        if any(team in away_upper for team in self.big_6):
            advantage += 0.25
        elif any(team in away_upper for team in self.second_tier):
            advantage += 0.15
        
        # Home team weakness
        weak_teams = ['BURNLEY', 'SHEFFIELD UNITED', 'LUTON TOWN']
        if any(team in home_upper for team in weak_teams):
            advantage += 0.20
        
        # Good away record teams
        excellent_away = ['MANCHESTER CITY', 'ARSENAL', 'BRIGHTON']
        if any(team in away_upper for team in excellent_away):
            advantage += 0.15
        
        return advantage
    
    def _calculate_fortress_boost(self, home_team: str) -> float:
        """Calculate home fortress boost"""
        home_upper = home_team.upper()
        
        if 'LIVERPOOL' in home_upper:  # Anfield
            return 15
        elif 'MANCHESTER CITY' in home_upper:  # Etihad
            return 12
        elif any(team in home_upper for team in ['ARSENAL', 'NEWCASTLE']):
            return 10
        else:
            return 8
    
    def _determine_stronger_team_fairly(self, home_team: str, away_team: str) -> str:
        """Fairly determine stronger team without home bias"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Big 6 beats non-Big 6
        home_big6 = any(team in home_upper for team in self.big_6)
        away_big6 = any(team in away_upper for team in self.big_6)
        
        if away_big6 and not home_big6:
            return away_team
        elif home_big6 and not away_big6:
            return home_team
        
        # Second tier beats lower
        home_second = any(team in home_upper for team in self.second_tier)
        away_second = any(team in away_upper for team in self.second_tier)
        
        if away_second and not (home_big6 or home_second):
            return away_team
        elif home_second and not (away_big6 or away_second):
            return home_team
        
        # Equal - return None for draw
        return None