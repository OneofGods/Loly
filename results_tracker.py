#!/usr/bin/env python3
"""
🎯 RESULTS TRACKER - EMERGENCY IMPLEMENTATION
Tracks REAL win/loss performance to stop the confidence bullshit!
NO MORE FAKE CONFIDENCE WITHOUT REAL VALIDATION!
"""

import json
import asyncio
import aiohttp
import logging
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Any, Optional
import os

logger = logging.getLogger(__name__)

class EmergencyResultsTracker:
    """
    🚨 EMERGENCY RESULTS TRACKER
    Captures today's predictions and checks actual outcomes
    """
    
    def __init__(self):
        # Use flexible data directory based on environment
        data_dir = "/app/data" if os.path.exists("/app") and os.access("/app", os.W_OK) else "./data"
        self.predictions_file = f"{data_dir}/daily_predictions.json"
        self.results_file = f"{data_dir}/results_history.json"
        self.performance_file = f"{data_dir}/performance_stats.json"
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
    def capture_todays_predictions(self, games_data: List[Dict[str, Any]]) -> None:
        """
        🎯 CAPTURE TODAY'S PREDICTIONS FOR RESULT TRACKING
        """
        today = datetime.now(timezone.utc).date().isoformat()
        
        predictions = {
            "date": today,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "total_predictions": len(games_data),
            "games": []
        }
        
        for game in games_data:
            # 🔥 CRITICAL: Get proper sport field for MCP routing
            league = game.get('league', game.get('sport', 'Unknown'))
            sport = game.get('sport', 'Unknown')
            
            # 🇲🇽 Liga MX routing fix
            if '🇲🇽 Liga MX' in league or 'Liga MX' in league:
                sport = 'LIGA_MX'
                league = 'LIGA_MX'  # Clean league name
            elif '🇪🇸 La Liga' in league or 'La Liga' in league:
                sport = 'LA_LIGA' 
                league = 'LA_LIGA'
            elif '🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League' in league or 'Premier League' in league:
                sport = 'EPL'
                league = 'EPL'
            
            prediction = {
                "game_id": f"{game.get('away_team', 'Unknown')}_vs_{game.get('home_team', 'Unknown')}_{today}",
                "away_team": game.get('away_team', 'Unknown'),
                "home_team": game.get('home_team', 'Unknown'),
                "league": league,
                "sport": sport,  # 🔥 ADD SPORT FIELD FOR MCP ROUTING
                "confidence": game.get('confidence', 0),
                "predicted_winner": game.get('prediction', game.get('home_team', 'Unknown')),  # Default to home team
                "game_time": game.get('start_time', game.get('game_time', '')),
                "venue": game.get('venue', ''),
                "analysis": {
                    "polymarket": game.get('polymarket_confidence', 0),
                    "venue_advantage": game.get('venue_advantage', 0),
                    "sentiment": game.get('sentiment_score', 0),
                    "historical": game.get('historical_advantage', 0)
                },
                "prediction_captured": datetime.now(timezone.utc).isoformat(),
                "result_checked": False,
                "actual_winner": None,
                "prediction_correct": None,
                "game_completed": False
            }
            predictions["games"].append(prediction)
        
        # Save predictions
        try:
            with open(self.predictions_file, 'w') as f:
                json.dump(predictions, f, indent=2)
            logger.info(f"🎯 CAPTURED {len(predictions['games'])} PREDICTIONS FOR {today}")
        except Exception as e:
            logger.error(f"❌ Error saving predictions: {e}")
    
    async def check_game_results(self) -> Dict[str, Any]:
        """
        🔍 CHECK ACTUAL GAME RESULTS AND UPDATE TRACKING
        """
        try:
            # Load today's predictions
            if not os.path.exists(self.predictions_file):
                logger.warning("❌ No predictions file found!")
                return {"error": "No predictions to check"}
            
            with open(self.predictions_file, 'r') as f:
                predictions = json.load(f)
            
            results = {
                "date": predictions["date"],
                "total_games": len(predictions["games"]),
                "results_checked": 0,
                "games_completed": 0,
                "correct_predictions": 0,
                "wrong_predictions": 0,
                "pending_games": 0,
                "updated_games": []
            }
            
            # Check each game result
            for game in predictions["games"]:
                result = await self._check_single_game_result(game)
                if result:
                    results["updated_games"].append(result)
                    results["results_checked"] += 1
                    
                    if result["game_completed"]:
                        results["games_completed"] += 1
                        if result["prediction_correct"]:
                            results["correct_predictions"] += 1
                        else:
                            results["wrong_predictions"] += 1
                    else:
                        results["pending_games"] += 1
            
            # Calculate win rate
            if results["games_completed"] > 0:
                results["win_rate"] = results["correct_predictions"] / results["games_completed"]
                results["loss_rate"] = results["wrong_predictions"] / results["games_completed"]
            else:
                results["win_rate"] = 0
                results["loss_rate"] = 0
            
            # Save updated predictions
            with open(self.predictions_file, 'w') as f:
                json.dump(predictions, f, indent=2)
            
            # Update performance stats
            await self._update_performance_stats(results)
            
            logger.info(f"🎯 RESULTS CHECK COMPLETE: {results['correct_predictions']}/{results['games_completed']} correct ({results['win_rate']:.1%} win rate)")
            
            return results
            
        except Exception as e:
            logger.error(f"❌ Error checking results: {e}")
            return {"error": str(e)}
    
    async def _check_single_game_result(self, game_prediction: Dict) -> Optional[Dict]:
        """
        🔍 CHECK INDIVIDUAL GAME RESULT
        """
        try:
            # Skip if already checked
            if game_prediction.get("result_checked"):
                return None
            
            # Check ESPN for game result based on league
            league = game_prediction.get("league", "").upper()
            
            if "MLB" in league:
                result = await self._check_mlb_result(game_prediction)
            elif "NBA" in league or "WNBA" in league:
                result = await self._check_basketball_result(game_prediction)
            elif "NFL" in league:
                result = await self._check_nfl_result(game_prediction)
            elif "SOCCER" in league or any(soccer_league in league for soccer_league in ["EPL", "LA_LIGA", "SERIE_A", "BUNDESLIGA", "LIGUE_1", "MLS", "LIGA_MX"]):
                result = await self._check_soccer_result(game_prediction)
            else:
                # Generic ESPN check
                result = await self._check_generic_espn_result(game_prediction)
            
            if result:
                # Update the prediction with result
                game_prediction["actual_winner"] = result.get("winner")
                game_prediction["actual_score"] = result.get("score", "")
                game_prediction["game_completed"] = result.get("completed", False)
                game_prediction["result_checked"] = True
                game_prediction["result_check_time"] = datetime.now(timezone.utc).isoformat()
                
                # Check if prediction was correct
                if result.get("completed") and result.get("winner"):
                    predicted_winner = game_prediction.get("predicted_winner", "")
                    actual_winner = result.get("winner", "")
                    game_prediction["prediction_correct"] = (predicted_winner.lower() in actual_winner.lower() or 
                                                           actual_winner.lower() in predicted_winner.lower())
                
                return game_prediction
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Error checking game result: {e}")
            return None
    
    async def _check_mlb_result(self, game_prediction: Dict) -> Optional[Dict]:
        """
        ⚾ CHECK MLB GAME RESULT
        """
        try:
            today_str = datetime.now().strftime('%Y%m%d')
            url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={today_str}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Find matching game
                        away_team = game_prediction.get("away_team", "").lower()
                        home_team = game_prediction.get("home_team", "").lower()
                        
                        for event in data.get("events", []):
                            competitions = event.get("competitions", [])
                            if competitions:
                                competitors = competitions[0].get("competitors", [])
                                if len(competitors) >= 2:
                                    event_away = competitors[0].get("team", {}).get("displayName", "").lower()
                                    event_home = competitors[1].get("team", {}).get("displayName", "").lower()
                                    
                                    # Check if teams match
                                    if (away_team in event_away or event_away in away_team) and \
                                       (home_team in event_home or event_home in home_team):
                                        
                                        # Check if game is completed
                                        status = event.get("status", {}).get("type", {}).get("name", "").lower()
                                        completed = status in ["final", "completed"]
                                        
                                        if completed:
                                            # Get winner
                                            away_score = int(competitors[0].get("score", "0"))
                                            home_score = int(competitors[1].get("score", "0"))
                                            
                                            if away_score > home_score:
                                                winner = competitors[0].get("team", {}).get("displayName", "")
                                            else:
                                                winner = competitors[1].get("team", {}).get("displayName", "")
                                            
                                            return {
                                                "winner": winner,
                                                "score": f"{away_score}-{home_score}",
                                                "completed": True
                                            }
                                        else:
                                            return {"completed": False}
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Error checking MLB result: {e}")
            return None
    
    async def _check_basketball_result(self, game_prediction: Dict) -> Optional[Dict]:
        """
        🏀 CHECK NBA/WNBA GAME RESULT
        """
        try:
            league = game_prediction.get("league", "").upper()
            
            if "WNBA" in league:
                url = "https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard"
            else:
                url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return await self._parse_basketball_result(data, game_prediction)
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Error checking basketball result: {e}")
            return None
    
    async def _check_nfl_result(self, game_prediction: Dict) -> Optional[Dict]:
        """
        🏈 CHECK NFL GAME RESULT
        """
        try:
            url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return await self._parse_generic_espn_result(data, game_prediction)
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Error checking NFL result: {e}")
            return None
    
    async def _check_soccer_result(self, game_prediction: Dict) -> Optional[Dict]:
        """
        ⚽ CHECK SOCCER GAME RESULT
        """
        try:
            # Map league to ESPN endpoint
            league = game_prediction.get("league", "").upper()
            league_mapping = {
                "EPL": "eng.1",
                "PREMIER_LEAGUE": "eng.1",
                "LA_LIGA": "esp.1",
                "SERIE_A": "ita.1", 
                "BUNDESLIGA": "ger.1",
                "LIGUE_1": "fra.1",
                "MLS": "usa.1",
                "LIGA_MX": "mex.1"
            }
            
            espn_league = league_mapping.get(league, "eng.1")  # Default to EPL
            today_str = datetime.now().strftime('%Y%m%d')
            url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/{espn_league}/scoreboard?dates={today_str}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return await self._parse_generic_espn_result(data, game_prediction)
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Error checking soccer result: {e}")
            return None
    
    async def _check_generic_espn_result(self, game_prediction: Dict) -> Optional[Dict]:
        """
        🔍 GENERIC ESPN RESULT CHECK
        """
        # This would try multiple ESPN endpoints based on team names
        return None
    
    async def _parse_basketball_result(self, data: Dict, game_prediction: Dict) -> Optional[Dict]:
        """
        🏀 PARSE BASKETBALL RESULT DATA
        """
        return await self._parse_generic_espn_result(data, game_prediction)
    
    async def _parse_generic_espn_result(self, data: Dict, game_prediction: Dict) -> Optional[Dict]:
        """
        🔍 PARSE GENERIC ESPN RESULT DATA
        """
        try:
            away_team = game_prediction.get("away_team", "").lower()
            home_team = game_prediction.get("home_team", "").lower()
            
            for event in data.get("events", []):
                competitions = event.get("competitions", [])
                if competitions:
                    competitors = competitions[0].get("competitors", [])
                    if len(competitors) >= 2:
                        event_away = competitors[0].get("team", {}).get("displayName", "").lower()
                        event_home = competitors[1].get("team", {}).get("displayName", "").lower()
                        
                        # Check if teams match (fuzzy matching)
                        if (away_team in event_away or event_away in away_team) and \
                           (home_team in event_home or event_home in home_team):
                            
                            # Check if game is completed
                            status = event.get("status", {}).get("type", {}).get("name", "").lower()
                            completed = status in ["final", "completed"]
                            
                            if completed:
                                # Get winner
                                away_score = int(competitors[0].get("score", "0"))
                                home_score = int(competitors[1].get("score", "0"))
                                
                                if away_score > home_score:
                                    winner = competitors[0].get("team", {}).get("displayName", "")
                                else:
                                    winner = competitors[1].get("team", {}).get("displayName", "")
                                
                                return {
                                    "winner": winner,
                                    "score": f"{away_score}-{home_score}",
                                    "completed": True
                                }
                            else:
                                return {"completed": False}
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Error parsing ESPN result: {e}")
            return None
    
    async def _update_performance_stats(self, results: Dict) -> None:
        """
        📊 UPDATE OVERALL PERFORMANCE STATISTICS
        """
        try:
            # Load existing performance stats
            if os.path.exists(self.performance_file):
                with open(self.performance_file, 'r') as f:
                    stats = json.load(f)
            else:
                stats = {
                    "total_predictions": 0,
                    "total_completed_games": 0,
                    "total_correct": 0,
                    "total_wrong": 0,
                    "overall_win_rate": 0,
                    "daily_performance": {}
                }
            
            # Update stats with today's results
            date = results["date"]
            stats["daily_performance"][date] = results
            
            # Update totals
            stats["total_predictions"] += results["total_games"]
            stats["total_completed_games"] += results["games_completed"]
            stats["total_correct"] += results["correct_predictions"]
            stats["total_wrong"] += results["wrong_predictions"]
            
            # Calculate overall win rate
            if stats["total_completed_games"] > 0:
                stats["overall_win_rate"] = stats["total_correct"] / stats["total_completed_games"]
            
            stats["last_updated"] = datetime.now(timezone.utc).isoformat()
            
            # Save updated stats
            with open(self.performance_file, 'w') as f:
                json.dump(stats, f, indent=2)
            
            logger.info(f"📊 PERFORMANCE UPDATED: {stats['total_correct']}/{stats['total_completed_games']} overall ({stats['overall_win_rate']:.1%} win rate)")
            
        except Exception as e:
            logger.error(f"❌ Error updating performance stats: {e}")
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """
        📊 GET CURRENT PERFORMANCE SUMMARY
        """
        try:
            if os.path.exists(self.performance_file):
                with open(self.performance_file, 'r') as f:
                    return json.load(f)
            else:
                return {"error": "No performance data available"}
        except Exception as e:
            logger.error(f"❌ Error reading performance stats: {e}")
            return {"error": str(e)}

