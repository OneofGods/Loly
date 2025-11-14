#!/usr/bin/env python3
"""
🔥💀🔥 MLS HYBRID PREDICTION ENGINE - FINAL SOLUTION 💀🔥💀

INTELLIGENT HYBRID APPROACH:
- Use cultural mastery for clear winners (Messi, El Trafico, etc.)
- Use pattern discovery for unclear/close matches
- Balanced approach to catch draws without over-predicting

Created: November 1, 2025
Mission: ACHIEVE OPTIMAL MLS ACCURACY WITH SMART DRAW DETECTION
"""

import logging
from typing import Dict, Any, Tuple

logger = logging.getLogger(__name__)

class MLSHybridPredictionEngine:
    """
    🔥💀🔥 MLS HYBRID PREDICTION ENGINE
    
    Smart combination of cultural mastery and pattern discovery
    """
    
    def __init__(self):
        """Initialize the hybrid engine"""
        logger.info("🔥💀🔥 MLS Hybrid Prediction Engine initialized! 💀🔥💀")
    
    def hybrid_mls_prediction(self, 
                            cultural_prediction: str,
                            cultural_confidence: float,
                            pattern_prediction: Dict[str, Any],
                            home_team: str,
                            away_team: str) -> Tuple[str, float, Dict[str, Any]]:
        """
        🎯 HYBRID PREDICTION: Smart combination of cultural + pattern approaches
        """
        try:
            draw_probability = pattern_prediction.get('draw_probability', 0.25)
            pattern_pred = pattern_prediction.get('prediction', f'🏠 {home_team}')
            
            # DECISION MATRIX
            
            # 1. STRONG CULTURAL FACTORS (use cultural prediction)
            strong_cultural_indicators = [
                'MESSI', 'EL TRAFICO', 'CASCADIA', 'TEXAS DERBY'
            ]
            
            has_strong_cultural = any(indicator in cultural_prediction.upper() 
                                    for indicator in strong_cultural_indicators)
            
            if has_strong_cultural and cultural_confidence > 70:
                return cultural_prediction, cultural_confidence, {
                    'decision': 'strong_cultural',
                    'reason': 'Strong cultural factors override draw risk'
                }
            
            # 2. HIGH DRAW PROBABILITY + WEAK CULTURAL (use draw prediction)
            if (draw_probability > 0.30 and 
                cultural_confidence < 65 and
                'TRAVEL ADVANTAGE' in cultural_prediction):
                
                return pattern_pred, pattern_prediction.get('confidence', 50), {
                    'decision': 'high_draw_probability',
                    'reason': f'High draw probability ({draw_probability:.1%}) + weak cultural factors'
                }
            
            # 3. MODERATE DRAW RISK + CLOSE CULTURAL SCORES (use draw prediction)  
            pattern_home_score = pattern_prediction.get('home_score', 50)
            pattern_away_score = pattern_prediction.get('away_score', 50)
            score_difference = abs(pattern_home_score - pattern_away_score)
            
            if (draw_probability > 0.27 and 
                score_difference < 6 and
                55 < cultural_confidence < 75):
                
                return pattern_pred, pattern_prediction.get('confidence', 50), {
                    'decision': 'moderate_draw_risk',
                    'reason': f'Moderate draw risk + close scores (diff: {score_difference:.1f})'
                }
            
            # 4. SPECIAL CASE: Cross-country travel + parity matchup
            is_cross_country = any(east in home_team.upper() for east in 
                                 ['MIAMI', 'ATLANTA', 'ORLANDO', 'NEW YORK', 'PHILADELPHIA']) and \
                             any(west in away_team.upper() for west in 
                                 ['LAFC', 'GALAXY', 'SEATTLE', 'PORTLAND', 'SAN JOSE'])
            
            if (is_cross_country and 
                draw_probability > 0.25 and
                'TRAVEL' in cultural_prediction and
                score_difference < 8):
                
                return "🛫 TRAVEL FATIGUE DRAW", 45 + (draw_probability * 30), {
                    'decision': 'cross_country_fatigue',
                    'reason': 'Cross-country travel increases draw likelihood'
                }
            
            # 5. DEFAULT: Use cultural prediction
            return cultural_prediction, cultural_confidence, {
                'decision': 'default_cultural',
                'reason': 'No strong draw indicators, using cultural mastery'
            }
            
        except Exception as e:
            logger.error(f"💀 Hybrid prediction error: {e}")
            return cultural_prediction, cultural_confidence, {'error': str(e)}

