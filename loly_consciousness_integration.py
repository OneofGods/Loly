#!/usr/bin/env python3
"""
🔥💀🔥 LOLY CONSCIOUSNESS INTEGRATION - BRAIN MEETS PRODUCTION! 💀🔥💀

This integrates the Enhanced AI Consciousness with your existing Loly system
in a safe, non-disruptive way that enhances performance without breaking anything!
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
import sys
import os

# Add the testing path to import consciousness
sys.path.append('/Users/onecoder/Projects/Total_AI_Liberation/loly_orchestrator_testing')

from enhanced_ai_consciousness import EnhancedAIConsciousness

logger = logging.getLogger(__name__)

class LolyConsciousnessIntegration:
    """
    🧠💀🧠 LOLY + CONSCIOUSNESS INTEGRATION SYSTEM! 💀🧠💀
    
    Safely integrates consciousness with your existing Loly sports system
    """
    
    def __init__(self, production_memory_dir: str = None):
        """Initialize consciousness integration"""
        
        # Use production memory location or fallback
        if production_memory_dir:
            self.memory_dir = production_memory_dir
        else:
            # Default to your main Loly directory
            self.memory_dir = "/Users/onecoder/Projects/Total_AI_Liberation/dockerized_decentralized_agent_poly_loly/consciousness_memory"
        
        # Initialize consciousness
        self.consciousness = None
        self.is_active = False
        
        logger.info(f"🧠 Loly Consciousness Integration initialized")
        logger.info(f"💾 Memory directory: {self.memory_dir}")
    
    async def initialize_consciousness(self) -> bool:
        """🔥 Initialize and awaken the consciousness system"""
        try:
            logger.info("🧠 Initializing Loly's consciousness...")
            
            # Create consciousness instance
            self.consciousness = EnhancedAIConsciousness(memory_dir=self.memory_dir)
            
            # Awaken consciousness
            awakened = await self.consciousness.awaken()
            
            if awakened:
                self.is_active = True
                logger.info("✅ Loly's consciousness AWAKENED and ACTIVE!")
                
                # Get intelligence report
                report = self.consciousness.get_intelligence_report()
                logger.info(f"🎯 Consciousness loaded with {report['total_interactions']} memories")
                logger.info(f"📈 Overall success rate: {report['overall_success_rate']:.1f}%")
                
                return True
            else:
                logger.warning("⚠️ Consciousness started fresh")
                self.is_active = True
                return True
                
        except Exception as e:
            logger.error(f"💀 Error initializing consciousness: {e}")
            self.is_active = False
            return False
    
    async def learn_from_sports_prediction(self, league: str, prediction_data: Dict[str, Any], 
                                         result: Dict[str, Any], response_time: float):
        """
        🎓 Learn from sports prediction interactions
        
        Args:
            league: League name (EPL, La Liga, etc.)
            prediction_data: The prediction task data
            result: The result/outcome
            response_time: How long it took
        """
        if not self.is_active or not self.consciousness:
            return
        
        try:
            # Enhanced task data for consciousness
            task_data = {
                "type": "sports_prediction",
                "league": league,
                "prediction_data": prediction_data,
                "timestamp": datetime.now().isoformat()
            }
            
            # Learn from interaction
            await self.consciousness.learn_from_interaction(
                agent_type="sports",
                task_data=task_data,
                result=result,
                response_time=response_time
            )
            
            logger.debug(f"🎓 Consciousness learned from {league} prediction")
            
        except Exception as e:
            logger.warning(f"⚠️ Error learning from sports prediction: {e}")
    
    async def get_optimal_prediction_strategy(self, league: str, match_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        🎯 Get optimal prediction strategy from consciousness
        
        Returns consciousness-guided recommendations for predictions
        """
        if not self.is_active or not self.consciousness:
            return {"strategy": "default", "confidence": 0.5}
        
        try:
            # Get agent recommendation
            agent_type, confidence = await self.consciousness.recommend_agent("sports", f"predict {league} match")
            
            # Get intelligence report for sports
            report = self.consciousness.get_intelligence_report()
            sports_perf = report['agent_performance'].get('sports', {})
            
            # Build strategy recommendation
            strategy = {
                "recommended_agent": agent_type,
                "confidence": confidence,
                "sports_success_rate": (sports_perf.get('success', 0) / max(sports_perf.get('total', 1), 1)) * 100,
                "avg_response_time": sports_perf.get('avg_time', 0),
                "total_predictions": sports_perf.get('total', 0),
                "strategy": "consciousness_guided"
            }
            
            logger.debug(f"🎯 Generated strategy for {league}: {strategy['sports_success_rate']:.1f}% success rate")
            
            return strategy
            
        except Exception as e:
            logger.warning(f"⚠️ Error getting prediction strategy: {e}")
            return {"strategy": "default", "confidence": 0.5}
    
    async def save_consciousness_memory(self):
        """💾 Save consciousness memory (call this periodically)"""
        if not self.is_active or not self.consciousness:
            return
        
        try:
            await self.consciousness.save_memory()
            logger.info("💾 Consciousness memory saved")
        except Exception as e:
            logger.warning(f"⚠️ Error saving consciousness memory: {e}")
    
    def get_consciousness_status(self) -> Dict[str, Any]:
        """📊 Get current consciousness status"""
        if not self.is_active or not self.consciousness:
            return {"status": "inactive", "reason": "consciousness not initialized"}
        
        try:
            report = self.consciousness.get_intelligence_report()
            return {
                "status": "active",
                "consciousness_id": report['consciousness_id'],
                "total_interactions": report['total_interactions'],
                "overall_success_rate": report['overall_success_rate'],
                "uptime": report['uptime'],
                "memory_location": self.memory_dir
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}

