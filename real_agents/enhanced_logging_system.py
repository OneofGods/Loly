#!/usr/bin/env python3
"""
📊💀📊 ENHANCED LOGGING SYSTEM 💀📊💀
STRUCTURED DEBUGGING WITH CORRELATION IDS

Advanced logging system with correlation tracking, structured data,
performance metrics, and intelligent log analysis.

Created by: The AI Debugging Revolution  
Blessed by: Goddess of Syrup
"""

import asyncio
import json
import logging
import time
import uuid
import threading
from typing import Dict, List, Any, Optional, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from contextlib import contextmanager
from functools import wraps
import traceback
import sys
import os

# Thread-local storage for correlation IDs
_local = threading.local()

@dataclass
class LogContext:
    """Structured log context with correlation tracking"""
    correlation_id: str
    session_id: str
    user_id: Optional[str] = None
    request_id: Optional[str] = None
    operation: Optional[str] = None
    component: Optional[str] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

@dataclass
class PerformanceMetrics:
    """Performance tracking for operations"""
    operation: str
    start_time: float
    end_time: Optional[float] = None
    duration_ms: Optional[float] = None
    memory_usage_mb: Optional[float] = None
    cpu_usage_percent: Optional[float] = None
    success: bool = True
    error_details: Optional[str] = None

