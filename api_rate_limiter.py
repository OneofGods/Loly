#!/usr/bin/env python3
"""
🔥💀🔥 API RATE LIMITER - RESPECT API LIMITS! 💀🔥💀

Token bucket rate limiting for external API calls!

FEATURES:
- Token bucket algorithm
- Per-API rate limiting
- Configurable limits per API
- Automatic token refill
- Rate limit statistics
- Retry-After calculation
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import time

logger = logging.getLogger(__name__)


class TokenBucket:
    """
    🪣 Token Bucket for rate limiting

    Classic token bucket algorithm:
    - Bucket holds N tokens
    - Each request consumes 1 token
    - Tokens refill at fixed rate
    """

    def __init__(self, capacity: int, refill_rate: float):
        """
        Args:
            capacity: Max tokens in bucket
            refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate

        # Current state
        self.tokens = float(capacity)
        self.last_refill = time.time()

    def _refill(self):
        """Refill tokens based on time elapsed"""
        now = time.time()
        time_elapsed = now - self.last_refill

        # Add tokens based on refill rate
        tokens_to_add = time_elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now

    def consume(self, tokens: int = 1) -> bool:
        """
        Try to consume tokens

        Returns True if successful, False if not enough tokens
        """
        self._refill()

        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def get_wait_time(self, tokens: int = 1) -> float:
        """Get seconds to wait until tokens are available"""
        self._refill()

        if self.tokens >= tokens:
            return 0.0

        tokens_needed = tokens - self.tokens
        return tokens_needed / self.refill_rate

    def get_tokens_available(self) -> float:
        """Get current number of tokens available"""
        self._refill()
        return self.tokens


