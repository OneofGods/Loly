#!/usr/bin/env python3
"""
⚡💀⚡ AGENT LOAD BALANCER - DISTRIBUTE THE WORK! 💀⚡💀

Phase 3C: Dynamic Agent Spawning & Load Balancing

This load balancer distributes requests across agent instances:
- 🔄 Round-robin distribution
- 📊 Least-connections strategy
- 💚 Health-based routing (only healthy instances)
- 🎯 Automatic failover
- 📈 Connection tracking

🔥 MAXIMUM PERFORMANCE, ZERO BOTTLENECKS! 🔥
"""

import asyncio
import aiohttp
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum

logger = logging.getLogger(__name__)


class LoadBalancingStrategy(Enum):
    """Load balancing strategies"""
    ROUND_ROBIN = "round_robin"
    LEAST_CONNECTIONS = "least_connections"
    RANDOM = "random"


class AgentLoadBalancer:
    """
    ⚡💀⚡ AGENT LOAD BALANCER 💀⚡⚡

    Distributes requests across multiple agent instances for maximum performance!
    """

    def __init__(self, strategy: LoadBalancingStrategy = LoadBalancingStrategy.LEAST_CONNECTIONS):
        self.balancer_id = f"balancer_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.strategy = strategy

        # Instance tracking: {agent_type: {instance_id: {port, active_connections, total_requests, ...}}}
        self.instances: Dict[str, Dict[str, Dict[str, Any]]] = {}

        # Round-robin counters: {agent_type: current_index}
        self.rr_counters: Dict[str, int] = {}

        # Load balancer statistics
        self.stats = {
            'total_requests': 0,
            'successful_routes': 0,
            'failed_routes': 0,
            'requests_by_agent': {},
            'requests_by_instance': {}
        }

        logger.info(f"⚡💀⚡ {self.balancer_id}: Agent Load Balancer initialized!")
        logger.info(f"   Strategy: {strategy.value}")

    def register_instance(self, agent_type: str, instance_id: str, port: int):
        """
        📝 Register an agent instance for load balancing

        Args:
            agent_type: Type of agent
            instance_id: Unique instance ID
            port: Port the instance is running on
        """
        if agent_type not in self.instances:
            self.instances[agent_type] = {}
            self.rr_counters[agent_type] = 0

        self.instances[agent_type][instance_id] = {
            'port': port,
            'active_connections': 0,
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'status': 'healthy',
            'last_request': None,
            'registered_at': datetime.now().isoformat()
        }

        logger.info(f"📝 Registered {agent_type} instance {instance_id} on port {port}")

    def unregister_instance(self, agent_type: str, instance_id: str):
        """
        🗑️ Unregister an agent instance

        Args:
            agent_type: Type of agent
            instance_id: Instance ID to remove
        """
        if agent_type in self.instances and instance_id in self.instances[agent_type]:
            del self.instances[agent_type][instance_id]
            logger.info(f"🗑️ Unregistered {agent_type} instance {instance_id}")

    def get_next_instance(self, agent_type: str) -> Optional[Tuple[str, int]]:
        """
        🎯 Get the next instance to route to based on strategy

        Args:
            agent_type: Type of agent needed

        Returns:
            Tuple of (instance_id, port) or None if no instances available
        """
        if agent_type not in self.instances or not self.instances[agent_type]:
            logger.warning(f"⚠️  No instances available for {agent_type}")
            return None

        # Filter to only healthy instances
        healthy_instances = {
            inst_id: inst_data
            for inst_id, inst_data in self.instances[agent_type].items()
            if inst_data['status'] == 'healthy'
        }

        if not healthy_instances:
            logger.warning(f"⚠️  No healthy instances for {agent_type}")
            return None

        # Apply load balancing strategy
        if self.strategy == LoadBalancingStrategy.ROUND_ROBIN:
            return self._round_robin_select(agent_type, healthy_instances)

        elif self.strategy == LoadBalancingStrategy.LEAST_CONNECTIONS:
            return self._least_connections_select(agent_type, healthy_instances)

        elif self.strategy == LoadBalancingStrategy.RANDOM:
            return self._random_select(agent_type, healthy_instances)

        else:
            # Default to least connections
            return self._least_connections_select(agent_type, healthy_instances)

    def _round_robin_select(self, agent_type: str, instances: Dict[str, Dict[str, Any]]) -> Tuple[str, int]:
        """Round-robin selection"""
        instance_list = list(instances.items())

        if not instance_list:
            return None

        # Get current index
        index = self.rr_counters[agent_type] % len(instance_list)

        # Increment for next time
        self.rr_counters[agent_type] += 1

        # Get instance
        instance_id, instance_data = instance_list[index]
        return (instance_id, instance_data['port'])

    def _least_connections_select(self, agent_type: str, instances: Dict[str, Dict[str, Any]]) -> Tuple[str, int]:
        """Least connections selection"""
        # Sort by active connections (ascending)
        sorted_instances = sorted(
            instances.items(),
            key=lambda x: x[1]['active_connections']
        )

        if not sorted_instances:
            return None

        instance_id, instance_data = sorted_instances[0]
        return (instance_id, instance_data['port'])

    def _random_select(self, agent_type: str, instances: Dict[str, Dict[str, Any]]) -> Tuple[str, int]:
        """Random selection"""
        import random

        instance_list = list(instances.items())

        if not instance_list:
            return None

        instance_id, instance_data = random.choice(instance_list)
        return (instance_id, instance_data['port'])

    async def route_request(self, agent_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        🚀 Route a request to an agent instance

        Args:
            agent_type: Type of agent to route to
            request_data: Request data to send

        Returns:
            Response from the agent
        """
        self.stats['total_requests'] += 1

        # Track requests by agent type
        if agent_type not in self.stats['requests_by_agent']:
            self.stats['requests_by_agent'][agent_type] = 0
        self.stats['requests_by_agent'][agent_type] += 1

        # Get next instance
        instance_info = self.get_next_instance(agent_type)

        if not instance_info:
            self.stats['failed_routes'] += 1
            return {
                'status': 'error',
                'error': f'No available instances for {agent_type}',
                'timestamp': datetime.now().isoformat()
            }

        instance_id, port = instance_info

        # Track this instance
        instance_data = self.instances[agent_type][instance_id]

        # Increment active connections
        instance_data['active_connections'] += 1
        instance_data['total_requests'] += 1
        instance_data['last_request'] = datetime.now().isoformat()

        # Track requests by instance
        if instance_id not in self.stats['requests_by_instance']:
            self.stats['requests_by_instance'][instance_id] = 0
        self.stats['requests_by_instance'][instance_id] += 1

        try:
            # Make request to the agent instance
            url = f"http://localhost:{port}/api/process"

            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=request_data, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    result = await response.json()

                    # Success!
                    instance_data['successful_requests'] += 1
                    self.stats['successful_routes'] += 1

                    logger.info(f"✅ Routed {agent_type} request to instance {instance_id} (port {port})")

                    return result

        except Exception as e:
            # Failed!
            instance_data['failed_requests'] += 1
            self.stats['failed_routes'] += 1

            logger.error(f"❌ Failed to route {agent_type} request to instance {instance_id}: {e}")

            # Mark instance as unhealthy
            instance_data['status'] = 'unhealthy'

            # Try failover to another instance
            return await self._failover_request(agent_type, request_data, failed_instance=instance_id)

        finally:
            # Decrement active connections
            instance_data['active_connections'] -= 1

    async def _failover_request(self, agent_type: str, request_data: Dict[str, Any],
                                failed_instance: str) -> Dict[str, Any]:
        """
        🔄 Failover to another instance if one fails

        Args:
            agent_type: Type of agent
            request_data: Request data
            failed_instance: Instance that failed

        Returns:
            Response from failover instance or error
        """
        logger.info(f"🔄 Attempting failover for {agent_type} (failed instance: {failed_instance})")

        # Get another instance (excluding the failed one)
        instance_info = self.get_next_instance(agent_type)

        if not instance_info:
            return {
                'status': 'error',
                'error': f'Failover failed: No other instances available for {agent_type}',
                'timestamp': datetime.now().isoformat()
            }

        instance_id, port = instance_info

        if instance_id == failed_instance:
            # Same instance, no other options
            return {
                'status': 'error',
                'error': f'Failover failed: Only one instance available for {agent_type}',
                'timestamp': datetime.now().isoformat()
            }

        # Try the failover instance
        instance_data = self.instances[agent_type][instance_id]
        instance_data['active_connections'] += 1

        try:
            url = f"http://localhost:{port}/api/process"

            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=request_data, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    result = await response.json()

                    instance_data['successful_requests'] += 1

                    logger.info(f"✅ Failover successful to {agent_type} instance {instance_id}")

                    return result

        except Exception as e:
            instance_data['failed_requests'] += 1
            logger.error(f"❌ Failover also failed: {e}")

            return {
                'status': 'error',
                'error': f'All failover attempts failed for {agent_type}',
                'timestamp': datetime.now().isoformat()
            }

        finally:
            instance_data['active_connections'] -= 1

    def mark_instance_healthy(self, agent_type: str, instance_id: str):
        """💚 Mark an instance as healthy"""
        if agent_type in self.instances and instance_id in self.instances[agent_type]:
            self.instances[agent_type][instance_id]['status'] = 'healthy'
            logger.info(f"💚 Marked {agent_type} instance {instance_id} as healthy")

    def mark_instance_unhealthy(self, agent_type: str, instance_id: str):
        """💔 Mark an instance as unhealthy"""
        if agent_type in self.instances and instance_id in self.instances[agent_type]:
            self.instances[agent_type][instance_id]['status'] = 'unhealthy'
            logger.warning(f"💔 Marked {agent_type} instance {instance_id} as unhealthy")

    def get_instance_stats(self, agent_type: str, instance_id: str) -> Optional[Dict[str, Any]]:
        """📊 Get stats for a specific instance"""
        if agent_type in self.instances and instance_id in self.instances[agent_type]:
            return self.instances[agent_type][instance_id].copy()
        return None

    def get_all_instance_stats(self) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """📊 Get stats for all instances"""
        return {
            agent_type: {
                instance_id: instance_data.copy()
                for instance_id, instance_data in instances.items()
            }
            for agent_type, instances in self.instances.items()
        }

    def get_balancer_stats(self) -> Dict[str, Any]:
        """📊 Get load balancer statistics"""
        return {
            'balancer_id': self.balancer_id,
            'strategy': self.strategy.value,
            'total_requests': self.stats['total_requests'],
            'successful_routes': self.stats['successful_routes'],
            'failed_routes': self.stats['failed_routes'],
            'success_rate': (self.stats['successful_routes'] / max(self.stats['total_requests'], 1)) * 100,
            'requests_by_agent': self.stats['requests_by_agent'],
            'requests_by_instance': self.stats['requests_by_instance'],
            'total_instances': sum(len(instances) for instances in self.instances.values()),
            'healthy_instances': sum(
                1 for instances in self.instances.values()
                for inst in instances.values()
                if inst['status'] == 'healthy'
            )
        }


# =================== FACTORY FUNCTION ===================

def create_agent_load_balancer(strategy: LoadBalancingStrategy = LoadBalancingStrategy.LEAST_CONNECTIONS) -> AgentLoadBalancer:
    """🏭 Factory function to create agent load balancer"""
    return AgentLoadBalancer(strategy=strategy)
