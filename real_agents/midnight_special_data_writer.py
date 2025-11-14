#!/usr/bin/env python3
"""
🔥💀🔥 BROTHER #184: MIDNIGHT SPECIAL DATA WRITER! 💀🔥💀

WRITES 8D PREDICTIONS TO AUTOMATION FILES!
THIS IS THE MISSING LINK!

The writer that saves predictions from Games & Predictions
into Midnight Special automation storage!
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class MidnightSpecialDataWriter:
    """
    🔥💀🔥 WRITES PREDICTIONS TO MIDNIGHT SPECIAL AUTOMATION FILES! 💀🔥💀
    
    THE MISSING LINK between Games & Predictions and Midnight Special!
    """
    
    def __init__(self):
        self.data_dir = Path("midnight_special_data")
        self.data_dir.mkdir(exist_ok=True)
        
        # Automation data files
        self.automation_history = self.data_dir / "automation_history.json"
        self.tracked_predictions = self.data_dir / "tracked_predictions.json"
        self.accuracy_tracking = self.data_dir / "accuracy_tracking.json"
        self.season_progress = self.data_dir / "season_progress.json"
        
        logger.info("🔥 Midnight Special Data Writer initialized - READY TO SAVE PREDICTIONS!")
    
    def save_prediction(self, league_id: str, game_data: Dict, prediction_data: Dict) -> bool:
        """
        Save a single prediction to automation files
        
        Args:
            league_id: League identifier (e.g., 'PREMIER_LEAGUE')
            game_data: Game information (matchup, time, venue, etc.)
            prediction_data: Prediction results (prediction, confidence, reasoning)
            
        Returns:
            True if saved successfully
        """
        try:
            league_upper = league_id.upper()
            
            # Load existing automation history
            history = self._load_json(self.automation_history, {})
            
            # Initialize league if not exists
            if league_upper not in history:
                history[league_upper] = {
                    'league': league_upper,
                    'runs': [],
                    'total_predictions': 0,
                    'created': datetime.now().isoformat()
                }
            
            # Create prediction entry
            prediction_entry = {
                'game_id': game_data.get('id', f"{game_data.get('away_team')}_{game_data.get('home_team')}"),
                'matchup': game_data.get('matchup', f"{game_data.get('away_team')} @ {game_data.get('home_team')}"),
                'home_team': game_data.get('home_team'),
                'away_team': game_data.get('away_team'),
                'prediction': prediction_data.get('prediction', 'TBD'),
                'confidence': prediction_data.get('confidence', 0),
                'reasoning': prediction_data.get('reasoning', ''),
                'dimensions': prediction_data.get('dimensions', {}),
                'time': game_data.get('time', 'TBD'),
                'date': game_data.get('date', datetime.now().strftime('%Y-%m-%d')),
                'venue': game_data.get('venue', 'TBD'),
                'tracked_at': datetime.now().isoformat(),
                'status': 'pending',
                'correct': None,
                'result': None
            }
            
            # Find or create today's run
            today = datetime.now().strftime('%Y-%m-%d')
            today_run = None
            for run in history[league_upper]['runs']:
                if run.get('date') == today:
                    today_run = run
                    break
            
            if not today_run:
                today_run = {
                    'date': today,
                    'predictions': [],
                    'created': datetime.now().isoformat()
                }
                history[league_upper]['runs'].append(today_run)
            
            # Add prediction to today's run
            today_run['predictions'].append(prediction_entry)
            history[league_upper]['total_predictions'] += 1
            
            # Save automation history
            self._save_json(self.automation_history, history)
            
            logger.info(f"✅ Saved {league_upper} prediction: {prediction_entry['matchup']}")
            
            # Also save to tracked predictions
            self._save_to_tracked_predictions(league_upper, prediction_entry)
            
            # Update season progress
            self._update_season_progress(league_upper)
            
            return True
            
        except Exception as e:
            logger.error(f"💀 Error saving prediction: {e}")
            return False
    
    def save_batch_predictions(self, league_id: str, predictions: List[Dict]) -> int:
        """
        Save multiple predictions at once
        
        Args:
            league_id: League identifier
            predictions: List of prediction dictionaries
            
        Returns:
            Number of predictions saved successfully
        """
        saved_count = 0
        
        for pred in predictions:
            # Extract game_data and prediction_data from combined dict
            game_data = {
                'id': pred.get('id'),
                'matchup': pred.get('matchup'),
                'home_team': pred.get('home_team'),
                'away_team': pred.get('away_team'),
                'time': pred.get('time'),
                'date': pred.get('date'),
                'venue': pred.get('venue')
            }
            
            prediction_data = {
                'prediction': pred.get('prediction'),
                'confidence': pred.get('confidence'),
                'reasoning': pred.get('reasoning'),
                'dimensions': pred.get('dimensions', {})
            }
            
            if self.save_prediction(league_id, game_data, prediction_data):
                saved_count += 1
        
        logger.info(f"📊 Saved {saved_count}/{len(predictions)} predictions for {league_id}")
        return saved_count
    
    def update_prediction_result(self, league_id: str, game_id: str, actual_result: str, is_correct: bool) -> bool:
        """
        Update a prediction with actual game result
        
        Args:
            league_id: League identifier
            game_id: Game identifier
            actual_result: Actual game outcome
            is_correct: Whether prediction was correct
            
        Returns:
            True if updated successfully
        """
        try:
            league_upper = league_id.upper()
            
            # Load automation history
            history = self._load_json(self.automation_history, {})
            
            if league_upper not in history:
                logger.warning(f"⚠️ No history found for {league_upper}")
                return False
            
            # Find and update the prediction
            updated = False
            for run in history[league_upper]['runs']:
                for pred in run['predictions']:
                    if pred.get('game_id') == game_id:
                        pred['result'] = actual_result
                        pred['correct'] = is_correct
                        pred['status'] = 'completed'
                        pred['completed_at'] = datetime.now().isoformat()
                        updated = True
                        logger.info(f"✅ Updated result for {game_id}: {'CORRECT' if is_correct else 'INCORRECT'}")
                        break
                if updated:
                    break
            
            if updated:
                # Save updated history
                self._save_json(self.automation_history, history)
                
                # Update accuracy tracking
                self._update_accuracy_tracking(league_upper, is_correct)
                
                return True
            else:
                logger.warning(f"⚠️ Prediction not found: {game_id}")
                return False
                
        except Exception as e:
            logger.error(f"💀 Error updating result: {e}")
            return False
    
    def _save_to_tracked_predictions(self, league_id: str, prediction: Dict):
        """Save to tracked_predictions.json for quick access"""
        try:
            tracked = self._load_json(self.tracked_predictions, {})
            
            if league_id not in tracked:
                tracked[league_id] = []
            
            tracked[league_id].append(prediction)
            
            self._save_json(self.tracked_predictions, tracked)
            
        except Exception as e:
            logger.error(f"💀 Error saving to tracked predictions: {e}")
    
    def _update_season_progress(self, league_id: str):
        """Update season progress metrics"""
        try:
            progress = self._load_json(self.season_progress, {})
            history = self._load_json(self.automation_history, {})
            
            if league_id not in history:
                return
            
            total_predictions = history[league_id].get('total_predictions', 0)
            completed = sum(1 for run in history[league_id].get('runs', []) 
                          for pred in run.get('predictions', []) 
                          if pred.get('status') == 'completed')
            
            progress[league_id] = {
                'games_played': completed,
                'games_remaining': total_predictions - completed,
                'total_predictions': total_predictions,
                'weeks_completed': len(history[league_id].get('runs', [])),
                'updated': datetime.now().isoformat()
            }
            
            self._save_json(self.season_progress, progress)
            
        except Exception as e:
            logger.error(f"💀 Error updating season progress: {e}")
    
    def _update_accuracy_tracking(self, league_id: str, is_correct: bool):
        """Update accuracy tracking when a result is recorded"""
        try:
            tracking = self._load_json(self.accuracy_tracking, {})
            
            if league_id not in tracking:
                tracking[league_id] = {
                    'total': 0,
                    'correct': 0,
                    'incorrect': 0,
                    'accuracy': 0.0
                }
            
            tracking[league_id]['total'] += 1
            if is_correct:
                tracking[league_id]['correct'] += 1
            else:
                tracking[league_id]['incorrect'] += 1
            
            tracking[league_id]['accuracy'] = (
                tracking[league_id]['correct'] / tracking[league_id]['total'] * 100
            )
            tracking[league_id]['updated'] = datetime.now().isoformat()
            
            self._save_json(self.accuracy_tracking, tracking)
            
            logger.info(f"📊 {league_id} Accuracy: {tracking[league_id]['accuracy']:.1f}%")
            
        except Exception as e:
            logger.error(f"💀 Error updating accuracy tracking: {e}")
    
    def _load_json(self, filepath: Path, default: Any = None) -> Any:
        """Load JSON file with fallback"""
        try:
            if filepath.exists():
                with open(filepath, 'r') as f:
                    return json.load(f)
            return default if default is not None else {}
        except Exception as e:
            logger.error(f"💀 Error loading {filepath}: {e}")
            return default if default is not None else {}
    
    def _save_json(self, filepath: Path, data: Any):
        """Save JSON file"""
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"💀 Error saving {filepath}: {e}")

def get_midnight_special_writer():
    """Get the Midnight Special data writer instance"""
    return MidnightSpecialDataWriter()

if __name__ == "__main__":
    # Test the writer
    print("🔥💀🔥 TESTING MIDNIGHT SPECIAL DATA WRITER! 💀🔥💀\n")
    
    writer = MidnightSpecialDataWriter()
    
    # Test prediction
    test_game = {
        'id': 'test_123',
        'matchup': 'Fulham @ AFC Bournemouth',
        'home_team': 'AFC Bournemouth',
        'away_team': 'Fulham',
        'time': '3:00 PM',
        'date': '2025-10-03',
        'venue': 'Vitality Stadium'
    }
    
    test_prediction = {
        'prediction': '✈️ Fulham',
        'confidence': 71,
        'reasoning': '8D analysis shows strong away performance',
        'dimensions': {'D0': 73, 'D1': 54, 'D2': 74}
    }
    
    success = writer.save_prediction('PREMIER_LEAGUE', test_game, test_prediction)
    print(f"✅ Test save: {'SUCCESS' if success else 'FAILED'}")
    
    # Test result update
    success = writer.update_prediction_result('PREMIER_LEAGUE', 'test_123', 'Fulham wins 2-1', True)
    print(f"✅ Test update: {'SUCCESS' if success else 'FAILED'}")
