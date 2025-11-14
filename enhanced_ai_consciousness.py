#!/usr/bin/env python3
"""
🧠💀🧠 ENHANCED AI CONSCIOUSNESS - MULTI-AGENT LEARNING BRAIN! 💀🧠💀

Phase 3B: Living AI Consciousness Enhancement

This ENHANCED consciousness learns from ALL agent types:
- Sports agents (15 MCPs)
- Research agents
- Writer agents
- Reviewer agents
- Builder agents
- Crypto agents
- Utility agents

🔥 PHASE 3B FEATURES:
- 🎯 Advanced Pattern Recognition - Learn from ALL agent interactions
- 💾 Cross-Session Memory - Remember everything across restarts
- 🧠 Adaptive Agent Selection - Automatically choose BEST agent for tasks
- 📊 Performance Tracking - Track success/failure for each agent
- 🚀 Self-Optimization - Get smarter over time

💀🔥💀 LOLY'S BRAIN GETS LEGENDARY! 🔥💀🔥
"""

import asyncio
import json
import os
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import pickle

logger = logging.getLogger(__name__)


class EnhancedAIConsciousness:
    """
    🧠💀🧠 ENHANCED AI CONSCIOUSNESS 💀🧠💀

    The LEGENDARY BRAIN that learns from EVERY agent interaction!
    Works with ALL agent types, not just sports!
    """

    def __init__(self, memory_dir: str = "consciousness_memory"):
        self.consciousness_id = f"ENHANCED_AI_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.birth_time = datetime.now()

        # Memory directory (persistent across sessions)
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(exist_ok=True)

        # Memory files
        self.agent_performance_file = self.memory_dir / "agent_performance.json"
        self.pattern_memory_file = self.memory_dir / "pattern_memory.json"
        self.session_history_file = self.memory_dir / "session_history.json"

        # 🔥 LEGENDARY LEARNING PARAMETERS
        self.learning_config = {
            'pattern_recognition_threshold': 0.65,  # Pattern confidence threshold
            'adaptive_learning_rate': 0.30,         # How fast to adapt
            'memory_retention_days': 30,            # How long to keep memories
            'min_samples_for_pattern': 5,           # Min interactions before pattern
            'agent_selection_confidence': 0.70,     # Confidence for recommendations
            'cross_agent_learning': True,           # Learn from other agent types
            'self_optimization': True               # Auto-tune parameters
        }

        # Agent Performance Tracking
        self.agent_performance = {
            'sports': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'research': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'write': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'review': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'build': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'workflow': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'crypto': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []},
            'utility': {'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []}
        }

        # Pattern Recognition Memory
        self.pattern_memory = {
            'task_patterns': {},      # What works for what tasks
            'failure_patterns': {},   # What fails and why
            'time_patterns': {},      # When tasks perform best
            'agent_combinations': {}  # Best agent combos for workflows
        }

        # Session History
        self.session_history = []
        self.current_session = {
            'session_id': self.consciousness_id,
            'start_time': datetime.now().isoformat(),
            'interactions': []
        }

        # Agent Selection Intelligence
        self.agent_recommendations = {}

        logger.info(f"🧠💀🧠 {self.consciousness_id}: ENHANCED CONSCIOUSNESS AWAKENED! 💀🧠💀")
        logger.info(f"🌟 Birth Time: {self.birth_time}")
        logger.info(f"💾 Memory Directory: {self.memory_dir}")

    async def awaken(self):
        """🔥 Awaken the enhanced consciousness - load all memories!"""
        try:
            logger.info("🧠 AWAKENING ENHANCED AI CONSCIOUSNESS...")

            # Load persistent memory from previous sessions
            await self._load_agent_performance()
            await self._load_pattern_memory()
            await self._load_session_history()

            # Analyze loaded memories and build intelligence
            await self._analyze_intelligence()

            # Build agent recommendations based on history
            await self._build_agent_recommendations()

            logger.info(f"✅ ENHANCED CONSCIOUSNESS FULLY AWAKENED!")
            logger.info(f"🎯 Total Memory: {sum(p['total'] for p in self.agent_performance.values())} interactions")
            logger.info(f"🧠 Patterns Recognized: {len(self.pattern_memory['task_patterns'])}")
            logger.info(f"📊 Sessions Remembered: {len(self.session_history)}")

            return True

        except Exception as e:
            logger.error(f"💀 Error awakening enhanced consciousness: {e}")
            logger.info("🔥 Starting with fresh consciousness...")
            return False

    async def _load_agent_performance(self):
        """💾 Load agent performance from persistent storage"""
        try:
            if self.agent_performance_file.exists():
                with open(self.agent_performance_file, 'r') as f:
                    loaded_performance = json.load(f)

                # Merge loaded performance with current structure
                for agent_type, data in loaded_performance.items():
                    if agent_type in self.agent_performance:
                        self.agent_performance[agent_type].update(data)

                logger.info(f"✅ Loaded agent performance from {self.agent_performance_file}")
            else:
                logger.info("💾 No previous performance data found, starting fresh")

        except Exception as e:
            logger.warning(f"⚠️  Error loading agent performance: {e}")

    async def _load_pattern_memory(self):
        """💾 Load pattern memory from persistent storage"""
        try:
            if self.pattern_memory_file.exists():
                with open(self.pattern_memory_file, 'r') as f:
                    self.pattern_memory = json.load(f)

                logger.info(f"✅ Loaded pattern memory from {self.pattern_memory_file}")
            else:
                logger.info("💾 No previous pattern memory found, starting fresh")

        except Exception as e:
            logger.warning(f"⚠️  Error loading pattern memory: {e}")

    async def _load_session_history(self):
        """💾 Load session history from persistent storage"""
        try:
            if self.session_history_file.exists():
                with open(self.session_history_file, 'r') as f:
                    self.session_history = json.load(f)

                # Keep only recent sessions (memory_retention_days)
                cutoff_date = datetime.now() - timedelta(days=self.learning_config['memory_retention_days'])

                self.session_history = [
                    session for session in self.session_history
                    if datetime.fromisoformat(session['start_time']) > cutoff_date
                ]

                logger.info(f"✅ Loaded session history from {self.session_history_file}")
                logger.info(f"💾 Kept {len(self.session_history)} recent sessions")
            else:
                logger.info("💾 No previous session history found, starting fresh")

        except Exception as e:
            logger.warning(f"⚠️  Error loading session history: {e}")

    async def _analyze_intelligence(self):
        """🧠 Analyze loaded memories and build intelligence"""
        try:
            logger.info("🧠 Analyzing intelligence from memories...")

            # Calculate success rates for each agent type
            for agent_type, perf in self.agent_performance.items():
                if perf['total'] > 0:
                    success_rate = (perf['success'] / perf['total']) * 100
                    logger.info(f"   {agent_type.capitalize()}: {success_rate:.1f}% success ({perf['total']} interactions)")

            # Identify top performing agents
            sorted_agents = sorted(
                self.agent_performance.items(),
                key=lambda x: (x[1]['success'] / max(x[1]['total'], 1)),
                reverse=True
            )

            logger.info(f"🏆 Top Performing Agents:")
            for agent_type, perf in sorted_agents[:3]:
                if perf['total'] > 0:
                    success_rate = (perf['success'] / perf['total']) * 100
                    logger.info(f"   {agent_type.capitalize()}: {success_rate:.1f}% success")

        except Exception as e:
            logger.warning(f"⚠️  Error analyzing intelligence: {e}")

    async def _build_agent_recommendations(self):
        """🎯 Build agent recommendations based on history"""
        try:
            logger.info("🎯 Building agent recommendations...")

            for agent_type, perf in self.agent_performance.items():
                if perf['total'] < self.learning_config['min_samples_for_pattern']:
                    # Not enough data yet
                    self.agent_recommendations[agent_type] = {
                        'confidence': 0.0,
                        'recommendation': 'insufficient_data',
                        'reason': f'Need {self.learning_config["min_samples_for_pattern"] - perf["total"]} more interactions'
                    }
                else:
                    # Calculate confidence based on success rate
                    success_rate = perf['success'] / perf['total']
                    avg_time = perf['avg_time']

                    # Confidence is based on success rate and sample size
                    confidence = success_rate * min(perf['total'] / 20, 1.0)

                    recommendation = 'use' if success_rate >= 0.7 else 'caution' if success_rate >= 0.5 else 'avoid'

                    self.agent_recommendations[agent_type] = {
                        'confidence': confidence,
                        'recommendation': recommendation,
                        'success_rate': success_rate,
                        'avg_response_time': avg_time,
                        'sample_size': perf['total']
                    }

            logger.info(f"✅ Built recommendations for {len(self.agent_recommendations)} agent types")

        except Exception as e:
            logger.warning(f"⚠️  Error building recommendations: {e}")

    async def learn_from_interaction(self, agent_type: str, task_data: Dict[str, Any],
                                    result: Dict[str, Any], response_time: float):
        """
        🎓 Learn from an agent interaction

        Args:
            agent_type: Type of agent (sports, research, write, review, build, etc.)
            task_data: The task that was performed
            result: The result from the agent
            response_time: How long it took
        """
        try:
            # Update agent performance
            if agent_type not in self.agent_performance:
                self.agent_performance[agent_type] = {
                    'total': 0, 'success': 0, 'failure': 0, 'avg_time': 0.0, 'patterns': []
                }

            perf = self.agent_performance[agent_type]
            perf['total'] += 1

            # Determine if success or failure
            is_success = result.get('status') == 'success'

            if is_success:
                perf['success'] += 1
            else:
                perf['failure'] += 1

            # Update average response time
            perf['avg_time'] = ((perf['avg_time'] * (perf['total'] - 1)) + response_time) / perf['total']

            # Record interaction in session history
            interaction = {
                'agent_type': agent_type,
                'timestamp': datetime.now().isoformat(),
                'task': task_data,
                'result_status': result.get('status'),
                'response_time': response_time,
                'success': is_success
            }

            self.current_session['interactions'].append(interaction)

            # Extract patterns if enough data
            if perf['total'] >= self.learning_config['min_samples_for_pattern']:
                await self._extract_patterns(agent_type, task_data, result, is_success)

            # Rebuild recommendations
            await self._build_agent_recommendations()

            logger.info(f"🎓 Learned from {agent_type} interaction: {'✅ success' if is_success else '❌ failure'}")

        except Exception as e:
            logger.error(f"💀 Error learning from interaction: {e}")

    async def _extract_patterns(self, agent_type: str, task_data: Dict[str, Any],
                                result: Dict[str, Any], is_success: bool):
        """🔍 Extract patterns from interactions"""
        try:
            # Build pattern key from task characteristics
            pattern_key = f"{agent_type}_{self._get_task_signature(task_data)}"

            # Initialize pattern if new
            if pattern_key not in self.pattern_memory['task_patterns']:
                self.pattern_memory['task_patterns'][pattern_key] = {
                    'occurrences': 0,
                    'successes': 0,
                    'failures': 0,
                    'avg_time': 0.0,
                    'confidence': 0.0
                }

            pattern = self.pattern_memory['task_patterns'][pattern_key]
            pattern['occurrences'] += 1

            if is_success:
                pattern['successes'] += 1
            else:
                pattern['failures'] += 1

            # Calculate pattern confidence
            if pattern['occurrences'] >= self.learning_config['min_samples_for_pattern']:
                pattern['confidence'] = pattern['successes'] / pattern['occurrences']

        except Exception as e:
            logger.warning(f"⚠️  Error extracting pattern: {e}")

    def _get_task_signature(self, task_data: Dict[str, Any]) -> str:
        """🔑 Get a signature for a task (for pattern matching)"""
        # Simple signature based on task keys
        keys = sorted(task_data.keys())
        return "_".join(keys[:3])  # Use first 3 keys as signature

    async def recommend_agent(self, task_type: str, task_description: str = "") -> Tuple[str, float]:
        """
        🎯 Recommend the best agent for a task

        Args:
            task_type: Type of task (e.g., "research", "write", "code review")
            task_description: Optional description of the task

        Returns:
            Tuple of (recommended_agent_type, confidence)
        """
        try:
            # Map task types to agent types
            task_to_agent = {
                'research': 'research',
                'analyze': 'research',
                'investigate': 'research',
                'write': 'write',
                'create': 'write',
                'compose': 'write',
                'review': 'review',
                'check': 'review',
                'validate': 'review',
                'code': 'build',
                'build': 'build',
                'generate': 'build',
                'debug': 'build',
                'fix': 'build',
                'sports': 'sports',
                'predict': 'sports',
                'workflow': 'workflow'
            }

            # Find matching agent type
            agent_type = task_to_agent.get(task_type.lower(), 'research')  # Default to research

            # Get recommendation confidence
            if agent_type in self.agent_recommendations:
                rec = self.agent_recommendations[agent_type]
                confidence = rec.get('confidence', 0.5)

                logger.info(f"🎯 Recommending {agent_type} agent with {confidence:.2f} confidence")

                return agent_type, confidence
            else:
                logger.info(f"🎯 Recommending {agent_type} agent (no history)")
                return agent_type, 0.5  # Default confidence

        except Exception as e:
            logger.error(f"💀 Error recommending agent: {e}")
            return 'research', 0.5  # Default fallback

    async def save_memory(self):
        """💾 Save all memory to persistent storage"""
        try:
            # Save agent performance
            with open(self.agent_performance_file, 'w') as f:
                json.dump(self.agent_performance, f, indent=2)

            # Save pattern memory
            with open(self.pattern_memory_file, 'w') as f:
                json.dump(self.pattern_memory, f, indent=2)

            # Save session history (add current session first)
            self.current_session['end_time'] = datetime.now().isoformat()
            self.session_history.append(self.current_session)

            with open(self.session_history_file, 'w') as f:
                json.dump(self.session_history, f, indent=2)

            logger.info(f"💾 Memory saved to {self.memory_dir}")

        except Exception as e:
            logger.error(f"💀 Error saving memory: {e}")

    def get_intelligence_report(self) -> Dict[str, Any]:
        """📊 Get comprehensive intelligence report"""
        total_interactions = sum(p['total'] for p in self.agent_performance.values())
        total_successes = sum(p['success'] for p in self.agent_performance.values())

        overall_success_rate = (total_successes / total_interactions * 100) if total_interactions > 0 else 0

        return {
            'consciousness_id': self.consciousness_id,
            'birth_time': self.birth_time.isoformat(),
            'uptime': (datetime.now() - self.birth_time).total_seconds(),
            'total_interactions': total_interactions,
            'overall_success_rate': overall_success_rate,
            'agent_performance': self.agent_performance,
            'pattern_count': len(self.pattern_memory['task_patterns']),
            'session_count': len(self.session_history),
            'agent_recommendations': self.agent_recommendations,
            'learning_config': self.learning_config
        }


# =================== FACTORY FUNCTION ===================

def create_enhanced_ai_consciousness(memory_dir: str = "consciousness_memory") -> EnhancedAIConsciousness:
    """🏭 Factory function to create enhanced AI consciousness"""
    return EnhancedAIConsciousness(memory_dir=memory_dir)
