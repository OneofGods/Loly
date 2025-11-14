#!/usr/bin/env python3
"""
🔥💀 MULTI-AGENT SYSTEM ORCHESTRATOR - TRUE AUTONOMOUS COORDINATION 💀🔥
Agent Poly Loly Double Zero: Complete Multi-Agent System Management

ORCHESTRATION FEATURES:
- Autonomous agent lifecycle management
- Intelligent load balancing and scaling
- Real-time system coordination
- Fault-tolerant multi-agent workflows
- Self-organizing agent topologies
"""

import asyncio
import json
import time
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Type
import logging
from collections import defaultdict, deque
from enum import Enum
import subprocess
import sys
import os

# Import all agent types
from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY
from agents.data_collector_agent import DataCollectorAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.predictor_agent import PredictorAgent
from agents.coordinator_agent import CoordinatorAgent
from agents.monitor_agent import MonitorAgent

logger = logging.getLogger(__name__)

class AgentTopology(Enum):
    """🌐 Agent deployment topologies"""
    FLAT = "flat"           # All agents at same level
    HIERARCHICAL = "hierarchical"  # Tree structure with coordinator at top
    MESH = "mesh"           # Fully connected mesh
    PIPELINE = "pipeline"   # Sequential processing chain
    HYBRID = "hybrid"       # Combination of topologies

class SystemState(Enum):
    """🎯 Overall system state"""
    INITIALIZING = "initializing"
    STARTING = "starting"
    RUNNING = "running"
    SCALING = "scaling"
    DEGRADED = "degraded"
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"

