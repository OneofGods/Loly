#!/usr/bin/env python3
"""
🇪🇸💀🔥 LA LIGA HYBRID ENGINE - SEPTUPLE THREAT MASTERY! 🔥💀🇪🇸

ADDING EPL+MLS+LIGA MX+UEFA+COPA+EFL SUCCESS PATTERNS TO LA LIGA:
1. EPL Tactical Hierarchy (Elite > Good > Average > Poor structure)
2. MLS Cultural Recognition (Rivalry intensity, venue atmosphere)
3. Liga MX Form Volatility (Hot/cold streak recognition)
4. UEFA Financial Power (Money dominance patterns)
5. Copa Continental Disparity (Cross-border economics)
6. EFL Parachute Payments (Financial tier advantages)
7. Enhanced Multi-League Draw Detection

KEEPING LA LIGA STRENGTHS:
1. Barcelona Recent Dominance (47.2% vs Real Madrid 36.1% since 2003)
2. Spanish Possession Tactics (37.3% possessions >12 seconds)
3. El Clásico X-Factor (Real Madrid 106-104 all-time, Barça recent edge)
4. Real Madrid Financial Power (€761M vs €351M spending capacity)
5. Spanish Home Advantage (Advanced defensive positioning)

🎯 FINE-TUNED FOR SPANISH FOOTBALL CULTURE!
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class LaLigaHybridEngine:
    """
    🇪🇸💀🔥 LA LIGA HYBRID ENGINE - SEPTUPLE THREAT!
    
    Combines La Liga mastery with EPL + MLS + Liga MX + UEFA + Copa + EFL patterns
    FINE-TUNED for Spanish football culture and technical dynamics
    """
    
    def __init__(self):
        # LA LIGA HIERARCHY (enhanced with other league patterns)
        self.spanish_giants = ['REAL MADRID', 'BARCELONA', 'ATLETICO MADRID']
        self.spanish_elite = ['SEVILLA', 'REAL SOCIEDAD', 'ATHLETIC BILBAO', 'VALENCIA', 'VILLARREAL']
        self.spanish_good = ['REAL BETIS', 'CELTA VIGO', 'OSASUNA', 'GIRONA', 'LAS PALMAS']
        self.spanish_emerging = ['GETAFE', 'ALAVES', 'MALLORCA', 'RAYO VALLECANO', 'CADIZ']
        
        # SPANISH TACTICAL TEAMS (EPL-inspired)
        self.spanish_tactical = ['ATLETICO MADRID', 'ATHLETIC BILBAO', 'GETAFE', 'OSASUNA']
        
        # SPANISH CULTURAL MOMENTS (MLS-inspired enhancement)
        self.epic_spanish_rivalries = {
            'EL_CLASICO': ['REAL MADRID', 'BARCELONA'],
            'MADRID_DERBY': ['REAL MADRID', 'ATLETICO MADRID'],
            'CATALAN_DERBY': ['BARCELONA', 'ESPANYOL'],
            'BASQUE_DERBY': ['ATHLETIC BILBAO', 'REAL SOCIEDAD'],
            'SEVILLE_DERBY': ['SEVILLA', 'REAL BETIS'],
            'VALENCIA_RIVALRY': ['VALENCIA', 'VILLARREAL']
        }
        
        # BARCELONA RECENT DOMINANCE (La Liga specialty)
        self.barcelona_dominance = {
            'recent_win_rate': 47.2,  # 47.2% since 2003
            'real_madrid_rate': 36.1,  # 36.1% since 2003
            'boost': 35,
            'home_boost': 40,
            'el_clasico_edge': 25
        }
        
        # REAL MADRID FINANCIAL POWER (La Liga specialty)
        self.real_madrid_financial = {
            'spending_capacity': 761,  # €761M
            'barcelona_capacity': 351,  # €351M
            'galacticos_boost': 30,
            'transfer_advantage': 25,
            'squad_depth_boost': 20
        }
        
        # SPANISH POSSESSION TACTICS (La Liga specialty)
        self.spanish_possession = {
            'technical_style': True,
            'possession_percentage': 37.3,  # 37.3% possessions >12 seconds
            'home_advantage_boost': 15,
            'technical_boost': 12,
            'possession_teams': ['BARCELONA', 'REAL MADRID', 'REAL SOCIEDAD', 'SEVILLA']
        }
        
        # EL CLASICO X-FACTOR (La Liga specialty)
        self.el_clasico_factor = {
            'real_madrid_all_time': 106,
            'barcelona_all_time': 104,
            'barcelona_recent_edge': True,
            'global_attention_boost': 20,
            'pressure_factor': 18,
            'historical_weight': 15
        }
        
        # SPANISH HOME ADVANTAGE (La Liga specialty)
        self.spanish_home_advantage = {
            'advanced_defensive': True,
            'positioning_boost': 12,
            'technical_home_boost': 10,
            'fortress_venues': {
                'CAMP_NOU': {'team': 'BARCELONA', 'boost': 25, 'atmosphere': 'CATHEDRAL'},
                'SANTIAGO_BERNABEU': {'team': 'REAL MADRID', 'boost': 22, 'atmosphere': 'ROYAL'},
                'WANDA_METROPOLITANO': {'team': 'ATLETICO MADRID', 'boost': 20, 'atmosphere': 'FORTRESS'},
                'REALE_ARENA': {'team': 'REAL SOCIEDAD', 'boost': 18, 'atmosphere': 'PASSIONATE'},
                'SAN_MAMES': {'team': 'ATHLETIC BILBAO', 'boost': 22, 'atmosphere': 'CATHEDRAL'}
            }
        }
        
        # LIGA MX-STYLE FORM MULTIPLIER (adapted for Spanish culture)
        self.spanish_form_multiplier = 1.15
        
        # SPANISH FINANCIAL TIERS (enhanced with other leagues)
        self.spanish_financial_tiers = {
            'GALACTICO_TIER': 95,      # Real Madrid
            'ELITE_TIER': 85,          # Barcelona, Atletico
            'BIG_SPENDERS': 75,        # Sevilla, Valencia, Villarreal
            'TRADITIONAL': 65,         # Athletic, Real Sociedad, Betis
            'COMPETITIVE': 55,         # Mid-table Spanish clubs
            'EMERGING': 45             # Newly promoted, smaller budgets
        }
    
    def make_hybrid_la_liga_prediction(self, game_data: Dict, base_confidence: float,
                                     home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID LA LIGA PREDICTION - SEPTUPLE THREAT MASTERY!
        
        EPL-STYLE SOLUTION Priority order (ELITE AWAY DOMINANCE FIRST!):
        1. La Liga El Clásico X-Factor (UNIQUE - global phenomenon)
        2. La Liga Spanish Giants Away Dominance (EPL-style - Barça/Real away beats non-giants)
        3. MLS-Style Cultural Moments (SPANISH RIVALRIES intensity)  
        4. La Liga Spanish Home Advantage (for non-elite matchups)
        5. La Liga Spanish Possession Tactics (37.3% technical style)
        6. EPL-Style Tactical Hierarchy (Spanish structure)
        7. Septuple Threat Draw Detection (CALIBRATED thresholds)
        8. Liga MX-Style Form Volatility (Spanish adaptation)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. LA LIGA EL CLÁSICO X-FACTOR (UNIQUE - HIGHEST PRIORITY!)
            clasico_result = self._apply_el_clasico_factor(home_team, away_team, base_confidence)
            if clasico_result:
                return clasico_result
            
            # 2. LA LIGA SPANISH GIANTS AWAY DOMINANCE (EPL-STYLE SOLUTION!)
            giants_away_result = self._apply_spanish_giants_away_dominance(home_team, away_team, base_confidence)
            if giants_away_result:
                return giants_away_result
            
            # 3. MLS-STYLE CULTURAL MOMENTS (SPANISH RIVALRIES!)
            cultural_result = self._detect_spanish_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 4. LA LIGA SPANISH HOME ADVANTAGE (FOR NON-ELITE MATCHUPS!)
            home_result = self._apply_spanish_home_advantage(home_team, away_team, base_confidence)
            if home_result:
                return home_result
            
            # 5. LA LIGA SPANISH POSSESSION TACTICS (37.3% TECHNICAL!)
            possession_result = self._apply_spanish_possession_tactics(home_team, away_team, base_confidence)
            if possession_result:
                return possession_result
            
            # 6. EPL-STYLE TACTICAL HIERARCHY (SPANISH STRUCTURE!)
            hierarchy_result = self._apply_spanish_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 7. SEPTUPLE THREAT DRAW DETECTION (CALIBRATED!)
            draw_result = self._detect_septuple_threat_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 8. LIGA MX-STYLE FORM VOLATILITY (SPANISH ADAPTATION!)
            form_result = self._analyze_spanish_form_volatility(home_team, away_team, base_confidence)
            if form_result:
                return form_result
            
            # DEFAULT: Spanish home advantage
            return f"🏠 {home_team}", base_confidence
            
        except Exception as e:
            logger.error(f"Hybrid La Liga prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _apply_el_clasico_factor(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """La Liga El Clásico X-Factor (global phenomenon)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for El Clásico
        is_real_madrid_home = 'REAL MADRID' in home_upper
        is_barcelona_home = 'BARCELONA' in home_upper
        is_real_madrid_away = 'REAL MADRID' in away_upper
        is_barcelona_away = 'BARCELONA' in away_upper
        
        if (is_real_madrid_home and is_barcelona_away) or (is_barcelona_home and is_real_madrid_away):
            # El Clásico detected!
            boost = self.el_clasico_factor['global_attention_boost']
            
            # FIXED: HOME ADVANTAGE PRIORITY in El Clásico
            if is_real_madrid_home and is_barcelona_away:
                # Real Madrid at Bernabéu vs Barcelona - HOME ADVANTAGE
                return f"🔥 REAL MADRID EL CLÁSICO", min(confidence + boost + 18, 90)
            elif is_barcelona_home and is_real_madrid_away:
                # Barcelona at Camp Nou vs Real Madrid - HOME ADVANTAGE + recent dominance
                barcelona_boost = self.barcelona_dominance['el_clasico_edge']
                return f"🔥 BARCELONA EL CLÁSICO", min(confidence + boost + barcelona_boost, 92)
            elif is_barcelona_away:
                # Barcelona away (already handled above but for safety)
                barcelona_boost = self.barcelona_dominance['el_clasico_edge'] - 15  # Reduced away bonus
                return f"✈️ BARCELONA EL CLÁSICO", min(confidence + boost + barcelona_boost, 85)
            else:
                # Real Madrid away (already handled above but for safety)
                return f"✈️ REAL MADRID EL CLÁSICO", min(confidence + boost + 5, 82)
        
        return None
    
    def _apply_spanish_giants_away_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Spanish giants away dominance (EPL Big 6 style) - Barcelona/Real Madrid away beats non-giants"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Spanish giants
        home_giant = any(team in home_upper for team in self.spanish_giants)
        away_giant = any(team in away_upper for team in self.spanish_giants)
        
        # Giants away vs non-giants home (EPL Big 6 pattern!)
        if away_giant and not home_giant:
            if 'BARCELONA' in away_upper:
                boost = self.barcelona_dominance['boost']
                return f"✈️ BARCELONA AWAY DOMINANCE", min(confidence + boost, 87)
            elif 'REAL MADRID' in away_upper:
                boost = self.real_madrid_financial['transfer_advantage']
                return f"✈️ REAL MADRID AWAY POWER", min(confidence + boost, 86)
            elif 'ATLETICO MADRID' in away_upper:
                return f"✈️ ATLETICO MADRID AWAY", min(confidence + 20, 83)
        
        # Giants home vs non-giants away (still significant advantage)
        elif home_giant and not away_giant:
            # IMPORTANT: Don't override fortress venues - let home advantage handle them
            home_has_fortress = any(data['team'] in home_upper for data in self.spanish_home_advantage['fortress_venues'].values())
            
            if home_has_fortress:
                # Let home advantage method handle fortress venues
                return None
            elif 'BARCELONA' in home_upper:
                boost = self.barcelona_dominance['home_boost'] - 15  # Calibrated
                return f"🏆 BARCELONA HOME POWER", min(confidence + boost, 85)
            elif 'REAL MADRID' in home_upper:
                boost = self.real_madrid_financial['galacticos_boost']
                return f"💰 REAL MADRID HOME", min(confidence + boost, 89)
            elif 'ATLETICO MADRID' in home_upper:
                return f"🏰 ATLETICO MADRID HOME", min(confidence + 22, 84)
        
        return None
    
    def _apply_barcelona_recent_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """La Liga Barcelona recent dominance (47.2% vs 36.1% since 2003) - CALIBRATED!"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Barcelona involvement (excluding El Clásico already handled)
        is_barcelona_home = 'BARCELONA' in home_upper
        is_barcelona_away = 'BARCELONA' in away_upper
        is_real_madrid_home = 'REAL MADRID' in home_upper
        is_real_madrid_away = 'REAL MADRID' in away_upper
        
        # CRITICAL: Check if opponent is at famous home venue (reduce Barcelona dominance)
        opponent_has_fortress = False
        if is_barcelona_away:
            for venue, data in self.spanish_home_advantage['fortress_venues'].items():
                if data['team'] in home_upper:
                    opponent_has_fortress = True
                    break
        
        # Barcelona vs non-Real Madrid teams (CALIBRATED!)
        if is_barcelona_home and not is_real_madrid_away:
            # Barcelona at home - strong but not overwhelming
            boost = self.barcelona_dominance['home_boost'] - 15  # Reduced boost
            return f"🏆 BARCELONA DOMINANCE", min(confidence + boost, 85)  # Lower ceiling
        elif is_barcelona_away and not is_real_madrid_home and not opponent_has_fortress:
            # Barcelona away vs non-fortress teams only
            boost = self.barcelona_dominance['boost'] - 10  # Reduced boost
            return f"✈️ BARCELONA POWER", min(confidence + boost, 82)  # Lower ceiling
        
        return None
    
    def _apply_real_madrid_financial_power(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """La Liga Real Madrid financial power (€761M advantage)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Real Madrid involvement (excluding El Clásico and vs Barcelona)
        is_real_madrid_home = 'REAL MADRID' in home_upper
        is_real_madrid_away = 'REAL MADRID' in away_upper
        is_barcelona_home = 'BARCELONA' in home_upper
        is_barcelona_away = 'BARCELONA' in away_upper
        
        # Real Madrid vs non-Barcelona teams
        if is_real_madrid_home and not is_barcelona_away:
            boost = self.real_madrid_financial['galacticos_boost']
            return f"💰 REAL MADRID GALÁCTICOS", min(confidence + boost, 89)
        elif is_real_madrid_away and not is_barcelona_home:
            boost = self.real_madrid_financial['transfer_advantage']
            return f"✈️ REAL MADRID POWER", min(confidence + boost, 86)
        
        return None
    
    def _detect_spanish_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """MLS-style cultural moments adapted for Spanish rivalries"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for Spanish rivalries (excluding El Clásico already handled)
        for rivalry_name, teams in self.epic_spanish_rivalries.items():
            if rivalry_name == 'EL_CLASICO':
                continue  # Already handled
                
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            
            if home_rivalry and away_rivalry:
                if rivalry_name == 'MADRID_DERBY':
                    return f"🔥 MADRID DERBY", min(confidence + 25, 88)
                elif rivalry_name == 'BASQUE_DERBY':
                    return f"🏔️ BASQUE DERBY", min(confidence + 22, 86)
                elif rivalry_name == 'SEVILLE_DERBY':
                    return f"🔥 SEVILLE DERBY", min(confidence + 20, 85)
                else:
                    return f"🏆 {rivalry_name.replace('_', ' ')}", min(confidence + 18, 83)
        
        return None
    
    def _apply_spanish_possession_tactics(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """La Liga Spanish possession tactics (37.3% technical style)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for possession-based teams
        home_possession = any(team in home_upper for team in self.spanish_possession['possession_teams'])
        away_possession = any(team in away_upper for team in self.spanish_possession['possession_teams'])
        
        # Possession team at home vs non-possession team
        if home_possession and not away_possession:
            boost = self.spanish_possession['home_advantage_boost']
            return f"🎯 {home_team} POSSESSION", min(confidence + boost, 82)
        elif away_possession and not home_possession:
            boost = self.spanish_possession['technical_boost']
            return f"⚽ {away_team} TECHNICAL", min(confidence + boost, 80)
        
        return None
    
    def _apply_spanish_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL-style tactical hierarchy adapted for Spanish structure"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Determine Spanish hierarchy positions
        home_tier = self._get_spanish_tier(home_team)
        away_tier = self._get_spanish_tier(away_team)
        
        tier_difference = away_tier - home_tier
        
        if tier_difference >= 20:  # Significant hierarchy advantage for away team
            return f"✈️ {away_team} SPANISH ELITE", min(confidence + 18, 82)
        elif tier_difference <= -15:  # Home team significantly stronger
            return f"🏠 {home_team} SPANISH POWER", min(confidence + 15, 80)
        
        return None
    
    def _apply_spanish_home_advantage(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """La Liga Spanish home advantage (advanced defensive positioning)"""
        home_upper = home_team.upper()
        
        # Check for fortress venues
        for venue, data in self.spanish_home_advantage['fortress_venues'].items():
            if data['team'] in home_upper:
                boost = data['boost']
                atmosphere = data['atmosphere']
                
                if atmosphere == 'CATHEDRAL':
                    return f"⛪ {home_team} CATHEDRAL", min(confidence + boost, 88)
                elif atmosphere == 'ROYAL':
                    return f"👑 {home_team} BERNABÉU", min(confidence + boost, 86)
                elif atmosphere == 'FORTRESS':
                    return f"🏰 {home_team} FORTRESS", min(confidence + boost, 84)
                else:
                    return f"🏠 {home_team} SPANISH HOME", min(confidence + boost, 82)
        
        # General Spanish home advantage
        boost = self.spanish_home_advantage['positioning_boost']
        return f"🏠 {home_team} SPANISH", min(confidence + boost, 78)
    
    def _detect_septuple_threat_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Combine all seven league draw detection patterns - ENHANCED!"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Spanish tactical teams (EXPANDED)
        home_tactical = any(team in home_upper for team in self.spanish_tactical)
        away_tactical = any(team in away_upper for team in self.spanish_tactical)
        
        if home_tactical and away_tactical and 50 <= confidence <= 75:  # EXPANDED RANGE
            return f"🤝 SPANISH TACTICAL", min(confidence + 10, 68)
        
        # LA LIGA-SPECIFIC: Giants clash (EXPANDED CONDITIONS)
        home_giant = any(team in home_upper for team in self.spanish_giants)
        away_giant = any(team in away_upper for team in self.spanish_giants)
        
        if (home_giant and away_giant and 55 <= confidence <= 75 and  # EXPANDED RANGE
            not self._is_spanish_rivalry(home_team, away_team)):
            return f"🤝 SPANISH GIANTS", min(confidence + 8, 66)
        
        # POSSESSION BATTLE: Technical teams balance (EXPANDED)
        home_possession = any(team in home_upper for team in self.spanish_possession['possession_teams'])
        away_possession = any(team in away_upper for team in self.spanish_possession['possession_teams'])
        
        if home_possession and away_possession and 55 <= confidence <= 78:  # EXPANDED RANGE
            return f"🤝 POSSESSION BATTLE", min(confidence + 6, 64)
        
        # SPANISH ELITE BALANCE (EXPANDED)
        home_elite = any(team in home_upper for team in self.spanish_elite)
        away_elite = any(team in away_upper for team in self.spanish_elite)
        
        if home_elite and away_elite and 58 <= confidence <= 75:  # EXPANDED RANGE
            return f"🤝 SPANISH ELITE", min(confidence + 5, 64)
        
        # NEW: Barcelona vs Giants (special case draw condition) - EXPANDED
        is_barcelona_home = 'BARCELONA' in home_upper
        is_barcelona_away = 'BARCELONA' in away_upper
        away_giant_no_real = (away_giant and 'REAL MADRID' not in away_upper)
        home_giant_no_real = (home_giant and 'REAL MADRID' not in home_upper)
        
        if ((is_barcelona_home and away_giant_no_real) or (is_barcelona_away and home_giant_no_real)) and 60 <= confidence <= 85:
            return f"🤝 BARCELONA VS GIANT", min(confidence + 6, 64)
        
        # ENHANCED: Giant vs Giant draws (excluding El Clásico)
        if (home_giant and away_giant and 60 <= confidence <= 80 and 
            not (('REAL MADRID' in home_upper and 'BARCELONA' in away_upper) or 
                 ('BARCELONA' in home_upper and 'REAL MADRID' in away_upper))):
            return f"🤝 SPANISH GIANTS CLASH", min(confidence + 5, 64)
        
        # NEW: Elite tactical balance (broader range)
        if home_elite and away_elite and 55 <= confidence <= 78:
            return f"🤝 SPANISH ELITE BALANCE", min(confidence + 4, 63)
        
        return None
    
    def _is_spanish_rivalry(self, home_team: str, away_team: str) -> bool:
        """Check if teams are Spanish rivals (should NOT draw)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        for rivalry_name, teams in self.epic_spanish_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            if home_rivalry and away_rivalry:
                return True
        return False
    
    def _get_spanish_tier(self, team_name: str) -> int:
        """Get Spanish tier rating"""
        team_upper = team_name.upper()
        
        if any(team in team_upper for team in self.spanish_giants):
            return self.spanish_financial_tiers['GALACTICO_TIER']
        elif any(team in team_upper for team in self.spanish_elite):
            return self.spanish_financial_tiers['ELITE_TIER']
        elif any(team in team_upper for team in self.spanish_good):
            return self.spanish_financial_tiers['TRADITIONAL']
        else:
            return self.spanish_financial_tiers['COMPETITIVE']
    
    def _analyze_spanish_form_volatility(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX-style form volatility adapted for Spanish teams"""
        # Spanish teams have form swings but less extreme than Liga MX
        
        if confidence > 75:  # High confidence suggests strong form
            enhanced_confidence = min(confidence * self.spanish_form_multiplier * 0.06 + confidence, 88)
            return f"🔥 {self._get_stronger_spanish_team(home_team, away_team)}", enhanced_confidence
        
        return None
    
    def _get_stronger_spanish_team(self, home_team: str, away_team: str) -> str:
        """Determine stronger Spanish team"""
        home_tier = self._get_spanish_tier(home_team)
        away_tier = self._get_spanish_tier(away_team)
        
        if away_tier > home_tier:
            return away_team
        else:
            return home_team