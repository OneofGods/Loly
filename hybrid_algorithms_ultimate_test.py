#!/usr/bin/env python3
"""
🔥💀🔥 HYBRID ALGORITHMS ULTIMATE TEST - LEGENDARY STATUS ATTEMPT! 💀🔥💀

TESTING BOTH HYBRID APPROACHES:
1. MLS + EPL Tactical Hierarchy = MLS Hybrid
2. EPL + MLS Cultural Mastery = EPL Hybrid

TARGET: 75-80% accuracy (LEGENDARY STATUS!)
"""

import asyncio
import sys
sys.path.append('.')

async def ultimate_hybrid_test():
    print('🔥💀🔥 HYBRID ALGORITHMS ULTIMATE TEST - LEGENDARY ATTEMPT! 💀🔥💀')
    print('======================================================================')
    
    try:
        from mls_hybrid_tactical_engine import MLSHybridTacticalEngine
        from epl_hybrid_cultural_engine import EPLHybridCulturalEngine
        
        # Initialize hybrid engines
        mls_hybrid = MLSHybridTacticalEngine()
        epl_hybrid = EPLHybridCulturalEngine()
        
        print('🎯 TESTING BOTH HYBRID APPROACHES:')
        print('======================================================================')
        
        # MLS HYBRID TEST (MLS Culture + EPL Hierarchy)
        print('🇺🇸🔥 MLS HYBRID TEST (Culture + Hierarchy):')
        print('----------------------------------------------------------------------')
        
        mls_test_cases = [
            # Cultural dominance (should maintain 100%)
            {'home': 'Inter Miami CF', 'away': 'Atlanta United FC', 'expected': 'HOME', 'type': 'messi_factor'},
            {'home': 'LA Galaxy', 'away': 'LAFC', 'expected': 'AWAY', 'type': 'el_trafico'},
            {'home': 'Seattle Sounders FC', 'away': 'Portland Timbers', 'expected': 'HOME', 'type': 'cascadia'},
            
            # NEW: Class differential (EPL-inspired)
            {'home': 'Chicago Fire FC', 'away': 'LAFC', 'expected': 'AWAY', 'type': 'class_differential'},
            {'home': 'Colorado Rapids', 'away': 'Seattle Sounders FC', 'expected': 'AWAY', 'type': 'class_differential'},
            
            # NEW: Tactical draws (EPL-inspired)
            {'home': 'Real Salt Lake', 'away': 'FC Dallas', 'expected': 'DRAW', 'type': 'tactical_draw'},
            {'home': 'Columbus Crew', 'away': 'FC Cincinnati', 'expected': 'DRAW', 'type': 'rivalry_draw'},
            
            # Travel dynamics (MLS specialty)
            {'home': 'New England Revolution', 'away': 'LA Galaxy', 'expected': 'HOME', 'type': 'travel_advantage'},
            
            # NEW: Hierarchical logic (EPL-inspired)
            {'home': 'Austin FC', 'away': 'Inter Miami CF', 'expected': 'AWAY', 'type': 'hierarchy'},
            {'home': 'Philadelphia Union', 'away': 'Chicago Fire FC', 'expected': 'HOME', 'type': 'hierarchy'}
        ]
        
        mls_correct = 0
        for i, case in enumerate(mls_test_cases):
            prediction, confidence = mls_hybrid.make_hybrid_mls_prediction(
                {}, 65, case['home'], case['away']
            )
            
            # Determine result
            if 'DRAW' in prediction.upper() or '🤝' in prediction:
                result = 'DRAW'
            elif case['home'].upper() in prediction.upper() or '🏠' in prediction or '🌟' in prediction or '🔥' in prediction or '🏔️' in prediction:
                result = 'HOME'
            elif case['away'].upper() in prediction.upper() or '✈️' in prediction or '⚡' in prediction or '🚀' in prediction:
                result = 'AWAY'
            else:
                result = 'UNKNOWN'
            
            is_correct = result == case['expected']
            if is_correct:
                mls_correct += 1
                icon = '✅'
            else:
                icon = '❌'
            
            print(f'   {icon} {case["away"]} @ {case["home"]}: {prediction} ({confidence:.1f}%)')
            print(f'      Expected: {case["expected"]} | Got: {result} | Type: {case["type"]}')
        
        mls_accuracy = (mls_correct / len(mls_test_cases)) * 100
        print(f'\\n🇺🇸 MLS HYBRID ACCURACY: {mls_accuracy:.1f}% ({mls_correct}/{len(mls_test_cases)})')
        
        print()
        
        # EPL HYBRID TEST (EPL Hierarchy + MLS Culture)
        print('🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥 EPL HYBRID TEST (Hierarchy + Culture):')
        print('----------------------------------------------------------------------')
        
        epl_test_cases = [
            # Big 6 dominance (should maintain strength)
            {'home': 'Burnley', 'away': 'Manchester City', 'expected': 'AWAY', 'type': 'big6_dominance'},
            {'home': 'Sheffield United', 'away': 'Arsenal', 'expected': 'AWAY', 'type': 'big6_dominance'},
            
            # NEW: Cultural moments (MLS-inspired)
            {'home': 'Arsenal', 'away': 'Tottenham Hotspur', 'expected': 'HOME', 'type': 'north_london_derby'},
            {'home': 'Liverpool', 'away': 'Everton', 'expected': 'HOME', 'type': 'merseyside_derby'},
            
            # NEW: Venue atmosphere (MLS-inspired)
            {'home': 'Liverpool', 'away': 'Crystal Palace', 'expected': 'HOME', 'type': 'anfield_atmosphere'},
            {'home': 'Newcastle United', 'away': 'Brentford', 'expected': 'HOME', 'type': 'fortress_atmosphere'},
            
            # Tactical draws (EPL strength + MLS insight)
            {'home': 'Wolverhampton Wanderers', 'away': 'Crystal Palace', 'expected': 'DRAW', 'type': 'tactical_draw'},
            {'home': 'Manchester City', 'away': 'Arsenal', 'expected': 'DRAW', 'type': 'big6_cultural_draw'},
            
            # NEW: Emotional context (MLS-inspired)
            {'home': 'Luton Town', 'away': 'Aston Villa', 'expected': 'HOME', 'type': 'survival_motivation'},
            
            # Class differential (EPL strength)
            {'home': 'Crystal Palace', 'away': 'Brighton & Hove Albion', 'expected': 'AWAY', 'type': 'class_differential'}
        ]
        
        epl_correct = 0
        for i, case in enumerate(epl_test_cases):
            prediction, confidence = epl_hybrid.make_hybrid_epl_prediction(
                {}, 65, case['home'], case['away']
            )
            
            # Determine result
            if 'DRAW' in prediction.upper() or '🤝' in prediction:
                result = 'DRAW'
            elif case['home'].upper() in prediction.upper() or '🏠' in prediction or '🔥' in prediction or '🏟️' in prediction or '🏰' in prediction or '🏆' in prediction or '💙' in prediction or '❤️' in prediction or '🔴' in prediction or '🔵' in prediction or '💪' in prediction:
                result = 'HOME'
            elif case['away'].upper() in prediction.upper() or '✈️' in prediction or '⚡' in prediction or '🚀' in prediction:
                result = 'AWAY'
            else:
                result = 'UNKNOWN'
            
            is_correct = result == case['expected']
            if is_correct:
                epl_correct += 1
                icon = '✅'
            else:
                icon = '❌'
            
            print(f'   {icon} {case["away"]} @ {case["home"]}: {prediction} ({confidence:.1f}%)')
            print(f'      Expected: {case["expected"]} | Got: {result} | Type: {case["type"]}')
        
        epl_accuracy = (epl_correct / len(epl_test_cases)) * 100
        print(f'\\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL HYBRID ACCURACY: {epl_accuracy:.1f}% ({epl_correct}/{len(epl_test_cases)})')
        
        print()
        
        # OVERALL HYBRID RESULTS
        print('🔥💀🔥 HYBRID ALGORITHMS RESULTS:')
        print('======================================================================')
        
        total_correct = mls_correct + epl_correct
        total_games = len(mls_test_cases) + len(epl_test_cases)
        overall_accuracy = (total_correct / total_games) * 100
        
        print(f'🇺🇸 MLS HYBRID: {mls_accuracy:.1f}% accuracy')
        print(f'🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL HYBRID: {epl_accuracy:.1f}% accuracy')
        print(f'🌍 COMBINED HYBRID: {overall_accuracy:.1f}% accuracy ({total_correct}/{total_games})')
        print()
        
        # LEGENDARY STATUS CHECK
        print('🏆 LEGENDARY STATUS VERIFICATION:')
        print('----------------------------------------------------------------------')
        
        # Individual league status
        if mls_accuracy >= 80:
            print(f'🇺🇸 MLS HYBRID: LEGENDARY STATUS ACHIEVED! ✅')
        elif mls_accuracy >= 70:
            print(f'🇺🇸 MLS HYBRID: NEAR-LEGENDARY! High Performance! ⚡')
        else:
            print(f'🇺🇸 MLS HYBRID: Needs improvement ({mls_accuracy:.1f}%)')
        
        if epl_accuracy >= 80:
            print(f'🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL HYBRID: LEGENDARY STATUS ACHIEVED! ✅')
        elif epl_accuracy >= 70:
            print(f'🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL HYBRID: NEAR-LEGENDARY! High Performance! ⚡')
        else:
            print(f'🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL HYBRID: Needs improvement ({epl_accuracy:.1f}%)')
        
        # Overall status
        if overall_accuracy >= 80:
            print(f'🌍 HYBRID SYSTEM: LEGENDARY STATUS ACHIEVED! 🏆✅')
            print('🔥💀🔥 VICTORY PATTERNS SUCCESSFULLY EXPLOITED! 💀🔥💀')
        elif overall_accuracy >= 75:
            print(f'🌍 HYBRID SYSTEM: NEAR-LEGENDARY! TARGET RANGE! 🚀')
            print('🎯 Victory patterns working as predicted!')
        elif overall_accuracy >= 70:
            print(f'🌍 HYBRID SYSTEM: HIGH PERFORMANCE! Good progress! ⚡')
        else:
            print(f'🌍 HYBRID SYSTEM: Needs refinement ({overall_accuracy:.1f}%)')
        
        # COMPARISON WITH ORIGINALS
        print()
        print('📈 IMPROVEMENT OVER ORIGINAL ALGORITHMS:')
        print('----------------------------------------------------------------------')
        print(f'🇺🇸 Original MLS: 85.0% → Hybrid: {mls_accuracy:.1f}% ({mls_accuracy-85.0:+.1f}%)')
        print(f'🏴󠁧󠁢󠁥󠁮󠁧󠁿 Original EPL: 64.2% → Hybrid: {epl_accuracy:.1f}% ({epl_accuracy-64.2:+.1f}%)')
        print(f'🌍 Average Original: 74.6% → Hybrid: {overall_accuracy:.1f}% ({overall_accuracy-74.6:+.1f}%)')
        
        return {
            'mls_accuracy': mls_accuracy,
            'epl_accuracy': epl_accuracy,
            'overall_accuracy': overall_accuracy,
            'legendary_status': overall_accuracy >= 80
        }
        
    except Exception as e:
        print(f'💀 Critical error in hybrid test: {e}')
        import traceback
        traceback.print_exc()
        return {'error': str(e)}

if __name__ == "__main__":
    results = asyncio.run(ultimate_hybrid_test())
    print(f'\\n🎯 FINAL HYBRID SYSTEM ACCURACY: {results.get("overall_accuracy", 0):.1f}%')
    if results.get('legendary_status'):
        print('🏆👑🏆 LEGENDARY STATUS ACHIEVED! VICTORY PATTERNS MASTERED! 👑🏆👑')
    else:
        print('🔥💀🔥 HYBRID REVOLUTION COMPLETE! 💀🔥💀')