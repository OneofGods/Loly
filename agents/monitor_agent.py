#!/usr/bin/env python3
"""
🔥💀 MONITOR AGENT - AUTONOMOUS SYSTEM HEALTH TRACKING 💀🔥
Agent Poly Loly Double Zero: Specialized Monitoring Intelligence

AUTONOMOUS BEHAVIORS:
- Independent system health monitoring
- Proactive alert generation and escalation
- Adaptive threshold adjustment
- Real-time performance tracking
- Self-healing system recovery
"""

import asyncio
import json
import time
import psutil
import platform
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import logging
from collections import defaultdict, deque
from enum import Enum
import numpy as np
import socket
import subprocess
import os

from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY

logger = logging.getLogger(__name__)

class AlertSeverity(Enum):
    """🚨 Alert severity levels"""
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    EMERGENCY = 5

class HealthStatus(Enum):
    """💚 Health status levels"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    CRITICAL = "critical"
    OFFLINE = "offline"

class SystemAlert:
    """🚨 System alert representation"""
    def __init__(self, alert_id: str, alert_type: str, severity: AlertSeverity,
                 message: str, source: str, details: Dict[str, Any]):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.severity = severity
        self.message = message
        self.source = source
        self.details = details
        
        # Alert lifecycle
        self.created_time = datetime.now()
        self.acknowledged_time = None
        self.resolved_time = None
        self.escalated = False
        
        # Alert state
        self.status = "active"
        self.assigned_to = None
        self.resolution_notes = ""

class HealthMetric:
    """📊 Health metric tracking"""
    def __init__(self, metric_name: str, metric_type: str, unit: str):
        self.metric_name = metric_name
        self.metric_type = metric_type  # 'gauge', 'counter', 'histogram'
        self.unit = unit
        
        # Metric data
        self.current_value = 0.0
        self.values = deque(maxlen=1000)  # Last 1000 readings
        self.timestamps = deque(maxlen=1000)
        
        # Thresholds
        self.warning_threshold = None
        self.critical_threshold = None
        self.threshold_direction = 'above'  # 'above' or 'below'
        
        # Statistics
        self.min_value = float('inf')
        self.max_value = float('-inf')
        self.avg_value = 0.0
        self.std_deviation = 0.0

class MonitorAgent(AutonomousAgent):
    """
    🎯 AUTONOMOUS MONITORING AGENT
    
    Specializes in:
    - System resource monitoring (CPU, Memory, Disk, Network)
    - Agent health and performance tracking
    - Application-specific metrics monitoring
    - Alert generation and management
    - Automated recovery and self-healing
    """
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        super().__init__(agent_id, config)
        
        # System monitoring configuration
        self.system_monitors = {
            'cpu': {'enabled': True, 'interval': 5, 'warning': 80, 'critical': 95},
            'memory': {'enabled': True, 'interval': 5, 'warning': 85, 'critical': 95},
            'disk': {'enabled': True, 'interval': 30, 'warning': 80, 'critical': 90},
            'network': {'enabled': True, 'interval': 10, 'warning': None, 'critical': None},
            'processes': {'enabled': True, 'interval': 15, 'warning': None, 'critical': None}
        }
        
        # Agent monitoring configuration
        self.agent_monitors = {
            'heartbeat': {'enabled': True, 'interval': 10, 'timeout': 30},
            'performance': {'enabled': True, 'interval': 30, 'degradation_threshold': 0.2},
            'errors': {'enabled': True, 'interval': 5, 'error_rate_threshold': 0.1},
            'resource_usage': {'enabled': True, 'interval': 15, 'memory_limit': 500}  # MB
        }
        
        # Application monitoring
        self.application_monitors = {
            'sports_data_freshness': {'enabled': True, 'interval': 60, 'max_age': 300},
            'prediction_accuracy': {'enabled': True, 'interval': 300, 'min_accuracy': 0.6},
            'workflow_completion': {'enabled': True, 'interval': 120, 'max_duration': 3600},
            'api_endpoints': {'enabled': True, 'interval': 30, 'timeout': 10}
        }
        
        # Monitoring state
        self.health_metrics = {}  # metric_name -> HealthMetric
        self.active_alerts = {}  # alert_id -> SystemAlert
        self.alert_history = deque(maxlen=5000)  # Alert history
        self.monitored_agents = {}  # agent_id -> agent_info
        self.system_health = HealthStatus.HEALTHY
        
        # Alert management
        self.alert_escalation_rules = {
            AlertSeverity.WARNING: {'escalate_after': 300, 'notify': ['coordinator']},
            AlertSeverity.ERROR: {'escalate_after': 180, 'notify': ['coordinator', 'admin']},
            AlertSeverity.CRITICAL: {'escalate_after': 60, 'notify': ['all']},
            AlertSeverity.EMERGENCY: {'escalate_after': 30, 'notify': ['all', 'external']}
        }
        
        # Recovery actions
        self.recovery_actions = {
            'high_memory_usage': self._recover_high_memory,
            'high_cpu_usage': self._recover_high_cpu,
            'agent_unresponsive': self._recover_unresponsive_agent,
            'disk_space_low': self._recover_disk_space,
            'network_issues': self._recover_network_issues
        }
        
        # Performance tracking
        self.monitoring_metrics = {
            'alerts_generated': 0,
            'alerts_resolved': 0,
            'recovery_actions_taken': 0,
            'system_uptime': time.time(),
            'monitoring_accuracy': 0.95,
            'false_positive_rate': 0.05
        }
        
        logger.info(f"🎯 MonitorAgent {self.agent_id} initialized with comprehensive monitoring")
    
    async def _initialize_systems(self):
        """⚙️ Initialize monitoring systems"""
        # Initialize health metrics
        await self._initialize_health_metrics()
        
        # Start monitoring loops
        asyncio.create_task(self._system_monitoring_loop())
        asyncio.create_task(self._agent_monitoring_loop())
        asyncio.create_task(self._application_monitoring_loop())
        asyncio.create_task(self._alert_management_loop())
        
        # Subscribe to system events
        await self.send_message('*', 'subscribe', {
            'agent_id': self.agent_id,
            'message_types': ['agent_spawned', 'agent_terminated', 'system_event', 'health_check']
        })
        
        # Start baseline monitoring
        await self._establish_baselines()
        
        logger.info("⚙️ Monitoring systems initialized")
    
    async def _agent_behavior(self):
        """🎯 Core monitoring autonomous behavior"""
        # Process pending health checks
        await self._process_health_checks()
        
        # Update system health status
        await self._update_system_health()
        
        # Check for alert escalations
        await self._check_alert_escalations()
        
        # Perform proactive health analysis
        await self._proactive_health_analysis()
        
        # Clean up resolved alerts
        await self._cleanup_resolved_alerts()
        
        await asyncio.sleep(1)
    
    async def _agent_specific_adaptation(self):
        """🧠 Adapt monitoring strategies based on system behavior"""
        # Analyze alert patterns
        recent_alerts = [
            alert for alert in self.alert_history 
            if alert.created_time > datetime.now() - timedelta(hours=1)
        ]
        
        if len(recent_alerts) > 10:
            # High alert volume - adapt thresholds to reduce noise
            await self._adapt_thresholds_for_noise_reduction()
            logger.info("🧠 Adapted thresholds to reduce alert noise")
            
        elif len(recent_alerts) < 2:
            # Low alert volume - might be missing issues
            await self._adapt_thresholds_for_sensitivity()
            logger.info("🧠 Adapted thresholds for higher sensitivity")
        
        # Adapt monitoring intervals based on system load
        system_load = psutil.cpu_percent()
        if system_load > 80:
            # High load - reduce monitoring frequency
            await self._adapt_monitoring_intervals(factor=1.5)
        elif system_load < 20:
            # Low load - can increase monitoring frequency
            await self._adapt_monitoring_intervals(factor=0.8)
        
        # Learn from recovery action success rates
        await self._adapt_recovery_strategies()
    
    async def _initialize_health_metrics(self):
        """📊 Initialize health metrics tracking"""
        # System metrics
        self.health_metrics['cpu_usage'] = HealthMetric('cpu_usage', 'gauge', '%')
        self.health_metrics['cpu_usage'].warning_threshold = 80
        self.health_metrics['cpu_usage'].critical_threshold = 95
        
        self.health_metrics['memory_usage'] = HealthMetric('memory_usage', 'gauge', '%')
        self.health_metrics['memory_usage'].warning_threshold = 85
        self.health_metrics['memory_usage'].critical_threshold = 95
        
        self.health_metrics['disk_usage'] = HealthMetric('disk_usage', 'gauge', '%')
        self.health_metrics['disk_usage'].warning_threshold = 80
        self.health_metrics['disk_usage'].critical_threshold = 90
        
        self.health_metrics['network_connections'] = HealthMetric('network_connections', 'gauge', 'count')
        
        # Agent metrics
        self.health_metrics['active_agents'] = HealthMetric('active_agents', 'gauge', 'count')
        self.health_metrics['agent_errors'] = HealthMetric('agent_errors', 'counter', 'count')
        self.health_metrics['task_completion_rate'] = HealthMetric('task_completion_rate', 'gauge', '%')
        
        # Application metrics
        self.health_metrics['prediction_accuracy'] = HealthMetric('prediction_accuracy', 'gauge', '%')
        self.health_metrics['prediction_accuracy'].warning_threshold = 60
        self.health_metrics['prediction_accuracy'].critical_threshold = 40
        self.health_metrics['prediction_accuracy'].threshold_direction = 'below'
        
        self.health_metrics['data_freshness'] = HealthMetric('data_freshness', 'gauge', 'seconds')
        self.health_metrics['data_freshness'].warning_threshold = 300
        self.health_metrics['data_freshness'].critical_threshold = 600
        
        logger.info("📊 Initialized health metrics tracking")
    
    async def _system_monitoring_loop(self):
        """💻 System resource monitoring loop"""
        while self.state != 'terminated':
            try:
                if self.system_monitors['cpu']['enabled']:
                    await self._monitor_cpu_usage()
                
                if self.system_monitors['memory']['enabled']:
                    await self._monitor_memory_usage()
                
                if self.system_monitors['disk']['enabled']:
                    await self._monitor_disk_usage()
                
                if self.system_monitors['network']['enabled']:
                    await self._monitor_network_usage()
                
                if self.system_monitors['processes']['enabled']:
                    await self._monitor_processes()
                
                await asyncio.sleep(5)  # Base monitoring interval
                
            except Exception as e:
                logger.error(f"❌ System monitoring error: {e}")
                await asyncio.sleep(10)
    
    async def _agent_monitoring_loop(self):
        """🤖 Agent health monitoring loop"""
        while self.state != 'terminated':
            try:
                if self.agent_monitors['heartbeat']['enabled']:
                    await self._monitor_agent_heartbeats()
                
                if self.agent_monitors['performance']['enabled']:
                    await self._monitor_agent_performance()
                
                if self.agent_monitors['errors']['enabled']:
                    await self._monitor_agent_errors()
                
                if self.agent_monitors['resource_usage']['enabled']:
                    await self._monitor_agent_resources()
                
                await asyncio.sleep(15)  # Agent monitoring interval
                
            except Exception as e:
                logger.error(f"❌ Agent monitoring error: {e}")
                await asyncio.sleep(15)
    
    async def _application_monitoring_loop(self):
        """📱 Application-specific monitoring loop"""
        while self.state != 'terminated':
            try:
                if self.application_monitors['sports_data_freshness']['enabled']:
                    await self._monitor_sports_data_freshness()
                
                if self.application_monitors['prediction_accuracy']['enabled']:
                    await self._monitor_prediction_accuracy()
                
                if self.application_monitors['workflow_completion']['enabled']:
                    await self._monitor_workflow_completion()
                
                if self.application_monitors['api_endpoints']['enabled']:
                    await self._monitor_api_endpoints()
                
                await asyncio.sleep(60)  # Application monitoring interval
                
            except Exception as e:
                logger.error(f"❌ Application monitoring error: {e}")
                await asyncio.sleep(60)
    
    async def _alert_management_loop(self):
        """🚨 Alert management and escalation loop"""
        while self.state != 'terminated':
            try:
                await self._process_alert_escalations()
                await self._check_alert_resolutions()
                await self._update_alert_statistics()
                
                await asyncio.sleep(30)  # Alert management interval
                
            except Exception as e:
                logger.error(f"❌ Alert management error: {e}")
                await asyncio.sleep(30)
    
    async def _monitor_cpu_usage(self):
        """🖥️ Monitor CPU usage"""
        cpu_percent = psutil.cpu_percent(interval=1)
        await self._update_metric('cpu_usage', cpu_percent)
        
        # Check thresholds
        if cpu_percent > self.system_monitors['cpu']['critical']:
            await self._generate_alert(
                'high_cpu_usage', AlertSeverity.CRITICAL,
                f"Critical CPU usage: {cpu_percent:.1f}%",
                'system', {'cpu_percent': cpu_percent}
            )
        elif cpu_percent > self.system_monitors['cpu']['warning']:
            await self._generate_alert(
                'high_cpu_usage', AlertSeverity.WARNING,
                f"High CPU usage: {cpu_percent:.1f}%",
                'system', {'cpu_percent': cpu_percent}
            )
    
    async def _monitor_memory_usage(self):
        """🧠 Monitor memory usage"""
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        await self._update_metric('memory_usage', memory_percent)
        
        # Check thresholds
        if memory_percent > self.system_monitors['memory']['critical']:
            await self._generate_alert(
                'high_memory_usage', AlertSeverity.CRITICAL,
                f"Critical memory usage: {memory_percent:.1f}%",
                'system', {
                    'memory_percent': memory_percent,
                    'available_gb': memory.available / (1024**3),
                    'total_gb': memory.total / (1024**3)
                }
            )
        elif memory_percent > self.system_monitors['memory']['warning']:
            await self._generate_alert(
                'high_memory_usage', AlertSeverity.WARNING,
                f"High memory usage: {memory_percent:.1f}%",
                'system', {'memory_percent': memory_percent}
            )
    
    async def _monitor_disk_usage(self):
        """💾 Monitor disk usage"""
        disk_usage = psutil.disk_usage('/')
        disk_percent = (disk_usage.used / disk_usage.total) * 100
        
        await self._update_metric('disk_usage', disk_percent)
        
        # Check thresholds
        if disk_percent > self.system_monitors['disk']['critical']:
            await self._generate_alert(
                'disk_space_low', AlertSeverity.CRITICAL,
                f"Critical disk usage: {disk_percent:.1f}%",
                'system', {
                    'disk_percent': disk_percent,
                    'free_gb': disk_usage.free / (1024**3),
                    'total_gb': disk_usage.total / (1024**3)
                }
            )
        elif disk_percent > self.system_monitors['disk']['warning']:
            await self._generate_alert(
                'disk_space_low', AlertSeverity.WARNING,
                f"Low disk space: {disk_percent:.1f}%",
                'system', {'disk_percent': disk_percent}
            )
    
    async def _monitor_network_usage(self):
        """🌐 Monitor network usage"""
        net_io = psutil.net_io_counters()
        connections = len(psutil.net_connections())
        
        await self._update_metric('network_connections', connections)
        
        # Check for unusual network activity
        if connections > 500:  # High connection count
            await self._generate_alert(
                'high_network_connections', AlertSeverity.WARNING,
                f"High network connections: {connections}",
                'system', {'connections': connections}
            )
    
    async def _monitor_processes(self):
        """⚚ Monitor system processes"""
        processes = []
        high_cpu_processes = []
        high_memory_processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                if pinfo['cpu_percent'] > 50:  # High CPU usage
                    high_cpu_processes.append(pinfo)
                if pinfo['memory_percent'] > 10:  # High memory usage
                    high_memory_processes.append(pinfo)
                processes.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        if high_cpu_processes:
            await self._generate_alert(
                'high_cpu_processes', AlertSeverity.INFO,
                f"Processes with high CPU usage: {len(high_cpu_processes)}",
                'system', {'processes': high_cpu_processes[:5]}  # Top 5
            )
    
    async def _monitor_agent_heartbeats(self):
        """💓 Monitor agent heartbeats"""
        current_time = time.time()
        timeout = self.agent_monitors['heartbeat']['timeout']
        
        unresponsive_agents = []
        
        for agent_id, agent_info in self.monitored_agents.items():
            last_heartbeat = agent_info.get('last_heartbeat', 0)
            if current_time - last_heartbeat > timeout:
                unresponsive_agents.append(agent_id)
                
                await self._generate_alert(
                    'agent_unresponsive', AlertSeverity.ERROR,
                    f"Agent {agent_id} unresponsive for {current_time - last_heartbeat:.0f}s",
                    'agent', {
                        'agent_id': agent_id,
                        'last_heartbeat': last_heartbeat,
                        'timeout_seconds': current_time - last_heartbeat
                    }
                )
        
        # Update metric
        responsive_agents = len(self.monitored_agents) - len(unresponsive_agents)
        await self._update_metric('active_agents', responsive_agents)
    
    async def _monitor_agent_performance(self):
        """📊 Monitor agent performance metrics"""
        performance_issues = []
        
        for agent_id, agent_info in self.monitored_agents.items():
            performance = agent_info.get('performance', {})
            
            # Check task completion rate
            completion_rate = performance.get('task_completion_rate', 1.0)
            if completion_rate < 0.7:  # Less than 70% completion
                performance_issues.append({
                    'agent_id': agent_id,
                    'issue': 'low_completion_rate',
                    'value': completion_rate
                })
            
            # Check average response time
            avg_response_time = performance.get('avg_response_time', 0)
            if avg_response_time > 30:  # More than 30 seconds
                performance_issues.append({
                    'agent_id': agent_id,
                    'issue': 'slow_response',
                    'value': avg_response_time
                })
        
        if performance_issues:
            await self._generate_alert(
                'agent_performance_degraded', AlertSeverity.WARNING,
                f"Performance issues detected in {len(performance_issues)} agents",
                'agent', {'performance_issues': performance_issues}
            )
        
        # Update overall task completion rate
        if self.monitored_agents:
            overall_completion = np.mean([
                agent_info.get('performance', {}).get('task_completion_rate', 1.0)
                for agent_info in self.monitored_agents.values()
            ])
            await self._update_metric('task_completion_rate', overall_completion * 100)
    
    async def _monitor_agent_errors(self):
        """❌ Monitor agent error rates"""
        high_error_agents = []
        total_errors = 0
        
        for agent_id, agent_info in self.monitored_agents.items():
            error_rate = agent_info.get('error_rate', 0.0)
            recent_errors = agent_info.get('recent_errors', 0)
            
            total_errors += recent_errors
            
            if error_rate > self.agent_monitors['errors']['error_rate_threshold']:
                high_error_agents.append({
                    'agent_id': agent_id,
                    'error_rate': error_rate,
                    'recent_errors': recent_errors
                })
        
        await self._update_metric('agent_errors', total_errors)
        
        if high_error_agents:
            await self._generate_alert(
                'high_agent_errors', AlertSeverity.ERROR,
                f"High error rates in {len(high_error_agents)} agents",
                'agent', {'high_error_agents': high_error_agents}
            )
    
    async def _monitor_agent_resources(self):
        """🔋 Monitor agent resource usage"""
        high_memory_agents = []
        memory_limit = self.agent_monitors['resource_usage']['memory_limit']
        
        for agent_id, agent_info in self.monitored_agents.items():
            memory_usage = agent_info.get('memory_usage_mb', 0)
            
            if memory_usage > memory_limit:
                high_memory_agents.append({
                    'agent_id': agent_id,
                    'memory_usage_mb': memory_usage,
                    'limit_mb': memory_limit
                })
        
        if high_memory_agents:
            await self._generate_alert(
                'agent_high_memory', AlertSeverity.WARNING,
                f"High memory usage in {len(high_memory_agents)} agents",
                'agent', {'high_memory_agents': high_memory_agents}
            )
    
    async def _monitor_sports_data_freshness(self):
        """⚽ Monitor sports data freshness"""
        # Request data freshness from data collector agents
        await self.send_message('*', 'data_freshness_check', {
            'requester': self.agent_id,
            'max_age_seconds': self.application_monitors['sports_data_freshness']['max_age']
        })
    
    async def _monitor_prediction_accuracy(self):
        """🎯 Monitor prediction accuracy"""
        # Request accuracy metrics from predictor agents
        await self.send_message('*', 'accuracy_report_request', {
            'requester': self.agent_id,
            'time_window_hours': 24
        })
    
    async def _monitor_workflow_completion(self):
        """🔄 Monitor workflow completion times"""
        # Request workflow status from coordinator agents
        await self.send_message('*', 'workflow_status_request', {
            'requester': self.agent_id,
            'include_metrics': True
        })
    
    async def _monitor_api_endpoints(self):
        """🌐 Monitor API endpoint health"""
        endpoints = [
            'http://localhost:3005/health',  # Main panel
            'http://localhost:3206/status'   # API status
        ]
        
        unhealthy_endpoints = []
        
        for endpoint in endpoints:
            try:
                import aiohttp
                timeout = aiohttp.ClientTimeout(total=self.application_monitors['api_endpoints']['timeout'])
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.get(endpoint) as response:
                        if response.status != 200:
                            unhealthy_endpoints.append({
                                'endpoint': endpoint,
                                'status_code': response.status
                            })
            except Exception as e:
                unhealthy_endpoints.append({
                    'endpoint': endpoint,
                    'error': str(e)
                })
        
        if unhealthy_endpoints:
            await self._generate_alert(
                'api_endpoints_unhealthy', AlertSeverity.ERROR,
                f"Unhealthy API endpoints: {len(unhealthy_endpoints)}",
                'application', {'unhealthy_endpoints': unhealthy_endpoints}
            )
    
    async def _update_metric(self, metric_name: str, value: float):
        """📊 Update health metric"""
        if metric_name not in self.health_metrics:
            return
        
        metric = self.health_metrics[metric_name]
        
        # Type safety check - ensure we have a HealthMetric object
        if not isinstance(metric, HealthMetric):
            logger.error(f"❌ Invalid metric type for {metric_name}: {type(metric)}")
            # Recreate the metric if it's corrupted
            self.health_metrics[metric_name] = HealthMetric(
                metric_name,  # Fixed: positional argument, not name=
                'gauge',
                'percent'
            )
            metric = self.health_metrics[metric_name]
            
        current_time = time.time()
        
        # Update metric data
        metric.current_value = value
        metric.values.append(value)
        metric.timestamps.append(current_time)
        
        # Update statistics
        if value < metric.min_value:
            metric.min_value = value
        if value > metric.max_value:
            metric.max_value = value
        
        if len(metric.values) > 1:
            metric.avg_value = np.mean(list(metric.values))
            metric.std_deviation = np.std(list(metric.values))
        
        # Check thresholds
        await self._check_metric_thresholds(metric_name, metric, value)
    
    async def _check_metric_thresholds(self, metric_name: str, metric: HealthMetric, value: float):
        """🚨 Check metric against thresholds"""
        if metric.critical_threshold is not None:
            if ((metric.threshold_direction == 'above' and value > metric.critical_threshold) or
                (metric.threshold_direction == 'below' and value < metric.critical_threshold)):
                
                await self._generate_alert(
                    f'{metric_name}_critical', AlertSeverity.CRITICAL,
                    f"Critical {metric_name}: {value} {metric.unit}",
                    'metric', {
                        'metric_name': metric_name,
                        'value': value,
                        'threshold': metric.critical_threshold,
                        'direction': metric.threshold_direction
                    }
                )
        
        elif metric.warning_threshold is not None:
            if ((metric.threshold_direction == 'above' and value > metric.warning_threshold) or
                (metric.threshold_direction == 'below' and value < metric.warning_threshold)):
                
                await self._generate_alert(
                    f'{metric_name}_warning', AlertSeverity.WARNING,
                    f"Warning {metric_name}: {value} {metric.unit}",
                    'metric', {
                        'metric_name': metric_name,
                        'value': value,
                        'threshold': metric.warning_threshold,
                        'direction': metric.threshold_direction
                    }
                )
    
    async def _generate_alert(self, alert_type: str, severity: AlertSeverity, 
                           message: str, source: str, details: Dict[str, Any]):
        """🚨 Generate system alert"""
        alert_id = f"{alert_type}_{source}_{int(time.time())}"
        
        # Check for duplicate alerts
        existing_alert = self._find_existing_alert(alert_type, source)
        if existing_alert and existing_alert.status == 'active':
            # Update existing alert instead of creating duplicate
            existing_alert.details.update(details)
            return
        
        # Create new alert
        alert = SystemAlert(alert_id, alert_type, severity, message, source, details)
        self.active_alerts[alert_id] = alert
        self.alert_history.append(alert)
        
        # Update metrics
        self.monitoring_metrics['alerts_generated'] += 1
        
        # Broadcast alert
        await self.broadcast_message('system_alert', {
            'alert_id': alert_id,
            'alert_type': alert_type,
            'severity': severity.name,
            'message': message,
            'source': source,
            'details': details,
            'created_time': alert.created_time.isoformat(),
            'monitor_agent': self.agent_id
        })
        
        # Immediate recovery action if available
        if alert_type in self.recovery_actions:
            asyncio.create_task(self._execute_recovery_action(alert_type, alert))
        
        logger.warning(f"🚨 Generated {severity.name} alert: {message}")
    
    def _find_existing_alert(self, alert_type: str, source: str) -> Optional[SystemAlert]:
        """🔍 Find existing alert of same type and source"""
        for alert in self.active_alerts.values():
            if alert.alert_type == alert_type and alert.source == source:
                return alert
        return None
    
    async def _execute_recovery_action(self, alert_type: str, alert: SystemAlert):
        """🔧 Execute automated recovery action"""
        if alert_type not in self.recovery_actions:
            return
        
        try:
            logger.info(f"🔧 Executing recovery action for {alert_type}")
            
            recovery_function = self.recovery_actions[alert_type]
            success = await recovery_function(alert)
            
            if success:
                alert.status = 'recovering'
                alert.resolution_notes = f"Automated recovery action executed successfully"
                self.monitoring_metrics['recovery_actions_taken'] += 1
                
                logger.info(f"✅ Recovery action succeeded for {alert_type}")
            else:
                logger.warning(f"❌ Recovery action failed for {alert_type}")
                
        except Exception as e:
            logger.error(f"❌ Recovery action error for {alert_type}: {e}")
    
    async def _recover_high_memory(self, alert: SystemAlert) -> bool:
        """🧠 Recover from high memory usage"""
        try:
            # Force garbage collection
            import gc
            gc.collect()
            
            # Request memory cleanup from agents
            await self.broadcast_message('memory_cleanup_request', {
                'requester': self.agent_id,
                'severity': 'high',
                'current_usage': alert.details.get('memory_percent', 0)
            })
            
            # Wait a moment and check if memory usage improved
            await asyncio.sleep(5)
            current_memory = psutil.virtual_memory().percent
            
            if current_memory < alert.details.get('memory_percent', 100) - 5:  # 5% improvement
                return True
                
        except Exception as e:
            logger.error(f"❌ Memory recovery error: {e}")
        
        return False
    
    async def _recover_high_cpu(self, alert: SystemAlert) -> bool:
        """🖥️ Recover from high CPU usage"""
        try:
            # Request CPU throttling from agents
            await self.broadcast_message('cpu_throttle_request', {
                'requester': self.agent_id,
                'severity': 'high',
                'current_usage': alert.details.get('cpu_percent', 0)
            })
            
            # Check if CPU usage improved
            await asyncio.sleep(10)
            current_cpu = psutil.cpu_percent(interval=1)
            
            if current_cpu < alert.details.get('cpu_percent', 100) - 10:  # 10% improvement
                return True
                
        except Exception as e:
            logger.error(f"❌ CPU recovery error: {e}")
        
        return False
    
    async def _recover_unresponsive_agent(self, alert: SystemAlert) -> bool:
        """🤖 Recover unresponsive agent"""
        try:
            agent_id = alert.details.get('agent_id')
            if not agent_id:
                return False
            
            # Send ping to agent
            await self.send_message(agent_id, 'health_ping', {
                'requester': self.agent_id,
                'timestamp': time.time()
            })
            
            # Request coordinator to check agent status
            await self.send_message('*', 'agent_health_check', {
                'target_agent': agent_id,
                'requester': self.agent_id,
                'last_seen': alert.details.get('last_heartbeat', 0)
            })
            
            return True  # Recovery action initiated
            
        except Exception as e:
            logger.error(f"❌ Agent recovery error: {e}")
        
        return False
    
    async def _recover_disk_space(self, alert: SystemAlert) -> bool:
        """💾 Recover disk space"""
        try:
            # Clean up temporary files
            temp_dirs = ['/tmp', '/var/tmp']
            for temp_dir in temp_dirs:
                if os.path.exists(temp_dir):
                    # Clean old temporary files (older than 1 day)
                    subprocess.run(['find', temp_dir, '-type', 'f', '-mtime', '+1', '-delete'], 
                                 capture_output=True)
            
            # Request cleanup from agents
            await self.broadcast_message('disk_cleanup_request', {
                'requester': self.agent_id,
                'severity': 'high',
                'current_usage': alert.details.get('disk_percent', 0)
            })
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Disk recovery error: {e}")
        
        return False
    
    async def _recover_network_issues(self, alert: SystemAlert) -> bool:
        """🌐 Recover from network issues"""
        try:
            # Reset network connections if too many
            connections = alert.details.get('connections', 0)
            if connections > 1000:
                # Request agents to close idle connections
                await self.broadcast_message('network_cleanup_request', {
                    'requester': self.agent_id,
                    'action': 'close_idle_connections',
                    'current_connections': connections
                })
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Network recovery error: {e}")
        
        return False
    
    async def _process_alert_escalations(self):
        """📈 Process alert escalations"""
        current_time = datetime.now()
        
        for alert_id, alert in list(self.active_alerts.items()):
            if alert.status != 'active' or alert.escalated:
                continue
            
            escalation_rules = self.alert_escalation_rules.get(alert.severity)
            if not escalation_rules:
                continue
            
            time_since_creation = (current_time - alert.created_time).total_seconds()
            
            if time_since_creation > escalation_rules['escalate_after']:
                await self._escalate_alert(alert, escalation_rules)
    
    async def _escalate_alert(self, alert: SystemAlert, escalation_rules: Dict[str, Any]):
        """📈 Escalate alert"""
        alert.escalated = True
        
        # Notify specified recipients
        recipients = escalation_rules.get('notify', [])
        
        for recipient in recipients:
            if recipient == 'coordinator':
                await self.send_message('*', 'alert_escalation', {
                    'alert_id': alert.alert_id,
                    'alert_type': alert.alert_type,
                    'severity': alert.severity.name,
                    'message': alert.message,
                    'escalation_reason': 'timeout',
                    'monitor_agent': self.agent_id
                })
        
        logger.warning(f"📈 Escalated alert {alert.alert_id} to {recipients}")
    
    async def _check_alert_resolutions(self):
        """✅ Check for resolved alerts"""
        for alert_id, alert in list(self.active_alerts.items()):
            if alert.status == 'active':
                # Check if alert condition is resolved
                if await self._is_alert_resolved(alert):
                    await self._resolve_alert(alert_id)
    
    async def _is_alert_resolved(self, alert: SystemAlert) -> bool:
        """🔍 Check if alert condition is resolved"""
        alert_type = alert.alert_type
        
        if alert_type == 'high_cpu_usage':
            current_cpu = psutil.cpu_percent()
            return current_cpu < self.system_monitors['cpu']['warning'] * 0.9  # 10% below warning
        
        elif alert_type == 'high_memory_usage':
            current_memory = psutil.virtual_memory().percent
            return current_memory < self.system_monitors['memory']['warning'] * 0.9
        
        elif alert_type == 'disk_space_low':
            disk_usage = psutil.disk_usage('/')
            current_disk = (disk_usage.used / disk_usage.total) * 100
            return current_disk < self.system_monitors['disk']['warning'] * 0.9
        
        elif alert_type == 'agent_unresponsive':
            agent_id = alert.details.get('agent_id')
            if agent_id in self.monitored_agents:
                last_heartbeat = self.monitored_agents[agent_id].get('last_heartbeat', 0)
                return time.time() - last_heartbeat < self.agent_monitors['heartbeat']['timeout']
        
        return False
    
    async def _resolve_alert(self, alert_id: str):
        """✅ Resolve alert"""
        if alert_id not in self.active_alerts:
            return
        
        alert = self.active_alerts[alert_id]
        alert.status = 'resolved'
        alert.resolved_time = datetime.now()
        
        # Remove from active alerts
        del self.active_alerts[alert_id]
        
        # Update metrics
        self.monitoring_metrics['alerts_resolved'] += 1
        
        # Broadcast resolution
        await self.broadcast_message('alert_resolved', {
            'alert_id': alert_id,
            'alert_type': alert.alert_type,
            'resolution_time': alert.resolved_time.isoformat(),
            'duration_seconds': (alert.resolved_time - alert.created_time).total_seconds(),
            'monitor_agent': self.agent_id
        })
        
        logger.info(f"✅ Resolved alert {alert_id}")
    
    async def _update_alert_statistics(self):
        """📊 Update alert statistics"""
        # Calculate false positive rate
        recent_alerts = [
            alert for alert in self.alert_history
            if alert.created_time > datetime.now() - timedelta(hours=24)
        ]
        
        if recent_alerts:
            resolved_quickly = [
                alert for alert in recent_alerts
                if (alert.resolved_time and 
                    (alert.resolved_time - alert.created_time).total_seconds() < 300)  # 5 minutes
            ]
            
            self.monitoring_metrics['false_positive_rate'] = len(resolved_quickly) / len(recent_alerts)
    
    async def _establish_baselines(self):
        """📊 Establish performance baselines"""
        logger.info("📊 Establishing system baselines...")
        
        # Collect baseline metrics for 30 seconds
        baseline_samples = 6  # 30 seconds / 5 second intervals
        
        for i in range(baseline_samples):
            await self._monitor_cpu_usage()
            await self._monitor_memory_usage()
            await asyncio.sleep(5)
        
        logger.info("📊 System baselines established")
    
    async def _adapt_thresholds_for_noise_reduction(self):
        """🔇 Adapt thresholds to reduce alert noise"""
        # Increase warning thresholds by 10%
        self.system_monitors['cpu']['warning'] = min(95, self.system_monitors['cpu']['warning'] * 1.1)
        self.system_monitors['memory']['warning'] = min(95, self.system_monitors['memory']['warning'] * 1.1)
        self.system_monitors['disk']['warning'] = min(95, self.system_monitors['disk']['warning'] * 1.1)
    
    async def _adapt_thresholds_for_sensitivity(self):
        """🔊 Adapt thresholds for higher sensitivity"""
        # Decrease warning thresholds by 5%
        self.system_monitors['cpu']['warning'] = max(50, self.system_monitors['cpu']['warning'] * 0.95)
        self.system_monitors['memory']['warning'] = max(50, self.system_monitors['memory']['warning'] * 0.95)
        self.system_monitors['disk']['warning'] = max(50, self.system_monitors['disk']['warning'] * 0.95)
    
    async def _adapt_monitoring_intervals(self, factor: float):
        """⏱️ Adapt monitoring intervals based on load"""
        for monitor_type in self.system_monitors:
            current_interval = self.system_monitors[monitor_type]['interval']
            new_interval = max(1, int(current_interval * factor))
            self.system_monitors[monitor_type]['interval'] = new_interval
    
    async def _adapt_recovery_strategies(self):
        """🧠 Learn and adapt recovery strategies"""
        # Analyze recovery success rates
        # This would implement learning from recovery action outcomes
        pass
    
    async def _process_health_checks(self):
        """🏥 Process pending health checks"""
        # Process any health check requests
        pass
    
    async def _update_system_health(self):
        """💚 Update overall system health status"""
        # Count active alerts by severity
        critical_alerts = len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.CRITICAL])
        error_alerts = len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.ERROR])
        warning_alerts = len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.WARNING])
        
        # Determine overall health
        if critical_alerts > 0:
            self.system_health = HealthStatus.CRITICAL
        elif error_alerts > 2:
            self.system_health = HealthStatus.UNHEALTHY
        elif error_alerts > 0 or warning_alerts > 5:
            self.system_health = HealthStatus.DEGRADED
        else:
            self.system_health = HealthStatus.HEALTHY
    
    async def _check_alert_escalations(self):
        """📈 Check for alert escalations"""
        await self._process_alert_escalations()
    
    async def _proactive_health_analysis(self):
        """🔮 Perform proactive health analysis"""
        # Analyze trends to predict potential issues
        
        # CPU trend analysis
        cpu_metric = self.health_metrics.get('cpu_usage')
        if cpu_metric and len(cpu_metric.values) > 10:
            recent_cpu = list(cpu_metric.values)[-10:]
            cpu_trend = np.polyfit(range(len(recent_cpu)), recent_cpu, 1)[0]  # Slope
            
            if cpu_trend > 2:  # Rising trend
                await self._generate_alert(
                    'cpu_trend_rising', AlertSeverity.INFO,
                    f"CPU usage trending upward: {cpu_trend:.1f}% per interval",
                    'prediction', {'trend_slope': cpu_trend}
                )
        
        # Memory trend analysis
        memory_metric = self.health_metrics.get('memory_usage')
        if memory_metric and len(memory_metric.values) > 10:
            recent_memory = list(memory_metric.values)[-10:]
            memory_trend = np.polyfit(range(len(recent_memory)), recent_memory, 1)[0]
            
            if memory_trend > 1:  # Rising trend
                await self._generate_alert(
                    'memory_trend_rising', AlertSeverity.INFO,
                    f"Memory usage trending upward: {memory_trend:.1f}% per interval",
                    'prediction', {'trend_slope': memory_trend}
                )
    
    async def _cleanup_resolved_alerts(self):
        """🧹 Clean up old resolved alerts"""
        cutoff_time = datetime.now() - timedelta(hours=24)
        
        # Remove old alerts from history
        self.alert_history = deque([
            alert for alert in self.alert_history
            if alert.created_time > cutoff_time
        ], maxlen=5000)
    
    # =================== MESSAGE HANDLERS ===================
    
    async def _handle_message(self, message):
        """📨 Handle messages from other agents"""
        await super()._handle_message(message)
        
        if message.message_type == "health_check":
            await self._handle_health_check_request(message)
        elif message.message_type == "agent_status_update":
            await self._handle_agent_status_update(message)
        elif message.message_type == "data_freshness_response":
            await self._handle_data_freshness_response(message)
        elif message.message_type == "accuracy_report":
            await self._handle_accuracy_report(message)
        elif message.message_type == "workflow_status_response":
            await self._handle_workflow_status_response(message)
    
    async def _handle_health_check_request(self, message):
        """🏥 Handle health check request"""
        payload = message.payload
        check_type = payload.get('check_type', 'basic')
        
        health_data = {
            'agent_id': self.agent_id,
            'system_health': self.system_health.value,
            'active_alerts': len(self.active_alerts),
            'monitoring_uptime': time.time() - self.monitoring_metrics['system_uptime'],
            'alerts_generated': self.monitoring_metrics['alerts_generated'],
            'alerts_resolved': self.monitoring_metrics['alerts_resolved']
        }
        
        if check_type == 'detailed':
            health_data.update({
                'health_metrics': {
                    name: {
                        'current_value': metric.current_value,
                        'avg_value': metric.avg_value,
                        'min_value': metric.min_value,
                        'max_value': metric.max_value
                    }
                    for name, metric in self.health_metrics.items()
                },
                'system_info': {
                    'cpu_count': psutil.cpu_count(),
                    'memory_total_gb': psutil.virtual_memory().total / (1024**3),
                    'platform': platform.platform()
                }
            })
        
        await self.send_message(message.sender_id, 'health_check_response', health_data)
    
    async def _handle_agent_status_update(self, message):
        """📊 Handle agent status update"""
        payload = message.payload
        agent_id = message.sender_id
        
        # Update monitored agent info
        if agent_id not in self.monitored_agents:
            self.monitored_agents[agent_id] = {}
        
        agent_info = self.monitored_agents[agent_id]
        agent_info.update({
            'last_heartbeat': time.time(),
            'status': payload.get('status', 'unknown'),
            'performance': payload.get('performance', {}),
            'resource_usage': payload.get('resource_usage', {}),
            'error_rate': payload.get('error_rate', 0.0),
            'memory_usage_mb': payload.get('memory_usage_mb', 0)
        })
    
    async def _handle_data_freshness_response(self, message):
        """📅 Handle data freshness response"""
        payload = message.payload
        data_age = payload.get('data_age_seconds', 0)
        
        await self._update_metric('data_freshness', data_age)
    
    async def _handle_accuracy_report(self, message):
        """🎯 Handle accuracy report"""
        payload = message.payload
        accuracy = payload.get('accuracy', 0.0)
        
        await self._update_metric('prediction_accuracy', accuracy * 100)
    
    async def _handle_workflow_status_response(self, message):
        """🔄 Handle workflow status response"""
        payload = message.payload
        completion_rate = payload.get('completion_rate', 1.0)
        avg_duration = payload.get('avg_completion_time', 0)
        
        await self._update_metric('task_completion_rate', completion_rate * 100)
    
    # =================== PUBLIC API ===================
    
    async def get_monitoring_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive monitoring status"""
        return {
            'agent_id': self.agent_id,
            'timestamp': time.time(),
            'system_health': self.system_health.value,
            'active_alerts': len(self.active_alerts),
            'monitored_agents': len(self.monitored_agents),
            'monitoring_metrics': self.monitoring_metrics,
            'health_metrics': {
                name: {
                    'current_value': metric.current_value,
                    'unit': metric.unit,
                    'warning_threshold': metric.warning_threshold,
                    'critical_threshold': metric.critical_threshold
                }
                for name, metric in self.health_metrics.items()
            },
            'alert_summary': {
                'critical': len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.CRITICAL]),
                'error': len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.ERROR]),
                'warning': len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.WARNING]),
                'info': len([a for a in self.active_alerts.values() if a.severity == AlertSeverity.INFO])
            }
        }
    
    async def get_system_health_report(self) -> Dict[str, Any]:
        """💚 Get detailed system health report"""
        return {
            'overall_health': self.system_health.value,
            'uptime_seconds': time.time() - self.monitoring_metrics['system_uptime'],
            'system_resources': {
                'cpu_percent': psutil.cpu_percent(),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_percent': (psutil.disk_usage('/').used / psutil.disk_usage('/').total) * 100,
                'network_connections': len(psutil.net_connections())
            },
            'agent_health': {
                'total_agents': len(self.monitored_agents),
                'responsive_agents': len([
                    a for a in self.monitored_agents.values()
                    if time.time() - a.get('last_heartbeat', 0) < self.agent_monitors['heartbeat']['timeout']
                ])
            },
            'alert_statistics': {
                'total_generated': self.monitoring_metrics['alerts_generated'],
                'total_resolved': self.monitoring_metrics['alerts_resolved'],
                'false_positive_rate': self.monitoring_metrics['false_positive_rate'],
                'recovery_actions': self.monitoring_metrics['recovery_actions_taken']
            }
        }
    
    async def get_active_alerts(self) -> List[Dict[str, Any]]:
        """🚨 Get list of active alerts"""
        return [
            {
                'alert_id': alert.alert_id,
                'alert_type': alert.alert_type,
                'severity': alert.severity.name,
                'message': alert.message,
                'source': alert.source,
                'created_time': alert.created_time.isoformat(),
                'escalated': alert.escalated,
                'status': alert.status
            }
            for alert in self.active_alerts.values()
        ]

if __name__ == "__main__":
    async def test_monitor():
        agent = MonitorAgent("monitor_001")
        AGENT_REGISTRY.register_agent(agent)
        
        await agent.spawn()
        await asyncio.sleep(10)  # Let it monitor for a bit
        
        # Get monitoring status
        status = await agent.get_monitoring_status()
        print(f"📊 Monitoring Status: {json.dumps(status, indent=2, default=str)}")
        
        # Get health report
        health_report = await agent.get_system_health_report()
        print(f"💚 Health Report: {json.dumps(health_report, indent=2, default=str)}")
        
        # Get active alerts
        alerts = await agent.get_active_alerts()
        print(f"🚨 Active Alerts: {json.dumps(alerts, indent=2, default=str)}")
        
        await agent.terminate()
    
    asyncio.run(test_monitor())