#!/usr/bin/env python3
"""
🇲🇽🔥 LIGA MX HYBRID CULTURAL ENGINE - EPL+MLS PATTERNS + MEXICAN MASTERY! 🔥🇲🇽

ADDING EPL+MLS SUCCESS PATTERNS TO LIGA MX:
1. EPL Tactical Hierarchy (Elite > Good > Average > Poor)
2. MLS Cultural Recognition (Rivalry intensity, venue atmosphere)
3. Enhanced Draw Detection (Tactical + emotional parity)

KEEPING LIGA MX STRENGTHS:
1. Mexican Giants Dominance (América, Chivas, Cruz Azul supremacy)
2. Form Volatility Mastery (Hot/cold streak recognition)
3. Liguilla System Logic (Reduced regular season weight)
4. CONCACAF Market Dynamics (International competition effects)
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class LigaMXHybridCulturalEngine:
    """
    🇲🇽🔥 LIGA MX HYBRID ENGINE - TRIPLE THREAT COMBINATION!
    
    Combines Liga MX cultural mastery with EPL tactical hierarchy + MLS cultural recognition
    """
    
    def __init__(self):
        # LIGA MX HIERARCHY (EPL-inspired classification)
        self.mexican_giants = ['AMÉRICA', 'CHIVAS', 'GUADALAJARA', 'CRUZ AZUL', 'PUMAS', 'MONTERREY', 'TIGRES']
        self.liga_mx_elite = ['SANTOS LAGUNA', 'LEÓN', 'PACHUCA', 'TOLUCA', 'ATLAS']
        self.liga_mx_good = ['PUEBLA', 'QUERÉTARO', 'NECAXA', 'TIJUANA', 'MAZATLÁN']
        self.liga_mx_poor = ['FC JUÁREZ', 'CANCÚN FC', 'ATLÉTICO SAN LUIS']
        
        # LIGA MX TACTICAL TEAMS (EPL-inspired)
        self.liga_mx_tactical = ['SANTOS LAGUNA', 'QUERÉTARO', 'FC JUÁREZ', 'PUEBLA']
        
        # LIGA MX CULTURAL MOMENTS (MLS-inspired enhancement)
        self.epic_mexican_rivalries = {
            'CLASICO_NACIONAL': ['AMÉRICA', 'CHIVAS', 'GUADALAJARA'],
            'CLASICO_JOVEN': ['AMÉRICA', 'CRUZ AZUL'],
            'CLASICO_REGIO': ['MONTERREY', 'TIGRES'],
            'CLASICO_TAPATIO': ['CHIVAS', 'ATLAS', 'GUADALAJARA'],
            'CLASICO_POBLANO': ['PUEBLA', 'PACHUCA']
        }
        
        # LIGA MX VENUE ATMOSPHERE (MLS-style specific analysis)
        self.legendary_mexican_venues = {
            'AZTECA': {'team': 'AMÉRICA', 'boost': 25, 'atmosphere': 'LEGENDARY'},
            'AKRON': {'team': 'CHIVAS', 'boost': 20, 'atmosphere': 'PASSIONATE'},
            'AZUL': {'team': 'CRUZ AZUL', 'boost': 18, 'atmosphere': 'FORTRESS'},
            'UNIVERSITARIO': {'team': 'PUMAS', 'boost': 15, 'atmosphere': 'HISTORIC'},
            'BBVA': {'team': 'MONTERREY', 'boost': 15, 'atmosphere': 'MODERN'},
            'VOLCAN': {'team': 'TIGRES', 'boost': 12, 'atmosphere': 'INTIMIDATING'}
        }
        
        # LIGA MX FORM VOLATILITY (Mexican specialty)
        self.form_volatility_multiplier = 1.8  # Mexican teams have extreme swings
        
        # LIGA MX LIGUILLA SYSTEM (unique factor)
        self.liguilla_reduction_factor = 0.7  # Regular season less predictive
        
        # CONCACAF COMPETITION EFFECTS
        self.concacaf_teams = ['AMÉRICA', 'CHIVAS', 'MONTERREY', 'TIGRES', 'CRUZ AZUL', 'PUMAS']
    
    def make_hybrid_liga_mx_prediction(self, game_data: Dict, base_confidence: float,
                                     home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID LIGA MX PREDICTION - EPL+MLS+MEXICAN MASTERY!
        
        Priority order (triple threat combination):
        1. Liga MX Mexican Giants Dominance (keeps Mexican strength)
        2. EPL-Style Tactical Hierarchy (adds structure)
        3. MLS-Style Cultural Moments (adds rivalry power)
        4. Liga MX + EPL + MLS Draw Detection (combines all)
        5. Liga MX Form Volatility (Mexican specialty)
        6. MLS-Style Venue Atmosphere (enhanced Mexican venues)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. LIGA MX MEXICAN GIANTS DOMINANCE (HIGHEST PRIORITY!)
            giants_result = self._apply_mexican_giants_dominance(home_team, away_team, base_confidence)
            if giants_result:
                return giants_result
            
            # 2. EPL-STYLE TACTICAL HIERARCHY (NEW - ADD STRUCTURE!)
            hierarchy_result = self._apply_liga_mx_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 3. MLS-STYLE CULTURAL MOMENTS (NEW - ADD RIVALRY POWER!)
            cultural_result = self._detect_mexican_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 4. TRIPLE THREAT DRAW DETECTION (COMBINE ALL THREE!)
            draw_result = self._detect_triple_threat_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 5. LIGA MX FORM VOLATILITY (MEXICAN SPECIALTY!)
            form_result = self._analyze_mexican_form_volatility(home_team, away_team, base_confidence)
            if form_result:
                return form_result
            
            # 6. MLS-STYLE VENUE ATMOSPHERE (ENHANCED MEXICAN VENUES!)
            venue_result = self._analyze_mexican_venue_atmosphere(home_team, away_team, base_confidence)
            if venue_result:
                return venue_result
            
            # 7. DEFAULT WITH LIGUILLA ADJUSTMENT
            adjusted_confidence = min(base_confidence * self.liguilla_reduction_factor + 10, 75)
            return f"🏠 {home_team} LIGUILLA", adjusted_confidence
            
        except Exception as e:
            logger.error(f"Hybrid Liga MX prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _apply_mexican_giants_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX Mexican Giants dominance (absolute priority)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        home_giant = any(giant in home_upper for giant in self.mexican_giants)
        away_giant = any(giant in away_upper for giant in self.mexican_giants)
        
        # Mexican Giant away vs non-Giant home
        if away_giant and not home_giant:
            boost = self._calculate_mexican_giant_boost(away_team)
            return f"⚡ {away_team} GIGANTE MEXICANO", min(confidence + boost, 92)
        
        # Giant vs Giant (often competitive)
        if home_giant and away_giant:
            return self._handle_giants_clash(home_team, away_team, confidence)
        
        # Giant at home vs non-Giant
        if home_giant and not away_giant:
            boost = self._calculate_mexican_giant_boost(home_team)
            return f"🏆 {home_team} CASA GIGANTE", min(confidence + boost - 5, 88)  # Slightly less than away
        
        return None
    
    def _apply_liga_mx_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL-style hierarchical logic applied to Liga MX"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check hierarchies
        home_elite = any(team in home_upper for team in self.liga_mx_elite)
        away_elite = any(team in away_upper for team in self.liga_mx_elite)
        home_good = any(team in home_upper for team in self.liga_mx_good)
        away_good = any(team in away_upper for team in self.liga_mx_good)
        home_poor = any(team in home_upper for team in self.liga_mx_poor)
        away_poor = any(team in away_upper for team in self.liga_mx_poor)
        
        # Elite away vs non-elite home (EPL-style)
        if away_elite and not home_elite:
            return f"🚀 {away_team} CLASE SUPERIOR", min(confidence + 18, 85)
        
        # Good away vs poor home
        if away_good and home_poor:
            return f"✈️ {away_team} CALIDAD", min(confidence + 12, 80)
        
        # Elite home vs poor away
        if home_elite and away_poor:
            return f"🏠 {home_team} ÉLITE CASA", min(confidence + 15, 83)
        
        return None
    
    def _detect_mexican_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect Mexican cultural moments (MLS-inspired!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPIC MEXICAN DERBIES
        for clasico_name, teams in self.epic_mexican_rivalries.items():
            home_clasico = any(team in home_upper for team in teams)
            away_clasico = any(team in away_upper for team in teams)
            
            if home_clasico and away_clasico:
                if clasico_name == 'CLASICO_NACIONAL':
                    if 'AMÉRICA' in home_upper:
                        return f"🏆 {home_team} CLÁSICO NACIONAL", min(confidence + 22, 88)
                    else:
                        return f"❤️ {home_team} REBAÑO SAGRADO", min(confidence + 20, 86)
                elif clasico_name == 'CLASICO_JOVEN':
                    return f"🔥 {home_team} CLÁSICO JOVEN", min(confidence + 18, 85)
                elif clasico_name == 'CLASICO_REGIO':
                    return f"⚡ {home_team} CLÁSICO REGIO", min(confidence + 16, 83)
                else:
                    return f"🇲🇽 {home_team} CLÁSICO", min(confidence + 14, 82)
        
        return None
    
    def _detect_triple_threat_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Combine EPL + MLS + Liga MX draw detection"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Tactical teams
        home_tactical = any(team in home_upper for team in self.liga_mx_tactical)
        away_tactical = any(team in away_upper for team in self.liga_mx_tactical)
        
        if home_tactical and away_tactical:
            return f"🤝 EMPATE TÁCTICO", min(confidence + 15, 72)
        
        # MLS-STYLE: Giants often draw (competitive balance)
        home_giant = any(team in home_upper for team in self.mexican_giants)
        away_giant = any(team in away_upper for team in self.mexican_giants)
        
        if home_giant and away_giant and 50 <= confidence <= 65:
            return f"🤝 EMPATE DE GIGANTES", min(confidence + 12, 70)
        
        # LIGA MX-STYLE: Liguilla positioning (teams playing for playoffs)
        if 55 <= confidence <= 70:  # Close games often draw in Liga MX
            return f"🤝 EMPATE LIGUILLA", min(confidence + 8, 68)
        
        return None
    
    def _analyze_mexican_form_volatility(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX form volatility analysis (Mexican specialty)"""
        # This would analyze recent form with Mexican volatility multiplier
        # For now, simulate based on confidence range and volatility
        
        if confidence > 70:  # High confidence suggests strong form
            return f"🔥 {home_team if confidence > 75 else away_team} RACHA CALIENTE", min(confidence * self.form_volatility_multiplier * 0.15 + confidence, 90)
        
        return None
    
    def _analyze_mexican_venue_atmosphere(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """MLS-style Mexican venue analysis"""
        home_upper = home_team.upper()
        
        # LEGENDARY MEXICAN VENUES
        for venue, data in self.legendary_mexican_venues.items():
            if data['team'] in home_upper:
                atmosphere = data['atmosphere']
                boost = data['boost']
                
                if atmosphere == 'LEGENDARY':
                    return f"🏟️ {home_team} {atmosphere} AZTECA", min(confidence + boost, 92)
                elif atmosphere == 'PASSIONATE':
                    return f"❤️ {home_team} {atmosphere} REBAÑO", min(confidence + boost, 88)
                elif atmosphere == 'FORTRESS':
                    return f"🏰 {home_team} {atmosphere} AZUL", min(confidence + boost, 85)
                else:
                    return f"🏠 {home_team} {atmosphere}", min(confidence + boost, 83)
        
        return None
    
    def _calculate_mexican_giant_boost(self, team: str) -> float:
        """Calculate Mexican Giant boost"""
        team_upper = team.upper()
        
        if 'AMÉRICA' in team_upper:
            return 25  # Las Águilas
        elif any(team in team_upper for team in ['CHIVAS', 'GUADALAJARA']):
            return 22  # El Rebaño Sagrado
        elif 'CRUZ AZUL' in team_upper:
            return 20  # La Máquina
        elif 'PUMAS' in team_upper:
            return 18  # Los Universitarios
        elif 'MONTERREY' in team_upper:
            return 16  # Rayados
        elif 'TIGRES' in team_upper:
            return 15  # Los Felinos
        else:
            return 12
    
    def _handle_giants_clash(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Handle Mexican Giants clashes"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # América dominance
        if 'AMÉRICA' in home_upper:
            return f"🏆 {home_team} ÁGUILAS PODER", min(confidence + 15, 87)
        elif 'AMÉRICA' in away_upper:
            return f"⚡ {away_team} ÁGUILAS VISITANTE", min(confidence + 12, 85)
        
        # Chivas emotional factor
        elif any(team in home_upper for team in ['CHIVAS', 'GUADALAJARA']):
            return f"❤️ {home_team} REBAÑO SAGRADO", min(confidence + 12, 84)
        elif any(team in away_upper for team in ['CHIVAS', 'GUADALAJARA']):
            return f"⚡ {away_team} ORGULLO TAPATÍO", min(confidence + 10, 82)
        
        # Default giants clash
        else:
            return f"🤝 BATALLA DE GIGANTES", min(confidence + 8, 78)