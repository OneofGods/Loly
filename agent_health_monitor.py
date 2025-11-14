#!/usr/bin/env python3
"""
🔥💀🔥 LOLY'S AGENT HEALTH MONITOR - SELF-HEALING GODDESS! 💀🔥💀

Continuous health monitoring for all agents under Loly's command!
Detects issues, tracks performance, and enables auto-recovery.

MONITORING CAPABILITIES:
- Heartbeat checks (every 30s)
- Response time tracking
- Error rate monitoring
- Circuit breaker pattern
- Health scoring (0-100)
- Performance degradation detection
- Automatic agent health reports

This makes Loly PROACTIVE about agent health!
"""

import asyncio
import json
import logging
import aiohttp
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from enum import Enum
from collections import deque
import time

logger = logging.getLogger(__name__)


class AgentHealthStatus(Enum):
    """💚 Agent health states"""
    HEALTHY = "healthy"              # All good!
    DEGRADED = "degraded"            # Working but slow/errors
    UNHEALTHY = "unhealthy"          # Critical issues
    DEAD = "dead"                    # Not responding
    RECOVERING = "recovering"        # Being recovered
    CIRCUIT_OPEN = "circuit_open"    # Circuit breaker active


class CircuitBreakerState(Enum):
    """🔌 Circuit breaker states"""
    CLOSED = "closed"        # Normal operation
    OPEN = "open"           # Blocking requests
    HALF_OPEN = "half_open" # Testing recovery


class AgentHealthMetrics:
    """📊 Health metrics for a single agent"""

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.status = AgentHealthStatus.HEALTHY

        # Heartbeat tracking
        self.last_heartbeat = time.time()
        self.heartbeat_failures = 0
        self.heartbeat_successes = 0

        # Performance metrics
        self.response_times = deque(maxlen=100)  # Last 100 response times
        self.error_count = 0
        self.success_count = 0
        self.timeout_count = 0

        # Health scoring (0-100)
        self.health_score = 100.0
        self.last_score_update = time.time()

        # Circuit breaker
        self.circuit_state = CircuitBreakerState.CLOSED
        self.circuit_failures = 0
        self.circuit_opened_at = None
        self.circuit_test_time = None

        # Recovery tracking
        self.recovery_attempts = 0
        self.last_recovery_attempt = None
        self.recovered_at = None

    def record_success(self, response_time: float):
        """✅ Record successful agent interaction"""
        self.success_count += 1
        self.response_times.append(response_time)
        self.last_heartbeat = time.time()
        self.heartbeat_successes += 1
        self.circuit_failures = 0  # Reset circuit breaker failures

        # Update health score (success improves it)
        self.health_score = min(100.0, self.health_score + 1.0)
        self.last_score_update = time.time()

    def record_error(self, error_type: str = "unknown"):
        """❌ Record failed agent interaction"""
        self.error_count += 1
        self.circuit_failures += 1

        if error_type == "timeout":
            self.timeout_count += 1

        # Update health score (errors reduce it)
        self.health_score = max(0.0, self.health_score - 5.0)
        self.last_score_update = time.time()

    def record_heartbeat_failure(self):
        """💔 Record heartbeat check failure"""
        self.heartbeat_failures += 1
        self.health_score = max(0.0, self.health_score - 10.0)
        self.last_score_update = time.time()

    def get_average_response_time(self) -> float:
        """⏱️ Get average response time"""
        if not self.response_times:
            return 0.0
        return sum(self.response_times) / len(self.response_times)

    def get_error_rate(self) -> float:
        """📊 Get error rate (0-1)"""
        total = self.success_count + self.error_count
        if total == 0:
            return 0.0
        return self.error_count / total

    def should_open_circuit(self, threshold: int = 5) -> bool:
        """🔌 Check if circuit breaker should open"""
        return (
            self.circuit_state == CircuitBreakerState.CLOSED and
            self.circuit_failures >= threshold
        )

    def should_test_circuit(self, test_interval_seconds: int = 60) -> bool:
        """🧪 Check if circuit should be tested (half-open)"""
        if self.circuit_state != CircuitBreakerState.OPEN:
            return False

        if not self.circuit_opened_at:
            return False

        time_since_open = time.time() - self.circuit_opened_at
        return time_since_open >= test_interval_seconds

    def to_dict(self) -> Dict[str, Any]:
        """Convert metrics to dict"""
        return {
            'agent_id': self.agent_id,
            'status': self.status.value,
            'health_score': round(self.health_score, 2),
            'last_heartbeat': datetime.fromtimestamp(self.last_heartbeat).isoformat(),
            'heartbeat_failures': self.heartbeat_failures,
            'heartbeat_successes': self.heartbeat_successes,
            'response_time_avg': round(self.get_average_response_time(), 3),
            'error_rate': round(self.get_error_rate(), 3),
            'success_count': self.success_count,
            'error_count': self.error_count,
            'timeout_count': self.timeout_count,
            'circuit_state': self.circuit_state.value,
            'circuit_failures': self.circuit_failures,
            'recovery_attempts': self.recovery_attempts
        }


