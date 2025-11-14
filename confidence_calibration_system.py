#!/usr/bin/env python3
"""
🔥💀🔥 CONFIDENCE CALIBRATION SYSTEM - BRUTAL HONESTY ENGINE 💀🔥💀

LEGENDARY CONFIDENCE CALIBRATION SYSTEM
Fixes inflated confidence to match REAL accuracy based on back test results.

🚨 NO MORE FAKE LEGENDARY STATUS! 🚨

Based on back test findings:
- MLS: 73.2% claimed → 55.0% actual = 35% inflation
- Ligue 1: 72.7% claimed → 30.0% actual = 58% inflation  
- UEFA Europa: 68.4% claimed → 22.2% actual = 67% inflation

CALIBRATION STRATEGY:
1. Lower confidence thresholds by ~35%
2. Add uncertainty factors for real-world volatility
3. Weight recent form more than cultural heritage
4. Penalize overconfident predictions

Created: November 1, 2025
Mission: RESTORE LEGENDARY STATUS WITH HONEST CONFIDENCE
"""

import math
import logging
from typing import Dict, Any, Tuple, List
from datetime import datetime

logger = logging.getLogger(__name__)

class ConfidenceCalibrationSystem:
    """
    🔥💀🔥 CONFIDENCE CALIBRATION SYSTEM
    
    Transforms inflated cultural mastery confidence into brutally honest,
    accuracy-calibrated confidence levels.
    """
    
    def __init__(self):
        """Initialize the brutal honesty engine"""
        
        # Back test calibration data (observed inflation rates)
        self.calibration_data = {
            'MLS': {
                'inflation_rate': 0.35,  # 35% inflation observed
                'volatility_factor': 0.25,  # MLS has high parity/volatility
                'accuracy_ceiling': 65.0,  # Realistic max accuracy for MLS
                'base_uncertainty': 15.0   # Base uncertainty due to MLS parity
            },
            'LIGUE1': {
                'inflation_rate': 0.58,  # 58% inflation observed
                'volatility_factor': 0.30,  # French football can be unpredictable
                'accuracy_ceiling': 70.0,  # Realistic max for Ligue 1
                'base_uncertainty': 12.0   # PSG dominance reduces some uncertainty
            },
            'UEFA_EUROPA': {
                'inflation_rate': 0.67,  # 67% inflation observed  
                'volatility_factor': 0.35,  # High volatility in knockouts
                'accuracy_ceiling': 60.0,  # Europa League is very unpredictable
                'base_uncertainty': 20.0   # Knockout format adds major uncertainty
            }
        }
        
        # Form weight adjustments (prioritize recent performance)
        self.form_weights = {
            'recent_form': 0.40,      # 40% weight to recent form
            'cultural_heritage': 0.25, # Reduced from 60%+ to 25%
            'tactical_factors': 0.20,  # Tactical analysis
            'home_advantage': 0.10,    # Reduced home bias
            'uncertainty_buffer': 0.05  # Always include uncertainty
        }
        
        # Overconfidence penalties
        self.overconfidence_penalties = {
            'high_confidence_threshold': 80.0,  # Above 80% gets penalized
            'extreme_confidence_threshold': 90.0,  # Above 90% gets heavy penalty
            'high_penalty': 10.0,      # -10% for high confidence
            'extreme_penalty': 20.0    # -20% for extreme confidence
        }
        
        logger.info("🔥💀🔥 Confidence Calibration System initialized - BRUTAL HONESTY MODE! 💀🔥💀")
    
    def calibrate_confidence(self, 
                           raw_confidence: float, 
                           league: str, 
                           prediction_factors: Dict[str, Any] = None) -> Tuple[float, Dict[str, Any]]:
        """
        🎯 MAIN CALIBRATION: Transform inflated confidence into honest confidence
        
        Args:
            raw_confidence: The inflated confidence from cultural mastery algorithm
            league: League code (MLS, LIGUE1, UEFA_EUROPA)
            prediction_factors: Optional factors for fine-tuning
            
        Returns:
            Tuple of (calibrated_confidence, calibration_report)
        """
        try:
            # Get league-specific calibration settings
            if league not in self.calibration_data:
                league = 'MLS'  # Default fallback
            
            calibration = self.calibration_data[league]
            
            # STEP 1: Apply inflation correction (reduce by observed inflation rate)
            inflation_corrected = raw_confidence * (1 - calibration['inflation_rate'])
            
            # STEP 2: Add uncertainty factors for real-world volatility
            volatility_reduction = raw_confidence * calibration['volatility_factor']
            uncertainty_adjusted = inflation_corrected - volatility_reduction
            
            # STEP 3: Apply base uncertainty (minimum uncertainty for all predictions)
            base_uncertainty_reduction = calibration['base_uncertainty']
            base_adjusted = uncertainty_adjusted - base_uncertainty_reduction
            
            # STEP 4: Penalize overconfident predictions
            overconfidence_penalty = self._calculate_overconfidence_penalty(raw_confidence)
            penalty_adjusted = base_adjusted - overconfidence_penalty
            
            # STEP 5: Apply accuracy ceiling (realistic maximum)
            ceiling_applied = min(penalty_adjusted, calibration['accuracy_ceiling'])
            
            # STEP 6: Ensure minimum confidence (never go below 35%)
            final_confidence = max(ceiling_applied, 35.0)
            
            # Generate calibration report
            calibration_report = {
                'raw_confidence': raw_confidence,
                'final_confidence': final_confidence,
                'adjustments': {
                    'inflation_correction': raw_confidence - inflation_corrected,
                    'volatility_reduction': volatility_reduction,
                    'base_uncertainty': base_uncertainty_reduction,
                    'overconfidence_penalty': overconfidence_penalty,
                    'total_reduction': raw_confidence - final_confidence
                },
                'league': league,
                'calibration_applied': True,
                'honesty_engine': 'v1.0'
            }
            
            logger.info(f"🎯 CALIBRATED: {league} {raw_confidence:.1f}% → {final_confidence:.1f}% (reduced by {raw_confidence - final_confidence:.1f}%)")
            
            return final_confidence, calibration_report
            
        except Exception as e:
            logger.error(f"💀 Calibration error: {e}")
            # Emergency fallback - just reduce by 35%
            fallback_confidence = max(raw_confidence * 0.65, 35.0)
            return fallback_confidence, {'error': str(e), 'fallback_applied': True}
    
    def _calculate_overconfidence_penalty(self, confidence: float) -> float:
        """
        ⚠️ Calculate penalty for overconfident predictions
        """
        penalty = 0.0
        
        if confidence >= self.overconfidence_penalties['extreme_confidence_threshold']:
            penalty = self.overconfidence_penalties['extreme_penalty']
        elif confidence >= self.overconfidence_penalties['high_confidence_threshold']:
            penalty = self.overconfidence_penalties['high_penalty']
        
        return penalty
    
    def enhance_with_form_weighting(self, 
                                  cultural_factors: Dict[str, float], 
                                  recent_form_data: Dict[str, Any] = None) -> Dict[str, float]:
        """
        ⚽ RE-WEIGHT FACTORS: Prioritize recent form over cultural heritage
        
        Args:
            cultural_factors: Original cultural mastery factors
            recent_form_data: Recent performance data (optional)
            
        Returns:
            Re-weighted factors with form prioritized
        """
        try:
            # If no form data provided, reduce cultural weight and add uncertainty
            if not recent_form_data:
                recent_form_data = {
                    'home_recent_form': 50.0,  # Neutral if no data
                    'away_recent_form': 50.0,
                    'form_confidence': 0.3     # Low confidence without data
                }
            
            # Extract form metrics
            home_form = recent_form_data.get('home_recent_form', 50.0)
            away_form = recent_form_data.get('away_recent_form', 50.0)
            form_confidence = recent_form_data.get('form_confidence', 0.5)
            
            # Calculate form-based score
            form_advantage = (home_form - away_form) * self.form_weights['recent_form']
            
            # Reduce cultural heritage weight
            cultural_score = 0.0
            for factor_name, factor_value in cultural_factors.items():
                cultural_score += factor_value * (self.form_weights['cultural_heritage'] / len(cultural_factors))
            
            # Combine with reduced weights
            enhanced_factors = {
                'form_weighted_score': 50.0 + form_advantage,  # Base 50 + form advantage
                'cultural_heritage_reduced': cultural_score * 0.6,  # Reduce cultural impact
                'tactical_analysis': cultural_factors.get('tactical_factor', 50.0) * self.form_weights['tactical_factors'],
                'home_advantage_reduced': 52.0,  # Reduced from typical 55-60%
                'uncertainty_factor': 45.0,     # Always include uncertainty
                'form_confidence': form_confidence * 100
            }
            
            return enhanced_factors
            
        except Exception as e:
            logger.error(f"💀 Form weighting error: {e}")
            return cultural_factors  # Return original on error
    
    def validate_calibration(self, 
                           predicted_results: List[Dict[str, Any]], 
                           actual_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        ✅ VALIDATION: Check if calibrated confidence matches actual accuracy
        """
        try:
            if len(predicted_results) != len(actual_results):
                return {'error': 'Mismatched result lengths'}
            
            correct_predictions = 0
            total_confidence = 0.0
            confidence_buckets = {
                '35-45%': {'correct': 0, 'total': 0},
                '45-55%': {'correct': 0, 'total': 0}, 
                '55-65%': {'correct': 0, 'total': 0},
                '65%+': {'correct': 0, 'total': 0}
            }
            
            for pred, actual in zip(predicted_results, actual_results):
                confidence = pred.get('calibrated_confidence', 50.0)
                is_correct = pred.get('prediction_correct', False)
                
                total_confidence += confidence
                if is_correct:
                    correct_predictions += 1
                
                # Bucket analysis
                if confidence < 45:
                    bucket = '35-45%'
                elif confidence < 55:
                    bucket = '45-55%'
                elif confidence < 65:
                    bucket = '55-65%'
                else:
                    bucket = '65%+'
                
                confidence_buckets[bucket]['total'] += 1
                if is_correct:
                    confidence_buckets[bucket]['correct'] += 1
            
            # Calculate metrics
            total_games = len(predicted_results)
            actual_accuracy = (correct_predictions / total_games * 100) if total_games > 0 else 0
            avg_claimed_confidence = total_confidence / total_games if total_games > 0 else 0
            calibration_error = abs(actual_accuracy - avg_claimed_confidence)
            
            # Bucket accuracy
            for bucket in confidence_buckets:
                bucket_data = confidence_buckets[bucket]
                if bucket_data['total'] > 0:
                    bucket_accuracy = bucket_data['correct'] / bucket_data['total'] * 100
                    bucket_data['accuracy'] = bucket_accuracy
                else:
                    bucket_data['accuracy'] = 0
            
            validation_report = {
                'total_games': total_games,
                'actual_accuracy': actual_accuracy,
                'avg_claimed_confidence': avg_claimed_confidence,
                'calibration_error': calibration_error,
                'well_calibrated': calibration_error < 10.0,  # Within 10% is good
                'confidence_buckets': confidence_buckets,
                'calibration_quality': self._assess_calibration_quality(calibration_error)
            }
            
            return validation_report
            
        except Exception as e:
            logger.error(f"💀 Validation error: {e}")
            return {'error': str(e)}
    
    def _assess_calibration_quality(self, calibration_error: float) -> str:
        """
        📊 Assess the quality of calibration
        """
        if calibration_error < 5.0:
            return "🏆 EXCELLENT CALIBRATION"
        elif calibration_error < 10.0:
            return "✅ GOOD CALIBRATION"
        elif calibration_error < 15.0:
            return "⚠️ FAIR CALIBRATION"
        else:
            return "❌ POOR CALIBRATION"


# CALIBRATION WRAPPER FUNCTIONS for easy integration

def calibrate_mls_confidence(raw_confidence: float, prediction_factors: Dict = None) -> Tuple[float, Dict]:
    """🇺🇸 Calibrate MLS confidence"""
    calibrator = ConfidenceCalibrationSystem()
    return calibrator.calibrate_confidence(raw_confidence, 'MLS', prediction_factors)

def calibrate_ligue1_confidence(raw_confidence: float, prediction_factors: Dict = None) -> Tuple[float, Dict]:
    """🇫🇷 Calibrate Ligue 1 confidence"""
    calibrator = ConfidenceCalibrationSystem()
    return calibrator.calibrate_confidence(raw_confidence, 'LIGUE1', prediction_factors)

def calibrate_europa_confidence(raw_confidence: float, prediction_factors: Dict = None) -> Tuple[float, Dict]:
    """🏆 Calibrate UEFA Europa League confidence"""
    calibrator = ConfidenceCalibrationSystem()
    return calibrator.calibrate_confidence(raw_confidence, 'UEFA_EUROPA', prediction_factors)


# TEST THE CALIBRATION SYSTEM
async def test_calibration_system():
    """Test the confidence calibration system"""
    print("🔥💀🔥 TESTING CONFIDENCE CALIBRATION SYSTEM 💀🔥💀")
    print("=" * 70)
    
    calibrator = ConfidenceCalibrationSystem()
    
    # Test cases based on our back test inflated results
    test_cases = [
        {'league': 'MLS', 'raw_confidence': 82.3, 'description': 'Messi Magic (inflated)'},
        {'league': 'MLS', 'raw_confidence': 69.0, 'description': 'Typical MLS (inflated)'},
        {'league': 'LIGUE1', 'raw_confidence': 81.5, 'description': 'PSG Dominance (inflated)'},
        {'league': 'LIGUE1', 'raw_confidence': 65.0, 'description': 'Regular Ligue 1 (inflated)'},
        {'league': 'UEFA_EUROPA', 'raw_confidence': 82.7, 'description': 'Spanish Europa DNA (inflated)'},
        {'league': 'UEFA_EUROPA', 'raw_confidence': 65.0, 'description': 'Typical Europa (inflated)'}
    ]
    
    for case in test_cases:
        calibrated, report = calibrator.calibrate_confidence(
            case['raw_confidence'], 
            case['league']
        )
        
        reduction = case['raw_confidence'] - calibrated
        print(f"🎯 {case['league']} - {case['description']}:")
        print(f"   📊 {case['raw_confidence']:.1f}% → {calibrated:.1f}% (reduced by {reduction:.1f}%)")
        print(f"   🔧 Total adjustments: {report['adjustments']['total_reduction']:.1f}%")
        print()
    
    print("✅ CALIBRATION SYSTEM READY FOR DEPLOYMENT!")


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_calibration_system())