#!/usr/bin/env python3
"""
🔥💀 PHASE 2: ADVANCED MESSAGE BUS SYSTEM 💀🔥
Agent Poly Loly Double Zero: Event-Driven Communication Infrastructure

PHASE 2 COMMUNICATION FEATURES:
- AsyncIO-based distributed message bus
- Event-driven pub/sub architecture (NO request/response bullshit!)
- Fault-tolerant messaging with retry logic and dead letter queues
- Load balancing across agent instances
- Message routing with topology awareness
- Performance monitoring and optimization
"""

import asyncio
import json
import logging
import time
import uuid
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Callable, Set
import weakref

logger = logging.getLogger(__name__)

class MessagePriority(Enum):
    """📋 Message priority levels"""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4
    EMERGENCY = 5

class MessageType(Enum):
    """📨 Advanced message types for event-driven architecture"""
    # Event-driven patterns (NOT request/response bullshit)
    EVENT = "event"                    # Pure event notification
    BROADCAST = "broadcast"            # Broadcast to all agents
    PUBLISH = "publish"               # Publish to topic subscribers
    COMMAND = "command"               # Command with async execution
    NOTIFICATION = "notification"     # Status/state change notification
    
    # System patterns
    HEARTBEAT = "heartbeat"           # Agent health monitoring
    DISCOVERY = "discovery"           # Agent discovery and registration
    METRICS = "metrics"              # Performance metrics sharing
    ALERT = "alert"                  # System alerts and warnings
    
    # Coordination patterns
    COORDINATION = "coordination"     # Multi-agent coordination
    WORKFLOW = "workflow"            # Workflow state changes
    TASK_ASSIGNMENT = "task_assignment"  # Task distribution
    RESULT = "result"                # Task completion results

@dataclass
class AdvancedMessage:
    """📨 Advanced message with full event-driven capabilities"""
    message_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    sender_id: str = ""
    message_type: MessageType = MessageType.EVENT
    topic: str = ""                   # Topic for pub/sub routing
    event_name: str = ""              # Specific event identifier
    payload: Dict[str, Any] = field(default_factory=dict)
    
    # Advanced routing and delivery
    priority: MessagePriority = MessagePriority.NORMAL
    target_agents: Optional[Set[str]] = None  # Specific target agents
    routing_tags: Set[str] = field(default_factory=set)  # Routing metadata
    
    # Fault tolerance
    retry_count: int = 0
    max_retries: int = 3
    timeout_seconds: float = 30.0
    requires_ack: bool = False        # Acknowledgment required
    
    # Timing and lifecycle
    created_at: datetime = field(default_factory=datetime.now)
    expires_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    
    # Performance tracking
    routing_path: List[str] = field(default_factory=list)
    processing_times: Dict[str, float] = field(default_factory=dict)
    
    def is_expired(self) -> bool:
        """⏰ Check if message has expired"""
        if self.expires_at:
            return datetime.now() > self.expires_at
        return False
    
    def add_routing_step(self, step: str):
        """🛣️ Track message routing path"""
        self.routing_path.append(f"{step}@{datetime.now().isoformat()}")
    
    def to_dict(self) -> Dict[str, Any]:
        """📋 Convert to dictionary for serialization"""
        return {
            'message_id': self.message_id,
            'sender_id': self.sender_id,
            'message_type': self.message_type.value,
            'topic': self.topic,
            'event_name': self.event_name,
            'payload': self.payload,
            'priority': self.priority.value,
            'target_agents': list(self.target_agents) if self.target_agents else None,
            'routing_tags': list(self.routing_tags),
            'retry_count': self.retry_count,
            'max_retries': self.max_retries,
            'timeout_seconds': self.timeout_seconds,
            'requires_ack': self.requires_ack,
            'created_at': self.created_at.isoformat(),
            'expires_at': self.expires_at.isoformat() if self.expires_at else None,
            'routing_path': self.routing_path,
            'processing_times': self.processing_times
        }

