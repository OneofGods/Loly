#!/usr/bin/env python3
"""
🔥💀 PHASE 2: SWARM INTELLIGENCE COORDINATOR 💀🔥
Advanced coordination patterns for multi-agent swarms
"""

import asyncio
import logging
import time
import numpy as np
from typing import Dict, List, Set, Any, Optional, Tuple
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass

logger = logging.getLogger(__name__)

class SwarmTopology(Enum):
    """🌐 Swarm coordination topologies"""
    MESH = "mesh"           # Full connectivity
    HIERARCHICAL = "hierarchical"  # Tree-like leadership
    RING = "ring"          # Circular coordination
    STAR = "star"          # Central coordinator
    DYNAMIC = "dynamic"    # Adaptive topology

class SwarmRole(Enum):
    """👑 Agent roles within swarm"""
    LEADER = "leader"
    WORKER = "worker"
    COORDINATOR = "coordinator"
    SCOUT = "scout"
    SPECIALIST = "specialist"

@dataclass
class SwarmAgent:
    """🤖 Swarm agent representation"""
    agent_id: str
    agent_type: str
    role: SwarmRole
    capabilities: Set[str]
    performance_score: float = 0.0
    last_heartbeat: float = 0.0  # Fixed: use float timestamp, not datetime
    task_count: int = 0
    success_rate: float = 1.0
    communication_latency: float = 0.0
    
