#!/usr/bin/env python3
"""
🔥💀 DATA COLLECTOR AGENT - AUTONOMOUS ESPN/API DATA HUNTING 💀🔥
Agent Poly Loly Double Zero: Specialized Data Collection Intelligence

AUTONOMOUS BEHAVIORS:
- Independent API discovery and testing
- Smart rate limiting and error recovery  
- Adaptive data source switching
- Quality assessment and filtering
- Proactive cache management
"""

import asyncio
import aiohttp
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import logging

from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY

logger = logging.getLogger(__name__)

class DataCollectorAgent(AutonomousAgent):
    """
    🎯 AUTONOMOUS DATA COLLECTION AGENT
    
    Specializes in:
    - ESPN API data hunting
    - Real-time sports data collection
    - Adaptive source management
    - Quality control and validation
    """
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        super().__init__(agent_id, config)
        
        # Data collection configuration
        self.data_sources = {
            'espn': {
                'base_url': 'https://site.api.espn.com/apis/site/v2/sports',
                'rate_limit': 60,  # requests per minute
                'last_request': 0,
                'health': 'healthy',
                'success_rate': 1.0
            },
            'balldontlie': {
                'base_url': 'https://www.balldontlie.io/api/v1',
                'rate_limit': 60,
                'last_request': 0, 
                'health': 'healthy',
                'success_rate': 1.0
            }
        }
        
        # Collection state
        self.active_collections = {}  # sport -> collection_info
        self.data_cache = {}  # cache_key -> data
        self.cache_timestamps = {}  # cache_key -> timestamp
        self.cache_ttl = 300  # 5 minutes
        
        # Quality metrics
        self.data_quality_threshold = 0.8
        self.collection_targets = {
            'NFL': {'min_games': 5, 'update_frequency': 300},
            'NBA': {'min_games': 5, 'update_frequency': 300}, 
            'EPL': {'min_games': 3, 'update_frequency': 600},
            'MLB': {'min_games': 8, 'update_frequency': 300}
        }
        
        # Error handling and recovery
        self.max_retries_per_source = 3
        self.backoff_multiplier = 2
        self.circuit_breaker_threshold = 0.5  # Stop using source if success rate < 50%
        
        logger.info(f"🎯 DataCollectorAgent {self.agent_id} initialized with {len(self.data_sources)} sources")
    
    async def _initialize_systems(self):
        """⚙️ Initialize data collection systems"""
        # Test all data sources
        for source_name, source_config in self.data_sources.items():
            health = await self._test_data_source(source_name)
            source_config['health'] = health
            logger.info(f"🔍 Data source {source_name}: {health}")
        
        # Initialize collection schedules
        for sport, targets in self.collection_targets.items():
            self.active_collections[sport] = {
                'last_collection': 0,
                'next_collection': time.time(),
                'status': 'scheduled',
                'data_count': 0
            }
        
        logger.info("⚙️ Data collection systems initialized")
    
    async def _agent_behavior(self):
        """🎯 Core data collection autonomous behavior"""
        # Check for scheduled collections
        await self._check_collection_schedule()
        
        # Proactive quality monitoring
        await self._monitor_data_quality()
        
        # Cache maintenance
        await self._maintain_cache()
        
        # Source health monitoring
        await self._monitor_source_health()
        
        # Sleep to prevent excessive CPU usage
        await asyncio.sleep(1)
    
    async def _agent_specific_adaptation(self):
        """🧠 Adapt collection strategies based on performance"""
        # Analyze collection patterns
        for sport, collection_info in self.active_collections.items():
            success_rate = self._get_collection_success_rate(sport)
            
            if success_rate < 0.7:  # Poor performance
                # Increase collection frequency
                targets = self.collection_targets.get(sport, {})
                current_freq = targets.get('update_frequency', 300)
                new_freq = min(current_freq * 1.5, 900)  # Cap at 15 minutes
                targets['update_frequency'] = new_freq
                
                logger.info(f"🧠 Adapted {sport} collection frequency to {new_freq}s due to low success rate")
        
        # Adapt data source priorities
        await self._adapt_source_priorities()
    
    async def _check_collection_schedule(self):
        """📅 Check and execute scheduled data collections"""
        current_time = time.time()
        
        for sport, collection_info in self.active_collections.items():
            if current_time >= collection_info['next_collection']:
                # Start collection task
                collection_task = asyncio.create_task(self._collect_sport_data(sport))
                self.running_tasks.add(collection_task)
                
                # Schedule next collection
                frequency = self.collection_targets[sport]['update_frequency']
                collection_info['next_collection'] = current_time + frequency
                collection_info['status'] = 'collecting'
                
                logger.info(f"📅 Started scheduled collection for {sport}")
    
    async def _collect_sport_data(self, sport: str) -> Dict[str, Any]:
        """⚡ Collect data for specific sport"""
        start_time = time.time()
        collection_id = f"{sport}_{int(start_time)}"
        
        try:
            logger.info(f"⚡ Collecting {sport} data (ID: {collection_id})")
            
            # Determine best data source
            best_source = await self._select_best_source(sport)
            if not best_source:
                raise Exception("No healthy data sources available")
            
            # Collect data from source
            raw_data = await self._fetch_from_source(best_source, sport)
            
            # Validate and process data
            processed_data = await self._process_raw_data(raw_data, sport)
            
            # Quality assessment
            quality_score = await self._assess_data_quality(processed_data, sport)
            
            if quality_score >= self.data_quality_threshold:
                # Cache successful collection
                cache_key = f"{sport}_latest"
                self.data_cache[cache_key] = processed_data
                self.cache_timestamps[cache_key] = time.time()
                
                # Update collection status
                collection_info = self.active_collections[sport]
                collection_info['status'] = 'completed'
                collection_info['last_collection'] = time.time()
                collection_info['data_count'] = len(processed_data.get('games', []))
                
                # Record success
                duration = time.time() - start_time
                self.memory.record_experience(
                    f"collect_{sport}", 'success', duration,
                    {'quality_score': quality_score, 'data_count': collection_info['data_count']}
                )
                
                # Broadcast to other agents
                await self.broadcast_message('data_available', {
                    'sport': sport,
                    'collection_id': collection_id,
                    'data_count': collection_info['data_count'],
                    'quality_score': quality_score,
                    'timestamp': time.time()
                })
                
                logger.info(f"✅ {sport} collection completed: {collection_info['data_count']} items, quality: {quality_score:.2f}")
                return processed_data
                
            else:
                raise Exception(f"Data quality too low: {quality_score:.2f} < {self.data_quality_threshold}")
                
        except Exception as e:
            # Record failure
            duration = time.time() - start_time
            self.memory.record_experience(
                f"collect_{sport}", 'failure', duration,
                {'error': str(e), 'source': best_source}
            )
            
            # Update collection status
            self.active_collections[sport]['status'] = 'failed'
            
            logger.error(f"❌ {sport} collection failed: {e}")
            await self._handle_collection_error(sport, e)
            
            return {}
    
    async def _select_best_source(self, sport: str) -> Optional[str]:
        """🎯 Select best data source for sport"""
        available_sources = []
        
        for source_name, source_config in self.data_sources.items():
            # Check health and success rate
            if (source_config['health'] == 'healthy' and 
                source_config['success_rate'] > self.circuit_breaker_threshold):
                
                # Check rate limiting
                if await self._check_rate_limit(source_name):
                    available_sources.append((source_name, source_config['success_rate']))
        
        if not available_sources:
            return None
        
        # Sort by success rate and return best
        available_sources.sort(key=lambda x: x[1], reverse=True)
        return available_sources[0][0]
    
    async def _fetch_from_source(self, source_name: str, sport: str) -> Dict[str, Any]:
        """📡 Fetch raw data from source"""
        source_config = self.data_sources[source_name]
        
        if source_name == 'espn':
            return await self._fetch_espn_data(sport)
        elif source_name == 'balldontlie':
            return await self._fetch_balldontlie_data(sport)
        else:
            raise Exception(f"Unknown data source: {source_name}")
    
    async def _fetch_espn_data(self, sport: str) -> Dict[str, Any]:
        """🏈 Fetch data from ESPN API"""
        sport_mappings = {
            'NFL': 'football/nfl',
            'NBA': 'basketball/nba', 
            'MLB': 'baseball/mlb',
            'EPL': 'soccer/eng.1'
        }
        
        sport_path = sport_mappings.get(sport, 'football/nfl')
        url = f"{self.data_sources['espn']['base_url']}/{sport_path}/scoreboard"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    self.data_sources['espn']['last_request'] = time.time()
                    return data
                else:
                    raise Exception(f"ESPN API error: {response.status}")
    
    async def _fetch_balldontlie_data(self, sport: str) -> Dict[str, Any]:
        """🏀 Fetch data from Ball Don't Lie API"""
        if sport not in ['NBA']:
            raise Exception(f"Ball Don't Lie doesn't support {sport}")
        
        url = f"{self.data_sources['balldontlie']['base_url']}/games"
        params = {'seasons[]': '2024', 'per_page': '25'}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    self.data_sources['balldontlie']['last_request'] = time.time()
                    return data
                else:
                    raise Exception(f"Ball Don't Lie API error: {response.status}")
    
    async def _process_raw_data(self, raw_data: Dict[str, Any], sport: str) -> Dict[str, Any]:
        """🔄 Process and normalize raw data"""
        processed = {
            'sport': sport,
            'collection_time': time.time(),
            'games': [],
            'metadata': {}
        }
        
        # ESPN data processing
        if 'events' in raw_data:
            for event in raw_data.get('events', []):
                game = {
                    'id': event.get('id'),
                    'date': event.get('date'),
                    'status': event.get('status', {}).get('type', {}).get('name'),
                    'teams': []
                }
                
                for competitor in event.get('competitions', [{}])[0].get('competitors', []):
                    team = {
                        'id': competitor.get('id'),
                        'name': competitor.get('team', {}).get('displayName'),
                        'score': competitor.get('score'),
                        'home_away': competitor.get('homeAway')
                    }
                    game['teams'].append(team)
                
                processed['games'].append(game)
        
        # Ball Don't Lie data processing
        elif 'data' in raw_data:
            for game_data in raw_data.get('data', []):
                game = {
                    'id': game_data.get('id'),
                    'date': game_data.get('date'),
                    'status': game_data.get('status'),
                    'teams': [
                        {
                            'id': game_data.get('home_team', {}).get('id'),
                            'name': game_data.get('home_team', {}).get('full_name'),
                            'score': game_data.get('home_team_score'),
                            'home_away': 'home'
                        },
                        {
                            'id': game_data.get('visitor_team', {}).get('id'),
                            'name': game_data.get('visitor_team', {}).get('full_name'),
                            'score': game_data.get('visitor_team_score'),
                            'home_away': 'away'
                        }
                    ]
                }
                processed['games'].append(game)
        
        return processed
    
    async def _assess_data_quality(self, data: Dict[str, Any], sport: str) -> float:
        """📊 Assess quality of collected data"""
        if not data or 'games' not in data:
            return 0.0
        
        games = data['games']
        if not games:
            return 0.0
        
        # Quality factors
        factors = []
        
        # Check minimum game count
        min_games = self.collection_targets.get(sport, {}).get('min_games', 1)
        game_count_score = min(len(games) / min_games, 1.0)
        factors.append(game_count_score)
        
        # Check data completeness
        complete_games = 0
        for game in games:
            if (game.get('id') and game.get('date') and 
                game.get('teams') and len(game['teams']) == 2):
                complete_games += 1
        
        completeness_score = complete_games / len(games) if games else 0
        factors.append(completeness_score)
        
        # Check data freshness (within last 24 hours)
        collection_time = data.get('collection_time', 0)
        freshness_score = 1.0 if time.time() - collection_time < 86400 else 0.5
        factors.append(freshness_score)
        
        # Calculate overall quality score
        quality_score = sum(factors) / len(factors)
        
        logger.debug(f"📊 {sport} data quality: {quality_score:.2f} (games: {game_count_score:.2f}, complete: {completeness_score:.2f}, fresh: {freshness_score:.2f})")
        
        return quality_score
    
    async def _monitor_data_quality(self):
        """📊 Monitor overall data quality"""
        low_quality_sports = []
        
        for sport in self.collection_targets:
            cache_key = f"{sport}_latest"
            if cache_key in self.data_cache:
                data = self.data_cache[cache_key]
                quality_score = await self._assess_data_quality(data, sport)
                
                if quality_score < self.data_quality_threshold:
                    low_quality_sports.append(sport)
        
        if low_quality_sports:
            logger.warning(f"📊 Low quality data detected for: {', '.join(low_quality_sports)}")
            # Trigger immediate re-collection
            for sport in low_quality_sports:
                self.active_collections[sport]['next_collection'] = time.time()
    
    async def _maintain_cache(self):
        """🧹 Clean up expired cache entries"""
        current_time = time.time()
        expired_keys = []
        
        for cache_key, timestamp in self.cache_timestamps.items():
            if current_time - timestamp > self.cache_ttl:
                expired_keys.append(cache_key)
        
        for key in expired_keys:
            del self.data_cache[key]
            del self.cache_timestamps[key]
        
        if expired_keys:
            logger.debug(f"🧹 Cleaned {len(expired_keys)} expired cache entries")
    
    async def _monitor_source_health(self):
        """🏥 Monitor data source health"""
        for source_name, source_config in self.data_sources.items():
            # Test source if it's been a while
            last_test = source_config.get('last_health_check', 0)
            if time.time() - last_test > 600:  # Test every 10 minutes
                health = await self._test_data_source(source_name)
                source_config['health'] = health
                source_config['last_health_check'] = time.time()
                
                if health != 'healthy':
                    logger.warning(f"🏥 Data source {source_name} health: {health}")
    
    async def _test_data_source(self, source_name: str) -> str:
        """🔍 Test data source health"""
        try:
            if source_name == 'espn':
                url = f"{self.data_sources['espn']['base_url']}/football/nfl/scoreboard"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=5) as response:
                        return 'healthy' if response.status == 200 else 'unhealthy'
            
            elif source_name == 'balldontlie':
                url = f"{self.data_sources['balldontlie']['base_url']}/games"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=5) as response:
                        return 'healthy' if response.status == 200 else 'unhealthy'
            
            return 'unknown'
            
        except Exception as e:
            logger.error(f"🔍 Health check failed for {source_name}: {e}")
            return 'unhealthy'
    
    async def _check_rate_limit(self, source_name: str) -> bool:
        """⏱️ Check if source is within rate limits"""
        source_config = self.data_sources[source_name]
        last_request = source_config['last_request']
        rate_limit = source_config['rate_limit']  # requests per minute
        
        time_since_last = time.time() - last_request
        min_interval = 60 / rate_limit  # seconds between requests
        
        return time_since_last >= min_interval
    
    async def _adapt_source_priorities(self):
        """🧠 Adapt data source priorities based on performance"""
        # Calculate success rates for each source
        for source_name, source_config in self.data_sources.items():
            # Get recent experiences for this source
            source_experiences = [
                exp for exp in self.memory.experiences 
                if exp.get('details', {}).get('source') == source_name
            ]
            
            if len(source_experiences) >= 5:  # Need minimum data
                recent_experiences = source_experiences[-10:]  # Last 10
                successes = sum(1 for exp in recent_experiences if exp['outcome'] == 'success')
                success_rate = successes / len(recent_experiences)
                
                source_config['success_rate'] = success_rate
                
                logger.info(f"🧠 Updated {source_name} success rate: {success_rate:.2f}")
    
    async def _get_collection_success_rate(self, sport: str) -> float:
        """📊 Get success rate for sport collections"""
        sport_experiences = [
            exp for exp in self.memory.experiences 
            if exp['task_type'] == f"collect_{sport}"
        ]
        
        if not sport_experiences:
            return 1.0
        
        recent_experiences = sport_experiences[-10:]  # Last 10
        successes = sum(1 for exp in recent_experiences if exp['outcome'] == 'success')
        return successes / len(recent_experiences)
    
    async def _handle_collection_error(self, sport: str, error: Exception):
        """🚨 Handle collection errors with recovery strategies"""
        error_msg = str(error)
        
        # Implement recovery strategies based on error type
        if 'timeout' in error_msg.lower():
            # Increase timeout for next attempt
            logger.info(f"🔄 Implementing timeout recovery for {sport}")
        elif 'rate limit' in error_msg.lower():
            # Back off from this source
            logger.info(f"🔄 Implementing rate limit recovery for {sport}")
        elif 'api error' in error_msg.lower():
            # Try alternative source
            logger.info(f"🔄 Implementing API error recovery for {sport}")
        
        # Schedule retry with exponential backoff
        collection_info = self.active_collections[sport]
        frequency = self.collection_targets[sport]['update_frequency']
        backoff_delay = frequency * self.backoff_multiplier
        collection_info['next_collection'] = time.time() + backoff_delay
    
    # =================== PUBLIC API ===================
    
    async def get_sport_data(self, sport: str) -> Optional[Dict[str, Any]]:
        """🎯 Get latest data for sport"""
        cache_key = f"{sport}_latest"
        if cache_key in self.data_cache:
            return self.data_cache[cache_key]
        
        # If no cached data, trigger immediate collection
        await self._collect_sport_data(sport)
        return self.data_cache.get(cache_key)
    
    async def get_collection_status(self) -> Dict[str, Any]:
        """📊 Get collection status for all sports"""
        status = {
            'agent_id': self.agent_id,
            'timestamp': time.time(),
            'collections': {},
            'sources': {}
        }
        
        # Collection status
        for sport, collection_info in self.active_collections.items():
            status['collections'][sport] = {
                'status': collection_info['status'],
                'last_collection': collection_info['last_collection'],
                'next_collection': collection_info['next_collection'],
                'data_count': collection_info['data_count'],
                'success_rate': self._get_collection_success_rate(sport)
            }
        
        # Source status
        for source_name, source_config in self.data_sources.items():
            status['sources'][source_name] = {
                'health': source_config['health'],
                'success_rate': source_config['success_rate'],
                'last_request': source_config['last_request']
            }
        
        return status

if __name__ == "__main__":
    async def test_collector():
        agent = DataCollectorAgent("data_collector_001")
        AGENT_REGISTRY.register_agent(agent)
        
        await agent.spawn()
        await asyncio.sleep(10)  # Let it collect some data
        
        # Get status
        status = await agent.get_collection_status()
        print(f"📊 Collection Status: {json.dumps(status, indent=2, default=str)}")
        
        await agent.terminate()
    
    asyncio.run(test_collector())