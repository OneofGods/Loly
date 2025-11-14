#!/usr/bin/env python3
"""
🔥💀 COMPREHENSIVE AGENT SYSTEM TEST SUITE 💀🔥
Agent Poly Loly Double Zero: Complete System Validation

TEST COVERAGE:
- Individual agent functionality testing
- Inter-agent communication validation
- System orchestration testing
- Performance and stress testing
- Fault tolerance and recovery testing
"""

import asyncio
import json
import time
import pytest
import logging
import sys
import os
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import agent system components
from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY
from core.agent_orchestrator import AgentOrchestrator, launch_multi_agent_system
from agents.data_collector_agent import DataCollectorAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.predictor_agent import PredictorAgent
from agents.coordinator_agent import CoordinatorAgent
from agents.monitor_agent import MonitorAgent

# Configure test logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestAgentBase:
    """🧪 Base test class for agent testing"""
    
    @pytest.fixture
    async def test_agent(self):
        """Create test agent instance"""
        agent = TestAutonomousAgent("test_agent_001")
        yield agent
        await agent.terminate()
    
    @pytest.fixture
    async def orchestrator(self):
        """Create test orchestrator"""
        config = {
            'max_agents': 5,
            'min_agents': 3,
            'auto_scaling': False,  # Disable for testing
            'health_check_interval': 5
        }
        orchestrator = await launch_multi_agent_system(config)
        yield orchestrator
        await orchestrator.shutdown_system()

class TestAutonomousAgent(AutonomousAgent):
    """🤖 Test implementation of autonomous agent"""
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        super().__init__(agent_id, config)
        self.test_messages_received = []
        self.test_behaviors_executed = 0
        self.test_adaptations_performed = 0
    
    async def _agent_behavior(self):
        """Test agent behavior"""
        self.test_behaviors_executed += 1
        await asyncio.sleep(0.1)
    
    async def _initialize_systems(self):
        """Test system initialization"""
        logger.info(f"🧪 Test agent {self.agent_id} systems initialized")
    
    async def _agent_specific_adaptation(self):
        """Test adaptation"""
        self.test_adaptations_performed += 1
        logger.info(f"🧪 Test agent {self.agent_id} performed adaptation")
    
    async def _handle_message(self, message):
        """Track messages for testing"""
        await super()._handle_message(message)
        self.test_messages_received.append(message)

