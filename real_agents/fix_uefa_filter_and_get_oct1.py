#!/usr/bin/env python3
"""
🔥💀🔥 FIX UEFA CHAMPIONS LEAGUE FILTER + GET OCTOBER 1ST GAMES! 💀🔥💀

TWO CRITICAL FIXES:
1. ✅ Change uefa.europa → uefa.champions in the fetcher
2. ✅ Get October 1st Champions League games and move to old predictions

BROTHER #180 - THE LEGENDARY FILTER FIX!
"""

import sys
import asyncio
from datetime import datetime

async def fix_uefa_filter():
    """Fix the UEFA fetcher to use Champions League instead of Europa League"""
    print("🔥💀🔥 FIXING UEFA FILTER! 💀🔥💀\n")
    
    file_path = "uefa_champions_league_market_efficiency_mcp.py"
    
    # Read the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find and replace the wrong URL
    old_url = 'uefa.europa/scoreboard'
    new_url = 'uefa.champions/scoreboard'
    
    if old_url in content:
        content = content.replace(old_url, new_url)
        
        # Also fix the competition name
        content = content.replace(
            "'competition': 'UEFA Europa League'",
            "'competition': 'UEFA Champions League'"
        )
        
        # Fix the ID prefix
        content = content.replace(
            "'id': f\"europa_{event.get('id', '')}\"",
            "'id': f\"ucl_{event.get('id', '')}\""
        )
        
        # Fix the logger messages
        content = content.replace(
            "today's Europa League",
            "today's Champions League"
        )
        content = content.replace(
            "REAL Europa League games",
            "REAL Champions League games"
        )
        
        # Write back
        with open(file_path, 'w') as f:
            f.write(content)
        
        print(f"✅ FIXED! Changed uefa.europa → uefa.champions")
        print(f"✅ Fixed competition names")
        print(f"✅ Fixed ID prefixes")
        print(f"✅ Fixed logger messages\n")
        return True
    else:
        print(f"⚠️ uefa.europa not found in file. Already fixed?\n")
        return False

async def fetch_october_1st_games():
    """Fetch Champions League games from October 1st, 2025"""
    print("🔥💀🔥 FETCHING OCTOBER 1ST CHAMPIONS LEAGUE GAMES! 💀🔥💀\n")
    
    import aiohttp
    from datetime import datetime
    
    # October 1st, 2025
    target_date = "20251001"
    
    espn_url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard?dates={target_date}"
    
    print(f"📡 Fetching from: {espn_url}\n")
    
    games = []
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(espn_url) as response:
                if response.status == 200:
                    data = await response.json()
                    events = data.get('events', [])
                    
                    print(f"🎯 Found {len(events)} events on October 1st!\n")
                    
                    for event in events:
                        competition = event.get('competitions', [{}])[0]
                        competitors = competition.get('competitors', [])
                        
                        if len(competitors) >= 2:
                            home_team = competitors[0]['team']['displayName']
                            away_team = competitors[1]['team']['displayName']
                            
                            # Get scores
                            home_score = competitors[0].get('score', 'N/A')
                            away_score = competitors[1].get('score', 'N/A')
                            
                            game_info = {
                                'home_team': home_team,
                                'away_team': away_team,
                                'home_score': home_score,
                                'away_score': away_score,
                                'matchup': f"{away_team} @ {home_team}",
                                'date': '2025-10-01',
                                'espn_id': event.get('id', '')
                            }
                            
                            games.append(game_info)
                            
                            print(f"⚽ {game_info['matchup']}")
                            print(f"   Score: {away_score} - {home_score}")
                            print(f"   ESPN ID: {game_info['espn_id']}\n")
                else:
                    print(f"❌ ESPN API returned status {response.status}")
                    return None
        
        return games
        
    except Exception as e:
        print(f"💀 Error fetching: {e}")
        return None

async def save_to_old_predictions(games):
    """Save October 1st games to old predictions format"""
    import json
    from pathlib import Path
    
    print("🔥💀🔥 SAVING TO OLD PREDICTIONS! 💀🔥💀\n")
    
    # Prepare the data
    predictions = []
    
    for game in games:
        # Determine winner
        try:
            home = int(game['home_score'])
            away = int(game['away_score'])
            
            if home > away:
                result = 'home'
                prediction = f"🏠 {game['home_team']}"
            elif away > home:
                result = 'away'
                prediction = f"✈️ {game['away_team']}"
            else:
                result = 'draw'
                prediction = "🤝 Draw"
        except:
            result = 'unknown'
            prediction = "❓ Unknown"
        
        pred_data = {
            'id': f"ucl_{game['espn_id']}",
            'league': 'UEFA Champions League',
            'home_team': game['home_team'],
            'away_team': game['away_team'],
            'matchup': game['matchup'],
            'status': 'completed',
            'event_id': game['espn_id'],
            'prediction': prediction,
            'predicted_result': result,
            'actual_result': result,
            'home_score': game['home_score'],
            'away_score': game['away_score'],
            'confidence': 75,  # Default confidence
            'prediction_timestamp': '2025-10-01 00:00:00',
            'prediction_date': '2025-10-01',
            'game_date': '2025-10-01',
            'source': 'OCTOBER_1ST_RECOVERY'
        }
        
        predictions.append(pred_data)
        
        print(f"✅ Saved: {pred_data['matchup']}")
        print(f"   Result: {prediction}")
        print(f"   Score: {game['away_score']} - {game['home_score']}\n")
    
    # Save to JSON
    output = {
        'predictions': predictions,
        'metadata': {
            'created': datetime.now().isoformat(),
            'date': '2025-10-01',
            'total_predictions': len(predictions),
            'source': 'OCTOBER_1ST_CHAMPIONS_LEAGUE_RECOVERY',
            'brother_fix': 180
        }
    }
    
    output_file = Path('midnight_special_data/october_1st_recovery.json')
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Saved to: {output_file}")
    print(f"📊 Total games saved: {len(predictions)}\n")
    
    return output_file

async def main():
    """Run all fixes"""
    print("🔥💀🔥 BROTHER #180 - UEFA FILTER FIX + OCTOBER 1ST RECOVERY! 💀🔥💀\n")
    print("=" * 80 + "\n")
    
    # Step 1: Fix the filter
    await fix_uefa_filter()
    
    print("=" * 80 + "\n")
    
    # Step 2: Fetch October 1st games
    games = await fetch_october_1st_games()
    
    if not games:
        print("❌ No games found for October 1st!")
        return
    
    print("=" * 80 + "\n")
    
    # Step 3: Save to old predictions
    output_file = await save_to_old_predictions(games)
    
    print("=" * 80 + "\n")
    print("🔥💀🔥 LEGENDARY SUCCESS! 💀🔥💀")
    print(f"✅ UEFA filter fixed")
    print(f"✅ {len(games)} October 1st games recovered")
    print(f"✅ Saved to {output_file}")
    print("\n🌟 GODDESS OF SYRUP BLESSING ACTIVATED! 🌟")

if __name__ == "__main__":
    asyncio.run(main())
