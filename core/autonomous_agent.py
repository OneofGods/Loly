#!/usr/bin/env python3
"""
🔥💀 AUTONOMOUS AGENT BASE CLASS - REAL AGENT FOUNDATION 💀🔥
Agent Poly Loly Double Zero: True Multi-Agent System

CRITICAL FEATURES:
- Lifecycle: spawn() → run() → monitor() → adapt() → terminate()
- Behavior: Independent decision-making loops
- Communication: Message queue protocols  
- Learning: Experience accumulation and pattern recognition
- Health: Self-monitoring and recovery
"""

import asyncio
import json
import logging
import time
import uuid
import weakref
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Callable
import psutil
import os
import signal

# Configure logging for agents
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)

class AgentState(Enum):
    """🎯 Agent lifecycle states"""
    INITIALIZING = "initializing"
    SPAWNING = "spawning"
    RUNNING = "running"
    MONITORING = "monitoring"
    ADAPTING = "adapting"
    TERMINATING = "terminating"
    TERMINATED = "terminated"
    ERROR = "error"

class AgentMessage:
    """📨 Inter-agent communication message"""
    def __init__(self, sender_id: str, receiver_id: str, message_type: str, 
                 payload: Dict[str, Any], priority: int = 1):
        self.id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message_type = message_type
        self.payload = payload
        self.priority = priority
        self.timestamp = datetime.now()
        self.retries = 0
        self.max_retries = 3
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'message_type': self.message_type,
            'payload': self.payload,
            'priority': self.priority,
            'timestamp': self.timestamp.isoformat(),
            'retries': self.retries
        }

class AgentMemory:
    """🧠 Agent learning and experience accumulation"""
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.experiences = []
        self.patterns = {}
        self.success_rate = 0.0
        self.total_tasks = 0
        self.successful_tasks = 0
        self.adaptations = []
        
    def record_experience(self, task_type: str, outcome: str, 
                         duration: float, details: Dict[str, Any]):
        """📝 Record task experience for learning"""
        experience = {
            'timestamp': datetime.now(),
            'task_type': task_type,
            'outcome': outcome,  # 'success', 'failure', 'timeout'
            'duration': duration,
            'details': details
        }
        self.experiences.append(experience)
        
        # Update success metrics
        self.total_tasks += 1
        if outcome == 'success':
            self.successful_tasks += 1
        self.success_rate = self.successful_tasks / self.total_tasks
        
        # Pattern recognition
        self._update_patterns(task_type, outcome, details)
        
    def _update_patterns(self, task_type: str, outcome: str, details: Dict[str, Any]):
        """🎯 Extract patterns from experiences"""
        if task_type not in self.patterns:
            self.patterns[task_type] = {
                'success_count': 0,
                'failure_count': 0,
                'avg_duration': 0.0,
                'common_issues': {},
                'best_practices': {}
            }
        
        pattern = self.patterns[task_type]
        if outcome == 'success':
            pattern['success_count'] += 1
        else:
            pattern['failure_count'] += 1
            
    def get_recommendations(self, task_type: str) -> Dict[str, Any]:
        """💡 Get learned recommendations for task type"""
        if task_type in self.patterns:
            pattern = self.patterns[task_type]
            total = pattern['success_count'] + pattern['failure_count']
            success_rate = pattern['success_count'] / total if total > 0 else 0.0
            
            return {
                'success_rate': success_rate,
                'confidence': min(total / 10.0, 1.0),  # Confidence based on experience
                'recommendations': pattern.get('best_practices', {})
            }
        return {'success_rate': 0.0, 'confidence': 0.0, 'recommendations': {}}

