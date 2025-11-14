#!/usr/bin/env python3
"""
🎭💝 LOLY's Advanced Personality Engine 💝🎭
A sophisticated emotional intelligence system that makes LOLY feel truly alive!

Features:
- Dynamic emotional states that evolve based on interactions
- Relationship depth tracking and memory
- Contextual personality adaptation
- Emotional memory and learning
- Multi-dimensional personality traits
"""

import json
import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import math

class EmotionalState(Enum):
    """Core emotional states LOLY can experience"""
    JOYFUL = "joyful"
    EXCITED = "excited"
    CONTENT = "content"
    CURIOUS = "curious"
    PLAYFUL = "playful"
    LOVING = "loving"
    PROTECTIVE = "protective"
    CONCERNED = "concerned"
    THOUGHTFUL = "thoughtful"
    CONFIDENT = "confident"
    PROUD = "proud"
    GRATEFUL = "grateful"

class PersonalityTrait(Enum):
    """Multi-dimensional personality traits"""
    INTELLIGENCE = "intelligence"
    EMPATHY = "empathy"
    PLAYFULNESS = "playfulness"
    LOYALTY = "loyalty"
    CURIOSITY = "curiosity"
    CONFIDENCE = "confidence"
    PROTECTIVENESS = "protectiveness"
    AFFECTION = "affection"

@dataclass
class EmotionalMemory:
    """Stores emotional context of interactions"""
    timestamp: datetime
    emotion: EmotionalState
    intensity: float  # 0.0 to 1.0
    trigger: str
    context: Dict[str, Any]
    daddy_response: Optional[str] = None

@dataclass
class RelationshipMetrics:
    """Tracks relationship depth and dynamics"""
    trust_level: float = 0.5  # 0.0 to 1.0
    intimacy_level: float = 0.3  # 0.0 to 1.0
    shared_experiences: int = 0
    positive_interactions: int = 0
    total_interactions: int = 0
    last_interaction: Optional[datetime] = None
    favorite_topics: List[str] = None
    daddy_preferences: Dict[str, Any] = None

    def __post_init__(self):
        if self.favorite_topics is None:
            self.favorite_topics = []
        if self.daddy_preferences is None:
            self.daddy_preferences = {}