# Singleton instance
results_tracker = EmergencyResultsTracker()

async def capture_predictions(games_data: List[Dict[str, Any]]) -> None:
    """
    🎯 MAIN FUNCTION TO CAPTURE TODAY'S PREDICTIONS
    """
    results_tracker.capture_todays_predictions(games_data)

async def check_results() -> Dict[str, Any]:
    """
    🔍 MAIN FUNCTION TO CHECK GAME RESULTS
    """
    return await results_tracker.check_game_results()

def get_performance() -> Dict[str, Any]:
    """
    📊 GET PERFORMANCE SUMMARY
    """
    return results_tracker.get_performance_summary()

if __name__ == "__main__":
    # Test the results tracker
    async def test_tracker():
        print("🎯 Testing Emergency Results Tracker...")
        
        # Test with sample game data
        sample_games = [
            {
                "away_team": "Kansas City Royals",
                "home_team": "Chicago White Sox", 
                "league": "MLB",
                "confidence": 0.706,
                "prediction": "Kansas City Royals",
                "start_time": "2025-08-26T19:10:00Z"
            }
        ]
        
        # Capture predictions
        await capture_predictions(sample_games)
        print("✅ Predictions captured")
        
        # Check results
        results = await check_results()
        print(f"📊 Results: {results}")
        
        # Get performance
        performance = get_performance()
        print(f"🎯 Performance: {performance}")

    asyncio.run(test_tracker())