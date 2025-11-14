#!/usr/bin/env python3
"""
🔥💀🔥 CLEAR OLD 3D PREDICTIONS - START FRESH WITH 7D! 💀🔥💀

This script clears all old predictions from before the 7D upgrade
so we can start tracking NEW predictions with REAL 7D analysis!
"""

import json
import os
from datetime import datetime

# Path to midnight special data
DATA_DIR = '/Users/onecoder/Projects/Total_AI_Liberation/dockerized_decentralized_agent_poly_loly/real_agents/midnight_special_data'

def clear_old_predictions():
    """Clear all old prediction data to start fresh with 7D"""
    
    print("🔥💀🔥 CLEARING OLD 3D PREDICTIONS - STARTING FRESH WITH 7D! 💀🔥💀")
    
    # Files to clear
    files_to_clear = [
        'accuracy_tracking.json',
        'automation_history.json',
        'laliga_automation_history.json',
        'lessons_learned.json',
        'season_progress.json'
    ]
    
    # Clear each file
    for filename in files_to_clear:
        filepath = os.path.join(DATA_DIR, filename)
        if os.path.exists(filepath):
            # Backup first
            backup_path = filepath + f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            os.rename(filepath, backup_path)
            print(f"📦 Backed up: {filename} -> {os.path.basename(backup_path)}")
            
            # Create fresh empty file
            with open(filepath, 'w') as f:
                json.dump({}, f)
            print(f"✅ Cleared: {filename}")
        else:
            print(f"⚠️  Not found: {filename}")
    
    # Clear season analysis files (keep structure but reset data)
    season_files = [f for f in os.listdir(DATA_DIR) if f.startswith('season_analysis_current_')]
    for filename in season_files:
        filepath = os.path.join(DATA_DIR, filename)
        # Backup
        backup_path = filepath + f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        os.rename(filepath, backup_path)
        print(f"📦 Backed up: {filename}")
    
    print("\n🔥💀🔥 OLD 3D PREDICTIONS CLEARED! READY FOR 7D GLORY! 💀🔥💀")
    print("\n📊 Next steps:")
    print("1. Restart the dashboard")
    print("2. Load UEFA league")
    print("3. Track NEW predictions with 'Track to Midnight Special' button")
    print("4. Wait for games to complete")
    print("5. Check REAL 7D accuracy!")

if __name__ == '__main__':
    clear_old_predictions()