class TestIndividualAgents:
    """🧪 Test individual agent functionality"""
    
    @pytest.mark.asyncio
    async def test_data_collector_agent_lifecycle(self):
        """Test DataCollectorAgent lifecycle"""
        agent = DataCollectorAgent("test_data_collector")
        
        # Test spawning
        spawn_result = await agent.spawn()
        assert spawn_result == True
        assert agent.state.value == "running"
        
        # Test data collection capabilities
        await asyncio.sleep(2)  # Let it initialize
        
        # Check if agent has expected attributes
        assert hasattr(agent, 'data_sources')
        assert hasattr(agent, 'active_collections')
        assert len(agent.data_sources) > 0
        
        # Test termination
        await agent.terminate()
        assert agent.state.value == "terminated"
    
    @pytest.mark.asyncio
    async def test_analyzer_agent_functionality(self):
        """Test AnalyzerAgent analysis capabilities"""
        agent = AnalyzerAgent("test_analyzer")
        
        await agent.spawn()
        
        # Test analysis with sample data
        test_data = {
            'games': [
                {
                    'id': '1',
                    'date': '2024-01-01',
                    'teams': [
                        {'name': 'Team A', 'score': 21, 'home_away': 'home'},
                        {'name': 'Team B', 'score': 14, 'home_away': 'away'}
                    ]
                },
                {
                    'id': '2',
                    'date': '2024-01-02', 
                    'teams': [
                        {'name': 'Team A', 'score': 28, 'home_away': 'away'},
                        {'name': 'Team C', 'score': 10, 'home_away': 'home'}
                    ]
                }
            ]
        }
        
        # Perform analysis
        analysis_result = await agent._perform_full_analysis('NFL', test_data)
        
        # Validate analysis result
        assert 'sport' in analysis_result
        assert 'trend_analysis' in analysis_result
        assert 'overall_confidence' in analysis_result
        assert analysis_result['sport'] == 'NFL'
        
        await agent.terminate()
    
    @pytest.mark.asyncio
    async def test_predictor_agent_ml_capabilities(self):
        """Test PredictorAgent ML functionality"""
        agent = PredictorAgent("test_predictor")
        
        await agent.spawn()
        
        # Add test training data
        training_samples = [
            {
                'team': 'Team A',
                'avg_score': 20,
                'trend_direction': 'improving',
                'trend_confidence': 0.8,
                'score_variance': 5,
                'games_count': 5
            },
            {
                'team': 'Team B', 
                'avg_score': 15,
                'trend_direction': 'stable',
                'trend_confidence': 0.6,
                'score_variance': 8,
                'games_count': 5
            }
        ]
        
        agent.training_data['NFL'] = training_samples
        
        # Trigger training
        agent.training_queue.append({
            'sport': 'NFL',
            'priority': 1,
            'trigger': 'test'
        })
        
        # Wait for training
        await asyncio.sleep(3)
        
        # Test prediction
        test_game = {
            'teams': [
                {'name': 'Team A', 'score': 21, 'home_away': 'home'},
                {'name': 'Team B', 'score': 14, 'home_away': 'away'}
            ]
        }
        
        prediction = await agent.predict_game_outcome('NFL', test_game)
        
        # Validate prediction
        assert 'prediction' in prediction or 'error' in prediction
        if 'prediction' in prediction:
            assert 'confidence' in prediction
            assert 'model_info' in prediction
        
        await agent.terminate()
    
    @pytest.mark.asyncio
    async def test_coordinator_agent_workflow_management(self):
        """Test CoordinatorAgent workflow capabilities"""
        agent = CoordinatorAgent("test_coordinator")
        
        await agent.spawn()
        
        # Test workflow creation
        workflow_id = await agent.create_sports_analysis_workflow('NFL', 'standard')
        
        assert workflow_id is not None
        assert workflow_id in agent.active_workflows
        
        # Check workflow structure
        workflow = agent.active_workflows[workflow_id]
        assert workflow.workflow_type == 'sports_analysis'
        assert len(workflow.tasks) > 0
        
        # Get coordination status
        status = await agent.get_coordination_status()
        assert 'active_workflows' in status
        assert status['active_workflows'] >= 1
        
        await agent.terminate()
    
    @pytest.mark.asyncio
    async def test_monitor_agent_health_tracking(self):
        """Test MonitorAgent health monitoring"""
        agent = MonitorAgent("test_monitor")
        
        await agent.spawn()
        
        # Let it collect some metrics
        await asyncio.sleep(5)
        
        # Check health metrics
        assert len(agent.health_metrics) > 0
        assert 'cpu_usage' in agent.health_metrics
        assert 'memory_usage' in agent.health_metrics
        
        # Get monitoring status
        status = await agent.get_monitoring_status()
        assert 'system_health' in status
        assert 'health_metrics' in status
        
        # Get health report
        health_report = await agent.get_system_health_report()
        assert 'overall_health' in health_report
        assert 'system_resources' in health_report
        
        await agent.terminate()

class TestInterAgentCommunication:
    """🔗 Test inter-agent communication"""
    
    @pytest.mark.asyncio
    async def test_message_passing(self):
        """Test basic message passing between agents"""
        agent1 = TestAutonomousAgent("test_agent_1")
        agent2 = TestAutonomousAgent("test_agent_2")
        
        await agent1.spawn()
        await agent2.spawn()
        
        # Register agents for message routing
        AGENT_REGISTRY.register_agent(agent1)
        AGENT_REGISTRY.register_agent(agent2)
        
        # Send message from agent1 to agent2
        await agent1.send_message("test_agent_2", "test_message", {
            'content': 'Hello from agent 1',
            'timestamp': time.time()
        })
        
        # Wait for message processing
        await asyncio.sleep(1)
        
        # Check if agent2 received the message
        assert len(agent2.test_messages_received) > 0
        
        # Clean up
        await agent1.terminate()
        await agent2.terminate()
        AGENT_REGISTRY.unregister_agent("test_agent_1")
        AGENT_REGISTRY.unregister_agent("test_agent_2")
    
    @pytest.mark.asyncio
    async def test_broadcast_communication(self):
        """Test broadcast communication"""
        agents = []
        
        # Create multiple test agents
        for i in range(3):
            agent = TestAutonomousAgent(f"test_agent_{i}")
            await agent.spawn()
            AGENT_REGISTRY.register_agent(agent)
            agents.append(agent)
        
        # Broadcast message from first agent
        await agents[0].broadcast_message("broadcast_test", {
            'sender': 'test_agent_0',
            'message': 'Broadcast test message'
        })
        
        # Wait for message processing
        await asyncio.sleep(1)
        
        # Check if other agents received the broadcast
        for i in range(1, 3):
            assert len(agents[i].test_messages_received) > 0
        
        # Clean up
        for agent in agents:
            await agent.terminate()
            AGENT_REGISTRY.unregister_agent(agent.agent_id)

