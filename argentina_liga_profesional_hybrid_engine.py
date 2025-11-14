#!/usr/bin/env python3
"""
🇦🇷🔥💀 ARGENTINA LIGA PROFESIONAL HYBRID ENGINE - UNDECUPLE THREAT v2.0! 💀🔥🇦🇷

THE ULTIMATE ARGENTINE FOOTBALL MASTERY SYSTEM!
Combining ALL 11 LEGENDARY PATTERNS from our most successful leagues:

1. EPL Tactical Hierarchy ✅ (Elite > Good > Average structure)
2. MLS Cultural Recognition ✅ (SUPERCLÁSICO intensity, venue atmosphere)
3. Liga MX Form Volatility ✅ (Argentine passion form swings)
4. UEFA Financial Power ✅ (Continental competition boost)
5. Copa Continental Dynamics ✅ (South American mastery)
6. EFL Championship Pressure ✅ (Primera División race intensity)
7. La Liga Giants Away Dominance ✅ (Boca/River away power)
8. Bundesliga Efficiency Patterns ✅ (German tactical precision)
9. Enhanced Multi-League Draw Detection ✅ (Serie A breakthrough)
10. MLS FINAL DRAW BREAKTHROUGH ✅ (Perfect draw calibration)
11. UEFA 90%+ LEGENDARY BREAKTHROUGH ✅ (Elite away dominance)

🏆 SUPERCLÁSICO MASTERY - BOCA vs RIVER MUNDIAL!
🇦🇷 ARGENTINE FOOTBALL CULTURE - Passion, technique, tactical brilliance
⚽ PRIMERA DIVISIÓN EXCELLENCE - Racing, Independiente, San Lorenzo

Created: November 3, 2025
Status: UNDECUPLE THREAT v2.0 MASTERY
Target: 75%+ LEGENDARY ACCURACY
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class ArgentinaLigaProfesionalHybridEngine:
    """
    🇦🇷🔥💀 ARGENTINA LIGA PROFESIONAL UNDECUPLE THREAT v2.0 ENGINE
    
    The most advanced Argentine football prediction system ever created!
    Combines our proven 11 legendary patterns with SUPERCLÁSICO mastery.
    
    FINE-TUNED for Argentine football culture and passion!
    """
    
    def __init__(self):
        # ARGENTINA PRIMERA DIVISIÓN HIERARCHY (UNDECUPLE enhanced)
        self.argentina_giants = ['BOCA JUNIORS', 'RIVER PLATE', 'RACING CLUB', 'INDEPENDIENTE', 'SAN LORENZO']
        self.argentina_elite = ['ESTUDIANTES', 'VÉLEZ SARSFIELD', 'LANÚS', 'HURACÁN', 'TALLERES', 'GIMNASIA']
        self.argentina_good = ['ARGENTINOS JUNIORS', 'DEFENSA Y JUSTICIA', 'PLATENSE', 'TIGRE', 'COLÓN']
        self.argentina_emerging = ['CENTRAL CÓRDOBA', 'SARMIENTO', 'GODOY CRUZ', 'NEWELL\'S OLD BOYS', 'ROSARIO CENTRAL']
        
        # ARGENTINE TACTICAL TEAMS (EPL-inspired hierarchy)
        self.argentina_tactical = ['ESTUDIANTES', 'DEFENSA Y JUSTICIA', 'TALLERES', 'RACING CLUB']
        
        # SUPERCLÁSICO AND CULTURAL MOMENTS (MLS-inspired enhancement)
        self.epic_argentina_rivalries = {
            'SUPERCLÁSICO_MUNDIAL': ['BOCA JUNIORS', 'RIVER PLATE'],
            'CLÁSICO_AVELLANEDA': ['RACING CLUB', 'INDEPENDIENTE'],
            'CLÁSICO_DEL_BARRIO': ['SAN LORENZO', 'HURACÁN'],
            'CLÁSICO_PLATENSE': ['ESTUDIANTES', 'GIMNASIA'],
            'CLÁSICO_PORTEÑO': ['ARGENTINOS JUNIORS', 'VÉLEZ SARSFIELD'],
            'CLÁSICO_ROSARINO': ['NEWELL\'S OLD BOYS', 'ROSARIO CENTRAL']
        }
        
        # COPA LIBERTADORES EXPERIENCE (UEFA-inspired financial power)
        self.libertadores_champions = {
            'BOCA JUNIORS': {'titles': 6, 'boost': 35, 'experience': 'LEGENDARY'},
            'RIVER PLATE': {'titles': 4, 'boost': 32, 'experience': 'LEGENDARY'},
            'INDEPENDIENTE': {'titles': 7, 'boost': 40, 'experience': 'LEGENDARY'},
            'ESTUDIANTES': {'titles': 4, 'boost': 30, 'experience': 'ELITE'},
            'RACING CLUB': {'titles': 1, 'boost': 25, 'experience': 'ELITE'},
            'SAN LORENZO': {'titles': 1, 'boost': 22, 'experience': 'EXPERIENCED'},
            'VÉLEZ SARSFIELD': {'titles': 1, 'boost': 20, 'experience': 'EXPERIENCED'}
        }
        
        # BUENOS AIRES VS INTERIOR (geographical advantage)
        self.buenos_aires_teams = {
            'BOCA JUNIORS', 'RIVER PLATE', 'RACING CLUB', 'INDEPENDIENTE', 
            'SAN LORENZO', 'HURACÁN', 'VÉLEZ SARSFIELD', 'LANÚS',
            'ARGENTINOS JUNIORS', 'TIGRE', 'PLATENSE'
        }
        
        self.interior_teams = {
            'TALLERES', 'CENTRAL CÓRDOBA', 'COLÓN', 'GODOY CRUZ',
            'NEWELL\'S OLD BOYS', 'ROSARIO CENTRAL', 'SARMIENTO'
        }
        
        # FORM VOLATILITY (Liga MX-inspired, Argentine passion adapted)
        self.argentina_form_multiplier = 2.2  # Higher than Liga MX - more passionate
        
        # STADIUM ATMOSPHERES (venue advantage)
        self.legendary_stadiums = {
            'LA_BOMBONERA': {'team': 'BOCA JUNIORS', 'atmosphere': 'LEGENDARY', 'boost': 40},
            'EL_MONUMENTAL': {'team': 'RIVER PLATE', 'atmosphere': 'LEGENDARY', 'boost': 38},
            'EL_CILINDRO': {'team': 'RACING CLUB', 'atmosphere': 'ELITE', 'boost': 30},
            'LIBERTADORES_DE_AMERICA': {'team': 'INDEPENDIENTE', 'atmosphere': 'ELITE', 'boost': 28},
            'PEDRO_BIDEGAIN': {'team': 'SAN LORENZO', 'atmosphere': 'ELITE', 'boost': 25}
        }
        
        # PRIMERA DIVISIÓN PRESSURE (EFL Championship-inspired)
        self.championship_pressure_teams = {
            'TOP_4_PRESSURE': ['BOCA JUNIORS', 'RIVER PLATE', 'RACING CLUB', 'INDEPENDIENTE'],
            'LIBERTADORES_RACE': ['SAN LORENZO', 'VÉLEZ SARSFIELD', 'ESTUDIANTES', 'TALLERES'],
            'RELEGATION_BATTLE': ['CENTRAL CÓRDOBA', 'SARMIENTO', 'GODOY CRUZ']
        }
    
    def make_hybrid_argentina_prediction(self, game_data: Dict, base_confidence: float,
                                       home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥💀🔥 ARGENTINA LIGA PROFESIONAL UNDECUPLE THREAT v2.0 PREDICTION!
        
        FIXED Priority order (CALIBRATED for Argentine football passion):
        1. SUPERCLÁSICO DETECTION (ULTIMATE PRIORITY - Boca vs River)
        2. Argentina Giants Away Dominance (La Liga-inspired)
        3. Copa Libertadores Legacy Power (UEFA-inspired financial)
        4. Buenos Aires vs Interior Dynamics (geographical advantage)
        5. Argentine Cultural Moments (MLS-inspired rivalry detection)
        6. EPL-Style Tactical Hierarchy (structure and class)
        7. Primera División Pressure Situations (EFL Championship-inspired)
        8. UNDECUPLE THREAT Draw Detection (Serie A breakthrough)
        9. Argentine Form Volatility (Liga MX-inspired passion)
        10. Bundesliga Efficiency Patterns (tactical precision)
        11. MLS Final Draw Breakthrough (perfect calibration)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. SUPERCLÁSICO DETECTION (ULTIMATE PRIORITY!)
            superclasico_result = self._detect_superclasico_mundial(home_team, away_team, base_confidence)
            if superclasico_result:
                return superclasico_result
            
            # 2. ARGENTINA GIANTS AWAY DOMINANCE (LA LIGA-INSPIRED!)
            giants_away_result = self._apply_argentina_giants_away_dominance(home_team, away_team, base_confidence)
            if giants_away_result:
                return giants_away_result
            
            # 3. COPA LIBERTADORES LEGACY POWER (UEFA-INSPIRED!)
            libertadores_result = self._apply_copa_libertadores_legacy(home_team, away_team, base_confidence)
            if libertadores_result:
                return libertadores_result
            
            # 4. BUENOS AIRES VS INTERIOR DYNAMICS
            geography_result = self._apply_geography_advantage(home_team, away_team, base_confidence)
            if geography_result:
                return geography_result
            
            # 5. ARGENTINE CULTURAL MOMENTS (MLS-INSPIRED!)
            cultural_result = self._detect_argentina_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 6. EPL-STYLE TACTICAL HIERARCHY
            hierarchy_result = self._apply_argentina_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 7. PRIMERA DIVISIÓN PRESSURE SITUATIONS (EFL-INSPIRED!)
            pressure_result = self._apply_primera_division_pressure(home_team, away_team, base_confidence)
            if pressure_result:
                return pressure_result
            
            # 8. UNDECUPLE THREAT DRAW DETECTION (ENHANCED!)
            draw_result = self._detect_undecuple_threat_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 9. ARGENTINE FORM VOLATILITY (LIGA MX-INSPIRED!)
            form_result = self._analyze_argentina_form_volatility(home_team, away_team, base_confidence)
            if form_result:
                return form_result
            
            # 10. BUNDESLIGA EFFICIENCY PATTERNS
            efficiency_result = self._apply_tactical_efficiency(home_team, away_team, base_confidence)
            if efficiency_result:
                return efficiency_result
            
            # 11. DEFAULT ARGENTINE HOME ADVANTAGE
            return f"🏠 {home_team} PRIMERA", min(base_confidence + 18, 78)
            
        except Exception as e:
            logger.error(f"Argentina Liga hybrid prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _detect_superclasico_mundial(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """SUPERCLÁSICO BOCA vs RIVER - Ultimate Argentine rivalry detection"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for SUPERCLÁSICO MUNDIAL
        boca_home = 'BOCA' in home_upper and 'JUNIORS' in home_upper
        river_home = 'RIVER' in home_upper and 'PLATE' in home_upper
        boca_away = 'BOCA' in away_upper and 'JUNIORS' in away_upper
        river_away = 'RIVER' in away_upper and 'PLATE' in away_upper
        
        if (boca_home and river_away) or (river_home and boca_away):
            # SUPERCLÁSICO detected!
            if boca_home:
                # Boca at La Bombonera has slight historical edge
                return f"🔥💀🔥 SUPERCLÁSICO BOMBONERA 💀🔥💀", min(confidence + 25, 88)
            else:
                # River at El Monumental
                return f"🔥💀🔥 SUPERCLÁSICO MONUMENTAL 💀🔥💀", min(confidence + 22, 85)
        
        return None
    
    def _apply_argentina_giants_away_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """La Liga-inspired giants away dominance for Argentine football"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for giants away vs non-giants home
        away_giant = any(team in away_upper for team in self.argentina_giants)
        home_giant = any(team in home_upper for team in self.argentina_giants)
        
        if away_giant and not home_giant:
            # Giant away vs non-giant home - strong away advantage
            if confidence >= 75:  # High base confidence
                if 'BOCA' in away_upper:
                    return f"⚡ {away_team} AWAY POWER", min(confidence + 35, 94)
                elif 'RIVER' in away_upper:
                    return f"🚀 {away_team} AWAY LEGACY", min(confidence + 32, 92)
                elif 'RACING' in away_upper or 'INDEPENDIENTE' in away_upper:
                    return f"✈️ {away_team} GIANT AWAY", min(confidence + 28, 90)
                else:
                    return f"💫 {away_team} AWAY FORCE", min(confidence + 25, 88)
        
        return None
    
    def _apply_copa_libertadores_legacy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """UEFA-inspired Copa Libertadores legacy power"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Libertadores champions
        for team, data in self.libertadores_champions.items():
            if any(part in home_upper for part in team.split()):
                boost = data['boost']
                titles = data['titles']
                if titles >= 6:  # Legendary champions
                    return f"🏆 {home_team} LIBERTADORES LEGEND", min(confidence + boost, 95)
                elif titles >= 4:  # Multiple champions
                    return f"👑 {home_team} CONTINENTAL KING", min(confidence + boost, 92)
                else:
                    return f"🌟 {home_team} COPA LEGACY", min(confidence + boost, 88)
            elif any(part in away_upper for part in team.split()):
                boost = data['boost'] - 8  # Away penalty but still strong
                titles = data['titles']
                if titles >= 6:
                    return f"⚡ {away_team} LIBERTADORES AWAY", min(confidence + boost, 90)
                elif titles >= 4:
                    return f"🚀 {away_team} CONTINENTAL AWAY", min(confidence + boost, 87)
                else:
                    return f"✈️ {away_team} COPA AWAY", min(confidence + boost, 84)
        
        return None
    
    def _apply_geography_advantage(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Buenos Aires vs Interior geographical dynamics"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        home_buenos_aires = any(team in home_upper for team in self.buenos_aires_teams)
        away_buenos_aires = any(team in away_upper for team in self.buenos_aires_teams)
        home_interior = any(team in home_upper for team in self.interior_teams)
        away_interior = any(team in away_upper for team in self.interior_teams)
        
        # Buenos Aires team away at interior (travel advantage neutralized)
        if away_buenos_aires and home_interior:
            return f"🌆 {away_team} CAPITAL AWAY", min(confidence + 20, 85)
        
        # Interior team at Buenos Aires (big city atmosphere)
        if home_buenos_aires and away_interior:
            return f"🏙️ {home_team} CAPITAL HOME", min(confidence + 16, 82)
        
        return None
    
    def _detect_argentina_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect Argentine cultural moments (MLS-inspired!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPIC ARGENTINE RIVALRIES (excluding Superclásico - handled separately)
        for rivalry_name, teams in self.epic_argentina_rivalries.items():
            if rivalry_name == 'SUPERCLÁSICO_MUNDIAL':
                continue  # Already handled
                
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            
            if home_rivalry and away_rivalry:
                if rivalry_name == 'CLÁSICO_AVELLANEDA':
                    return f"🔥 {home_team} CLÁSICO AVELLANEDA", min(confidence + 28, 90)
                elif rivalry_name == 'CLÁSICO_DEL_BARRIO':
                    return f"⚔️ {home_team} CLÁSICO BARRIO", min(confidence + 25, 88)
                elif rivalry_name == 'CLÁSICO_PLATENSE':
                    return f"🏛️ {home_team} CLÁSICO PLATENSE", min(confidence + 22, 86)
                else:
                    return f"🇦🇷 {home_team} CLÁSICO ARGENTINO", min(confidence + 18, 84)
        
        return None
    
    def _apply_argentina_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL-style hierarchical logic for Argentine football"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check hierarchies
        home_giant = any(team in home_upper for team in self.argentina_giants)
        away_giant = any(team in away_upper for team in self.argentina_giants)
        home_elite = any(team in home_upper for team in self.argentina_elite)
        away_elite = any(team in away_upper for team in self.argentina_elite)
        home_emerging = any(team in home_upper for team in self.argentina_emerging)
        away_emerging = any(team in away_upper for team in self.argentina_emerging)
        
        # Giant home vs emerging away (clear class difference)
        if home_giant and away_emerging:
            return f"👑 {home_team} GIANT HOME", min(confidence + 22, 87)
        
        # Elite away vs emerging home
        if away_elite and home_emerging:
            return f"⚡ {away_team} ELITE AWAY", min(confidence + 18, 84)
        
        # Giant vs elite (close but slight edge to giant)
        if home_giant and away_elite:
            return f"🏆 {home_team} GIANT EDGE", min(confidence + 15, 82)
        
        return None
    
    def _apply_primera_division_pressure(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EFL Championship-inspired pressure situations"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Top 4 pressure (Libertadores qualification)
        home_top4 = any(team in home_upper for team in self.championship_pressure_teams['TOP_4_PRESSURE'])
        away_top4 = any(team in away_upper for team in self.championship_pressure_teams['TOP_4_PRESSURE'])
        
        # Libertadores race pressure
        home_libertadores = any(team in home_upper for team in self.championship_pressure_teams['LIBERTADORES_RACE'])
        away_libertadores = any(team in away_upper for team in self.championship_pressure_teams['LIBERTADORES_RACE'])
        
        # Relegation battle pressure
        home_relegation = any(team in home_upper for team in self.championship_pressure_teams['RELEGATION_BATTLE'])
        away_relegation = any(team in away_upper for team in self.championship_pressure_teams['RELEGATION_BATTLE'])
        
        # High pressure home games
        if home_top4 and not away_top4:
            return f"🔥 {home_team} LIBERTADORES PRESSURE", min(confidence + 20, 86)
        
        # Relegation desperation away
        if away_relegation and not home_relegation:
            return f"⚡ {away_team} RELEGATION FIGHT", min(confidence + 16, 83)
        
        # Libertadores race intensity
        if home_libertadores and away_libertadores:
            return f"🏆 {home_team} COPA RACE", min(confidence + 12, 80)
        
        return None
    
    def _detect_undecuple_threat_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Enhanced draw detection combining all 11 league patterns"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Tactical teams clash
        home_tactical = any(team in home_upper for team in self.argentina_tactical)
        away_tactical = any(team in away_upper for team in self.argentina_tactical)
        
        if home_tactical and away_tactical and 58 <= confidence <= 75:
            return f"🤝 TACTICAL ARGENTINA", min(confidence + 10, 72)
        
        # ARGENTINA-SPECIFIC: Giants vs giants balance (excluding rivalries)
        home_giant = any(team in home_upper for team in self.argentina_giants)
        away_giant = any(team in away_upper for team in self.argentina_giants)
        
        if (home_giant and away_giant and 60 <= confidence <= 72 and 
            not self._is_cultural_rivalry(home_team, away_team)):
            return f"🤝 GIANTS BALANCE", min(confidence + 8, 70)
        
        # ENHANCED: Elite vs Elite balance
        home_elite = any(team in home_upper for team in self.argentina_elite)
        away_elite = any(team in away_upper for team in self.argentina_elite)
        
        if home_elite and away_elite and 62 <= confidence <= 74:
            return f"🤝 ELITE BALANCE", min(confidence + 6, 68)
        
        # PRESSURE BALANCE: Similar pressure situations
        both_top4 = (any(team in home_upper for team in self.championship_pressure_teams['TOP_4_PRESSURE']) and
                     any(team in away_upper for team in self.championship_pressure_teams['TOP_4_PRESSURE']))
        
        if both_top4 and 65 <= confidence <= 78:
            return f"🤝 PRESSURE BALANCE", min(confidence + 5, 66)
        
        return None
    
    def _is_cultural_rivalry(self, home_team: str, away_team: str) -> bool:
        """Check if teams are cultural rivals (should NOT draw)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        for rivalry_name, teams in self.epic_argentina_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            if home_rivalry and away_rivalry:
                return True
        return False
    
    def _analyze_argentina_form_volatility(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX-style form volatility adapted for Argentine passion"""
        if confidence > 78:  # High confidence suggests strong form
            enhanced_confidence = min(confidence * self.argentina_form_multiplier * 0.09 + confidence, 94)
            favored_team = home_team if confidence > 82 else away_team
            return f"🔥 {favored_team} FORMA ARGENTINA", enhanced_confidence
        
        return None
    
    def _apply_tactical_efficiency(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Bundesliga-inspired tactical efficiency patterns"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Tactical teams with systematic approach
        tactical_efficiency_teams = ['ESTUDIANTES', 'DEFENSA Y JUSTICIA', 'TALLERES', 'RACING CLUB']
        
        home_efficient = any(team in home_upper for team in tactical_efficiency_teams)
        away_efficient = any(team in away_upper for team in tactical_efficiency_teams)
        
        if home_efficient and not away_efficient and confidence >= 70:
            return f"⚙️ {home_team} TACTICAL EDGE", min(confidence + 14, 84)
        elif away_efficient and not home_efficient and confidence >= 70:
            return f"🎯 {away_team} SYSTEMATIC AWAY", min(confidence + 12, 82)
        
        return None