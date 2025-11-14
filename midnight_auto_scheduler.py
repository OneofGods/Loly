#!/usr/bin/env python3
"""
⏰🌙⚡ MIDNIGHT AUTO-UPDATE SCHEDULER - AUTOMATED LEARNING MACHINE!
The most sophisticated auto-update system for BUILD TO WIN mentality!

MISSION:
- Automatically fetch game results at midnight
- Update prediction accuracy when games complete
- Trigger hardcore criticism and learning analysis
- Schedule system updates and maintenance
- FULLY AUTOMATED LEARNING THAT NEVER SLEEPS!
"""

import asyncio
import aiohttp
import json
import logging
from datetime import datetime, timedelta, time
from pathlib import Path
import pytz
from typing import Dict, List, Any, Optional
import schedule
import threading

# Import our learning components
from real_agents.midnight_prediction_tracker import MidnightPredictionTracker
from real_agents.hardcore_accuracy_critic import HardcoreAccuracyCritic
from real_agents.season_long_learning_system import SeasonLongLearningSystem

class MidnightAutoScheduler:
    def __init__(self):
        self.prediction_tracker = MidnightPredictionTracker()
        self.accuracy_critic = HardcoreAccuracyCritic()
        self.learning_system = SeasonLongLearningSystem()
        
        # Timezone settings
        self.mexico_tz = pytz.timezone('America/Mexico_City')
        
        # Scheduler settings
        self.is_running = False
        self.scheduler_thread = None
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # ESPN API settings
        self.espn_api_base = "https://site.api.espn.com/apis/site/v2/sports"
        
        # Last update tracking
        self.last_update_file = Path("/tmp/midnight_last_update.json")
        
    async def start_scheduler(self):
        """
        🚀 START THE MIDNIGHT SCHEDULER!
        
        This will run continuously and handle all automated updates
        """
        print("⏰🌙 STARTING MIDNIGHT AUTO-SCHEDULER 🌙⏰")
        print("🎯 Automated learning system ACTIVATED!")
        print("💀 No more manual updates - the machine learns continuously!")
        
        self.is_running = True
        
        # Schedule midnight updates
        schedule.every().day.at("00:01").do(self._run_midnight_update)
        
        # Schedule daily accuracy checks
        schedule.every().day.at("06:00").do(self._run_daily_accuracy_check)
        
        # Schedule weekly brutal criticism
        schedule.every().sunday.at("23:00").do(self._run_weekly_brutal_criticism)
        
        # Schedule hourly result checks (for completed games) + PROGOL checks
        schedule.every().hour.do(self._check_completed_games_and_progol)
        
        # Start scheduler in thread
        self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.scheduler_thread.start()
        
        print("✅ MIDNIGHT SCHEDULER STARTED!")
        print("📅 Schedule:")
        print("   🌙 00:01 - Full midnight system update")
        print("   🌅 06:00 - Daily accuracy check") 
        print("   💀 23:00 Sunday - Weekly brutal criticism")
        print("   ⚡ Every hour - Check for completed games")
        
        return True
    
    def stop_scheduler(self):
        """Stop the scheduler"""
        self.is_running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)
        print("🛑 MIDNIGHT SCHEDULER STOPPED")
    
    def _run_scheduler(self):
        """Run the scheduler loop"""
        while self.is_running:
            schedule.run_pending()
            threading.Event().wait(60)  # Check every minute
    
    async def _run_midnight_update(self):
        """
        🌙 FULL MIDNIGHT SYSTEM UPDATE
        
        The most important update - when the day's games are complete
        and we analyze our performance!
        """
        try:
            print("\n🌙💀 MIDNIGHT UPDATE INITIATED 💀🌙")
            print(f"🕐 Time: {datetime.now(self.mexico_tz).strftime('%Y-%m-%d %H:%M:%S')} Mexico City")
            
            # Step 1: Fetch completed game results
            print("📊 STEP 1: Fetching completed game results...")
            completed_games = await self._fetch_completed_games()
            print(f"✅ Found {len(completed_games)} completed games")
            
            # Step 2: Update prediction results
            print("🎯 STEP 2: Updating prediction accuracy...")
            updated_predictions = 0
            for game in completed_games:
                success = await self._update_game_result(game)
                if success:
                    updated_predictions += 1
            print(f"✅ Updated {updated_predictions} predictions")
            
            # Step 3: Generate brutal criticism report
            print("💀 STEP 3: Generating brutal accuracy criticism...")
            criticism_report = await self.accuracy_critic.brutal_accuracy_analysis(days_back=1)
            if criticism_report:
                print("✅ Brutal criticism complete - agents have been judged!")
            
            # Step 4: Update season learning
            print("🏆 STEP 4: Updating season-long learning...")
            season_report = await self.learning_system.analyze_season_progress()
            if season_report:
                print("✅ Season learning updated")
            
            # Step 5: Generate midnight report
            print("📋 STEP 5: Generating midnight summary...")
            await self._generate_midnight_summary(completed_games, updated_predictions, criticism_report, season_report)
            
            # Update last run timestamp
            self._update_last_run_timestamp("midnight_update")
            
            print("🌙✅ MIDNIGHT UPDATE COMPLETE!")
            print("💀 The machine has learned from today's results!")
            
        except Exception as e:
            self.logger.error(f"💀 MIDNIGHT UPDATE ERROR: {e}")
            print(f"🚨 MIDNIGHT UPDATE FAILED: {e}")
    
    async def _run_daily_accuracy_check(self):
        """🌅 Daily accuracy check and system health"""
        try:
            print("\n🌅📊 DAILY ACCURACY CHECK INITIATED")
            
            # Quick accuracy check
            report = await self.accuracy_critic.brutal_accuracy_analysis(days_back=3)
            
            if report:
                accuracy = report["raw_analysis"]["overall_stats"]["accuracy_percentage"]
                print(f"📈 3-Day Accuracy: {accuracy}%")
                
                if accuracy < 50:
                    print("🚨 CRITICAL: Accuracy below 50% - IMMEDIATE ACTION REQUIRED!")
                elif accuracy < 60:
                    print("⚠️ WARNING: Accuracy below 60% - Need improvement!")
                elif accuracy > 75:
                    print("🔥 EXCELLENT: Accuracy above 75% - Keep it up!")
                
            self._update_last_run_timestamp("daily_check")
            print("✅ DAILY ACCURACY CHECK COMPLETE")
            
        except Exception as e:
            self.logger.error(f"💀 DAILY CHECK ERROR: {e}")
    
    async def _run_weekly_brutal_criticism(self):
        """💀 Weekly brutal criticism session"""
        try:
            print("\n💀🔥 WEEKLY BRUTAL CRITICISM INITIATED 🔥💀")
            print("⚠️ Prepare for HARSH TRUTHS about performance!")
            
            # Full 7-day brutal analysis
            report = await self.accuracy_critic.brutal_accuracy_analysis(days_back=7)
            
            if report:
                print("💀 WEEKLY CRITICISM COMPLETE!")
                print("📊 Full brutal analysis generated")
                
                # Display key findings
                verdict = report["verdict"]
                print(f"⚖️ VERDICT: {verdict['verdict']}")
                print(f"📝 MESSAGE: {verdict['message']}")
                
            self._update_last_run_timestamp("weekly_criticism")
            
        except Exception as e:
            self.logger.error(f"💀 WEEKLY CRITICISM ERROR: {e}")
    
    async def _check_completed_games_and_progol(self):
        """🔥 ENHANCED HOURLY CHECK: ESPN games + PROGOL results 🔥"""
        try:
            current_time = datetime.now(self.mexico_tz)
            print(f"⚡🎰 HOURLY CHECK: ESPN + PROGOL at {current_time.strftime('%H:%M')}")
            
            # Check ESPN completed games
            recent_games = await self._fetch_recent_completed_games(hours_back=4)
            if recent_games:
                print(f"📊 Found {len(recent_games)} completed ESPN games")
                for game in recent_games:
                    await self._update_game_result(game)
            
            # 🎰 NEW: Check PROGOL results automatically every hour
            progol_result = await self._check_progol_results()
            if progol_result.get('updated', 0) > 0:
                print(f"🎰 PROGOL HOURLY SUCCESS: {progol_result['updated']} predictions updated!")
                    
            self._update_last_run_timestamp("hourly_check")
            
        except Exception as e:
            self.logger.error(f"💀 HOURLY CHECK ERROR: {e}")
    
    # Keep old method for backward compatibility  
    async def _check_completed_games(self):
        """⚡ Check for recently completed games (legacy)"""
        await self._check_completed_games_and_progol()
    
    async def _fetch_completed_games(self):
        """Fetch completed games from ESPN API"""
        completed_games = []
        
        try:
            # Get yesterday's date (games that should be complete)
            yesterday = datetime.now(self.mexico_tz) - timedelta(days=1)
            date_str = yesterday.strftime('%Y%m%d')
            
            # Major sports to check - INCLUDING LIGA MX AND MLS!
            sports_endpoints = [
                ("soccer", "mex.1"),  # 🇲🇽 LIGA MX - MEXICAN FOOTBALL!
                ("soccer", "usa.1"),  # 🇺🇸 MLS - MAJOR LEAGUE SOCCER!
                ("soccer", "eng.1"),  # Premier League
                ("soccer", "esp.1"),  # La Liga
                ("soccer", "ger.1"),  # Bundesliga
                ("soccer", "ita.1"),  # Serie A
                ("soccer", "fra.1"),  # Ligue 1
                ("soccer", "ned.1"),  # 🇳🇱 EREDIVISIE - DUTCH FOOTBALL!
                ("soccer", "tur.1"),  # 🇹🇷 SUPERLIG - TURKISH FOOTBALL!
                ("soccer", "uefa.champions"),  # 🏆 UEFA CHAMPIONS LEAGUE!
                ("soccer", "conmebol.libertadores"),  # 🏆 COPA LIBERTADORES!
                ("basketball", "nba"),  # NBA
                ("basketball", "wnba"), # 🏀 WNBA - WOMEN'S BASKETBALL! 
                ("football", "nfl"),   # NFL
                ("baseball", "mlb")    # MLB
            ]
            
            async with aiohttp.ClientSession() as session:
                for sport, league in sports_endpoints:
                    try:
                        url = f"{self.espn_api_base}/{sport}/{league}/scoreboard"
                        params = {"dates": date_str}
                        
                        async with session.get(url, params=params) as response:
                            if response.status == 200:
                                data = await response.json()
                                games = self._parse_espn_games(data, sport, league)
                                completed_games.extend(games)
                                
                    except Exception as e:
                        self.logger.warning(f"Failed to fetch {sport}/{league}: {e}")
                        
        except Exception as e:
            self.logger.error(f"Error fetching completed games: {e}")
            
        return completed_games
    
    async def _fetch_recent_completed_games(self, hours_back: int = 4):
        """Fetch games completed in the last N hours"""
        completed_games = []
        
        try:
            current_time = datetime.now(self.mexico_tz)
            unique_games = {}  # Use dict to avoid duplicates by game key
            
            # Check unique dates only (don't check same date multiple times)
            dates_checked = set()
            for hours_ago in range(0, hours_back + 24, 1):  # Check last N hours + 24 for safety
                check_time = current_time - timedelta(hours=hours_ago)
                date_str = check_time.strftime('%Y%m%d')
                
                # Skip if we already checked this date
                if date_str in dates_checked:
                    continue
                dates_checked.add(date_str)
                
                # Major sports to check - INCLUDING LIGA MX!
                sports_endpoints = [
                    ("soccer", "mex.1"),  # 🇲🇽 LIGA MX - MEXICAN FOOTBALL!
                    ("soccer", "usa.1"),  # 🇺🇸 MLS - MAJOR LEAGUE SOCCER!
                    ("soccer", "eng.1"),  # Premier League
                    ("soccer", "esp.1"),  # La Liga
                    ("soccer", "ger.1"),  # Bundesliga
                    ("soccer", "ita.1"),  # Serie A
                    ("soccer", "uefa.champions"),  # 🏆 UEFA CHAMPIONS LEAGUE!
                    ("basketball", "nba"),  # NBA
                    ("football", "nfl"),   # NFL
                    ("baseball", "mlb")    # MLB
                ]
                
                async with aiohttp.ClientSession() as session:
                    for sport, league in sports_endpoints:
                        try:
                            url = f"{self.espn_api_base}/{sport}/{league}/scoreboard"
                            if date_str != datetime.now(self.mexico_tz).strftime('%Y%m%d'):
                                url += f"?dates={date_str}"
                                
                            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                                if response.status == 200:
                                    data = await response.json()
                                    recent_games = self._parse_espn_games_recent(data, sport, league, hours_back)
                                    
                                    # Add games to unique dict to avoid duplicates
                                    for game in recent_games:
                                        game_key = f"{game['league']}_{game['home_team']}_{game['away_team']}_{game['date']}"
                                        unique_games[game_key] = game
                                    
                                    if recent_games:
                                        print(f"🎯 Found {len(recent_games)} completed {league} games from {date_str}")
                                        
                        except Exception as e:
                            self.logger.warning(f"⚠️ Error checking {league} on {date_str}: {e}")
                            continue
                
                # Don't check too many days for hourly checks
                if len(dates_checked) >= 3:  # Only check last 3 unique dates
                    break
            
            # Convert back to list
            completed_games = list(unique_games.values())
                    
        except Exception as e:
            self.logger.error(f"💀 Error fetching recent completed games: {e}")
            
        if completed_games:
            print(f"🏆 TOTAL RECENT COMPLETED GAMES FOUND: {len(completed_games)}")
            
        return completed_games
    
    def _parse_espn_games_recent(self, data: dict, sport: str, league: str, hours_back: int) -> List[dict]:
        """Parse ESPN API response to extract recently completed games"""
        games = []
        current_time = datetime.now(self.mexico_tz)
        
        try:
            events = data.get("events", [])
            
            for event in events:
                # Check if game is completed
                status = event.get("status", {})
                if status.get("type", {}).get("completed", False):
                    
                    # Check if game completed within the specified hours
                    event_date = event.get("date")
                    if event_date:
                        try:
                            # Parse ESPN date format
                            game_time = datetime.fromisoformat(event_date.replace('Z', '+00:00'))
                            game_time = game_time.astimezone(self.mexico_tz)
                            
                            # Check if game completed within hours_back hours
                            time_diff = current_time - game_time
                            if time_diff.total_seconds() > hours_back * 3600:
                                continue  # Too old, skip
                                
                        except Exception as e:
                            # If we can't parse date, include it to be safe
                            pass
                    
                    competitions = event.get("competitions", [])
                    for competition in competitions:
                        competitors = competition.get("competitors", [])
                        
                        if len(competitors) == 2:
                            home_team = None
                            away_team = None
                            home_score = 0
                            away_score = 0
                            
                            for competitor in competitors:
                                team_name = competitor.get("team", {}).get("displayName", "Unknown")
                                score = int(competitor.get("score", 0))
                                
                                if competitor.get("homeAway") == "home":
                                    home_team = team_name
                                    home_score = score
                                else:
                                    away_team = team_name
                                    away_score = score
                            
                            # Determine result
                            if home_score > away_score:
                                result = "home_win"
                                winner = home_team
                            elif away_score > home_score:
                                result = "away_win"
                                winner = away_team
                            else:
                                result = "draw"
                                winner = "draw"
                            
                            game_info = {
                                "home_team": home_team,
                                "away_team": away_team,
                                "home_score": home_score,
                                "away_score": away_score,
                                "result": result,
                                "winner": winner,
                                "league": league,
                                "sport": sport,
                                "date": event_date,
                                "status": "completed"
                            }
                            
                            games.append(game_info)
                            
        except Exception as e:
            self.logger.error(f"Error parsing {league} games: {e}")
            
        return games
    
    def _parse_espn_games(self, data: dict, sport: str, league: str) -> List[dict]:
        """Parse ESPN API response to extract completed games"""
        games = []
        
        try:
            events = data.get("events", [])
            
            for event in events:
                # Check if game is completed
                status = event.get("status", {})
                if status.get("type", {}).get("completed", False):
                    
                    competitions = event.get("competitions", [])
                    for competition in competitions:
                        competitors = competition.get("competitors", [])
                        
                        if len(competitors) == 2:
                            home_team = None
                            away_team = None
                            home_score = 0
                            away_score = 0
                            
                            for competitor in competitors:
                                team_name = competitor.get("team", {}).get("displayName", "Unknown")
                                score = int(competitor.get("score", 0))
                                
                                if competitor.get("homeAway") == "home":
                                    home_team = team_name
                                    home_score = score
                                else:
                                    away_team = team_name
                                    away_score = score
                            
                            # Determine result
                            if home_score > away_score:
                                result = "home_win"
                            elif away_score > home_score:
                                result = "away_win"
                            else:
                                result = "draw"
                            
                            game_info = {
                                "home_team": home_team,
                                "away_team": away_team,
                                "home_score": home_score,
                                "away_score": away_score,
                                "result": result,
                                "sport": sport.upper(),
                                "league": league.upper(),
                                "date": event.get("date"),
                                "espn_event_id": event.get("id")
                            }
                            
                            games.append(game_info)
                            
        except Exception as e:
            self.logger.error(f"Error parsing ESPN games: {e}")
            
        return games
    
    async def _update_game_result(self, game_info: dict):
        """Update prediction result for a completed game"""
        try:
            # Create game data in format expected by prediction tracker
            game_data = {
                'home_team': game_info['home_team'],
                'away_team': game_info['away_team'],
                'league': game_info['league'],
                'sport': game_info['sport'],
                'date': game_info['date']
            }
            
            # Update result
            success = await self.prediction_tracker.update_game_result(
                game_data, 
                game_info['result']
            )
            
            if success:
                print(f"✅ Updated: {game_info['away_team']} @ {game_info['home_team']} - {game_info['result']}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error updating game result: {e}")
            return False
    
    async def _check_progol_results(self):
        """🎰 INTEGRATED PROGOL RESULT CHECKING 🎰"""
        try:
            self.logger.info("🎰 Checking PROGOL results automatically...")
            
            # Import the PROGOL result checker
            sys.path.append('/Users/onecoder/Projects/Total_AI_Liberation/dockerized_decentralized_agent_poly_loly/real_agents')
            from progol_result_checker import ProgolResultChecker
            
            checker = ProgolResultChecker()
            result = await checker.check_and_update_all_results()
            
            if result.get('status') == 'success' and result.get('updated', 0) > 0:
                self.logger.info(f"🎰 PROGOL SUCCESS: Updated {result['updated']} predictions!")
            else:
                self.logger.info(f"🎰 PROGOL check complete: {result.get('status')}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"🎰 PROGOL check error: {e}")
            return {"status": "error", "error": str(e)}
    
    async def _generate_midnight_summary(self, completed_games, updated_predictions, criticism_report, season_report):
        """Generate comprehensive midnight summary"""
        try:
            summary = {
                "midnight_update_date": datetime.now(self.mexico_tz).isoformat(),
                "completed_games": len(completed_games),
                "updated_predictions": updated_predictions,
                "criticism_generated": criticism_report is not None,
                "season_analysis_updated": season_report is not None,
                "next_midnight_update": (datetime.now(self.mexico_tz) + timedelta(days=1)).replace(hour=0, minute=1).isoformat()
            }
            
            # Save summary
            summary_file = Path(f"/tmp/midnight_summary_{datetime.now().strftime('%Y%m%d')}.json")
            with open(summary_file, 'w') as f:
                json.dump(summary, f, indent=2)
            
            print(f"📋 Midnight summary saved: {summary_file}")
            
        except Exception as e:
            self.logger.error(f"Error generating midnight summary: {e}")
    
    def _update_last_run_timestamp(self, operation: str):
        """Update last run timestamp for operation"""
        try:
            timestamps = {}
            if self.last_update_file.exists():
                with open(self.last_update_file, 'r') as f:
                    timestamps = json.load(f)
            
            timestamps[operation] = datetime.now(self.mexico_tz).isoformat()
            
            with open(self.last_update_file, 'w') as f:
                json.dump(timestamps, f, indent=2)
                
        except Exception as e:
            self.logger.error(f"Error updating timestamp: {e}")
    
    def get_scheduler_status(self):
        """Get current scheduler status"""
        try:
            timestamps = {}
            if self.last_update_file.exists():
                with open(self.last_update_file, 'r') as f:
                    timestamps = json.load(f)
            
            return {
                "is_running": self.is_running,
                "last_updates": timestamps,
                "current_time": datetime.now(self.mexico_tz).isoformat(),
                "next_scheduled": {
                    "midnight_update": "Every day at 00:01",
                    "daily_check": "Every day at 06:00", 
                    "weekly_criticism": "Every Sunday at 23:00",
                    "hourly_check": "Every hour"
                }
            }
            
        except Exception as e:
            self.logger.error(f"Error getting scheduler status: {e}")
            return {"error": str(e)}

async def main():
    """Test the midnight auto-scheduler"""
    print("⏰🌙 TESTING MIDNIGHT AUTO-SCHEDULER 🌙⏰")
    
    scheduler = MidnightAutoScheduler()
    
    # Start scheduler
    await scheduler.start_scheduler()
    
    # Show status
    status = scheduler.get_scheduler_status()
    print(f"📊 Scheduler Status: {status}")
    
    # Keep running for demonstration
    try:
        print("🔄 Scheduler running... (Ctrl+C to stop)")
        while True:
            await asyncio.sleep(60)
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping scheduler...")
        scheduler.stop_scheduler()
        print("✅ MIDNIGHT SCHEDULER TEST COMPLETE!")

if __name__ == "__main__":
    asyncio.run(main())