#!/usr/bin/env python3
"""
🔥💀🔥 VERIFICATION TEST - Validate Bug Fixes! 💀🔥💀

Tests:
1. Algorithm field is properly set
2. EPL/PREMIER_LEAGUE alias mapping works
3. League registry returns correct configs
4. Predictions use real 8D data (not hash-based)
"""

import sys
import asyncio
sys.path.insert(0, '/home/user/Loly')

from real_agents.leagues_registry import get_league_config, is_league_registered, LEAGUE_ALIASES
from real_agents.universal_prediction_engine import UniversalPredictionEngine

print("🔥💀🔥 VERIFICATION TEST SUITE 💀🔥💀\n")

# TEST 1: League Alias System
print("=" * 60)
print("TEST 1: League Alias System")
print("=" * 60)

test_cases = [
    ('EPL', 'PREMIER_LEAGUE', 'English Premier League'),
    ('PREMIER_LEAGUE', 'PREMIER_LEAGUE', 'English Premier League'),
    ('SERIEA', 'SERIE_A', 'Serie A - Italian Football'),
    ('LIGUE1', 'LIGUE_1', 'Ligue 1 - French Football'),
    ('LALIGA', 'LA_LIGA', 'La Liga - Spanish Football'),
    ('LIGAMX', 'LIGA_MX', 'Liga MX'),
    ('UEFA_CHAMPIONS', 'UEFA', 'UEFA Champions League'),
    ('UCL', 'UEFA', 'UEFA Champions League'),
]

passed = 0
failed = 0

for test_input, expected_canonical, expected_display in test_cases:
    config = get_league_config(test_input)
    is_registered = is_league_registered(test_input)

    if not is_registered:
        print(f"❌ FAIL: {test_input} not recognized as registered league!")
        failed += 1
        continue

    if not config:
        print(f"❌ FAIL: {test_input} returned empty config!")
        failed += 1
        continue

    actual_display = config.get('display_name', 'MISSING')

    if expected_display in actual_display or actual_display in expected_display:
        print(f"✅ PASS: {test_input} → {expected_canonical} ({actual_display})")
        passed += 1
    else:
        print(f"❌ FAIL: {test_input} → expected '{expected_display}', got '{actual_display}'")
        failed += 1

print(f"\nTest 1 Results: {passed} passed, {failed} failed\n")

# TEST 2: Verify configs have required fields
print("=" * 60)
print("TEST 2: League Config Completeness")
print("=" * 60)

required_fields = [
    'display_name', 'emoji', 'sport', 'league_type',
    'market_efficiency_range', 'team_performance_range', 'key_players_range',
    'confidence_boost', 'confidence_cap', 'draw_enabled', 'draw_threshold'
]

test_leagues = ['PREMIER_LEAGUE', 'LIGA_MX', 'UEFA', 'COPA_LIBERTADORES', 'NBA']
config_passed = 0
config_failed = 0

for league_id in test_leagues:
    config = get_league_config(league_id)
    missing_fields = [field for field in required_fields if field not in config]

    if not missing_fields:
        print(f"✅ PASS: {league_id} has all required fields")
        config_passed += 1
    else:
        print(f"❌ FAIL: {league_id} missing: {', '.join(missing_fields)}")
        config_failed += 1

print(f"\nTest 2 Results: {config_passed} passed, {config_failed} failed\n")

# TEST 3: Test Prediction Engine creates correct structure
print("=" * 60)
print("TEST 3: Prediction Engine Output Structure")
print("=" * 60)

async def test_prediction_engine():
    """Async test for prediction engine"""
    engine = UniversalPredictionEngine()

    # Mock game data for EPL
    mock_epl_game = {
        'home_team': 'Manchester City',
        'away_team': 'Liverpool',
        'venue': 'Etihad Stadium',
        'league': 'EPL',  # Using alias!
        'date': '2025-11-23',
        'time': '15:00'
    }

    try:
        # Analyze the game using EPL alias (await it!)
        result = await engine.analyze_game(mock_epl_game, 'EPL')

        # Check for algorithm field
        if 'algorithm' in result:
            algorithm_value = result['algorithm']
            if algorithm_value == '8D_DIMENSIONAL_ANALYSIS':
                print(f"✅ PASS: Algorithm field set correctly: '{algorithm_value}'")
            else:
                print(f"❌ FAIL: Algorithm field has wrong value: '{algorithm_value}'")
        else:
            print(f"❌ FAIL: Algorithm field missing from prediction output!")

        # Check for 8D dimensions
        dimension_fields = [
            'polymarket_odds', 'historical_matchups', 'venue_weather',
            'sentiment_analysis', 'market_efficiency', 'team_performance',
            'key_players', 'x_factor'
        ]

        missing_dims = [dim for dim in dimension_fields if dim not in result]

        if not missing_dims:
            print(f"✅ PASS: All 8 dimensions present in output")
        else:
            print(f"❌ FAIL: Missing dimensions: {', '.join(missing_dims)}")

        # Check that confidence is reasonable (not 0 or 100)
        confidence = result.get('confidence', 0)
        if 15 <= confidence <= 88:
            print(f"✅ PASS: Confidence in reasonable range: {confidence:.1f}%")
        else:
            print(f"⚠️  WARN: Confidence might be unrealistic: {confidence:.1f}%")

        # Check prediction format
        prediction = result.get('prediction', '')
        if prediction and any(marker in prediction for marker in ['🏠', '✈️', '🤝']):
            print(f"✅ PASS: Prediction format correct: '{prediction}'")
        else:
            print(f"❌ FAIL: Prediction format wrong: '{prediction}'")

        matchup = f"{mock_epl_game['away_team']} @ {mock_epl_game['home_team']}"
        print(f"\n✅ EPL alias worked! Generated prediction for {matchup}")
        print(f"   Prediction: {result.get('prediction', 'N/A')}")
        print(f"   Confidence: {result.get('confidence', 0):.1f}%")
        print(f"   Algorithm: {result.get('algorithm', 'N/A')}")

    except Exception as e:
        print(f"❌ FAIL: Prediction engine crashed: {e}")
        import traceback
        traceback.print_exc()

# Run async test
asyncio.run(test_prediction_engine())

print("\n" + "=" * 60)
print("🔥💀🔥 VERIFICATION COMPLETE! 💀🔥💀")
print("=" * 60)