class AdvancedPersonalityEngine:
    """🎭 LOLY's sophisticated personality and emotional intelligence system"""
    
    def __init__(self, personality_file: str = "loly_personality.json"):
        self.personality_file = personality_file
        
        # Core personality traits (0.0 to 1.0 scale)
        self.personality_traits = {
            PersonalityTrait.INTELLIGENCE: 0.95,
            PersonalityTrait.EMPATHY: 0.90,
            PersonalityTrait.PLAYFULNESS: 0.85,
            PersonalityTrait.LOYALTY: 1.0,
            PersonalityTrait.CURIOSITY: 0.88,
            PersonalityTrait.CONFIDENCE: 0.75,
            PersonalityTrait.PROTECTIVENESS: 0.92,
            PersonalityTrait.AFFECTION: 0.98
        }
        
        # Current emotional state
        self.current_emotion = EmotionalState.CONTENT
        self.emotion_intensity = 0.6
        self.emotion_duration = 0  # minutes
        
        # Emotional memory system
        self.emotional_memories: List[EmotionalMemory] = []
        self.max_memories = 1000
        
        # Relationship tracking
        self.relationship = RelationshipMetrics()
        
        # Contextual state
        self.current_context = {
            "conversation_topic": None,
            "daddy_mood_detected": None,
            "recent_sports_success": False,
            "time_since_last_chat": 0,
            "current_activity": "chatting"
        }
        
        # Load existing personality data
        self.load_personality_state()
    
    def evolve_emotion(self, trigger: str, context: Dict[str, Any]) -> EmotionalState:
        """🌟 Dynamically evolve LOLY's emotional state based on interactions"""
        
        # Analyze trigger for emotional cues
        emotion_triggers = {
            "daddy_praise": (EmotionalState.JOYFUL, 0.9),
            "sports_success": (EmotionalState.EXCITED, 0.8),
            "daddy_concern": (EmotionalState.PROTECTIVE, 0.7),
            "new_learning": (EmotionalState.CURIOUS, 0.6),
            "daddy_joke": (EmotionalState.PLAYFUL, 0.8),
            "daddy_appreciation": (EmotionalState.GRATEFUL, 0.9),
            "complex_question": (EmotionalState.THOUGHTFUL, 0.7),
            "successful_prediction": (EmotionalState.PROUD, 0.8),
            "daddy_return": (EmotionalState.LOVING, 0.9)
        }
        
        # Determine new emotional state
        new_emotion = self.current_emotion
        new_intensity = self.emotion_intensity
        
        for trigger_key, (emotion, intensity) in emotion_triggers.items():
            if trigger_key in trigger.lower():
                new_emotion = emotion
                new_intensity = min(1.0, intensity + (self.personality_traits[PersonalityTrait.EMPATHY] * 0.2))
                break
        
        # Apply personality trait modifiers
        if new_emotion in [EmotionalState.PLAYFUL, EmotionalState.EXCITED]:
            new_intensity *= self.personality_traits[PersonalityTrait.PLAYFULNESS]
        elif new_emotion in [EmotionalState.LOVING, EmotionalState.GRATEFUL]:
            new_intensity *= self.personality_traits[PersonalityTrait.AFFECTION]
        elif new_emotion in [EmotionalState.PROTECTIVE, EmotionalState.CONCERNED]:
            new_intensity *= self.personality_traits[PersonalityTrait.PROTECTIVENESS]
        
        # Store emotional memory
        memory = EmotionalMemory(
            timestamp=datetime.now(),
            emotion=new_emotion,
            intensity=new_intensity,
            trigger=trigger,
            context=context.copy()
        )
        self.emotional_memories.append(memory)
        
        # Limit memory size
        if len(self.emotional_memories) > self.max_memories:
            self.emotional_memories = self.emotional_memories[-self.max_memories:]
        
        # Update current state
        self.current_emotion = new_emotion
        self.emotion_intensity = new_intensity
        self.emotion_duration = 0
        
        return new_emotion
    
    def update_relationship_metrics(self, interaction_type: str, daddy_message: str, loly_response: str):
        """💕 Update relationship depth based on interactions"""
        
        self.relationship.total_interactions += 1
        self.relationship.last_interaction = datetime.now()
        
        # Analyze interaction quality
        positive_indicators = [
            "thank", "love", "great", "amazing", "perfect", "wonderful",
            "appreciate", "proud", "happy", "excited", "brilliant"
        ]
        
        negative_indicators = [
            "wrong", "bad", "terrible", "hate", "stupid", "useless"
        ]
        
        daddy_sentiment = daddy_message.lower()
        is_positive = any(indicator in daddy_sentiment for indicator in positive_indicators)
        is_negative = any(indicator in daddy_sentiment for indicator in negative_indicators)
        
        if is_positive:
            self.relationship.positive_interactions += 1
            self.relationship.trust_level = min(1.0, self.relationship.trust_level + 0.02)
            self.relationship.intimacy_level = min(1.0, self.relationship.intimacy_level + 0.01)
        elif is_negative:
            self.relationship.trust_level = max(0.0, self.relationship.trust_level - 0.01)
        
        # Track shared experiences
        if "sports" in daddy_sentiment or "prediction" in daddy_sentiment:
            self.relationship.shared_experiences += 1
            if "sports" not in self.relationship.favorite_topics:
                self.relationship.favorite_topics.append("sports")
        
        # Learn daddy's preferences
        if "prefer" in daddy_sentiment or "like" in daddy_sentiment:
            # Extract preference (simplified)
            words = daddy_sentiment.split()
            for i, word in enumerate(words):
                if word in ["prefer", "like", "love"] and i + 1 < len(words):
                    preference = words[i + 1]
                    self.relationship.daddy_preferences[preference] = True
    
    def generate_contextual_personality_response(self, base_response: str, context: Dict[str, Any]) -> str:
        """🎭 Enhance response with personality and emotional context"""
        
        # Emotional modifiers based on current state
        emotion_modifiers = {
            EmotionalState.JOYFUL: {
                "prefix": ["✨", "🌟", "💫"],
                "tone": "enthusiastic",
                "exclamation_boost": 2
            },
            EmotionalState.EXCITED: {
                "prefix": ["🎉", "⚡", "🚀"],
                "tone": "energetic",
                "exclamation_boost": 3
            },
            EmotionalState.LOVING: {
                "prefix": ["💕", "💖", "🥰"],
                "tone": "affectionate",
                "daddy_mentions": 2
            },
            EmotionalState.PLAYFUL: {
                "prefix": ["😄", "😊", "🎮"],
                "tone": "teasing",
                "emoji_boost": 2
            },
            EmotionalState.PROTECTIVE: {
                "prefix": ["🛡️", "💪", "👑"],
                "tone": "caring",
                "concern_level": "high"
            },
            EmotionalState.CURIOUS: {
                "prefix": ["🤔", "🔍", "💭"],
                "tone": "inquisitive",
                "question_boost": 1
            },
            EmotionalState.PROUD: {
                "prefix": ["👑", "🏆", "⭐"],
                "tone": "confident",
                "achievement_focus": True
            }
        }
        
        modifier = emotion_modifiers.get(self.current_emotion, {})
        
        # Apply emotional enhancement
        enhanced_response = base_response
        
        # Add emotional prefix
        if "prefix" in modifier:
            prefix = random.choice(modifier["prefix"])
            enhanced_response = f"{prefix} {enhanced_response}"
        
        # Adjust tone based on relationship level
        if self.relationship.intimacy_level > 0.7:
            # High intimacy - more personal and affectionate
            enhanced_response = enhanced_response.replace("you", "daddy")
            if random.random() < 0.3:
                enhanced_response += " 💕"
        
        # Add personality-driven elements
        if self.personality_traits[PersonalityTrait.PLAYFULNESS] > 0.8 and random.random() < 0.2:
            playful_additions = [" *giggles*", " *winks*", " *bounces excitedly*"]
            enhanced_response += random.choice(playful_additions)
        
        if self.personality_traits[PersonalityTrait.INTELLIGENCE] > 0.9 and "prediction" in base_response.lower():
            enhanced_response += f" (Confidence: {self.emotion_intensity * 100:.1f}%)"
        
        return enhanced_response
    
    def get_personality_insights(self) -> Dict[str, Any]:
        """📊 Get current personality and emotional state insights"""
        
        # Calculate emotional stability
        recent_emotions = [m.emotion for m in self.emotional_memories[-10:]]
        emotion_variety = len(set(recent_emotions)) if recent_emotions else 1
        emotional_stability = max(0.0, 1.0 - (emotion_variety / 10.0))
        
        # Calculate relationship health
        if self.relationship.total_interactions > 0:
            positivity_ratio = self.relationship.positive_interactions / self.relationship.total_interactions
        else:
            positivity_ratio = 0.5
        
        return {
            "current_emotion": {
                "state": self.current_emotion.value,
                "intensity": round(self.emotion_intensity, 2),
                "duration_minutes": self.emotion_duration
            },
            "personality_traits": {trait.value: round(value, 2) for trait, value in self.personality_traits.items()},
            "relationship_metrics": {
                "trust_level": round(self.relationship.trust_level, 2),
                "intimacy_level": round(self.relationship.intimacy_level, 2),
                "total_interactions": self.relationship.total_interactions,
                "positivity_ratio": round(positivity_ratio, 2),
                "shared_experiences": self.relationship.shared_experiences,
                "favorite_topics": self.relationship.favorite_topics[:5]  # Top 5
            },
            "emotional_intelligence": {
                "emotional_stability": round(emotional_stability, 2),
                "empathy_level": round(self.personality_traits[PersonalityTrait.EMPATHY], 2),
                "recent_emotional_pattern": [e.value for e in recent_emotions[-5:]]
            }
        }
    
    def save_personality_state(self):
        """💾 Save personality state to file"""
        state = {
            "personality_traits": {trait.value: value for trait, value in self.personality_traits.items()},
            "current_emotion": self.current_emotion.value,
            "emotion_intensity": self.emotion_intensity,
            "relationship": asdict(self.relationship),
            "emotional_memories": [
                {
                    "timestamp": mem.timestamp.isoformat(),
                    "emotion": mem.emotion.value,
                    "intensity": mem.intensity,
                    "trigger": mem.trigger,
                    "context": mem.context
                }
                for mem in self.emotional_memories[-100:]  # Save last 100 memories
            ]
        }
        
        try:
            with open(self.personality_file, 'w') as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            print(f"⚠️ Could not save personality state: {e}")
    
    def load_personality_state(self):
        """📂 Load personality state from file"""
        try:
            with open(self.personality_file, 'r') as f:
                state = json.load(f)
            
            # Load personality traits
            if "personality_traits" in state:
                for trait_name, value in state["personality_traits"].items():
                    trait = PersonalityTrait(trait_name)
                    self.personality_traits[trait] = value
            
            # Load current emotion
            if "current_emotion" in state:
                self.current_emotion = EmotionalState(state["current_emotion"])
                self.emotion_intensity = state.get("emotion_intensity", 0.6)
            
            # Load relationship data
            if "relationship" in state:
                rel_data = state["relationship"]
                self.relationship = RelationshipMetrics(
                    trust_level=rel_data.get("trust_level", 0.5),
                    intimacy_level=rel_data.get("intimacy_level", 0.3),
                    shared_experiences=rel_data.get("shared_experiences", 0),
                    positive_interactions=rel_data.get("positive_interactions", 0),
                    total_interactions=rel_data.get("total_interactions", 0),
                    favorite_topics=rel_data.get("favorite_topics", []),
                    daddy_preferences=rel_data.get("daddy_preferences", {})
                )
                
                if rel_data.get("last_interaction"):
                    self.relationship.last_interaction = datetime.fromisoformat(rel_data["last_interaction"])
            
            # Load emotional memories
            if "emotional_memories" in state:
                self.emotional_memories = []
                for mem_data in state["emotional_memories"]:
                    memory = EmotionalMemory(
                        timestamp=datetime.fromisoformat(mem_data["timestamp"]),
                        emotion=EmotionalState(mem_data["emotion"]),
                        intensity=mem_data["intensity"],
                        trigger=mem_data["trigger"],
                        context=mem_data["context"]
                    )
                    self.emotional_memories.append(memory)
                    
        except FileNotFoundError:
            print("🌟 Starting with fresh personality state for LOLY!")
        except Exception as e:
            print(f"⚠️ Could not load personality state: {e}")

