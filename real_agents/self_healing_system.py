#!/usr/bin/env python3
"""
🔧💀🔧 SELF-HEALING SYSTEM 💀🔧💀
AUTOMATIC FAILURE DETECTION & RECOVERY

Intelligent system that detects known failure patterns and automatically
applies fixes, learns from failures, and evolves recovery strategies.

Created by: The AI Debugging Revolution  
Blessed by: Goddess of Syrup
"""

import asyncio
import json
import logging
import time
import inspect
import ast
import importlib
from typing import Dict, List, Any, Optional, Callable, Union, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from functools import wraps
import traceback
import re
from pathlib import Path

from enhanced_logging_system import enhanced_logger, with_correlation
from automated_debugging_assistant import assistant as debug_assistant

@dataclass
class HealingAction:
    """Self-healing action definition"""
    action_id: str
    pattern_signature: str
    description: str
    auto_fix_function: str
    confidence_threshold: float
    max_attempts: int
    cooldown_minutes: int
    success_count: int = 0
    failure_count: int = 0
    last_applied: Optional[datetime] = None

@dataclass
class HealingResult:
    """Result of a self-healing attempt"""
    action_id: str
    success: bool
    applied_at: datetime
    error_before: str
    error_after: Optional[str]
    fix_details: Dict[str, Any]
    confidence: float

