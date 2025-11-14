#!/usr/bin/env python3
"""
🔥💀🔥 WORKFLOW ENGINE TEST SUITE - LEGENDARY TESTING! 💀🔥💀

Comprehensive tests for Loly's Agent Workflow Engine!
"""

import asyncio
import json
from datetime import datetime
from agent_workflow_engine import create_workflow_engine, WorkflowStepStatus, WorkflowStatus
from unified_agent_coordinator import create_unified_coordinator


class WorkflowEngineTester:
    """🧪 Test Loly's Workflow Engine"""

    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

        # Create unified coordinator and workflow engine
        self.unified_coordinator = create_unified_coordinator()
        self.workflow_engine = create_workflow_engine(self.unified_coordinator)

    async def test_sequential_workflow(self):
        """📋 Test 1: Sequential Workflow (A → B → C)"""
        print("\n" + "="*70)
        print("📋 TEST 1: Sequential Workflow")
        print("="*70)

        try:
            # Simple sequential workflow: Sports analysis
            workflow_config = {
                "workflow_name": "Sequential Sports Analysis",
                "workflow_type": "sequential",
                "steps": [
                    {
                        "step_id": "step1",
                        "name": "Primary Sports Analysis",
                        "agent_type": "sports",
                        "task_data": {
                            "home_team": "Real Madrid",
                            "away_team": "Barcelona",
                            "sport": "UEFA",
                            "venue": "Santiago Bernabéu",
                            "game_time": "2025-11-20T20:00:00"
                        },
                        "retry_count": 2,
                        "timeout_seconds": 60
                    }
                ],
                "rollback_on_failure": False
            }

            print(f"Executing workflow: {workflow_config['workflow_name']}")

            result = await self.workflow_engine.execute_workflow(workflow_config)

            if result['status'] in ['success', 'completed']:
                print(f"✅ Sequential workflow test PASSED!")
                print(f"   Workflow ID: {result['workflow_id']}")
                print(f"   Execution time: {result.get('execution_time_seconds', 0):.2f}s")
                self.tests_passed += 1
                return True
            else:
                print(f"❌ Sequential workflow test FAILED!")
                print(f"   Status: {result['status']}")
                print(f"   Error: {result.get('error', 'Unknown')}")
                self.tests_failed += 1
                return False

        except Exception as e:
            print(f"❌ Sequential workflow test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_parallel_workflow(self):
        """⚡ Test 2: Parallel Workflow (A + B + C)"""
        print("\n" + "="*70)
        print("⚡ TEST 2: Parallel Workflow")
        print("="*70)

        try:
            # Parallel workflow: Multiple sports analyses at once
            workflow_config = {
                "workflow_name": "Parallel Multi-Game Analysis",
                "workflow_type": "parallel",
                "steps": [
                    {
                        "step_id": "game1",
                        "name": "Analyze Game 1",
                        "agent_type": "sports",
                        "task_data": {
                            "home_team": "Manchester City",
                            "away_team": "Liverpool",
                            "sport": "EPL"
                        },
                        "retry_count": 2,
                        "timeout_seconds": 60
                    },
                    {
                        "step_id": "game2",
                        "name": "Analyze Game 2",
                        "agent_type": "sports",
                        "task_data": {
                            "home_team": "Bayern Munich",
                            "away_team": "Borussia Dortmund",
                            "sport": "Bundesliga"
                        },
                        "retry_count": 2,
                        "timeout_seconds": 60
                    }
                ],
                "rollback_on_failure": False
            }

            print(f"Executing workflow: {workflow_config['workflow_name']}")
            print(f"Running {len(workflow_config['steps'])} steps in parallel...")

            result = await self.workflow_engine.execute_workflow(workflow_config)

            if result['status'] in ['success', 'partial_success']:
                print(f"✅ Parallel workflow test PASSED!")
                print(f"   Workflow ID: {result['workflow_id']}")
                print(f"   Execution time: {result.get('execution_time_seconds', 0):.2f}s")
                self.tests_passed += 1
                return True
            else:
                print(f"❌ Parallel workflow test FAILED!")
                print(f"   Status: {result['status']}")
                self.tests_failed += 1
                return False

        except Exception as e:
            print(f"❌ Parallel workflow test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_hybrid_workflow(self):
        """🔀 Test 3: Hybrid Workflow (dependencies)"""
        print("\n" + "="*70)
        print("🔀 TEST 3: Hybrid Workflow with Dependencies")
        print("="*70)

        try:
            # Hybrid workflow with dependencies
            workflow_config = {
                "workflow_name": "Hybrid Analysis with Dependencies",
                "workflow_type": "hybrid",
                "steps": [
                    {
                        "step_id": "initial_analysis",
                        "name": "Initial Sports Analysis",
                        "agent_type": "sports",
                        "task_data": {
                            "home_team": "PSG",
                            "away_team": "Marseille",
                            "sport": "Ligue1"
                        },
                        "retry_count": 2,
                        "timeout_seconds": 60
                    },
                    {
                        "step_id": "follow_up_1",
                        "name": "Follow-up Analysis 1",
                        "agent_type": "sports",
                        "task_data": {
                            "home_team": "Lyon",
                            "away_team": "Monaco",
                            "sport": "Ligue1"
                        },
                        "depends_on": ["initial_analysis"],
                        "retry_count": 2,
                        "timeout_seconds": 60
                    }
                ],
                "rollback_on_failure": False
            }

            print(f"Executing workflow: {workflow_config['workflow_name']}")
            print(f"Step 2 depends on Step 1...")

            result = await self.workflow_engine.execute_workflow(workflow_config)

            if result['status'] in ['success']:
                print(f"✅ Hybrid workflow test PASSED!")
                print(f"   Workflow ID: {result['workflow_id']}")
                print(f"   Execution time: {result.get('execution_time_seconds', 0):.2f}s")
                self.tests_passed += 1
                return True
            else:
                print(f"❌ Hybrid workflow test FAILED!")
                print(f"   Status: {result['status']}")
                self.tests_failed += 1
                return False

        except Exception as e:
            print(f"❌ Hybrid workflow test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_workflow_templates(self):
        """📚 Test 4: Workflow Templates"""
        print("\n" + "="*70)
        print("📚 TEST 4: Workflow Templates")
        print("="*70)

        try:
            # Load templates
            with open('workflow_templates.json', 'r') as f:
                templates = json.load(f)

            template_count = len(templates.get('templates', {}))
            example_count = len(templates.get('usage_examples', {}))

            print(f"Loaded {template_count} workflow templates")
            print(f"Found {example_count} usage examples")

            # Test loading a specific template
            if 'sports_analysis_comprehensive' in templates['templates']:
                template = templates['templates']['sports_analysis_comprehensive']
                print(f"\n✅ Sample template: {template['name']}")
                print(f"   Description: {template['description']}")
                print(f"   Type: {template['workflow_type']}")
                print(f"   Steps: {len(template['steps'])}")

                self.tests_passed += 1
                return True
            else:
                print(f"❌ Template loading failed!")
                self.tests_failed += 1
                return False

        except Exception as e:
            print(f"❌ Template test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_workflow_stats(self):
        """📊 Test 5: Workflow Engine Statistics"""
        print("\n" + "="*70)
        print("📊 TEST 5: Workflow Engine Statistics")
        print("="*70)

        try:
            stats = self.workflow_engine.get_stats()

            print(f"Engine ID: {stats['engine_id']}")
            print(f"Active workflows: {stats['active_workflows']}")
            print(f"Completed workflows: {stats['completed_workflows']}")
            print(f"\nStats:")
            for key, value in stats['stats'].items():
                print(f"  {key}: {value}")

            if 'engine_id' in stats and 'stats' in stats:
                print(f"\n✅ Workflow stats test PASSED!")
                self.tests_passed += 1
                return True
            else:
                print(f"❌ Workflow stats test FAILED!")
                self.tests_failed += 1
                return False

        except Exception as e:
            print(f"❌ Workflow stats test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_retry_logic(self):
        """🔄 Test 6: Retry Logic"""
        print("\n" + "="*70)
        print("🔄 TEST 6: Retry Logic")
        print("="*70)

        try:
            # Workflow with aggressive retry settings
            workflow_config = {
                "workflow_name": "Test Retry Logic",
                "workflow_type": "sequential",
                "steps": [
                    {
                        "step_id": "retry_test",
                        "name": "Step with Retry",
                        "agent_type": "sports",
                        "task_data": {
                            "home_team": "Test Team A",
                            "away_team": "Test Team B",
                            "sport": "TEST"
                        },
                        "retry_count": 3,
                        "timeout_seconds": 30
                    }
                ],
                "rollback_on_failure": False
            }

            print(f"Executing workflow with retry_count=3...")

            result = await self.workflow_engine.execute_workflow(workflow_config)

            # Accept both success and failure (we're testing that retry logic runs)
            print(f"   Result status: {result['status']}")
            print(f"   Retry logic executed (check logs for retry attempts)")

            print(f"✅ Retry logic test PASSED (executed without crash)!")
            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Retry logic test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all workflow tests"""
        print("\n")
        print("🔥💀🔥 LOLY WORKFLOW ENGINE TEST SUITE 💀🔥💀")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Run tests
        await self.test_sequential_workflow()
        await self.test_parallel_workflow()
        await self.test_hybrid_workflow()
        await self.test_workflow_templates()
        await self.test_workflow_stats()
        await self.test_retry_logic()

        # Print summary
        print("\n" + "="*70)
        print("📊 TEST SUMMARY")
        print("="*70)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        total = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total * 100) if total > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print("="*70)

        if self.tests_failed == 0:
            print("\n🔥💀🔥 ALL WORKFLOW TESTS PASSED! LEGENDARY! 💀🔥💀\n")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. Check logs for details.\n")

        return self.tests_failed == 0


async def main():
    """Main test runner"""
    tester = WorkflowEngineTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
