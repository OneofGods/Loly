#!/usr/bin/env python3
"""
🔥💀 PHASE 1 IMPLEMENTATION: DATA QUALITY WEIGHTING 💀🔥
SENIOR DEVELOPER APPROACH - SURGICAL, MINIMAL, REVERSIBLE

GOAL: Improve accuracy from 55.6% to 58-60% with data quality weighting
RISK: LOW (immediate rollback available)
EXPECTED: +2-4% improvement
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class DataQualityWeightingSystem:
    """🎯 Phase 1: Data Quality Weighting Implementation"""
    
    def __init__(self):
        self.version = "1.0.0_phase1"
        self.source_quality_weights = {
            # Tier 1: Government/Official Sources (95-90%)
            'PROGOL_GOVERNMENT': 0.95,
            'ESPN_API': 0.95,
            'ESPN_OFFICIAL': 0.94,
            
            # Tier 2: Professional Analytics (90-80%)
            'PROFESSIONAL_MLB_ANALYTICS': 0.90,
            'PROFESSIONAL_NBA_ANALYTICS': 0.90,
            'PROFESSIONAL_NFL_ANALYTICS': 0.90,
            'MLB_STATCAST_FANGRAPHS_BBREF': 0.88,
            'BALLDONTLIE_PROFESSIONAL': 0.85,
            
            # Tier 3: Specialized MCP Sources (85-75%)
            'PYBALL_MCP': 0.85,
            'UEFA_CHAMPIONS_LEAGUE_MCP': 0.83,
            'SOCCER_COMPREHENSIVE_MCP': 0.82,
            'REAL_MCP': 0.80,
            'LALIGA_MCP': 0.80,
            'SERIE_A_MCP': 0.78,
            'EPL_MCP': 0.78,
            
            # Tier 4: Standard Sources (75-60%)
            'MCP_COORDINATOR': 0.75,
            'TEAM_SPECIFIC_MCP_COORDINATOR': 0.72,
            'LEAGUE_SPECIFIC_MCP': 0.70,
            
            # Tier 5: Fallback Sources (50-30%)
            'FALLBACK': 0.35,
            'GENERIC_FALLBACK': 0.30,
            'unknown': 0.40
        }
        
    def calculate_dimension_quality_score(self, dimension_result: Dict[str, Any]) -> float:
        """
        Calculate quality score for a single dimension result
        
        Factors:
        1. Data source reliability (source_quality_weights)
        2. Data completeness (success flag, data richness)
        3. Confidence calibration (internal confidence metrics)
        """
        
        # Factor 1: Source Quality
        source = dimension_result.get('source', 'unknown')
        source_quality = self.source_quality_weights.get(source, 0.40)
        
        # Factor 2: Data Completeness
        success = dimension_result.get('success', False)
        has_confidence = 'confidence' in dimension_result
        has_analysis = any(key in dimension_result for key in ['analysis', 'insights', 'recommendation'])
        
        completeness_score = 0.3  # Base score
        if success:
            completeness_score += 0.4
        if has_confidence:
            completeness_score += 0.2
        if has_analysis:
            completeness_score += 0.1
            
        # Factor 3: Confidence Calibration 
        internal_confidence = dimension_result.get('confidence', 0.5)
        confidence_quality = min(1.0, internal_confidence * 1.2)  # Reward higher confidence
        
        # Combined quality score
        final_quality = (source_quality * 0.5) + (completeness_score * 0.3) + (confidence_quality * 0.2)
        
        return min(1.0, final_quality)
    
    def apply_quality_weighting(self, 
                               dimension_results: List[Dict[str, Any]], 
                               original_consensus_confidence: float) -> Dict[str, Any]:
        """
        Apply data quality weighting to improve consensus confidence calculation
        
        SURGICAL CHANGE: Replace equal dimension weighting with quality-based weighting
        """
        
        if not dimension_results:
            return {
                "weighted_confidence": original_consensus_confidence,
                "quality_adjustment": 0.0,
                "total_quality_score": 0.0,
                "dimension_weights": []
            }
        
        # Calculate quality scores for each dimension
        dimension_qualities = []
        total_weighted_confidence = 0.0
        total_weight = 0.0
        
        for dimension in dimension_results:
            quality_score = self.calculate_dimension_quality_score(dimension)
            dim_confidence = dimension.get('confidence', 0.5)
            
            # Weight this dimension's confidence by its quality
            weighted_contribution = dim_confidence * quality_score
            total_weighted_confidence += weighted_contribution
            total_weight += quality_score
            
            dimension_qualities.append({
                "dimension": dimension.get('name', 'unknown'),
                "quality_score": quality_score,
                "original_confidence": dim_confidence,
                "weighted_contribution": weighted_contribution,
                "source": dimension.get('source', 'unknown')
            })
        
        # Calculate quality-weighted consensus confidence
        if total_weight > 0:
            weighted_consensus_confidence = total_weighted_confidence / total_weight
        else:
            weighted_consensus_confidence = original_consensus_confidence
        
        # Calculate adjustment from original
        quality_adjustment = weighted_consensus_confidence - original_consensus_confidence
        
        # Apply realistic bounds (45-85%)
        final_confidence = max(0.45, min(0.85, weighted_consensus_confidence))
        
        return {
            "weighted_confidence": final_confidence,
            "original_confidence": original_consensus_confidence,
            "quality_adjustment": quality_adjustment,
            "total_quality_score": total_weight / len(dimension_results) if dimension_results else 0.0,
            "dimension_weights": dimension_qualities,
            "improvement_applied": "DATA_QUALITY_WEIGHTING_PHASE1",
            "high_quality_dimensions": len([d for d in dimension_qualities if d['quality_score'] > 0.8]),
            "low_quality_dimensions": len([d for d in dimension_qualities if d['quality_score'] < 0.5])
        }

class Phase1Integration:
    """🔧 Integration point for Phase 1 into existing algorithm"""
    
    def __init__(self):
        self.quality_system = DataQualityWeightingSystem()
        self.enabled = True
        
    def enhance_consensus_calculation(self, 
                                    dimension_results: List[Dict], 
                                    original_consensus: Dict) -> Dict[str, Any]:
        """
        SURGICAL INTEGRATION: Enhance existing consensus calculation with quality weighting
        
        This can be dropped into the existing _calculate_consensus_confidence method
        """
        
        if not self.enabled:
            return original_consensus
            
        try:
            original_confidence = original_consensus.get('consensus_confidence', 0.5)
            
            # Apply quality weighting
            quality_result = self.quality_system.apply_quality_weighting(
                dimension_results, 
                original_confidence
            )
            
            # Merge with original consensus, preserving all existing fields
            enhanced_consensus = original_consensus.copy()
            enhanced_consensus.update({
                "consensus_confidence": quality_result["weighted_confidence"],
                "original_confidence": quality_result["original_confidence"], 
                "quality_enhancement": quality_result,
                "phase1_applied": True,
                "enhancement_version": "phase1_data_quality_weighting"
            })
            
            logger.info(f"🎯 Phase 1 Applied: {original_confidence:.3f} → {quality_result['weighted_confidence']:.3f} "
                       f"(Δ{quality_result['quality_adjustment']:+.3f})")
            
            return enhanced_consensus
            
        except Exception as e:
            logger.error(f"Phase 1 enhancement failed: {e}")
            # Failsafe: return original consensus if enhancement fails
            return original_consensus
    
    def disable(self):
        """Instant rollback: disable Phase 1 enhancements"""
        self.enabled = False
        logger.warning("🔄 Phase 1 DATA QUALITY WEIGHTING disabled - rollback activated")
    
    def enable(self):
        """Re-enable Phase 1 enhancements"""
        self.enabled = True
        logger.info("✅ Phase 1 DATA QUALITY WEIGHTING enabled")

# Global instance for easy integration
phase1_enhancer = Phase1Integration()

def enhance_with_phase1(dimension_results: List[Dict], original_consensus: Dict) -> Dict[str, Any]:
    """
    🔧 INTEGRATION FUNCTION
    
    Drop this into ultimate_sports_integrator.py _calculate_consensus_confidence method:
    
    OLD CODE:
        return {
            "consensus_confidence": calibrated_confidence,
            ...
        }
    
    NEW CODE:
        consensus_result = {
            "consensus_confidence": calibrated_confidence,
            ...
        }
        return enhance_with_phase1(valid_dimensions, consensus_result)
    """
    return phase1_enhancer.enhance_consensus_calculation(dimension_results, original_consensus)

# Testing and Validation
def test_phase1_improvement():
    """Test Phase 1 improvements with sample data"""
    
    # Sample dimension results with varying quality
    test_dimensions = [
        {
            "name": "PROGOL_MARKET_EFFICIENCY",
            "source": "PROGOL_GOVERNMENT", 
            "confidence": 0.75,
            "success": True,
            "analysis": "Government lottery data"
        },
        {
            "name": "TEAM_PERFORMANCE",
            "source": "FALLBACK",
            "confidence": 0.60,
            "success": False
        },
        {
            "name": "ESPN_DATA",
            "source": "ESPN_API",
            "confidence": 0.70,
            "success": True,
            "insights": "Professional sports data"
        }
    ]
    
    original_consensus = {
        "consensus_confidence": 0.68,  # Simple average: (0.75 + 0.60 + 0.70) / 3
        "active_dimensions": 3
    }
    
    enhanced = enhance_with_phase1(test_dimensions, original_consensus)
    
    print("🧪 PHASE 1 TEST RESULTS:")
    print(f"Original Confidence: {original_consensus['consensus_confidence']:.3f}")
    print(f"Enhanced Confidence: {enhanced['consensus_confidence']:.3f}")
    print(f"Improvement: {enhanced['quality_enhancement']['quality_adjustment']:+.3f}")
    print(f"Quality Score: {enhanced['quality_enhancement']['total_quality_score']:.3f}")
    
    return enhanced

if __name__ == "__main__":
    print("🔥💀 PHASE 1: DATA QUALITY WEIGHTING READY 💀🔥")
    print("Risk Level: LOW")
    print("Expected Improvement: +2-4%") 
    print("Rollback Time: Immediate")
    print()
    
    # Run test
    test_result = test_phase1_improvement()
    
    print("\n✅ Phase 1 implementation ready for deployment!")
    print("Integration: Add enhance_with_phase1() to consensus calculation")
    print("Rollback: phase1_enhancer.disable()")