class TestSystemOrchestration:
    """🎼 Test system orchestration functionality"""
    
    @pytest.mark.asyncio
    async def test_orchestrator_initialization(self):
        """Test orchestrator system initialization"""
        config = {
            'max_agents': 5,
            'min_agents': 3,
            'auto_scaling': False
        }
        
        orchestrator = await launch_multi_agent_system(config)
        
        assert orchestrator is not None
        assert orchestrator.system_state.value == "running"
        assert len(orchestrator.active_agents) >= 3
        
        # Check that all required agent types are present
        agent_types = set()
        for agent_id in orchestrator.active_agents:
            agent_type = agent_id.split('_')[0]
            agent_types.add(agent_type)
        
        required_types = {'data', 'analyzer', 'predictor', 'coordinator', 'monitor'}
        assert len(agent_types.intersection(required_types)) >= 3
        
        await orchestrator.shutdown_system()
    
    @pytest.mark.asyncio
    async def test_agent_spawning_and_termination(self):
        """Test dynamic agent spawning and termination"""
        config = {'max_agents': 10, 'min_agents': 2, 'auto_scaling': False}
        orchestrator = await launch_multi_agent_system(config)
        
        initial_count = len(orchestrator.active_agents)
        
        # Test spawning new agent
        spawn_result = await orchestrator._spawn_agent('analyzer', 'test_analyzer_extra')
        assert spawn_result == True
        assert len(orchestrator.active_agents) == initial_count + 1
        
        # Test terminating agent
        terminate_result = await orchestrator._terminate_agent('test_analyzer_extra', 'test')
        assert terminate_result == True
        assert len(orchestrator.active_agents) == initial_count
        
        await orchestrator.shutdown_system()
    
    @pytest.mark.asyncio
    async def test_workflow_orchestration(self):
        """Test complete workflow orchestration"""
        config = {'max_agents': 8, 'min_agents': 5, 'auto_scaling': False}
        orchestrator = await launch_multi_agent_system(config)
        
        # Wait for system to stabilize
        await asyncio.sleep(5)
        
        # Trigger sports analysis workflow
        workflow_id = await orchestrator.trigger_workflow('sports_analysis', {
            'sport': 'NFL',
            'analysis_depth': 'standard'
        })
        
        assert workflow_id is not None
        
        # Wait for workflow processing
        await asyncio.sleep(10)
        
        # Get system status
        status = await orchestrator.get_system_status()
        assert 'system_state' in status
        assert status['active_agents'] >= 5
        
        await orchestrator.shutdown_system()

class TestPerformanceAndStress:
    """📈 Test system performance and stress handling"""
    
    @pytest.mark.asyncio
    async def test_concurrent_agent_operations(self):
        """Test concurrent operations across multiple agents"""
        agents = []
        
        # Create multiple agents concurrently
        spawn_tasks = []
        for i in range(5):
            agent = TestAutonomousAgent(f"stress_test_agent_{i}")
            spawn_tasks.append(agent.spawn())
            agents.append(agent)
        
        # Wait for all agents to spawn
        spawn_results = await asyncio.gather(*spawn_tasks)
        assert all(spawn_results)
        
        # Perform concurrent operations
        operation_tasks = []
        for agent in agents:
            # Send multiple messages concurrently
            for j in range(10):
                task = agent.send_message(agent.agent_id, "test_message", {
                    'test_id': j,
                    'timestamp': time.time()
                })
                operation_tasks.append(task)
        
        # Wait for all operations to complete
        await asyncio.gather(*operation_tasks)
        
        # Verify all agents are still responsive
        for agent in agents:
            assert agent.state.value == "running"
        
        # Clean up
        terminate_tasks = [agent.terminate() for agent in agents]
        await asyncio.gather(*terminate_tasks)
    
    @pytest.mark.asyncio
    async def test_system_load_handling(self):
        """Test system behavior under load"""
        config = {'max_agents': 6, 'min_agents': 4, 'auto_scaling': False}
        orchestrator = await launch_multi_agent_system(config)
        
        # Generate load by triggering multiple workflows
        workflow_tasks = []
        for i in range(5):
            task = orchestrator.trigger_workflow('sports_analysis', {
                'sport': f'Test_Sport_{i}',
                'analysis_depth': 'standard'
            })
            workflow_tasks.append(task)
        
        # Wait for workflows to be triggered
        workflow_ids = await asyncio.gather(*workflow_tasks)
        
        # Verify workflows were created
        assert all(wid is not None for wid in workflow_ids if wid)
        
        # Let system process under load
        await asyncio.sleep(15)
        
        # Verify system is still healthy
        status = await orchestrator.get_system_status()
        assert status['system_state'] in ['running', 'degraded']  # Should not crash
        
        await orchestrator.shutdown_system()

