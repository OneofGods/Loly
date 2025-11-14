#!/usr/bin/env python3
"""
🔄💀🔄 DYNAMIC AGENT SPAWNER - SPAWN AGENTS ON DEMAND! 💀🔄💀

Phase 3C: Dynamic Agent Spawning & Load Balancing

This spawner creates agent instances dynamically based on load:
- 🚀 Spawn new agents when load increases
- 🛑 Kill idle agents when load decreases
- 🎯 Min/Max instance management
- 💚 Health check spawned instances
- 📊 Track all running instances

🔥 WHEN LOLY GETS POPULAR, SHE SCALES! 🔥
"""

import asyncio
import subprocess
import signal
import os
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class DynamicAgentSpawner:
    """
    🔄💀🔄 DYNAMIC AGENT SPAWNER 💀🔄💀

    Spawns and manages agent instances dynamically based on load!
    """

    def __init__(self, agent_scripts_dir: str = "."):
        self.spawner_id = f"spawner_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.agent_scripts_dir = Path(agent_scripts_dir)

        # Agent configuration (min/max instances per agent type)
        self.agent_config = {
            'research_agent': {
                'script': 'research_agent.py',
                'base_port': 3201,
                'min_instances': 1,
                'max_instances': 5,
                'spawn_threshold': 0.8,  # Spawn at 80% capacity
                'kill_threshold': 0.3    # Kill at 30% capacity
            },
            'writer_agent': {
                'script': 'writer_agent.py',
                'base_port': 3203,
                'min_instances': 1,
                'max_instances': 5,
                'spawn_threshold': 0.8,
                'kill_threshold': 0.3
            },
            'reviewer_agent': {
                'script': 'reviewer_agent.py',
                'base_port': 3204,
                'min_instances': 1,
                'max_instances': 5,
                'spawn_threshold': 0.8,
                'kill_threshold': 0.3
            },
            'builder_agent': {
                'script': 'builder_agent.py',
                'base_port': 3205,
                'min_instances': 1,
                'max_instances': 5,
                'spawn_threshold': 0.8,
                'kill_threshold': 0.3
            }
        }

        # Running instances: {agent_type: [{instance_id, port, pid, process, started_at, status}]}
        self.running_instances: Dict[str, List[Dict[str, Any]]] = {
            agent_type: [] for agent_type in self.agent_config.keys()
        }

        # Spawner statistics
        self.stats = {
            'total_spawned': 0,
            'total_killed': 0,
            'current_instances': 0,
            'spawn_events': [],
            'kill_events': []
        }

        logger.info(f"🔄💀🔄 {self.spawner_id}: Dynamic Agent Spawner initialized!")

    async def spawn_agent(self, agent_type: str, port: Optional[int] = None) -> Optional[Dict[str, Any]]:
        """
        🚀 Spawn a new agent instance

        Args:
            agent_type: Type of agent to spawn
            port: Optional specific port (otherwise auto-assign)

        Returns:
            Instance info dict or None if failed
        """
        try:
            if agent_type not in self.agent_config:
                logger.error(f"❌ Unknown agent type: {agent_type}")
                return None

            config = self.agent_config[agent_type]
            instances = self.running_instances[agent_type]

            # Check if we've hit max instances
            if len(instances) >= config['max_instances']:
                logger.warning(f"⚠️  {agent_type} at max instances ({config['max_instances']})")
                return None

            # Determine port
            if port is None:
                port = self._find_available_port(agent_type)

            if port is None:
                logger.error(f"❌ No available port for {agent_type}")
                return None

            # Build command to spawn agent
            script_path = self.agent_scripts_dir / config['script']

            if not script_path.exists():
                logger.error(f"❌ Agent script not found: {script_path}")
                return None

            # Set environment variable for port
            env = os.environ.copy()
            env[f'{agent_type.upper()}_PORT'] = str(port)

            # Spawn the process
            process = subprocess.Popen(
                ['python3', str(script_path)],
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                start_new_session=True  # Create new session for clean shutdown
            )

            # Create instance info
            instance_id = f"{agent_type}_{port}_{datetime.now().strftime('%H%M%S')}"
            instance = {
                'instance_id': instance_id,
                'agent_type': agent_type,
                'port': port,
                'pid': process.pid,
                'process': process,
                'started_at': datetime.now().isoformat(),
                'status': 'starting',
                'request_count': 0,
                'last_request': None
            }

            # Add to running instances
            instances.append(instance)

            # Update stats
            self.stats['total_spawned'] += 1
            self.stats['current_instances'] += 1
            self.stats['spawn_events'].append({
                'instance_id': instance_id,
                'agent_type': agent_type,
                'port': port,
                'timestamp': datetime.now().isoformat()
            })

            logger.info(f"🚀 Spawned {agent_type} instance on port {port} (PID: {process.pid})")

            # Wait a moment for startup
            await asyncio.sleep(2)

            # Update status
            if process.poll() is None:  # Process still running
                instance['status'] = 'running'
                logger.info(f"✅ {agent_type} instance {instance_id} is running!")
                return instance
            else:
                # Process died
                instance['status'] = 'failed'
                logger.error(f"❌ {agent_type} instance {instance_id} failed to start")
                return None

        except Exception as e:
            logger.error(f"❌ Error spawning {agent_type}: {e}")
            return None

    async def kill_agent(self, agent_type: str, instance_id: str) -> bool:
        """
        🛑 Kill an agent instance

        Args:
            agent_type: Type of agent
            instance_id: ID of instance to kill

        Returns:
            True if killed successfully
        """
        try:
            instances = self.running_instances[agent_type]

            # Find the instance
            instance = None
            for inst in instances:
                if inst['instance_id'] == instance_id:
                    instance = inst
                    break

            if not instance:
                logger.warning(f"⚠️  Instance not found: {instance_id}")
                return False

            # Kill the process
            pid = instance['pid']
            process = instance['process']

            try:
                # Try graceful shutdown first
                process.terminate()
                await asyncio.sleep(2)

                # Force kill if still running
                if process.poll() is None:
                    process.kill()
                    await asyncio.sleep(1)

                logger.info(f"🛑 Killed {agent_type} instance {instance_id} (PID: {pid})")

            except Exception as e:
                logger.warning(f"⚠️  Error killing process {pid}: {e}")

            # Remove from running instances
            instances.remove(instance)

            # Update stats
            self.stats['total_killed'] += 1
            self.stats['current_instances'] -= 1
            self.stats['kill_events'].append({
                'instance_id': instance_id,
                'agent_type': agent_type,
                'timestamp': datetime.now().isoformat()
            })

            return True

        except Exception as e:
            logger.error(f"❌ Error killing {agent_type} instance: {e}")
            return False

    def _find_available_port(self, agent_type: str) -> Optional[int]:
        """🔍 Find an available port for the agent type"""
        config = self.agent_config[agent_type]
        base_port = config['base_port']

        # Try ports in range [base_port, base_port + max_instances]
        for offset in range(config['max_instances']):
            port = base_port + offset

            # Check if port already in use by our instances
            instances = self.running_instances[agent_type]
            if any(inst['port'] == port for inst in instances):
                continue

            # Check if port is actually available on system
            if self._is_port_available(port):
                return port

        return None

    def _is_port_available(self, port: int) -> bool:
        """Check if a port is available on the system"""
        import socket
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return True
        except:
            return False

    async def scale_up(self, agent_type: str, count: int = 1) -> int:
        """
        📈 Scale up agent instances

        Args:
            agent_type: Type of agent to scale
            count: Number of instances to add

        Returns:
            Number of instances actually spawned
        """
        spawned = 0

        for i in range(count):
            instance = await self.spawn_agent(agent_type)
            if instance:
                spawned += 1

        logger.info(f"📈 Scaled up {agent_type}: added {spawned} instances")
        return spawned

    async def scale_down(self, agent_type: str, count: int = 1) -> int:
        """
        📉 Scale down agent instances

        Args:
            agent_type: Type of agent to scale
            count: Number of instances to remove

        Returns:
            Number of instances actually killed
        """
        killed = 0
        instances = self.running_instances[agent_type]
        config = self.agent_config[agent_type]

        # Don't go below min instances
        current_count = len(instances)
        can_kill = max(0, current_count - config['min_instances'])
        count = min(count, can_kill)

        # Kill least recently used instances
        sorted_instances = sorted(instances, key=lambda x: x.get('last_request') or '')

        for i in range(count):
            if i < len(sorted_instances):
                instance = sorted_instances[i]
                if await self.kill_agent(agent_type, instance['instance_id']):
                    killed += 1

        logger.info(f"📉 Scaled down {agent_type}: removed {killed} instances")
        return killed

    async def ensure_min_instances(self, agent_type: str) -> int:
        """
        🎯 Ensure minimum instances are running

        Args:
            agent_type: Type of agent

        Returns:
            Number of instances spawned to reach minimum
        """
        config = self.agent_config[agent_type]
        instances = self.running_instances[agent_type]

        current_count = len(instances)
        min_count = config['min_instances']

        if current_count < min_count:
            needed = min_count - current_count
            logger.info(f"🎯 Ensuring min instances for {agent_type}: spawning {needed}")
            return await self.scale_up(agent_type, needed)

        return 0

    async def ensure_all_min_instances(self):
        """🎯 Ensure all agent types have minimum instances"""
        for agent_type in self.agent_config.keys():
            await self.ensure_min_instances(agent_type)

    def get_instance_count(self, agent_type: str) -> int:
        """📊 Get current instance count for agent type"""
        return len(self.running_instances[agent_type])

    def get_all_instances(self) -> Dict[str, List[Dict[str, Any]]]:
        """📊 Get all running instances"""
        return {
            agent_type: [
                {
                    'instance_id': inst['instance_id'],
                    'port': inst['port'],
                    'pid': inst['pid'],
                    'status': inst['status'],
                    'started_at': inst['started_at'],
                    'request_count': inst['request_count']
                }
                for inst in instances
            ]
            for agent_type, instances in self.running_instances.items()
        }

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get spawner statistics"""
        return {
            'spawner_id': self.spawner_id,
            'total_spawned': self.stats['total_spawned'],
            'total_killed': self.stats['total_killed'],
            'current_instances': self.stats['current_instances'],
            'instances_by_type': {
                agent_type: len(instances)
                for agent_type, instances in self.running_instances.items()
            },
            'recent_spawn_events': self.stats['spawn_events'][-10:],
            'recent_kill_events': self.stats['kill_events'][-10:]
        }

    async def health_check_instances(self) -> Dict[str, Any]:
        """💚 Health check all running instances"""
        healthy = 0
        unhealthy = 0

        for agent_type, instances in self.running_instances.items():
            for instance in instances:
                process = instance['process']

                if process.poll() is None:  # Process still running
                    instance['status'] = 'running'
                    healthy += 1
                else:
                    instance['status'] = 'dead'
                    unhealthy += 1
                    logger.warning(f"⚠️  Instance {instance['instance_id']} is dead!")

        return {
            'healthy': healthy,
            'unhealthy': unhealthy,
            'total': healthy + unhealthy
        }

    async def cleanup(self):
        """🧹 Cleanup all spawned instances"""
        logger.info("🧹 Cleaning up all spawned instances...")

        for agent_type, instances in self.running_instances.items():
            for instance in list(instances):  # Copy list to avoid modification during iteration
                await self.kill_agent(agent_type, instance['instance_id'])

        logger.info("✅ All instances cleaned up!")


# =================== FACTORY FUNCTION ===================

def create_dynamic_agent_spawner(agent_scripts_dir: str = ".") -> DynamicAgentSpawner:
    """🏭 Factory function to create dynamic agent spawner"""
    return DynamicAgentSpawner(agent_scripts_dir=agent_scripts_dir)
