#!/usr/bin/env python3
"""
🎯 PREDICTION TRACKER - Save Today's Predictions for Tomorrow's Analysis
Part of The Midnight Special learning system

MISSION:
- Track all predictions made today
- Store confidence levels and reasoning
- Enable tomorrow's accuracy analysis
- Feed the BUILD TO WIN learning system
"""

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import pytz

logger = logging.getLogger(__name__)

class PredictionTracker:
    """🎯 Track predictions for midnight analysis"""
    
    def __init__(self):
        self.mexico_tz = pytz.timezone('America/Mexico_City')
        self.data_path = Path("midnight_special_data")
        self.data_path.mkdir(exist_ok=True)
        
    async def save_daily_predictions(self, predictions_data: Dict[str, Any]):
        """💾 Save today's predictions for tomorrow's midnight analysis"""
        
        today = datetime.now(self.mexico_tz).strftime("%Y-%m-%d")
        filename = self.data_path / f"predictions_{today}.json"
        
        # Enhanced prediction data structure
        enhanced_data = {
            "date": today,
            "timestamp": datetime.now(self.mexico_tz).isoformat(),
            "total_predictions": len(predictions_data.get('games', [])),
            "games": [],
            "system_version": "MIDNIGHT_SPECIAL_V1",
            "confidence_distribution": {}
        }
        
        # Process each game prediction
        confidence_buckets = {"high": 0, "medium": 0, "low": 0}
        
        for game in predictions_data.get('games', []):
            enhanced_game = {
                "home_team": game.get('home_team', ''),
                "away_team": game.get('away_team', ''), 
                "league": game.get('league', ''),
                "sport": game.get('sport', ''),
                "start_time": game.get('start_time', ''),
                "predicted_winner": game.get('predicted_winner', ''),
                "confidence": game.get('confidence', 0),
                "prediction_reasoning": game.get('analysis', ''),
                "market_efficiency": game.get('market_efficiency', 0),
                "team_performance": game.get('team_performance', 0),
                "key_players": game.get('key_players', 0),
                "venue": game.get('venue', ''),
                "source": game.get('source', ''),
                "seven_d_analysis": {
                    "dimension_1": game.get('dimension_1', {}),
                    "dimension_2": game.get('dimension_2', {}),
                    "dimension_3": game.get('dimension_3', {}),
                    "dimension_4": game.get('dimension_4', {}),
                    "dimension_5": game.get('dimension_5', {}),
                    "dimension_6": game.get('dimension_6', {}),
                    "dimension_7": game.get('dimension_7', {})
                }
            }
            
            # Track confidence distribution
            conf = enhanced_game["confidence"]
            if conf >= 75:
                confidence_buckets["high"] += 1
            elif conf >= 60:
                confidence_buckets["medium"] += 1
            else:
                confidence_buckets["low"] += 1
            
            enhanced_data["games"].append(enhanced_game)
        
        enhanced_data["confidence_distribution"] = confidence_buckets
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(enhanced_data, f, indent=2)
        
        logger.info(f"💾 Saved {len(enhanced_data['games'])} predictions for {today}")
        logger.info(f"   High confidence: {confidence_buckets['high']}")
        logger.info(f"   Medium confidence: {confidence_buckets['medium']}")
        logger.info(f"   Low confidence: {confidence_buckets['low']}")
        
        return enhanced_data

    async def extract_predictions_from_sports_data(self, sports_data: Dict[str, Any]) -> Dict[str, Any]:
        """🔍 Extract prediction data from main sports system"""
        
        predictions = {
            "games": [],
            "extraction_timestamp": datetime.now(self.mexico_tz).isoformat()
        }
        
        # Process each league's games
        for league_name, games in sports_data.items():
            if isinstance(games, list):
                for game in games:
                    # Extract prediction from game analysis
                    prediction = await self._extract_game_prediction(game, league_name)
                    if prediction:
                        predictions["games"].append(prediction)
        
        return predictions

    async def _extract_game_prediction(self, game: Dict, league: str) -> Dict[str, Any]:
        """Extract specific prediction from game data"""
        
        # Look for prediction indicators in the game data
        home_team = game.get('home_team', '')
        away_team = game.get('away_team', '')
        
        if not home_team or not away_team:
            return None
        
        # Extract prediction from various possible fields
        predicted_winner = None
        confidence = 0
        
        # Check for explicit prediction fields
        if 'predicted_winner' in game:
            predicted_winner = game['predicted_winner']
        elif 'winner_prediction' in game:
            predicted_winner = game['winner_prediction']
        elif 'prediction' in game:
            predicted_winner = game['prediction']
        
        # Extract confidence
        if 'confidence' in game:
            confidence = game['confidence']
        elif 'prediction_confidence' in game:
            confidence = game['prediction_confidence']
        
        # If no explicit prediction, try to infer from analysis
        if not predicted_winner:
            analysis = game.get('analysis', '').upper()
            if 'HOME TEAM' in analysis or 'HOME WIN' in analysis:
                predicted_winner = home_team
            elif 'AWAY TEAM' in analysis or 'AWAY WIN' in analysis:
                predicted_winner = away_team
            elif 'DRAW' in analysis:
                predicted_winner = 'DRAW'
            else:
                # Default based on team performance if available
                home_perf = game.get('team_performance', {}).get('home', 0)
                away_perf = game.get('team_performance', {}).get('away', 0)
                if home_perf > away_perf:
                    predicted_winner = home_team
                elif away_perf > home_perf:
                    predicted_winner = away_team
                else:
                    predicted_winner = 'DRAW'
        
        # Set default confidence if not found
        if confidence == 0:
            confidence = 65  # Default medium confidence
        
        return {
            "home_team": home_team,
            "away_team": away_team,
            "league": league,
            "sport": game.get('sport', league),
            "start_time": game.get('start_time', '') or game.get('date', ''),
            "predicted_winner": predicted_winner,
            "confidence": confidence,
            "analysis": game.get('analysis', ''),
            "market_efficiency": game.get('market_efficiency', 0),
            "team_performance": game.get('team_performance', 0),
            "key_players": game.get('key_players', 0),
            "venue": game.get('venue', ''),
            "source": game.get('source', ''),
            "dimension_1": game.get('dimension_1', {}),
            "dimension_2": game.get('dimension_2', {}),
            "dimension_3": game.get('dimension_3', {}),
            "dimension_4": game.get('dimension_4', {}),
            "dimension_5": game.get('dimension_5', {}),
            "dimension_6": game.get('dimension_6', {}),
            "dimension_7": game.get('dimension_7', {})
        }

async def track_todays_predictions(sports_data: Dict[str, Any]):
    """🎯 Main function to track today's predictions"""
    
    tracker = PredictionTracker()
    
    # Extract predictions from sports data
    predictions = await tracker.extract_predictions_from_sports_data(sports_data)
    
    # Save for midnight analysis
    saved_data = await tracker.save_daily_predictions(predictions)
    
    logger.info("🎯 TODAY'S PREDICTIONS TRACKED FOR MIDNIGHT SPECIAL ANALYSIS!")
    
    return saved_data

if __name__ == "__main__":
    # Test the prediction tracker
    test_data = {
        "LA_LIGA": [
            {
                "home_team": "Real Madrid",
                "away_team": "Barcelona", 
                "predicted_winner": "Real Madrid",
                "confidence": 78,
                "analysis": "Real Madrid strong home form",
                "start_time": "2025-09-15T20:00Z"
            }
        ]
    }
    
    asyncio.run(track_todays_predictions(test_data))