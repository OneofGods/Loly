#!/usr/bin/env python3
"""
🕐 SPORTS SCHEDULE & TIME ANALYZER - 6TH MCP DIMENSION
The missing piece! Analyzes game scheduling, timing, and availability
"""

import asyncio
import json
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Any, Optional
import logging
import pytz

logger = logging.getLogger(__name__)

class SportsScheduleTimeAnalyzer:
    """
    🕐 6TH MCP DIMENSION: GAMES SCHEDULE & TIME INTELLIGENCE
    
    The missing critical dimension that determines:
    - Which games are actually happening TODAY
    - Accurate live vs upcoming game detection  
    - Timezone-aware scheduling analysis
    - Game availability windows and timing
    """
    
    def __init__(self):
        self.timezone_mapping = {
            'NFL': 'America/New_York',
            'NBA': 'America/New_York', 
            'MLB': 'America/New_York',
            'NHL': 'America/New_York',
            'WNBA': 'America/New_York',
            'MLS': 'America/New_York',
            'EPL': 'Europe/London',
            'LEAGUES_CUP': 'America/Mexico_City',
            'TENNIS': 'America/Toronto',  # Current ATP/WTA tournaments
            'F1': 'Europe/London'
        }
        
        # Sport-specific live game windows (in hours)
        self.live_windows = {
            'NFL': 3.5,      # Long games with overtime
            'NBA': 2.5,      # Basketball games
            'MLB': 3.0,      # Baseball games
            'NHL': 2.5,      # Hockey games
            'WNBA': 2.0,     # Women's basketball
            'MLS': 2.0,      # Soccer matches
            'EPL': 2.0,      # English Premier League
            'LEAGUES_CUP': 2.0,  # Soccer tournament
            'TENNIS': 4.0,   # Can go very long
            'F1': 2.0        # Formula 1 races
        }
        
    async def get_schedule_time_analysis(self, home_team: str, away_team: str, 
                                       sport: str, game_time: str = "", 
                                       venue: str = "") -> Dict[str, Any]:
        """
        🕐 MAIN SCHEDULE & TIME ANALYSIS
        Determines exact game timing, live status, and availability
        """
        try:
            print(f"🕐 SCHEDULE TIME ANALYZER: {away_team} @ {home_team} ({sport})")
            
            # Get current time in appropriate timezone
            sport_timezone = pytz.timezone(self.timezone_mapping.get(sport, 'America/New_York'))
            current_time = datetime.now(sport_timezone)
            
            # Parse game time if provided
            if game_time:
                try:
                    if game_time.endswith('Z'):
                        game_datetime = datetime.fromisoformat(game_time.replace('Z', '+00:00'))
                    else:
                        game_datetime = datetime.fromisoformat(game_time)
                    
                    # Convert to sport timezone
                    if game_datetime.tzinfo is None:
                        game_datetime = sport_timezone.localize(game_datetime)
                    else:
                        game_datetime = game_datetime.astimezone(sport_timezone)
                        
                except Exception as e:
                    logger.warning(f"Error parsing game time {game_time}: {e}")
                    game_datetime = current_time
            else:
                # Default game time based on sport patterns
                game_datetime = self._estimate_game_time(sport, current_time)
            
            # Calculate time analysis
            time_until_game = (game_datetime - current_time).total_seconds() / 3600  # hours
            game_status = self._determine_game_status(time_until_game, sport)
            
            # Analyze scheduling factors
            scheduling_factors = await self._analyze_scheduling_factors(
                home_team, away_team, sport, game_datetime, current_time
            )
            
            # Game availability analysis
            availability_analysis = self._analyze_game_availability(
                sport, game_datetime, current_time, scheduling_factors
            )
            
            # Time-based betting implications
            timing_implications = self._analyze_timing_implications(
                game_status, time_until_game, sport, scheduling_factors
            )
            
            schedule_analysis = {
                "game_timing": {
                    "scheduled_time": game_datetime.isoformat(),
                    "current_time": current_time.isoformat(),
                    "hours_until_game": round(time_until_game, 2),
                    "game_status": game_status,
                    "timezone": sport_timezone.zone
                },
                "scheduling_factors": scheduling_factors,
                "availability_analysis": availability_analysis,
                "timing_implications": timing_implications,
                "schedule_confidence": self._calculate_schedule_confidence(
                    game_status, scheduling_factors, availability_analysis
                ),
                "data_source": "SPORTS_SCHEDULE_TIME_MCP",
                "analysis_timestamp": current_time.isoformat()
            }
            
            print(f"✅ Schedule Analysis: {game_status} ({time_until_game:.1f}h until game)")
            return schedule_analysis
            
        except Exception as e:
            logger.error(f"Error in schedule time analysis: {e}")
            return self._get_fallback_schedule_analysis(home_team, away_team, sport)
    
    def _determine_game_status(self, hours_until_game: float, sport: str) -> str:
        """Determine current game status based on time analysis"""
        live_window = self.live_windows.get(sport, 2.5)
        
        if hours_until_game < -live_window:
            return "FINISHED"
        elif hours_until_game <= 0 and hours_until_game > -live_window:
            return "LIVE"
        elif 0 < hours_until_game <= 2:
            return "STARTING_SOON"
        elif 2 < hours_until_game <= 6:
            return "TODAY"
        elif 6 < hours_until_game <= 24:
            return "TOMORROW"
        else:
            return "FUTURE"
    
    def _estimate_game_time(self, sport: str, current_time: datetime) -> datetime:
        """Estimate game time based on sport patterns"""
        game_time_patterns = {
            'NFL': {'hour': 13, 'days': [3, 6, 0]},    # Thu, Sun, Mon
            'NBA': {'hour': 19, 'days': [1, 2, 3, 5, 6]},  # Tue-Thu, Sat-Sun
            'MLB': {'hour': 19, 'days': list(range(7))},   # Daily
            'WNBA': {'hour': 19, 'days': [2, 4, 6]},      # Wed, Fri, Sun
            'MLS': {'hour': 19, 'days': [5, 6]},          # Weekends
            'LEAGUES_CUP': {'hour': 21, 'days': [1, 2, 3]}, # Tue-Thu
            'TENNIS': {'hour': 14, 'days': list(range(7))},  # Daily tournaments
        }
        
        pattern = game_time_patterns.get(sport, {'hour': 19, 'days': list(range(7))})
        
        # Find next game day
        for i in range(7):
            check_date = current_time + timedelta(days=i)
            if check_date.weekday() in pattern['days']:
                return check_date.replace(
                    hour=pattern['hour'], 
                    minute=0, 
                    second=0, 
                    microsecond=0
                )
        
        # Fallback
        return current_time.replace(hour=pattern['hour'], minute=0, second=0, microsecond=0)
    
    async def _analyze_scheduling_factors(self, home_team: str, away_team: str, 
                                        sport: str, game_datetime: datetime, 
                                        current_time: datetime) -> Dict[str, Any]:
        """Analyze factors affecting game scheduling"""
        
        # Day of week analysis
        game_day = game_datetime.strftime('%A')
        is_weekend = game_datetime.weekday() in [5, 6]  # Sat, Sun
        is_primetime = 19 <= game_datetime.hour <= 22
        
        # Scheduling patterns by sport
        optimal_scheduling = {
            'NFL': is_weekend or game_datetime.weekday() == 3,  # Thu/Sat/Sun
            'NBA': not is_weekend or is_primetime,
            'MLB': True,  # Daily sport
            'TENNIS': True,  # Tournament format
            'MLS': is_weekend,
            'LEAGUES_CUP': game_datetime.weekday() in [1, 2, 3]  # Tue-Thu
        }
        
        # Travel considerations (simplified)
        travel_factor = 1.0
        if "International" in f"{home_team} {away_team}" or sport == "LEAGUES_CUP":
            travel_factor = 1.3  # International games more complex
        
        return {
            "game_day": game_day,
            "is_weekend": is_weekend,
            "is_primetime": is_primetime,
            "optimal_scheduling": optimal_scheduling.get(sport, True),
            "travel_complexity": travel_factor,
            "scheduling_quality": "OPTIMAL" if optimal_scheduling.get(sport, True) else "SUBOPTIMAL"
        }
    
    def _analyze_game_availability(self, sport: str, game_datetime: datetime, 
                                 current_time: datetime, 
                                 scheduling_factors: Dict) -> Dict[str, Any]:
        """Analyze game availability and detection accuracy"""
        
        time_diff_hours = (game_datetime - current_time).total_seconds() / 3600
        
        # Availability windows
        if time_diff_hours < -self.live_windows.get(sport, 2.5):
            availability = "GAME_FINISHED"
            detection_accuracy = 0.95
        elif -self.live_windows.get(sport, 2.5) <= time_diff_hours <= 0:
            availability = "CURRENTLY_LIVE"
            detection_accuracy = 0.90
        elif 0 < time_diff_hours <= 2:
            availability = "STARTING_SOON"
            detection_accuracy = 0.85
        elif 2 < time_diff_hours <= 6:
            availability = "TODAY_GAMES"
            detection_accuracy = 0.80
        else:
            availability = "FUTURE_GAMES"
            detection_accuracy = 0.70
        
        # Confidence based on scheduling quality
        confidence_modifier = 1.1 if scheduling_factors["optimal_scheduling"] else 0.9
        final_confidence = min(0.95, detection_accuracy * confidence_modifier)
        
        return {
            "availability_status": availability,
            "detection_accuracy": final_confidence,
            "time_window_hours": round(time_diff_hours, 2),
            "live_window_sport": self.live_windows.get(sport, 2.5),
            "availability_confidence": "HIGH" if final_confidence > 0.8 else "MEDIUM" if final_confidence > 0.6 else "LOW"
        }
    
    def _analyze_timing_implications(self, game_status: str, time_until_game: float,
                                   sport: str, scheduling_factors: Dict) -> Dict[str, Any]:
        """Analyze betting and prediction implications of timing"""
        
        timing_implications = {
            "betting_window": "CLOSED" if game_status in ["LIVE", "FINISHED"] else "OPEN",
            "prediction_reliability": 0.8,  # Base reliability
            "data_freshness": "CURRENT",
            "market_efficiency": "NORMAL"
        }
        
        # Adjust based on time until game
        if game_status == "STARTING_SOON":
            timing_implications["prediction_reliability"] = 0.9
            timing_implications["market_efficiency"] = "HIGH"
        elif game_status == "TODAY":
            timing_implications["prediction_reliability"] = 0.85
        elif game_status == "FUTURE":
            timing_implications["prediction_reliability"] = 0.7
            timing_implications["data_freshness"] = "PROJECTED"
        
        # Primetime games often have better data
        if scheduling_factors.get("is_primetime", False):
            timing_implications["prediction_reliability"] *= 1.1
        
        timing_implications["timing_edge"] = self._calculate_timing_edge(
            game_status, scheduling_factors
        )
        
        return timing_implications
    
    def _calculate_timing_edge(self, game_status: str, scheduling_factors: Dict) -> str:
        """Calculate any timing-based betting edge"""
        
        edges = []
        
        # Weekend games often have different betting patterns
        if scheduling_factors.get("is_weekend", False):
            edges.append("WEEKEND_CASUAL_BETTING")
        
        # Primetime games get more attention
        if scheduling_factors.get("is_primetime", False):
            edges.append("PRIMETIME_EXPOSURE")
        
        # Optimal scheduling usually means better analysis available
        if scheduling_factors.get("optimal_scheduling", False):
            edges.append("OPTIMAL_INFO_AVAILABILITY")
        
        if not edges:
            return "NO_TIMING_EDGE"
        
        return " + ".join(edges)
    
    def _calculate_schedule_confidence(self, game_status: str, scheduling_factors: Dict, 
                                     availability_analysis: Dict) -> Dict[str, Any]:
        """Calculate overall confidence in schedule analysis"""
        
        base_confidence = {
            "LIVE": 0.95,
            "STARTING_SOON": 0.90,
            "TODAY": 0.85,
            "TOMORROW": 0.80,
            "FUTURE": 0.70,
            "FINISHED": 0.95
        }.get(game_status, 0.75)
        
        # Adjust for scheduling quality
        if scheduling_factors["optimal_scheduling"]:
            base_confidence *= 1.05
        
        # Adjust for detection accuracy
        detection_confidence = availability_analysis["detection_accuracy"]
        
        final_confidence = min(0.95, (base_confidence + detection_confidence) / 2)
        
        return {
            "overall_confidence": final_confidence,
            "confidence_level": "HIGH" if final_confidence > 0.85 else "MEDIUM" if final_confidence > 0.70 else "LOW",
            "confidence_factors": {
                "game_status_clarity": base_confidence,
                "scheduling_optimality": scheduling_factors["optimal_scheduling"],
                "detection_accuracy": detection_confidence
            }
        }
    
    def _get_fallback_schedule_analysis(self, home_team: str, away_team: str, sport: str) -> Dict[str, Any]:
        """Fallback analysis when main analysis fails"""
        current_time = datetime.now(pytz.timezone('America/New_York'))
        
        return {
            "game_timing": {
                "scheduled_time": current_time.isoformat(),
                "current_time": current_time.isoformat(),
                "hours_until_game": 2.0,
                "game_status": "TODAY",
                "timezone": "America/New_York"
            },
            "scheduling_factors": {
                "game_day": current_time.strftime('%A'),
                "optimal_scheduling": True,
                "scheduling_quality": "ESTIMATED"
            },
            "availability_analysis": {
                "availability_status": "TODAY_GAMES",
                "detection_accuracy": 0.75,
                "availability_confidence": "MEDIUM"
            },
            "timing_implications": {
                "betting_window": "OPEN",
                "prediction_reliability": 0.75,
                "timing_edge": "FALLBACK_ANALYSIS"
            },
            "schedule_confidence": {
                "overall_confidence": 0.75,
                "confidence_level": "MEDIUM"
            },
            "data_source": "FALLBACK_SCHEDULE_ANALYSIS",
            "analysis_timestamp": current_time.isoformat()
        }

