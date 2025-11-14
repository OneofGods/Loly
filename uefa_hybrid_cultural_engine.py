#!/usr/bin/env python3
"""
🏆⭐ UEFA HYBRID CULTURAL ENGINE - EPL+MLS+LIGA MX PATTERNS + EUROPEAN MASTERY! ⭐🏆

ADDING EPL+MLS+LIGA MX SUCCESS PATTERNS TO UEFA:
1. EPL Tactical Hierarchy (Elite European powers)
2. MLS Cultural Recognition (Derby intensity, venue atmosphere)
3. Liga MX Form Volatility (Hot/cold streak recognition)
4. Enhanced Draw Detection (All league patterns combined)

KEEPING UEFA STRENGTHS:
1. Real Madrid European Legacy (15 Champions League titles)
2. Financial Fair Play Dynamics (€2.5B prize pool)
3. European Home Variance (47.7% win rate variations)
4. Oil Money vs Tradition Battles (Man City vs heritage clubs)
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class UEFAHybridCulturalEngine:
    """
    🏆⭐ UEFA HYBRID ENGINE - QUADRUPLE THREAT COMBINATION!
    
    Combines UEFA European mastery with EPL + MLS + Liga MX patterns
    """
    
    def __init__(self):
        # UEFA EUROPEAN HIERARCHY (enhanced with other league patterns)
        self.european_giants = ['REAL MADRID', 'BARCELONA', 'BAYERN MUNICH', 'LIVERPOOL', 'MANCHESTER CITY']
        self.european_elite = ['CHELSEA', 'MANCHESTER UNITED', 'PSG', 'JUVENTUS', 'ATLETICO MADRID']
        self.european_good = ['ARSENAL', 'TOTTENHAM', 'BORUSSIA DORTMUND', 'AC MILAN', 'INTER MILAN']
        self.european_emerging = ['NAPOLI', 'NEWCASTLE', 'RB LEIPZIG', 'SEVILLA', 'PORTO']
        
        # UEFA TACTICAL TEAMS (EPL-inspired)
        self.uefa_tactical = ['ATLETICO MADRID', 'CHELSEA', 'JUVENTUS', 'INTER MILAN']
        
        # UEFA CULTURAL MOMENTS (MLS-inspired enhancement)
        self.epic_european_rivalries = {
            'EL_CLASICO': ['REAL MADRID', 'BARCELONA'],
            'MANCHESTER_DERBY': ['MANCHESTER CITY', 'MANCHESTER UNITED'],
            'MERSEYSIDE_DERBY': ['LIVERPOOL', 'EVERTON'],
            'MILAN_DERBY': ['AC MILAN', 'INTER MILAN'],
            'MADRID_DERBY': ['REAL MADRID', 'ATLETICO MADRID'],
            'LONDON_RIVALS': ['CHELSEA', 'ARSENAL', 'TOTTENHAM']
        }
        
        # UEFA VENUE ATMOSPHERE (MLS-style specific analysis)
        self.legendary_european_venues = {
            'BERNABEU': {'team': 'REAL MADRID', 'boost': 30, 'atmosphere': 'LEGENDARY'},
            'CAMP_NOU': {'team': 'BARCELONA', 'boost': 25, 'atmosphere': 'PASSIONATE'},
            'ANFIELD': {'team': 'LIVERPOOL', 'boost': 22, 'atmosphere': 'FORTRESS'},
            'ALLIANZ': {'team': 'BAYERN MUNICH', 'boost': 20, 'atmosphere': 'ELITE'},
            'ETIHAD': {'team': 'MANCHESTER CITY', 'boost': 18, 'atmosphere': 'MODERN'},
            'STAMFORD_BRIDGE': {'team': 'CHELSEA', 'boost': 15, 'atmosphere': 'HISTORIC'}
        }
        
        # REAL MADRID LEGACY (UEFA specialty)
        self.real_madrid_titles = 15  # Most Champions League titles
        self.real_madrid_revenue = 1.065  # €1.065B revenue
        
        # FINANCIAL FAIR PLAY (UEFA unique factor)
        self.ffp_elite_clubs = {
            'REAL MADRID': 95,
            'MANCHESTER CITY': 90,
            'PSG': 85,
            'BAYERN MUNICH': 88,
            'LIVERPOOL': 82
        }
        
        # FORM VOLATILITY (Liga MX-inspired)
        self.european_form_multiplier = 1.5  # European teams have form swings
        
        # OIL MONEY VS TRADITION (UEFA battleground)
        self.oil_money_clubs = ['MANCHESTER CITY', 'PSG', 'NEWCASTLE']
        self.traditional_powers = ['REAL MADRID', 'BARCELONA', 'BAYERN MUNICH', 'LIVERPOOL', 'MANCHESTER UNITED']
    
    def make_hybrid_uefa_prediction(self, game_data: Dict, base_confidence: float,
                                  home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID UEFA PREDICTION - EPL+MLS+LIGA MX+EUROPEAN MASTERY!
        
        Priority order (quadruple threat combination):
        1. UEFA Real Madrid Legacy (keeps European dominance)
        2. UEFA Financial Fair Play (European money power)
        3. EPL-Style Tactical Hierarchy (adds structure)
        4. MLS-Style Cultural Moments (adds rivalry power)
        5. Quadruple Threat Draw Detection (combines all four)
        6. Liga MX-Style Form Volatility (enhanced European swings)
        7. MLS-Style Venue Atmosphere (legendary European stadiums)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. UEFA REAL MADRID LEGACY (HIGHEST PRIORITY!)
            real_madrid_result = self._apply_real_madrid_legacy(home_team, away_team, base_confidence)
            if real_madrid_result:
                return real_madrid_result
            
            # 2. UEFA FINANCIAL FAIR PLAY DOMINANCE (EUROPEAN MONEY POWER!)
            ffp_result = self._apply_uefa_ffp_dominance(home_team, away_team, base_confidence)
            if ffp_result:
                return ffp_result
            
            # 3. EPL-STYLE TACTICAL HIERARCHY (NEW - ADD STRUCTURE!)
            hierarchy_result = self._apply_uefa_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 4. MLS-STYLE CULTURAL MOMENTS (NEW - ADD RIVALRY POWER!)
            cultural_result = self._detect_european_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 5. QUADRUPLE THREAT DRAW DETECTION (COMBINE ALL FOUR!)
            draw_result = self._detect_quadruple_threat_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 6. LIGA MX-STYLE FORM VOLATILITY (ENHANCED EUROPEAN SWINGS!)
            form_result = self._analyze_european_form_volatility(home_team, away_team, base_confidence)
            if form_result:
                return form_result
            
            # 7. MLS-STYLE VENUE ATMOSPHERE (LEGENDARY EUROPEAN STADIUMS!)
            venue_result = self._analyze_european_venue_atmosphere(home_team, away_team, base_confidence)
            if venue_result:
                return venue_result
            
            # 8. DEFAULT EUROPEAN HOME ADVANTAGE
            return f"🏠 {home_team} EUROPEAN", min(base_confidence + 12, 78)
            
        except Exception as e:
            logger.error(f"Hybrid UEFA prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _apply_real_madrid_legacy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """UEFA Real Madrid legacy (absolute European priority)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        real_madrid_identifiers = ['REAL MADRID', 'MADRID', 'R MADRID']
        
        home_real = any(identifier in home_upper for identifier in real_madrid_identifiers)
        away_real = any(identifier in away_upper for identifier in real_madrid_identifiers)
        
        if home_real:
            # Real Madrid at home in Europe (15 titles legacy)
            boost = 30  # Massive European legacy boost
            return f"👑 {home_team} KINGS OF EUROPE", min(confidence + boost, 95)
        elif away_real:
            # Real Madrid away in Europe (European travel masters)
            boost = 25  # Strong away European legacy
            return f"⚡ {away_team} EUROPEAN ROYALTY", min(confidence + boost, 92)
        
        return None
    
    def _apply_uefa_ffp_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """UEFA Financial Fair Play dominance (European money power)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check FFP elite status
        home_ffp = None
        away_ffp = None
        
        for club, rating in self.ffp_elite_clubs.items():
            if club in home_upper:
                home_ffp = rating
            if club in away_upper:
                away_ffp = rating
        
        # FFP elite away vs non-elite home
        if away_ffp and not home_ffp:
            boost = (away_ffp - 70) // 5  # Scale FFP rating to boost
            return f"💰 {away_team} FFP POWER", min(confidence + boost, 90)
        
        # FFP elite at home
        if home_ffp and not away_ffp:
            boost = (home_ffp - 75) // 5  # Slightly less for home
            return f"🏆 {home_team} FFP FORTRESS", min(confidence + boost, 88)
        
        return None
    
    def _apply_uefa_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL-style hierarchical logic applied to UEFA"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check hierarchies
        home_giant = any(team in home_upper for team in self.european_giants)
        away_giant = any(team in away_upper for team in self.european_giants)
        home_elite = any(team in home_upper for team in self.european_elite)
        away_elite = any(team in away_upper for team in self.european_elite)
        home_emerging = any(team in home_upper for team in self.european_emerging)
        away_emerging = any(team in away_upper for team in self.european_emerging)
        
        # European giant away vs non-giant home
        if away_giant and not home_giant:
            return f"🚀 {away_team} EUROPEAN GIANT", min(confidence + 22, 88)
        
        # Elite away vs emerging home
        if away_elite and home_emerging:
            return f"✈️ {away_team} ELITE POWER", min(confidence + 18, 85)
        
        # Giant home vs emerging away
        if home_giant and away_emerging:
            return f"🏆 {home_team} GIANT HOME", min(confidence + 20, 87)
        
        return None
    
    def _detect_european_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect European cultural moments (MLS-inspired!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPIC EUROPEAN RIVALRIES
        for rivalry_name, teams in self.epic_european_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            
            if home_rivalry and away_rivalry:
                if rivalry_name == 'EL_CLASICO':
                    if 'REAL MADRID' in home_upper:
                        return f"👑 {home_team} EL CLÁSICO", min(confidence + 25, 90)
                    else:
                        return f"💙 {home_team} BLAUGRANA", min(confidence + 22, 88)
                elif rivalry_name == 'MANCHESTER_DERBY':
                    return f"🔥 {home_team} MANCHESTER POWER", min(confidence + 20, 86)
                elif rivalry_name == 'MILAN_DERBY':
                    return f"⚡ {home_team} MILAN DERBY", min(confidence + 18, 84)
                else:
                    return f"🏆 {home_team} EUROPEAN RIVALRY", min(confidence + 16, 82)
        
        return None
    
    def _detect_quadruple_threat_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Combine EPL + MLS + Liga MX + UEFA draw detection"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Tactical teams
        home_tactical = any(team in home_upper for team in self.uefa_tactical)
        away_tactical = any(team in away_upper for team in self.uefa_tactical)
        
        if home_tactical and away_tactical:
            return f"🤝 EUROPEAN TACTICAL DRAW", min(confidence + 18, 75)
        
        # MLS-STYLE: Giants often draw (competitive balance)
        home_giant = any(team in home_upper for team in self.european_giants)
        away_giant = any(team in away_upper for team in self.european_giants)
        
        if home_giant and away_giant and 55 <= confidence <= 70:
            return f"🤝 GIANTS EUROPEAN CLASH", min(confidence + 15, 72)
        
        # LIGA MX-STYLE: Close competition (European parity)
        if 60 <= confidence <= 75:  # Close European games often draw
            return f"🤝 EUROPEAN BALANCE", min(confidence + 10, 70)
        
        # UEFA-STYLE: Oil money vs tradition stalemate
        home_oil = any(team in home_upper for team in self.oil_money_clubs)
        away_oil = any(team in away_upper for team in self.oil_money_clubs)
        home_traditional = any(team in home_upper for team in self.traditional_powers)
        away_traditional = any(team in away_upper for team in self.traditional_powers)
        
        if (home_oil and away_traditional) or (home_traditional and away_oil):
            return f"🤝 MONEY VS TRADITION", min(confidence + 12, 68)
        
        return None
    
    def _analyze_european_form_volatility(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX-style form volatility applied to European teams"""
        # European teams have form swings in Champions League
        
        if confidence > 75:  # High confidence suggests strong form
            enhanced_confidence = min(confidence * self.european_form_multiplier * 0.12 + confidence, 92)
            favored_team = home_team if confidence > 80 else away_team
            return f"🔥 {favored_team} EUROPEAN FORM", enhanced_confidence
        
        return None
    
    def _analyze_european_venue_atmosphere(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """MLS-style European venue analysis"""
        home_upper = home_team.upper()
        
        # LEGENDARY EUROPEAN VENUES
        for venue, data in self.legendary_european_venues.items():
            if data['team'] in home_upper:
                atmosphere = data['atmosphere']
                boost = data['boost']
                
                if atmosphere == 'LEGENDARY':
                    return f"🏟️ {home_team} {atmosphere} BERNABÉU", min(confidence + boost, 95)
                elif atmosphere == 'PASSIONATE':
                    return f"💙 {home_team} {atmosphere} CAMP NOU", min(confidence + boost, 92)
                elif atmosphere == 'FORTRESS':
                    return f"🔴 {home_team} {atmosphere} ANFIELD", min(confidence + boost, 90)
                else:
                    return f"🏠 {home_team} {atmosphere}", min(confidence + boost, 88)
        
        return None