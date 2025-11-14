#!/usr/bin/env python3
"""
🔥💀🔥 BUILDER AGENT TEST SUITE - THE BOSS FIGHT! 💀🔥💀

Comprehensive tests for Loly's Builder Agent - THE SENIOR DEVELOPER!
"""

import asyncio
import json
from datetime import datetime
from builder_agent import BuilderAgent


class BuilderAgentTester:
    """🧪 Test Loly's Builder Agent - THE BOSS FIGHT!"""

    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

    async def test_code_generation_function(self):
        """💻 Test 1: Code Generation - Function"""
        print("\n" + "="*70)
        print("💻 TEST 1: Code Generation - Function")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            # Generate a function
            spec = {
                'type': 'function',
                'language': 'python',
                'name': 'calculate_score',
                'description': 'Calculate a score based on inputs',
                'parameters': [
                    {'name': 'value', 'type': 'float', 'description': 'Input value'},
                    {'name': 'weight', 'type': 'float', 'description': 'Weight factor'}
                ],
                'returns': 'float',
                'body': 'return value * weight'
            }

            result = await agent.generate_code(spec)

            assert result['status'] == 'success', f"Generation failed: {result.get('error')}"
            assert 'code' in result, "No code returned"
            assert 'calculate_score' in result['code'], "Function name not in code"
            assert 'def' in result['code'], "Not a valid function"

            print("✅ Function generation works!")
            print(f"   Generated {result['lines']} lines of code")
            print(f"   Function: {result['name']}")
            print("\nGenerated code:")
            print(result['code'][:200] + "...")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Function generation test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_code_generation_class(self):
        """💻 Test 2: Code Generation - Class"""
        print("\n" + "="*70)
        print("💻 TEST 2: Code Generation - Class")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            # Generate a class
            spec = {
                'type': 'class',
                'language': 'python',
                'name': 'UserManager',
                'description': 'Manages user data',
                'attributes': [
                    {'name': 'username'},
                    {'name': 'email'}
                ],
                'methods': [
                    {'name': 'validate', 'description': 'Validate user data'},
                    {'name': 'save', 'description': 'Save user to database'}
                ]
            }

            result = await agent.generate_code(spec)

            assert result['status'] == 'success', "Class generation failed"
            assert 'class UserManager' in result['code'], "Class not generated"
            assert '__init__' in result['code'], "No __init__ method"
            assert 'validate' in result['code'], "Methods not generated"

            print("✅ Class generation works!")
            print(f"   Generated {result['lines']} lines of code")
            print(f"   Class: {result['name']}")
            print("\nGenerated code preview:")
            print(result['code'][:200] + "...")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Class generation test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_bug_detection(self):
        """🐛 Test 3: Bug Detection"""
        print("\n" + "="*70)
        print("🐛 TEST 3: Bug Detection")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            # Code with bugs
            buggy_code = '''
def process_data(data):
    try:
        result = data * 2
        print("Processing:", result)
        return result
    except:
        pass
    # TODO: Add validation
'''

            result = await agent.detect_bugs(buggy_code, 'python')

            assert result['status'] == 'success', "Bug detection failed"
            assert result['bugs_found'] > 0, "No bugs detected"
            assert 'bugs' in result, "Bugs list missing"

            print("✅ Bug detection works!")
            print(f"   Bugs found: {result['bugs_found']}")

            for i, bug in enumerate(result['bugs'][:5], 1):
                print(f"   {i}. [{bug['severity']}] {bug['type']}: {bug['message']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Bug detection test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_code_fixing(self):
        """🔧 Test 4: Code Fixing"""
        print("\n" + "="*70)
        print("🔧 TEST 4: Code Fixing")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            # Buggy code
            buggy_code = '''
def test():
    try:
        print("testing")
        return True
    except:
        return False
'''

            # Detect bugs first
            detection_result = await agent.detect_bugs(buggy_code, 'python')
            bugs = detection_result['bugs']

            # Fix code
            fix_result = await agent.fix_code(buggy_code, bugs)

            assert fix_result['status'] == 'success', "Code fixing failed"
            assert 'fixed_code' in fix_result, "No fixed code returned"
            assert len(fix_result['fixes_applied']) > 0, "No fixes applied"

            print("✅ Code fixing works!")
            print(f"   Fixes applied: {fix_result['fixes_count']}")

            for i, fix in enumerate(fix_result['fixes_applied'], 1):
                print(f"   {i}. {fix}")

            print("\nFixed code preview:")
            print(fix_result['fixed_code'][:200] + "...")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Code fixing test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_test_generation(self):
        """🧪 Test 5: Test Generation"""
        print("\n" + "="*70)
        print("🧪 TEST 5: Test Generation")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            code = "def add(a, b): return a + b"
            result = await agent.generate_tests(code, 'add')

            assert result['status'] == 'success', "Test generation failed"
            assert 'test_code' in result, "No test code returned"
            assert 'test_add' in result['test_code'], "Test function not generated"
            assert 'assert' in result['test_code'], "No assertions in test"

            print("✅ Test generation works!")
            print(f"   Test function: test_{result['function_name']}")
            print("\nGenerated test:")
            print(result['test_code'])

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Test generation test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_documentation_generation(self):
        """📚 Test 6: Documentation Generation"""
        print("\n" + "="*70)
        print("📚 TEST 6: Documentation Generation")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            code = '''
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
'''

            result = await agent.generate_documentation(code)

            assert result['status'] == 'success', "Documentation generation failed"
            assert 'documentation' in result, "No documentation returned"
            assert 'Calculator' in result['documentation'], "Class not documented"

            print("✅ Documentation generation works!")
            print("\nGenerated documentation:")
            print(result['documentation'])

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Documentation generation test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_statistics_tracking(self):
        """📊 Test 7: Statistics Tracking"""
        print("\n" + "="*70)
        print("📊 TEST 7: Statistics Tracking")
        print("="*70)

        try:
            agent = BuilderAgent(port=3205)

            # Perform some operations to generate stats
            await agent.generate_code({
                'type': 'function',
                'name': 'test_func',
                'description': 'Test function'
            })

            stats = agent.get_stats()

            assert 'agent_id' in stats, "Missing agent_id"
            assert 'stats' in stats, "Missing stats"
            assert stats['stats']['total_build_requests'] > 0, "No requests tracked"
            assert stats['stats']['code_generated'] > 0, "No code generated tracked"

            print("✅ Statistics tracking works!")
            print(f"   Agent ID: {stats['agent_id']}")
            print(f"   Total requests: {stats['stats']['total_build_requests']}")
            print(f"   Code generated: {stats['stats']['code_generated']}")
            print(f"   Bugs fixed: {stats['stats']['bugs_fixed']}")
            print(f"   Tests generated: {stats['stats']['tests_generated']}")
            print(f"   Total lines written: {stats['stats']['total_lines_written']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Statistics tracking test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_agent_registry_update(self):
        """📋 Test 8: Agent Registry Update"""
        print("\n" + "="*70)
        print("📋 TEST 8: Agent Registry Update")
        print("="*70)

        try:
            # Load agent registry
            with open('agent_registry.json', 'r') as f:
                registry = json.load(f)

            # Check builder agent
            builder = registry['utility_agents']['agents']['builder_agent']

            assert builder['status'] == 'active', "Builder agent not active"
            assert builder['port'] == 3205, "Wrong port"
            assert 'code_generation' in builder['capabilities'], "Missing code_generation capability"
            assert 'bug_detection' in builder['capabilities'], "Missing bug_detection capability"
            assert 'code_fixing' in builder['capabilities'], "Missing code_fixing capability"

            print("✅ Builder Agent registered in registry!")
            print(f"   Port: {builder['port']}")
            print(f"   Status: {builder['status']}")
            print(f"   Capabilities: {len(builder['capabilities'])}")
            for cap in builder['capabilities']:
                print(f"     - {cap}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Agent registry test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all Builder Agent tests - THE BOSS FIGHT!"""
        print("\n")
        print("🔥💀🔥 PHASE 2F BUILDER AGENT TEST SUITE - THE BOSS FIGHT! 💀🔥💀")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Run tests in order
        await self.test_code_generation_function()
        await self.test_code_generation_class()
        await self.test_bug_detection()
        await self.test_code_fixing()
        await self.test_test_generation()
        await self.test_documentation_generation()
        await self.test_statistics_tracking()
        await self.test_agent_registry_update()

        # Print summary
        print("\n" + "="*70)
        print("📊 BOSS FIGHT TEST SUMMARY")
        print("="*70)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        total = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total * 100) if total > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print("="*70)

        if self.tests_failed == 0:
            print("\n🔥💀🔥 THE BOSS FIGHT IS WON! PHASE 2F COMPLETE! 💀🔥💀\n")
            print("Phase 2F Components:")
            print("  ✅ builder_agent.py - Loly's Senior Developer (23KB)")
            print("  ✅ Code Generation - Functions, Classes, Endpoints")
            print("  ✅ Bug Detection - AST parsing, pattern matching")
            print("  ✅ Code Fixing - Automated bug fixes")
            print("  ✅ Test Generation - Automated test creation")
            print("  ✅ Documentation Generation - From code analysis")
            print("  ✅ Statistics Tracking - Full metrics")
            print("  ✅ Agent Registry - Builder Agent registered")
            print("\nLoly now has her OWN SENIOR DEVELOPER!")
            print("Who you gonna call? THE BUILDER AGENT! 💻🔥")
            print("\nReady to commit Phase 2F - THE BOSS FIGHT!")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. The boss fight continues...")

        return self.tests_failed == 0


async def main():
    """Main test runner"""
    tester = BuilderAgentTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