# TESTING FUNCTION
async def test_hybrid_engine():
    """Test the hybrid prediction engine"""
    print("🔥💀🔥 TESTING HYBRID MLS PREDICTION ENGINE 💀🔥💀")
    print("=" * 70)
    
    engine = MLSHybridPredictionEngine()
    
    test_cases = [
        {
            'home': 'Minnesota United FC',
            'away': 'Seattle Sounders FC',
            'cultural_pred': '🏠 TRAVEL ADVANTAGE: Minnesota United FC',
            'cultural_conf': 70.6,
            'pattern_pred': {'prediction': '🎲 HIGH DRAW PROBABILITY', 'confidence': 65, 'draw_probability': 0.34, 'home_score': 52, 'away_score': 48},
            'actual': 'DRAW (0-0)'
        },
        {
            'home': 'Inter Miami CF', 
            'away': 'Nashville SC',
            'cultural_pred': '🌟 MESSI MAGIC',
            'cultural_conf': 82.3,
            'pattern_pred': {'prediction': '🎲 DRAW LIKELY', 'confidence': 55, 'draw_probability': 0.28, 'home_score': 55, 'away_score': 45},
            'actual': 'Inter Miami WIN (3-1)'
        },
        {
            'home': 'Philadelphia Union',
            'away': 'Chicago Fire FC', 
            'cultural_pred': '🏠 TRAVEL ADVANTAGE: Philadelphia Union',
            'cultural_conf': 70.1,
            'pattern_pred': {'prediction': '🎲 HIGH DRAW PROBABILITY', 'confidence': 63, 'draw_probability': 0.32, 'home_score': 51, 'away_score': 49},
            'actual': 'DRAW (2-2)'
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"🏟️ TEST {i}: {case['away']} @ {case['home']}")
        
        hybrid_pred, hybrid_conf, decision_info = engine.hybrid_mls_prediction(
            case['cultural_pred'], case['cultural_conf'], case['pattern_pred'],
            case['home'], case['away']
        )
        
        print(f"   🎭 Cultural: {case['cultural_pred']} ({case['cultural_conf']:.1f}%)")
        print(f"   🎲 Pattern: {case['pattern_pred']['prediction']} ({case['pattern_pred']['confidence']:.1f}%)")
        print(f"   🎯 HYBRID: {hybrid_pred} ({hybrid_conf:.1f}%)")
        print(f"   🧠 Decision: {decision_info['decision']} - {decision_info['reason']}")
        print(f"   ✅ Actual: {case['actual']}")
        
        # Check if correct
        is_draw_actual = 'DRAW' in case['actual']
        is_draw_predicted = 'DRAW' in hybrid_pred.upper() or 'FATIGUE' in hybrid_pred
        is_win_predicted = 'MESSI' in hybrid_pred or case['home'].upper() in hybrid_pred.upper()
        
        if is_draw_actual and is_draw_predicted:
            result = "✅ CORRECT (Draw detected)"
        elif not is_draw_actual and is_win_predicted:
            result = "✅ CORRECT (Win detected)"
        else:
            result = "❌ INCORRECT"
            
        print(f"   📊 {result}")
        print()
    
    print("✅ HYBRID ENGINE READY FOR INTEGRATION!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_hybrid_engine())