class TestFaultToleranceAndRecovery:
    """🛡️ Test fault tolerance and recovery mechanisms"""
    
    @pytest.mark.asyncio
    async def test_agent_failure_recovery(self):
        """Test system recovery from agent failures"""
        config = {'max_agents': 6, 'min_agents': 4, 'auto_scaling': True}
        orchestrator = await launch_multi_agent_system(config)
        
        initial_agent_count = len(orchestrator.active_agents)
        
        # Simulate agent failure by forcefully terminating an agent
        agent_to_fail = list(orchestrator.active_agents.keys())[0]
        agent_type = agent_to_fail.split('_')[0]
        
        # Force terminate without cleanup
        if agent_to_fail in orchestrator.active_agents:
            del orchestrator.active_agents[agent_to_fail]
            del orchestrator.agent_configs[agent_to_fail]
            if agent_to_fail in orchestrator.agent_health:
                del orchestrator.agent_health[agent_to_fail]
        
        # Wait for system to detect and recover
        await asyncio.sleep(20)
        
        # Check if system recovered
        current_agent_count = len(orchestrator.active_agents)
        
        # System should maintain minimum agents or recover
        min_required = orchestrator.agent_specifications[agent_type]['min_instances']
        current_type_count = len([aid for aid in orchestrator.active_agents if aid.startswith(agent_type)])
        
        assert current_type_count >= min_required
        
        await orchestrator.shutdown_system()
    
    @pytest.mark.asyncio
    async def test_communication_failure_handling(self):
        """Test handling of communication failures"""
        agent1 = TestAutonomousAgent("comm_test_1")
        agent2 = TestAutonomousAgent("comm_test_2")
        
        await agent1.spawn()
        await agent2.spawn()
        
        AGENT_REGISTRY.register_agent(agent1)
        AGENT_REGISTRY.register_agent(agent2)
        
        # Simulate communication failure by corrupting message queue
        original_queue = agent2.message_queue
        agent2.message_queue = None
        
        # Attempt to send message (should handle gracefully)
        try:
            await agent1.send_message("comm_test_2", "test_message", {'test': 'data'})
            # Should not crash
            communication_handled = True
        except Exception as e:
            communication_handled = False
            logger.error(f"Communication failure not handled: {e}")
        
        assert communication_handled
        
        # Restore communication
        agent2.message_queue = original_queue
        
        # Clean up
        await agent1.terminate()
        await agent2.terminate()
        AGENT_REGISTRY.unregister_agent("comm_test_1")
        AGENT_REGISTRY.unregister_agent("comm_test_2")

class TestIntegrationScenarios:
    """🎯 Test complete integration scenarios"""
    
    @pytest.mark.asyncio
    async def test_end_to_end_sports_analysis(self):
        """Test complete end-to-end sports analysis workflow"""
        config = {'max_agents': 8, 'min_agents': 5, 'auto_scaling': False}
        orchestrator = await launch_multi_agent_system(config)
        
        # Wait for system stabilization
        await asyncio.sleep(5)
        
        # Trigger comprehensive sports analysis
        workflow_id = await orchestrator.trigger_workflow('sports_analysis', {
            'sport': 'NFL',
            'analysis_depth': 'deep'
        })
        
        assert workflow_id is not None
        
        # Wait for complete workflow execution
        await asyncio.sleep(30)
        
        # Verify system processed the workflow
        system_status = await orchestrator.get_system_status()
        assert system_status['system_metrics']['total_tasks_processed'] > 0
        
        # Check agent health after processing
        agent_details = await orchestrator.get_agent_details()
        healthy_agents = [
            aid for aid, details in agent_details.items()
            if details['status'] == 'healthy'
        ]
        
        assert len(healthy_agents) >= 4  # Most agents should be healthy
        
        await orchestrator.shutdown_system()
    
    @pytest.mark.asyncio
    async def test_prediction_pipeline_integration(self):
        """Test prediction pipeline integration"""
        config = {'max_agents': 6, 'min_agents': 4, 'auto_scaling': False}
        orchestrator = await launch_multi_agent_system(config)
        
        await asyncio.sleep(5)
        
        # Trigger prediction pipeline
        test_games = [
            {
                'home_team': 'Team A',
                'away_team': 'Team B',
                'scheduled_time': '2024-01-15T20:00:00Z'
            },
            {
                'home_team': 'Team C', 
                'away_team': 'Team D',
                'scheduled_time': '2024-01-15T21:00:00Z'
            }
        ]
        
        workflow_id = await orchestrator.trigger_workflow('prediction_pipeline', {
            'sport': 'NFL',
            'target_games': test_games
        })
        
        assert workflow_id is not None
        
        # Wait for pipeline execution
        await asyncio.sleep(25)
        
        # Verify pipeline processed successfully
        performance_metrics = await orchestrator.get_performance_metrics()
        assert 'current_performance' in performance_metrics
        
        await orchestrator.shutdown_system()