# 🕐 SPORTS SCHEDULE TIME ANALYZER INSTANCE
sports_schedule_analyzer = SportsScheduleTimeAnalyzer()

# 🎯 MAIN MCP INTERFACE FOR SCHEDULE ANALYSIS
async def get_schedule_time_analysis(home_team: str, away_team: str, sport: str, 
                                   game_time: str = "", venue: str = "") -> Dict[str, Any]:
    """
    🕐 MAIN INTERFACE FOR SCHEDULE & TIME ANALYSIS
    The 6th dimension that was missing - accurate game timing and availability
    """
    return await sports_schedule_analyzer.get_schedule_time_analysis(
        home_team, away_team, sport, game_time, venue
    )

if __name__ == "__main__":
    # Test the schedule time analysis
    async def test():
        print("🕐 Testing Sports Schedule Time Analysis...")
        
        test_cases = [
            ("Kansas City Chiefs", "Buffalo Bills", "NFL", "2024-12-15T18:00:00-05:00"),
            ("Lakers", "Warriors", "NBA", ""),  # No time provided
            ("Real Madrid", "Barcelona", "LEAGUES_CUP", "2024-08-11T21:00:00-06:00")
        ]
        
        for home_team, away_team, sport, game_time in test_cases:
            print(f"\n🕐 Testing: {away_team} @ {home_team} ({sport})")
            result = await get_schedule_time_analysis(home_team, away_team, sport, game_time)
            
            print("=" * 50)
            print(f"Game Status: {result['game_timing']['game_status']}")
            print(f"Hours Until Game: {result['game_timing']['hours_until_game']}")
            print(f"Availability: {result['availability_analysis']['availability_status']}")
            print(f"Betting Window: {result['timing_implications']['betting_window']}")
            print(f"Schedule Confidence: {result['schedule_confidence']['confidence_level']}")
            print("=" * 50)
    
    asyncio.run(test())