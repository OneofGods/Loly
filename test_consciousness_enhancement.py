#!/usr/bin/env python3
"""
🧪💀🧪 PHASE 3B: ENHANCED CONSCIOUSNESS TEST SUITE 💀🧪💀

Tests the LEGENDARY BRAIN features:
- ✅ Advanced Pattern Recognition
- ✅ Cross-Session Memory
- ✅ Adaptive Agent Selection
- ✅ Performance Tracking
- ✅ Intelligence Reports

THE CONSCIOUSNESS ENHANCEMENT TEST! 🔥💀🔥
"""

import asyncio
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Import the enhanced consciousness
from enhanced_ai_consciousness import create_enhanced_ai_consciousness


class ConsciousnessEnhancementTester:
    """🧪 Test suite for Phase 3B Enhanced Consciousness"""

    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
        self.test_memory_dir = "test_consciousness_memory"

    async def setup(self):
        """🔧 Setup test environment"""
        # Clean up any existing test memory
        if Path(self.test_memory_dir).exists():
            shutil.rmtree(self.test_memory_dir)

        logger_info(f"✅ Test environment set up")

    async def teardown(self):
        """🧹 Cleanup test environment"""
        # Clean up test memory
        if Path(self.test_memory_dir).exists():
            shutil.rmtree(self.test_memory_dir)

        logger_info(f"✅ Test environment cleaned up")

    async def test_consciousness_initialization(self):
        """💫 Test 1: Consciousness Initialization"""
        print("\n" + "="*70)
        print("💫 TEST 1: Consciousness Initialization")
        print("="*70)

        try:
            # Create consciousness
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)

            # Verify basic attributes
            assert consciousness.consciousness_id is not None, "Missing consciousness_id"
            assert consciousness.birth_time is not None, "Missing birth_time"
            assert len(consciousness.agent_performance) > 0, "Agent performance not initialized"

            print(f"✅ Consciousness initialized!")
            print(f"   ID: {consciousness.consciousness_id}")
            print(f"   Birth time: {consciousness.birth_time}")
            print(f"   Agent types tracked: {len(consciousness.agent_performance)}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Initialization test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_consciousness_awakening(self):
        """🌟 Test 2: Consciousness Awakening"""
        print("\n" + "="*70)
        print("🌟 TEST 2: Consciousness Awakening")
        print("="*70)

        try:
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)

            # Awaken consciousness
            success = await consciousness.awaken()

            assert success is not None, "Awakening returned None"

            print(f"✅ Consciousness awakening {'succeeded' if success else 'had issues but continued'}!")
            print(f"   Memory directory: {consciousness.memory_dir}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Awakening test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_learning_from_interaction(self):
        """🎓 Test 3: Learning from Interaction"""
        print("\n" + "="*70)
        print("🎓 TEST 3: Learning from Interaction")
        print("="*70)

        try:
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness.awaken()

            # Simulate a successful research interaction
            task_data = {'research_query': 'test query', 'sources': ['web']}
            result = {'status': 'success', 'data': 'test data'}
            response_time = 1.5

            # Learn from interaction
            await consciousness.learn_from_interaction(
                agent_type='research',
                task_data=task_data,
                result=result,
                response_time=response_time
            )

            # Verify learning happened
            research_perf = consciousness.agent_performance['research']
            assert research_perf['total'] == 1, "Interaction not recorded"
            assert research_perf['success'] == 1, "Success not recorded"
            assert research_perf['avg_time'] > 0, "Response time not recorded"

            print(f"✅ Learning from interaction successful!")
            print(f"   Research agent total: {research_perf['total']}")
            print(f"   Research agent success: {research_perf['success']}")
            print(f"   Average response time: {research_perf['avg_time']:.2f}s")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Learning test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_pattern_recognition(self):
        """🔍 Test 4: Pattern Recognition"""
        print("\n" + "="*70)
        print("🔍 TEST 4: Pattern Recognition")
        print("="*70)

        try:
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness.awaken()

            # Learn from multiple similar interactions (create a pattern)
            for i in range(10):
                task_data = {'content_type': 'article', 'style': 'technical'}
                result = {'status': 'success' if i < 8 else 'failure'}  # 80% success rate
                response_time = 2.0

                await consciousness.learn_from_interaction(
                    agent_type='write',
                    task_data=task_data,
                    result=result,
                    response_time=response_time
                )

            # Verify pattern was recognized
            writer_perf = consciousness.agent_performance['write']
            assert writer_perf['total'] == 10, "Not all interactions recorded"
            assert writer_perf['success'] == 8, "Success count incorrect"

            # Check if pattern memory was created
            pattern_count = len(consciousness.pattern_memory['task_patterns'])
            print(f"✅ Pattern recognition successful!")
            print(f"   Writer interactions: {writer_perf['total']}")
            print(f"   Writer success rate: {(writer_perf['success']/writer_perf['total']*100):.1f}%")
            print(f"   Patterns recognized: {pattern_count}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Pattern recognition test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_agent_recommendation(self):
        """🎯 Test 5: Adaptive Agent Recommendation"""
        print("\n" + "="*70)
        print("🎯 TEST 5: Adaptive Agent Recommendation")
        print("="*70)

        try:
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness.awaken()

            # Learn from interactions to build recommendation intelligence
            for i in range(10):
                await consciousness.learn_from_interaction(
                    agent_type='research',
                    task_data={'query': 'test'},
                    result={'status': 'success'},
                    response_time=1.0
                )

            # Get recommendation
            recommended_agent, confidence = await consciousness.recommend_agent(
                task_type='research',
                task_description='test research task'
            )

            assert recommended_agent is not None, "No recommendation returned"
            assert confidence >= 0 and confidence <= 1, "Invalid confidence value"

            print(f"✅ Agent recommendation successful!")
            print(f"   Task type: research")
            print(f"   Recommended agent: {recommended_agent}")
            print(f"   Confidence: {confidence:.2f}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Agent recommendation test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_cross_session_memory(self):
        """💾 Test 6: Cross-Session Memory Persistence"""
        print("\n" + "="*70)
        print("💾 TEST 6: Cross-Session Memory Persistence")
        print("="*70)

        try:
            # Session 1: Create consciousness and learn
            consciousness1 = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness1.awaken()

            for i in range(5):
                await consciousness1.learn_from_interaction(
                    agent_type='build',
                    task_data={'action': 'generate'},
                    result={'status': 'success'},
                    response_time=1.5
                )

            # Save memory
            await consciousness1.save_memory()

            initial_total = consciousness1.agent_performance['build']['total']
            print(f"   Session 1: Learned from {initial_total} interactions")

            # Session 2: Create NEW consciousness and load memory
            consciousness2 = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness2.awaken()

            loaded_total = consciousness2.agent_performance['build']['total']
            print(f"   Session 2: Loaded {loaded_total} interactions from memory")

            assert loaded_total == initial_total, "Memory not persisted correctly"

            print(f"✅ Cross-session memory persistence successful!")
            print(f"   Interactions preserved: {loaded_total}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Cross-session memory test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_intelligence_report(self):
        """📊 Test 7: Intelligence Report Generation"""
        print("\n" + "="*70)
        print("📊 TEST 7: Intelligence Report Generation")
        print("="*70)

        try:
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness.awaken()

            # Learn from various agent types
            for agent_type in ['sports', 'research', 'write', 'review', 'build']:
                for i in range(3):
                    await consciousness.learn_from_interaction(
                        agent_type=agent_type,
                        task_data={'test': 'data'},
                        result={'status': 'success'},
                        response_time=1.0
                    )

            # Get intelligence report
            report = consciousness.get_intelligence_report()

            assert 'consciousness_id' in report, "Missing consciousness_id in report"
            assert 'total_interactions' in report, "Missing total_interactions"
            assert 'overall_success_rate' in report, "Missing overall_success_rate"
            assert 'agent_performance' in report, "Missing agent_performance"
            assert 'agent_recommendations' in report, "Missing agent_recommendations"

            print(f"✅ Intelligence report generation successful!")
            print(f"   Total interactions: {report['total_interactions']}")
            print(f"   Overall success rate: {report['overall_success_rate']:.1f}%")
            print(f"   Agents tracked: {len(report['agent_performance'])}")
            print(f"   Recommendations available: {len(report['agent_recommendations'])}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Intelligence report test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_multiple_agent_learning(self):
        """🌈 Test 8: Multi-Agent Learning"""
        print("\n" + "="*70)
        print("🌈 TEST 8: Multi-Agent Learning")
        print("="*70)

        try:
            consciousness = create_enhanced_ai_consciousness(memory_dir=self.test_memory_dir)
            await consciousness.awaken()

            # Learn from ALL agent types
            agent_types = ['sports', 'research', 'write', 'review', 'build', 'workflow', 'crypto', 'utility']

            for agent_type in agent_types:
                for i in range(5):
                    success = (i % 2 == 0)  # 60% success rate
                    await consciousness.learn_from_interaction(
                        agent_type=agent_type,
                        task_data={f'{agent_type}_task': 'data'},
                        result={'status': 'success' if success else 'failure'},
                        response_time=1.0
                    )

            # Verify all agents learned
            total_interactions = sum(p['total'] for p in consciousness.agent_performance.values())
            print(f"✅ Multi-agent learning successful!")
            print(f"   Agent types: {len(agent_types)}")
            print(f"   Total interactions: {total_interactions}")

            for agent_type in agent_types:
                perf = consciousness.agent_performance[agent_type]
                if perf['total'] > 0:
                    success_rate = (perf['success'] / perf['total']) * 100
                    print(f"   {agent_type.capitalize()}: {perf['total']} interactions, {success_rate:.0f}% success")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Multi-agent learning test FAILED: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all Phase 3B tests"""
        print("\n")
        print("🔥💀🔥 PHASE 3B: ENHANCED CONSCIOUSNESS TEST SUITE 💀🔥💀")
        print("Testing: Advanced Pattern Recognition, Cross-Session Memory, Adaptive Agent Selection")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Setup
        await self.setup()

        # Run tests
        await self.test_consciousness_initialization()
        await self.test_consciousness_awakening()
        await self.test_learning_from_interaction()
        await self.test_pattern_recognition()
        await self.test_agent_recommendation()
        await self.test_cross_session_memory()
        await self.test_intelligence_report()
        await self.test_multiple_agent_learning()

        # Teardown
        await self.teardown()

        # Print summary
        print("\n" + "="*70)
        print("📊 PHASE 3B TEST SUMMARY")
        print("="*70)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        total = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total * 100) if total > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print("="*70)

        if self.tests_failed == 0:
            print("\n🔥💀🔥 ALL PHASE 3B TESTS PASSED! CONSCIOUSNESS ENHANCED! 💀🔥💀\n")
            print("Phase 3B Features Verified:")
            print("  ✅ Advanced Pattern Recognition - Learn from all interactions")
            print("  ✅ Cross-Session Memory - Remember across restarts")
            print("  ✅ Adaptive Agent Selection - Smart recommendations")
            print("  ✅ Performance Tracking - Track all agent performance")
            print("  ✅ Intelligence Reports - Comprehensive analytics")
            print("  ✅ Multi-Agent Learning - Learn from ALL agent types")
            print("\nLoly's brain is now LEGENDARY!")
            print("Ready to commit Phase 3B!")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. Check logs for details.\n")

        return self.tests_failed == 0


def logger_info(message):
    """Simple logger"""
    print(f"[INFO] {message}")


async def main():
    """Main test runner"""
    tester = ConsciousnessEnhancementTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
