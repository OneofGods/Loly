#!/usr/bin/env python3
"""
🔥💀 PHASE 2: ENHANCED AUTONOMOUS AGENT 💀🔥
Agent Poly Loly Double Zero: Phase 1 + Phase 2 Integration

PHASE 2 ENHANCED FEATURES:
- Advanced message bus integration
- Event-driven communication (NO request/response bullshit!)
- Fault-tolerant messaging with retry logic
- Load-balanced message distribution
- Topic-based pub/sub patterns
- Performance monitoring integration
"""

import asyncio
import logging
from abc import ABC
from typing import Dict, Any, Optional, Set, List
from datetime import datetime

from core.autonomous_agent import AutonomousAgent, AgentState
from core.message_bus import (
    get_message_bus, AdvancedMessage, MessageType, MessagePriority
)

logger = logging.getLogger(__name__)

class EnhancedAutonomousAgent(AutonomousAgent, ABC):
    """
    🚀 PHASE 2 ENHANCED AUTONOMOUS AGENT
    
    Combines Phase 1 foundation with Phase 2 advanced communication:
    - Inherits all Phase 1 autonomous behaviors
    - Integrates advanced message bus system
    - Event-driven communication patterns
    - Fault-tolerant messaging
    - Performance monitoring integration
    """
    
    def __init__(self, agent_id: str, agent_type: str = "Enhanced"):
        super().__init__(agent_id)
        
        self.agent_type = agent_type
        self.message_bus = get_message_bus()
        
        # Enhanced communication features
        self.subscribed_topics: Set[str] = set()
        self.event_handlers: Dict[str, callable] = {}
        self.message_stats = {
            'sent': 0,
            'received': 0,
            'events_published': 0,
            'commands_processed': 0
        }
        
        # Phase 2 configuration
        self.enable_load_balancing = True
        self.message_priority = MessagePriority.NORMAL
        self.fault_tolerance_enabled = True
        
        logger.info(f"🚀 EnhancedAutonomousAgent {self.agent_id} ({self.agent_type}) initialized")
    
    async def spawn(self):
        """🚀 Enhanced spawn with message bus registration"""
        try:
            # Phase 1 spawn
            await super().spawn()
            
            # Phase 2 enhancements
            await self._register_with_message_bus()
            await self._setup_enhanced_communication()
            
            logger.info(f"✅ EnhancedAgent {self.agent_id} spawned with advanced communication")
            
        except Exception as e:
            logger.error(f"❌ Enhanced spawn failed for {self.agent_id}: {e}")
            raise
    
    async def terminate(self):
        """🛑 Enhanced termination with message bus cleanup"""
        try:
            # Cleanup Phase 2 features
            await self._cleanup_message_bus_registration()
            
            # Phase 1 termination
            await super().terminate()
            
            logger.info(f"✅ EnhancedAgent {self.agent_id} terminated gracefully")
            
        except Exception as e:
            logger.error(f"❌ Enhanced termination failed for {self.agent_id}: {e}")
    
    async def _register_with_message_bus(self):
        """📝 Register with advanced message bus"""
        try:
            # Register for load balancing and message delivery
            self.message_bus.register_agent(
                self.agent_id, 
                self.agent_type,
                self._handle_enhanced_message
            )
            
            logger.info(f"📝 Agent {self.agent_id} registered with message bus")
            
        except Exception as e:
            logger.error(f"❌ Message bus registration failed: {e}")
    
    async def _cleanup_message_bus_registration(self):
        """❌ Cleanup message bus registration"""
        try:
            # Unsubscribe from all topics
            for topic in self.subscribed_topics.copy():
                await self.unsubscribe_from_topic(topic)
            
            # Unregister from message bus
            self.message_bus.unregister_agent(self.agent_id)
            
            logger.info(f"❌ Agent {self.agent_id} cleaned up message bus registration")
            
        except Exception as e:
            logger.error(f"❌ Message bus cleanup failed: {e}")
    
    async def _setup_enhanced_communication(self):
        """⚙️ Setup enhanced communication patterns"""
        try:
            # Subscribe to agent-type specific topics
            await self.subscribe_to_topic(f"{self.agent_type.lower()}_events")
            await self.subscribe_to_topic("system_events")
            await self.subscribe_to_topic("coordination_events")
            
            # Setup event handlers
            await self._register_event_handlers()
            
            logger.info(f"⚙️ Enhanced communication setup complete for {self.agent_id}")
            
        except Exception as e:
            logger.error(f"❌ Enhanced communication setup failed: {e}")
    
    async def _register_event_handlers(self):
        """🎯 Register event handlers for different message types"""
        self.event_handlers.update({
            'system_announcement': self._handle_system_announcement,
            'coordination_request': self._handle_coordination_request,
            'health_check': self._handle_health_check,
            'performance_report': self._handle_performance_report,
            'task_assignment': self._handle_task_assignment,
            'workflow_update': self._handle_workflow_update
        })
    
    # =================== ENHANCED MESSAGING METHODS ===================
    
    async def subscribe_to_topic(self, topic: str):
        """📡 Subscribe to topic for event-driven communication"""
        try:
            self.message_bus.subscribe_to_topic(self.agent_id, topic)
            self.subscribed_topics.add(topic)
            
            logger.info(f"📡 Agent {self.agent_id} subscribed to '{topic}'")
            
        except Exception as e:
            logger.error(f"❌ Topic subscription failed for '{topic}': {e}")
    
    async def unsubscribe_from_topic(self, topic: str):
        """📡 Unsubscribe from topic"""
        try:
            self.message_bus.unsubscribe_from_topic(self.agent_id, topic)
            self.subscribed_topics.discard(topic)
            
            logger.info(f"📡 Agent {self.agent_id} unsubscribed from '{topic}'")
            
        except Exception as e:
            logger.error(f"❌ Topic unsubscription failed for '{topic}': {e}")
    
    async def publish_event(self, event_name: str, topic: str, payload: Dict[str, Any], 
                          priority: MessagePriority = None) -> str:
        """📢 Publish event (Phase 2 event-driven, NO request/response!)"""
        try:
            message = AdvancedMessage(
                sender_id=self.agent_id,
                message_type=MessageType.PUBLISH,
                topic=topic,
                event_name=event_name,
                payload=payload,
                priority=priority or self.message_priority
            )
            
            message_id = await self.message_bus.publish(message)
            self.message_stats['events_published'] += 1
            
            logger.debug(f"📢 Published event '{event_name}' to topic '{topic}': {message_id}")
            return message_id
            
        except Exception as e:
            logger.error(f"❌ Event publishing failed: {e}")
            raise
    
    async def broadcast_announcement(self, event_name: str, payload: Dict[str, Any]) -> str:
        """📻 Broadcast announcement to all agents"""
        try:
            message = AdvancedMessage(
                sender_id=self.agent_id,
                message_type=MessageType.BROADCAST,
                event_name=event_name,
                payload=payload,
                priority=MessagePriority.HIGH
            )
            
            message_id = await self.message_bus.publish(message)
            self.message_stats['sent'] += 1
            
            logger.info(f"📻 Broadcasted '{event_name}' to all agents: {message_id}")
            return message_id
            
        except Exception as e:
            logger.error(f"❌ Broadcast failed: {e}")
            raise
    
    async def send_command(self, target_agents: Set[str], command: str, 
                         parameters: Dict[str, Any], priority: MessagePriority = None) -> str:
        """⚡ Send command to specific agents"""
        try:
            message = AdvancedMessage(
                sender_id=self.agent_id,
                message_type=MessageType.COMMAND,
                target_agents=target_agents,
                event_name=command,
                payload=parameters,
                priority=priority or MessagePriority.HIGH,
                requires_ack=True
            )
            
            message_id = await self.message_bus.publish(message)
            self.message_stats['sent'] += 1
            
            logger.info(f"⚡ Sent command '{command}' to {len(target_agents)} agents: {message_id}")
            return message_id
            
        except Exception as e:
            logger.error(f"❌ Command sending failed: {e}")
            raise
    
    async def notify_status_change(self, status: str, details: Dict[str, Any]):
        """📊 Notify other agents of status change"""
        try:
            await self.publish_event(
                event_name="status_change",
                topic="system_events",
                payload={
                    'agent_id': self.agent_id,
                    'agent_type': self.agent_type,
                    'status': status,
                    'details': details,
                    'timestamp': datetime.now().isoformat()
                }
            )
            
        except Exception as e:
            logger.error(f"❌ Status notification failed: {e}")
    
    # =================== ENHANCED MESSAGE PROCESSING ===================
    
    async def _communication_loop(self):
        """💬 Enhanced communication loop with message bus integration"""
        while self.state != AgentState.TERMINATED:
            try:
                # Process messages from enhanced message bus
                message = await self.message_bus.get_agent_message(self.agent_id, timeout=0.1)
                
                if message:
                    await self._handle_enhanced_message(message)
                    self.message_stats['received'] += 1
                
                # Process legacy messages (Phase 1 compatibility)
                legacy_message = await self.receive_message()
                if legacy_message:
                    await self._handle_message(legacy_message)
                
            except Exception as e:
                logger.error(f"❌ Enhanced communication error: {e}")
                
            await asyncio.sleep(0.05)  # Higher frequency for Phase 2
    
    async def _handle_enhanced_message(self, message: AdvancedMessage):
        """📨 Handle enhanced message from Phase 2 message bus"""
        try:
            logger.debug(f"📨 Processing enhanced message: {message.event_name} from {message.sender_id}")
            
            # Route to specific event handler
            if message.event_name in self.event_handlers:
                handler = self.event_handlers[message.event_name]
                await handler(message)
            else:
                # Generic message handling
                await self._handle_generic_enhanced_message(message)
            
            # Update performance stats
            await self._update_message_performance_stats(message)
            
        except Exception as e:
            logger.error(f"❌ Enhanced message handling failed: {e}")
    
    async def _handle_generic_enhanced_message(self, message: AdvancedMessage):
        """📋 Handle generic enhanced messages"""
        if message.message_type == MessageType.COMMAND:
            await self._handle_enhanced_command(message)
        elif message.message_type == MessageType.EVENT:
            await self._handle_enhanced_event(message)
        elif message.message_type == MessageType.NOTIFICATION:
            await self._handle_enhanced_notification(message)
        else:
            logger.debug(f"📋 Generic handling for {message.message_type.value} message")
    
    async def _handle_enhanced_command(self, message: AdvancedMessage):
        """⚡ Handle command messages"""
        self.message_stats['commands_processed'] += 1
        
        # Override in subclasses for specific command handling
        logger.info(f"⚡ Command received: {message.event_name} from {message.sender_id}")
        
        # Send acknowledgment if required
        if message.requires_ack:
            await self._send_command_acknowledgment(message)
    
    async def _handle_enhanced_event(self, message: AdvancedMessage):
        """🎯 Handle event messages"""
        logger.debug(f"🎯 Event received: {message.event_name} on topic {message.topic}")
        
        # Override in subclasses for specific event handling
        pass
    
    async def _handle_enhanced_notification(self, message: AdvancedMessage):
        """📢 Handle notification messages"""
        logger.debug(f"📢 Notification: {message.event_name} from {message.sender_id}")
        
        # Override in subclasses for specific notification handling
        pass
    
    async def _send_command_acknowledgment(self, original_message: AdvancedMessage):
        """✅ Send command acknowledgment"""
        try:
            ack_message = AdvancedMessage(
                sender_id=self.agent_id,
                message_type=MessageType.NOTIFICATION,
                target_agents={original_message.sender_id},
                event_name="command_acknowledged",
                payload={
                    'original_message_id': original_message.message_id,
                    'acknowledged_at': datetime.now().isoformat(),
                    'status': 'received'
                }
            )
            
            await self.message_bus.publish(ack_message)
            
        except Exception as e:
            logger.error(f"❌ Command acknowledgment failed: {e}")
    
    # =================== EVENT HANDLERS ===================
    
    async def _handle_system_announcement(self, message: AdvancedMessage):
        """📻 Handle system announcements"""
        logger.info(f"📻 System announcement: {message.payload.get('message', 'No message')}")
        
        # Update agent state based on system announcements
        if 'maintenance_mode' in message.payload:
            await self._prepare_for_maintenance()
        elif 'shutdown_signal' in message.payload:
            await self._prepare_for_shutdown()
    
    async def _handle_coordination_request(self, message: AdvancedMessage):
        """🤝 Handle coordination requests"""
        logger.info(f"🤝 Coordination request from {message.sender_id}: {message.event_name}")
        
        # Override in subclasses for specific coordination behavior
        pass
    
    async def _handle_health_check(self, message: AdvancedMessage):
        """💚 Handle health check requests"""
        try:
            health_status = await self._get_health_status()
            
            await self.publish_event(
                event_name="health_status",
                topic="system_events",
                payload={
                    'agent_id': self.agent_id,
                    'health': health_status,
                    'timestamp': datetime.now().isoformat()
                }
            )
            
        except Exception as e:
            logger.error(f"❌ Health check response failed: {e}")
    
    async def _handle_performance_report(self, message: AdvancedMessage):
        """📊 Handle performance report requests"""
        try:
            performance_data = await self._get_performance_metrics()
            
            await self.publish_event(
                event_name="performance_metrics",
                topic="system_events",
                payload=performance_data
            )
            
        except Exception as e:
            logger.error(f"❌ Performance report failed: {e}")
    
    async def _handle_task_assignment(self, message: AdvancedMessage):
        """📋 Handle task assignments"""
        logger.info(f"📋 Task assigned: {message.payload.get('task_type', 'unknown')}")
        
        # Override in subclasses for specific task handling
        pass
    
    async def _handle_workflow_update(self, message: AdvancedMessage):
        """🔄 Handle workflow updates"""
        logger.info(f"🔄 Workflow update: {message.payload.get('workflow_status', 'unknown')}")
        
        # Override in subclasses for specific workflow handling
        pass
    
    # =================== ENHANCED MONITORING ===================
    
    async def _update_message_performance_stats(self, message: AdvancedMessage):
        """📊 Update message performance statistics"""
        try:
            # Calculate message processing time
            if message.delivered_at:
                processing_time = (datetime.now() - message.delivered_at).total_seconds()
                message.processing_times[f'agent_{self.agent_id}'] = processing_time
            
            # Update routing path
            message.add_routing_step(f"processed_by_{self.agent_id}")
            
        except Exception as e:
            logger.error(f"❌ Message stats update failed: {e}")
    
    async def _get_enhanced_performance_metrics(self) -> Dict[str, Any]:
        """📊 Get enhanced performance metrics"""
        base_metrics = await self._get_performance_metrics()
        
        enhanced_metrics = {
            **base_metrics,
            'message_stats': self.message_stats.copy(),
            'subscribed_topics': list(self.subscribed_topics),
            'message_bus_stats': self.message_bus.get_stats(),
            'enhanced_features': {
                'load_balancing': self.enable_load_balancing,
                'fault_tolerance': self.fault_tolerance_enabled,
                'event_handlers': len(self.event_handlers)
            }
        }
        
        return enhanced_metrics
    
    async def _prepare_for_maintenance(self):
        """🔧 Prepare for system maintenance"""
        logger.info(f"🔧 Agent {self.agent_id} preparing for maintenance mode")
        
        # Finish current tasks
        # Reduce processing intensity
        # Save critical state
        pass
    
    async def _prepare_for_shutdown(self):
        """🛑 Prepare for system shutdown"""
        logger.info(f"🛑 Agent {self.agent_id} preparing for shutdown")
        
        # Graceful termination
        await self.terminate()

# =================== ENHANCED AGENT FACTORY ===================

class EnhancedAgentFactory:
    """🏭 Factory for creating enhanced agents"""
    
    @staticmethod
    async def create_enhanced_agent(agent_class, agent_id: str, **kwargs) -> EnhancedAutonomousAgent:
        """🚀 Create and initialize enhanced agent"""
        
        # Create agent instance
        agent = agent_class(agent_id, **kwargs)
        
        # Ensure it inherits from EnhancedAutonomousAgent
        if not isinstance(agent, EnhancedAutonomousAgent):
            raise TypeError(f"Agent must inherit from EnhancedAutonomousAgent")
        
        # Initialize and spawn
        await agent.spawn()
        
        return agent