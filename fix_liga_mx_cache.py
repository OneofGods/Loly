#!/usr/bin/env python3
"""
🔥 LIGA MX CACHE FIX - ELIMINATE EMOJI BULLSHIT FROM CACHED DATA!
Fixes the daily_predictions.json file to use proper sport routing
"""

import json
import os
from datetime import datetime

def fix_liga_mx_cached_data():
    """🔥 Fix Liga MX games in cached daily_predictions.json"""
    
    data_file = "/Users/onecoder/Projects/Total_AI_Liberation/dockerized_decentralized_agent_poly_loly/data/daily_predictions.json"
    
    if not os.path.exists(data_file):
        print("❌ No daily_predictions.json file found!")
        return
    
    print("🔥 LOADING CACHED DATA...")
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    total_games = len(data.get('games', []))
    liga_mx_games_fixed = 0
    
    print(f"📊 Found {total_games} total games in cache")
    
    # Fix Liga MX games
    for game in data.get('games', []):
        league = game.get('league', '')
        
        # Check for Liga MX with emoji names
        if '🇲🇽 Liga MX' in league or 'Liga MX' in league:
            print(f"🇲🇽 FIXING LIGA MX GAME: {game.get('away_team')} @ {game.get('home_team')}")
            
            # Add proper sport field for MCP routing
            game['sport'] = 'LIGA_MX'
            
            # Clean up league name (remove emoji)
            game['league'] = 'LIGA_MX'
            
            liga_mx_games_fixed += 1
            print(f"   ✅ Fixed: sport=LIGA_MX, league=LIGA_MX")
    
    print(f"🔥 FIXED {liga_mx_games_fixed} Liga MX games")
    
    # Create backup first
    backup_file = data_file + ".backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"💾 BACKUP CREATED: {backup_file}")
    
    # Save fixed data
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ CACHE FIXED! {liga_mx_games_fixed} Liga MX games now have proper sport routing")
    print("🔥 NO MORE EMOJI BULLSHIT IN CACHED DATA!")

if __name__ == "__main__":
    fix_liga_mx_cached_data()