class SwarmIntelligenceCoordinator:
    """
    🧠 SWARM INTELLIGENCE COORDINATOR
    
    Implements advanced swarm coordination patterns:
    - Emergent behavior through local interactions
    - Collective decision making
    - Self-organizing task distribution
    - Adaptive topology management
    - Performance-based role assignment
    """
    
    def __init__(self, message_bus, swarm_id: str = None):
        self.swarm_id = swarm_id or f"swarm_{int(time.time())}"
        self.message_bus = message_bus
        
        # Swarm state
        self.agents: Dict[str, SwarmAgent] = {}
        self.topology = SwarmTopology.DYNAMIC
        self.active_tasks: Dict[str, Dict[str, Any]] = {}
        self.completed_tasks: List[Dict[str, Any]] = []
        
        # Intelligence parameters
        self.pheromone_trails: Dict[str, float] = {}  # Task routing optimization
        self.consensus_threshold = 0.67  # 2/3 majority for decisions
        self.adaptation_rate = 0.1       # Learning rate for performance updates
        self.heartbeat_timeout = 30      # Agent heartbeat timeout (seconds)
        
        # Performance tracking
        self.swarm_metrics = {
            'tasks_completed': 0,
            'average_completion_time': 0.0,
            'swarm_efficiency': 1.0,
            'consensus_decisions': 0,
            'topology_changes': 0,
            'failed_agents': 0
        }
        
        logger.info(f"🧠 SwarmIntelligenceCoordinator {self.swarm_id} initialized")
    
    async def register_agent(self, agent_id: str, agent_type: str, 
                           capabilities: Set[str] = None) -> SwarmRole:
        """🤖 Register agent with swarm and assign optimal role"""
        capabilities = capabilities or set()
        
        # Determine optimal role based on swarm state and agent capabilities
        role = await self._determine_optimal_role(agent_id, agent_type, capabilities)
        
        swarm_agent = SwarmAgent(
            agent_id=agent_id,
            agent_type=agent_type,
            role=role,
            capabilities=capabilities,
            last_heartbeat=time.time()  # Fixed: use timestamp for comparisons
        )
        
        self.agents[agent_id] = swarm_agent
        
        # Adapt topology if needed
        await self._adapt_topology()
        
        logger.info(f"🤖 Agent {agent_id} registered as {role.value} in swarm {self.swarm_id}")
        
        return role
    
    async def _determine_optimal_role(self, agent_id: str, agent_type: str, 
                                    capabilities: Set[str]) -> SwarmRole:
        """🎯 Determine optimal role for new agent"""
        current_roles = {agent.role for agent in self.agents.values()}
        
        # Leadership assignment logic
        if not any(role == SwarmRole.LEADER for role in current_roles):
            return SwarmRole.LEADER
        
        # Coordinator assignment for complex coordination
        if (len(self.agents) > 5 and 
            len([r for r in current_roles if r == SwarmRole.COORDINATOR]) < 2):
            return SwarmRole.COORDINATOR
        
        # Scout assignment for exploration tasks
        if 'exploration' in capabilities or 'data_collection' in capabilities:
            return SwarmRole.SCOUT
        
        # Specialist assignment for unique capabilities
        if len(capabilities) > 3:  # Rich capability set
            return SwarmRole.SPECIALIST
        
        # Default to worker
        return SwarmRole.WORKER
    
    async def distribute_task(self, task_id: str, task_type: str, 
                            payload: Dict[str, Any], 
                            required_capabilities: Set[str] = None) -> bool:
        """📋 Intelligently distribute task to optimal agent(s)"""
        required_capabilities = required_capabilities or set()
        
        # Find capable agents
        capable_agents = [
            agent for agent in self.agents.values()
            if (not required_capabilities or 
                required_capabilities.issubset(agent.capabilities))
        ]
        
        if not capable_agents:
            logger.warning(f"⚠️ No capable agents found for task {task_id}")
            return False
        
        # Ant Colony Optimization for task assignment
        selected_agent = await self._select_agent_aco(capable_agents, task_type)
        
        # Create task record
        task_record = {
            'task_id': task_id,
            'task_type': task_type,
            'assigned_agent': selected_agent.agent_id,
            'payload': payload,
            'started_at': datetime.now(),
            'status': 'assigned'
        }
        
        self.active_tasks[task_id] = task_record
        
        # Send task to selected agent
        await self.message_bus.publish_to_agent(
            target_agent=selected_agent.agent_id,
            event_name="task_assignment",
            payload={
                'task_id': task_id,
                'task_type': task_type,
                'data': payload,
                'swarm_id': self.swarm_id
            }
        )
        
        # Update pheromone trails
        trail_key = f"{task_type}:{selected_agent.agent_id}"
        self.pheromone_trails[trail_key] = self.pheromone_trails.get(trail_key, 0.5) + 0.1
        
        logger.info(f"📋 Task {task_id} assigned to {selected_agent.agent_id}")
        
        return True
    
    async def _select_agent_aco(self, capable_agents: List[SwarmAgent], 
                              task_type: str) -> SwarmAgent:
        """🐜 Ant Colony Optimization for agent selection"""
        if not capable_agents:
            return None
        
        # Calculate selection probabilities
        probabilities = []
        
        for agent in capable_agents:
            # Pheromone strength (learning from past success)
            trail_key = f"{task_type}:{agent.agent_id}"
            pheromone = self.pheromone_trails.get(trail_key, 0.5)
            
            # Heuristic factors
            performance_factor = agent.performance_score
            availability_factor = 1.0 / max(1, agent.task_count)  # Prefer less loaded agents
            recency_factor = 1.0 / max(1, (datetime.now() - agent.last_heartbeat).seconds)
            
            # Combined probability
            probability = (pheromone ** 2) * performance_factor * availability_factor * recency_factor
            probabilities.append(probability)
        
        # Probabilistic selection
        total_prob = sum(probabilities)
        if total_prob == 0:
            return capable_agents[0]  # Fallback to first agent
        
        normalized_probs = [p / total_prob for p in probabilities]
        selected_index = np.random.choice(len(capable_agents), p=normalized_probs)
        
        return capable_agents[selected_index]
    
    async def consensus_decision(self, decision_id: str, options: List[str], 
                               voting_agents: Set[str] = None) -> str:
        """🗳️ Collective decision making through consensus"""
        voting_agents = voting_agents or set(self.agents.keys())
        
        # Collect votes from agents
        votes = {}
        vote_requests = []
        
        for agent_id in voting_agents:
            if agent_id in self.agents:
                vote_requests.append(
                    self._request_vote(agent_id, decision_id, options)
                )
        
        # Collect votes with timeout
        vote_results = await asyncio.gather(*vote_requests, return_exceptions=True)
        
        # Tally votes
        vote_counts = {option: 0 for option in options}
        valid_votes = 0
        
        for vote_result in vote_results:
            if isinstance(vote_result, str) and vote_result in options:
                vote_counts[vote_result] += 1
                valid_votes += 1
        
        # Determine consensus
        if valid_votes == 0:
            return options[0]  # Fallback to first option
        
        # Check for majority consensus
        required_votes = int(valid_votes * self.consensus_threshold)
        
        for option, count in vote_counts.items():
            if count >= required_votes:
                self.swarm_metrics['consensus_decisions'] += 1
                logger.info(f"🗳️ Consensus reached: {option} ({count}/{valid_votes} votes)")
                return option
        
        # No consensus - return most voted option
        best_option = max(vote_counts.items(), key=lambda x: x[1])[0]
        logger.info(f"🗳️ No consensus, selecting popular choice: {best_option}")
        
        return best_option
    
    async def _request_vote(self, agent_id: str, decision_id: str, 
                          options: List[str]) -> Optional[str]:
        """📊 Request vote from individual agent"""
        try:
            # Send vote request
            await self.message_bus.publish_to_agent(
                target_agent=agent_id,
                event_name="vote_request",
                payload={
                    'decision_id': decision_id,
                    'options': options,
                    'swarm_id': self.swarm_id
                }
            )
            
            # Wait for response (with timeout)
            response = await asyncio.wait_for(
                self.message_bus.wait_for_response(agent_id, decision_id),
                timeout=5.0
            )
            
            return response.get('vote')
            
        except asyncio.TimeoutError:
            logger.warning(f"⏰ Vote timeout from agent {agent_id}")
            return None
        except Exception as e:
            logger.error(f"❌ Vote request failed for {agent_id}: {e}")
            return None
    
    async def _adapt_topology(self):
        """🌐 Dynamically adapt swarm topology based on performance"""
        agent_count = len(self.agents)
        current_efficiency = self.swarm_metrics['swarm_efficiency']
        
        # Topology adaptation rules
        if agent_count <= 3:
            new_topology = SwarmTopology.MESH
        elif agent_count <= 8 and current_efficiency > 0.8:
            new_topology = SwarmTopology.STAR
        elif agent_count <= 15:
            new_topology = SwarmTopology.HIERARCHICAL
        else:
            new_topology = SwarmTopology.RING
        
        if new_topology != self.topology:
            old_topology = self.topology
            self.topology = new_topology
            self.swarm_metrics['topology_changes'] += 1
            
            logger.info(f"🌐 Topology adapted: {old_topology.value} → {new_topology.value}")
            
            # Notify agents of topology change
            await self.message_bus.broadcast(
                event_name="topology_change",
                payload={
                    'swarm_id': self.swarm_id,
                    'new_topology': new_topology.value,
                    'agent_count': agent_count
                }
            )
    
    async def monitor_swarm_health(self):
        """💓 Monitor and maintain swarm health"""
        current_time = datetime.now()
        failed_agents = []
        
        # Check agent heartbeats
        for agent_id, agent in list(self.agents.items()):
            time_since_heartbeat = (current_time - agent.last_heartbeat).seconds
            
            if time_since_heartbeat > self.heartbeat_timeout:
                logger.warning(f"💓 Agent {agent_id} heartbeat timeout ({time_since_heartbeat}s)")
                failed_agents.append(agent_id)
        
        # Handle failed agents
        for agent_id in failed_agents:
            await self._handle_agent_failure(agent_id)
        
        # Update swarm efficiency
        await self._update_swarm_efficiency()
        
        # Evaporate pheromone trails (prevents stagnation)
        for trail_key in list(self.pheromone_trails.keys()):
            self.pheromone_trails[trail_key] *= 0.95  # 5% evaporation
            if self.pheromone_trails[trail_key] < 0.1:
                del self.pheromone_trails[trail_key]
    
    async def _handle_agent_failure(self, agent_id: str):
        """🚨 Handle agent failure and task reassignment"""
        if agent_id not in self.agents:
            return
        
        failed_agent = self.agents[agent_id]
        
        # Find tasks assigned to failed agent
        failed_tasks = [
            task for task in self.active_tasks.values()
            if task['assigned_agent'] == agent_id and task['status'] != 'completed'
        ]
        
        # Reassign tasks to other agents
        for task in failed_tasks:
            task['status'] = 'reassigning'
            
            # Find replacement agent
            capable_agents = [
                agent for agent in self.agents.values()
                if (agent.agent_id != agent_id and 
                    agent.role in [SwarmRole.WORKER, SwarmRole.SPECIALIST])
            ]
            
            if capable_agents:
                replacement_agent = min(capable_agents, key=lambda a: a.task_count)
                task['assigned_agent'] = replacement_agent.agent_id
                task['reassigned_at'] = datetime.now()
                
                # Send task to replacement agent
                await self.message_bus.publish_to_agent(
                    target_agent=replacement_agent.agent_id,
                    event_name="task_reassignment",
                    payload={
                        'task_id': task['task_id'],
                        'task_type': task['task_type'],
                        'data': task['payload'],
                        'original_agent': agent_id,
                        'swarm_id': self.swarm_id
                    }
                )
                
                logger.info(f"📋 Task {task['task_id']} reassigned: {agent_id} → {replacement_agent.agent_id}")
        
        # Remove failed agent from swarm
        del self.agents[agent_id]
        self.swarm_metrics['failed_agents'] += 1
        
        # Adapt topology after agent removal
        await self._adapt_topology()
        
        logger.warning(f"🚨 Agent {agent_id} removed from swarm due to failure")
    
    async def _update_swarm_efficiency(self):
        """📊 Update swarm performance metrics"""
        if not self.agents:
            return
        
        # Calculate average performance
        total_performance = sum(agent.performance_score for agent in self.agents.values())
        avg_performance = total_performance / len(self.agents)
        
        # Calculate task completion rate
        total_tasks = len(self.completed_tasks) + len(self.active_tasks)
        completion_rate = len(self.completed_tasks) / max(1, total_tasks)
        
        # Calculate communication efficiency
        avg_latency = np.mean([agent.communication_latency for agent in self.agents.values()])
        communication_efficiency = max(0, 1.0 - (avg_latency / 1000))  # Assume 1s is poor
        
        # Combined efficiency score
        self.swarm_metrics['swarm_efficiency'] = (
            0.4 * avg_performance +
            0.4 * completion_rate +
            0.2 * communication_efficiency
        )
        
        # Update average completion time
        if self.completed_tasks:
            completion_times = [
                (task['completed_at'] - task['started_at']).total_seconds()
                for task in self.completed_tasks
                if 'completed_at' in task
            ]
            if completion_times:
                self.swarm_metrics['average_completion_time'] = np.mean(completion_times)
    
    async def get_swarm_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive swarm status"""
        agent_summary = {}
        for role in SwarmRole:
            role_agents = [a for a in self.agents.values() if a.role == role]
            agent_summary[role.value] = {
                'count': len(role_agents),
                'avg_performance': np.mean([a.performance_score for a in role_agents]) if role_agents else 0
            }
        
        return {
            'swarm_id': self.swarm_id,
            'topology': self.topology.value,
            'total_agents': len(self.agents),
            'agent_roles': agent_summary,
            'active_tasks': len(self.active_tasks),
            'completed_tasks': len(self.completed_tasks),
            'pheromone_trails': len(self.pheromone_trails),
            'metrics': self.swarm_metrics.copy(),
            'health_status': 'healthy' if self.swarm_metrics['swarm_efficiency'] > 0.7 else 'degraded'
        }
    
    async def emergency_shutdown(self):
        """🚨 Emergency swarm shutdown with graceful task handling"""
        logger.warning(f"🚨 Emergency shutdown initiated for swarm {self.swarm_id}")
        
        # Notify all agents
        await self.message_bus.broadcast(
            event_name="emergency_shutdown",
            payload={
                'swarm_id': self.swarm_id,
                'reason': 'emergency_shutdown',
                'timestamp': datetime.now().isoformat()
            }
        )
        
        # Mark active tasks as failed
        for task_id, task in self.active_tasks.items():
            task['status'] = 'failed'
            task['failure_reason'] = 'emergency_shutdown'
            task['failed_at'] = datetime.now()
        
        self.agents.clear()
        self.active_tasks.clear()
        self.pheromone_trails.clear()
        
        logger.warning(f"🚨 Swarm {self.swarm_id} emergency shutdown completed")