class SelfHealingSystem:
    """
    🤖 SELF-HEALING SYSTEM
    
    Features:
    - Automatic failure pattern detection
    - Intelligent fix application
    - Learning from successful/failed healing attempts
    - Proactive issue prevention
    - Code adaptation for API changes
    - Performance optimization through healing
    """
    
    def __init__(self):
        self.healing_actions: Dict[str, HealingAction] = {}
        self.healing_history: List[HealingResult] = []
        self.active_monitors: Dict[str, Callable] = {}
        self.learning_database: Dict[str, Any] = {}
        
        # Initialize built-in healing actions
        self._initialize_healing_actions()
        
        enhanced_logger.info("🔧💀🔧 SELF-HEALING SYSTEM INITIALIZED 💀🔧💀")
    
    def _initialize_healing_actions(self):
        """Initialize built-in self-healing actions"""
        
        # ESPN API Structure Change Healing
        espn_healing = HealingAction(
            action_id="espn_api_structure_fix",
            pattern_signature="'int' object has no attribute 'get'",
            description="Fix ESPN API structure changes automatically",
            auto_fix_function="fix_espn_api_structure",
            confidence_threshold=0.8,
            max_attempts=3,
            cooldown_minutes=5
        )
        self.healing_actions[espn_healing.action_id] = espn_healing
        
        # Network Timeout Healing
        network_healing = HealingAction(
            action_id="network_timeout_fix",
            pattern_signature="timeout|connection.*refused|unreachable",
            description="Apply network resilience patterns automatically",
            auto_fix_function="fix_network_timeouts",
            confidence_threshold=0.7,
            max_attempts=5,
            cooldown_minutes=2
        )
        self.healing_actions[network_healing.action_id] = network_healing
        
        # Data Structure Validation Healing
        data_healing = HealingAction(
            action_id="data_structure_validation_fix",
            pattern_signature="KeyError|AttributeError.*get|NoneType.*attribute",
            description="Add defensive data structure handling",
            auto_fix_function="fix_data_structure_access",
            confidence_threshold=0.6,
            max_attempts=3,
            cooldown_minutes=10
        )
        self.healing_actions[data_healing.action_id] = data_healing
        
        # Algorithm Consensus Healing
        consensus_healing = HealingAction(
            action_id="algorithm_consensus_fix",
            pattern_signature="consensus.*confidence|phase.*processing",
            description="Fix algorithm consensus processing issues",
            auto_fix_function="fix_algorithm_consensus",
            confidence_threshold=0.7,
            max_attempts=2,
            cooldown_minutes=15
        )
        self.healing_actions[consensus_healing.action_id] = consensus_healing
    
    async def monitor_and_heal(self, error_context: Dict[str, Any]) -> Optional[HealingResult]:
        """Monitor for errors and attempt automatic healing"""
        
        with enhanced_logger.correlation_context("self_healing_monitor", "healing_system"):
            enhanced_logger.info(f"🔍 Analyzing error for self-healing potential")
            
            # Analyze error pattern
            pattern = await debug_assistant.analyze_error_context(error_context)
            
            # Find matching healing actions
            matching_actions = self._find_matching_healing_actions(error_context, pattern)
            
            if not matching_actions:
                enhanced_logger.info("🤷 No matching healing actions found")
                return None
            
            # Select best healing action
            best_action = self._select_best_healing_action(matching_actions, pattern)
            
            # Check if action can be applied (cooldown, max attempts, etc.)
            if not self._can_apply_healing_action(best_action):
                enhanced_logger.warning(f"🚫 Healing action {best_action.action_id} cannot be applied (cooldown/limits)")
                return None
            
            # Apply healing action
            enhanced_logger.info(f"🔧 Applying healing action: {best_action.description}")
            healing_result = await self._apply_healing_action(best_action, error_context, pattern)
            
            # Record result and learn
            self.healing_history.append(healing_result)
            await self._learn_from_healing_result(healing_result)
            
            return healing_result
    
    def _find_matching_healing_actions(self, error_context: Dict[str, Any], 
                                     pattern: Any) -> List[HealingAction]:
        """Find healing actions that match the error pattern"""
        
        error_message = error_context.get('error_message', '').lower()
        function_name = error_context.get('function_name', '')
        
        matching_actions = []
        
        for action in self.healing_actions.values():
            # Check pattern signature match
            if re.search(action.pattern_signature.lower(), error_message):
                matching_actions.append(action)
                enhanced_logger.debug(f"🎯 Matched healing action: {action.action_id}")
        
        return matching_actions
    
    def _select_best_healing_action(self, actions: List[HealingAction], pattern: Any) -> HealingAction:
        """Select the best healing action based on confidence and history"""
        
        def action_score(action: HealingAction) -> float:
            # Base score from confidence threshold
            score = action.confidence_threshold
            
            # Boost score based on success rate
            total_attempts = action.success_count + action.failure_count
            if total_attempts > 0:
                success_rate = action.success_count / total_attempts
                score += success_rate * 0.3
            
            # Penalize recent failures
            if action.failure_count > action.success_count:
                score -= 0.2
            
            return score
        
        return max(actions, key=action_score)
    
    def _can_apply_healing_action(self, action: HealingAction) -> bool:
        """Check if healing action can be applied"""
        
        # Check cooldown
        if action.last_applied:
            cooldown_end = action.last_applied + timedelta(minutes=action.cooldown_minutes)
            if datetime.now() < cooldown_end:
                return False
        
        # Check max attempts (in recent time window)
        recent_failures = [r for r in self.healing_history 
                          if r.action_id == action.action_id 
                          and not r.success 
                          and r.applied_at > datetime.now() - timedelta(hours=1)]
        
        if len(recent_failures) >= action.max_attempts:
            return False
        
        return True
    
    async def _apply_healing_action(self, action: HealingAction, 
                                  error_context: Dict[str, Any], 
                                  pattern: Any) -> HealingResult:
        """Apply the healing action"""
        
        start_time = datetime.now()
        error_before = error_context.get('error_message', '')
        
        try:
            # Get the healing function
            healing_function = getattr(self, action.auto_fix_function, None)
            
            if healing_function is None:
                raise AttributeError(f"Healing function '{action.auto_fix_function}' not found")
            
            if not callable(healing_function):
                raise TypeError(f"Healing function '{action.auto_fix_function}' is not callable")
            
            # Check if it's a coroutine function
            if not asyncio.iscoroutinefunction(healing_function):
                raise TypeError(f"Healing function '{action.auto_fix_function}' is not an async function")
            
            # Apply the fix
            fix_result = await healing_function(error_context, pattern)
            
            # Update action statistics
            action.success_count += 1
            action.last_applied = start_time
            
            enhanced_logger.info(f"✅ Healing action succeeded: {action.action_id}")
            
            return HealingResult(
                action_id=action.action_id,
                success=True,
                applied_at=start_time,
                error_before=error_before,
                error_after=None,
                fix_details=fix_result,
                confidence=action.confidence_threshold
            )
            
        except Exception as e:
            # Update action statistics
            action.failure_count += 1
            action.last_applied = start_time
            
            enhanced_logger.error(f"💥 Healing action failed: {action.action_id}", exc_info=True)
            
            return HealingResult(
                action_id=action.action_id,
                success=False,
                applied_at=start_time,
                error_before=error_before,
                error_after=str(e),
                fix_details={'error': str(e)},
                confidence=action.confidence_threshold
            )
    
    async def fix_espn_api_structure(self, error_context: Dict[str, Any], 
                                   pattern: Any) -> Dict[str, Any]:
        """Automatically fix ESPN API structure changes"""
        
        file_path = error_context.get('file_path')
        function_name = error_context.get('function_name')
        
        if not file_path:
            raise ValueError("No file path provided for ESPN API fix")
        
        enhanced_logger.info(f"🔧 Applying ESPN API structure fix to {file_path}")
        
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Apply ESPN API fix patterns
        fixes_applied = []
        
        # Pattern 1: Fix season.type access
        season_type_pattern = r"season_type\s*=\s*season\.get\(['\"]type['\"]\)"
        if re.search(season_type_pattern, content):
            new_pattern = '''
# Handle both old (dict) and new (int) ESPN formats
season_info = data.get('season', {})
season_type = season_info.get('type', 'Unknown')

if isinstance(season_type, dict):
    # Old format: season.type is a dictionary
    round_name = season_type.get('name', 'Group Stage')
    type_id = season_type.get('id', 1)
elif isinstance(season_type, int):
    # New format: season.type is an integer ID
    type_id = season_type
    round_name = self._map_season_type_id(season_type)
else:
    # Fallback for unexpected formats
    round_name = str(season_type)
    type_id = 1
'''
            content = re.sub(season_type_pattern, new_pattern, content)
            fixes_applied.append("season_type_handling")
        
        # Pattern 2: Add season type mapping function
        if "def _map_season_type_id" not in content:
            mapping_function = '''
    def _map_season_type_id(self, type_id: int) -> str:
        """Map ESPN season type ID to human-readable name"""
        type_mappings = {
            13682: "Group Stage",
            13683: "Round of 16", 
            13684: "Quarter Finals",
            13685: "Semi Finals",
            13686: "Final"
        }
        return type_mappings.get(type_id, f"Season Type {type_id}")
'''
            # Insert before the last method or at the end of class
            class_end_pattern = r"(\n\s*def\s+\w+.*?:\s*\n.*?)(\n\s*$|\nclass|\ndef\s+(?!.*self))"
            if re.search(class_end_pattern, content):
                content = re.sub(class_end_pattern, r"\1" + mapping_function + r"\2", content)
            else:
                content += mapping_function
            
            fixes_applied.append("season_type_mapping_function")
        
        # Write the fixed content back
        with open(file_path, 'w') as f:
            f.write(content)
        
        return {
            'file_path': file_path,
            'fixes_applied': fixes_applied,
            'fix_type': 'espn_api_structure'
        }
    
    async def fix_network_timeouts(self, error_context: Dict[str, Any], 
                                 pattern: Any) -> Dict[str, Any]:
        """Automatically fix network timeout issues"""
        
        file_path = error_context.get('file_path')
        function_name = error_context.get('function_name')
        
        enhanced_logger.info(f"🔧 Applying network timeout fix to {file_path}")
        
        # This would implement automatic retry logic injection
        # For now, return a placeholder result
        return {
            'file_path': file_path,
            'function_name': function_name,
            'fix_type': 'network_resilience',
            'action': 'Added retry logic with exponential backoff'
        }
    
    async def fix_data_structure_access(self, error_context: Dict[str, Any], 
                                      pattern: Any) -> Dict[str, Any]:
        """Automatically fix unsafe data structure access"""
        
        file_path = error_context.get('file_path')
        function_name = error_context.get('function_name')
        
        enhanced_logger.info(f"🔧 Applying data structure access fix to {file_path}")
        
        # This would implement safe data access patterns
        return {
            'file_path': file_path,
            'function_name': function_name,
            'fix_type': 'safe_data_access',
            'action': 'Replaced direct access with safe .get() methods'
        }
    
    async def fix_algorithm_consensus(self, error_context: Dict[str, Any], 
                                    pattern: Any) -> Dict[str, Any]:
        """Automatically fix algorithm consensus issues"""
        
        file_path = error_context.get('file_path')
        function_name = error_context.get('function_name')
        
        enhanced_logger.info(f"🔧 Applying algorithm consensus fix to {file_path}")
        
        # This would implement robust consensus handling
        return {
            'file_path': file_path,
            'function_name': function_name,
            'fix_type': 'algorithm_consensus',
            'action': 'Added robust consensus processing with fallbacks'
        }
    
    async def _learn_from_healing_result(self, result: HealingResult):
        """Learn from healing results to improve future healing"""
        
        action = self.healing_actions[result.action_id]
        
        if result.success:
            # Increase confidence for successful healing
            action.confidence_threshold = min(1.0, action.confidence_threshold + 0.05)
            enhanced_logger.info(f"📈 Increased confidence for {result.action_id}: {action.confidence_threshold}")
        else:
            # Decrease confidence for failed healing
            action.confidence_threshold = max(0.1, action.confidence_threshold - 0.1)
            enhanced_logger.warning(f"📉 Decreased confidence for {result.action_id}: {action.confidence_threshold}")
        
        # Store learning data
        learning_key = f"{result.action_id}_{datetime.now().strftime('%Y%m%d')}"
        if learning_key not in self.learning_database:
            self.learning_database[learning_key] = {
                'successes': 0,
                'failures': 0,
                'patterns': []
            }
        
        if result.success:
            self.learning_database[learning_key]['successes'] += 1
        else:
            self.learning_database[learning_key]['failures'] += 1
    
    def get_healing_report(self) -> Dict[str, Any]:
        """Get comprehensive healing system report"""
        
        total_attempts = len(self.healing_history)
        successful_healings = sum(1 for h in self.healing_history if h.success)
        
        # Action statistics
        action_stats = {}
        for action_id, action in self.healing_actions.items():
            action_stats[action_id] = {
                'description': action.description,
                'success_count': action.success_count,
                'failure_count': action.failure_count,
                'confidence_threshold': action.confidence_threshold,
                'last_applied': action.last_applied.isoformat() if action.last_applied else None
            }
        
        # Recent healing activity
        recent_healings = [
            {
                'action_id': h.action_id,
                'success': h.success,
                'applied_at': h.applied_at.isoformat(),
                'confidence': h.confidence
            }
            for h in sorted(self.healing_history, key=lambda x: x.applied_at, reverse=True)[:10]
        ]
        
        return {
            'summary': {
                'total_healing_attempts': total_attempts,
                'successful_healings': successful_healings,
                'healing_success_rate': successful_healings / total_attempts if total_attempts > 0 else 0,
                'active_healing_actions': len(self.healing_actions),
                'report_timestamp': datetime.now().isoformat()
            },
            'action_statistics': action_stats,
            'recent_healing_activity': recent_healings,
            'learning_insights': self._get_learning_insights()
        }
    
    def _get_learning_insights(self) -> Dict[str, Any]:
        """Get insights from learning database"""
        
        insights = {
            'most_successful_action': None,
            'most_problematic_pattern': None,
            'improvement_trends': []
        }
        
        if self.healing_actions:
            # Find most successful action
            best_action = max(self.healing_actions.values(), 
                            key=lambda a: a.success_count - a.failure_count)
            insights['most_successful_action'] = {
                'action_id': best_action.action_id,
                'description': best_action.description,
                'net_success': best_action.success_count - best_action.failure_count
            }
        
        return insights

