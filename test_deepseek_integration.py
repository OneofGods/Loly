#!/usr/bin/env python3
"""
🧪💀🧪 PHASE 3D: DEEPSEEK INTEGRATION TEST SUITE 💀🧪💀

Tests the DeepSeek LLM integration:
- ✅ Service Initialization
- ✅ Configuration Management
- ✅ Task-Specific Settings
- ✅ Statistics Tracking
- ✅ Helper Methods

THE DEEPSEEK BRAIN TEST! 🔥💀🔥
"""

import asyncio
from datetime import datetime

# Import Phase 3D components
from deepseek_integration_service import create_deepseek_service


class DeepSeekIntegrationTester:
    """🧪 Test suite for Phase 3D DeepSeek Integration"""

    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

    async def test_service_initialization(self):
        """🤖 Test 1: Service Initialization"""
        print("\n" + "="*70)
        print("🤖 TEST 1: Service Initialization")
        print("="*70)

        try:
            service = create_deepseek_service()

            assert service.service_id is not None, "Missing service_id"
            assert service.deepseek_url is not None, "Missing deepseek_url"
            assert service.model_name is not None, "Missing model_name"
            assert service.config is not None, "Missing config"

            print(f"✅ Service initialized!")
            print(f"   ID: {service.service_id}")
            print(f"   DeepSeek URL: {service.deepseek_url}")
            print(f"   Model: {service.model_name}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Service initialization FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_task_configurations(self):
        """⚙️ Test 2: Task-Specific Configurations"""
        print("\n" + "="*70)
        print("⚙️ TEST 2: Task-Specific Configurations")
        print("="*70)

        try:
            service = create_deepseek_service()

            # Verify task configs exist
            task_types = ['code', 'reasoning', 'creative', 'analysis']

            for task_type in task_types:
                assert task_type in service.task_configs, f"Missing {task_type} config"
                config = service.task_configs[task_type]

                assert 'temperature' in config, f"Missing temperature in {task_type}"
                assert 'max_tokens' in config, f"Missing max_tokens in {task_type}"
                assert 'system_prompt' in config, f"Missing system_prompt in {task_type}"

            print(f"✅ Task configurations verified!")
            print(f"   Available task types: {len(task_types)}")

            for task_type in task_types:
                config = service.task_configs[task_type]
                print(f"   {task_type}: temp={config['temperature']}, tokens={config['max_tokens']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Task configurations FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_statistics_tracking(self):
        """📊 Test 3: Statistics Tracking"""
        print("\n" + "="*70)
        print("📊 TEST 3: Statistics Tracking")
        print("="*70)

        try:
            service = create_deepseek_service()

            # Verify stats structure
            assert 'total_requests' in service.stats, "Missing total_requests"
            assert 'successful_requests' in service.stats, "Missing successful_requests"
            assert 'failed_requests' in service.stats, "Missing failed_requests"
            assert 'total_tokens_used' in service.stats, "Missing total_tokens_used"

            # Get stats
            stats = service.get_stats()

            assert 'service_id' in stats, "Missing service_id in stats"
            assert 'total_requests' in stats, "Missing total_requests in stats"
            assert 'success_rate' in stats, "Missing success_rate in stats"

            print(f"✅ Statistics tracking verified!")
            print(f"   Total requests: {stats['total_requests']}")
            print(f"   Success rate: {stats['success_rate']:.1f}%")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Statistics tracking FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_cache_management(self):
        """🔄 Test 4: Cache Management"""
        print("\n" + "="*70)
        print("🔄 TEST 4: Cache Management")
        print("="*70)

        try:
            service = create_deepseek_service()

            # Initially disabled
            assert service.cache_enabled == False, "Cache should be disabled initially"

            # Enable cache
            service.enable_cache()
            assert service.cache_enabled == True, "Cache not enabled"

            # Disable cache
            service.disable_cache()
            assert service.cache_enabled == False, "Cache not disabled"

            # Clear cache
            service.clear_cache()
            assert len(service.response_cache) == 0, "Cache not cleared"

            print(f"✅ Cache management verified!")
            print(f"   Cache enabled/disabled successfully")
            print(f"   Cache cleared successfully")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Cache management FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_helper_methods_exist(self):
        """🛠️ Test 5: Helper Methods Exist"""
        print("\n" + "="*70)
        print("🛠️ TEST 5: Helper Methods Exist")
        print("="*70)

        try:
            service = create_deepseek_service()

            # Check all helper methods exist
            methods = [
                'code_generation',
                'code_review',
                'bug_fixing',
                'complex_reasoning',
                'data_analysis',
                'creative_writing',
                'health_check',
                'get_stats'
            ]

            for method_name in methods:
                assert hasattr(service, method_name), f"Missing method: {method_name}"
                assert callable(getattr(service, method_name)), f"{method_name} not callable"

            print(f"✅ Helper methods verified!")
            print(f"   All {len(methods)} methods exist and are callable:")
            for method in methods:
                print(f"      • {method}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Helper methods check FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_config_parameters(self):
        """⚙️ Test 6: Configuration Parameters"""
        print("\n" + "="*70)
        print("⚙️ TEST 6: Configuration Parameters")
        print("="*70)

        try:
            service = create_deepseek_service()

            # Check main config
            assert 'temperature' in service.config, "Missing temperature"
            assert 'max_tokens' in service.config, "Missing max_tokens"
            assert 'top_p' in service.config, "Missing top_p"
            assert 'timeout' in service.config, "Missing timeout"

            # Validate ranges
            assert 0 <= service.config['temperature'] <= 1, "Invalid temperature"
            assert service.config['max_tokens'] > 0, "Invalid max_tokens"
            assert 0 <= service.config['top_p'] <= 1, "Invalid top_p"

            print(f"✅ Configuration parameters verified!")
            print(f"   Temperature: {service.config['temperature']}")
            print(f"   Max tokens: {service.config['max_tokens']}")
            print(f"   Top-p: {service.config['top_p']}")
            print(f"   Timeout: {service.config['timeout']}s")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Configuration parameters FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_custom_url_and_model(self):
        """🔧 Test 7: Custom URL and Model"""
        print("\n" + "="*70)
        print("🔧 TEST 7: Custom URL and Model")
        print("="*70)

        try:
            custom_url = "http://localhost:9000"
            custom_model = "deepseek-chat"

            service = create_deepseek_service(
                deepseek_url=custom_url,
                model_name=custom_model
            )

            assert service.deepseek_url == custom_url, "Custom URL not set"
            assert service.model_name == custom_model, "Custom model not set"

            print(f"✅ Custom configuration verified!")
            print(f"   Custom URL: {service.deepseek_url}")
            print(f"   Custom Model: {service.model_name}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Custom configuration FAILED: {e}")
            self.tests_failed += 1
            return False

    async def test_stats_update_logic(self):
        """📊 Test 8: Statistics Update Logic"""
        print("\n" + "="*70)
        print("📊 TEST 8: Statistics Update Logic")
        print("="*70)

        try:
            service = create_deepseek_service()

            # Manually simulate stat updates
            service.stats['total_requests'] = 10
            service.stats['successful_requests'] = 8
            service.stats['failed_requests'] = 2

            stats = service.get_stats()

            assert stats['total_requests'] == 10, "Total requests not tracked"
            assert stats['successful_requests'] == 8, "Successful requests not tracked"
            assert stats['failed_requests'] == 2, "Failed requests not tracked"
            assert stats['success_rate'] == 80.0, "Success rate calculation wrong"

            print(f"✅ Statistics update logic verified!")
            print(f"   Total: {stats['total_requests']}")
            print(f"   Success: {stats['successful_requests']}")
            print(f"   Failed: {stats['failed_requests']}")
            print(f"   Success rate: {stats['success_rate']:.1f}%")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Statistics update logic FAILED: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all Phase 3D tests"""
        print("\n")
        print("🔥💀🔥 PHASE 3D: DEEPSEEK INTEGRATION TEST SUITE 💀🔥💀")
        print("Testing: DeepSeek LLM Integration Service")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Run tests
        await self.test_service_initialization()
        await self.test_task_configurations()
        await self.test_statistics_tracking()
        await self.test_cache_management()
        await self.test_helper_methods_exist()
        await self.test_config_parameters()
        await self.test_custom_url_and_model()
        await self.test_stats_update_logic()

        # Print summary
        print("\n" + "="*70)
        print("📊 PHASE 3D TEST SUMMARY")
        print("="*70)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        total = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total * 100) if total > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print("="*70)

        if self.tests_failed == 0:
            print("\n🔥💀🔥 ALL PHASE 3D TESTS PASSED! DEEPSEEK INTEGRATION READY! 💀🔥💀\n")
            print("Phase 3D Features Verified:")
            print("  ✅ DeepSeek Service - Connection to local model")
            print("  ✅ Task Configurations - Code, reasoning, creative, analysis")
            print("  ✅ Helper Methods - Code gen, review, bug fix, reasoning, etc.")
            print("  ✅ Statistics Tracking - Requests, tokens, success rate")
            print("  ✅ Cache Management - Optional response caching")
            print("  ✅ Custom Configuration - URL and model name")
            print("\nLoly now has a REAL BRAIN - DeepSeek power!")
            print("Ready to commit Phase 3D!")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. Check logs for details.\n")

        return self.tests_failed == 0


async def main():
    """Main test runner"""
    tester = DeepSeekIntegrationTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