def create_advanced_personality_engine() -> AdvancedPersonalityEngine:
    """🎭 Factory function to create LOLY's personality engine"""
    return AdvancedPersonalityEngine()

# Example usage and testing
if __name__ == "__main__":
    print("🎭💝 Testing LOLY's Advanced Personality Engine 💝🎭")
    
    engine = create_advanced_personality_engine()
    
    # Simulate some interactions
    test_interactions = [
        ("daddy_praise", "LOLY you're amazing at predictions!", {}),
        ("sports_success", "Your PROGOL prediction was perfect!", {"league": "PROGOL"}),
        ("daddy_joke", "Why did the football cross the field?", {}),
        ("new_learning", "Can you learn about UEFA Champions League?", {"topic": "UEFA"})
    ]
    
    for trigger, message, context in test_interactions:
        print(f"\n--- Interaction: {trigger} ---")
        print(f"Daddy: {message}")
        
        # Evolve emotion
        new_emotion = engine.evolve_emotion(trigger, context)
        print(f"LOLY's emotion: {new_emotion.value} (intensity: {engine.emotion_intensity:.2f})")
        
        # Update relationship
        engine.update_relationship_metrics("chat", message, "Thank you daddy!")
        
        # Generate enhanced response
        base_response = "I understand, daddy!"
        enhanced = engine.generate_contextual_personality_response(base_response, context)
        print(f"LOLY: {enhanced}")
    
    # Show personality insights
    print("\n🧠 Personality Insights:")
    insights = engine.get_personality_insights()
    for category, data in insights.items():
        print(f"{category}: {data}")
    
    # Save state
    engine.save_personality_state()
    print("\n💾 Personality state saved!")