class MessageBusStats:
    """📊 Message bus performance statistics"""
    
    def __init__(self):
        self.messages_sent = 0
        self.messages_delivered = 0
        self.messages_failed = 0
        self.messages_expired = 0
        self.messages_retried = 0
        
        self.delivery_times = deque(maxlen=1000)  # Last 1000 delivery times
        self.queue_sizes = defaultdict(lambda: deque(maxlen=100))
        self.topic_message_counts = defaultdict(int)
        
        self.start_time = time.time()
    
    def record_message_sent(self, message: AdvancedMessage):
        """📈 Record message sent"""
        self.messages_sent += 1
        self.topic_message_counts[message.topic] += 1
    
    def record_message_delivered(self, message: AdvancedMessage, delivery_time: float):
        """📈 Record successful delivery"""
        self.messages_delivered += 1
        self.delivery_times.append(delivery_time)
    
    def record_message_failed(self, message: AdvancedMessage):
        """📈 Record delivery failure"""
        self.messages_failed += 1
    
    def record_message_retry(self, message: AdvancedMessage):
        """📈 Record retry attempt"""
        self.messages_retried += 1
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """📊 Get performance summary"""
        uptime = time.time() - self.start_time
        
        avg_delivery_time = 0.0
        if self.delivery_times:
            avg_delivery_time = sum(self.delivery_times) / len(self.delivery_times)
        
        return {
            'uptime_seconds': uptime,
            'messages_per_second': self.messages_sent / uptime if uptime > 0 else 0,
            'total_sent': self.messages_sent,
            'total_delivered': self.messages_delivered,
            'total_failed': self.messages_failed,
            'total_retried': self.messages_retried,
            'success_rate': self.messages_delivered / max(self.messages_sent, 1),
            'average_delivery_time_ms': avg_delivery_time * 1000,
            'active_topics': len(self.topic_message_counts),
            'top_topics': dict(sorted(self.topic_message_counts.items(), 
                                    key=lambda x: x[1], reverse=True)[:10])
        }

