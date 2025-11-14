#!/usr/bin/env python3
"""
🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥 EPL HYBRID CULTURAL ENGINE - MLS PATTERNS + EPL HIERARCHY! 🔥🏴󠁧󠁢󠁥󠁮󠁧󠁿

ADDING MLS SUCCESS PATTERNS TO EPL:
1. Cultural Moment Recognition (Derby significance, star impact)
2. Venue Atmosphere Analysis (Anfield magic > generic fortress)
3. Emotional Factor Integration (Motivation, seasonal context)

KEEPING EPL STRENGTHS:
1. Tactical Hierarchy (Big 6 > Second Tier > etc)
2. Class Differential (Quality beats venue)
3. Form-based Analysis (Tactical draws)
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class EPLHybridCulturalEngine:
    """
    🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥 EPL HYBRID ENGINE - BEST OF BOTH WORLDS!
    
    Combines EPL tactical hierarchy with MLS cultural mastery
    """
    
    def __init__(self):
        # EPL HIERARCHY (keep from original)
        self.big_6 = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL', 'CHELSEA', 'MANCHESTER UNITED', 'TOTTENHAM']
        self.second_tier = ['NEWCASTLE', 'BRIGHTON', 'ASTON VILLA', 'WEST HAM', 'FULHAM']
        self.tactical_teams = ['BURNLEY', 'SHEFFIELD UNITED', 'LUTON TOWN', 'CRYSTAL PALACE', 'WOLVERHAMPTON']
        
        # EPL CULTURAL MOMENTS (MLS-inspired!)
        self.epic_derbies = {
            'NORTH_LONDON': ['ARSENAL', 'TOTTENHAM'],
            'MANCHESTER': ['MANCHESTER CITY', 'MANCHESTER UNITED'],
            'MERSEYSIDE': ['LIVERPOOL', 'EVERTON'],
            'LONDON_BIG': ['CHELSEA', 'ARSENAL', 'TOTTENHAM'],
            'LONDON_WEST': ['CHELSEA', 'FULHAM', 'BRENTFORD']
        }
        
        # EPL VENUE ATMOSPHERE (MLS-style specific analysis)
        self.legendary_venues = {
            'ANFIELD': {'team': 'LIVERPOOL', 'boost': 20, 'atmosphere': 'LEGENDARY'},
            'ETIHAD': {'team': 'MANCHESTER CITY', 'boost': 15, 'atmosphere': 'ELITE'},
            'EMIRATES': {'team': 'ARSENAL', 'boost': 12, 'atmosphere': 'PASSIONATE'},
            'STAMFORD_BRIDGE': {'team': 'CHELSEA', 'boost': 12, 'atmosphere': 'HISTORIC'},
            'OLD_TRAFFORD': {'team': 'MANCHESTER UNITED', 'boost': 10, 'atmosphere': 'TRADITION'},
            'ST_JAMES': {'team': 'NEWCASTLE', 'boost': 15, 'atmosphere': 'FORTRESS'}
        }
        
        # EPL STAR PLAYER IMPACT (MLS Messi-style)
        self.game_changers = {
            'HAALAND': {'team': 'MANCHESTER CITY', 'impact': 15},
            'SALAH': {'team': 'LIVERPOOL', 'impact': 12},
            'SAKA': {'team': 'ARSENAL', 'impact': 10},
            'KANE': {'team': 'TOTTENHAM', 'impact': 12},  # When he was there
            'PALMER': {'team': 'CHELSEA', 'impact': 8}
        }
        
        # EPL EMOTIONAL CONTEXT (MLS-inspired)
        self.seasonal_motivations = {
            'TITLE_RACE': ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL'],
            'TOP_4_BATTLE': ['CHELSEA', 'MANCHESTER UNITED', 'TOTTENHAM', 'NEWCASTLE'],
            'RELEGATION_FIGHT': ['BURNLEY', 'SHEFFIELD UNITED', 'LUTON TOWN']
        }
    
    def make_hybrid_epl_prediction(self, game_data: Dict, base_confidence: float,
                                 home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID EPL PREDICTION - MLS CULTURE + EPL HIERARCHY!
        
        Priority order (combining best patterns):
        1. EPL Big 6 Dominance (keeps EPL strength)
        2. MLS-Style Cultural Moments (adds MLS power)
        3. MLS-Style Venue Atmosphere (adds MLS specialty)
        4. EPL + MLS Tactical Draws (combines both)
        5. MLS-Style Emotional Context (adds MLS insight)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. EPL BIG 6 DOMINANCE (KEEP EPL STRENGTH!)
            big6_result = self._apply_epl_big6_dominance(home_team, away_team, base_confidence)
            if big6_result:
                return big6_result
            
            # 2. MLS-STYLE CULTURAL MOMENTS (NEW - ADD MLS POWER!)
            cultural_result = self._detect_epl_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 3. MLS-STYLE VENUE ATMOSPHERE (NEW - ADD MLS SPECIALTY!)
            venue_result = self._analyze_venue_atmosphere(home_team, away_team, base_confidence)
            if venue_result:
                return venue_result
            
            # 4. HYBRID TACTICAL DRAWS (COMBINE EPL + MLS!)
            draw_result = self._detect_hybrid_epl_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 5. MLS-STYLE EMOTIONAL CONTEXT (NEW - ADD MLS INSIGHT!)
            emotional_result = self._analyze_emotional_context(home_team, away_team, base_confidence)
            if emotional_result:
                return emotional_result
            
            # 6. EPL CLASS DIFFERENTIAL (EPL STRENGTH)
            class_result = self._apply_epl_class_differential(home_team, away_team, base_confidence)
            if class_result:
                return class_result
            
            # 7. DEFAULT
            return f"🏠 {home_team}", min(base_confidence + 5, 70)
            
        except Exception as e:
            logger.error(f"Hybrid EPL prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _apply_epl_big6_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL Big 6 dominance (keep original strength)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        home_big6 = any(team in home_upper for team in self.big_6)
        away_big6 = any(team in away_upper for team in self.big_6)
        
        # Big 6 away vs non-Big 6 home
        if away_big6 and not home_big6:
            boost = self._calculate_big6_away_boost(away_team)
            return f"✈️ {away_team} BIG 6 DOMINANCE", min(confidence + boost, 90)
        
        # Big 6 vs Big 6 (often draws due to quality)
        if home_big6 and away_big6:
            return self._handle_big6_clash(home_team, away_team, confidence)
        
        return None
    
    def _detect_epl_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect EPL cultural moments (MLS-inspired!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPIC DERBIES (MLS El Trafico-style)
        for derby_name, teams in self.epic_derbies.items():
            home_derby = any(team in home_upper for team in teams)
            away_derby = any(team in away_upper for team in teams)
            
            if home_derby and away_derby:
                if derby_name == 'NORTH_LONDON':
                    if 'ARSENAL' in home_upper:
                        return f"🔥 {home_team} NORTH LONDON DOMINANCE", min(confidence + 18, 85)
                    else:
                        return f"⚡ {home_team} SPURS PASSION", min(confidence + 15, 82)
                elif derby_name == 'MANCHESTER':
                    if 'MANCHESTER CITY' in home_upper:
                        return f"💙 {home_team} CITY POWER", min(confidence + 16, 84)
                    else:
                        return f"❤️ {home_team} UNITED SPIRIT", min(confidence + 12, 80)
                elif derby_name == 'MERSEYSIDE':
                    if 'LIVERPOOL' in home_upper:
                        return f"🔴 {home_team} MERSEYSIDE MAGIC", min(confidence + 20, 88)
                    else:
                        return f"🔵 {home_team} EVERTON PRIDE", min(confidence + 10, 75)
        
        return None
    
    def _analyze_venue_atmosphere(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """MLS-style specific venue analysis"""
        home_upper = home_team.upper()
        
        # LEGENDARY VENUES (MLS Messi-factor style)
        for venue, data in self.legendary_venues.items():
            if data['team'] in home_upper:
                atmosphere = data['atmosphere']
                boost = data['boost']
                
                if atmosphere == 'LEGENDARY':
                    return f"🏟️ {home_team} {atmosphere} ANFIELD", min(confidence + boost, 90)
                elif atmosphere == 'FORTRESS':
                    return f"🏰 {home_team} {atmosphere} STADIUM", min(confidence + boost, 85)
                else:
                    return f"🏠 {home_team} {atmosphere} VENUE", min(confidence + boost, 82)
        
        return None
    
    def _detect_hybrid_epl_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Hybrid EPL + MLS draw detection"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Tactical teams
        home_tactical = any(team in home_upper for team in self.tactical_teams)
        away_tactical = any(team in away_upper for team in self.tactical_teams)
        
        if home_tactical and away_tactical:
            return f"🤝 EPL TACTICAL STALEMATE", min(confidence + 15, 72)
        
        # MLS-STYLE: Big teams often draw (emotional parity)
        home_big6 = any(team in home_upper for team in self.big_6)
        away_big6 = any(team in away_upper for team in self.big_6)
        
        if home_big6 and away_big6 and 50 <= confidence <= 65:
            return f"🤝 BIG 6 CULTURAL DRAW", min(confidence + 12, 70)
        
        # MLS-STYLE: Similar motivation levels
        both_title_race = (any(team in home_upper for team in self.seasonal_motivations['TITLE_RACE']) and
                          any(team in away_upper for team in self.seasonal_motivations['TITLE_RACE']))
        
        if both_title_race:
            return f"🤝 TITLE RACE TENSION", min(confidence + 10, 68)
        
        return None
    
    def _analyze_emotional_context(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """MLS-style emotional/motivational analysis"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # TITLE RACE MOTIVATION
        home_title = any(team in home_upper for team in self.seasonal_motivations['TITLE_RACE'])
        away_title = any(team in away_upper for team in self.seasonal_motivations['TITLE_RACE'])
        
        if home_title and not away_title:
            return f"🏆 {home_team} TITLE MOTIVATION", min(confidence + 12, 82)
        elif away_title and not home_title:
            return f"⚡ {away_team} TITLE HUNGER", min(confidence + 10, 80)
        
        # RELEGATION DESPERATION
        home_relegation = any(team in home_upper for team in self.seasonal_motivations['RELEGATION_FIGHT'])
        away_relegation = any(team in away_upper for team in self.seasonal_motivations['RELEGATION_FIGHT'])
        
        if home_relegation and not away_relegation:
            return f"💪 {home_team} SURVIVAL FIGHT", min(confidence + 8, 75)
        
        return None
    
    def _apply_epl_class_differential(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL class differential (keep strength)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        home_second = any(team in home_upper for team in self.second_tier)
        away_second = any(team in away_upper for team in self.second_tier)
        home_tactical = any(team in home_upper for team in self.tactical_teams)
        away_tactical = any(team in away_upper for team in self.tactical_teams)
        
        # Second tier away vs tactical home
        if away_second and home_tactical:
            return f"🚀 {away_team} CLASS ADVANTAGE", min(confidence + 15, 80)
        
        # Quality home vs weak away
        if home_second and away_tactical:
            return f"🏠 {home_team} QUALITY", min(confidence + 10, 78)
        
        return None
    
    def _calculate_big6_away_boost(self, away_team: str) -> float:
        """Calculate Big 6 away boost"""
        away_upper = away_team.upper()
        
        if 'MANCHESTER CITY' in away_upper:
            return 25
        elif any(team in away_upper for team in ['ARSENAL', 'LIVERPOOL']):
            return 20
        elif any(team in away_upper for team in ['CHELSEA', 'TOTTENHAM']):
            return 15
        else:
            return 12
    
    def _handle_big6_clash(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Handle Big 6 clashes"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        title_contenders = ['MANCHESTER CITY', 'ARSENAL', 'LIVERPOOL']
        
        home_title = any(team in home_upper for team in title_contenders)
        away_title = any(team in away_upper for team in title_contenders)
        
        if away_title and not home_title:
            return f"⚡ {away_team} TITLE CONTENDER", min(confidence + 15, 85)
        elif home_title and not away_title:
            return f"🏆 {home_team} TITLE STRENGTH", min(confidence + 12, 82)
        else:
            return f"🤝 BIG 6 EPIC CLASH", min(confidence + 8, 75)