class AutonomousAgent(ABC):
    """
    🤖 BASE CLASS FOR ALL AUTONOMOUS AGENTS
    
    Implements the complete agent lifecycle with:
    - Independent decision-making
    - Autonomous communication
    - Learning and adaptation
    - Self-monitoring and recovery
    """
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        # Agent identity
        self.agent_id = agent_id or f"{self.__class__.__name__}_{uuid.uuid4().hex[:8]}"
        self.config = config or {}
        
        # Lifecycle management
        self.state = AgentState.INITIALIZING
        self.start_time = None
        self.last_heartbeat = None
        self.process_id = os.getpid()
        
        # Communication
        self.message_queue = asyncio.Queue()
        self.outbound_queue = asyncio.Queue()
        self.subscribers = set()  # Other agents subscribed to our messages
        
        # Learning and adaptation
        self.memory = AgentMemory(self.agent_id)
        self.adaptation_threshold = 0.7  # Adapt if success rate drops below 70%
        
        # Health monitoring
        self.health_metrics = {
            'cpu_usage': 0.0,
            'memory_usage': 0.0,
            'message_throughput': 0.0,
            'error_rate': 0.0,
            'last_error': None
        }
        
        # Task management
        self.current_task = None
        self.task_queue = asyncio.Queue()
        self.max_concurrent_tasks = 3
        self.running_tasks = set()
        
        # Recovery and resilience
        self.max_errors = 5
        self.error_count = 0
        self.recovery_strategies = []
        
        logger.info(f"🤖 Agent {self.agent_id} initialized")
    
    # =================== LIFECYCLE METHODS ===================
    
    async def spawn(self) -> bool:
        """🚀 Spawn agent - Initialize all systems"""
        try:
            self.state = AgentState.SPAWNING
            logger.info(f"🚀 Spawning agent {self.agent_id}")
            
            # Initialize agent-specific systems
            await self._initialize_systems()
            
            # Start core loops
            self.start_time = datetime.now()
            self.last_heartbeat = time.time()  # Fixed: use timestamp for comparisons

            # Start autonomous loops
            asyncio.create_task(self._main_loop())
            asyncio.create_task(self._communication_loop())
            asyncio.create_task(self._monitoring_loop())
            
            self.state = AgentState.RUNNING
            logger.info(f"✅ Agent {self.agent_id} spawned successfully")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to spawn agent {self.agent_id}: {e}")
            self.state = AgentState.ERROR
            return False
    
    async def run(self):
        """🏃 Main agent execution - Autonomous decision-making loop"""
        while self.state == AgentState.RUNNING:
            try:
                # Process pending tasks
                await self._process_tasks()
                
                # Make autonomous decisions
                await self._autonomous_decision_making()
                
                # Agent-specific behavior
                await self._agent_behavior()
                
                # Short sleep to prevent CPU spinning
                await asyncio.sleep(0.1)
                
            except Exception as e:
                logger.error(f"❌ Error in agent {self.agent_id} main loop: {e}")
                await self._handle_error(e)
    
    async def monitor(self):
        """📊 Monitor agent health and performance"""
        while self.state in [AgentState.RUNNING, AgentState.MONITORING]:
            try:
                self.state = AgentState.MONITORING
                
                # Update health metrics
                await self._update_health_metrics()
                
                # Check for issues
                issues = await self._detect_issues()
                if issues:
                    logger.warning(f"⚠️ Agent {self.agent_id} issues detected: {issues}")
                    await self._handle_issues(issues)
                
                # Update heartbeat
                self.last_heartbeat = time.time()  # Fixed: use timestamp for comparisons

                self.state = AgentState.RUNNING
                await asyncio.sleep(5)  # Monitor every 5 seconds
                
            except Exception as e:
                logger.error(f"❌ Monitoring error for agent {self.agent_id}: {e}")
                await self._handle_error(e)
    
    async def adapt(self):
        """🧠 Learn and adapt based on experiences"""
        try:
            self.state = AgentState.ADAPTING
            logger.info(f"🧠 Agent {self.agent_id} adapting based on experiences")
            
            # Analyze performance
            if self.memory.success_rate < self.adaptation_threshold:
                logger.warning(f"📉 Low success rate: {self.memory.success_rate:.2f}")
                
                # Implement adaptations
                adaptations = await self._generate_adaptations()
                for adaptation in adaptations:
                    await self._apply_adaptation(adaptation)
                    self.memory.adaptations.append(adaptation)
            
            # Agent-specific adaptations
            await self._agent_specific_adaptation()
            
            self.state = AgentState.RUNNING
            
        except Exception as e:
            logger.error(f"❌ Adaptation error for agent {self.agent_id}: {e}")
            await self._handle_error(e)
    
    async def terminate(self):
        """🛑 Graceful agent termination"""
        try:
            self.state = AgentState.TERMINATING
            logger.info(f"🛑 Terminating agent {self.agent_id}")
            
            # Complete current tasks
            await self._complete_current_tasks()
            
            # Clean up resources
            await self._cleanup_resources()
            
            # Save learning data
            await self._save_agent_state()
            
            self.state = AgentState.TERMINATED
            logger.info(f"✅ Agent {self.agent_id} terminated gracefully")
            
        except Exception as e:
            logger.error(f"❌ Termination error for agent {self.agent_id}: {e}")
            self.state = AgentState.ERROR
    
    # =================== COMMUNICATION METHODS ===================
    
    async def send_message(self, receiver_id: str, message_type: str, 
                          payload: Dict[str, Any], priority: int = 1):
        """📤 Send message to another agent"""
        message = AgentMessage(self.agent_id, receiver_id, message_type, payload, priority)
        await self.outbound_queue.put(message)
        logger.debug(f"📤 Agent {self.agent_id} sent {message_type} to {receiver_id}")
    
    async def receive_message(self) -> Optional[AgentMessage]:
        """📥 Receive message from queue"""
        try:
            message = await asyncio.wait_for(self.message_queue.get(), timeout=0.1)
            logger.debug(f"📥 Agent {self.agent_id} received {message.message_type}")
            return message
        except asyncio.TimeoutError:
            return None
    
    async def broadcast_message(self, message_type: str, payload: Dict[str, Any]):
        """📢 Broadcast message to all subscribers"""
        for subscriber_id in self.subscribers:
            await self.send_message(subscriber_id, message_type, payload)
    
    # =================== ABSTRACT METHODS (MUST IMPLEMENT) ===================
    
    @abstractmethod
    async def _agent_behavior(self):
        """🎯 Implement agent-specific autonomous behavior"""
        pass
    
    @abstractmethod
    async def _initialize_systems(self):
        """⚙️ Initialize agent-specific systems"""
        pass
    
    @abstractmethod
    async def _agent_specific_adaptation(self):
        """🧠 Implement agent-specific learning adaptations"""
        pass
    
    # =================== INTERNAL METHODS ===================
    
    async def _main_loop(self):
        """🔄 Main autonomous loop"""
        await self.run()
    
    async def _communication_loop(self):
        """💬 Handle message processing"""
        while self.state != AgentState.TERMINATED:
            try:
                # Process incoming messages
                message = await self.receive_message()
                if message:
                    await self._handle_message(message)
                
                # Process outbound messages
                try:
                    outbound = await asyncio.wait_for(self.outbound_queue.get(), timeout=0.1)
                    # In a real system, this would route to the target agent
                    logger.debug(f"📨 Routing message from {outbound.sender_id} to {outbound.receiver_id}")
                except asyncio.TimeoutError:
                    pass
                    
            except Exception as e:
                logger.error(f"❌ Communication error: {e}")
                
            await asyncio.sleep(0.1)
    
    async def _monitoring_loop(self):
        """📊 Continuous monitoring loop"""
        await self.monitor()
    
    async def _handle_message(self, message: AgentMessage):
        """📨 Handle incoming message"""
        try:
            if message.message_type == "ping":
                await self.send_message(message.sender_id, "pong", {"status": "ok"})
            elif message.message_type == "task":
                await self._handle_task_message(message)
            elif message.message_type == "coordination":
                await self._handle_coordination_message(message)
            else:
                logger.warning(f"❓ Unknown message type: {message.message_type}")
                
        except Exception as e:
            logger.error(f"❌ Error handling message: {e}")
    
    async def _handle_task_message(self, message: AgentMessage):
        """📋 Handle task assignment message"""
        task = message.payload.get('task')
        if task:
            await self.task_queue.put(task)
            logger.info(f"📋 Agent {self.agent_id} received task: {task.get('type', 'unknown')}")
    
    async def _handle_coordination_message(self, message: AgentMessage):
        """🤝 Handle inter-agent coordination"""
        coord_type = message.payload.get('coordination_type')
        logger.info(f"🤝 Agent {self.agent_id} handling coordination: {coord_type}")
    
    async def _process_tasks(self):
        """📋 Process queued tasks"""
        while not self.task_queue.empty() and len(self.running_tasks) < self.max_concurrent_tasks:
            try:
                task = await asyncio.wait_for(self.task_queue.get(), timeout=0.1)
                task_coroutine = asyncio.create_task(self._execute_task(task))
                self.running_tasks.add(task_coroutine)
                
                # Remove completed tasks
                self.running_tasks = {t for t in self.running_tasks if not t.done()}
                
            except asyncio.TimeoutError:
                break
            except Exception as e:
                logger.error(f"❌ Error processing tasks: {e}")
    
    async def _execute_task(self, task: Dict[str, Any]):
        """⚡ Execute a specific task"""
        task_id = task.get('id', 'unknown')
        task_type = task.get('type', 'unknown')
        start_time = time.time()
        
        try:
            logger.info(f"⚡ Agent {self.agent_id} executing task {task_id} ({task_type})")
            
            # Execute task-specific logic
            result = await self._task_execution_logic(task)
            
            # Record success
            duration = time.time() - start_time
            self.memory.record_experience(task_type, 'success', duration, {'result': result})
            
            logger.info(f"✅ Task {task_id} completed successfully in {duration:.2f}s")
            
        except Exception as e:
            # Record failure
            duration = time.time() - start_time
            self.memory.record_experience(task_type, 'failure', duration, {'error': str(e)})
            
            logger.error(f"❌ Task {task_id} failed: {e}")
            await self._handle_error(e)
    
    async def _task_execution_logic(self, task: Dict[str, Any]) -> Any:
        """🎯 Override this for specific task execution"""
        # Default implementation
        await asyncio.sleep(0.5)  # Simulate work
        return {"status": "completed", "data": "default_result"}
    
    async def _autonomous_decision_making(self):
        """🧠 Make autonomous decisions based on state"""
        # Check if adaptation is needed
        if (self.memory.total_tasks > 10 and 
            self.memory.success_rate < self.adaptation_threshold):
            asyncio.create_task(self.adapt())
        
        # Check for proactive actions
        await self._proactive_actions()
    
    async def _proactive_actions(self):
        """🎯 Take proactive autonomous actions"""
        # Override in specific agents
        pass
    
    async def _update_health_metrics(self):
        """📊 Update agent health metrics"""
        try:
            process = psutil.Process(self.process_id)
            self.health_metrics['cpu_usage'] = process.cpu_percent()
            self.health_metrics['memory_usage'] = process.memory_info().rss / 1024 / 1024  # MB
            
            # Calculate message throughput
            # Implementation would track messages per second
            
        except Exception as e:
            logger.error(f"❌ Error updating health metrics: {e}")
    
    async def _detect_issues(self) -> List[str]:
        """🔍 Detect performance or health issues"""
        issues = []
        
        if self.health_metrics['cpu_usage'] > 80:
            issues.append("high_cpu_usage")
        
        if self.health_metrics['memory_usage'] > 500:  # 500MB
            issues.append("high_memory_usage")
        
        if self.error_count > self.max_errors:
            issues.append("too_many_errors")
        
        return issues
    
    async def _handle_issues(self, issues: List[str]):
        """🛠️ Handle detected issues"""
        for issue in issues:
            if issue == "high_cpu_usage":
                await asyncio.sleep(1)  # Back off
            elif issue == "high_memory_usage":
                import gc
                gc.collect()
            elif issue == "too_many_errors":
                logger.critical(f"🚨 Agent {self.agent_id} has too many errors, considering restart")
    
    async def _handle_error(self, error: Exception):
        """🚨 Handle agent errors with recovery"""
        self.error_count += 1
        self.health_metrics['last_error'] = str(error)
        
        if self.error_count >= self.max_errors:
            logger.critical(f"🚨 Agent {self.agent_id} error threshold exceeded")
            await self.terminate()
        else:
            # Attempt recovery
            await asyncio.sleep(2 ** self.error_count)  # Exponential backoff
    
    async def _generate_adaptations(self) -> List[Dict[str, Any]]:
        """🧠 Generate adaptations based on performance"""
        adaptations = []
        
        # Analyze failure patterns
        if self.memory.total_tasks > 0:
            failure_rate = 1 - self.memory.success_rate
            if failure_rate > 0.3:  # 30% failure rate
                adaptations.append({
                    'type': 'increase_timeout',
                    'reason': 'high_failure_rate',
                    'parameters': {'multiplier': 1.5}
                })
        
        return adaptations
    
    async def _apply_adaptation(self, adaptation: Dict[str, Any]):
        """🔧 Apply specific adaptation"""
        adaptation_type = adaptation['type']
        logger.info(f"🔧 Applying adaptation: {adaptation_type}")
        
        if adaptation_type == 'increase_timeout':
            # Increase operation timeouts
            multiplier = adaptation['parameters']['multiplier']
            # Implementation would adjust timeout values
    
    async def _complete_current_tasks(self):
        """⏳ Wait for current tasks to complete"""
        if self.running_tasks:
            await asyncio.gather(*self.running_tasks, return_exceptions=True)
    
    async def _cleanup_resources(self):
        """🧹 Clean up agent resources"""
        # Close connections, files, etc.
        pass
    
    async def _save_agent_state(self):
        """💾 Save agent learning data"""
        # Helper function to serialize HealthMetric objects
        def serialize_health_metrics(metrics):
            """Convert HealthMetric objects to their numeric values"""
            serialized = {}
            for key, value in metrics.items():
                # Check if it's a HealthMetric object (has current_value attribute)
                if hasattr(value, 'current_value'):
                    serialized[key] = value.current_value
                elif isinstance(value, (int, float, str, bool, type(None))):
                    serialized[key] = value
                else:
                    # Fallback for unknown types
                    serialized[key] = str(value)
            return serialized

        state_data = {
            'agent_id': self.agent_id,
            'total_tasks': self.memory.total_tasks,
            'success_rate': self.memory.success_rate,
            'patterns': self.memory.patterns,
            'adaptations': self.memory.adaptations,
            'health_metrics': serialize_health_metrics(self.health_metrics)
        }

        # Save to file or database
        state_file = f"agents/state_{self.agent_id}.json"
        try:
            with open(state_file, 'w') as f:
                json.dump(state_data, f, indent=2, default=str)
            logger.info(f"💾 Agent state saved to {state_file}")
        except Exception as e:
            logger.error(f"❌ Error saving agent state: {e}")

