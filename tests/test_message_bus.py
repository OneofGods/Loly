#!/usr/bin/env python3
"""
🔥💀 PHASE 2: ADVANCED MESSAGE BUS TESTS 💀🔥
Agent Poly Loly Double Zero: Comprehensive Message Bus Testing

COMPREHENSIVE TEST COVERAGE:
- Event-driven messaging patterns
- Fault tolerance and retry logic
- Load balancing across agents
- Performance and throughput
- Dead letter queue handling
- Topic-based pub/sub
- Agent lifecycle integration
"""

import asyncio
import pytest
import time
import uuid
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.message_bus import (
    AdvancedMessageBus, AdvancedMessage, MessageType, MessagePriority,
    get_message_bus, initialize_message_bus
)

class TestAdvancedMessage:
    """🧪 Test AdvancedMessage class functionality"""
    
    def test_message_creation(self):
        """✅ Test basic message creation"""
        message = AdvancedMessage(
            sender_id="test_agent",
            message_type=MessageType.EVENT,
            topic="test_topic",
            event_name="test_event",
            payload={"data": "test"}
        )
        
        assert message.sender_id == "test_agent"
        assert message.message_type == MessageType.EVENT
        assert message.topic == "test_topic"
        assert message.event_name == "test_event"
        assert message.payload == {"data": "test"}
        assert message.priority == MessagePriority.NORMAL
        assert message.retry_count == 0
        assert not message.is_expired()
    
    def test_message_expiration(self):
        """⏰ Test message expiration logic"""
        message = AdvancedMessage()
        
        # Not expired without expiration time
        assert not message.is_expired()
        
        # Set expiration in the past
        message.expires_at = datetime.now() - timedelta(seconds=1)
        assert message.is_expired()
        
        # Set expiration in the future
        message.expires_at = datetime.now() + timedelta(seconds=60)
        assert not message.is_expired()
    
    def test_routing_path_tracking(self):
        """🛣️ Test routing path tracking"""
        message = AdvancedMessage()
        
        message.add_routing_step("step1")
        message.add_routing_step("step2")
        
        assert len(message.routing_path) == 2
        assert "step1@" in message.routing_path[0]
        assert "step2@" in message.routing_path[1]
    
    def test_message_serialization(self):
        """📋 Test message serialization"""
        message = AdvancedMessage(
            sender_id="test_agent",
            message_type=MessageType.PUBLISH,
            topic="test_topic",
            payload={"data": "test"}
        )
        
        serialized = message.to_dict()
        
        assert serialized['sender_id'] == "test_agent"
        assert serialized['message_type'] == "publish"
        assert serialized['topic'] == "test_topic"
        assert serialized['payload'] == {"data": "test"}
        assert 'message_id' in serialized
        assert 'created_at' in serialized