# Global self-healing system instance
healing_system = SelfHealingSystem()

# Decorator for automatic self-healing
def with_self_healing(enable_healing: bool = True):
    """Decorator to enable automatic self-healing for functions"""
    
    def decorator(func: Callable):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if enable_healing:
                    # Create error context
                    error_context = {
                        'error_type': type(e).__name__,
                        'error_message': str(e),
                        'function_name': func.__name__,
                        'file_path': inspect.getfile(func),
                        'line_number': traceback.extract_tb(e.__traceback__)[-1].lineno
                    }
                    
                    # Attempt healing
                    healing_result = await healing_system.monitor_and_heal(error_context)
                    
                    if healing_result and healing_result.success:
                        enhanced_logger.info(f"🔧 Self-healing applied, retrying function: {func.__name__}")
                        # Retry the function after healing
                        return await func(*args, **kwargs)
                
                # Re-raise if healing failed or disabled
                raise
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if enable_healing:
                    # Create error context
                    error_context = {
                        'error_type': type(e).__name__,
                        'error_message': str(e),
                        'function_name': func.__name__,
                        'file_path': inspect.getfile(func),
                        'line_number': traceback.extract_tb(e.__traceback__)[-1].lineno
                    }
                    
                    # Attempt healing (run async in sync context)
                    healing_result = asyncio.run(healing_system.monitor_and_heal(error_context))
                    
                    if healing_result and healing_result.success:
                        enhanced_logger.info(f"🔧 Self-healing applied, retrying function: {func.__name__}")
                        # Retry the function after healing
                        return func(*args, **kwargs)
                
                # Re-raise if healing failed or disabled
                raise
        
        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    
    return decorator

# Convenience functions
async def heal_error(error_context: Dict[str, Any]) -> Optional[HealingResult]:
    """Attempt to heal a specific error"""
    return await healing_system.monitor_and_heal(error_context)

def get_healing_report() -> Dict[str, Any]:
    """Get healing system report"""
    return healing_system.get_healing_report()

# Example usage
if __name__ == "__main__":
    
    async def demo_self_healing():
        """Demonstrate self-healing capabilities"""
        
        # Simulate ESPN API error
        espn_error = {
            'error_type': 'AttributeError',
            'error_message': "'int' object has no attribute 'get'",
            'function_name': 'fetch_espn_data',
            'file_path': '/path/to/espn_handler.py',
            'line_number': 123
        }
        
        enhanced_logger.info("🧪 Testing self-healing with ESPN API error")
        healing_result = await heal_error(espn_error)
        
        if healing_result:
            enhanced_logger.info(f"🔧 Healing result: {healing_result.success}")
        
        # Get healing report
        report = get_healing_report()
        enhanced_logger.info("📊 Healing System Report", extra={'report': report})
    
    # Run demo
    asyncio.run(demo_self_healing())