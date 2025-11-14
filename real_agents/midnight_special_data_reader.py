#!/usr/bin/env python3
"""
🔥💀🔥 BROTHER #182: FIX OLD PREDICTIONS PANEL! 💀🔥💀

OLD PREDICTIONS MUST ONLY READ FROM MIDNIGHT SPECIAL AUTOMATION DATA!
NO MORE CONTAMINATION FROM GAMES & PREDICTIONS!

This is the CRITICAL ARCHITECTURAL FIX!
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class MidnightSpecialDataReader:
    """
    🔥💀🔥 READS ONLY FROM MIDNIGHT SPECIAL AUTOMATION DATA! 💀🔥💀
    
    NO ACCESS TO GAMES & PREDICTIONS!
    PURE SEASON DATA ONLY!
    """
    
    def __init__(self):
        # 🔥💀🔥 FIX: Use absolute path to ensure web handlers find the data! 💀🔥💀
        base_dir = Path(__file__).parent.parent  # Go up from real_agents to main directory
        self.data_dir = base_dir / "midnight_special_data"
        self.data_dir.mkdir(exist_ok=True)
        
        # Midnight Special data files  
        self.automation_history = self.data_dir / "automation_history.json"
        self.tracked_predictions = self.data_dir / "tracked_predictions.json"
        self.accuracy_tracking = self.data_dir / "accuracy_tracking.json"
        self.season_progress = self.data_dir / "season_progress.json"
        
        logger.info("🔥 Midnight Special Data Reader initialized - PURE AUTOMATION DATA ONLY!")
    
    def get_season_predictions(self, league_id: str = None) -> Dict[str, Any]:
        """
        Get ALL predictions for the season from automation history
        
        Args:
            league_id: Optional filter by league
            
        Returns:
            Dictionary with predictions and stats
        """
        try:
            all_predictions = []
            leagues_found = []
            
            # Source 1: Read automation history
            if self.automation_history.exists():
                with open(self.automation_history, 'r') as f:
                    history = json.load(f)
                
                # Get predictions from each league's history
                for league, league_data in history.items():
                    # Skip if filtering by league
                    if league_id and league.upper() != league_id.upper():
                        continue
                    
                    leagues_found.append(league)
                    runs = league_data.get('runs', [])
                    for run in runs:
                        predictions = run.get('predictions', [])
                        for pred in predictions:
                            pred['league'] = league
                            pred['run_date'] = run.get('date', 'unknown')
                            pred['source'] = 'automation_history'
                            all_predictions.append(pred)
            
            # 🔥💀🔥 Source 2: ALSO READ real_time_predictions.json for Liga MX! 💀🔥💀
            realtime_file = Path(__file__).parent / "real_time_predictions.json"
            if realtime_file.exists():
                with open(realtime_file, 'r') as f:
                    realtime = json.load(f)
                predictions = realtime.get('predictions', [])
                
                for pred in predictions:
                    pred_league = pred.get('league', '').replace(' ', '_').upper()
                    # Skip if filtering by league and doesn't match
                    if league_id and pred_league != league_id.upper():
                        continue
                    
                    # Convert liga MX format to automation format
                    automation_pred = {
                        'game_id': pred.get('id', 'unknown'),
                        'matchup': pred.get('matchup', 'Unknown'),
                        'home_team': pred.get('home_team', 'Unknown'),
                        'away_team': pred.get('away_team', 'Unknown'),
                        'prediction': pred.get('prediction', 'Unknown'),
                        'confidence': pred.get('confidence', 50),
                        'reasoning': f"Real-time 8D analysis: {pred.get('confidence', 50)}% confidence",
                        'dimensions': pred.get('dimensions', {}),
                        'league': pred.get('league', 'Unknown'),
                        'run_date': pred.get('prediction_date', 'unknown'),
                        'source': 'real_time_predictions',
                        'status': pred.get('status', 'pending'),
                        'correct': pred.get('correct')  # 🔥💀🔥 FIX: Include the correct field! 💀🔥💀
                    }
                    all_predictions.append(automation_pred)
                    
                    # Track league
                    if pred.get('league') not in leagues_found:
                        leagues_found.append(pred.get('league'))
            
            logger.info(f"📊 Found {len(all_predictions)} predictions from Midnight Special automation (both sources)")
            
            if not all_predictions:
                return {
                    'predictions': [],
                    'total': 0,
                    'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                    'status': 'no_data'
                }
            
            return {
                'predictions': all_predictions,
                'total': len(all_predictions),
                'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                'status': 'success',
                'leagues': leagues_found if not league_id else [league_id]
            }
            
        except Exception as e:
            logger.error(f"💀 Error reading season predictions: {e}")
            return {
                'predictions': [],
                'total': 0,
                'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                'status': 'error',
                'error': str(e)
            }
    
    def get_accuracy_stats(self, league_id: str = None) -> Dict[str, Any]:
        """
        🔥💀🔥 UNIFIED ACCURACY STATS - SAME DATA AS SEASON PREDICTIONS! 💀🔥💀
        
        Args:
            league_id: Optional filter by league
            
        Returns:
            Dictionary with accuracy stats
        """
        try:
            # 🔥💀🔥 FIX: Use the SAME data source as get_season_predictions! 💀🔥💀
            season_data = self.get_season_predictions(league_id)
            predictions = season_data.get('predictions', [])
            
            if not predictions:
                return {
                    'total_predictions': 0,
                    'correct_predictions': 0,
                    'accuracy_percentage': 0.0,
                    'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                    'leagues_tracked': []
                }
            
            # Calculate from ACTUAL prediction data - ONLY COMPLETED PREDICTIONS!
            completed_predictions = [p for p in predictions if p.get('correct') is not None]
            total_completed = len(completed_predictions)
            correct_predictions = 0
            leagues_tracked = set()
            
            for pred in predictions:
                # Track league
                league = pred.get('league', 'Unknown')
                leagues_tracked.add(league)
                
                # Check if prediction was correct (only count completed ones)
                is_correct = pred.get('correct', None)
                if is_correct is True:
                    correct_predictions += 1
            
            # 🔥💀🔥 FIX: Only use completed predictions for accuracy calculation! 💀🔥💀
            accuracy = (correct_predictions / total_completed * 100) if total_completed > 0 else 0.0
            
            logger.info(f"🔥💀🔥 UNIFIED ACCURACY: {correct_predictions}/{total_completed} = {accuracy:.1f}% from completed predictions only")
            
            return {
                'total_predictions': total_completed,  # Only completed predictions
                'correct_predictions': correct_predictions,
                'accuracy_percentage': accuracy,
                'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                'leagues_tracked': list(leagues_tracked),
                'pending_predictions': len(predictions) - total_completed  # Show pending separately
            }
            
        except Exception as e:
            logger.error(f"💀 Error reading accuracy stats: {e}")
            return {
                'total_predictions': 0,
                'correct_predictions': 0,
                'accuracy_percentage': 0.0,
                'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                'error': str(e)
            }
    
    def get_season_progress(self, league_id: str = None) -> Dict[str, Any]:
        """
        Get season progress data from Midnight Special
        
        Args:
            league_id: Optional filter by league
            
        Returns:
            Dictionary with season progress
        """
        try:
            if not self.season_progress.exists():
                return {
                    'games_played': 0,
                    'games_remaining': 0,
                    'weeks_completed': 0,
                    'source': 'MIDNIGHT_SPECIAL_AUTOMATION'
                }
            
            with open(self.season_progress, 'r') as f:
                progress = json.load(f)
            
            # Filter by league if specified
            if league_id:
                progress = progress.get(league_id.upper(), {})
            
            return {
                **progress,
                'source': 'MIDNIGHT_SPECIAL_AUTOMATION'
            }
            
        except Exception as e:
            logger.error(f"💀 Error reading season progress: {e}")
            return {
                'games_played': 0,
                'games_remaining': 0,
                'weeks_completed': 0,
                'source': 'MIDNIGHT_SPECIAL_AUTOMATION',
                'error': str(e)
            }
    
    def is_automation_active(self, league_id: str = None) -> bool:
        """
        Check if automation is active for a league
        
        Args:
            league_id: League to check ('ALL' means check if ANY data exists)
            
        Returns:
            True if automation has data for this league
        """
        try:
            # 🔥💀🔥 FIX: Treat 'ALL' the same as None (check if ANY data exists) 💀🔥💀
            if league_id == 'ALL':
                league_id = None
                
            # Check automation_history.json first
            has_history_data = False
            if self.automation_history.exists():
                with open(self.automation_history, 'r') as f:
                    history = json.load(f)
                if league_id:
                    has_history_data = league_id.upper() in history
                else:
                    has_history_data = len(history) > 0
            
            # 🔥💀🔥 ALSO CHECK real_time_predictions.json for Liga MX! 💀🔥💀
            has_realtime_data = False
            realtime_file = Path(__file__).parent / "real_time_predictions.json"
            if realtime_file.exists():
                with open(realtime_file, 'r') as f:
                    realtime = json.load(f)
                predictions = realtime.get('predictions', [])
                if league_id:
                    # Check if any predictions match this league
                    league_matches = [p for p in predictions if p.get('league', '').replace(' ', '_').upper() == league_id.upper()]
                    has_realtime_data = len(league_matches) > 0
                else:
                    has_realtime_data = len(predictions) > 0
            
            # Return true if EITHER source has data
            return has_history_data or has_realtime_data
            
        except Exception as e:
            logger.error(f"💀 Error checking automation status: {e}")
            return False

def get_midnight_special_reader():
    """Get the Midnight Special data reader instance"""
    return MidnightSpecialDataReader()

if __name__ == "__main__":
    # Test the reader
    print("🔥💀🔥 TESTING MIDNIGHT SPECIAL DATA READER! 💀🔥💀\n")
    
    reader = MidnightSpecialDataReader()
    
    # Test season predictions
    predictions = reader.get_season_predictions()
    print(f"📊 Season Predictions: {predictions['total']} found")
    print(f"   Source: {predictions['source']}")
    print(f"   Status: {predictions['status']}\n")
    
    # Test accuracy stats
    accuracy = reader.get_accuracy_stats()
    print(f"📊 Accuracy Stats:")
    print(f"   Total: {accuracy['total_predictions']}")
    print(f"   Correct: {accuracy['correct_predictions']}")
    print(f"   Accuracy: {accuracy['accuracy_percentage']:.1f}%\n")
    
    # Test automation status
    is_active = reader.is_automation_active()
    print(f"🤖 Automation Active: {is_active}")