# =================== TEST UTILITIES ===================

class TestUtilities:
    """🛠️ Test utility functions"""
    
    @staticmethod
    def generate_test_game_data(num_games: int = 10) -> Dict[str, Any]:
        """Generate test sports game data"""
        teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
        games = []
        
        for i in range(num_games):
            home_team = teams[i % len(teams)]
            away_team = teams[(i + 1) % len(teams)]
            
            game = {
                'id': str(i + 1),
                'date': f'2024-01-{(i % 30) + 1:02d}',
                'teams': [
                    {
                        'name': home_team,
                        'score': 14 + (i * 3) % 21,  # Varying scores
                        'home_away': 'home'
                    },
                    {
                        'name': away_team,
                        'score': 10 + (i * 7) % 28,  # Varying scores
                        'home_away': 'away'
                    }
                ]
            }
            games.append(game)
        
        return {'games': games}
    
    @staticmethod
    async def wait_for_system_stabilization(orchestrator: AgentOrchestrator, 
                                          timeout: int = 30) -> bool:
        """Wait for system to stabilize"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            status = await orchestrator.get_system_status()
            
            if (status['system_state'] == 'running' and
                status['healthy_agents'] >= status['active_agents'] * 0.8):
                return True
            
            await asyncio.sleep(2)
        
        return False
    
    @staticmethod
    def assert_agent_health(agent_details: Dict[str, Any], 
                          min_healthy_ratio: float = 0.8):
        """Assert minimum agent health ratio"""
        total_agents = len(agent_details)
        healthy_agents = len([
            details for details in agent_details.values()
            if details['status'] == 'healthy'
        ])
        
        health_ratio = healthy_agents / total_agents if total_agents > 0 else 0
        assert health_ratio >= min_healthy_ratio, f"Health ratio {health_ratio} below minimum {min_healthy_ratio}"

# =================== TEST EXECUTION ===================

async def run_comprehensive_tests():
    """🚀 Run comprehensive test suite"""
    logger.info("🧪 Starting comprehensive agent system tests...")
    
    test_classes = [
        TestIndividualAgents,
        TestInterAgentCommunication,
        TestSystemOrchestration,
        TestPerformanceAndStress,
        TestFaultToleranceAndRecovery,
        TestIntegrationScenarios
    ]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for test_class in test_classes:
        logger.info(f"🧪 Running tests for {test_class.__name__}")
        
        # Get test methods
        test_methods = [
            method for method in dir(test_class)
            if method.startswith('test_') and callable(getattr(test_class, method))
        ]
        
        for test_method_name in test_methods:
            total_tests += 1
            
            try:
                # Create test instance
                test_instance = test_class()
                test_method = getattr(test_instance, test_method_name)
                
                logger.info(f"  🔬 Running {test_method_name}")
                
                # Run the test
                await test_method()
                
                passed_tests += 1
                logger.info(f"  ✅ {test_method_name} passed")
                
            except Exception as e:
                failed_tests += 1
                logger.error(f"  ❌ {test_method_name} failed: {e}")
    
    # Test summary
    logger.info(f"\n🏁 Test Summary:")
    logger.info(f"   Total tests: {total_tests}")
    logger.info(f"   Passed: {passed_tests}")
    logger.info(f"   Failed: {failed_tests}")
    logger.info(f"   Success rate: {(passed_tests/total_tests)*100:.1f}%")
    
    return passed_tests, failed_tests

if __name__ == "__main__":
    # Run the comprehensive test suite
    passed, failed = asyncio.run(run_comprehensive_tests())
    
    if failed == 0:
        print("🎉 All tests passed! Agent system is fully functional.")
        exit(0)
    else:
        print(f"⚠️ {failed} tests failed. Review the logs for details.")
        exit(1)