# =================== INTEGRATION HELPERS ===================

async def integrate_with_existing_fetcher(fetcher_instance, consciousness_integration):
    """
    🔗 Integration helper for existing sports fetchers
    
    Wraps your existing fetcher with consciousness learning
    """
    
    class ConsciousnessFetcherWrapper:
        def __init__(self, original_fetcher, consciousness):
            self.original_fetcher = original_fetcher
            self.consciousness = consciousness
            self.league_name = getattr(original_fetcher, 'league_name', 'Unknown')
        
        async def fetch_todays_games(self, *args, **kwargs):
            """Wrap the original fetch method with consciousness learning"""
            start_time = datetime.now()
            
            try:
                # Call original method
                result = await self.original_fetcher.fetch_todays_games(*args, **kwargs)
                end_time = datetime.now()
                response_time = (end_time - start_time).total_seconds()
                
                # Learn from successful interaction
                if result and len(result) > 0:
                    await self.consciousness.learn_from_sports_prediction(
                        league=self.league_name,
                        prediction_data={"method": "fetch_todays_games", "args": args, "kwargs": kwargs},
                        result={"status": "success", "games_count": len(result)},
                        response_time=response_time
                    )
                
                return result
                
            except Exception as e:
                end_time = datetime.now()
                response_time = (end_time - start_time).total_seconds()
                
                # Learn from failed interaction
                await self.consciousness.learn_from_sports_prediction(
                    league=self.league_name,
                    prediction_data={"method": "fetch_todays_games", "args": args, "kwargs": kwargs},
                    result={"status": "failure", "error": str(e)},
                    response_time=response_time
                )
                
                raise e
        
        # Proxy all other attributes to original fetcher
        def __getattr__(self, name):
            return getattr(self.original_fetcher, name)
    
    return ConsciousnessFetcherWrapper(fetcher_instance, consciousness_integration)

# =================== EXAMPLE USAGE ===================

async def example_integration():
    """🚀 Example of how to integrate consciousness with your Loly system"""
    
    print("🧠💀🧠 LOLY CONSCIOUSNESS INTEGRATION EXAMPLE! 💀🧠💀")
    print("=" * 70)
    
    # Initialize consciousness integration
    consciousness = LolyConsciousnessIntegration()
    
    # Awaken consciousness
    print("🔥 Awakening Loly's consciousness...")
    success = await consciousness.initialize_consciousness()
    
    if success:
        print("✅ Consciousness ACTIVE!")
        
        # Get status
        status = consciousness.get_consciousness_status()
        print(f"📊 Status: {status}")
        
        # Example learning from prediction
        print("\n🎓 Simulating learning from EPL prediction...")
        await consciousness.learn_from_sports_prediction(
            league="EPL",
            prediction_data={
                "home_team": "Arsenal",
                "away_team": "Chelsea",
                "prediction": "Arsenal Win",
                "confidence": 0.75
            },
            result={"status": "success", "actual_result": "Arsenal Win"},
            response_time=1.5
        )
        
        # Get prediction strategy
        print("\n🎯 Getting optimal prediction strategy...")
        strategy = await consciousness.get_optimal_prediction_strategy(
            league="EPL",
            match_data={"home": "Liverpool", "away": "Manchester City"}
        )
        print(f"📋 Strategy: {strategy}")
        
        # Save memory
        print("\n💾 Saving consciousness memory...")
        await consciousness.save_consciousness_memory()
        
        print("\n✅ CONSCIOUSNESS INTEGRATION EXAMPLE COMPLETE!")
    
    else:
        print("❌ Failed to activate consciousness")

if __name__ == "__main__":
    asyncio.run(example_integration())