#!/usr/bin/env python3
"""
🇦🇷🇧🇷🇨🇴🔥 COPA SUDAMERICANA HYBRID ENGINE - QUINTUPLE THREAT MASTERY! 🔥🇨🇴🇧🇷🇦🇷

ADDING EPL+MLS+LIGA MX+UEFA SUCCESS PATTERNS TO COPA SUDAMERICANA:
1. EPL Tactical Hierarchy (Elite > Good > Average > Poor structure)
2. MLS Cultural Recognition (Rivalry intensity, venue atmosphere)
3. Liga MX Form Volatility (Hot/cold streak recognition)
4. UEFA Financial Power (Money dominance patterns)
5. Enhanced Multi-League Draw Detection

KEEPING COPA SUDAMERICANA STRENGTHS:
1. Argentina Dominance (Independiente 3x champion supremacy)
2. Brazilian Financial Power (€50-100M vs €2-5M disparity)
3. Altitude Advantage (La Paz 3,500m, Quito 2,850m advantage)
4. Continental Financial Disparity (Nation-based economics)
5. Knockout Pressure (Single elimination format)

🎯 FINE-TUNED FOR SOUTH AMERICAN FOOTBALL CULTURE!
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class CopaSudamericanaHybridEngine:
    """
    🇦🇷🇧🇷🇨🇴🔥 COPA SUDAMERICANA HYBRID ENGINE - QUINTUPLE THREAT!
    
    Combines Copa Sudamericana mastery with EPL + MLS + Liga MX + UEFA patterns
    FINE-TUNED for South American football culture and continental dynamics
    """
    
    def __init__(self):
        # COPA SUDAMERICANA HIERARCHY (enhanced with other league patterns)
        self.south_american_giants = ['INDEPENDIENTE', 'BOCA JUNIORS', 'RIVER PLATE', 'PALMEIRAS', 'SAO PAULO', 'FLAMENGO']
        self.south_american_elite = ['SANTOS', 'CORINTHIANS', 'ATLETICO PARANAENSE', 'RACING', 'ESTUDIANTES', 'SAN LORENZO']
        self.south_american_good = ['INTERNACIONAL', 'GREMIO', 'NACIONAL', 'PENAROL', 'COLO COLO', 'MILLONARIOS']
        self.south_american_emerging = ['CARACAS FC', 'BOLIVAR', 'STRONGEST', 'EMELEC', 'BARCELONA SC']
        
        # SOUTH AMERICAN TACTICAL TEAMS (EPL-inspired)
        self.copa_tactical = ['DEFENSA Y JUSTICIA', 'ESTUDIANTES', 'RACING', 'ATLETICO PARANAENSE']
        
        # SOUTH AMERICAN CULTURAL MOMENTS (MLS-inspired enhancement)
        self.epic_south_american_rivalries = {
            'SUPERCLASICO': ['BOCA JUNIORS', 'RIVER PLATE'],
            'BRAZILIAN_CLASICO': ['FLAMENGO', 'FLUMINENSE'],
            'PAULISTA_DERBY': ['PALMEIRAS', 'SAO PAULO', 'CORINTHIANS', 'SANTOS'],
            'URUGUAYAN_CLASICO': ['NACIONAL', 'PENAROL'],
            'CHILEAN_CLASICO': ['COLO COLO', 'UNIVERSIDAD CHILE'],
            'COLOMBIAN_RIVALRY': ['MILLONARIOS', 'NACIONAL']
        }
        
        # ALTITUDE ADVANTAGE (Copa Sudamericana specialty)
        self.altitude_cities = {
            'LA_PAZ': {'altitude': 3500, 'boost': 35, 'atmosphere': 'EXTREME'},
            'QUITO': {'altitude': 2850, 'boost': 28, 'atmosphere': 'HIGH'},
            'BOGOTA': {'altitude': 2640, 'boost': 22, 'atmosphere': 'MODERATE'},
            'COCHABAMBA': {'altitude': 2560, 'boost': 20, 'atmosphere': 'MODERATE'},
            'CUSCO': {'altitude': 3400, 'boost': 32, 'atmosphere': 'EXTREME'}
        }
        
        # ARGENTINA DOMINANCE (Copa specialty)
        self.argentina_champions = {
            'INDEPENDIENTE': {'titles': 3, 'boost': 35},
            'DEFENSA Y JUSTICIA': {'titles': 1, 'boost': 25},
            'BOCA JUNIORS': {'titles': 1, 'boost': 30},
            'ARSENAL': {'titles': 1, 'boost': 20},
            'ESTUDIANTES': {'titles': 1, 'boost': 25}
        }
        
        # BRAZILIAN FINANCIAL POWER (Copa specialty)
        self.brazilian_budgets = {
            'PALMEIRAS': {'budget': 80, 'boost': 30},
            'SAO_PAULO': {'budget': 70, 'boost': 28},
            'FLAMENGO': {'budget': 75, 'boost': 29},
            'SANTOS': {'budget': 50, 'boost': 22},
            'CORINTHIANS': {'budget': 65, 'boost': 26}
        }
        
        # FORM VOLATILITY (Liga MX-inspired, South American adapted)
        self.south_american_form_multiplier = 2.0  # South American teams have extreme swings
        
        # FINANCIAL DISPARITY (Copa unique factor)
        self.nation_financial_power = {
            'BRAZIL': 95,
            'ARGENTINA': 85,
            'COLOMBIA': 72,
            'CHILE': 68,
            'URUGUAY': 65,
            'ECUADOR': 58,
            'BOLIVIA': 45,
            'VENEZUELA': 50
        }
    
    def make_hybrid_copa_sudamericana_prediction(self, game_data: Dict, base_confidence: float,
                                               home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID COPA SUDAMERICANA PREDICTION - QUINTUPLE THREAT MASTERY!
        
        FIXED Priority order (CALIBRATED for South American football):
        1. Copa Altitude Advantage (UNIQUE - can't be replicated elsewhere)
        2. Copa Brazilian Financial Power (STRONGEST factor - €50M+ budgets)
        3. Copa Argentina Dominance (COMPLEMENTARY - works with Brazilian)
        4. MLS-Style Cultural Moments (SUPERCLÁSICO priority)
        5. UEFA-Style Financial Disparity (nation-based economics)
        6. EPL-Style Tactical Hierarchy (structure)
        7. Quintuple Threat Draw Detection (RECALIBRATED thresholds)
        8. Liga MX-Style Form Volatility (South American swings)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. COPA ALTITUDE ADVANTAGE (UNIQUE - HIGHEST PRIORITY!)
            altitude_result = self._apply_altitude_advantage(home_team, away_team, base_confidence)
            if altitude_result:
                return altitude_result
            
            # 2. COPA BRAZILIAN FINANCIAL POWER (STRONGEST FACTOR!)
            brazilian_result = self._apply_brazilian_financial_power(home_team, away_team, base_confidence)
            if brazilian_result:
                return brazilian_result
            
            # 3. MLS-STYLE CULTURAL MOMENTS (SUPERCLÁSICO PRIORITY!)
            cultural_result = self._detect_south_american_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 4. COPA ARGENTINA DOMINANCE (COMPLEMENTARY - NO CONFLICT!)
            argentina_result = self._apply_argentina_dominance(home_team, away_team, base_confidence)
            if argentina_result:
                return argentina_result
            
            # 5. UEFA-STYLE FINANCIAL DISPARITY (ENHANCED CONTINENTAL!)
            disparity_result = self._apply_continental_financial_disparity(home_team, away_team, base_confidence)
            if disparity_result:
                return disparity_result
            
            # 6. EPL-STYLE TACTICAL HIERARCHY (NEW - ADD STRUCTURE!)
            hierarchy_result = self._apply_south_american_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 7. QUINTUPLE THREAT DRAW DETECTION (RECALIBRATED!)
            draw_result = self._detect_quintuple_threat_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 8. LIGA MX-STYLE FORM VOLATILITY (ENHANCED SOUTH AMERICAN!)
            form_result = self._analyze_south_american_form_volatility(home_team, away_team, base_confidence)
            if form_result:
                return form_result
            
            # 9. DEFAULT SOUTH AMERICAN HOME ADVANTAGE
            return f"🏠 {home_team} CONTINENTAL", min(base_confidence + 15, 78)
            
        except Exception as e:
            logger.error(f"Hybrid Copa Sudamericana prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _apply_argentina_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Copa Argentina dominance (absolute South American priority)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Argentine champions
        for team, data in self.argentina_champions.items():
            if any(part in home_upper for part in team.split()):
                boost = data['boost']
                if team == 'INDEPENDIENTE':  # 3x champion
                    return f"🏆 {home_team} TRICAMPEÓN", min(confidence + boost, 95)
                else:
                    return f"🇦🇷 {home_team} ARGENTINE POWER", min(confidence + boost, 92)
            elif any(part in away_upper for part in team.split()):
                boost = data['boost'] - 5  # Away penalty
                if team == 'INDEPENDIENTE':
                    return f"⚡ {away_team} TRICAMPEÓN AWAY", min(confidence + boost, 90)
                else:
                    return f"✈️ {away_team} ARGENTINE AWAY", min(confidence + boost, 88)
        
        # Other Argentine giants
        other_argentine = ['BOCA', 'RIVER', 'RACING', 'SAN LORENZO']
        home_argentine = any(team in home_upper for team in other_argentine)
        away_argentine = any(team in away_upper for team in other_argentine)
        
        if home_argentine:
            return f"🇦🇷 {home_team} ARGENTINE GIANT", min(confidence + 25, 88)
        elif away_argentine:
            return f"⚡ {away_team} ARGENTINE POWER", min(confidence + 20, 85)
        
        return None
    
    def _apply_altitude_advantage(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Copa altitude advantage (unique South American factor)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # CRITICAL: Check for ARGENTINA GIANTS exception first!
        argentina_giants = ['BOCA JUNIORS', 'RIVER PLATE', 'INDEPENDIENTE', 'RACING', 'SAN LORENZO']
        away_is_argentina_giant = any(giant in away_upper for giant in argentina_giants)
        
        # High altitude teams at home
        altitude_teams = {
            'BOLIVAR': {'city': 'LA_PAZ', 'boost': 35},
            'STRONGEST': {'city': 'LA_PAZ', 'boost': 32},
            'WILSTERMANN': {'city': 'COCHABAMBA', 'boost': 25},
            'BARCELONA': {'city': 'QUITO', 'boost': 28},  # Ecuador
            'EMELEC': {'city': 'QUITO', 'boost': 25}
        }
        
        for team, data in altitude_teams.items():
            if team in home_upper:
                boost = data['boost']
                city = data['city']
                altitude_data = self.altitude_cities[city]
                
                # ARGENTINA GIANT EXCEPTION: Reduce altitude advantage significantly
                if away_is_argentina_giant:
                    boost = max(boost - 20, 10)  # Drastically reduce altitude effect
                    # Let Argentina giants compete better at altitude
                    if boost <= 15:  # If boost too small, let it pass to Argentina dominance
                        return None
                    return f"⚡ {home_team} vs ARGENTINA", min(confidence + boost, 75)
                
                # Extra boost vs sea-level teams (but not Argentina giants)
                sea_level_teams = ['SANTOS', 'FLAMENGO', 'BOTAFOGO']
                if any(team in away_upper for team in sea_level_teams):
                    boost += 15  # Massive altitude advantage
                
                if altitude_data['atmosphere'] == 'EXTREME':
                    return f"🏔️ {home_team} ALTITUDE FORTRESS", min(confidence + boost, 95)
                else:
                    return f"⛰️ {home_team} HIGH ALTITUDE", min(confidence + boost, 90)
        
        return None
    
    def _apply_brazilian_financial_power(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Copa Brazilian financial power (South American money dominance) - ENHANCED!"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Brazilian financial powerhouses (EXACT MATCHING)
        for team, data in self.brazilian_budgets.items():
            if team in home_upper:
                boost = data['boost']
                return f"🇧🇷 {home_team} BRAZILIAN POWER", min(confidence + boost, 92)
            elif team in away_upper:
                boost = data['boost'] - 5  # REDUCED away penalty
                return f"💰 {away_team} FINANCIAL POWER", min(confidence + boost, 90)
        
        # BROADER Brazilian team detection (financial league strength)
        broader_brazilian = ['FLAMENGO', 'ATLETICO', 'INTERNACIONAL', 'GREMIO']
        
        for team in broader_brazilian:
            if team in home_upper:
                return f"🇧🇷 {home_team} BRAZILIAN LEAGUE", min(confidence + 25, 88)
            elif team in away_upper:
                return f"💰 {away_team} BRAZILIAN AWAY", min(confidence + 20, 85)
        
        return None
    
    def _apply_continental_financial_disparity(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """UEFA-style financial disparity applied to South America"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Identify nations
        home_nation = self._identify_south_american_nation(home_team)
        away_nation = self._identify_south_american_nation(away_team)
        
        if home_nation and away_nation:
            home_power = self.nation_financial_power.get(home_nation, 50)
            away_power = self.nation_financial_power.get(away_nation, 50)
            
            disparity = abs(home_power - away_power)
            
            # Significant disparity (20+ points)
            if disparity >= 20:
                if home_power > away_power:
                    return f"💰 {home_team} FINANCIAL ADVANTAGE", min(confidence + 22, 88)
                else:
                    return f"🚀 {away_team} ECONOMIC POWER", min(confidence + 18, 85)
            
            # Moderate disparity (10+ points)
            elif disparity >= 10:
                stronger_team = home_team if home_power > away_power else away_team
                return f"💰 {stronger_team} ECONOMIC EDGE", min(confidence + 12, 82)
        
        return None
    
    def _apply_south_american_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL-style hierarchical logic applied to South America"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check hierarchies
        home_giant = any(team in home_upper for team in self.south_american_giants)
        away_giant = any(team in away_upper for team in self.south_american_giants)
        home_elite = any(team in home_upper for team in self.south_american_elite)
        away_elite = any(team in away_upper for team in self.south_american_elite)
        home_emerging = any(team in home_upper for team in self.south_american_emerging)
        away_emerging = any(team in away_upper for team in self.south_american_emerging)
        
        # Giant away vs non-giant home
        if away_giant and not home_giant:
            return f"🚀 {away_team} GIANT POWER", min(confidence + 20, 88)
        
        # Elite away vs emerging home
        if away_elite and home_emerging:
            return f"✈️ {away_team} ELITE AWAY", min(confidence + 16, 85)
        
        # Giant home vs emerging away
        if home_giant and away_emerging:
            return f"🏆 {home_team} GIANT HOME", min(confidence + 18, 87)
        
        return None
    
    def _detect_south_american_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect South American cultural moments (MLS-inspired!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPIC SOUTH AMERICAN RIVALRIES
        for rivalry_name, teams in self.epic_south_american_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            
            if home_rivalry and away_rivalry:
                if rivalry_name == 'SUPERCLASICO':
                    return f"🔥 {home_team} SUPERCLÁSICO", min(confidence + 30, 92)
                elif rivalry_name == 'BRAZILIAN_CLASICO':
                    return f"🇧🇷 {home_team} CLÁSSICO BRASILEIRO", min(confidence + 25, 90)
                elif rivalry_name == 'PAULISTA_DERBY':
                    return f"⚡ {home_team} DERBY PAULISTA", min(confidence + 22, 88)
                else:
                    return f"🏆 {home_team} CLÁSICO CONTINENTAL", min(confidence + 18, 85)
        
        return None
    
    def _detect_quintuple_threat_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Combine EPL + MLS + Liga MX + UEFA + Copa draw detection - ENHANCED!"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Tactical teams (EXPANDED CONDITIONS)
        home_tactical = any(team in home_upper for team in self.copa_tactical)
        away_tactical = any(team in away_upper for team in self.copa_tactical)
        
        if home_tactical and away_tactical and 50 <= confidence <= 70:  # EXPANDED RANGE
            return f"🤝 SOUTH AMERICAN TACTICAL", min(confidence + 12, 70)
        
        # COPA-SPECIFIC: Altitude vs Financial powerhouse (UNIQUE DRAW!)
        altitude_teams = ['BOLIVAR', 'STRONGEST', 'WILSTERMANN']
        financial_teams = ['PALMEIRAS', 'SAO_PAULO', 'FLAMENGO', 'CORINTHIANS']
        
        home_altitude = any(team in home_upper for team in altitude_teams)
        away_financial = any(team in away_upper for team in financial_teams)
        
        if home_altitude and away_financial and 55 <= confidence <= 75:  # EXPANDED RANGE
            return f"🤝 ALTITUDE VS MONEY", min(confidence + 10, 68)
        
        # ENHANCED: Argentina vs Brazil GIANTS (continental balance)
        argentina_giants = ['RIVER PLATE', 'BOCA JUNIORS', 'INDEPENDIENTE', 'RACING']
        brazil_giants = ['PALMEIRAS', 'SAO_PAULO', 'FLAMENGO']
        
        home_argentina = any(team in home_upper for team in argentina_giants)
        away_brazil = any(team in away_upper for team in brazil_giants)
        home_brazil = any(team in home_upper for team in brazil_giants)
        away_argentina = any(team in away_upper for team in argentina_giants)
        
        if ((home_argentina and away_brazil) or (home_brazil and away_argentina)) and 58 <= confidence <= 75:
            return f"🤝 ARGENTINA VS BRAZIL", min(confidence + 8, 66)
        
        # MLS-STYLE: Giants clash (EXPANDED CONDITIONS)
        home_giant = any(team in home_upper for team in self.south_american_giants)
        away_giant = any(team in away_upper for team in self.south_american_giants)
        
        # EXPANDED: Better range and no cultural rivalry restriction
        if (home_giant and away_giant and 55 <= confidence <= 68 and 
            not self._is_cultural_rivalry(home_team, away_team)):
            return f"🤝 GIANTS CONTINENTAL", min(confidence + 8, 68)
        
        # NEW: Elite vs Elite tactical balance (expanded recognition)
        home_elite = any(team in home_upper for team in self.south_american_elite)
        away_elite = any(team in away_upper for team in self.south_american_elite)
        
        if home_elite and away_elite and 60 <= confidence <= 72:
            return f"🤝 ELITE BALANCE", min(confidence + 6, 66)
        
        return None
    
    def _is_cultural_rivalry(self, home_team: str, away_team: str) -> bool:
        """Check if teams are cultural rivals (should NOT draw)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        for rivalry_name, teams in self.epic_south_american_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            if home_rivalry and away_rivalry:
                return True
        return False
    
    def _analyze_south_american_form_volatility(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX-style form volatility adapted for South American teams"""
        # South American teams have extreme form swings in continental competition
        
        if confidence > 75:  # High confidence suggests strong form
            enhanced_confidence = min(confidence * self.south_american_form_multiplier * 0.08 + confidence, 92)
            favored_team = home_team if confidence > 80 else away_team
            return f"🔥 {favored_team} CONTINENTAL FORM", enhanced_confidence
        
        return None
    
    def _identify_south_american_nation(self, team_name: str) -> str:
        """Identify South American nation based on team patterns"""
        team_upper = team_name.upper()
        
        if any(indicator in team_upper for indicator in ['PALMEIRAS', 'FLAMENGO', 'SAO_PAULO', 'SANTOS', 'CORINTHIANS']):
            return 'BRAZIL'
        elif any(indicator in team_upper for indicator in ['BOCA', 'RIVER', 'INDEPENDIENTE', 'RACING', 'ESTUDIANTES']):
            return 'ARGENTINA'
        elif any(indicator in team_upper for indicator in ['NACIONAL', 'PENAROL']):
            return 'URUGUAY'
        elif any(indicator in team_upper for indicator in ['COLO_COLO', 'UNIVERSIDAD']):
            return 'CHILE'
        elif any(indicator in team_upper for indicator in ['MILLONARIOS', 'NACIONAL', 'ONCE_CALDAS']):
            return 'COLOMBIA'
        elif any(indicator in team_upper for indicator in ['BOLIVAR', 'STRONGEST']):
            return 'BOLIVIA'
        elif any(indicator in team_upper for indicator in ['BARCELONA', 'EMELEC']):
            return 'ECUADOR'
        elif any(indicator in team_upper for indicator in ['CARACAS']):
            return 'VENEZUELA'
        
        return None