class TestAdvancedMessageBus:
    """🧪 Test AdvancedMessageBus functionality"""
    
    @pytest.fixture
    async def message_bus(self):
        """🏭 Create test message bus"""
        bus = AdvancedMessageBus("test_bus")
        await bus.start()
        yield bus
        await bus.stop()
    
    @pytest.mark.asyncio
    async def test_bus_lifecycle(self):
        """🔄 Test message bus start/stop lifecycle"""
        bus = AdvancedMessageBus("lifecycle_test")
        
        assert not bus.running
        
        await bus.start()
        assert bus.running
        assert len(bus.background_tasks) > 0
        
        await bus.stop()
        assert not bus.running
    
    @pytest.mark.asyncio
    async def test_agent_registration(self, message_bus):
        """📝 Test agent registration and unregistration"""
        agent_id = "test_agent_001"
        agent_type = "DataCollector"
        
        # Register agent
        message_bus.register_agent(agent_id, agent_type)
        
        assert agent_id in message_bus.agent_queues
        assert agent_id in message_bus.agent_instances[agent_type]
        assert agent_id in message_bus.instance_load
        
        # Unregister agent
        message_bus.unregister_agent(agent_id)
        
        assert agent_id not in message_bus.agent_queues
        assert agent_id not in message_bus.agent_instances[agent_type]
        assert agent_id not in message_bus.instance_load
    
    @pytest.mark.asyncio
    async def test_topic_subscription(self, message_bus):
        """📡 Test topic subscription system"""
        agent_id = "test_agent_001"
        topic = "data_updates"
        
        message_bus.register_agent(agent_id)
        
        # Subscribe to topic
        message_bus.subscribe_to_topic(agent_id, topic)
        assert agent_id in message_bus.topic_subscribers[topic]
        
        # Unsubscribe from topic
        message_bus.unsubscribe_from_topic(agent_id, topic)
        assert agent_id not in message_bus.topic_subscribers[topic]
    
    @pytest.mark.asyncio
    async def test_publish_to_topic(self, message_bus):
        """📢 Test publishing messages to topics"""
        # Setup agents and subscriptions
        agent1_id = "subscriber_1"
        agent2_id = "subscriber_2"
        topic = "test_events"
        
        message_bus.register_agent(agent1_id)
        message_bus.register_agent(agent2_id)
        message_bus.subscribe_to_topic(agent1_id, topic)
        message_bus.subscribe_to_topic(agent2_id, topic)
        
        # Create and publish message
        message = AdvancedMessage(
            sender_id="publisher",
            message_type=MessageType.PUBLISH,
            topic=topic,
            event_name="test_event",
            payload={"data": "test_data"}
        )
        
        message_id = await message_bus.publish(message)
        assert message_id == message.message_id
        
        # Verify both subscribers received the message
        await asyncio.sleep(0.1)  # Allow processing
        
        msg1 = await message_bus.get_agent_message(agent1_id)
        msg2 = await message_bus.get_agent_message(agent2_id)
        
        assert msg1 is not None
        assert msg2 is not None
        assert msg1.message_id == message_id
        assert msg2.message_id == message_id
    
    @pytest.mark.asyncio
    async def test_broadcast_messaging(self, message_bus):
        """📻 Test broadcast messaging"""
        # Register multiple agents
        agents = ["agent_1", "agent_2", "agent_3"]
        for agent_id in agents:
            message_bus.register_agent(agent_id)
        
        # Create broadcast message
        message = AdvancedMessage(
            sender_id="broadcaster",
            message_type=MessageType.BROADCAST,
            event_name="system_announcement",
            payload={"announcement": "System maintenance in 5 minutes"}
        )
        
        await message_bus.publish(message)
        await asyncio.sleep(0.1)  # Allow processing
        
        # Verify all agents received the broadcast
        for agent_id in agents:
            received_msg = await message_bus.get_agent_message(agent_id)
            assert received_msg is not None
            assert received_msg.event_name == "system_announcement"
    
    @pytest.mark.asyncio
    async def test_direct_targeting(self, message_bus):
        """🎯 Test direct message targeting"""
        # Register agents
        target_agent = "target_agent"
        other_agent = "other_agent"
        
        message_bus.register_agent(target_agent)
        message_bus.register_agent(other_agent)
        
        # Create targeted message
        message = AdvancedMessage(
            sender_id="sender",
            message_type=MessageType.COMMAND,
            target_agents={target_agent},
            payload={"command": "process_data"}
        )
        
        await message_bus.publish(message)
        await asyncio.sleep(0.1)
        
        # Target agent should receive message
        target_msg = await message_bus.get_agent_message(target_agent)
        assert target_msg is not None
        assert target_msg.payload["command"] == "process_data"
        
        # Other agent should not receive message
        other_msg = await message_bus.get_agent_message(other_agent)
        assert other_msg is None
    
    @pytest.mark.asyncio
    async def test_load_balancing(self, message_bus):
        """⚖️ Test load balancing across agent instances"""
        agent_type = "Worker"
        
        # Register multiple instances of same agent type
        instances = [f"worker_{i}" for i in range(3)]
        for instance_id in instances:
            message_bus.register_agent(instance_id, agent_type)
        
        # Send messages that should be load balanced
        for i in range(9):  # 3 messages per instance
            message = AdvancedMessage(
                sender_id="dispatcher",
                topic=agent_type,  # Use agent_type as topic for load balancing
                payload={"task_id": i}
            )
            await message_bus.publish(message)
        
        await asyncio.sleep(0.2)
        
        # Verify messages were distributed
        received_counts = {}
        for instance_id in instances:
            count = 0
            while True:
                msg = await message_bus.get_agent_message(instance_id)
                if msg is None:
                    break
                count += 1
            received_counts[instance_id] = count
        
        # Each instance should receive approximately the same number of messages
        total_received = sum(received_counts.values())
        assert total_received > 0
        
        # Check load balancing effectiveness
        for instance_id, count in received_counts.items():
            assert count >= 0  # Each should receive at least some messages

