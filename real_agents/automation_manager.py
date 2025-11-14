#!/usr/bin/env python3
"""
🔥💀🔥 AUTOMATION MANAGER - COMPLETE AUTOMATION INTEGRATION 🔥💀🔥
Manages all automation tasks including result checking, dashboard integration, and scheduling
"""

import asyncio
import logging
import json
from datetime import datetime, timedelta
from typing import Dict, Optional
from pathlib import Path
import threading
import time

from progol_result_checker import ProgolResultChecker
from universal_prediction_engine import UniversalPredictionEngine
from leagues_registry import LEAGUES_REGISTRY

logger = logging.getLogger(__name__)

class AutomationManager:
    """
    🤖 AUTOMATION MANAGER 🤖
    
    Complete automation system for PROGOL result tracking and dashboard integration
    """
    
    def __init__(self):
        self.progol_checker = ProgolResultChecker()
        self.prediction_engine = UniversalPredictionEngine()  # 🔥💀🔥 ADD 8D ENGINE!
        self.is_running = False
        self.automation_thread = None
        self.last_check_time = None
        self.check_interval = 3600  # Check every hour
        self.status_file = Path('/tmp/automation_status.json')
        logger.info("🤖 AUTOMATION MANAGER INITIALIZED")
    
    async def start_automation(self) -> Dict:
        """
        🚀 START AUTOMATION
        
        Starts the complete automation system
        """
        try:
            if self.is_running:
                return {"status": "already_running", "message": "Automation already active"}
            
            logger.info("🔥💀🔥 STARTING COMPLETE AUTOMATION SYSTEM 💀🔥💀")
            
            # Start automation in background thread
            self.is_running = True
            self.automation_thread = threading.Thread(target=self._run_automation_loop, daemon=True)
            self.automation_thread.start()
            
            # Update status
            self._update_status("started")
            
            # Run immediate check
            initial_result = await self.progol_checker.check_and_update_all_results()
            
            logger.info("✅ AUTOMATION SYSTEM STARTED SUCCESSFULLY!")
            
            return {
                "status": "started", 
                "message": "Automation system is now running",
                "initial_check": initial_result,
                "next_check": self._get_next_check_time()
            }
            
        except Exception as e:
            logger.error(f"💀 ERROR STARTING AUTOMATION: {e}")
            return {"status": "error", "error": str(e)}
    
    def stop_automation(self) -> Dict:
        """
        🛑 STOP AUTOMATION
        
        Stops the automation system
        """
        try:
            if not self.is_running:
                return {"status": "not_running", "message": "Automation not active"}
            
            logger.info("🛑 STOPPING AUTOMATION SYSTEM...")
            
            self.is_running = False
            
            # Wait for thread to finish
            if self.automation_thread and self.automation_thread.is_alive():
                self.automation_thread.join(timeout=5)
            
            # Update status
            self._update_status("stopped")
            
            logger.info("✅ AUTOMATION SYSTEM STOPPED")
            
            return {"status": "stopped", "message": "Automation system has been stopped"}
            
        except Exception as e:
            logger.error(f"💀 ERROR STOPPING AUTOMATION: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_automation_status(self) -> Dict:
        """
        📊 GET AUTOMATION STATUS
        
        Returns current status of the automation system
        """
        try:
            # Load status from file
            status_data = self._load_status()
            
            # Calculate stats
            uptime = None
            if self.is_running and status_data.get('started_at'):
                started = datetime.fromisoformat(status_data['started_at'])
                uptime = str(datetime.now() - started)
            
            return {
                "is_running": self.is_running,
                "last_check": self.last_check_time,
                "next_check": self._get_next_check_time(),
                "check_interval_hours": self.check_interval / 3600,
                "uptime": uptime,
                "status_history": status_data.get('history', []),
                "current_time": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error getting automation status: {e}")
            return {"error": str(e)}
    
    async def manual_check(self) -> Dict:
        """
        🔧 MANUAL CHECK
        
        Manually trigger a result check
        """
        try:
            logger.info("🔧 MANUAL AUTOMATION CHECK TRIGGERED")
            
            result = await self.progol_checker.check_and_update_all_results()
            self.last_check_time = datetime.now().isoformat()
            
            # Update status
            self._update_status("manual_check", {"result": result})
            
            logger.info(f"✅ MANUAL CHECK COMPLETE: {result}")
            
            return {
                "status": "completed",
                "check_result": result,
                "timestamp": self.last_check_time
            }
            
        except Exception as e:
            logger.error(f"💀 ERROR IN MANUAL CHECK: {e}")
            return {"status": "error", "error": str(e)}
    
    def _run_automation_loop(self):
        """Run the main automation loop in background thread"""
        logger.info("🔄 Starting automation background loop...")
        
        while self.is_running:
            try:
                # Run async result check
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                # 🔥💀🔥 RUN 8D PREDICTIONS FIRST! 💀🔥💀
                predictions_result = loop.run_until_complete(
                    self.run_8d_predictions_for_all_leagues()
                )
                logger.info(f"🔥 8D Predictions Result: {predictions_result}")
                
                # Then run PROGOL result check
                result = loop.run_until_complete(
                    self.progol_checker.check_and_update_all_results()
                )
                
                self.last_check_time = datetime.now().isoformat()
                
                # Update status with both results
                self._update_status("automatic_check", {
                    "progol_result": result,
                    "predictions_result": predictions_result
                })
                
                logger.info(f"🔄 Automatic check completed: PROGOL={result}, 8D={predictions_result}")
                
                loop.close()
                
                # Sleep until next check
                sleep_time = 0
                while sleep_time < self.check_interval and self.is_running:
                    time.sleep(60)  # Check every minute if we should stop
                    sleep_time += 60
                
            except Exception as e:
                logger.error(f"Error in automation loop: {e}")
                time.sleep(300)  # Sleep 5 minutes on error
    
    def _get_next_check_time(self) -> Optional[str]:
        """Calculate next check time"""
        if not self.last_check_time:
            return "Immediate (no previous check)"
        
        try:
            last_check = datetime.fromisoformat(self.last_check_time)
            next_check = last_check + timedelta(seconds=self.check_interval)
            return next_check.isoformat()
        except Exception:
            return "Unknown"
    
    def _update_status(self, event: str, data: Dict = None):
        """Update automation status file"""
        try:
            status_data = self._load_status()
            
            # Add new event to history
            event_record = {
                "event": event,
                "timestamp": datetime.now().isoformat(),
                "data": data
            }
            
            if "history" not in status_data:
                status_data["history"] = []
            
            status_data["history"].append(event_record)
            
            # Keep only last 50 events
            status_data["history"] = status_data["history"][-50:]
            
            # Update current status
            status_data["current_status"] = event
            status_data["last_updated"] = datetime.now().isoformat()
            
            if event == "started":
                status_data["started_at"] = datetime.now().isoformat()
            elif event == "stopped":
                status_data.pop("started_at", None)
            
            # Save status
            with open(self.status_file, 'w') as f:
                json.dump(status_data, f, indent=2)
                
        except Exception as e:
            logger.warning(f"Error updating status: {e}")
    
    def _load_status(self) -> Dict:
        """Load automation status from file"""
        try:
            if self.status_file.exists():
                with open(self.status_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            logger.warning(f"Error loading status: {e}")
            return {}
    
    async def run_8d_predictions_for_all_leagues(self) -> Dict:
        """
        🔥💀🔥 RUN 8D PREDICTIONS FOR ALL LEAGUES AND SAVE TO JSON! 💀🔥💀
        
        This is the CRITICAL missing method that runs 8D predictions and saves them
        to automation JSON files for Midnight Special dashboard consumption!
        """
        try:
            logger.info("🔥💀🔥 RUNNING 8D PREDICTIONS FOR ALL LEAGUES! 💀🔥💀")
            
            results = {}
            total_predictions = 0
            
            for league_id, league_config in LEAGUES_REGISTRY.items():
                try:
                    logger.info(f"🎯 Running 8D predictions for {league_id}...")
                    
                    # Get today's games for this league (this would normally come from league fetchers)
                    # For now, create sample games to demonstrate the data flow
                    sample_games = self._get_sample_games_for_league(league_id, league_config)
                    
                    if not sample_games:
                        logger.info(f"📭 No games found for {league_id}")
                        continue
                    
                    # Run 8D predictions for each game
                    league_predictions = []
                    for game_data in sample_games:
                        try:
                            # 🔥💀🔥 RUN REAL 8D ANALYSIS WITH D1+D2 MCP! 💀🔥💀
                            prediction = await self.prediction_engine.analyze_game(game_data, league_id)
                            
                            # Format for automation JSON
                            formatted_prediction = {
                                "game_id": f"{league_id}_{game_data['home_team']}_{game_data['away_team']}_{datetime.now().strftime('%Y%m%d')}",
                                "matchup": f"{game_data['away_team']} @ {game_data['home_team']}",
                                "home_team": game_data['home_team'],
                                "away_team": game_data['away_team'],
                                "prediction": prediction['prediction'],
                                "confidence": prediction['confidence'],
                                "reasoning": prediction['reasoning'],
                                "dimensions": prediction.get('dimensions', {}),
                                "time": "TBD",
                                "date": datetime.now().strftime('%Y-%m-%d'),
                                "venue": game_data.get('venue', 'TBD'),
                                "tracked_at": datetime.now().isoformat(),
                                "status": "predicted"
                            }
                            
                            league_predictions.append(formatted_prediction)
                            total_predictions += 1
                            
                            logger.info(f"✅ {league_id}: {prediction['prediction']} ({prediction['confidence']}%)")
                            
                        except Exception as e:
                            logger.error(f"❌ Error predicting {game_data}: {e}")
                    
                    if league_predictions:
                        # Save predictions to automation JSON file
                        await self._save_predictions_to_automation_json(league_id, league_predictions)
                        results[league_id] = len(league_predictions)
                    
                except Exception as e:
                    logger.error(f"❌ Error processing {league_id}: {e}")
                    results[league_id] = f"Error: {e}"
            
            logger.info(f"🎯 8D PREDICTIONS COMPLETE: {total_predictions} total predictions across {len(results)} leagues")
            
            return {
                "status": "success",
                "total_predictions": total_predictions,
                "leagues_processed": len(results),
                "results": results,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"💀 ERROR RUNNING 8D PREDICTIONS: {e}")
            return {"status": "error", "error": str(e)}
    
    def _get_sample_games_for_league(self, league_id: str, league_config: Dict) -> list:
        """
        Get sample games for testing. In production, this would fetch from league APIs.
        """
        sport = league_config.get('sport', 'Soccer')
        
        sample_games = {
            'PREMIER_LEAGUE': [
                {'home_team': 'Manchester United', 'away_team': 'Arsenal', 'venue': 'Old Trafford', 'city': 'Manchester'},
                {'home_team': 'Liverpool', 'away_team': 'Chelsea', 'venue': 'Anfield', 'city': 'Liverpool'}
            ],
            'NBA': [
                {'home_team': 'Los Angeles Lakers', 'away_team': 'Boston Celtics', 'venue': 'Staples Center', 'city': 'Los Angeles'},
                {'home_team': 'Golden State Warriors', 'away_team': 'Miami Heat', 'venue': 'Chase Center', 'city': 'San Francisco'}
            ],
            'UEFA': [
                {'home_team': 'Real Madrid', 'away_team': 'Barcelona', 'venue': 'Santiago Bernabéu', 'city': 'Madrid'},
                {'home_team': 'Bayern Munich', 'away_team': 'PSG', 'venue': 'Allianz Arena', 'city': 'Munich'}
            ]
        }
        
        return sample_games.get(league_id, [])
    
    async def _save_predictions_to_automation_json(self, league_id: str, predictions: list):
        """
        🔥💀🔥 SAVE 8D PREDICTIONS TO AUTOMATION JSON FOR MIDNIGHT SPECIAL! 💀🔥💀
        
        This is the CRITICAL method that saves predictions to the JSON files
        that Midnight Special dashboard reads from!
        """
        try:
            # Define automation data directory
            automation_dir = Path("midnight_special_data")
            automation_dir.mkdir(exist_ok=True)
            
            # Automation JSON file path
            automation_file = automation_dir / "automation_history.json"
            
            # Load existing automation data
            automation_data = {}
            if automation_file.exists():
                with open(automation_file, 'r') as f:
                    automation_data = json.load(f)
            
            # Ensure league exists in automation data
            if league_id not in automation_data:
                automation_data[league_id] = {
                    "league": league_id,
                    "runs": [],
                    "total_predictions": 0,
                    "created": datetime.now().isoformat()
                }
            
            # Create new run with predictions
            new_run = {
                "date": datetime.now().strftime('%Y-%m-%d'),
                "predictions": predictions,
                "created": datetime.now().isoformat()
            }
            
            # Add run to league data
            automation_data[league_id]["runs"].append(new_run)
            automation_data[league_id]["total_predictions"] += len(predictions)
            
            # Keep only last 10 runs per league
            automation_data[league_id]["runs"] = automation_data[league_id]["runs"][-10:]
            
            # Save updated automation data
            with open(automation_file, 'w') as f:
                json.dump(automation_data, f, indent=2)
            
            logger.info(f"💾 SAVED {len(predictions)} 8D predictions for {league_id} to {automation_file}")
            
        except Exception as e:
            logger.error(f"💀 ERROR SAVING PREDICTIONS: {e}")
            raise

# Global automation manager instance
automation_manager = AutomationManager()

async def main():
    """Test the automation manager"""
    print("🤖🔥🤖 TESTING AUTOMATION MANAGER 🤖🔥🤖")
    
    # Start automation
    start_result = await automation_manager.start_automation()
    print(f"📊 Start Result: {start_result}")
    
    # Check status
    status = automation_manager.get_automation_status()
    print(f"📊 Status: {status}")
    
    # Manual check
    manual_result = await automation_manager.manual_check()
    print(f"📊 Manual Check: {manual_result}")
    
    # Keep running for demonstration
    print("🔄 Running for 30 seconds...")
    await asyncio.sleep(30)
    
    # Stop automation
    stop_result = automation_manager.stop_automation()
    print(f"📊 Stop Result: {stop_result}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())