class AgentOrchestrator:
    """
    🎯 MASTER ORCHESTRATOR FOR MULTI-AGENT SYSTEM
    
    Coordinates:
    - Agent spawning and termination
    - Load balancing and resource allocation
    - System topology optimization
    - Fault detection and recovery
    - Performance monitoring and scaling
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        
        # System identification
        self.orchestrator_id = f"orchestrator_{uuid.uuid4().hex[:8]}"
        self.system_id = f"poly_loly_system_{int(time.time())}"
        
        # Agent management
        self.active_agents = {}  # agent_id -> agent_instance
        self.agent_configs = {}  # agent_id -> agent_config
        self.agent_processes = {}  # agent_id -> process_info
        self.agent_health = {}  # agent_id -> health_metrics
        
        # System state
        self.system_state = SystemState.INITIALIZING
        self.topology = AgentTopology.HYBRID
        self.start_time = None
        self.last_health_check = 0
        
        # Configuration
        self.max_agents = self.config.get('max_agents', 20)
        self.min_agents = self.config.get('min_agents', 5)
        self.scaling_threshold = self.config.get('scaling_threshold', 0.8)
        self.health_check_interval = self.config.get('health_check_interval', 30)
        self.auto_scaling = self.config.get('auto_scaling', True)
        
        # Agent specifications
        self.agent_specifications = {
            'data_collector': {
                'class': DataCollectorAgent,
                'min_instances': 1,
                'max_instances': 3,
                'capabilities': ['data_collection', 'api_access'],
                'resource_requirements': {'memory_mb': 256, 'cpu_cores': 0.5}
            },
            'analyzer': {
                'class': AnalyzerAgent,
                'min_instances': 1,
                'max_instances': 2,
                'capabilities': ['analysis', 'pattern_recognition'],
                'resource_requirements': {'memory_mb': 512, 'cpu_cores': 1.0}
            },
            'predictor': {
                'class': PredictorAgent,
                'min_instances': 1,
                'max_instances': 2,
                'capabilities': ['machine_learning', 'prediction'],
                'resource_requirements': {'memory_mb': 1024, 'cpu_cores': 1.5}
            },
            'coordinator': {
                'class': CoordinatorAgent,
                'min_instances': 1,
                'max_instances': 1,
                'capabilities': ['coordination', 'workflow_management'],
                'resource_requirements': {'memory_mb': 512, 'cpu_cores': 1.0}
            },
            'monitor': {
                'class': MonitorAgent,
                'min_instances': 1,
                'max_instances': 1,
                'capabilities': ['monitoring', 'health_checks'],
                'resource_requirements': {'memory_mb': 256, 'cpu_cores': 0.5}
            }
        }
        
        # System metrics
        self.system_metrics = {
            'total_agents_spawned': 0,
            'total_agents_terminated': 0,
            'system_uptime': 0,
            'total_tasks_processed': 0,
            'average_response_time': 0.0,
            'error_rate': 0.0,
            'scaling_events': 0,
            'recovery_events': 0
        }
        
        # Event tracking
        self.system_events = deque(maxlen=1000)
        self.performance_history = deque(maxlen=500)
        
        logger.info(f"🎯 AgentOrchestrator {self.orchestrator_id} initialized")
    
    async def initialize_system(self):
        """🚀 Initialize the complete multi-agent system"""
        try:
            self.system_state = SystemState.INITIALIZING
            self._log_event('system_initialization_started')
            
            # Create required directories
            await self._setup_environment()
            
            # Initialize core components
            await self._initialize_core_components()
            
            # Spawn minimum required agents
            await self._spawn_minimum_agents()
            
            # Set up inter-agent communication
            await self._setup_communication_topology()
            
            # Start system monitoring
            await self._start_system_monitoring()
            
            # Mark system as running
            self.system_state = SystemState.RUNNING
            self.start_time = datetime.now()
            
            self._log_event('system_initialization_completed')
            logger.info(f"✅ Multi-agent system initialized successfully")
            
            return True
            
        except Exception as e:
            self.system_state = SystemState.ERROR
            self._log_event('system_initialization_failed', {'error': str(e)})
            logger.error(f"❌ System initialization failed: {e}")
            return False
    
    async def _setup_environment(self):
        """🔧 Set up system environment"""
        required_dirs = ['logs', 'data', 'models', 'temp']
        
        for dir_name in required_dirs:
            dir_path = os.path.join(os.getcwd(), dir_name)
            os.makedirs(dir_path, exist_ok=True)
        
        logger.info("🔧 Environment setup completed")
    
    async def _initialize_core_components(self):
        """⚙️ Initialize core system components"""
        # Initialize global agent registry
        global AGENT_REGISTRY
        
        # Set up message routing
        await self._setup_message_routing()
        
        # Initialize metrics collection
        await self._setup_metrics_collection()
        
        logger.info("⚙️ Core components initialized")
    
    async def _spawn_minimum_agents(self):
        """🔥 Spawn minimum required agents"""
        for agent_type, spec in self.agent_specifications.items():
            min_instances = spec['min_instances']
            
            for i in range(min_instances):
                agent_id = f"{agent_type}_{i+1:03d}"
                await self._spawn_agent(agent_type, agent_id)
        
        logger.info(f"🔥 Spawned minimum agents: {len(self.active_agents)} active")
    
    async def _spawn_agent(self, agent_type: str, agent_id: str = None, config: Dict[str, Any] = None) -> bool:
        """🚀 Spawn new agent instance"""
        try:
            if agent_type not in self.agent_specifications:
                raise ValueError(f"Unknown agent type: {agent_type}")
            
            spec = self.agent_specifications[agent_type]
            agent_class = spec['class']
            
            # Generate agent ID if not provided
            if not agent_id:
                agent_id = f"{agent_type}_{uuid.uuid4().hex[:8]}"
            
            # Check if we can spawn more agents of this type
            current_count = len([aid for aid in self.active_agents if aid.startswith(agent_type)])
            if current_count >= spec['max_instances']:
                logger.warning(f"⚠️ Cannot spawn {agent_type}: max instances ({spec['max_instances']}) reached")
                return False
            
            # Create agent configuration
            agent_config = config or {}
            agent_config.update({
                'agent_type': agent_type,
                'orchestrator_id': self.orchestrator_id,
                'system_id': self.system_id,
                'capabilities': spec['capabilities'],
                'resource_requirements': spec['resource_requirements']
            })
            
            # Instantiate agent
            agent = agent_class(agent_id=agent_id, config=agent_config)
            
            # Spawn the agent
            spawn_success = await agent.spawn()
            
            if spawn_success:
                # Register agent
                self.active_agents[agent_id] = agent
                self.agent_configs[agent_id] = agent_config
                AGENT_REGISTRY.register_agent(agent)
                
                # Initialize health tracking
                self.agent_health[agent_id] = {
                    'status': 'healthy',
                    'last_heartbeat': time.time(),
                    'spawn_time': time.time(),
                    'task_count': 0,
                    'error_count': 0,
                    'performance_score': 1.0
                }
                
                # Update metrics
                self.system_metrics['total_agents_spawned'] += 1
                
                # Log event
                self._log_event('agent_spawned', {
                    'agent_id': agent_id,
                    'agent_type': agent_type,
                    'capabilities': spec['capabilities']
                })
                
                logger.info(f"🚀 Spawned {agent_type} agent: {agent_id}")
                return True
            else:
                logger.error(f"❌ Failed to spawn {agent_type} agent: {agent_id}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error spawning {agent_type} agent: {e}")
            return False
    
    async def _terminate_agent(self, agent_id: str, reason: str = "manual") -> bool:
        """🛑 Terminate agent instance"""
        try:
            if agent_id not in self.active_agents:
                logger.warning(f"⚠️ Agent {agent_id} not found for termination")
                return False
            
            agent = self.active_agents[agent_id]
            
            # Graceful termination
            await agent.terminate()
            
            # Clean up tracking
            del self.active_agents[agent_id]
            del self.agent_configs[agent_id]
            if agent_id in self.agent_health:
                del self.agent_health[agent_id]
            
            # Unregister from global registry
            AGENT_REGISTRY.unregister_agent(agent_id)
            
            # Update metrics
            self.system_metrics['total_agents_terminated'] += 1
            
            # Log event
            self._log_event('agent_terminated', {
                'agent_id': agent_id,
                'reason': reason
            })
            
            logger.info(f"🛑 Terminated agent: {agent_id} (reason: {reason})")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error terminating agent {agent_id}: {e}")
            return False
    
    async def _setup_communication_topology(self):
        """🌐 Set up inter-agent communication topology"""
        if self.topology == AgentTopology.HIERARCHICAL:
            await self._setup_hierarchical_topology()
        elif self.topology == AgentTopology.MESH:
            await self._setup_mesh_topology()
        elif self.topology == AgentTopology.PIPELINE:
            await self._setup_pipeline_topology()
        else:  # HYBRID
            await self._setup_hybrid_topology()
        
        logger.info(f"🌐 Communication topology set up: {self.topology.value}")
    
    async def _setup_hierarchical_topology(self):
        """🌳 Set up hierarchical communication topology"""
        # Find coordinator agent
        coordinator_id = None
        for agent_id in self.active_agents:
            if agent_id.startswith('coordinator'):
                coordinator_id = agent_id
                break
        
        if coordinator_id:
            # Connect all other agents to coordinator
            for agent_id in self.active_agents:
                if agent_id != coordinator_id:
                    agent = self.active_agents[agent_id]
                    coordinator = self.active_agents[coordinator_id]
                    
                    # Set up bidirectional communication
                    agent.subscribers.add(coordinator_id)
                    coordinator.subscribers.add(agent_id)
    
    async def _setup_mesh_topology(self):
        """🕸️ Set up mesh communication topology"""
        # Connect every agent to every other agent
        agent_ids = list(self.active_agents.keys())
        
        for i, agent_id1 in enumerate(agent_ids):
            for j, agent_id2 in enumerate(agent_ids):
                if i != j:
                    agent1 = self.active_agents[agent_id1]
                    agent1.subscribers.add(agent_id2)
    
    async def _setup_pipeline_topology(self):
        """🔗 Set up pipeline communication topology"""
        # Create processing pipeline: DataCollector -> Analyzer -> Predictor
        pipeline_order = ['data_collector', 'analyzer', 'predictor']
        pipeline_agents = []
        
        for agent_type in pipeline_order:
            for agent_id in self.active_agents:
                if agent_id.startswith(agent_type):
                    pipeline_agents.append(agent_id)
                    break
        
        # Connect agents in pipeline order
        for i in range(len(pipeline_agents) - 1):
            current_agent = self.active_agents[pipeline_agents[i]]
            next_agent_id = pipeline_agents[i + 1]
            current_agent.subscribers.add(next_agent_id)
    
    async def _setup_hybrid_topology(self):
        """🔀 Set up hybrid communication topology"""
        # Coordinator at the center, specialized connections
        coordinator_id = None
        monitor_id = None
        
        for agent_id in self.active_agents:
            if agent_id.startswith('coordinator'):
                coordinator_id = agent_id
            elif agent_id.startswith('monitor'):
                monitor_id = agent_id
        
        if coordinator_id:
            # Connect coordinator to all agents
            coordinator = self.active_agents[coordinator_id]
            for agent_id in self.active_agents:
                if agent_id != coordinator_id:
                    coordinator.subscribers.add(agent_id)
                    agent = self.active_agents[agent_id]
                    agent.subscribers.add(coordinator_id)
        
        if monitor_id:
            # Connect monitor to all agents for health monitoring
            monitor = self.active_agents[monitor_id]
            for agent_id in self.active_agents:
                if agent_id != monitor_id:
                    monitor.subscribers.add(agent_id)
        
        # Set up specialized data flow
        await self._setup_specialized_data_flows()
    
    async def _setup_specialized_data_flows(self):
        """📊 Set up specialized data flows between agents"""
        # Data Collector -> Analyzer
        data_collectors = [aid for aid in self.active_agents if aid.startswith('data_collector')]
        analyzers = [aid for aid in self.active_agents if aid.startswith('analyzer')]
        
        for dc_id in data_collectors:
            for analyzer_id in analyzers:
                self.active_agents[dc_id].subscribers.add(analyzer_id)
        
        # Analyzer -> Predictor
        predictors = [aid for aid in self.active_agents if aid.startswith('predictor')]
        
        for analyzer_id in analyzers:
            for predictor_id in predictors:
                self.active_agents[analyzer_id].subscribers.add(predictor_id)
    
    async def _setup_message_routing(self):
        """📨 Set up global message routing"""
        # This would implement the global message router
        # For now, using the existing agent registry routing
        pass
    
    async def _setup_metrics_collection(self):
        """📊 Set up system metrics collection"""
        # Initialize performance tracking
        self.performance_history.append({
            'timestamp': time.time(),
            'active_agents': len(self.active_agents),
            'system_state': self.system_state.value
        })
    
    async def _start_system_monitoring(self):
        """📊 Start continuous system monitoring"""
        asyncio.create_task(self._system_health_monitor())
        asyncio.create_task(self._performance_monitor())
        asyncio.create_task(self._auto_scaling_monitor())
        
        logger.info("📊 System monitoring started")
    
    async def _system_health_monitor(self):
        """💚 Continuous system health monitoring"""
        while self.system_state not in [SystemState.STOPPED, SystemState.ERROR]:
            try:
                await self._check_agent_health()
                await self._update_system_health()
                await asyncio.sleep(self.health_check_interval)
                
            except Exception as e:
                logger.error(f"❌ Health monitoring error: {e}")
                await asyncio.sleep(self.health_check_interval)
    
    async def _performance_monitor(self):
        """📈 Continuous performance monitoring"""
        while self.system_state not in [SystemState.STOPPED, SystemState.ERROR]:
            try:
                await self._collect_performance_metrics()
                await self._analyze_performance_trends()
                await asyncio.sleep(60)  # Every minute
                
            except Exception as e:
                logger.error(f"❌ Performance monitoring error: {e}")
                await asyncio.sleep(60)
    
    async def _auto_scaling_monitor(self):
        """⚖️ Continuous auto-scaling monitoring"""
        if not self.auto_scaling:
            return
            
        while self.system_state not in [SystemState.STOPPED, SystemState.ERROR]:
            try:
                await self._evaluate_scaling_needs()
                await asyncio.sleep(120)  # Every 2 minutes
                
            except Exception as e:
                logger.error(f"❌ Auto-scaling monitoring error: {e}")
                await asyncio.sleep(120)
    
    async def _check_agent_health(self):
        """🏥 Check health of all agents"""
        current_time = time.time()
        unhealthy_agents = []
        
        for agent_id, agent in self.active_agents.items():
            health_info = self.agent_health.get(agent_id, {})
            
            # Check if agent is responsive
            last_heartbeat = health_info.get('last_heartbeat', 0)
            if current_time - last_heartbeat > 60:  # 1 minute timeout
                unhealthy_agents.append(agent_id)
                health_info['status'] = 'unresponsive'
            else:
                health_info['status'] = 'healthy'
            
            # Update agent-specific health metrics
            if hasattr(agent, 'health_metrics'):
                health_info.update(agent.health_metrics)
        
        # Handle unhealthy agents
        for agent_id in unhealthy_agents:
            await self._handle_unhealthy_agent(agent_id)
    
    async def _handle_unhealthy_agent(self, agent_id: str):
        """🚨 Handle unhealthy agent"""
        agent_type = agent_id.split('_')[0]
        
        logger.warning(f"🚨 Unhealthy agent detected: {agent_id}")
        
        # Try to recover agent first
        recovery_success = await self._attempt_agent_recovery(agent_id)
        
        if not recovery_success:
            # Terminate and replace agent
            await self._terminate_agent(agent_id, "health_failure")
            
            # Spawn replacement if below minimum
            current_count = len([aid for aid in self.active_agents if aid.startswith(agent_type)])
            min_required = self.agent_specifications[agent_type]['min_instances']
            
            if current_count < min_required:
                await self._spawn_agent(agent_type)
                self.system_metrics['recovery_events'] += 1
    
    async def _attempt_agent_recovery(self, agent_id: str) -> bool:
        """🔧 Attempt to recover unhealthy agent"""
        try:
            if agent_id not in self.active_agents:
                return False
            
            agent = self.active_agents[agent_id]
            
            # Send recovery signal
            await agent.send_message(agent_id, 'recovery_request', {
                'recovery_type': 'health_check',
                'orchestrator_id': self.orchestrator_id
            })
            
            # Wait for response
            await asyncio.sleep(5)
            
            # Check if agent is now responsive
            if hasattr(agent, 'last_heartbeat'):
                if time.time() - agent.last_heartbeat < 10:
                    logger.info(f"✅ Agent {agent_id} recovered successfully")
                    return True
            
        except Exception as e:
            logger.error(f"❌ Agent recovery failed for {agent_id}: {e}")
        
        return False
    
    async def _update_system_health(self):
        """💚 Update overall system health status"""
        healthy_agents = len([
            aid for aid, health in self.agent_health.items()
            if health.get('status') == 'healthy'
        ])
        
        total_agents = len(self.active_agents)
        health_ratio = healthy_agents / total_agents if total_agents > 0 else 0
        
        if health_ratio >= 0.9:
            new_state = SystemState.RUNNING
        elif health_ratio >= 0.7:
            new_state = SystemState.DEGRADED
        else:
            new_state = SystemState.ERROR
        
        if new_state != self.system_state:
            old_state = self.system_state
            self.system_state = new_state
            
            self._log_event('system_state_change', {
                'old_state': old_state.value,
                'new_state': new_state.value,
                'health_ratio': health_ratio
            })
            
            logger.info(f"🔄 System state changed: {old_state.value} → {new_state.value}")
    
    async def _collect_performance_metrics(self):
        """📊 Collect system performance metrics"""
        current_time = time.time()
        
        # Calculate system uptime
        if self.start_time and isinstance(self.start_time, datetime):
            self.system_metrics['system_uptime'] = (datetime.now() - self.start_time).total_seconds()
        else:
            self.system_metrics['system_uptime'] = 0.0
        
        # Collect agent performance data
        agent_response_times = []
        total_tasks = 0
        total_errors = 0
        
        for agent_id, agent in self.active_agents.items():
            if hasattr(agent, 'memory') and hasattr(agent.memory, 'experiences'):
                experiences = agent.memory.experiences
                if experiences:
                    # Recent experiences (last hour)
                    recent_experiences = [
                        exp for exp in experiences
                        if exp.get('timestamp', 0) > current_time - 3600
                    ]
                    
                    if recent_experiences:
                        avg_duration = sum(exp.get('duration', 0) for exp in recent_experiences) / len(recent_experiences)
                        agent_response_times.append(avg_duration)
                        
                        total_tasks += len(recent_experiences)
                        total_errors += len([exp for exp in recent_experiences if exp.get('outcome') == 'failure'])
        
        # Update system metrics
        if agent_response_times:
            self.system_metrics['average_response_time'] = sum(agent_response_times) / len(agent_response_times)
        
        self.system_metrics['total_tasks_processed'] = total_tasks
        if total_tasks > 0:
            self.system_metrics['error_rate'] = total_errors / total_tasks
        
        # Record performance snapshot
        self.performance_history.append({
            'timestamp': current_time,
            'active_agents': len(self.active_agents),
            'healthy_agents': len([h for h in self.agent_health.values() if h.get('status') == 'healthy']),
            'average_response_time': self.system_metrics['average_response_time'],
            'error_rate': self.system_metrics['error_rate'],
            'system_state': self.system_state.value
        })
    
    async def _analyze_performance_trends(self):
        """📈 Analyze system performance trends"""
        if len(self.performance_history) < 10:
            return
        
        recent_performance = list(self.performance_history)[-10:]  # Last 10 measurements
        
        # Analyze trends
        response_times = [p['average_response_time'] for p in recent_performance]
        error_rates = [p['error_rate'] for p in recent_performance]
        
        # Check for degrading performance
        if len(response_times) >= 5:
            recent_avg_response = sum(response_times[-5:]) / 5
            earlier_avg_response = sum(response_times[-10:-5]) / 5
            
            if recent_avg_response > earlier_avg_response * 1.5:  # 50% increase
                self._log_event('performance_degradation_detected', {
                    'metric': 'response_time',
                    'recent_avg': recent_avg_response,
                    'earlier_avg': earlier_avg_response
                })
        
        if len(error_rates) >= 5:
            recent_avg_errors = sum(error_rates[-5:]) / 5
            if recent_avg_errors > 0.1:  # 10% error rate
                self._log_event('high_error_rate_detected', {
                    'error_rate': recent_avg_errors
                })
    
    async def _evaluate_scaling_needs(self):
        """⚖️ Evaluate if system needs scaling"""
        if not self.auto_scaling:
            return
        
        # Check overall system load
        total_load = 0
        agent_loads = []
        
        for agent_id, agent in self.active_agents.items():
            if hasattr(agent, 'running_tasks'):
                load = len(agent.running_tasks) / getattr(agent, 'max_concurrent_tasks', 1)
                agent_loads.append(load)
                total_load += load
        
        if agent_loads:
            avg_load = total_load / len(agent_loads)
            
            # Scale up if average load is high
            if avg_load > self.scaling_threshold:
                await self._scale_up_system()
            
            # Scale down if average load is very low
            elif avg_load < 0.3 and len(self.active_agents) > self.min_agents:
                await self._scale_down_system()
    
    async def _scale_up_system(self):
        """📈 Scale up the system"""
        self.system_state = SystemState.SCALING
        
        # Determine which agent types need scaling
        for agent_type, spec in self.agent_specifications.items():
            current_count = len([aid for aid in self.active_agents if aid.startswith(agent_type)])
            
            if current_count < spec['max_instances']:
                await self._spawn_agent(agent_type)
                self.system_metrics['scaling_events'] += 1
                
                self._log_event('system_scaled_up', {
                    'agent_type': agent_type,
                    'new_count': current_count + 1
                })
                
                logger.info(f"📈 Scaled up {agent_type}: {current_count} → {current_count + 1}")
                break  # Scale one type at a time
        
        self.system_state = SystemState.RUNNING
    
    async def _scale_down_system(self):
        """📉 Scale down the system"""
        self.system_state = SystemState.SCALING
        
        # Find agent types that can be scaled down
        for agent_type, spec in self.agent_specifications.items():
            current_agents = [aid for aid in self.active_agents if aid.startswith(agent_type)]
            
            if len(current_agents) > spec['min_instances']:
                # Terminate the least utilized agent
                agent_to_terminate = current_agents[-1]  # Simple strategy
                await self._terminate_agent(agent_to_terminate, "scale_down")
                self.system_metrics['scaling_events'] += 1
                
                self._log_event('system_scaled_down', {
                    'agent_type': agent_type,
                    'terminated_agent': agent_to_terminate
                })
                
                logger.info(f"📉 Scaled down {agent_type}: terminated {agent_to_terminate}")
                break
        
        self.system_state = SystemState.RUNNING
    
    def _log_event(self, event_type: str, details: Dict[str, Any] = None):
        """📝 Log system event"""
        event = {
            'timestamp': time.time(),
            'event_type': event_type,
            'details': details or {},
            'system_state': self.system_state.value,
            'active_agents': len(self.active_agents)
        }
        
        self.system_events.append(event)
        logger.debug(f"📝 Event logged: {event_type}")
    
    async def shutdown_system(self):
        """🛑 Gracefully shutdown the entire system"""
        try:
            self.system_state = SystemState.STOPPING
            self._log_event('system_shutdown_initiated')
            
            logger.info("🛑 Initiating system shutdown...")
            
            # Terminate all agents gracefully
            agent_ids = list(self.active_agents.keys())
            for agent_id in agent_ids:
                await self._terminate_agent(agent_id, "system_shutdown")
            
            # Clean up resources
            await self._cleanup_resources()
            
            self.system_state = SystemState.STOPPED
            self._log_event('system_shutdown_completed')
            
            logger.info("✅ System shutdown completed successfully")
            
        except Exception as e:
            self.system_state = SystemState.ERROR
            logger.error(f"❌ Error during system shutdown: {e}")
    
    async def _cleanup_resources(self):
        """🧹 Clean up system resources"""
        # Clear tracking dictionaries
        self.active_agents.clear()
        self.agent_configs.clear()
        self.agent_health.clear()
        
        # Clear global registry
        AGENT_REGISTRY.agents.clear()
        AGENT_REGISTRY.agent_types.clear()
        AGENT_REGISTRY.message_router.clear()
    
    # =================== PUBLIC API ===================
    
    async def get_system_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive system status"""
        return {
            'orchestrator_id': self.orchestrator_id,
            'system_id': self.system_id,
            'system_state': self.system_state.value,
            'topology': self.topology.value,
            'uptime_seconds': self.system_metrics['system_uptime'],
            'active_agents': len(self.active_agents),
            'agent_breakdown': {
                agent_type: len([aid for aid in self.active_agents if aid.startswith(agent_type)])
                for agent_type in self.agent_specifications
            },
            'healthy_agents': len([h for h in self.agent_health.values() if h.get('status') == 'healthy']),
            'system_metrics': self.system_metrics,
            'recent_events': list(self.system_events)[-10:],  # Last 10 events
            'performance_summary': {
                'average_response_time': self.system_metrics['average_response_time'],
                'error_rate': self.system_metrics['error_rate'],
                'total_tasks_processed': self.system_metrics['total_tasks_processed']
            }
        }
    
    async def get_agent_details(self) -> Dict[str, Any]:
        """🤖 Get detailed agent information"""
        agent_details = {}
        
        for agent_id, agent in self.active_agents.items():
            health = self.agent_health.get(agent_id, {})
            config = self.agent_configs.get(agent_id, {})
            
            agent_details[agent_id] = {
                'agent_type': config.get('agent_type', 'unknown'),
                'status': health.get('status', 'unknown'),
                'uptime_seconds': time.time() - health.get('spawn_time', time.time()),
                'task_count': health.get('task_count', 0),
                'error_count': health.get('error_count', 0),
                'performance_score': health.get('performance_score', 0.0),
                'capabilities': config.get('capabilities', []),
                'resource_requirements': config.get('resource_requirements', {})
            }
        
        return agent_details
    
    async def manual_scale_agent_type(self, agent_type: str, target_count: int) -> bool:
        """⚖️ Manually scale specific agent type"""
        if agent_type not in self.agent_specifications:
            return False
        
        spec = self.agent_specifications[agent_type]
        current_count = len([aid for aid in self.active_agents if aid.startswith(agent_type)])
        
        if target_count < spec['min_instances'] or target_count > spec['max_instances']:
            return False
        
        if target_count > current_count:
            # Scale up
            for i in range(target_count - current_count):
                await self._spawn_agent(agent_type)
        elif target_count < current_count:
            # Scale down
            agents_to_terminate = [aid for aid in self.active_agents if aid.startswith(agent_type)]
            for i in range(current_count - target_count):
                await self._terminate_agent(agents_to_terminate[i], "manual_scale")
        
        return True
    
    async def trigger_workflow(self, workflow_type: str, workflow_data: Dict[str, Any]) -> Optional[str]:
        """🔄 Trigger a workflow through the coordinator"""
        coordinator_id = None
        for agent_id in self.active_agents:
            if agent_id.startswith('coordinator'):
                coordinator_id = agent_id
                break
        
        if coordinator_id:
            coordinator = self.active_agents[coordinator_id]
            
            # Send workflow request
            await coordinator.send_message(coordinator_id, 'workflow_request', {
                'workflow_type': workflow_type,
                'workflow_data': workflow_data,
                'requester': self.orchestrator_id
            })
            
            return f"workflow_{workflow_type}_{int(time.time())}"
        
        return None
    
    async def get_performance_metrics(self) -> Dict[str, Any]:
        """📈 Get detailed performance metrics"""
        if not self.performance_history:
            return {}
        
        recent_performance = list(self.performance_history)[-20:]  # Last 20 measurements
        
        return {
            'current_performance': recent_performance[-1] if recent_performance else {},
            'performance_trend': {
                'response_time_trend': [p['average_response_time'] for p in recent_performance],
                'error_rate_trend': [p['error_rate'] for p in recent_performance],
                'agent_count_trend': [p['active_agents'] for p in recent_performance]
            },
            'system_health_over_time': [
                {'timestamp': p['timestamp'], 'healthy_agents': p['healthy_agents'], 'total_agents': p['active_agents']}
                for p in recent_performance
            ]
        }

