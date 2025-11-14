#!/usr/bin/env python3
"""
🔥💀🔥 MAKE EPL PREDICTION FOR TODAY'S GAME! 💀🔥💀
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path

async def make_epl_prediction():
    """Make prediction for today's EPL game"""
    print("🔥💀🔥 MAKING EPL PREDICTION WITH 8D SYSTEM! 💀🔥💀\n")
    
    # Import fetcher
    from premier_league_fetcher import PremierLeagueFetcher
    from universal_prediction_engine import get_universal_prediction_engine
    
    # Fetch today's games
    fetcher = PremierLeagueFetcher()
    games = await fetcher.get_todays_games()
    
    if not games:
        print("⚠️ No EPL games found for today!")
        return
    
    print(f"✅ Found {len(games)} EPL game(s)!\n")
    
    # Initialize prediction engine
    engine = get_universal_prediction_engine()
    
    predictions = []
    
    for game in games:
        print(f"🎯 Predicting: {game['matchup']}\n")
        
        # Make prediction using 8D system
        prediction = engine.analyze_game(
            game_data=game,
            league_id='PREMIER_LEAGUE'
        )
        
        predictions.append(prediction)
        
        # Display prediction
        print(f"⚽ PREDICTION: {prediction['prediction']}")
        print(f"📊 CONFIDENCE: {prediction['confidence']}%")
        print(f"\n🎲 8D DIMENSIONS:")
        dims = prediction.get('dimensions', {})
        for dim_name, dim_value in dims.items():
            print(f"   {dim_name}: {dim_value}%")
        
        print(f"\n💡 REASONING: {prediction.get('reasoning', 'N/A')}\n")
    
    # Save predictions
    output = {
        'predictions': predictions,
        'metadata': {
            'created': datetime.now().isoformat(),
            'league': 'English Premier League',
            'total_predictions': len(predictions),
            'source': 'BROTHER_181_EPL_FIRST_PREDICTION',
            'prediction_date': datetime.now().strftime('%Y-%m-%d')
        }
    }
    
    output_file = Path('epl_predictions_oct3_2025.json')
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Saved prediction to: {output_file}\n")
    print("🔥💀🔥 EPL PREDICTION COMPLETE! 💀🔥💀")
    print("⚽ THE PREMIER LEAGUE IS NOW PART OF THE 8D SYSTEM! ⚽")
    
    return predictions

if __name__ == "__main__":
    asyncio.run(make_epl_prediction())