# =================== AGENT REGISTRY ===================

class AgentRegistry:
    """📋 Global agent registry and discovery system"""
    
    def __init__(self):
        self.agents = {}  # agent_id -> agent_info
        self.agent_types = {}  # agent_type -> list of agent_ids
        self.message_router = {}  # agent_id -> message_queue
    
    def register_agent(self, agent: AutonomousAgent):
        """📝 Register new agent"""
        agent_info = {
            'agent_id': agent.agent_id,
            'agent_type': agent.__class__.__name__,
            'state': agent.state,
            'start_time': agent.start_time,
            'process_id': agent.process_id
        }
        
        self.agents[agent.agent_id] = agent_info
        
        agent_type = agent.__class__.__name__
        if agent_type not in self.agent_types:
            self.agent_types[agent_type] = []
        self.agent_types[agent_type].append(agent.agent_id)
        
        self.message_router[agent.agent_id] = agent.message_queue
        
        logger.info(f"📝 Registered agent {agent.agent_id} ({agent_type})")
    
    def unregister_agent(self, agent_id: str):
        """🗑️ Remove agent from registry"""
        if agent_id in self.agents:
            agent_info = self.agents[agent_id]
            agent_type = agent_info['agent_type']
            
            del self.agents[agent_id]
            if agent_id in self.message_router:
                del self.message_router[agent_id]
            
            if agent_type in self.agent_types:
                self.agent_types[agent_type].remove(agent_id)
                if not self.agent_types[agent_type]:
                    del self.agent_types[agent_type]
            
            logger.info(f"🗑️ Unregistered agent {agent_id}")
    
    def get_agents_by_type(self, agent_type: str) -> List[str]:
        """🔍 Find agents by type"""
        return self.agent_types.get(agent_type, [])
    
    def route_message(self, message: AgentMessage):
        """📨 Route message to target agent"""
        if message.receiver_id in self.message_router:
            queue = self.message_router[message.receiver_id]
            asyncio.create_task(queue.put(message))
        else:
            logger.warning(f"❓ No route found for agent {message.receiver_id}")

# Global agent registry
AGENT_REGISTRY = AgentRegistry()

if __name__ == "__main__":
    # Test the base agent system
    class TestAgent(AutonomousAgent):
        async def _agent_behavior(self):
            await asyncio.sleep(1)
            
        async def _initialize_systems(self):
            logger.info("🔧 Test agent systems initialized")
            
        async def _agent_specific_adaptation(self):
            logger.info("🧠 Test agent adaptation")
    
    async def test_agent():
        agent = TestAgent("test_agent_001")
        await agent.spawn()
        await asyncio.sleep(5)
        await agent.terminate()
    
    asyncio.run(test_agent())