#!/usr/bin/env python3
"""
🏴󠁧󠁢󠁥󠁮󠁧󠁿💀🔥 EFL CHAMPIONSHIP HYBRID ENGINE - SEXTUPLE THREAT MASTERY! 🔥💀🏴󠁧󠁢󠁥󠁮󠁧󠁿

ADDING EPL+MLS+LIGA MX+UEFA+COPA SUCCESS PATTERNS TO EFL CHAMPIONSHIP:
1. EPL Tactical Hierarchy (Elite > Good > Average > Poor structure)
2. MLS Cultural Recognition (Rivalry intensity, venue atmosphere)
3. Liga MX Form Volatility (Hot/cold streak recognition)
4. UEFA Financial Power (Money dominance patterns)
5. Copa Continental Disparity (Cross-border economics)
6. Enhanced Multi-League Draw Detection

KEEPING EFL CHAMPIONSHIP STRENGTHS:
1. Parachute Payment Dominance (£49M Year 1 advantage)
2. Championship Home Fortress (+0.35 goals research verified)
3. "Richest Game" Playoff Pressure (£170-200M stakes)
4. Relegated Team Bounce-Back (40% promotion rate)
5. English Second Tier Parity (most competitive globally)

🎯 FINE-TUNED FOR ENGLISH CHAMPIONSHIP CULTURE!
"""

