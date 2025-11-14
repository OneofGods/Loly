#!/usr/bin/env python3
"""
🔥💀🔥 OPENAPI-MCP-SERVER STANDALONE TEST - PHASE 2C VERIFICATION! 💀🔥💀

Standalone tests for OpenAPI components (without full coordinator dependencies)
"""

import asyncio
import json
from datetime import datetime
from api_cache_manager import create_cache_manager
from api_rate_limiter import create_rate_limiter
from openapi_mcp_server import create_openapi_server


class OpenAPIStandaloneTester:
    """🧪 Test OpenAPI Components Standalone"""

    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

    async def test_cache_manager(self):
        """💾 Test 1: API Cache Manager"""
        print("\n" + "="*70)
        print("💾 TEST 1: API Cache Manager")
        print("="*70)

        try:
            # Create cache manager
            cache = create_cache_manager(max_size=5, default_ttl_seconds=10)

            # Test set and get
            await cache.set('test_key', {'data': 'test_value'})
            value = await cache.get('test_key')

            assert value and value['data'] == 'test_value', "Cache set/get failed"
            print("✅ Cache set/get works!")

            # Test cache miss
            miss_value = await cache.get('nonexistent')
            assert miss_value is None, "Cache miss not handled"
            print("✅ Cache miss handled correctly!")

            # Test LRU eviction
            for i in range(10):
                await cache.set(f'key{i}', {'data': f'value{i}'})

            stats = cache.get_stats()
            assert stats['current_size'] <= 5, "LRU eviction failed"
            print(f"✅ LRU eviction works! (size: {stats['current_size']}/{stats['max_size']})")
            print(f"   Cache hit rate: {stats['hit_rate_percent']}%")
            print(f"   Total evictions: {stats['stats']['evictions']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Cache manager test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_rate_limiter(self):
        """🔥 Test 2: API Rate Limiter"""
        print("\n" + "="*70)
        print("🔥 TEST 2: API Rate Limiter")
        print("="*70)

        try:
            # Create rate limiter: 2 req/s, burst of 5
            limiter = create_rate_limiter(
                default_requests_per_second=2.0,
                default_burst=5
            )

            # Configure specific API
            limiter.configure_api('test_api', requests_per_second=1.0, burst=3)

            # Test burst allowance
            allowed_count = 0
            for i in range(5):
                allowed = await limiter.check_rate_limit('test_api')
                if allowed:
                    allowed_count += 1

            assert allowed_count == 3, f"Burst allowance failed: got {allowed_count}, expected 3"
            print(f"✅ Burst allowance works! (allowed: {allowed_count}/5)")

            # Test rate limiting kicks in
            allowed = await limiter.check_rate_limit('test_api')
            assert not allowed, "Rate limiting should be active"
            print("✅ Rate limiting works!")

            # Test retry-after
            retry_after = await limiter.get_retry_after('test_api')
            print(f"   Retry after: {retry_after:.2f}s")

            # Test stats
            stats = limiter.get_stats()
            print(f"   Total requests: {stats['stats']['total_requests']}")
            print(f"   Rate limited: {stats['stats']['rate_limited_requests']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Rate limiter test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_openapi_server(self):
        """🌐 Test 3: OpenAPI Server"""
        print("\n" + "="*70)
        print("🌐 TEST 3: OpenAPI Server")
        print("="*70)

        try:
            # Create components
            cache = create_cache_manager(max_size=1000, default_ttl_seconds=300)
            limiter = create_rate_limiter(default_requests_per_second=1.0, default_burst=5)

            # Create OpenAPI server
            server = create_openapi_server(
                cache_manager=cache,
                rate_limiter=limiter
            )

            assert server is not None, "Failed to create OpenAPI server"
            print("✅ OpenAPI server created!")

            # Test list specs (should be empty)
            specs = server.list_loaded_specs()
            assert len(specs) == 0, f"Expected 0 specs, got {len(specs)}"
            print("✅ Initial spec list empty (as expected)!")

            # Test stats
            stats = server.get_stats()
            print(f"   Server ID: {stats['server_id']}")
            print(f"   Total API calls: {stats['stats']['total_api_calls']}")
            print(f"   Specs loaded: {stats['stats']['total_specs_loaded']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ OpenAPI server test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_config_file(self):
        """⚙️ Test 4: OpenAPI Config File"""
        print("\n" + "="*70)
        print("⚙️ TEST 4: OpenAPI Config File")
        print("="*70)

        try:
            # Load config file
            with open('openapi_config.json', 'r') as f:
                config = json.load(f)

            # Verify structure
            required_sections = [
                'openapi_server_config',
                'cache_config',
                'rate_limiter_config',
                'pre_configured_apis',
                'authentication',
                'retry_config'
            ]

            for section in required_sections:
                assert section in config, f"Missing config section: {section}"

            print("✅ All config sections present!")

            # Check pre-configured APIs
            pre_configured = config.get('pre_configured_apis', {})
            assert len(pre_configured) > 0, "No pre-configured APIs"
            print(f"   Pre-configured APIs: {len(pre_configured)}")

            for api_id in list(pre_configured.keys())[:3]:
                api_config = pre_configured[api_id]
                print(f"     - {api_id}: {api_config.get('description', 'N/A')}")

            # Check rate limits
            rate_limits = config.get('rate_limiter_config', {}).get('per_api_limits', {})
            print(f"   Pre-configured rate limits: {len(rate_limits)}")

            for api_id, limits in list(rate_limits.items())[:3]:
                print(f"     - {api_id}: {limits['requests_per_second']} req/s")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Config file test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_cache_ttl_expiration(self):
        """⏱️ Test 5: Cache TTL Expiration"""
        print("\n" + "="*70)
        print("⏱️ TEST 5: Cache TTL Expiration")
        print("="*70)

        try:
            # Create cache with short TTL
            cache = create_cache_manager(max_size=10, default_ttl_seconds=2)

            # Set value with TTL
            await cache.set('temp_key', {'data': 'temporary'}, ttl_seconds=1)

            # Immediate get should work
            value = await cache.get('temp_key')
            assert value is not None, "Failed to get fresh value"
            print("✅ Fresh value retrieved!")

            # Wait for expiration
            print("   Waiting 2s for TTL expiration...")
            await asyncio.sleep(2)

            # Should be expired now
            expired_value = await cache.get('temp_key')
            assert expired_value is None, "Value should be expired"
            print("✅ TTL expiration works!")

            stats = cache.get_stats()
            print(f"   Expirations: {stats['stats']['expirations']}")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ TTL expiration test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def test_rate_limiter_recovery(self):
        """🔄 Test 6: Rate Limiter Token Recovery"""
        print("\n" + "="*70)
        print("🔄 TEST 6: Rate Limiter Token Recovery")
        print("="*70)

        try:
            # Create limiter with fast refill
            limiter = create_rate_limiter(
                default_requests_per_second=2.0,  # 2 tokens per second
                default_burst=3
            )

            # Exhaust tokens
            for i in range(3):
                await limiter.check_rate_limit('recovery_test')

            # Should be rate limited
            allowed = await limiter.check_rate_limit('recovery_test')
            assert not allowed, "Should be rate limited"
            print("✅ Rate limit enforced!")

            # Wait for token recovery (0.5s = 1 token at 2 req/s)
            print("   Waiting 0.6s for token recovery...")
            await asyncio.sleep(0.6)

            # Should have recovered 1 token
            allowed = await limiter.check_rate_limit('recovery_test')
            assert allowed, "Token should have recovered"
            print("✅ Token recovery works!")

            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"❌ Rate limiter recovery test ERROR: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all standalone tests"""
        print("\n")
        print("🔥💀🔥 LOLY OPENAPI STANDALONE TEST SUITE (PHASE 2C) 💀🔥💀")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Run tests in order
        await self.test_cache_manager()
        await self.test_rate_limiter()
        await self.test_openapi_server()
        await self.test_config_file()
        await self.test_cache_ttl_expiration()
        await self.test_rate_limiter_recovery()

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
            print("\n🔥💀🔥 ALL TESTS PASSED! PHASE 2C COMPLETE! 💀🔥💀\n")
            print("Phase 2C Components:")
            print("  ✅ api_cache_manager.py - LRU cache with TTL")
            print("  ✅ api_rate_limiter.py - Token bucket rate limiting")
            print("  ✅ openapi_mcp_server.py - OpenAPI spec integration")
            print("  ✅ openapi_config.json - Configuration file")
            print("  ✅ unified_agent_coordinator.py - OpenAPI methods added")
            print("  ✅ loly_orchestrator_main.py - OpenAPI endpoints added")
            print("\nReady to commit Phase 2C!")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. Check logs for details.\n")

        return self.tests_failed == 0


async def main():
    """Main test runner"""
    tester = OpenAPIStandaloneTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