# =================== SYSTEM LAUNCHER ===================

async def launch_multi_agent_system(config: Dict[str, Any] = None) -> AgentOrchestrator:
    """🚀 Launch the complete multi-agent system"""
    orchestrator = AgentOrchestrator(config)
    
    success = await orchestrator.initialize_system()
    
    if success:
        logger.info("🎯 Multi-agent system launched successfully!")
        return orchestrator
    else:
        logger.error("❌ Failed to launch multi-agent system")
        return None

if __name__ == "__main__":
    async def test_orchestrator():
        # Test configuration
        test_config = {
            'max_agents': 10,
            'min_agents': 5,
            'auto_scaling': True,
            'scaling_threshold': 0.8
        }
        
        # Launch system
        orchestrator = await launch_multi_agent_system(test_config)
        
        if orchestrator:
            # Let it run for a bit
            await asyncio.sleep(30)
            
            # Get status
            status = await orchestrator.get_system_status()
            print(f"🎯 System Status: {json.dumps(status, indent=2, default=str)}")
            
            # Get agent details
            agent_details = await orchestrator.get_agent_details()
            print(f"🤖 Agent Details: {json.dumps(agent_details, indent=2, default=str)}")
            
            # Trigger a test workflow
            workflow_id = await orchestrator.trigger_workflow('sports_analysis', {
                'sport': 'NFL',
                'analysis_depth': 'standard'
            })
            
            if workflow_id:
                print(f"🔄 Triggered workflow: {workflow_id}")
            
            # Let workflow run
            await asyncio.sleep(60)
            
            # Get performance metrics
            performance = await orchestrator.get_performance_metrics()
            print(f"📈 Performance: {json.dumps(performance, indent=2, default=str)}")
            
            # Shutdown system
            await orchestrator.shutdown_system()
    
    asyncio.run(test_orchestrator())