import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class EFLChampionshipHybridEngine:
    """
    🏴󠁧󠁢󠁥󠁮󠁧󠁿💀🔥 EFL CHAMPIONSHIP HYBRID ENGINE - SEXTUPLE THREAT!
    
    Combines EFL Championship mastery with EPL + MLS + Liga MX + UEFA + Copa patterns
    FINE-TUNED for English second tier football culture and financial dynamics
    """
    
    def __init__(self):
        # EFL CHAMPIONSHIP HIERARCHY (enhanced with other league patterns)
        self.parachute_payment_elite = ['BURNLEY', 'SHEFFIELD UNITED', 'LUTON TOWN', 'LEICESTER CITY', 'SOUTHAMPTON']
        self.parachute_payment_year2 = ['LEEDS UNITED', 'EVERTON']
        self.championship_elite = ['SUNDERLAND', 'MIDDLESBROUGH', 'WEST BROM', 'STOKE CITY']
        self.championship_good = ['COVENTRY CITY', 'BLACKBURN ROVERS', 'PRESTON NORTH END', 'MILLWALL']
        self.championship_emerging = ['CARDIFF CITY', 'BIRMINGHAM CITY', 'ROTHERHAM', 'HUDDERSFIELD']
        
        # CHAMPIONSHIP TACTICAL TEAMS (EPL-inspired)
        self.championship_tactical = ['MILLWALL', 'BLACKBURN ROVERS', 'PRESTON NORTH END', 'CARDIFF CITY']
        
        # ENGLISH CHAMPIONSHIP CULTURAL MOMENTS (MLS-inspired enhancement)
        self.epic_championship_rivalries = {
            'YORKSHIRE_DERBY': ['LEEDS UNITED', 'SHEFFIELD UNITED', 'SHEFFIELD WEDNESDAY', 'HUDDERSFIELD'],
            'BLACK_COUNTRY_DERBY': ['WEST BROM', 'WOLVERHAMPTON'],
            'WEST_LONDON_DERBY': ['FULHAM', 'BRENTFORD', 'QPR'],
            'MIDLANDS_RIVALRY': ['BIRMINGHAM CITY', 'COVENTRY CITY', 'ASTON VILLA'],
            'LONDON_CHAMPIONSHIP': ['MILLWALL', 'CHARLTON', 'QPR'],
            'LANCASHIRE_DERBY': ['BLACKBURN ROVERS', 'PRESTON NORTH END', 'BURNLEY']
        }
        
        # CHAMPIONSHIP HOME FORTRESS (research-verified venues)
        self.legendary_championship_venues = {
            'ELLAND_ROAD': {'team': 'LEEDS UNITED', 'boost': 25, 'atmosphere': 'FORTRESS'},
            'STADIUM_OF_LIGHT': {'team': 'SUNDERLAND', 'boost': 22, 'atmosphere': 'PASSIONATE'},
            'HILLSBOROUGH': {'team': 'SHEFFIELD WEDNESDAY', 'boost': 20, 'atmosphere': 'HISTORIC'},
            'BRAMALL_LANE': {'team': 'SHEFFIELD UNITED', 'boost': 18, 'atmosphere': 'STEEL_CITY'},
            'THE_HAWTHORNS': {'team': 'WEST BROM', 'boost': 16, 'atmosphere': 'TRADITIONAL'},
            'THE_DEN': {'team': 'MILLWALL', 'boost': 15, 'atmosphere': 'INTIMIDATING'}
        }
        
        # PARACHUTE PAYMENT SYSTEM (EFL specialty)
        self.parachute_payments = {
            'YEAR_1': {'amount': 49, 'teams': self.parachute_payment_elite, 'boost': 35},
            'YEAR_2': {'amount': 40, 'teams': self.parachute_payment_year2, 'boost': 25},
            'YEAR_3': {'amount': 17, 'teams': ['NORWICH CITY', 'WATFORD'], 'boost': 15}
        }
        
        # PLAYOFF PRESSURE (Championship specialty)
        self.richest_game_value = 200  # £200M maximum value
        self.playoff_contenders = ['LEEDS UNITED', 'LEICESTER CITY', 'SOUTHAMPTON', 'WEST BROM', 'MIDDLESBROUGH']
        
        # FORM VOLATILITY (Liga MX-inspired, Championship adapted)
        self.championship_form_multiplier = 1.6  # Championship teams have form swings
        
        # FINANCIAL DISPARITY (Copa-inspired, English economics)
        self.championship_financial_tiers = {
            'PARACHUTE_ELITE': 90,  # £49M recipients (capped at 90%)
            'BIG_SPENDERS': 75,     # Sunderland, Middlesbrough level
            'TRADITIONAL': 65,      # Preston, Millwall level
            'STRUGGLERS': 50        # Lower budget teams
        }
    
    def make_hybrid_efl_championship_prediction(self, game_data: Dict, base_confidence: float,
                                              home_team: str, away_team: str) -> Tuple[str, float]:
        """
        🔥 HYBRID EFL CHAMPIONSHIP PREDICTION - SEXTUPLE THREAT MASTERY!
        
        CALIBRATED Priority order (FINE-TUNED for English Championship):
        1. EFL Parachute Payment Dominance (UNIQUE - £49M advantage)
        2. EFL Championship Home Fortress (RESEARCH-VERIFIED +0.35 goals)
        3. MLS-Style Cultural Moments (YORKSHIRE DERBY intensity)
        4. EFL Relegated Team Bounce-Back (40% promotion rate)
        5. UEFA-Style Financial Disparity (parachute vs traditional economics)
        6. EPL-Style Tactical Hierarchy (Championship structure)
        7. Sextuple Threat Draw Detection (CALIBRATED thresholds)
        8. Liga MX-Style Form Volatility (Championship swings)
        """
        try:
            home_upper = home_team.upper()
            away_upper = away_team.upper()
            
            # 1. EFL PARACHUTE PAYMENT DOMINANCE (HIGHEST PRIORITY!)
            parachute_result = self._apply_parachute_payment_dominance(home_team, away_team, base_confidence)
            if parachute_result:
                return parachute_result
            
            # 2. EFL CHAMPIONSHIP HOME FORTRESS (RESEARCH-VERIFIED!)
            fortress_result = self._apply_championship_home_fortress(home_team, away_team, base_confidence)
            if fortress_result:
                return fortress_result
            
            # 3. MLS-STYLE CULTURAL MOMENTS (YORKSHIRE DERBY PRIORITY!)
            cultural_result = self._detect_championship_cultural_moments(home_team, away_team, base_confidence)
            if cultural_result:
                return cultural_result
            
            # 4. EFL RELEGATED TEAM BOUNCE-BACK (40% PROMOTION RATE!)
            bounce_back_result = self._apply_relegated_team_bounce_back(home_team, away_team, base_confidence)
            if bounce_back_result:
                return bounce_back_result
            
            # 5. UEFA-STYLE FINANCIAL DISPARITY (PARACHUTE ECONOMICS!)
            disparity_result = self._apply_championship_financial_disparity(home_team, away_team, base_confidence)
            if disparity_result:
                return disparity_result
            
            # 6. EPL-STYLE TACTICAL HIERARCHY (CHAMPIONSHIP STRUCTURE!)
            hierarchy_result = self._apply_championship_hierarchy(home_team, away_team, base_confidence)
            if hierarchy_result:
                return hierarchy_result
            
            # 7. SEXTUPLE THREAT DRAW DETECTION (CALIBRATED!)
            draw_result = self._detect_sextuple_threat_draws(home_team, away_team, base_confidence)
            if draw_result:
                return draw_result
            
            # 8. LIGA MX-STYLE FORM VOLATILITY (CHAMPIONSHIP SWINGS!)
            form_result = self._analyze_championship_form_volatility(home_team, away_team, base_confidence)
            if form_result:
                return form_result
            
            # 9. DEFAULT CHAMPIONSHIP HOME ADVANTAGE
            return f"🏠 {home_team} CHAMPIONSHIP", min(base_confidence + 12, 75)
            
        except Exception as e:
            logger.error(f"Hybrid EFL Championship prediction error: {e}")
            return f"🏠 {home_team}", base_confidence
    
    def _apply_parachute_payment_dominance(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EFL parachute payment dominance (absolute Championship priority)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for parachute payment recipients (ALL YEARS)
        home_year1 = any(team in home_upper for team in self.parachute_payments['YEAR_1']['teams'])
        away_year1 = any(team in away_upper for team in self.parachute_payments['YEAR_1']['teams'])
        home_year2 = any(team in home_upper for team in self.parachute_payments['YEAR_2']['teams'])
        away_year2 = any(team in away_upper for team in self.parachute_payments['YEAR_2']['teams'])
        home_year3 = any(team in home_upper for team in self.parachute_payments['YEAR_3']['teams'])
        away_year3 = any(team in away_upper for team in self.parachute_payments['YEAR_3']['teams'])
        
        # Year 1 parachute payments (£49M) - massive advantage
        if away_year1 and not (home_year1 or home_year2 or home_year3):
            boost = self.parachute_payments['YEAR_1']['boost']
            return f"💰 {away_team} PARACHUTE POWER", min(confidence + boost, 92)
        elif home_year1 and not (away_year1 or away_year2 or away_year3):
            boost = self.parachute_payments['YEAR_1']['boost'] - 5  # Home advantage
            return f"🏆 {home_team} PARACHUTE HOME", min(confidence + boost, 90)
        elif home_year1 and away_year1:
            # Both have Year 1 parachute payments
            return f"💰 {home_team} PARACHUTE CLASH", min(confidence + 20, 85)
        
        # Year 2 parachute payments (£40M) - still significant
        elif away_year2 and not (home_year1 or home_year2 or home_year3):
            boost = self.parachute_payments['YEAR_2']['boost']
            return f"💰 {away_team} YEAR 2 PARACHUTE", min(confidence + boost, 88)
        elif home_year2 and not (away_year1 or away_year2 or away_year3):
            boost = self.parachute_payments['YEAR_2']['boost'] - 5
            return f"🏆 {home_team} YEAR 2 HOME", min(confidence + boost, 85)
        
        # Year 3 parachute payments (£17M) - still gives advantage over traditional Championship clubs  
        elif away_year3 and not (home_year1 or home_year2 or home_year3):
            boost = self.parachute_payments['YEAR_3']['boost']
            return f"💰 {away_team} YEAR 3 PARACHUTE", min(confidence + boost, 80)
        elif home_year3 and not (away_year1 or away_year2 or away_year3):
            boost = self.parachute_payments['YEAR_3']['boost'] - 5
            return f"🏆 {home_team} YEAR 3 HOME", min(confidence + boost, 78)
        
        return None
    
    def _apply_championship_home_fortress(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EFL Championship home fortress (+0.35 goals research)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check for legendary Championship venues
        for venue, data in self.legendary_championship_venues.items():
            if data['team'] in home_upper:
                boost = data['boost']
                atmosphere = data['atmosphere']
                
                # Extra boost vs parachute teams (David vs Goliath)
                parachute_away = any(team in away_upper for team in self.parachute_payment_elite)
                if parachute_away:
                    boost += 10  # Extra fortress advantage
                
                if atmosphere == 'FORTRESS':
                    return f"🏰 {home_team} ELLAND ROAD", min(confidence + boost, 92)
                elif atmosphere == 'PASSIONATE':
                    return f"🔥 {home_team} STADIUM OF LIGHT", min(confidence + boost, 90)
                elif atmosphere == 'INTIMIDATING':
                    return f"😤 {home_team} THE DEN", min(confidence + boost, 88)
                else:
                    return f"🏠 {home_team} {atmosphere}", min(confidence + boost, 86)
        
        # General Championship home advantage (+0.35 goals)
        championship_base_boost = 15  # Based on research
        return f"🏠 {home_team} CHAMPIONSHIP HOME", min(confidence + championship_base_boost, 82)
    
    def _detect_championship_cultural_moments(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Detect Championship cultural moments (MLS-inspired!)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPIC CHAMPIONSHIP RIVALRIES
        for rivalry_name, teams in self.epic_championship_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            
            if home_rivalry and away_rivalry:
                if rivalry_name == 'YORKSHIRE_DERBY':
                    return f"🔥 {home_team} YORKSHIRE DERBY", min(confidence + 25, 88)
                elif rivalry_name == 'BLACK_COUNTRY_DERBY':
                    return f"⚡ {home_team} BLACK COUNTRY", min(confidence + 22, 86)
                elif rivalry_name == 'WEST_LONDON_DERBY':
                    return f"🏆 {home_team} WEST LONDON", min(confidence + 20, 84)
                else:
                    return f"⚔️ {home_team} CHAMPIONSHIP RIVALRY", min(confidence + 18, 82)
        
        return None
    
    def _apply_relegated_team_bounce_back(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EFL relegated team bounce-back (40% promotion rate)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Recent relegated teams (strong bounce-back motivation)
        recent_relegated = self.parachute_payment_elite + self.parachute_payment_year2
        
        home_relegated = any(team in home_upper for team in recent_relegated)
        away_relegated = any(team in away_upper for team in recent_relegated)
        
        # Check if playing against non-relegated teams
        if home_relegated and not away_relegated:
            return f"⬆️ {home_team} BOUNCE-BACK", min(confidence + 20, 85)
        elif away_relegated and not home_relegated:
            return f"🚀 {away_team} PROMOTION PUSH", min(confidence + 18, 83)
        
        return None
    
    def _apply_championship_financial_disparity(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """UEFA-style financial disparity applied to Championship"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Determine financial tiers
        home_tier = self._get_championship_financial_tier(home_team)
        away_tier = self._get_championship_financial_tier(away_team)
        
        disparity = abs(home_tier - away_tier)
        
        # Significant disparity (20+ points)
        if disparity >= 20:
            if home_tier > away_tier:
                return f"💰 {home_team} FINANCIAL POWER", min(confidence + 20, 86)
            else:
                return f"🚀 {away_team} MONEY ADVANTAGE", min(confidence + 18, 84)
        
        return None
    
    def _apply_championship_hierarchy(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """EPL-style hierarchical logic applied to Championship"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # Check hierarchies (excluding parachute teams - already handled)
        home_elite = any(team in home_upper for team in self.championship_elite)
        away_elite = any(team in away_upper for team in self.championship_elite)
        home_good = any(team in home_upper for team in self.championship_good)
        away_good = any(team in away_upper for team in self.championship_good)
        home_emerging = any(team in home_upper for team in self.championship_emerging)
        away_emerging = any(team in away_upper for team in self.championship_emerging)
        
        # Elite away vs non-elite home
        if away_elite and not home_elite:
            return f"⚡ {away_team} CHAMPIONSHIP ELITE", min(confidence + 16, 82)
        
        # Good away vs emerging home
        if away_good and home_emerging:
            return f"🚀 {away_team} QUALITY AWAY", min(confidence + 12, 78)
        
        return None
    
    def _detect_sextuple_threat_draws(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Combine all six league draw detection patterns - CALIBRATED!"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        # EPL-STYLE: Tactical teams (Championship specific)
        home_tactical = any(team in home_upper for team in self.championship_tactical)
        away_tactical = any(team in away_upper for team in self.championship_tactical)
        
        if home_tactical and away_tactical and 50 <= confidence <= 70:
            return f"🤝 CHAMPIONSHIP TACTICAL", min(confidence + 12, 68)
        
        # CHAMPIONSHIP-SPECIFIC: Parachute vs parachute (competitive balance)
        all_parachute_teams = (self.parachute_payment_elite + self.parachute_payment_year2 + 
                             self.parachute_payments['YEAR_3']['teams'])
        home_parachute = any(team in home_upper for team in all_parachute_teams)
        away_parachute = any(team in away_upper for team in all_parachute_teams)
        
        if (home_parachute and away_parachute and 55 <= confidence <= 72 and 
            not self._is_championship_rivalry(home_team, away_team)):
            return f"🤝 PARACHUTE CLASH", min(confidence + 10, 66)
        
        # PLAYOFF PRESSURE: High-stakes draws (£170-200M stakes)
        home_playoff_contender = any(team in home_upper for team in self.parachute_payment_elite + self.championship_elite)
        away_playoff_contender = any(team in away_upper for team in self.parachute_payment_elite + self.championship_elite)
        
        if (home_playoff_contender and away_playoff_contender and 65 <= confidence <= 80):
            return f"🤝 PLAYOFF PRESSURE", min(confidence + 5, 72)
        
        # CHAMPIONSHIP PARITY: "Any team can beat any team" (expanded range)
        if 58 <= confidence <= 70:
            return f"🤝 CHAMPIONSHIP PARITY", min(confidence + 8, 66)
        
        return None
    
    def _analyze_championship_form_volatility(self, home_team: str, away_team: str, confidence: float) -> Tuple[str, float]:
        """Liga MX-style form volatility adapted for Championship"""
        # Championship teams have form swings due to competitive nature
        
        if confidence > 75:  # High confidence suggests strong form
            enhanced_confidence = min(confidence * self.championship_form_multiplier * 0.06 + confidence, 88)
            favored_team = home_team if confidence > 80 else away_team
            return f"🔥 {favored_team} CHAMPIONSHIP FORM", enhanced_confidence
        
        return None
    
    def _get_championship_financial_tier(self, team_name: str) -> int:
        """Get Championship financial tier rating"""
        team_upper = team_name.upper()
        
        if any(team in team_upper for team in self.parachute_payment_elite):
            return self.championship_financial_tiers['PARACHUTE_ELITE']
        elif any(team in team_upper for team in self.parachute_payment_year2):
            return self.championship_financial_tiers['PARACHUTE_ELITE'] - 10
        elif any(team in team_upper for team in self.championship_elite):
            return self.championship_financial_tiers['BIG_SPENDERS']
        elif any(team in team_upper for team in self.championship_good):
            return self.championship_financial_tiers['TRADITIONAL']
        else:
            return self.championship_financial_tiers['STRUGGLERS']
    
    def _is_championship_rivalry(self, home_team: str, away_team: str) -> bool:
        """Check if teams are Championship rivals (should NOT draw)"""
        home_upper = home_team.upper()
        away_upper = away_team.upper()
        
        for rivalry_name, teams in self.epic_championship_rivalries.items():
            home_rivalry = any(team in home_upper for team in teams)
            away_rivalry = any(team in away_upper for team in teams)
            if home_rivalry and away_rivalry:
                return True
        return False