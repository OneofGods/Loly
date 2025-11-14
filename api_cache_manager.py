#!/usr/bin/env python3
"""
🔥💀🔥 API CACHE MANAGER - SPEED UP LOLY'S API CALLS! 💀🔥💀

Intelligent caching for API responses to reduce external calls!

FEATURES:
- In-memory cache (fast!)
- TTL (time-to-live) expiration
- LRU eviction when cache is full
- Cache size limits
- Cache statistics
- Selective caching (GET only)
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from collections import OrderedDict
import time

logger = logging.getLogger(__name__)


class APICacheManager:
    """
    💾 API Cache Manager

    Fast in-memory cache for API responses with TTL and LRU eviction
    """

    def __init__(self, max_size: int = 1000, default_ttl_seconds: int = 300):
        self.cache_id = f"api_cache_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Cache storage (OrderedDict for LRU)
        self.cache: OrderedDict[str, Dict[str, Any]] = OrderedDict()

        # Configuration
        self.max_size = max_size
        self.default_ttl = default_ttl_seconds

        # Statistics
        self.stats = {
            'total_gets': 0,
            'cache_hits': 0,
            'cache_misses': 0,
            'total_sets': 0,
            'evictions': 0,
            'expirations': 0
        }

        logger.info(f"💾 API Cache Manager initialized (max_size={max_size}, ttl={default_ttl_seconds}s)")

    async def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache

        Returns None if not found or expired
        """
        self.stats['total_gets'] += 1

        if key not in self.cache:
            self.stats['cache_misses'] += 1
            return None

        # Check expiration
        entry = self.cache[key]
        if time.time() > entry['expires_at']:
            # Expired - remove it
            del self.cache[key]
            self.stats['cache_misses'] += 1
            self.stats['expirations'] += 1
            logger.debug(f"💾 Cache expired: {key}")
            return None

        # Cache hit - move to end (LRU)
        self.cache.move_to_end(key)
        self.stats['cache_hits'] += 1

        logger.debug(f"💾 Cache hit: {key}")
        return entry['value']

    async def set(self, key: str, value: Any, ttl_seconds: int = None):
        """
        Set value in cache with TTL

        Args:
            key: Cache key
            value: Value to cache
            ttl_seconds: Time to live (defaults to default_ttl)
        """
        self.stats['total_sets'] += 1

        ttl = ttl_seconds if ttl_seconds is not None else self.default_ttl
        expires_at = time.time() + ttl

        # If key exists, remove it first (will be re-added at end)
        if key in self.cache:
            del self.cache[key]

        # Check if cache is full
        if len(self.cache) >= self.max_size:
            # Evict oldest (first item in OrderedDict)
            evicted_key, _ = self.cache.popitem(last=False)
            self.stats['evictions'] += 1
            logger.debug(f"💾 Cache evicted (LRU): {evicted_key}")

        # Add to cache
        self.cache[key] = {
            'value': value,
            'expires_at': expires_at,
            'created_at': time.time()
        }

        logger.debug(f"💾 Cache set: {key} (ttl={ttl}s)")

    async def delete(self, key: str) -> bool:
        """Delete specific key from cache"""
        if key in self.cache:
            del self.cache[key]
            logger.debug(f"💾 Cache deleted: {key}")
            return True
        return False

    async def clear(self):
        """Clear entire cache"""
        size_before = len(self.cache)
        self.cache.clear()
        logger.info(f"💾 Cache cleared ({size_before} entries)")

    async def cleanup_expired(self):
        """Remove all expired entries"""
        current_time = time.time()
        expired_keys = [
            key for key, entry in self.cache.items()
            if current_time > entry['expires_at']
        ]

        for key in expired_keys:
            del self.cache[key]
            self.stats['expirations'] += 1

        if expired_keys:
            logger.info(f"💾 Cleaned up {len(expired_keys)} expired entries")

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get cache statistics"""
        hit_rate = (self.stats['cache_hits'] / self.stats['total_gets'] * 100) if self.stats['total_gets'] > 0 else 0

        return {
            'cache_id': self.cache_id,
            'current_size': len(self.cache),
            'max_size': self.max_size,
            'default_ttl_seconds': self.default_ttl,
            'stats': self.stats,
            'hit_rate_percent': round(hit_rate, 2),
            'timestamp': datetime.now().isoformat()
        }

    def get_cache_info(self) -> Dict[str, Any]:
        """📋 Get detailed cache information"""
        entries = []
        current_time = time.time()

        for key, entry in list(self.cache.items())[:20]:  # First 20 entries
            entries.append({
                'key': key,
                'created_at': datetime.fromtimestamp(entry['created_at']).isoformat(),
                'expires_at': datetime.fromtimestamp(entry['expires_at']).isoformat(),
                'ttl_remaining_seconds': max(0, int(entry['expires_at'] - current_time)),
                'is_expired': current_time > entry['expires_at']
            })

        return {
            'cache_id': self.cache_id,
            'total_entries': len(self.cache),
            'entries_sample': entries,
            'timestamp': datetime.now().isoformat()
        }


# =================== FACTORY FUNCTION ===================

def create_cache_manager(max_size: int = 1000, default_ttl_seconds: int = 300) -> APICacheManager:
    """🏭 Create cache manager instance"""
    return APICacheManager(max_size, default_ttl_seconds)


# =================== BACKGROUND CLEANUP TASK ===================

async def start_cache_cleanup_task(cache_manager: APICacheManager, interval_seconds: int = 60):
    """
    🧹 Start background task to cleanup expired entries

    Args:
        cache_manager: Cache manager instance
        interval_seconds: Cleanup interval
    """
    logger.info(f"🧹 Starting cache cleanup task (interval={interval_seconds}s)")

    while True:
        try:
            await asyncio.sleep(interval_seconds)
            await cache_manager.cleanup_expired()
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error(f"❌ Cache cleanup error: {e}")


# =================== TESTING ===================

if __name__ == "__main__":
    async def test_cache_manager():
        print("💾 Testing API Cache Manager!\n")

        cache = create_cache_manager(max_size=5, default_ttl_seconds=5)

        # Test 1: Set and get
        print("1️⃣ Set and Get")
        await cache.set('key1', {'data': 'value1'})
        value = await cache.get('key1')
        print(f"   Retrieved: {value}")

        # Test 2: Cache miss
        print("\n2️⃣ Cache Miss")
        value = await cache.get('nonexistent')
        print(f"   Result: {value}")

        # Test 3: Fill cache (LRU eviction)
        print("\n3️⃣ Fill Cache (LRU eviction)")
        for i in range(10):
            await cache.set(f'key{i}', {'data': f'value{i}'})
        stats = cache.get_stats()
        print(f"   Cache size: {stats['current_size']}/{stats['max_size']}")
        print(f"   Evictions: {stats['stats']['evictions']}")

        # Test 4: Expiration
        print("\n4️⃣ Expiration Test")
        await cache.set('temp', {'data': 'temporary'}, ttl_seconds=2)
        value = await cache.get('temp')
        print(f"   Immediate get: {value}")
        await asyncio.sleep(3)
        value = await cache.get('temp')
        print(f"   After 3s: {value}")

        # Test 5: Stats
        print("\n5️⃣ Cache Stats")
        stats = cache.get_stats()
        print(f"   Hit rate: {stats['hit_rate_percent']}%")
        print(f"   Total gets: {stats['stats']['total_gets']}")
        print(f"   Cache hits: {stats['stats']['cache_hits']}")

        print("\n✅ Cache Manager Test Complete!")

    asyncio.run(test_cache_manager())