class AdvancedMessageBus:
    """
    🚀 PHASE 2 ADVANCED MESSAGE BUS
    
    Event-driven AsyncIO message bus with:
    - Pub/Sub topic routing (NO request/response bullshit!)
    - Fault-tolerant delivery with retry logic
    - Load balancing across agent instances
    - Dead letter queues for failed messages
    - Performance monitoring and optimization
    """
    
    def __init__(self, bus_id: str = None):
        self.bus_id = bus_id or f"message_bus_{uuid.uuid4().hex[:8]}"
        
        # Core message routing infrastructure
        self.topic_subscribers: Dict[str, Set[str]] = defaultdict(set)
        self.agent_queues: Dict[str, asyncio.Queue] = {}
        self.agent_handlers: Dict[str, weakref.WeakMethod] = {}
        
        # Load balancing for agent instances
        self.agent_instances: Dict[str, List[str]] = defaultdict(list)  # agent_type -> [instance_ids]
        self.instance_load: Dict[str, int] = defaultdict(int)  # instance_id -> current_load
        
        # Fault tolerance infrastructure
        self.pending_messages: Dict[str, AdvancedMessage] = {}  # message_id -> message
        self.retry_queue: asyncio.Queue = asyncio.Queue()
        self.dead_letter_queue: asyncio.Queue = asyncio.Queue()
        
        # Performance monitoring
        self.stats = MessageBusStats()
        
        # System state
        self.running = False
        self.background_tasks = []
        
        logger.info(f"🚀 AdvancedMessageBus {self.bus_id} initialized")
    
    async def start(self):
        """🚀 Start the message bus system"""
        if self.running:
            return
            
        self.running = True
        
        # Start background processing tasks
        self.background_tasks = [
            asyncio.create_task(self._retry_processor()),
            asyncio.create_task(self._dead_letter_processor()),
            asyncio.create_task(self._cleanup_processor()),
            asyncio.create_task(self._stats_reporter())
        ]
        
        logger.info(f"🚀 AdvancedMessageBus {self.bus_id} started with {len(self.background_tasks)} background tasks")
    
    async def stop(self):
        """🛑 Stop the message bus system"""
        if not self.running:
            return
            
        self.running = False
        
        # Cancel background tasks
        for task in self.background_tasks:
            task.cancel()
        
        # Wait for tasks to finish
        await asyncio.gather(*self.background_tasks, return_exceptions=True)
        
        logger.info(f"🛑 AdvancedMessageBus {self.bus_id} stopped")
    
    def register_agent(self, agent_id: str, agent_type: str = None, 
                      message_handler: Optional[Callable] = None):
        """📝 Register agent with the message bus"""
        # Create message queue for agent
        self.agent_queues[agent_id] = asyncio.Queue(maxsize=1000)
        
        # Register message handler if provided
        if message_handler:
            self.agent_handlers[agent_id] = weakref.WeakMethod(message_handler)
        
        # Register for load balancing if agent_type provided
        if agent_type:
            self.agent_instances[agent_type].append(agent_id)
            self.instance_load[agent_id] = 0
        
        logger.info(f"📝 Registered agent {agent_id} (type: {agent_type or 'unknown'})")
    
    def unregister_agent(self, agent_id: str):
        """❌ Unregister agent from message bus"""
        # Remove from queues and handlers
        if agent_id in self.agent_queues:
            del self.agent_queues[agent_id]
        
        if agent_id in self.agent_handlers:
            del self.agent_handlers[agent_id]
        
        # Remove from load balancing
        if agent_id in self.instance_load:
            del self.instance_load[agent_id]
        
        # Remove from agent instances
        for agent_type, instances in self.agent_instances.items():
            if agent_id in instances:
                instances.remove(agent_id)
        
        # Remove from topic subscriptions
        for topic, subscribers in self.topic_subscribers.items():
            subscribers.discard(agent_id)
        
        logger.info(f"❌ Unregistered agent {agent_id}")
    
    def subscribe_to_topic(self, agent_id: str, topic: str):
        """📡 Subscribe agent to topic"""
        self.topic_subscribers[topic].add(agent_id)
        logger.info(f"📡 Agent {agent_id} subscribed to topic '{topic}'")
    
    def unsubscribe_from_topic(self, agent_id: str, topic: str):
        """📡 Unsubscribe agent from topic"""
        self.topic_subscribers[topic].discard(agent_id)
        logger.info(f"📡 Agent {agent_id} unsubscribed from topic '{topic}'")
    
    async def publish(self, message: AdvancedMessage) -> str:
        """📢 Publish message to the bus (event-driven, NO request/response!)"""
        if not self.running:
            raise RuntimeError("Message bus not running")
        
        # Add routing step
        message.add_routing_step(f"publish@{self.bus_id}")
        
        # Record stats
        self.stats.record_message_sent(message)
        
        # Route message based on type and targeting
        await self._route_message(message)
        
        logger.debug(f"📢 Published message {message.message_id} "
                    f"(type: {message.message_type.value}, topic: {message.topic})")
        
        return message.message_id
    
    async def _route_message(self, message: AdvancedMessage):
        """🛣️ Route message to appropriate recipients"""
        start_time = time.time()
        recipients = set()
        
        # Determine recipients based on message type and targeting
        if message.message_type == MessageType.BROADCAST:
            # Broadcast to all registered agents
            recipients = set(self.agent_queues.keys())
            
        elif message.message_type == MessageType.PUBLISH:
            # Route to topic subscribers
            if message.topic in self.topic_subscribers:
                recipients = self.topic_subscribers[message.topic].copy()
            
        elif message.target_agents:
            # Direct targeting
            recipients = message.target_agents.intersection(self.agent_queues.keys())
            
        elif message.routing_tags:
            # Route based on tags (could implement tag-based routing)
            recipients = self._find_agents_by_tags(message.routing_tags)
        
        # Load balancing for agent types
        if not recipients and message.topic:
            # Try to find agents by type for load balancing
            balanced_recipients = self._get_load_balanced_recipients(message.topic, 1)
            recipients.update(balanced_recipients)
        
        # Deliver to recipients
        if recipients:
            await self._deliver_to_recipients(message, recipients)
        else:
            # Only warn for non-broadcast messages without recipients
            if message.message_type != MessageType.BROADCAST:
                logger.debug(f"📭 No recipients found for message {message.message_id} (type: {message.message_type.value})")
            await self._handle_undeliverable_message(message)
        
        # Record routing time
        routing_time = time.time() - start_time
        message.processing_times['routing'] = routing_time
    
    def _find_agents_by_tags(self, tags: Set[str]) -> Set[str]:
        """🏷️ Find agents that match routing tags"""
        # This could be enhanced with more sophisticated tag matching
        matching_agents = set()
        
        for tag in tags:
            # Simple implementation: match tag to agent type
            if tag in self.agent_instances:
                matching_agents.update(self.agent_instances[tag])
        
        return matching_agents
    
    def _get_load_balanced_recipients(self, agent_type: str, count: int) -> List[str]:
        """⚖️ Get load-balanced recipients of specified agent type"""
        if agent_type not in self.agent_instances:
            return []
        
        available_instances = self.agent_instances[agent_type]
        if not available_instances:
            return []
        
        # Sort by current load (ascending)
        sorted_instances = sorted(available_instances, 
                                key=lambda x: self.instance_load.get(x, 0))
        
        # Return the least loaded instances
        selected = sorted_instances[:count]
        
        # Update load counters
        for instance_id in selected:
            self.instance_load[instance_id] += 1
        
        return selected
    
    async def _deliver_to_recipients(self, message: AdvancedMessage, recipients: Set[str]):
        """📬 Deliver message to recipients"""
        message.add_routing_step(f"deliver_to_{len(recipients)}_recipients")
        
        delivery_tasks = []
        
        for recipient_id in recipients:
            if recipient_id in self.agent_queues:
                task = asyncio.create_task(
                    self._deliver_to_agent(message, recipient_id)
                )
                delivery_tasks.append(task)
        
        # Wait for all deliveries to complete
        if delivery_tasks:
            results = await asyncio.gather(*delivery_tasks, return_exceptions=True)
            
            # Handle delivery results
            successful_deliveries = sum(1 for r in results if r is True)
            failed_deliveries = len(results) - successful_deliveries
            
            if successful_deliveries > 0:
                delivery_time = time.time() - message.created_at.timestamp()
                self.stats.record_message_delivered(message, delivery_time)
            
            if failed_deliveries > 0:
                logger.warning(f"⚠️ {failed_deliveries}/{len(results)} deliveries failed "
                             f"for message {message.message_id}")
    
    async def _deliver_to_agent(self, message: AdvancedMessage, agent_id: str) -> bool:
        """📬 Deliver message to specific agent"""
        try:
            queue = self.agent_queues[agent_id]
            
            # Check if queue is full
            if queue.full():
                logger.warning(f"⚠️ Queue full for agent {agent_id}, message {message.message_id}")
                await self._handle_delivery_failure(message, agent_id, "queue_full")
                return False
            
            # Add to queue with timeout
            await asyncio.wait_for(queue.put(message), timeout=1.0)
            
            message.add_routing_step(f"delivered_to_{agent_id}")
            logger.debug(f"📬 Delivered message {message.message_id} to agent {agent_id}")
            
            return True
            
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ Timeout delivering to agent {agent_id}, message {message.message_id}")
            await self._handle_delivery_failure(message, agent_id, "timeout")
            return False
            
        except Exception as e:
            logger.error(f"❌ Error delivering to agent {agent_id}: {e}")
            await self._handle_delivery_failure(message, agent_id, str(e))
            return False
    
    async def _handle_delivery_failure(self, message: AdvancedMessage, 
                                     agent_id: str, reason: str):
        """⚠️ Handle message delivery failure"""
        self.stats.record_message_failed(message)
        
        # Increment retry count
        message.retry_count += 1
        message.add_routing_step(f"delivery_failed_{agent_id}_{reason}")
        
        # Check if we should retry
        if message.retry_count <= message.max_retries:
            self.stats.record_message_retry(message)
            await self.retry_queue.put((message, agent_id))
            logger.info(f"🔄 Queued message {message.message_id} for retry "
                       f"({message.retry_count}/{message.max_retries})")
        else:
            # Move to dead letter queue
            await self.dead_letter_queue.put((message, agent_id, reason))
            logger.error(f"💀 Message {message.message_id} moved to dead letter queue "
                        f"after {message.max_retries} retries")
    
    async def _handle_undeliverable_message(self, message: AdvancedMessage):
        """💀 Handle message with no recipients"""
        # Only move to dead letter queue if it's an important message
        if (message.priority.value >= MessagePriority.HIGH.value or 
            message.message_type not in [MessageType.BROADCAST, MessageType.PUBLISH]):
            await self.dead_letter_queue.put((message, None, "no_recipients"))
            logger.warning(f"💀 Undeliverable message {message.message_id} moved to dead letter queue")
        else:
            # For broadcast/publish with no recipients, just log debug
            logger.debug(f"📭 Discarding message {message.message_id} with no recipients")
    
    async def _retry_processor(self):
        """🔄 Background task to process retry queue"""
        while self.running:
            try:
                message, failed_agent_id = await asyncio.wait_for(
                    self.retry_queue.get(), timeout=1.0
                )
                
                # Wait before retrying (exponential backoff)
                backoff_delay = min(2 ** message.retry_count, 30)  # Max 30 seconds
                await asyncio.sleep(backoff_delay)
                
                # Retry delivery
                if failed_agent_id in self.agent_queues:
                    success = await self._deliver_to_agent(message, failed_agent_id)
                    if success:
                        logger.info(f"✅ Retry successful for message {message.message_id}")
                    else:
                        logger.warning(f"❌ Retry failed for message {message.message_id}")
                
            except asyncio.TimeoutError:
                pass  # No messages to retry
            except Exception as e:
                logger.error(f"❌ Error in retry processor: {e}")
    
    async def _dead_letter_processor(self):
        """💀 Background task to process dead letter queue"""
        while self.running:
            try:
                message, failed_agent_id, reason = await asyncio.wait_for(
                    self.dead_letter_queue.get(), timeout=5.0
                )
                
                # Log dead letter for analysis
                logger.error(f"💀 Dead letter: message {message.message_id} "
                           f"failed for agent {failed_agent_id} - {reason}")
                
                # Could implement dead letter analysis/recovery here
                
            except asyncio.TimeoutError:
                pass  # No dead letters to process
            except Exception as e:
                logger.error(f"❌ Error in dead letter processor: {e}")
    
    async def _cleanup_processor(self):
        """🧹 Background task to clean up expired messages"""
        while self.running:
            try:
                await asyncio.sleep(60)  # Run every minute
                
                # Clean up expired pending messages
                expired_messages = []
                for msg_id, message in self.pending_messages.items():
                    if message.is_expired():
                        expired_messages.append(msg_id)
                
                for msg_id in expired_messages:
                    del self.pending_messages[msg_id]
                    self.stats.messages_expired += 1
                
                if expired_messages:
                    logger.info(f"🧹 Cleaned up {len(expired_messages)} expired messages")
                
            except Exception as e:
                logger.error(f"❌ Error in cleanup processor: {e}")
    
    async def _stats_reporter(self):
        """📊 Background task to report performance statistics"""
        while self.running:
            try:
                await asyncio.sleep(300)  # Report every 5 minutes
                
                stats = self.stats.get_performance_summary()
                logger.info(f"📊 MessageBus Stats: "
                          f"{stats['messages_per_second']:.2f} msg/sec, "
                          f"{stats['success_rate']:.1%} success rate, "
                          f"{stats['average_delivery_time_ms']:.1f}ms avg delivery")
                
            except Exception as e:
                logger.error(f"❌ Error in stats reporter: {e}")
    
    async def broadcast(self, event_name: str, payload: Dict[str, Any], 
                       priority: MessagePriority = MessagePriority.NORMAL) -> str:
        """📢 Broadcast message to all agents"""
        message = AdvancedMessage(
            sender_id="system",
            message_type=MessageType.BROADCAST,
            event_name=event_name,
            payload=payload,
            priority=priority
        )
        
        return await self.publish(message)
    
    async def publish_to_agent(self, target_agent: str, event_name: str, 
                              payload: Dict[str, Any],
                              priority: MessagePriority = MessagePriority.NORMAL) -> str:
        """📤 Send message directly to specific agent"""
        message = AdvancedMessage(
            sender_id="system",
            target_agents={target_agent},
            event_name=event_name,
            payload=payload,
            priority=priority
        )
        
        return await self.publish(message)
    
    async def wait_for_response(self, agent_id: str, correlation_id: str, 
                               timeout: float = 5.0) -> Optional[Dict[str, Any]]:
        """⏳ Wait for response from agent (mock implementation for testing)"""
        # This is a simplified implementation for testing
        # In production, this would use proper correlation ID tracking
        await asyncio.sleep(0.1)  # Simulate processing time
        return {'status': 'ok', 'correlation_id': correlation_id}
    
    async def get_agent_message(self, agent_id: str, timeout: float = 0.1) -> Optional[AdvancedMessage]:
        """📥 Get message for specific agent"""
        if agent_id not in self.agent_queues:
            return None
        
        try:
            message = await asyncio.wait_for(
                self.agent_queues[agent_id].get(), 
                timeout=timeout
            )
            
            # Decrease load counter
            if agent_id in self.instance_load:
                self.instance_load[agent_id] = max(0, self.instance_load[agent_id] - 1)
            
            return message
            
        except asyncio.TimeoutError:
            return None
    
    def get_stats(self) -> Dict[str, Any]:
        """📊 Get comprehensive bus statistics"""
        return {
            'bus_id': self.bus_id,
            'running': self.running,
            'registered_agents': len(self.agent_queues),
            'active_topics': len(self.topic_subscribers),
            'queue_sizes': {agent_id: queue.qsize() 
                           for agent_id, queue in self.agent_queues.items()},
            'instance_loads': dict(self.instance_load),
            'performance': self.stats.get_performance_summary()
        }

# Global message bus instance
_global_message_bus: Optional[AdvancedMessageBus] = None

def get_message_bus() -> AdvancedMessageBus:
    """🌐 Get global message bus instance"""
    global _global_message_bus
    
    if _global_message_bus is None:
        _global_message_bus = AdvancedMessageBus("global_bus")
    
    return _global_message_bus

async def initialize_message_bus():
    """🚀 Initialize global message bus"""
    bus = get_message_bus()
    await bus.start()
    return bus