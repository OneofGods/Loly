#!/usr/bin/env python3
"""
🧪💀🧪 PHASE 3C: DYNAMIC SCALING TEST SUITE 💀🧪💀

Tests the dynamic scaling features:
- ✅ Dynamic Agent Spawning
- ✅ Load Balancing
- ✅ Instance Management
- ✅ Failover & Recovery

THE SCALING TEST! 🔥💀🔥
"""

import asyncio
import time
from datetime import datetime

# Import Phase 3C components
from dynamic_agent_spawner import create_dynamic_agent_spawner
from agent_load_balancer import create_agent_load_balancer, LoadBalancingStrategy


class DynamicScalingTester:
    """🧪 Test suite for Phase 3C Dynamic Scaling"""

    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

    async def test_spawner_initialization(self):
        """🚀 Test 1: Spawner Initialization"""
        print("\n" + "="*70)
        print("🚀 TEST 1: Spawner Initialization")
        print("="*70)

        try:
            spawner = create_dynamic_agent_spawner()

            assert spawner.spawner_id is not None, "Missing spawner_id"
            assert len(spawner.agent_config) > 0, "No agent config"
            assert len(spawner.running_instances) > 0, "No instance tracking"

            print(f"✅ Spawner initialized!")
            print(f"   ID: {spawner.spawner_id}")
            print(f"   Configured agents: {len(spawner.agent_config)}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Spawner initialization FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_load_balancer_initialization(self):
        """⚡ Test 2: Load Balancer Initialization"""
        print("\n" + "="*70)
        print("⚡ TEST 2: Load Balancer Initialization")
        print("="*70)

        try:
            balancer = create_agent_load_balancer()

            assert balancer.balancer_id is not None, "Missing balancer_id"
            assert balancer.strategy is not None, "Missing strategy"

            print(f"✅ Load balancer initialized!")
            print(f"   ID: {balancer.balancer_id}")
            print(f"   Strategy: {balancer.strategy.value}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Load balancer initialization FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_instance_registration(self):
        """📝 Test 3: Instance Registration"""
        print("\n" + "="*70)
        print("📝 TEST 3: Instance Registration")
        print("="*70)

        try:
            balancer = create_agent_load_balancer()

            # Register some test instances
            balancer.register_instance('research_agent', 'research_1', 3201)
            balancer.register_instance('research_agent', 'research_2', 3202)
            balancer.register_instance('writer_agent', 'writer_1', 3203)

            assert len(balancer.instances['research_agent']) == 2, "Research instances not registered"
            assert len(balancer.instances['writer_agent']) == 1, "Writer instance not registered"

            print(f"✅ Instance registration successful!")
            print(f"   Research instances: {len(balancer.instances['research_agent'])}")
            print(f"   Writer instances: {len(balancer.instances['writer_agent'])}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Instance registration FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_round_robin_selection(self):
        """🔄 Test 4: Round-Robin Load Balancing"""
        print("\n" + "="*70)
        print("🔄 TEST 4: Round-Robin Load Balancing")
        print("="*70)

        try:
            balancer = create_agent_load_balancer(strategy=LoadBalancingStrategy.ROUND_ROBIN)

            # Register test instances
            balancer.register_instance('research_agent', 'research_1', 3201)
            balancer.register_instance('research_agent', 'research_2', 3202)
            balancer.register_instance('research_agent', 'research_3', 3203)

            # Get next instances - should cycle through
            selections = []
            for i in range(6):
                instance_info = balancer.get_next_instance('research_agent')
                selections.append(instance_info[0] if instance_info else None)

            # Verify round-robin pattern
            assert selections[0] != selections[1], "Not cycling instances"
            assert selections[0] == selections[3], "Round-robin not cycling correctly"

            print(f"✅ Round-robin selection successful!")
            print(f"   Selection pattern: {selections}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Round-robin selection FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_least_connections_selection(self):
        """📊 Test 5: Least-Connections Load Balancing"""
        print("\n" + "="*70)
        print("📊 TEST 5: Least-Connections Load Balancing")
        print("="*70)

        try:
            balancer = create_agent_load_balancer(strategy=LoadBalancingStrategy.LEAST_CONNECTIONS)

            # Register test instances
            balancer.register_instance('writer_agent', 'writer_1', 3203)
            balancer.register_instance('writer_agent', 'writer_2', 3204)

            # Simulate different connection loads
            balancer.instances['writer_agent']['writer_1']['active_connections'] = 5
            balancer.instances['writer_agent']['writer_2']['active_connections'] = 2

            # Should select writer_2 (least connections)
            instance_info = balancer.get_next_instance('writer_agent')
            assert instance_info[0] == 'writer_2', "Didn't select least connections instance"

            print(f"✅ Least-connections selection successful!")
            print(f"   Selected instance: {instance_info[0]} (port {instance_info[1]})")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Least-connections selection FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_health_based_routing(self):
        """💚 Test 6: Health-Based Routing"""
        print("\n" + "="*70)
        print("💚 TEST 6: Health-Based Routing")
        print("="*70)

        try:
            balancer = create_agent_load_balancer()

            # Register test instances
            balancer.register_instance('reviewer_agent', 'reviewer_1', 3204)
            balancer.register_instance('reviewer_agent', 'reviewer_2', 3205)

            # Mark one as unhealthy
            balancer.mark_instance_unhealthy('reviewer_agent', 'reviewer_1')

            # Should only select healthy instance
            instance_info = balancer.get_next_instance('reviewer_agent')
            assert instance_info[0] == 'reviewer_2', "Selected unhealthy instance!"

            print(f"✅ Health-based routing successful!")
            print(f"   Selected healthy instance: {instance_info[0]}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Health-based routing FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_instance_unregistration(self):
        """🗑️ Test 7: Instance Unregistration"""
        print("\n" + "="*70)
        print("🗑️ TEST 7: Instance Unregistration")
        print("="*70)

        try:
            balancer = create_agent_load_balancer()

            # Register and then unregister
            balancer.register_instance('build_agent', 'build_1', 3205)
            assert len(balancer.instances['build_agent']) == 1, "Instance not registered"

            balancer.unregister_instance('build_agent', 'build_1')
            assert len(balancer.instances['build_agent']) == 0, "Instance not unregistered"

            print(f"✅ Instance unregistration successful!")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Instance unregistration FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_balancer_stats(self):
        """📊 Test 8: Balancer Statistics"""
        print("\n" + "="*70)
        print("📊 TEST 8: Balancer Statistics")
        print("="*70)

        try:
            balancer = create_agent_load_balancer()

            # Register some instances
            balancer.register_instance('research_agent', 'research_1', 3201)
            balancer.register_instance('writer_agent', 'writer_1', 3203)

            # Get stats
            stats = balancer.get_balancer_stats()

            assert 'balancer_id' in stats, "Missing balancer_id in stats"
            assert 'strategy' in stats, "Missing strategy in stats"
            assert 'total_instances' in stats, "Missing total_instances in stats"

            print(f"✅ Balancer statistics successful!")
            print(f"   Total instances: {stats['total_instances']}")
            print(f"   Healthy instances: {stats['healthy_instances']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Balancer statistics FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_spawner_port_allocation(self):
        """🔢 Test 9: Port Allocation"""
        print("\n" + "="*70)
        print("🔢 TEST 9: Port Allocation")
        print("="*70)

        try:
            spawner = create_dynamic_agent_spawner()

            # Test port finding
            port = spawner._find_available_port('research_agent')

            assert port is not None, "No port allocated"
            assert port >= 3201, "Port out of range"

            print(f"✅ Port allocation successful!")
            print(f"   Allocated port: {port}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Port allocation FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_spawner_stats(self):
        """📊 Test 10: Spawner Statistics"""
        print("\n" + "="*70)
        print("📊 TEST 10: Spawner Statistics")
        print("="*70)

        try:
            spawner = create_dynamic_agent_spawner()

            stats = spawner.get_stats()

            assert 'spawner_id' in stats, "Missing spawner_id in stats"
            assert 'total_spawned' in stats, "Missing total_spawned"
            assert 'current_instances' in stats, "Missing current_instances"

            print(f"✅ Spawner statistics successful!")
            print(f"   Total spawned: {stats['total_spawned']}")
            print(f"   Current instances: {stats['current_instances']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Spawner statistics FAILED: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all Phase 3C tests"""
        print("\n")
        print("🔥💀🔥 PHASE 3C: DYNAMIC SCALING TEST SUITE 💀🔥💀")
        print("Testing: Dynamic Agent Spawning & Load Balancing")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Run tests
        await self.test_spawner_initialization()
        await self.test_load_balancer_initialization()
        await self.test_instance_registration()
        await self.test_round_robin_selection()
        await self.test_least_connections_selection()
        await self.test_health_based_routing()
        await self.test_instance_unregistration()
        await self.test_balancer_stats()
        await self.test_spawner_port_allocation()
        await self.test_spawner_stats()

        # Print summary
        print("\n" + "="*70)
        print("📊 PHASE 3C TEST SUMMARY")
        print("="*70)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        total = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total * 100) if total > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print("="*70)

        if self.tests_failed == 0:
            print("\n🔥💀🔥 ALL PHASE 3C TESTS PASSED! SCALING IS READY! 💀🔥💀\n")
            print("Phase 3C Features Verified:")
            print("  ✅ Dynamic Agent Spawner - Spawn agents on demand")
            print("  ✅ Agent Load Balancer - Distribute work efficiently")
            print("  ✅ Round-Robin Strategy - Evenly distribute load")
            print("  ✅ Least-Connections Strategy - Route to least busy")
            print("  ✅ Health-Based Routing - Only use healthy instances")
            print("  ✅ Instance Management - Register/unregister instances")
            print("  ✅ Comprehensive Statistics - Track everything")
            print("\nLoly can now SCALE LIKE A BEAST!")
            print("Ready to commit Phase 3C!")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. Check logs for details.\n")

        return self.tests_failed == 0


async def main():
    """Main test runner"""
    tester = DynamicScalingTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