class StructuredLogger:
    """
    🔍 ENHANCED STRUCTURED LOGGER
    
    Features:
    - Correlation ID tracking across operations
    - Structured JSON logging with metadata
    - Performance metrics collection
    - Error context capture
    - Log aggregation and analysis
    - Real-time debugging insights
    """
    
    def __init__(self, name: str = "enhanced_logger"):
        self.logger = logging.getLogger(name)
        self.performance_metrics: List[PerformanceMetrics] = []
        self.error_patterns: Dict[str, int] = {}
        self.session_id = str(uuid.uuid4())
        
        # Configure structured logging
        self._setup_structured_logging()
        
        # Initialize correlation tracking
        self._correlation_stack: List[str] = []
        
        self.logger.info("📊💀📊 ENHANCED LOGGING SYSTEM INITIALIZED 💀📊💀", 
                        extra=self._get_base_context())
    
    def _setup_structured_logging(self):
        """Setup structured JSON logging format"""
        
        class StructuredFormatter(logging.Formatter):
            def format(self, record):
                # Base log structure
                log_entry = {
                    'timestamp': datetime.utcnow().isoformat(),
                    'level': record.levelname,
                    'logger': record.name,
                    'message': record.getMessage(),
                    'module': record.module,
                    'function': record.funcName,
                    'line': record.lineno
                }
                
                # Add correlation context if available
                if hasattr(record, 'correlation_id'):
                    log_entry['correlation_id'] = record.correlation_id
                if hasattr(record, 'session_id'):
                    log_entry['session_id'] = record.session_id
                if hasattr(record, 'operation'):
                    log_entry['operation'] = record.operation
                if hasattr(record, 'component'):
                    log_entry['component'] = record.component
                if hasattr(record, 'metadata'):
                    log_entry['metadata'] = record.metadata
                
                # Add performance metrics if available
                if hasattr(record, 'duration_ms'):
                    log_entry['duration_ms'] = record.duration_ms
                if hasattr(record, 'memory_usage_mb'):
                    log_entry['memory_usage_mb'] = record.memory_usage_mb
                
                # Add error details if present
                if record.exc_info:
                    log_entry['exception'] = {
                        'type': record.exc_info[0].__name__,
                        'message': str(record.exc_info[1]),
                        'traceback': traceback.format_exception(*record.exc_info)
                    }
                
                return json.dumps(log_entry, default=str)
        
        # Setup handler with structured formatter
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter())
        
        # Clear existing handlers and add structured handler
        self.logger.handlers.clear()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    
    def _get_base_context(self) -> Dict[str, Any]:
        """Get base logging context"""
        return {
            'session_id': self.session_id,
            'correlation_id': self.get_correlation_id(),
            'timestamp': datetime.utcnow().isoformat()
        }
    
    def get_correlation_id(self) -> str:
        """Get current correlation ID"""
        if hasattr(_local, 'correlation_id'):
            return _local.correlation_id
        return str(uuid.uuid4())
    
    def set_correlation_id(self, correlation_id: str):
        """Set correlation ID for current thread"""
        _local.correlation_id = correlation_id
    
    def generate_correlation_id(self) -> str:
        """Generate new correlation ID"""
        correlation_id = str(uuid.uuid4())
        self.set_correlation_id(correlation_id)
        return correlation_id
    
    @contextmanager
    def correlation_context(self, operation: str, component: str = None, 
                          metadata: Dict[str, Any] = None):
        """Context manager for correlation tracking"""
        
        correlation_id = self.generate_correlation_id()
        
        # Store previous context
        previous_operation = getattr(_local, 'operation', None)
        previous_component = getattr(_local, 'component', None)
        previous_metadata = getattr(_local, 'metadata', {})
        
        # Set new context
        _local.operation = operation
        _local.component = component or 'unknown'
        _local.metadata = metadata or {}
        
        start_time = time.time()
        
        try:
            self.info(f"🚀 Starting operation: {operation}", 
                     extra={'operation_start': True})
            yield correlation_id
            
        except Exception as e:
            self.error(f"💥 Operation failed: {operation}", 
                      extra={'operation_error': True}, exc_info=True)
            raise
            
        finally:
            duration_ms = (time.time() - start_time) * 1000
            self.info(f"✅ Completed operation: {operation}", 
                     extra={
                         'operation_end': True,
                         'duration_ms': duration_ms
                     })
            
            # Restore previous context
            _local.operation = previous_operation
            _local.component = previous_component
            _local.metadata = previous_metadata
    
    def _log_with_context(self, level: str, message: str, 
                         extra: Dict[str, Any] = None, **kwargs):
        """Log with full context information"""
        
        log_extra = self._get_base_context()
        
        # Add current thread context
        if hasattr(_local, 'operation'):
            log_extra['operation'] = _local.operation
        if hasattr(_local, 'component'):
            log_extra['component'] = _local.component
        if hasattr(_local, 'metadata'):
            log_extra['metadata'] = _local.metadata
        
        # Merge additional context
        if extra:
            log_extra.update(extra)
        
        # Log at appropriate level
        getattr(self.logger, level.lower())(message, extra=log_extra, **kwargs)
    
    def debug(self, message: str, extra: Dict[str, Any] = None, **kwargs):
        """Debug level logging with context"""
        self._log_with_context('DEBUG', message, extra, **kwargs)
    
    def info(self, message: str, extra: Dict[str, Any] = None, **kwargs):
        """Info level logging with context"""
        self._log_with_context('INFO', message, extra, **kwargs)
    
    def warning(self, message: str, extra: Dict[str, Any] = None, **kwargs):
        """Warning level logging with context"""
        self._log_with_context('WARNING', message, extra, **kwargs)
    
    def error(self, message: str, extra: Dict[str, Any] = None, **kwargs):
        """Error level logging with context"""
        self._log_with_context('ERROR', message, extra, **kwargs)
        
        # Track error patterns
        error_key = f"{getattr(_local, 'operation', 'unknown')}:{message[:50]}"
        self.error_patterns[error_key] = self.error_patterns.get(error_key, 0) + 1
    
    def critical(self, message: str, extra: Dict[str, Any] = None, **kwargs):
        """Critical level logging with context"""
        self._log_with_context('CRITICAL', message, extra, **kwargs)
    
    @contextmanager
    def performance_tracking(self, operation: str):
        """Context manager for performance tracking"""
        
        metrics = PerformanceMetrics(
            operation=operation,
            start_time=time.time()
        )
        
        try:
            self.debug(f"📊 Performance tracking started: {operation}")
            yield metrics
            
            metrics.success = True
            
        except Exception as e:
            metrics.success = False
            metrics.error_details = str(e)
            raise
            
        finally:
            metrics.end_time = time.time()
            metrics.duration_ms = (metrics.end_time - metrics.start_time) * 1000
            
            self.performance_metrics.append(metrics)
            
            # Log performance summary
            self.info(f"⏱️ Performance: {operation}", extra={
                'performance_metrics': {
                    'duration_ms': metrics.duration_ms,
                    'success': metrics.success,
                    'error_details': metrics.error_details
                }
            })
    
    def log_api_call(self, url: str, method: str = 'GET', 
                    status_code: Optional[int] = None,
                    response_time_ms: Optional[float] = None,
                    error: Optional[str] = None):
        """Log API call with structured data"""
        
        api_data = {
            'api_call': {
                'url': url,
                'method': method,
                'status_code': status_code,
                'response_time_ms': response_time_ms,
                'error': error,
                'success': error is None and (status_code is None or 200 <= status_code < 300)
            }
        }
        
        if error:
            self.error(f"🌐 API call failed: {method} {url}", extra=api_data)
        else:
            self.info(f"🌐 API call: {method} {url}", extra=api_data)
    
    def log_data_processing(self, operation: str, input_count: int, 
                          output_count: int, processing_time_ms: float,
                          errors: List[str] = None):
        """Log data processing operations"""
        
        processing_data = {
            'data_processing': {
                'operation': operation,
                'input_count': input_count,
                'output_count': output_count,
                'processing_time_ms': processing_time_ms,
                'success_rate': output_count / input_count if input_count > 0 else 0,
                'errors': errors or []
            }
        }
        
        if errors:
            self.warning(f"📊 Data processing with errors: {operation}", extra=processing_data)
        else:
            self.info(f"📊 Data processing: {operation}", extra=processing_data)
    
    def get_performance_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get performance summary for recent operations"""
        
        cutoff_time = time.time() - (hours * 3600)
        recent_metrics = [m for m in self.performance_metrics if m.start_time >= cutoff_time]
        
        if not recent_metrics:
            return {'message': 'No recent performance data'}
        
        # Calculate statistics
        total_operations = len(recent_metrics)
        successful_operations = sum(1 for m in recent_metrics if m.success)
        failed_operations = total_operations - successful_operations
        
        durations = [m.duration_ms for m in recent_metrics if m.duration_ms]
        avg_duration = sum(durations) / len(durations) if durations else 0
        max_duration = max(durations) if durations else 0
        min_duration = min(durations) if durations else 0
        
        # Operation breakdown
        operation_stats = {}
        for metric in recent_metrics:
            op = metric.operation
            if op not in operation_stats:
                operation_stats[op] = {'count': 0, 'success': 0, 'avg_duration': 0}
            
            operation_stats[op]['count'] += 1
            if metric.success:
                operation_stats[op]['success'] += 1
            if metric.duration_ms:
                operation_stats[op]['avg_duration'] = (
                    operation_stats[op]['avg_duration'] + metric.duration_ms
                ) / 2
        
        return {
            'summary': {
                'total_operations': total_operations,
                'successful_operations': successful_operations,
                'failed_operations': failed_operations,
                'success_rate': successful_operations / total_operations,
                'avg_duration_ms': avg_duration,
                'max_duration_ms': max_duration,
                'min_duration_ms': min_duration
            },
            'operation_breakdown': operation_stats,
            'error_patterns': dict(sorted(self.error_patterns.items(), 
                                        key=lambda x: x[1], reverse=True)[:10])
        }

# Global logger instance
enhanced_logger = StructuredLogger("enhanced_system")

# Decorator for automatic correlation tracking
def with_correlation(operation: str = None, component: str = None):
    """Decorator to automatically add correlation tracking to functions"""
    
    def decorator(func: Callable):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            op_name = operation or f"{func.__module__}.{func.__name__}"
            comp_name = component or func.__module__.split('.')[-1]
            
            with enhanced_logger.correlation_context(op_name, comp_name):
                with enhanced_logger.performance_tracking(op_name):
                    return await func(*args, **kwargs)
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            op_name = operation or f"{func.__module__}.{func.__name__}"
            comp_name = component or func.__module__.split('.')[-1]
            
            with enhanced_logger.correlation_context(op_name, comp_name):
                with enhanced_logger.performance_tracking(op_name):
                    return func(*args, **kwargs)
        
        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    
    return decorator

# Convenience functions
def get_logger(name: str = None) -> StructuredLogger:
    """Get enhanced logger instance"""
    if name:
        return StructuredLogger(name)
    return enhanced_logger

def log_debug(message: str, **kwargs):
    """Quick debug logging"""
    enhanced_logger.debug(message, **kwargs)

def log_info(message: str, **kwargs):
    """Quick info logging"""
    enhanced_logger.info(message, **kwargs)

def log_warning(message: str, **kwargs):
    """Quick warning logging"""
    enhanced_logger.warning(message, **kwargs)

def log_error(message: str, **kwargs):
    """Quick error logging"""
    enhanced_logger.error(message, **kwargs)

def log_api_call(url: str, method: str = 'GET', **kwargs):
    """Quick API call logging"""
    enhanced_logger.log_api_call(url, method, **kwargs)

def get_performance_report(hours: int = 24) -> Dict[str, Any]:
    """Get performance report"""
    return enhanced_logger.get_performance_summary(hours)

# Example usage and integration
if __name__ == "__main__":
    
    async def demo_enhanced_logging():
        """Demonstrate enhanced logging capabilities"""
        
        # Example 1: Correlation context
        with enhanced_logger.correlation_context("demo_operation", "demo_component"):
            enhanced_logger.info("🎯 Starting demo operation")
            
            # Simulate API call
            enhanced_logger.log_api_call("https://api.example.com/data", "GET", 
                                       status_code=200, response_time_ms=150)
            
            # Simulate data processing
            enhanced_logger.log_data_processing("data_transformation", 100, 95, 250.5,
                                              errors=["Invalid record at index 42"])
            
            enhanced_logger.info("✅ Demo operation completed")
        
        # Example 2: Performance tracking
        with enhanced_logger.performance_tracking("complex_calculation"):
            await asyncio.sleep(0.1)  # Simulate work
            enhanced_logger.debug("🔢 Complex calculation in progress")
        
        # Example 3: Error handling with context
        try:
            raise ValueError("Demo error for testing")
        except Exception as e:
            enhanced_logger.error("💥 Demo error occurred", exc_info=True)
        
        # Get performance summary
        summary = enhanced_logger.get_performance_summary(1)
        enhanced_logger.info("📊 Performance Summary", extra={'summary': summary})
    
    # Run demo
    asyncio.run(demo_enhanced_logging())