#!/usr/bin/env python3
"""
🎯💀🎯 MIDNIGHT PREDICTION TRACKER - EVERY PREDICTION TRACKED 🎯💀🎯
Tracks every single prediction made by the system for hardcore accuracy analysis.
"""

import json
import os
import logging
from datetime import datetime
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class MidnightPredictionTracker:
    """
    🎯 MIDNIGHT PREDICTION TRACKER 🎯
    
    Tracks every prediction made by the system, maintaining detailed records
    for accuracy analysis and learning purposes.
    """
    
    def __init__(self):
        self.predictions_file = '/tmp/midnight_predictions.json'
        logger.info("🎯 MIDNIGHT PREDICTION TRACKER INITIALIZED - TRACKING EVERYTHING!")
    
    def track_prediction(self, game_data: Dict, prediction_result: Dict) -> bool:
        """
        🎯 TRACK PREDICTION
        
        Records a new prediction for tracking and future accuracy analysis.
        """
        try:
            # Create prediction record
            prediction_record = {
                "game_id": game_data.get('id', f"game_{datetime.now().timestamp()}"),
                "date": datetime.now().strftime('%Y-%m-%d'),
                "matchup": f"{game_data.get('away_team', 'Away')} @ {game_data.get('home_team', 'Home')}",
                "prediction": prediction_result.get('prediction', 'Unknown'),
                "confidence": prediction_result.get('confidence', 0),
                "actual_result": None,  # Will be filled when game completes
                "status": "pending",
                "league": game_data.get('league', 'Unknown'),
                "analysis_timestamp": datetime.now().isoformat()
            }
            
            # Add additional prediction details if available
            if 'probabilities' in prediction_result:
                prediction_record['probabilities'] = prediction_result['probabilities']
            
            if 'reasoning' in prediction_result:
                prediction_record['reasoning'] = prediction_result['reasoning']
            
            if 'dimensions' in prediction_result:
                prediction_record['dimensions'] = prediction_result['dimensions']
            
            # Load existing predictions
            predictions = self._load_json(self.predictions_file)
            
            # Add to today's predictions
            today = prediction_record['date']
            if today not in predictions:
                predictions[today] = []
            
            predictions[today].append(prediction_record)
            
            # Save updated predictions
            self._save_json(self.predictions_file, predictions)
            
            logger.info(f"🎯 Prediction tracked: {prediction_record['matchup']} -> {prediction_record['prediction']}")
            return True
            
        except Exception as e:
            logger.error(f"🎯 TRACKING ERROR: {e}")
            return False
    
    def update_prediction_result(self, game_id: str, actual_result: str) -> bool:
        """
        🎯 UPDATE PREDICTION RESULT
        
        Updates a prediction with the actual game result for accuracy tracking.
        """
        try:
            predictions = self._load_json(self.predictions_file)
            
            # Find and update the prediction
            updated = False
            for date, date_predictions in predictions.items():
                for prediction in date_predictions:
                    if prediction.get('game_id') == game_id:
                        prediction['actual_result'] = actual_result
                        
                        # Determine if prediction was correct
                        predicted = prediction.get('prediction', '').lower()
                        actual = actual_result.lower()
                        
                        if predicted == actual:
                            prediction['status'] = 'correct'
                        else:
                            prediction['status'] = 'incorrect'
                        
                        prediction['result_timestamp'] = datetime.now().isoformat()
                        updated = True
                        break
                
                if updated:
                    break
            
            if updated:
                self._save_json(self.predictions_file, predictions)
                logger.info(f"🎯 Prediction result updated: {game_id} -> {actual_result}")
                return True
            else:
                logger.warning(f"🎯 Prediction not found for game: {game_id}")
                return False
                
        except Exception as e:
            logger.error(f"🎯 UPDATE ERROR: {e}")
            return False
    
    async def update_game_result(self, game_data: Dict, result: str) -> bool:
        """
        🎯 UPDATE GAME RESULT (Async wrapper for scheduler compatibility)
        
        Updates prediction results based on game data and actual result.
        This method is called by the midnight scheduler.
        """
        try:
            # Generate game ID from game data
            home_team = game_data.get('home_team', 'Unknown')
            away_team = game_data.get('away_team', 'Unknown')
            league = game_data.get('league', 'Unknown')
            date = game_data.get('date', datetime.now().strftime('%Y-%m-%d'))
            
            # Try different game ID formats to find existing predictions
            possible_ids = [
                f"{league}_{home_team}_{away_team}_{date.split('T')[0].replace('-', '')}",
                f"game_{home_team}_{away_team}",
                f"{away_team}_@_{home_team}",
            ]
            
            # Load existing predictions to search
            predictions = self._load_json(self.predictions_file)
            
            updated = False
            for date_key, date_predictions in predictions.items():
                for prediction in date_predictions:
                    # Check if this prediction matches our game
                    pred_matchup = prediction.get('matchup', '')
                    expected_matchup = f"{away_team} @ {home_team}"
                    
                    if (prediction.get('game_id') in possible_ids or 
                        pred_matchup == expected_matchup or
                        (home_team in pred_matchup and away_team in pred_matchup)):
                        
                        # Update the prediction result
                        prediction['actual_result'] = result
                        prediction['status'] = 'completed'
                        
                        # Determine if prediction was correct
                        predicted = prediction.get('prediction', '').lower()
                        if 'home' in predicted and result == 'home_win':
                            prediction['correct'] = True
                        elif 'away' in predicted and result == 'away_win':
                            prediction['correct'] = True
                        elif 'draw' in predicted and result == 'draw':
                            prediction['correct'] = True
                        else:
                            prediction['correct'] = False
                        
                        prediction['result_timestamp'] = datetime.now().isoformat()
                        updated = True
                        
                        logger.info(f"🎯 Game result updated: {expected_matchup} -> {result}")
                        break
                
                if updated:
                    break
            
            if updated:
                self._save_json(self.predictions_file, predictions)
                return True
            else:
                logger.info(f"🎯 No existing prediction found for {away_team} @ {home_team}")
                return False
                
        except Exception as e:
            logger.error(f"🎯 UPDATE GAME RESULT ERROR: {e}")
            return False

    def get_predictions_for_date(self, date: str) -> List[Dict]:
        """Get all predictions for a specific date"""
        try:
            predictions = self._load_json(self.predictions_file)
            return predictions.get(date, [])
        except Exception as e:
            logger.error(f"Error getting predictions for {date}: {e}")
            return []
    
    def get_accuracy_stats(self, days_back: int = 7) -> Dict:
        """Get accuracy statistics for the specified period"""
        try:
            predictions = self._load_json(self.predictions_file)
            
            total_predictions = 0
            correct_predictions = 0
            pending_predictions = 0
            
            for date, date_predictions in predictions.items():
                for prediction in date_predictions:
                    total_predictions += 1
                    
                    status = prediction.get('status', 'pending')
                    if status == 'correct':
                        correct_predictions += 1
                    elif status == 'pending':
                        pending_predictions += 1
            
            # Calculate accuracy (excluding pending)
            completed_predictions = total_predictions - pending_predictions
            accuracy = 0.0
            if completed_predictions > 0:
                accuracy = (correct_predictions / completed_predictions) * 100
            
            return {
                "total_predictions": total_predictions,
                "correct_predictions": correct_predictions,
                "pending_predictions": pending_predictions,
                "completed_predictions": completed_predictions,
                "accuracy_percentage": accuracy,
                "analysis_period": f"Last {days_back} days"
            }
            
        except Exception as e:
            logger.error(f"Error calculating accuracy stats: {e}")
            return {"error": str(e)}
    
    def _load_json(self, filepath: str) -> Dict:
        """Load JSON data from file"""
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    return json.load(f)
            else:
                return {}
        except Exception as e:
            logger.error(f"Error loading JSON from {filepath}: {e}")
            return {}
    
    def _save_json(self, filepath: str, data: Dict) -> bool:
        """Save JSON data to file"""
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error saving JSON to {filepath}: {e}")
            return False