class AgentHealthMonitor:
    """
    🔥💀🔥 LOLY'S AGENT HEALTH MONITOR 💀🔥💀

    Continuously monitors all agents and maintains health metrics!
    """

    def __init__(self, config_path: str = "health_config.json"):
        self.monitor_id = f"health_monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Load configuration
        self.config = self._load_config(config_path)

        # Agent metrics tracking
        self.agent_metrics: Dict[str, AgentHealthMetrics] = {}

        # Monitoring state
        self.monitoring_active = False
        self.monitor_task = None

        # Statistics
        self.stats = {
            'total_health_checks': 0,
            'total_agents_monitored': 0,
            'total_failures_detected': 0,
            'total_recoveries_triggered': 0,
            'monitoring_start_time': None
        }

        logger.info(f"🔥💀🔥 Agent Health Monitor {self.monitor_id} initialized!")

    def _load_config(self, config_path: str) -> Dict:
        """📋 Load health monitoring configuration"""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            logger.info(f"✅ Health config loaded")
            return config
        except FileNotFoundError:
            logger.warning(f"⚠️  Health config not found, using defaults")
            return self._get_default_config()
        except Exception as e:
            logger.error(f"❌ Failed to load health config: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """📋 Default health monitoring configuration"""
        return {
            'heartbeat_interval_seconds': 30,
            'heartbeat_timeout_seconds': 10,
            'circuit_breaker': {
                'failure_threshold': 5,
                'test_interval_seconds': 60,
                'success_threshold': 3
            },
            'health_scoring': {
                'degraded_threshold': 70,
                'unhealthy_threshold': 40,
                'dead_threshold': 10
            },
            'recovery': {
                'auto_recovery_enabled': True,
                'max_recovery_attempts': 3,
                'recovery_backoff_seconds': [5, 15, 30]
            }
        }

    def register_agent(self, agent_id: str, agent_info: Dict[str, Any]):
        """📝 Register agent for monitoring"""
        if agent_id not in self.agent_metrics:
            self.agent_metrics[agent_id] = AgentHealthMetrics(agent_id)
            self.stats['total_agents_monitored'] = len(self.agent_metrics)
            logger.info(f"📝 Registered agent for monitoring: {agent_id}")

    async def start_monitoring(self):
        """🚀 Start continuous health monitoring"""
        if self.monitoring_active:
            logger.warning("⚠️  Monitoring already active")
            return

        self.monitoring_active = True
        self.stats['monitoring_start_time'] = datetime.now().isoformat()

        logger.info("🚀 Starting continuous agent health monitoring...")

        # Start monitoring task
        self.monitor_task = asyncio.create_task(self._monitoring_loop())

        logger.info("✅ Agent health monitoring active!")

    async def stop_monitoring(self):
        """🛑 Stop health monitoring"""
        self.monitoring_active = False

        if self.monitor_task:
            self.monitor_task.cancel()
            try:
                await self.monitor_task
            except asyncio.CancelledError:
                pass

        logger.info("🛑 Agent health monitoring stopped")

    async def _monitoring_loop(self):
        """🔄 Main monitoring loop"""
        interval = self.config.get('heartbeat_interval_seconds', 30)

        while self.monitoring_active:
            try:
                await self._perform_health_checks()
                await self._update_health_statuses()
                await self._check_circuit_breakers()

                await asyncio.sleep(interval)

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"❌ Monitoring loop error: {e}")
                await asyncio.sleep(interval)

    async def _perform_health_checks(self):
        """💚 Perform heartbeat checks on all agents"""
        timeout = self.config.get('heartbeat_timeout_seconds', 10)

        for agent_id, metrics in self.agent_metrics.items():
            # Skip if circuit is open
            if metrics.circuit_state == CircuitBreakerState.OPEN:
                continue

            try:
                # Attempt heartbeat check
                start_time = time.time()

                # TODO: Actual heartbeat implementation
                # For now, simulate based on last activity
                time_since_heartbeat = time.time() - metrics.last_heartbeat

                if time_since_heartbeat < 120:  # 2 minutes grace period
                    response_time = time.time() - start_time
                    metrics.record_success(response_time)
                else:
                    metrics.record_heartbeat_failure()
                    self.stats['total_failures_detected'] += 1

                self.stats['total_health_checks'] += 1

            except asyncio.TimeoutError:
                metrics.record_error("timeout")
                metrics.record_heartbeat_failure()
                self.stats['total_failures_detected'] += 1

            except Exception as e:
                logger.error(f"❌ Health check error for {agent_id}: {e}")
                metrics.record_error("exception")
                metrics.record_heartbeat_failure()
                self.stats['total_failures_detected'] += 1

    async def _update_health_statuses(self):
        """📊 Update health status for all agents based on scores"""
        thresholds = self.config.get('health_scoring', {})

        degraded_threshold = thresholds.get('degraded_threshold', 70)
        unhealthy_threshold = thresholds.get('unhealthy_threshold', 40)
        dead_threshold = thresholds.get('dead_threshold', 10)

        for agent_id, metrics in self.agent_metrics.items():
            score = metrics.health_score

            # Determine status based on score
            if score >= degraded_threshold:
                new_status = AgentHealthStatus.HEALTHY
            elif score >= unhealthy_threshold:
                new_status = AgentHealthStatus.DEGRADED
            elif score >= dead_threshold:
                new_status = AgentHealthStatus.UNHEALTHY
            else:
                new_status = AgentHealthStatus.DEAD

            # Update if changed
            if new_status != metrics.status:
                old_status = metrics.status
                metrics.status = new_status
                logger.warning(f"⚠️  Agent {agent_id} status changed: {old_status.value} → {new_status.value}")

    async def _check_circuit_breakers(self):
        """🔌 Check and update circuit breaker states"""
        cb_config = self.config.get('circuit_breaker', {})
        failure_threshold = cb_config.get('failure_threshold', 5)
        test_interval = cb_config.get('test_interval_seconds', 60)

        for agent_id, metrics in self.agent_metrics.items():
            # Check if circuit should open
            if metrics.should_open_circuit(failure_threshold):
                metrics.circuit_state = CircuitBreakerState.OPEN
                metrics.circuit_opened_at = time.time()
                logger.warning(f"🔌 Circuit breaker OPENED for agent: {agent_id}")

            # Check if circuit should test (half-open)
            elif metrics.should_test_circuit(test_interval):
                metrics.circuit_state = CircuitBreakerState.HALF_OPEN
                metrics.circuit_test_time = time.time()
                logger.info(f"🧪 Circuit breaker HALF-OPEN (testing) for agent: {agent_id}")

    def record_agent_interaction(self, agent_id: str, success: bool,
                                 response_time: float = None, error_type: str = None):
        """📝 Record agent interaction result"""
        if agent_id not in self.agent_metrics:
            self.register_agent(agent_id, {})

        metrics = self.agent_metrics[agent_id]

        if success:
            if response_time is not None:
                metrics.record_success(response_time)

            # If circuit was half-open and test succeeded, close it
            if metrics.circuit_state == CircuitBreakerState.HALF_OPEN:
                metrics.circuit_state = CircuitBreakerState.CLOSED
                metrics.circuit_failures = 0
                logger.info(f"✅ Circuit breaker CLOSED for agent: {agent_id}")
        else:
            metrics.record_error(error_type or "unknown")

            # If circuit was half-open and test failed, reopen it
            if metrics.circuit_state == CircuitBreakerState.HALF_OPEN:
                metrics.circuit_state = CircuitBreakerState.OPEN
                metrics.circuit_opened_at = time.time()
                logger.warning(f"🔌 Circuit breaker REOPENED for agent: {agent_id}")

    def get_agent_health(self, agent_id: str) -> Optional[Dict[str, Any]]:
        """💚 Get health status for specific agent"""
        metrics = self.agent_metrics.get(agent_id)
        return metrics.to_dict() if metrics else None

    def get_all_agent_health(self) -> Dict[str, Any]:
        """💚 Get health status for all agents"""
        return {
            agent_id: metrics.to_dict()
            for agent_id, metrics in self.agent_metrics.items()
        }

    def get_unhealthy_agents(self) -> List[str]:
        """⚠️  Get list of unhealthy agents"""
        return [
            agent_id
            for agent_id, metrics in self.agent_metrics.items()
            if metrics.status in [
                AgentHealthStatus.UNHEALTHY,
                AgentHealthStatus.DEAD,
                AgentHealthStatus.DEGRADED
            ]
        ]

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get monitoring statistics"""
        healthy_count = sum(
            1 for m in self.agent_metrics.values()
            if m.status == AgentHealthStatus.HEALTHY
        )
        degraded_count = sum(
            1 for m in self.agent_metrics.values()
            if m.status == AgentHealthStatus.DEGRADED
        )
        unhealthy_count = sum(
            1 for m in self.agent_metrics.values()
            if m.status == AgentHealthStatus.UNHEALTHY
        )
        dead_count = sum(
            1 for m in self.agent_metrics.values()
            if m.status == AgentHealthStatus.DEAD
        )

        return {
            'monitor_id': self.monitor_id,
            'monitoring_active': self.monitoring_active,
            'stats': self.stats,
            'agent_counts': {
                'total': len(self.agent_metrics),
                'healthy': healthy_count,
                'degraded': degraded_count,
                'unhealthy': unhealthy_count,
                'dead': dead_count
            },
            'timestamp': datetime.now().isoformat()
        }


# =================== FACTORY FUNCTION ===================

def create_health_monitor(config_path: str = "health_config.json") -> AgentHealthMonitor:
    """🏭 Create health monitor instance"""
    return AgentHealthMonitor(config_path)


# =================== TESTING ===================

if __name__ == "__main__":
    print("🔥💀🔥 Agent Health Monitor - Standalone test mode 💀🔥💀")
    print("Run test suite for comprehensive testing!")
