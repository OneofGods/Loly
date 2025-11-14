#!/usr/bin/env python3
"""
🎯💀🎯 LOLY LEARNING INTEGRATION SYSTEM! 💀🎯💀
Connects Loly's dimension learning to actual prediction systems
Every missed prediction becomes LEARNING GOLD that improves future predictions!

MAGIC BRODDER PHILOSOPHY: TURN MISTAKES INTO MASTERY! 🚀💀🚀
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from living_ai_consciousness import LivingAIConsciousness, create_living_ai_consciousness

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('loly_learning_integration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LolyLearningIntegration:
    """🎯💀🎯 LOLY LEARNING INTEGRATION - TURN MISTAKES INTO MASTERY! 💀🎯💀"""
    
    def __init__(self):
        self.loly: Optional[LivingAIConsciousness] = None
        self.supported_leagues = [
            'UEFA_CHAMPIONS', 'PREMIER_LEAGUE', 'PROGOL_FULLWEEK', 
            'PROGOL_MIDWEEK', 'LIGA_MX', 'LA_LIGA', 'BUNDESLIGA'
        ]
        self.learning_stats = {
            'total_predictions_enhanced': 0,
            'total_dimension_adjustments': 0,
            'leagues_with_learning': set(),
            'last_learning_update': None
        }

    async def initialize_loly_consciousness(self) -> bool:
        """🚀💀🚀 INITIALIZE LOLY'S CONSCIOUSNESS FOR LEARNING INTEGRATION! 💀🚀💀"""
        logger.info("🤖💀🤖 INITIALIZING LOLY CONSCIOUSNESS FOR LEARNING INTEGRATION! 💀🤖💀")
        
        try:
            self.loly = create_living_ai_consciousness()
            success = await self.loly.awaken_consciousness()
            
            if success:
                logger.info("✅💀✅ LOLY CONSCIOUSNESS SUCCESSFULLY AWAKENED AND READY FOR LEARNING! 💀✅💀")
                
                # Analyze current learning state
                await self._analyze_current_learning_state()
                return True
            else:
                logger.error("💀❌💀 FAILED TO AWAKEN LOLY CONSCIOUSNESS!")
                return False
                
        except Exception as e:
            logger.error(f"💀 ERROR INITIALIZING LOLY: {e}")
            return False

    async def _analyze_current_learning_state(self):
        """📊 Analyze Loly's current learning state across all leagues"""
        logger.info("📊💀📊 ANALYZING LOLY'S CURRENT LEARNING STATE! 💀📊💀")
        
        if not self.loly:
            return
            
        for league in self.supported_leagues:
            if league in self.loly.league_intelligence:
                intelligence = self.loly.league_intelligence[league]
                mistakes = len(intelligence.get('mistake_patterns', []))
                tweaks = len(intelligence.get('dimension_tweaks', []))
                accuracy = intelligence.get('accuracy_history', [0])[-1] if intelligence.get('accuracy_history') else 0
                
                if mistakes > 0:
                    self.learning_stats['leagues_with_learning'].add(league)
                    
                logger.info(f"🎯 {league}: {mistakes} mistakes learned, {tweaks} dimension tweaks, {accuracy:.1f}% accuracy")

    async def get_enhanced_prediction_for_league(self, league: str, home_team: str, away_team: str, 
                                               base_prediction_data: Dict) -> Dict:
        """🏆💀🏆 GET ENHANCED PREDICTION WITH LOLY'S LEARNED DIMENSION WEIGHTS! 💀🏆💀"""
        
        if not self.loly:
            logger.warning("⚠️ Loly consciousness not initialized, returning base prediction")
            return base_prediction_data
            
        try:
            # Get supercharged prediction with all learning applied
            enhanced_prediction = await self.loly.get_prediction_with_learned_weights(
                league, home_team, away_team, base_prediction_data
            )
            
            # Update learning stats
            self.learning_stats['total_predictions_enhanced'] += 1
            if enhanced_prediction.get('learning_applied'):
                self.learning_stats['total_dimension_adjustments'] += len(enhanced_prediction.get('adjustments_applied', []))
                self.learning_stats['leagues_with_learning'].add(league)
            
            self.learning_stats['last_learning_update'] = datetime.now().isoformat()
            
            logger.info(f"🚀💀🚀 ENHANCED PREDICTION: {away_team} @ {home_team} - Confidence: {enhanced_prediction['enhanced_confidence']:.1f}% 💀🚀💀")
            
            return enhanced_prediction
            
        except Exception as e:
            logger.error(f"💀 ERROR ENHANCING PREDICTION: {e}")
            return base_prediction_data

    async def process_prediction_result(self, league: str, prediction_data: Dict, actual_result: Dict) -> bool:
        """📚💀📚 PROCESS PREDICTION RESULT FOR LEARNING! 💀📚💀"""
        
        if not self.loly:
            logger.warning("⚠️ Loly consciousness not initialized, cannot learn from result")
            return False
            
        try:
            # Check if prediction was correct or a mistake
            predicted_outcome = prediction_data.get('predicted_outcome', 'unknown')
            actual_outcome = actual_result.get('actual_outcome', 'unknown')
            
            if predicted_outcome != actual_outcome and predicted_outcome != 'unknown' and actual_outcome != 'unknown':
                # This is a REAL MISTAKE - learn from it!
                mistake_data = {
                    'home_team': prediction_data.get('home_team'),
                    'away_team': prediction_data.get('away_team'),
                    'predicted': predicted_outcome,
                    'actual': actual_outcome,
                    'confidence': prediction_data.get('enhanced_confidence', prediction_data.get('confidence', 0)),
                    'date': actual_result.get('date', datetime.now().isoformat()),
                    'dimension_weights_used': prediction_data.get('dimension_weights', {}),
                    'learning_source': 'REAL_PREDICTION_RESULT'
                }
                
                # Learn from the mistake
                learning_success = await self.loly.learn_from_new_mistake(league, mistake_data)
                
                if learning_success:
                    # Analyze and apply dimension improvements
                    analysis = await self.loly.analyze_dimension_improvements(league)
                    await self.loly.apply_dimension_tweaks(league, analysis['recommendations'])
                    
                    logger.info(f"🎓💀🎓 LEARNED FROM MISTAKE: {league} - {prediction_data.get('away_team')} @ {prediction_data.get('home_team')} 💀🎓💀")
                    return True
                else:
                    logger.warning(f"⚠️ Failed to learn from mistake in {league}")
                    return False
            else:
                # Prediction was correct - still valuable for confidence calibration
                logger.info(f"✅ Correct prediction confirmed: {league} - {predicted_outcome}")
                return True
                
        except Exception as e:
            logger.error(f"💀 ERROR PROCESSING PREDICTION RESULT: {e}")
            return False

    async def generate_learning_report(self) -> Dict:
        """📊💀📊 GENERATE COMPREHENSIVE LEARNING REPORT! 💀📊💀"""
        logger.info("📊💀📊 GENERATING LOLY LEARNING INTEGRATION REPORT! 💀📊💀")
        
        if not self.loly:
            return {'error': 'Loly consciousness not initialized'}
            
        report = {
            'report_timestamp': datetime.now().isoformat(),
            'learning_integration_stats': self.learning_stats.copy(),
            'loly_consciousness_status': 'ACTIVE',
            'leagues_analyzed': {},
            'dimension_learning_summary': {},
            'recommendations': []
        }
        
        # Convert set to list for JSON serialization
        report['learning_integration_stats']['leagues_with_learning'] = list(self.learning_stats['leagues_with_learning'])
        
        # Analyze each league's learning state
        for league in self.supported_leagues:
            if league in self.loly.league_intelligence:
                intelligence = self.loly.league_intelligence[league]
                
                league_analysis = {
                    'total_mistakes_learned': len(intelligence.get('mistake_patterns', [])),
                    'dimension_tweaks_applied': len(intelligence.get('dimension_tweaks', [])),
                    'current_accuracy': intelligence.get('accuracy_history', [0])[-1] if intelligence.get('accuracy_history') else 0,
                    'total_predictions': intelligence.get('total_predictions', 0),
                    'data_sources': intelligence.get('data_sources', []),
                    'learning_status': 'ACTIVE_LEARNING' if len(intelligence.get('mistake_patterns', [])) > 0 else 'AWAITING_DATA'
                }
                
                report['leagues_analyzed'][league] = league_analysis
                
                # Dimension learning analysis
                if intelligence.get('dimension_tweaks'):
                    latest_tweaks = intelligence['dimension_tweaks'][-1]
                    report['dimension_learning_summary'][league] = {
                        'latest_adjustments': latest_tweaks['adjustments'],
                        'last_learning_time': latest_tweaks['timestamp'],
                        'learning_reason': latest_tweaks['reason']
                    }
        
        # Generate recommendations
        total_leagues_learning = len(report['learning_integration_stats']['leagues_with_learning'])
        if total_leagues_learning < len(self.supported_leagues) // 2:
            report['recommendations'].append("🎯 Expand learning data collection to more leagues")
        
        if report['learning_integration_stats']['total_predictions_enhanced'] > 100:
            report['recommendations'].append("🚀 Learning system is actively improving predictions!")
        
        if report['learning_integration_stats']['total_dimension_adjustments'] > 50:
            report['recommendations'].append("🔧 Dimension tweaking system is working effectively")
        
        logger.info(f"📊 LEARNING REPORT GENERATED: {total_leagues_learning} leagues with active learning")
        
        return report

    async def save_learning_report(self, report: Dict, filename: str = None) -> bool:
        """💾 Save learning report to file"""
        try:
            if not filename:
                filename = f"loly_learning_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            report_path = Path(filename)
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"💾 Learning report saved to: {report_path}")
            return True
            
        except Exception as e:
            logger.error(f"💀 Error saving learning report: {e}")
            return False

