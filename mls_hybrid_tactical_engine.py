#!/usr/bin/env python3
"""
🇺🇸🔥 MLS HYBRID TACTICAL ENGINE - EPL PATTERNS + MLS CULTURE! 🔥🇺🇸

ADDING EPL SUCCESS PATTERNS TO MLS:
1. Tactical Hierarchy (Elite > Good > Average > Poor)
2. Class Differential Logic (Quality teams can win anywhere)
3. Form-based Draw Detection (Defensive teams neutralize)

KEEPING MLS STRENGTHS:
1. Cultural Dominance (Messi, El Trafico, Cascadia)
2. Travel Dynamics (American geography)
3. Rivalry Stalemates (Regional emotional parity)
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class MLSHybridTacticalEngine:
    """
    🇺🇸🔥 MLS HYBRID ENGINE - BEST OF BOTH WORLDS!
    
    Combines MLS cultural mastery with EPL tactical hierarchy
    """
    
    def __init__(self):
        # MLS ELITE HIERARCHY (adapted from EPL concept)
        self.mls_elite = ['INTER MIAMI', 'LAFC', 'LA GALAXY', 'SEATTLE SOUNDERS']
        self.mls_good = ['ATLANTA UNITED', 'PORTLAND TIMBERS', 'PHILADELPHIA UNION', 'COLUMBUS CREW']
        self.mls_average = ['NEW YORK CITY FC', 'AUSTIN FC', 'CHARLOTTE FC', 'VANCOUVER WHITECAPS']
        self.mls_poor = ['CHICAGO FIRE', 'COLORADO RAPIDS', 'SAN JOSE EARTHQUAKES', 'NEW ENGLAND REVOLUTION']
        
        # MLS TACTICAL TEAMS (defensive/draw-prone)
        self.mls_tactical = ['REAL SALT LAKE', 'FC DALLAS', 'HOUSTON DYNAMO', 'COLORADO RAPIDS']
        
        # MLS CULTURAL FACTORS (kept from original)
        self.cultural_games = {
            'MESSI_FACTOR': ['INTER MIAMI'],
            'EL_TRAFICO': ['LAFC', 'LA GALAXY'],
            'CASCADIA': ['SEATTLE SOUNDERS', 'PORTLAND TIMBERS', 'VANCOUVER WHITECAPS'],
            'CALIFORNIA_CLASICO': ['LA GALAXY', 'SAN JOSE EARTHQUAKES']
        }
        
        # MLS TRAVEL DYNAMICS (American geography)
        self.cross_country_distance = 2500  # miles
        self.coast_to_coast_teams = {
            'WEST': ['LAFC', 'LA GALAXY', 'SAN JOSE', 'SEATTLE', 'PORTLAND', 'VANCOUVER'],
            'EAST': ['INTER MIAMI', 'ATLANTA', 'NEW YORK', 'PHILADELPHIA', 'NEW ENGLAND', 'TORONTO']
        }
    
    def make_hybrid_mls_prediction(self, game_data: Dict, base_confidence: float,
                                 home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID MLS PREDICTION - EPL HIERARCHY + MLS CULTURE!
        
        Priority order (combining best patterns):
        1. MLS Cultural Dominance (keeps MLS strength)
        2. EPL Class Differential (adds EPL power)
        3. MLS + EPL Tactical Draws (combines both)
        4. MLS Travel Dynamics (keeps MLS specialty)
        5. EPL Hierarchical Logic (adds EPL structure)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. MLS CULTURAL DOMINANCE (HIGHEST PRIORITY - KEEP MLS STRENGTH!)
            cultural_result = self._detect_cultural_moment(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 2. EPL CLASS DIFFERENTIAL LOGIC (NEW - ADD EPL POWER!)
            class_result = self._apply_mls_class_differential(home_team, away_team, base_confidence)
            if class_result:
                return class_result
            
            # 3. HYBRID TACTICAL DRAWS (COMBINE EPL + MLS PATTERNS!)
            draw_result = self._detect_hybrid_tactical_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 4. MLS TRAVEL DYNAMICS (KEEP MLS SPECIALTY!)
            travel_result = self._analyze_travel_dynamics(home_team, away_team, base_confidence)
            if travel_result:
                return travel_result
            
            # 5. EPL HIERARCHICAL LOGIC (NEW - ADD EPL STRUCTURE!)
            hierarchy_result = self._apply_mls_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 6. DEFAULT HOME ADVANTAGE (MLS STYLE)
            return f"🏠 {home_team} ADVANTAGE", min(base_confidence + 8, 75)
            
        except Exception as e:
            logger.error(f"Hybrid MLS prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _detect_cultural_moment(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect MLS cultural moments (keep original strength)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # MESSI FACTOR (absolute priority)
        if any(team in home_upper for team in self.cultural_games['MESSI_FACTOR']):
            return f"🌟 {home_team} MESSI MAGIC", min(confidence + 25, 95)
        elif any(team in away_upper for team in self.cultural_games['MESSI_FACTOR']):
            return f"✈️ {away_team} MESSI AWAY", min(confidence + 20, 90)
        
        # EL TRAFICO
        home_trafico = any(team in home_upper for team in self.cultural_games['EL_TRAFICO'])
        away_trafico = any(team in away_upper for team in self.cultural_games['EL_TRAFICO'])
        
        if home_trafico and away_trafico:
            if 'LAFC' in home_upper:
                return f"🔥 {home_team} EL TRAFICO", min(confidence + 15, 85)
            else:
                return f"⭐ {home_team} GALAXY TRADITION", min(confidence + 12, 82)
        
        # CASCADIA CUP
        home_cascadia = any(team in home_upper for team in self.cultural_games['CASCADIA'])
        away_cascadia = any(team in away_upper for team in self.cultural_games['CASCADIA'])
        
        if home_cascadia and away_cascadia:
            return f"🏔️ {home_team} CASCADIA", min(confidence + 10, 80)
        
        return None
    
    def _apply_mls_class_differential(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Apply EPL-style class differential to MLS (NEW PATTERN!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check team hierarchies
        home_elite = any(team in home_upper for team in self.mls_elite)
        away_elite = any(team in away_upper for team in self.mls_elite)
        home_good = any(team in home_upper for team in self.mls_good)
        away_good = any(team in away_upper for team in self.mls_good)
        home_poor = any(team in home_upper for team in self.mls_poor)
        away_poor = any(team in away_upper for team in self.mls_poor)
        
        # ELITE AWAY VS NON-ELITE HOME (EPL-style dominance)
        if away_elite and not home_elite:
            boost = 20 if away_poor else 15  # Bigger boost vs poor teams
            return f"⚡ {away_team} CLASS ADVANTAGE", min(confidence + boost, 85)
        
        # GOOD AWAY VS POOR HOME
        if away_good and home_poor:
            return f"🚀 {away_team} QUALITY", min(confidence + 12, 78)
        
        return None
    
    def _detect_hybrid_tactical_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Combine EPL tactical + MLS rivalry draw detection"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Both tactical teams
        home_tactical = any(team in home_upper for team in self.mls_tactical)
        away_tactical = any(team in away_upper for team in self.mls_tactical)
        
        if home_tactical and away_tactical:
            return f"🤝 MLS TACTICAL DRAW", min(confidence + 15, 70)
        
        # MLS-STYLE: Regional rivalries
        rivalries = [
            (['COLUMBUS CREW', 'FC CINCINNATI'], 'Ohio'),
            (['FC DALLAS', 'HOUSTON DYNAMO', 'AUSTIN FC'], 'Texas'),
            (['CHICAGO FIRE', 'MINNESOTA UNITED'], 'Midwest'),
            (['PORTLAND TIMBERS', 'VANCOUVER WHITECAPS'], 'Cascadia'),
        ]
        
        for teams, region in rivalries:
            home_rival = any(team in home_upper for team in teams)
            away_rival = any(team in away_upper for team in teams)
            if home_rival and away_rival:
                return f"🤝 {region.upper()} RIVALRY DRAW", min(confidence + 12, 68)
        
        # EPL-STYLE: Close confidence suggests tactical match
        if 45 <= confidence <= 60:
            return f"🤝 CLOSE TACTICAL MATCH", min(confidence + 8, 65)
        
        return None
    
    def _analyze_travel_dynamics(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """MLS travel dynamics (keep specialty)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Cross-country travel fatigue
        home_west = any(team in home_upper for team in self.coast_to_coast_teams['WEST'])
        home_east = any(team in home_upper for team in self.coast_to_coast_teams['EAST'])
        away_west = any(team in away_upper for team in self.coast_to_coast_teams['WEST'])
        away_east = any(team in away_upper for team in self.coast_to_coast_teams['EAST'])
        
        # Coast-to-coast travel (2500+ miles)
        if (home_west and away_east) or (home_east and away_west):
            return f"🏠 {home_team} TRAVEL ADVANTAGE", min(confidence + 12, 78)
        
        return None
    
    def _apply_mls_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Apply EPL hierarchical logic to MLS (NEW STRUCTURE!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Elite teams should win most games
        home_elite = any(team in home_upper for team in self.mls_elite)
        away_elite = any(team in away_upper for team in self.mls_elite)
        home_good = any(team in home_upper for team in self.mls_good)
        away_good = any(team in away_upper for team in self.mls_good)
        
        # High confidence + quality difference
        if confidence > 65:
            if home_elite and not away_elite:
                return f"🏆 {home_team} ELITE", min(confidence + 10, 85)
            elif away_elite and not home_elite:
                return f"⚡ {away_team} ELITE", min(confidence + 8, 83)
            elif home_good and not (away_elite or away_good):
                return f"🏠 {home_team} QUALITY", min(confidence + 6, 80)
        
        return None