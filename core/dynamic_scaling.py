#!/usr/bin/env python3
"""
🔥💀 PHASE 2: DYNAMIC SCALING SYSTEM 💀🔥
Auto-scaling and intelligent load balancing for agent swarms
"""

import asyncio
import logging
import time
import psutil
import statistics
from typing import Dict, List, Set, Any, Optional, Tuple
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass
import numpy as np

logger = logging.getLogger(__name__)

class ScalingDirection(Enum):
    """📈 Scaling direction options"""
    SCALE_UP = "scale_up"
    SCALE_DOWN = "scale_down"
    MAINTAIN = "maintain"

class LoadMetric(Enum):
    """📊 Load measurement metrics"""
    CPU_USAGE = "cpu_usage"
    MEMORY_USAGE = "memory_usage"
    TASK_QUEUE_LENGTH = "task_queue_length"
    RESPONSE_TIME = "response_time"
    THROUGHPUT = "throughput"
    ERROR_RATE = "error_rate"

@dataclass
class ScalingPolicy:
    """📋 Auto-scaling policy definition"""
    policy_id: str
    metric: LoadMetric
    scale_up_threshold: float
    scale_down_threshold: float
    min_agents: int = 1
    max_agents: int = 50
    cooldown_seconds: int = 300
    evaluation_window: int = 60
    scale_up_step: int = 2
    scale_down_step: int = 1

@dataclass
class AgentMetrics:
    """📊 Individual agent performance metrics"""
    agent_id: str
    cpu_usage: float = 0.0
    memory_usage: float = 0.0
    active_tasks: int = 0
    completed_tasks: int = 0
    failed_tasks: int = 0
    avg_response_time: float = 0.0
    throughput: float = 0.0
    error_rate: float = 0.0
    last_heartbeat: datetime = None
    health_score: float = 1.0

