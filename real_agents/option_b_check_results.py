#!/usr/bin/env python3
"""
🔥💀🔥 OPTION B: RESULTS CHECKER! 💀🔥💀

Checks today's game results and compares against our predictions!
Run this TONIGHT after games finish!
"""

import asyncio
import aiohttp
import json
from datetime import datetime
from pathlib import Path

class ResultsChecker:
    def __init__(self):
        self.predictions_file = Path("real_time_predictions.json")
    
    def load_predictions(self):
        """Load our saved predictions"""
        if not self.predictions_file.exists():
            print("❌ No predictions file found!")
            return None
        
        with open(self.predictions_file, 'r') as f:
            return json.load(f)
    
    async def check_game_result(self, game):
        """Check if a game has finished and get the result"""
        today = datetime.now().strftime('%Y%m%d')
        league_map = {
            'Liga MX': 'mex.1',
            'Premier League': 'eng.1',
            'La Liga': 'esp.1',
            'Serie A': 'ita.1',
            'Bundesliga': 'ger.1',
            'Ligue 1': 'fra.1'
        }
        
        league_id = league_map.get(game['league'])
        if not league_id:
            return None
        
        url = f'https://site.api.espn.com/apis/site/v2/sports/soccer/{league_id}/scoreboard?dates={today}'
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        events = data.get('events', [])
                        
                        for event in events:
                            if str(event.get('id', '')) == str(game['event_id']):
                                comp = event.get('competitions', [{}])[0]
                                competitors = comp.get('competitors', [])
                                status = comp.get('status', {}).get('type', {}).get('description', 'Unknown')
                                
                                if len(competitors) >= 2 and status == 'Full Time':
                                    home_score = int(competitors[0].get('score', 0))
                                    away_score = int(competitors[1].get('score', 0))
                                    
                                    if home_score > away_score:
                                        actual_result = 'home'
                                    elif away_score > home_score:
                                        actual_result = 'away'
                                    else:
                                        actual_result = 'draw'
                                    
                                    return {
                                        'home_score': home_score,
                                        'away_score': away_score,
                                        'actual_result': actual_result,
                                        'status': status
                                    }
                                elif status != 'Full Time':
                                    return {'status': status}
            except Exception as e:
                print(f"⚠️ Error checking {game['matchup']}: {e}")
        
        return None
    
    async def check_all_results(self):
        """Check results for all our predictions"""
        data = self.load_predictions()
        if not data:
            return
        
        predictions = data.get('predictions', [])
        pending = [p for p in predictions if p.get('status') == 'pending']
        
        if not pending:
            print("❌ No pending predictions found!")
            return
        
        print(f"🔍 Checking results for {len(pending)} predictions...\n")
        
        completed = 0
        correct = 0
        incorrect = 0
        still_pending = 0
        
        for pred in pending:
            print(f"⚽ {pred['matchup']} ({pred['league']})")
            print(f"  🔮 Our Prediction: {pred['prediction']} ({pred['confidence']}%)")
            
            result = await self.check_game_result(pred)
            
            if result and result.get('status') == 'Full Time':
                print(f"  📊 Final Score: {result['away_score']}-{result['home_score']}")
                print(f"  🎯 Actual Result: {result['actual_result']}")
                
                is_correct = pred['predicted_result'] == result['actual_result']
                
                if is_correct:
                    print(f"  ✅ CORRECT!")
                    correct += 1
                else:
                    print(f"  ❌ WRONG!")
                    incorrect += 1
                
                completed += 1
                pred['status'] = 'completed'
                pred['actual_result'] = result['actual_result']
                pred['home_score'] = result['home_score']
                pred['away_score'] = result['away_score']
                pred['is_correct'] = is_correct
            else:
                status = result.get('status', 'Unknown') if result else 'Not Started'
                print(f"  ⏳ Status: {status}")
                still_pending += 1
            
            print()
        
        # Save updated predictions
        with open(self.predictions_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        # Show summary
        print("="*60)
        print("🔥💀🔥 REAL-TIME ACCURACY RESULTS 💀🔥💀\n")
        print(f"📊 Games Completed: {completed}")
        print(f"✅ Correct Predictions: {correct}")
        print(f"❌ Wrong Predictions: {incorrect}")
        print(f"⏳ Still Pending: {still_pending}\n")
        
        if completed > 0:
            accuracy = (correct / completed) * 100
            print(f"🎯 **REAL 8D SYSTEM ACCURACY: {accuracy:.1f}%**\n")
            
            if accuracy > 50:
                print("🏆 BETTER THAN RANDOM! WE'RE WINNING!")
            elif accuracy > 33.3:
                print("💪 BEATING 3-WAY RANDOM CHANCE (33.3%)!")
            else:
                print("⚠️ Below random chance... need Option C!")
        
        print("="*60)

async def main():
    print("🔥💀🔥 RESULTS CHECKER 💀🔥💀\n")
    checker = ResultsChecker()
    await checker.check_all_results()

if __name__ == "__main__":
    asyncio.run(main())
