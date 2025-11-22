#!/usr/bin/env python3
"""
🧠💀 AI BRAIN STUB - Temporary until real implementation! 💀🧠

This is a STUB to allow Loly to run while we build the real AI brain!
"""

import logging
from enum import Enum
from typing import Dict, Any, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class DecisionComplexity(Enum):
    """Decision complexity levels"""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    CRITICAL = "critical"


@dataclass
class AIContext:
    """Context for AI decision making"""
    agent_id: str
    task_description: str
    context_data: Dict[str, Any]
    complexity: DecisionComplexity
    priority: int = 5


class AIBrainStub:
    """
    🧠 STUB AI Brain - Returns simple responses

    TODO: Replace with real LLM integration!
    """

    def __init__(self, brain_id: str):
        self.brain_id = brain_id
        logger.info(f"🧠 AIBrain stub initialized: {brain_id}")
        logger.warning("⚠️ Using STUB AI Brain - real implementation needed!")

    async def make_intelligent_decision(self, context: AIContext) -> Dict[str, Any]:
        """
        Make a decision (STUB - just returns context for now)

        TODO: Implement real LLM call here!
        """
        logger.info(f"🧠 AI Brain processing: {context.task_description}")

        # STUB: Just return a simple response based on context
        message = context.context_data.get('current_message', '')

        # Very basic response
        response = f"I understand you said: {message}. I'm still learning to respond intelligently!"

        return {
            'decision': response,
            'confidence': 0.5,
            'reasoning': 'STUB response - real AI brain needed',
            'engine': 'ai_brain_stub'
        }


# Global instance
_ai_brain_instance = None


def get_ai_brain(brain_id: str = "default") -> AIBrainStub:
    """Get the AI brain instance"""
    global _ai_brain_instance
    if _ai_brain_instance is None:
        _ai_brain_instance = AIBrainStub(brain_id)
    return _ai_brain_instance