class DynamicScalingManager:
    """
    🚀 DYNAMIC SCALING MANAGER
    
    Provides intelligent auto-scaling with:
    - Real-time performance monitoring
    - Predictive scaling based on trends
    - Multi-metric scaling decisions
    - Load balancing optimization
    - Resource-aware agent placement
    - Graceful scaling transitions
    """
    
    def __init__(self, message_bus, swarm_coordinator, agent_factory):
        self.message_bus = message_bus
        self.swarm_coordinator = swarm_coordinator
        self.agent_factory = agent_factory
        
        # Scaling configuration
        self.scaling_policies: Dict[str, ScalingPolicy] = {}
        self.agent_metrics: Dict[str, AgentMetrics] = {}
        self.scaling_history: List[Dict[str, Any]] = []
        
        # Load balancer
        self.load_balancer = IntelligentLoadBalancer(self)
        
        # Performance monitoring
        self.metrics_collector = MetricsCollector(self)
        self.trend_predictor = TrendPredictor()
        
        # Scaling state
        self.last_scaling_action = {}
        self.scaling_in_progress = False
        self.target_agent_count = {}
        
        # Resource monitoring
        self.system_resources = SystemResourceMonitor()
        
        # Default policies
        self._initialize_default_policies()
        
        logger.info("🚀 DynamicScalingManager initialized")
    
    def _initialize_default_policies(self):
        """📋 Initialize default scaling policies"""
        # CPU-based scaling
        cpu_policy = ScalingPolicy(
            policy_id="cpu_scaling",
            metric=LoadMetric.CPU_USAGE,
            scale_up_threshold=75.0,
            scale_down_threshold=25.0,
            min_agents=2,
            max_agents=20,
            cooldown_seconds=180,
            scale_up_step=2,
            scale_down_step=1
        )
        self.scaling_policies["cpu_scaling"] = cpu_policy
        
        # Task queue-based scaling
        queue_policy = ScalingPolicy(
            policy_id="queue_scaling",
            metric=LoadMetric.TASK_QUEUE_LENGTH,
            scale_up_threshold=10.0,
            scale_down_threshold=2.0,
            min_agents=1,
            max_agents=15,
            cooldown_seconds=120,
            scale_up_step=3,
            scale_down_step=1
        )
        self.scaling_policies["queue_scaling"] = queue_policy
        
        # Response time-based scaling
        latency_policy = ScalingPolicy(
            policy_id="latency_scaling",
            metric=LoadMetric.RESPONSE_TIME,
            scale_up_threshold=2000.0,  # 2 seconds
            scale_down_threshold=500.0,  # 0.5 seconds
            min_agents=1,
            max_agents=10,
            cooldown_seconds=240,
            scale_up_step=2,
            scale_down_step=1
        )
        self.scaling_policies["latency_scaling"] = latency_policy
    
    async def start_monitoring(self):
        """🔍 Start dynamic scaling monitoring"""
        logger.info("🔍 Starting dynamic scaling monitoring")
        
        # Start metrics collection
        metrics_task = asyncio.create_task(self.metrics_collector.start_collection())
        
        # Start scaling evaluation loop
        scaling_task = asyncio.create_task(self._scaling_evaluation_loop())
        
        # Start load balancing optimization
        lb_task = asyncio.create_task(self.load_balancer.optimization_loop())
        
        # Start resource monitoring
        resource_task = asyncio.create_task(self.system_resources.monitor_resources())
        
        # Run all monitoring tasks
        await asyncio.gather(
            metrics_task, scaling_task, lb_task, resource_task,
            return_exceptions=True
        )
    
    async def _scaling_evaluation_loop(self):
        """⚖️ Main scaling evaluation loop"""
        while True:
            try:
                if not self.scaling_in_progress:
                    # Evaluate all scaling policies
                    scaling_decisions = []
                    
                    for policy_id, policy in self.scaling_policies.items():
                        decision = await self._evaluate_scaling_policy(policy)
                        if decision != ScalingDirection.MAINTAIN:
                            scaling_decisions.append((policy, decision))
                    
                    # Process scaling decisions
                    if scaling_decisions:
                        await self._process_scaling_decisions(scaling_decisions)
                
                # Wait before next evaluation
                await asyncio.sleep(30)
                
            except Exception as e:
                logger.error(f"❌ Scaling evaluation error: {e}")
                await asyncio.sleep(10)
    
    async def _evaluate_scaling_policy(self, policy: ScalingPolicy) -> ScalingDirection:
        """📊 Evaluate individual scaling policy"""
        try:
            # Check cooldown period
            if await self._is_in_cooldown(policy):
                return ScalingDirection.MAINTAIN
            
            # Get current metric value
            current_value = await self._get_current_metric_value(policy.metric)
            
            if current_value is None:
                return ScalingDirection.MAINTAIN
            
            # Get current agent count for this policy's scope
            current_agents = await self._get_current_agent_count(policy)
            
            # Scaling logic
            if current_value > policy.scale_up_threshold and current_agents < policy.max_agents:
                logger.info(f"📈 Scale up trigger: {policy.metric.value}={current_value} > {policy.scale_up_threshold}")
                return ScalingDirection.SCALE_UP
                
            elif current_value < policy.scale_down_threshold and current_agents > policy.min_agents:
                # Additional checks for scale down
                if await self._safe_to_scale_down(policy, current_agents):
                    logger.info(f"📉 Scale down trigger: {policy.metric.value}={current_value} < {policy.scale_down_threshold}")
                    return ScalingDirection.SCALE_DOWN
            
            return ScalingDirection.MAINTAIN
            
        except Exception as e:
            logger.error(f"❌ Policy evaluation failed for {policy.policy_id}: {e}")
            return ScalingDirection.MAINTAIN
    
    async def _get_current_metric_value(self, metric: LoadMetric) -> Optional[float]:
        """📊 Get current value for specified metric"""
        try:
            if metric == LoadMetric.CPU_USAGE:
                # Average CPU usage across all agents
                cpu_values = [m.cpu_usage for m in self.agent_metrics.values()]
                return statistics.mean(cpu_values) if cpu_values else 0.0
                
            elif metric == LoadMetric.MEMORY_USAGE:
                # Average memory usage across all agents
                memory_values = [m.memory_usage for m in self.agent_metrics.values()]
                return statistics.mean(memory_values) if memory_values else 0.0
                
            elif metric == LoadMetric.TASK_QUEUE_LENGTH:
                # Total active tasks across all agents
                return sum(m.active_tasks for m in self.agent_metrics.values())
                
            elif metric == LoadMetric.RESPONSE_TIME:
                # Average response time across all agents
                response_times = [m.avg_response_time for m in self.agent_metrics.values()]
                return statistics.mean(response_times) if response_times else 0.0
                
            elif metric == LoadMetric.THROUGHPUT:
                # Total throughput across all agents
                return sum(m.throughput for m in self.agent_metrics.values())
                
            elif metric == LoadMetric.ERROR_RATE:
                # Average error rate across all agents
                error_rates = [m.error_rate for m in self.agent_metrics.values()]
                return statistics.mean(error_rates) if error_rates else 0.0
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Metric collection failed for {metric.value}: {e}")
            return None
    
    async def _get_current_agent_count(self, policy: ScalingPolicy) -> int:
        """🔢 Get current agent count"""
        swarm_status = await self.swarm_coordinator.get_swarm_status()
        return swarm_status.get('total_agents', 0)
    
    async def _is_in_cooldown(self, policy: ScalingPolicy) -> bool:
        """⏱️ Check if policy is in cooldown period"""
        last_action_time = self.last_scaling_action.get(policy.policy_id)
        if last_action_time:
            time_since_action = time.time() - last_action_time
            return time_since_action < policy.cooldown_seconds
        return False
    
    async def _safe_to_scale_down(self, policy: ScalingPolicy, current_agents: int) -> bool:
        """🛡️ Check if it's safe to scale down"""
        # Ensure we don't scale down too aggressively
        if current_agents <= policy.min_agents:
            return False
        
        # Check if any agents are under high load
        high_load_agents = [
            agent for agent in self.agent_metrics.values()
            if (agent.cpu_usage > 80.0 or 
                agent.active_tasks > 5 or 
                agent.health_score < 0.8)
        ]
        
        if len(high_load_agents) > current_agents * 0.3:  # More than 30% under high load
            return False
        
        # Use trend prediction
        predicted_load = await self.trend_predictor.predict_load_trend()
        if predicted_load == "increasing":
            return False
        
        return True
    
    async def _process_scaling_decisions(self, scaling_decisions: List[Tuple[ScalingPolicy, ScalingDirection]]):
        """⚙️ Process and execute scaling decisions"""
        if self.scaling_in_progress:
            return
        
        self.scaling_in_progress = True
        
        try:
            # Prioritize scaling decisions (scale up > scale down)
            scale_up_decisions = [d for d in scaling_decisions if d[1] == ScalingDirection.SCALE_UP]
            scale_down_decisions = [d for d in scaling_decisions if d[1] == ScalingDirection.SCALE_DOWN]
            
            # Process scale up first
            for policy, direction in scale_up_decisions:
                await self._execute_scaling(policy, direction)
                break  # Only one scale up action per cycle
            
            # Process scale down if no scale up occurred
            if not scale_up_decisions and scale_down_decisions:
                policy, direction = scale_down_decisions[0]
                await self._execute_scaling(policy, direction)
            
        finally:
            self.scaling_in_progress = False
    
    async def _execute_scaling(self, policy: ScalingPolicy, direction: ScalingDirection):
        """🚀 Execute scaling action"""
        try:
            current_time = time.time()
            current_agents = await self._get_current_agent_count(policy)
            
            if direction == ScalingDirection.SCALE_UP:
                target_count = min(current_agents + policy.scale_up_step, policy.max_agents)
                agents_to_add = target_count - current_agents
                
                if agents_to_add > 0:
                    success = await self._scale_up_agents(agents_to_add)
                    if success:
                        self.last_scaling_action[policy.policy_id] = current_time
                        
                        # Record scaling event
                        self.scaling_history.append({
                            'timestamp': datetime.now(),
                            'policy_id': policy.policy_id,
                            'direction': direction.value,
                            'from_count': current_agents,
                            'to_count': target_count,
                            'success': True
                        })
                        
                        logger.info(f"🚀 Scaled up: {current_agents} → {target_count} agents")
            
            elif direction == ScalingDirection.SCALE_DOWN:
                target_count = max(current_agents - policy.scale_down_step, policy.min_agents)
                agents_to_remove = current_agents - target_count
                
                if agents_to_remove > 0:
                    success = await self._scale_down_agents(agents_to_remove)
                    if success:
                        self.last_scaling_action[policy.policy_id] = current_time
                        
                        # Record scaling event
                        self.scaling_history.append({
                            'timestamp': datetime.now(),
                            'policy_id': policy.policy_id,
                            'direction': direction.value,
                            'from_count': current_agents,
                            'to_count': target_count,
                            'success': True
                        })
                        
                        logger.info(f"📉 Scaled down: {current_agents} → {target_count} agents")
        
        except Exception as e:
            logger.error(f"❌ Scaling execution failed: {e}")
    
    async def _scale_up_agents(self, count: int) -> bool:
        """📈 Scale up by adding new agents"""
        try:
            # Check system resources before scaling
            if not await self.system_resources.can_support_more_agents(count):
                logger.warning("⚠️ Insufficient system resources for scaling up")
                return False
            
            # Create new agents
            new_agents = []
            for i in range(count):
                agent_id = f"scaled_agent_{int(time.time())}_{i}"
                agent = await self.agent_factory.create_agent(agent_id, "DataCollector")
                
                if agent:
                    await agent.spawn()
                    new_agents.append(agent)
            
            if new_agents:
                logger.info(f"📈 Successfully created {len(new_agents)} new agents")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"❌ Scale up failed: {e}")
            return False
    
    async def _scale_down_agents(self, count: int) -> bool:
        """📉 Scale down by gracefully removing agents"""
        try:
            # Find agents to remove (prefer idle agents)
            agents_to_remove = await self._select_agents_for_removal(count)
            
            if not agents_to_remove:
                return False
            
            # Gracefully terminate selected agents
            termination_tasks = []
            for agent_id in agents_to_remove:
                termination_tasks.append(self._gracefully_terminate_agent(agent_id))
            
            results = await asyncio.gather(*termination_tasks, return_exceptions=True)
            successful_terminations = sum(1 for r in results if r is True)
            
            if successful_terminations > 0:
                logger.info(f"📉 Successfully removed {successful_terminations} agents")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"❌ Scale down failed: {e}")
            return False
    
    async def _select_agents_for_removal(self, count: int) -> List[str]:
        """🎯 Select optimal agents for removal"""
        # Score agents for removal (lower score = better candidate)
        agent_scores = []
        
        for agent_id, metrics in self.agent_metrics.items():
            # Factors: low task count, low CPU, good health, recent activity
            score = (
                metrics.active_tasks * 2.0 +           # Prefer agents with fewer tasks
                metrics.cpu_usage / 100.0 +            # Prefer lower CPU usage
                (1.0 - metrics.health_score) +         # Prefer healthier agents (reverse)
                metrics.error_rate * 3.0               # Avoid agents with high error rates
            )
            
            agent_scores.append((agent_id, score))
        
        # Sort by score and select candidates
        agent_scores.sort(key=lambda x: x[1])
        selected_agents = [agent_id for agent_id, _ in agent_scores[:count]]
        
        return selected_agents
    
    async def _gracefully_terminate_agent(self, agent_id: str) -> bool:
        """👋 Gracefully terminate an agent"""
        try:
            # First, stop assigning new tasks
            await self.load_balancer.exclude_agent(agent_id)
            
            # Wait for current tasks to complete (with timeout)
            timeout_seconds = 60
            start_time = time.time()
            
            while time.time() - start_time < timeout_seconds:
                metrics = self.agent_metrics.get(agent_id)
                if not metrics or metrics.active_tasks == 0:
                    break
                await asyncio.sleep(2)
            
            # Send termination signal
            await self.message_bus.publish_to_agent(
                target_agent=agent_id,
                event_name="graceful_termination",
                payload={'reason': 'scaling_down'}
            )
            
            # Remove from tracking
            if agent_id in self.agent_metrics:
                del self.agent_metrics[agent_id]
            
            logger.info(f"👋 Agent {agent_id} gracefully terminated")
            return True
            
        except Exception as e:
            logger.error(f"❌ Graceful termination failed for {agent_id}: {e}")
            return False
    
    async def update_agent_metrics(self, agent_id: str, metrics: Dict[str, Any]):
        """📊 Update agent performance metrics"""
        if agent_id not in self.agent_metrics:
            self.agent_metrics[agent_id] = AgentMetrics(agent_id=agent_id)
        
        agent_metrics = self.agent_metrics[agent_id]
        
        # Update metrics
        agent_metrics.cpu_usage = metrics.get('cpu_usage', 0.0)
        agent_metrics.memory_usage = metrics.get('memory_usage', 0.0)
        agent_metrics.active_tasks = metrics.get('active_tasks', 0)
        agent_metrics.completed_tasks = metrics.get('completed_tasks', 0)
        agent_metrics.failed_tasks = metrics.get('failed_tasks', 0)
        agent_metrics.avg_response_time = metrics.get('avg_response_time', 0.0)
        agent_metrics.throughput = metrics.get('throughput', 0.0)
        agent_metrics.error_rate = metrics.get('error_rate', 0.0)
        agent_metrics.last_heartbeat = datetime.now()
        
        # Calculate health score
        agent_metrics.health_score = await self._calculate_health_score(agent_metrics)
    
    async def _calculate_health_score(self, metrics: AgentMetrics) -> float:
        """💚 Calculate agent health score"""
        score = 1.0
        
        # Penalize high CPU usage
        if metrics.cpu_usage > 90:
            score -= 0.3
        elif metrics.cpu_usage > 75:
            score -= 0.1
        
        # Penalize high error rate
        if metrics.error_rate > 0.1:  # More than 10% errors
            score -= 0.4
        elif metrics.error_rate > 0.05:  # More than 5% errors
            score -= 0.2
        
        # Penalize high response time
        if metrics.avg_response_time > 5000:  # More than 5 seconds
            score -= 0.2
        elif metrics.avg_response_time > 2000:  # More than 2 seconds
            score -= 0.1
        
        # Penalize if no recent heartbeat
        if metrics.last_heartbeat:
            time_since_heartbeat = (datetime.now() - metrics.last_heartbeat).seconds
            if time_since_heartbeat > 300:  # More than 5 minutes
                score -= 0.5
            elif time_since_heartbeat > 120:  # More than 2 minutes
                score -= 0.2
        
        return max(0.0, min(1.0, score))
    
    async def get_scaling_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive scaling system status"""
        current_agents = len(self.agent_metrics)
        
        # Policy statuses
        policy_statuses = {}
        for policy_id, policy in self.scaling_policies.items():
            is_cooldown = await self._is_in_cooldown(policy)
            current_metric = await self._get_current_metric_value(policy.metric)
            
            policy_statuses[policy_id] = {
                'metric': policy.metric.value,
                'current_value': current_metric,
                'scale_up_threshold': policy.scale_up_threshold,
                'scale_down_threshold': policy.scale_down_threshold,
                'in_cooldown': is_cooldown,
                'min_agents': policy.min_agents,
                'max_agents': policy.max_agents
            }
        
        # Agent health summary
        healthy_agents = sum(1 for m in self.agent_metrics.values() if m.health_score > 0.8)
        degraded_agents = sum(1 for m in self.agent_metrics.values() if 0.5 <= m.health_score <= 0.8)
        unhealthy_agents = sum(1 for m in self.agent_metrics.values() if m.health_score < 0.5)
        
        # Resource utilization
        avg_cpu = statistics.mean([m.cpu_usage for m in self.agent_metrics.values()]) if self.agent_metrics else 0
        avg_memory = statistics.mean([m.memory_usage for m in self.agent_metrics.values()]) if self.agent_metrics else 0
        total_active_tasks = sum(m.active_tasks for m in self.agent_metrics.values())
        
        return {
            'current_agents': current_agents,
            'scaling_in_progress': self.scaling_in_progress,
            'policies': policy_statuses,
            'agent_health': {
                'healthy': healthy_agents,
                'degraded': degraded_agents,
                'unhealthy': unhealthy_agents
            },
            'resource_utilization': {
                'avg_cpu_usage': avg_cpu,
                'avg_memory_usage': avg_memory,
                'total_active_tasks': total_active_tasks
            },
            'scaling_history_count': len(self.scaling_history),
            'last_scaling_actions': {
                policy_id: datetime.fromtimestamp(timestamp).isoformat()
                for policy_id, timestamp in self.last_scaling_action.items()
            }
        }


class IntelligentLoadBalancer:
    """⚖️ Intelligent load balancing system"""
    
    def __init__(self, scaling_manager):
        self.scaling_manager = scaling_manager
        self.load_distribution_weights = {}
        self.excluded_agents = set()
    
    async def optimization_loop(self):
        """🔄 Continuous load balancing optimization"""
        while True:
            try:
                await self._optimize_load_distribution()
                await asyncio.sleep(30)
            except Exception as e:
                logger.error(f"❌ Load balancing optimization error: {e}")
                await asyncio.sleep(10)
    
    async def _optimize_load_distribution(self):
        """⚖️ Optimize task distribution across agents"""
        # This would implement intelligent load distribution
        # For now, just update weights based on performance
        pass
    
    async def exclude_agent(self, agent_id: str):
        """🚫 Exclude agent from load balancing"""
        self.excluded_agents.add(agent_id)


class MetricsCollector:
    """📊 System metrics collection"""
    
    def __init__(self, scaling_manager):
        self.scaling_manager = scaling_manager
    
    async def start_collection(self):
        """🔍 Start metrics collection loop"""
        while True:
            try:
                await self._collect_agent_metrics()
                await asyncio.sleep(10)  # Collect every 10 seconds
            except Exception as e:
                logger.error(f"❌ Metrics collection error: {e}")
                await asyncio.sleep(5)
    
    async def _collect_agent_metrics(self):
        """📊 Collect metrics from all agents"""
        # This would collect real metrics from agents
        # For now, simulate metric collection
        pass


class TrendPredictor:
    """📈 Load trend prediction"""
    
    def __init__(self):
        self.historical_data = []
    
    async def predict_load_trend(self) -> str:
        """📈 Predict load trend direction"""
        # Simple trend prediction - in production would use ML
        return "stable"


class SystemResourceMonitor:
    """🖥️ System resource monitoring"""
    
    def __init__(self):
        self.cpu_usage = 0.0
        self.memory_usage = 0.0
        self.available_memory = 0
    
    async def monitor_resources(self):
        """🔍 Monitor system resources"""
        while True:
            try:
                self.cpu_usage = psutil.cpu_percent()
                self.memory_usage = psutil.virtual_memory().percent
                self.available_memory = psutil.virtual_memory().available
                await asyncio.sleep(5)
            except Exception as e:
                logger.error(f"❌ Resource monitoring error: {e}")
                await asyncio.sleep(10)
    
    async def can_support_more_agents(self, count: int) -> bool:
        """🖥️ Check if system can support more agents"""
        # Estimate resource requirements per agent
        estimated_memory_per_agent = 100 * 1024 * 1024  # 100MB per agent
        required_memory = count * estimated_memory_per_agent
        
        return (self.memory_usage < 80.0 and 
                self.available_memory > required_memory and
                self.cpu_usage < 85.0)