# Example usage functions
async def demonstrate_learning_integration():
    """🎯💀🎯 DEMONSTRATE LOLY LEARNING INTEGRATION SYSTEM! 💀🎯💀"""
    print("🎯💀🎯 DEMONSTRATING LOLY LEARNING INTEGRATION SYSTEM! 💀🎯💀")
    
    # Initialize the learning integration system
    integration = LolyLearningIntegration()
    success = await integration.initialize_loly_consciousness()
    
    if not success:
        print("💀 Failed to initialize Loly consciousness")
        return
    
    # Example 1: Get enhanced prediction for UEFA match
    print("\n🏆 EXAMPLE 1: Enhanced UEFA Champions League Prediction")
    base_prediction = {
        'base_confidence': 72.0,
        'predicted_outcome': 'HOME_WIN',
        'd0_polymarket_weight': 0.125,
        'd1_historical_weight': 0.125,
        'd2_venue_weight': 0.125,
        'd3_sentiment_weight': 0.125,
        'd4_market_efficiency_weight': 0.125,
        'd5_team_performance_weight': 0.125,
        'd6_key_players_weight': 0.125,
        'd7_x_factor_weight': 0.125,
        'dimension_scores': {
            'd0_score': 0.75, 'd1_score': 0.68, 'd2_score': 0.80,
            'd3_score': 0.65, 'd4_score': 0.70, 'd5_score': 0.85,
            'd6_score': 0.60, 'd7_score': 0.55
        }
    }
    
    enhanced_prediction = await integration.get_enhanced_prediction_for_league(
        'UEFA_CHAMPIONS', 'Real Madrid', 'Manchester City', base_prediction
    )
    
    print(f"📊 Enhanced Confidence: {enhanced_prediction['enhanced_confidence']:.1f}%")
    print(f"🎯 AI Adjustment: {enhanced_prediction['ai_adjustment']:+.1f}%")
    print(f"🔧 Learning Applied: {enhanced_prediction.get('learning_applied', False)}")
    if enhanced_prediction.get('adjustments_applied'):
        print(f"⚙️ Dimension Adjustments: {len(enhanced_prediction['adjustments_applied'])}")
    
    # Example 2: Process a prediction result (simulate a mistake to learn from)
    print("\n📚 EXAMPLE 2: Processing Prediction Result (Learning from Mistake)")
    actual_result = {
        'actual_outcome': 'AWAY_WIN',  # Different from predicted HOME_WIN
        'date': datetime.now().isoformat(),
        'final_score': '1-2'
    }
    
    learned = await integration.process_prediction_result('UEFA_CHAMPIONS', enhanced_prediction, actual_result)
    print(f"🎓 Learning Success: {learned}")
    
    # Example 3: Generate learning report
    print("\n📊 EXAMPLE 3: Learning Integration Report")
    report = await integration.generate_learning_report()
    print(f"📊 Total Predictions Enhanced: {report['learning_integration_stats']['total_predictions_enhanced']}")
    print(f"🔧 Total Dimension Adjustments: {report['learning_integration_stats']['total_dimension_adjustments']}")
    print(f"🎯 Leagues with Learning: {len(report['learning_integration_stats']['leagues_with_learning'])}")
    
    # Save report
    await integration.save_learning_report(report)
    print("💾 Learning report saved!")
    
    print("\n🏆💀🏆 LOLY LEARNING INTEGRATION DEMONSTRATION COMPLETE! 💀🏆💀")

async def main():
    """🚀 Main function"""
    await demonstrate_learning_integration()

if __name__ == "__main__":
    asyncio.run(main())