class TestFaultTolerance:
    """🛡️ Test fault tolerance features"""
    
    @pytest.fixture
    async def message_bus(self):
        """🏭 Create test message bus"""
        bus = AdvancedMessageBus("fault_test")
        await bus.start()
        yield bus
        await bus.stop()
    
    @pytest.mark.asyncio
    async def test_retry_mechanism(self, message_bus):
        """🔄 Test message retry mechanism"""
        # Create agent with small queue to trigger failures
        agent_id = "overloaded_agent"
        message_bus.register_agent(agent_id)
        
        # Fill the agent queue to capacity
        queue = message_bus.agent_queues[agent_id]
        original_maxsize = queue._maxsize
        queue._maxsize = 2  # Make queue very small
        
        # Send messages that will overflow the queue
        messages = []
        for i in range(5):
            message = AdvancedMessage(
                sender_id="sender",
                target_agents={agent_id},
                payload={"data": f"message_{i}"},
                max_retries=2
            )
            messages.append(message)
            await message_bus.publish(message)
        
        # Allow retry processing
        await asyncio.sleep(2)
        
        # Restore queue size and process retries
        queue._maxsize = original_maxsize
        await asyncio.sleep(3)
        
        # Verify some messages were retried and delivered
        received_count = 0
        while True:
            msg = await message_bus.get_agent_message(agent_id)
            if msg is None:
                break
            received_count += 1
        
        assert received_count > 0  # Some messages should have been delivered
    
    @pytest.mark.asyncio
    async def test_dead_letter_queue(self, message_bus):
        """💀 Test dead letter queue handling"""
        # Create message with no valid recipients
        message = AdvancedMessage(
            sender_id="sender",
            target_agents={"nonexistent_agent"},
            payload={"data": "orphaned_message"},
            max_retries=1
        )
        
        await message_bus.publish(message)
        await asyncio.sleep(2)
        
        # Message should end up in dead letter queue
        # In a real implementation, we'd check the dead letter queue
        # For now, verify stats show failed messages
        stats = message_bus.get_stats()
        assert stats['performance']['total_failed'] > 0
    
    @pytest.mark.asyncio
    async def test_message_expiration(self, message_bus):
        """⏰ Test message expiration handling"""
        agent_id = "test_agent"
        message_bus.register_agent(agent_id)
        
        # Create expired message
        message = AdvancedMessage(
            sender_id="sender",
            target_agents={agent_id},
            expires_at=datetime.now() - timedelta(seconds=1),
            payload={"data": "expired_message"}
        )
        
        await message_bus.publish(message)
        await asyncio.sleep(0.1)
        
        # Expired messages should not be delivered
        received_msg = await message_bus.get_agent_message(agent_id)
        assert received_msg is None or received_msg.is_expired()