class APIRateLimiter:
    """
    🔥💀🔥 API RATE LIMITER 💀🔥💀

    Manages rate limits for multiple APIs using token buckets
    """

    def __init__(self, default_requests_per_second: float = 1.0, default_burst: int = 5):
        self.limiter_id = f"rate_limiter_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Rate limit configuration
        self.default_rps = default_requests_per_second
        self.default_burst = default_burst

        # Token buckets per API
        self.buckets: Dict[str, TokenBucket] = {}

        # Rate limit configs per API
        self.configs: Dict[str, Dict[str, Any]] = {}

        # Statistics
        self.stats = {
            'total_requests': 0,
            'allowed_requests': 0,
            'rate_limited_requests': 0,
            'apis_tracked': 0
        }

        logger.info(f"🔥 Rate Limiter initialized (default={default_requests_per_second} req/s, burst={default_burst})")

    def configure_api(self, api_id: str, requests_per_second: float, burst: int = None):
        """
        ⚙️ Configure rate limit for specific API

        Args:
            api_id: API identifier
            requests_per_second: Sustained rate limit
            burst: Maximum burst capacity (defaults to 2x RPS)
        """
        if burst is None:
            burst = int(requests_per_second * 2)

        self.configs[api_id] = {
            'requests_per_second': requests_per_second,
            'burst': burst
        }

        # Create token bucket
        self.buckets[api_id] = TokenBucket(capacity=burst, refill_rate=requests_per_second)
        self.stats['apis_tracked'] = len(self.buckets)

        logger.info(f"⚙️ Configured rate limit for {api_id}: {requests_per_second} req/s, burst={burst}")

    async def check_rate_limit(self, api_id: str, tokens: int = 1) -> bool:
        """
        ✅ Check if request is allowed under rate limit

        Args:
            api_id: API identifier
            tokens: Number of tokens to consume (default 1)

        Returns:
            True if allowed, False if rate limited
        """
        self.stats['total_requests'] += 1

        # Get or create bucket
        if api_id not in self.buckets:
            # Use default config
            self.buckets[api_id] = TokenBucket(
                capacity=self.default_burst,
                refill_rate=self.default_rps
            )
            self.stats['apis_tracked'] = len(self.buckets)

        bucket = self.buckets[api_id]

        # Try to consume tokens
        if bucket.consume(tokens):
            self.stats['allowed_requests'] += 1
            return True
        else:
            self.stats['rate_limited_requests'] += 1
            logger.warning(f"⚠️  Rate limited: {api_id}")
            return False

    async def get_retry_after(self, api_id: str, tokens: int = 1) -> float:
        """
        ⏱️ Get seconds to wait before retry

        Args:
            api_id: API identifier
            tokens: Number of tokens needed

        Returns:
            Seconds to wait
        """
        if api_id not in self.buckets:
            return 0.0

        bucket = self.buckets[api_id]
        return bucket.get_wait_time(tokens)

    async def wait_for_rate_limit(self, api_id: str, tokens: int = 1):
        """
        ⏳ Wait until request is allowed

        This will block until tokens are available
        """
        retry_after = await self.get_retry_after(api_id, tokens)

        if retry_after > 0:
            logger.info(f"⏳ Waiting {retry_after:.2f}s for rate limit: {api_id}")
            await asyncio.sleep(retry_after)

    def get_bucket_status(self, api_id: str) -> Optional[Dict[str, Any]]:
        """📊 Get status of specific API's rate limit bucket"""
        if api_id not in self.buckets:
            return None

        bucket = self.buckets[api_id]
        config = self.configs.get(api_id, {
            'requests_per_second': self.default_rps,
            'burst': self.default_burst
        })

        return {
            'api_id': api_id,
            'tokens_available': round(bucket.get_tokens_available(), 2),
            'capacity': bucket.capacity,
            'refill_rate': bucket.refill_rate,
            'config': config,
            'utilization_percent': round((1 - bucket.get_tokens_available() / bucket.capacity) * 100, 2)
        }

    def get_all_bucket_status(self) -> Dict[str, Any]:
        """📊 Get status of all rate limit buckets"""
        return {
            api_id: self.get_bucket_status(api_id)
            for api_id in self.buckets.keys()
        }

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get rate limiter statistics"""
        allowed_rate = (self.stats['allowed_requests'] / self.stats['total_requests'] * 100) if self.stats['total_requests'] > 0 else 0

        return {
            'limiter_id': self.limiter_id,
            'stats': self.stats,
            'allowed_rate_percent': round(allowed_rate, 2),
            'timestamp': datetime.now().isoformat()
        }


# =================== FACTORY FUNCTION ===================

def create_rate_limiter(default_requests_per_second: float = 1.0, default_burst: int = 5) -> APIRateLimiter:
    """🏭 Create rate limiter instance"""
    return APIRateLimiter(default_requests_per_second, default_burst)


# =================== TESTING ===================

if __name__ == "__main__":
    async def test_rate_limiter():
        print("🔥 Testing API Rate Limiter!\n")

        # Create rate limiter: 2 requests per second, burst of 5
        limiter = create_rate_limiter(default_requests_per_second=2.0, default_burst=5)

        # Configure specific API
        limiter.configure_api('github', requests_per_second=1.0, burst=3)

        # Test 1: Burst requests
        print("1️⃣ Burst Requests Test (should allow burst, then rate limit)")
        for i in range(8):
            allowed = await limiter.check_rate_limit('test_api')
            status = "✅ ALLOWED" if allowed else "❌ RATE LIMITED"
            bucket_status = limiter.get_bucket_status('test_api')
            tokens = bucket_status['tokens_available']
            print(f"   Request {i+1}: {status} (tokens: {tokens:.2f})")

        # Test 2: Wait and retry
        print("\n2️⃣ Wait and Retry Test")
        retry_after = await limiter.get_retry_after('test_api')
        print(f"   Retry after: {retry_after:.2f}s")
        await limiter.wait_for_rate_limit('test_api')
        allowed = await limiter.check_rate_limit('test_api')
        print(f"   After wait: {'✅ ALLOWED' if allowed else '❌ RATE LIMITED'}")

        # Test 3: Stats
        print("\n3️⃣ Rate Limiter Stats")
        stats = limiter.get_stats()
        print(f"   Total requests: {stats['stats']['total_requests']}")
        print(f"   Allowed: {stats['stats']['allowed_requests']}")
        print(f"   Rate limited: {stats['stats']['rate_limited_requests']}")
        print(f"   Allowed rate: {stats['allowed_rate_percent']}%")

        # Test 4: Bucket status
        print("\n4️⃣ Bucket Status")
        all_status = limiter.get_all_bucket_status()
        for api_id, status in all_status.items():
            print(f"   {api_id}:")
            print(f"     Tokens: {status['tokens_available']}/{status['capacity']}")
            print(f"     Refill rate: {status['refill_rate']} tokens/s")

        print("\n✅ Rate Limiter Test Complete!")

    asyncio.run(test_rate_limiter())
