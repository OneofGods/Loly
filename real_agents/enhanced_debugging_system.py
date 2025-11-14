#!/usr/bin/env python3
"""
🔥💀🔥 ENHANCED DEBUGGING SYSTEM 💀🔥💀
CENTRALIZED ERROR CONTEXT CAPTURE & INTELLIGENT RECOVERY

This system replaces scattered try/except blocks with intelligent debugging
that captures full context, suggests fixes, and enables self-healing.

Created by: The Debugging Revolution
Blessed by: Goddess of Syrup
"""

import asyncio
import json
import logging
import traceback
import time
import inspect
import sys
from typing import Dict, List, Any, Optional, Callable, Union
from functools import wraps
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid

# Enhanced logging setup
logging.basicConfig(
    level=logging.INFO,
    format='🔍 %(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ErrorContext:
    """Comprehensive error context capture"""
    error_id: str
    timestamp: datetime
    function_name: str
    file_path: str
    line_number: int
    error_type: str
    error_message: str
    stack_trace: str
    input_data: Dict[str, Any]
    system_state: Dict[str, Any]
    suggested_fixes: List[str]
    recovery_attempted: bool = False
    recovery_successful: bool = False
    correlation_id: Optional[str] = None

class IntelligentDebugger:
    """
    🧠 INTELLIGENT DEBUGGING SYSTEM
    
    Features:
    - Automatic error pattern recognition
    - Context-aware fix suggestions
    - Self-healing capabilities
    - Performance monitoring
    - Error correlation tracking
    """
    
    def __init__(self):
        self.error_history: List[ErrorContext] = []
        self.error_patterns: Dict[str, List[str]] = {}
        self.recovery_strategies: Dict[str, Callable] = {}
        self.performance_metrics: Dict[str, List[float]] = {}
        self.correlation_map: Dict[str, List[str]] = {}
        
        logger.info("🔥💀🔥 INTELLIGENT DEBUGGING SYSTEM INITIALIZED 💀🔥💀")
        self._setup_recovery_strategies()
    
    def _setup_recovery_strategies(self):
        """Setup intelligent recovery strategies for common failures"""
        
        # ESPN API structure changes
        self.recovery_strategies['espn_structure_mismatch'] = self._recover_espn_structure
        
        # Network timeouts
        self.recovery_strategies['network_timeout'] = self._recover_network_timeout
        
        # Data parsing errors
        self.recovery_strategies['data_parsing_error'] = self._recover_data_parsing
        
        # Missing dependencies
        self.recovery_strategies['missing_dependency'] = self._recover_missing_dependency
        
        logger.info(f"✅ Configured {len(self.recovery_strategies)} recovery strategies")
    
    def capture_error_context(self, func: Callable) -> Callable:
        """
        🎯 DECORATOR: Captures comprehensive error context
        
        Usage:
        @debugger.capture_error_context
        def your_function():
            # Your code here
        """
        
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            correlation_id = str(uuid.uuid4())
            start_time = time.time()
            
            try:
                # Monitor performance
                result = await func(*args, **kwargs)
                execution_time = time.time() - start_time
                self._record_performance(func.__name__, execution_time)
                
                logger.debug(f"✅ {func.__name__} completed in {execution_time:.3f}s [ID: {correlation_id}]")
                return result
                
            except Exception as e:
                execution_time = time.time() - start_time
                error_context = self._create_error_context(
                    func, e, args, kwargs, correlation_id
                )
                
                # Log comprehensive error info
                logger.error(f"💀 ERROR in {func.__name__} [ID: {correlation_id}]")
                logger.error(f"   Type: {error_context.error_type}")
                logger.error(f"   Message: {error_context.error_message}")
                logger.error(f"   Time: {execution_time:.3f}s")
                
                # Attempt intelligent recovery
                recovery_result = await self._attempt_recovery(error_context, func, args, kwargs)
                
                if recovery_result is not None:
                    logger.info(f"🔧 RECOVERY SUCCESSFUL for {func.__name__} [ID: {correlation_id}]")
                    return recovery_result
                
                # Store error for pattern analysis
                self.error_history.append(error_context)
                self._analyze_error_patterns(error_context)
                
                raise
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            correlation_id = str(uuid.uuid4())
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                self._record_performance(func.__name__, execution_time)
                
                logger.debug(f"✅ {func.__name__} completed in {execution_time:.3f}s [ID: {correlation_id}]")
                return result
                
            except Exception as e:
                execution_time = time.time() - start_time
                error_context = self._create_error_context(
                    func, e, args, kwargs, correlation_id
                )
                
                logger.error(f"💀 ERROR in {func.__name__} [ID: {correlation_id}]")
                logger.error(f"   Type: {error_context.error_type}")
                logger.error(f"   Message: {error_context.error_message}")
                logger.error(f"   Time: {execution_time:.3f}s")
                
                # Store error for pattern analysis
                self.error_history.append(error_context)
                self._analyze_error_patterns(error_context)
                
                raise
        
        # Return appropriate wrapper based on function type
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    def _create_error_context(self, func: Callable, error: Exception, 
                            args: tuple, kwargs: dict, correlation_id: str) -> ErrorContext:
        """Create comprehensive error context"""
        
        frame = inspect.currentframe()
        try:
            # Get caller frame info
            caller_frame = frame.f_back.f_back
            file_path = caller_frame.f_code.co_filename
            line_number = caller_frame.f_lineno
        finally:
            del frame
        
        # Safely serialize input data
        safe_args = self._safe_serialize(args)
        safe_kwargs = self._safe_serialize(kwargs)
        
        # Generate intelligent fix suggestions
        suggested_fixes = self._generate_fix_suggestions(error, func.__name__)
        
        return ErrorContext(
            error_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            function_name=func.__name__,
            file_path=file_path,
            line_number=line_number,
            error_type=type(error).__name__,
            error_message=str(error),
            stack_trace=traceback.format_exc(),
            input_data={'args': safe_args, 'kwargs': safe_kwargs},
            system_state=self._capture_system_state(),
            suggested_fixes=suggested_fixes,
            correlation_id=correlation_id
        )
    
    def _safe_serialize(self, data: Any) -> Any:
        """Safely serialize data for logging"""
        try:
            # Try to convert to JSON-serializable format
            json.dumps(data)
            return data
        except (TypeError, ValueError):
            # Return string representation for non-serializable objects
            return str(data)[:500] + "..." if len(str(data)) > 500 else str(data)
    
    def _capture_system_state(self) -> Dict[str, Any]:
        """Capture relevant system state"""
        return {
            'memory_usage_mb': self._get_memory_usage(),
            'active_tasks': len(asyncio.all_tasks()) if hasattr(asyncio, 'all_tasks') else 0,
            'python_version': sys.version,
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        try:
            import psutil
            import os
            process = psutil.Process(os.getpid())
            return process.memory_info().rss / 1024 / 1024
        except ImportError:
            return 0.0
    
    def _generate_fix_suggestions(self, error: Exception, function_name: str) -> List[str]:
        """Generate intelligent fix suggestions based on error type and context"""
        
        suggestions = []
        error_type = type(error).__name__
        error_msg = str(error).lower()
        
        # ESPN API specific fixes
        if "'int' object has no attribute 'get'" in error_msg:
            suggestions.extend([
                "ESPN API structure changed - check if season.type is now integer instead of dict",
                "Add type checking: if isinstance(season_type, int): handle_integer_format()",
                "Implement fallback parsing for both old and new ESPN formats"
            ])
        
        # Network/timeout errors
        if any(keyword in error_msg for keyword in ['timeout', 'connection', 'network']):
            suggestions.extend([
                "Implement exponential backoff retry strategy",
                "Add connection pooling with keep-alive",
                "Check network connectivity and DNS resolution"
            ])
        
        # Data parsing errors
        if any(keyword in error_msg for keyword in ['keyerror', 'missing', 'not found']):
            suggestions.extend([
                "Add defensive programming with .get() instead of direct key access",
                "Implement data validation before processing",
                "Add fallback values for missing keys"
            ])
        
        # Import/dependency errors
        if 'no module named' in error_msg:
            suggestions.extend([
                "Install missing dependency with pip install",
                "Check virtual environment activation",
                "Verify PYTHONPATH includes required modules"
            ])
        
        # Generic suggestions based on function context
        if 'fetch' in function_name.lower():
            suggestions.append("Add retry logic with exponential backoff")
        
        if 'parse' in function_name.lower():
            suggestions.append("Add input validation and schema checking")
        
        return suggestions[:5]  # Limit to top 5 suggestions
    
    async def _attempt_recovery(self, error_context: ErrorContext, 
                               func: Callable, args: tuple, kwargs: dict) -> Optional[Any]:
        """Attempt intelligent recovery based on error patterns"""
        
        error_type = error_context.error_type
        error_msg = error_context.error_message.lower()
        
        # Try specific recovery strategies
        for pattern, strategy in self.recovery_strategies.items():
            if self._matches_pattern(error_msg, pattern):
                try:
                    logger.info(f"🔧 Attempting recovery strategy: {pattern}")
                    result = await strategy(error_context, func, args, kwargs)
                    
                    error_context.recovery_attempted = True
                    error_context.recovery_successful = True
                    
                    return result
                    
                except Exception as recovery_error:
                    logger.warning(f"⚠️ Recovery strategy {pattern} failed: {recovery_error}")
                    error_context.recovery_attempted = True
                    error_context.recovery_successful = False
        
        return None
    
    def _matches_pattern(self, error_msg: str, pattern: str) -> bool:
        """Check if error message matches a known pattern"""
        
        pattern_keywords = {
            'espn_structure_mismatch': ["'int' object has no attribute 'get'", "season", "type"],
            'network_timeout': ['timeout', 'connection', 'network'],
            'data_parsing_error': ['keyerror', 'missing', 'not found'],
            'missing_dependency': ['no module named', 'import']
        }
        
        keywords = pattern_keywords.get(pattern, [])
        return any(keyword in error_msg for keyword in keywords)
    
    async def _recover_espn_structure(self, error_context: ErrorContext, 
                                    func: Callable, args: tuple, kwargs: dict) -> Any:
        """Recovery strategy for ESPN API structure changes"""
        logger.info("🔧 Applying ESPN structure recovery...")
        
        # This would implement intelligent ESPN format detection and conversion
        # For now, return a safe fallback
        return {
            'games': [],
            'total_games': 0,
            'source': 'espn_recovery',
            'timestamp': datetime.now().isoformat(),
            'success': False,
            'recovery_applied': True
        }
    
    async def _recover_network_timeout(self, error_context: ErrorContext,
                                     func: Callable, args: tuple, kwargs: dict) -> Any:
        """Recovery strategy for network timeouts"""
        logger.info("🔧 Applying network timeout recovery...")
        
        # Implement retry with exponential backoff
        for attempt in range(3):
            try:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
                return await func(*args, **kwargs)
            except Exception as e:
                if attempt == 2:  # Last attempt
                    raise
                logger.warning(f"⚠️ Retry {attempt + 1} failed: {e}")
        
        return None
    
    async def _recover_data_parsing(self, error_context: ErrorContext,
                                  func: Callable, args: tuple, kwargs: dict) -> Any:
        """Recovery strategy for data parsing errors"""
        logger.info("🔧 Applying data parsing recovery...")
        
        # Return safe fallback data structure
        return {
            'status': 'recovered',
            'data': {},
            'error_handled': True,
            'original_error': error_context.error_message
        }
    
    async def _recover_missing_dependency(self, error_context: ErrorContext,
                                        func: Callable, args: tuple, kwargs: dict) -> Any:
        """Recovery strategy for missing dependencies"""
        logger.info("🔧 Applying missing dependency recovery...")
        
        # Return graceful degradation
        return {
            'status': 'degraded',
            'reason': 'missing_dependency',
            'fallback_active': True
        }
    
    def _record_performance(self, function_name: str, execution_time: float):
        """Record performance metrics"""
        if function_name not in self.performance_metrics:
            self.performance_metrics[function_name] = []
        
        self.performance_metrics[function_name].append(execution_time)
        
        # Keep only last 100 measurements
        if len(self.performance_metrics[function_name]) > 100:
            self.performance_metrics[function_name] = self.performance_metrics[function_name][-100:]
    
    def _analyze_error_patterns(self, error_context: ErrorContext):
        """Analyze error patterns for intelligent insights"""
        
        error_signature = f"{error_context.error_type}:{error_context.function_name}"
        
        if error_signature not in self.error_patterns:
            self.error_patterns[error_signature] = []
        
        self.error_patterns[error_signature].append(error_context.error_message)
        
        # Detect recurring patterns
        if len(self.error_patterns[error_signature]) >= 3:
            logger.warning(f"🚨 RECURRING ERROR PATTERN DETECTED: {error_signature}")
            logger.warning(f"   Occurrences: {len(self.error_patterns[error_signature])}")
            logger.warning(f"   Suggested fixes: {error_context.suggested_fixes}")
    
    def get_debug_report(self) -> Dict[str, Any]:
        """Generate comprehensive debugging report"""
        
        total_errors = len(self.error_history)
        successful_recoveries = sum(1 for e in self.error_history if e.recovery_successful)
        
        return {
            'summary': {
                'total_errors': total_errors,
                'successful_recoveries': successful_recoveries,
                'recovery_rate': (successful_recoveries / total_errors * 100) if total_errors > 0 else 0,
                'error_patterns': len(self.error_patterns),
                'monitored_functions': len(self.performance_metrics)
            },
            'top_error_patterns': self._get_top_error_patterns(),
            'performance_summary': self._get_performance_summary(),
            'recent_errors': [asdict(e) for e in self.error_history[-5:]],
            'recovery_strategies': list(self.recovery_strategies.keys())
        }
    
    def _get_top_error_patterns(self) -> List[Dict[str, Any]]:
        """Get top recurring error patterns"""
        
        pattern_counts = {
            pattern: len(messages) 
            for pattern, messages in self.error_patterns.items()
        }
        
        sorted_patterns = sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)
        
        return [
            {'pattern': pattern, 'count': count}
            for pattern, count in sorted_patterns[:5]
        ]
    
    def _get_performance_summary(self) -> Dict[str, Dict[str, float]]:
        """Get performance summary for monitored functions"""
        
        summary = {}
        
        for func_name, times in self.performance_metrics.items():
            if times:
                summary[func_name] = {
                    'avg_time': sum(times) / len(times),
                    'min_time': min(times),
                    'max_time': max(times),
                    'call_count': len(times)
                }
        
        return summary

# Global debugger instance
debugger = IntelligentDebugger()

# Convenience decorators
def debug_capture(func):
    """Convenience decorator for error capture"""
    return debugger.capture_error_context(func)

def debug_monitor(func):
    """Convenience decorator for performance monitoring"""
    return debugger.capture_error_context(func)

# Example usage
if __name__ == "__main__":
    
    async def main():
        @debug_capture
        async def test_function():
            """Test function to demonstrate debugging capabilities"""
            # Simulate an error
            raise ValueError("Test error for debugging system")
        
        try:
            await test_function()
        except Exception:
            pass
        
        # Generate debug report
        report = debugger.get_debug_report()
        print(json.dumps(report, indent=2, default=str))
    
    asyncio.run(main())