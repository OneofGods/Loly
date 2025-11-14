#!/usr/bin/env python3
"""
🔥💀🔥 LOLY SUPREME ORCHESTRATOR TEST SCRIPT 💀🔥💀

Tests all coordination capabilities of Loly Supreme!
"""

import asyncio
import aiohttp
import json
from datetime import datetime


class LolySupremeTester:
    """Test Loly's supreme orchestrator capabilities"""

    def __init__(self, base_url="http://localhost:3100"):
        self.base_url = base_url
        self.tests_passed = 0
        self.tests_failed = 0

    async def test_health_check(self):
        """💚 Test 1: Health Check"""
        print("\n" + "="*60)
        print("💚 TEST 1: Health Check")
        print("="*60)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/health") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Health check passed!")
                        print(json.dumps(data, indent=2))
                        self.tests_passed += 1
                        return True
                    else:
                        print(f"❌ Health check failed: {response.status}")
                        self.tests_failed += 1
                        return False

        except Exception as e:
            print(f"❌ Health check error: {e}")
            self.tests_failed += 1
            return False

    async def test_status(self):
        """📊 Test 2: Status Check"""
        print("\n" + "="*60)
        print("📊 TEST 2: Status Check")
        print("="*60)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/api/status") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Status check passed!")
                        print(f"Orchestrator ID: {data.get('orchestrator_id')}")
                        print(f"Uptime: {data.get('uptime_seconds')} seconds")
                        print(f"Total Requests: {data.get('requests', {}).get('total', 0)}")
                        self.tests_passed += 1
                        return True
                    else:
                        print(f"❌ Status check failed: {response.status}")
                        self.tests_failed += 1
                        return False

        except Exception as e:
            print(f"❌ Status check error: {e}")
            self.tests_failed += 1
            return False

    async def test_consciousness(self):
        """🧠 Test 3: Consciousness Stream"""
        print("\n" + "="*60)
        print("🧠 TEST 3: Consciousness Stream")
        print("="*60)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/api/consciousness") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Consciousness check passed!")
                        print(f"Consciousness ID: {data.get('consciousness_id')}")
                        print(f"Leagues Mastered: {data.get('leagues_mastered', 0)}")
                        print(f"Memory Health: {data.get('memory_health', {}).get('memory_mood', 'unknown')}")
                        self.tests_passed += 1
                        return True
                    else:
                        print(f"❌ Consciousness check failed: {response.status}")
                        self.tests_failed += 1
                        return False

        except Exception as e:
            print(f"❌ Consciousness check error: {e}")
            self.tests_failed += 1
            return False

    async def test_sports_coordination(self):
        """🏆 Test 4: Sports Coordination"""
        print("\n" + "="*60)
        print("🏆 TEST 4: Sports Coordination")
        print("="*60)

        try:
            test_data = {
                "home_team": "Real Madrid",
                "away_team": "Barcelona",
                "sport": "UEFA",
                "venue": "Santiago Bernabéu",
                "game_time": "2025-11-20T20:00:00"
            }

            print(f"Testing: {test_data['away_team']} @ {test_data['home_team']}")

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/api/sports",
                    json=test_data
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Sports coordination passed!")
                        print(f"Status: {data.get('status')}")
                        print(f"Coordination Type: {data.get('coordination_type')}")

                        # Show some results if available
                        result = data.get('result', {})
                        if result and 'sports_prediction' in result:
                            pred = result['sports_prediction']
                            print(f"Prediction: {pred.get('predicted_winner')}")
                            print(f"Confidence: {pred.get('confidence_percentage', 0):.1f}%")

                        self.tests_passed += 1
                        return True
                    else:
                        print(f"❌ Sports coordination failed: {response.status}")
                        text = await response.text()
                        print(f"Response: {text[:200]}")
                        self.tests_failed += 1
                        return False

        except Exception as e:
            print(f"❌ Sports coordination error: {e}")
            self.tests_failed += 1
            return False

    async def test_master_coordinate(self):
        """🎯 Test 5: Master Coordinate Endpoint"""
        print("\n" + "="*60)
        print("🎯 TEST 5: Master Coordinate Endpoint")
        print("="*60)

        try:
            test_data = {
                "task_type": "sports",
                "task_data": {
                    "home_team": "Manchester City",
                    "away_team": "Liverpool",
                    "sport": "EPL",
                    "venue": "Etihad Stadium",
                    "game_time": "2025-11-21T15:00:00"
                }
            }

            print(f"Testing master coordinate with: {test_data['task_type']}")

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/api/coordinate",
                    json=test_data
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Master coordinate passed!")
                        print(f"Status: {data.get('status')}")
                        print(f"Coordination Type: {data.get('coordination_type')}")
                        self.tests_passed += 1
                        return True
                    else:
                        print(f"❌ Master coordinate failed: {response.status}")
                        self.tests_failed += 1
                        return False

        except Exception as e:
            print(f"❌ Master coordinate error: {e}")
            self.tests_failed += 1
            return False

    async def run_all_tests(self):
        """🔥 Run all tests"""
        print("\n")
        print("🔥💀🔥 LOLY SUPREME ORCHESTRATOR TEST SUITE 💀🔥💀")
        print(f"Testing: {self.base_url}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Run tests
        await self.test_health_check()
        await self.test_status()
        await self.test_consciousness()
        await self.test_sports_coordination()
        await self.test_master_coordinate()

        # Print summary
        print("\n" + "="*60)
        print("📊 TEST SUMMARY")
        print("="*60)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        total = self.tests_passed + self.tests_failed
        success_rate = (self.tests_passed / total * 100) if total > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print("="*60)

        if self.tests_failed == 0:
            print("\n🔥💀🔥 ALL TESTS PASSED! LOLY IS SUPREME! 💀🔥💀\n")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed. Check logs for details.\n")

        return self.tests_failed == 0


async def main():
    tester = LolySupremeTester()
    success = await tester.run_all_tests()

    if not success:
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