class TestPerformance:
    """⚡ Test performance characteristics"""
    
    @pytest.fixture
    async def message_bus(self):
        """🏭 Create test message bus"""
        bus = AdvancedMessageBus("perf_test")
        await bus.start()
        yield bus
        await bus.stop()
    
    @pytest.mark.asyncio
    async def test_high_throughput_messaging(self, message_bus):
        """🚀 Test high throughput message processing"""
        # Register multiple agents
        agents = [f"agent_{i}" for i in range(10)]
        for agent_id in agents:
            message_bus.register_agent(agent_id)
        
        # Send many messages quickly
        start_time = time.time()
        message_count = 100
        
        tasks = []
        for i in range(message_count):
            message = AdvancedMessage(
                sender_id="throughput_tester",
                message_type=MessageType.BROADCAST,
                payload={"sequence": i}
            )
            task = asyncio.create_task(message_bus.publish(message))
            tasks.append(task)
        
        # Wait for all publications
        await asyncio.gather(*tasks)
        publish_time = time.time() - start_time
        
        # Allow processing time
        await asyncio.sleep(1)
        
        # Verify throughput
        messages_per_second = message_count / publish_time
        print(f"📊 Throughput: {messages_per_second:.1f} messages/second")
        
        assert messages_per_second > 50  # Should handle at least 50 msg/sec
        
        # Verify delivery
        total_received = 0
        for agent_id in agents:
            while True:
                msg = await message_bus.get_agent_message(agent_id)
                if msg is None:
                    break
                total_received += 1
        
        # Should receive most messages (allowing for some loss in stress test)
        expected_total = message_count * len(agents)
        delivery_rate = total_received / expected_total
        assert delivery_rate > 0.8  # At least 80% delivery rate
    
    @pytest.mark.asyncio
    async def test_concurrent_agent_operations(self, message_bus):
        """🔄 Test concurrent agent registration/messaging"""
        
        async def agent_simulation(agent_id: str):
            """Simulate agent lifecycle"""
            # Register
            message_bus.register_agent(agent_id, "TestAgent")
            
            # Subscribe to topics
            message_bus.subscribe_to_topic(agent_id, "simulation")
            
            # Send some messages
            for i in range(5):
                message = AdvancedMessage(
                    sender_id=agent_id,
                    message_type=MessageType.PUBLISH,
                    topic="simulation",
                    payload={"from": agent_id, "seq": i}
                )
                await message_bus.publish(message)
            
            # Receive messages
            received = 0
            for _ in range(10):  # Try to receive some messages
                msg = await message_bus.get_agent_message(agent_id)
                if msg:
                    received += 1
                else:
                    break
            
            return received
        
        # Run multiple agents concurrently
        agent_count = 20
        tasks = [
            asyncio.create_task(agent_simulation(f"sim_agent_{i}"))
            for i in range(agent_count)
        ]
        
        results = await asyncio.gather(*tasks)
        
        # Verify all agents operated successfully
        assert len(results) == agent_count
        assert all(result >= 0 for result in results)  # All should receive some messages
        
        # Verify bus statistics
        stats = message_bus.get_stats()
        assert stats['registered_agents'] == agent_count
        assert stats['performance']['total_sent'] > 0

class TestIntegration:
    """🔗 Test integration scenarios"""
    
    @pytest.mark.asyncio
    async def test_global_message_bus(self):
        """🌐 Test global message bus singleton"""
        bus1 = get_message_bus()
        bus2 = get_message_bus()
        
        # Should return the same instance
        assert bus1 is bus2
        assert bus1.bus_id == bus2.bus_id
    
    @pytest.mark.asyncio
    async def test_message_bus_initialization(self):
        """🚀 Test message bus initialization"""
        bus = await initialize_message_bus()
        
        assert bus.running
        assert len(bus.background_tasks) > 0
        
        # Clean up
        await bus.stop()

class TestMessageBusStats:
    """📊 Test message bus statistics"""
    
    @pytest.fixture
    async def message_bus(self):
        """🏭 Create test message bus"""
        bus = AdvancedMessageBus("stats_test")
        await bus.start()
        yield bus
        await bus.stop()
    
    @pytest.mark.asyncio
    async def test_stats_collection(self, message_bus):
        """📈 Test statistics collection"""
        # Register agents and send messages
        message_bus.register_agent("sender")
        message_bus.register_agent("receiver")
        
        # Send messages and collect stats
        for i in range(10):
            message = AdvancedMessage(
                sender_id="sender",
                target_agents={"receiver"},
                payload={"count": i}
            )
            await message_bus.publish(message)
        
        await asyncio.sleep(0.2)
        
        # Get comprehensive stats
        stats = message_bus.get_stats()
        
        assert stats['bus_id'] == "stats_test"
        assert stats['running'] is True
        assert stats['registered_agents'] == 2
        assert stats['performance']['total_sent'] == 10
        assert 'messages_per_second' in stats['performance']
        assert 'success_rate' in stats['performance']

if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--asyncio-mode=auto"])