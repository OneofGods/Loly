# 🛡️ **API INTEGRATION BEST PRACTICES**

## **🔧 PRODUCTION-GRADE ERROR HANDLING & INTEGRATION PATTERNS**

### **🎯 PURPOSE**
Comprehensive guide for building robust API integrations that survive real-world data variations, based on lessons learned from the UEFA Champions League connectivity breakthrough.

---

## 🔥 **FUNDAMENTAL PRINCIPLES**

### **PRINCIPLE 1: ASSUME NOTHING ABOUT DATA STRUCTURE**
```python
# ❌ DANGEROUS: Assumes nested structure
result = data['season']['type']['name']

# ✅ SAFE: Validates each level
result = safe_get_nested(data, ['season', 'type', 'name'], 'Unknown')
```

### **PRINCIPLE 2: VALIDATE TYPES BEFORE OPERATIONS**
```python
# ❌ DANGEROUS: Assumes dictionary
round_info = season_type.get('name', 'Group Stage')

# ✅ SAFE: Check type first
if isinstance(season_type, dict):
    round_info = season_type.get('name', 'Group Stage')
elif isinstance(season_type, (int, str)):
    round_info = str(season_type)
else:
    round_info = 'Group Stage'
```

### **PRINCIPLE 3: FAIL GRACEFULLY WITH USEFUL FALLBACKS**
```python
# ❌ DANGEROUS: Let errors propagate
def process_team_data(team_data):
    return {
        'name': team_data['displayName'],
        'logo': team_data['logos'][0]['href']
    }

# ✅ SAFE: Graceful degradation
def process_team_data(team_data):
    return {
        'name': team_data.get('displayName', 'Unknown Team'),
        'logo': extract_logo_safely(team_data.get('logos', [])),
        'fallback_used': not team_data.get('displayName')
    }
```

### **PRINCIPLE 4: LOG EVERYTHING FOR DEBUGGING**
```python
# ✅ COMPREHENSIVE LOGGING
def process_api_response(response_data):
    logger.debug(f"🔍 API Response structure: {type(response_data)}")
    logger.debug(f"🔍 API Response keys: {list(response_data.keys()) if isinstance(response_data, dict) else 'Not a dict'}")
    
    try:
        result = extract_data(response_data)
        logger.info(f"✅ Successfully processed API response")
        return result
    except Exception as e:
        logger.error(f"❌ API processing failed: {e}")
        logger.error(f"🔍 Problematic data: {response_data}")
        raise
```

---

## 🛠️ **ROBUST INTEGRATION PATTERNS**

### **PATTERN 1: THE SAFE EXTRACTOR**

```python
def safe_get_nested(data, keys, default=None, log_path=True):
    """
    Safely extract nested values with comprehensive error handling
    
    Args:
        data: Source data structure
        keys: List of keys for nested access ['level1', 'level2', 'level3']
        default: Default value if extraction fails
        log_path: Whether to log the extraction path for debugging
        
    Returns:
        Extracted value or default
    """
    if log_path:
        logger.debug(f"🔍 Extracting path: {' -> '.join(keys)}")
    
    current = data
    path_taken = []
    
    try:
        for i, key in enumerate(keys):
            path_taken.append(key)
            
            if not isinstance(current, dict):
                if log_path:
                    logger.debug(f"🔍 Path blocked at {' -> '.join(path_taken)}: not a dict (type: {type(current)})")
                return default
            
            if key not in current:
                if log_path:
                    logger.debug(f"🔍 Path blocked at {' -> '.join(path_taken)}: key missing")
                return default
            
            current = current[key]
            
            if log_path:
                logger.debug(f"🔍 Path step {i+1}: {key} = {current} (type: {type(current)})")
        
        if log_path:
            logger.debug(f"✅ Successfully extracted: {' -> '.join(keys)} = {current}")
        
        return current
        
    except Exception as e:
        if log_path:
            logger.error(f"❌ Extraction failed at {' -> '.join(path_taken)}: {e}")
        return default
```

### **PATTERN 2: THE TYPE-AWARE PROCESSOR**

```python
def process_with_type_awareness(data, processors_map, default_processor=None):
    """
    Process data based on its actual type, not assumed type
    
    Args:
        data: Data to process
        processors_map: {type: processor_function} mapping
        default_processor: Fallback processor for unknown types
        
    Returns:
        Processed result
    """
    data_type = type(data)
    
    logger.debug(f"🔍 Processing data of type: {data_type}")
    
    if data_type in processors_map:
        processor = processors_map[data_type]
        logger.debug(f"✅ Using specific processor for {data_type}")
        return processor(data)
    
    if default_processor:
        logger.debug(f"⚠️ Using default processor for unknown type {data_type}")
        return default_processor(data)
    
    logger.error(f"❌ No processor available for type {data_type}")
    raise ValueError(f"Unsupported data type: {data_type}")

# Example usage for season processing
def process_season_info(season_data):
    processors = {
        dict: process_dict_season,
        int: process_int_season,
        str: process_str_season,
        type(None): lambda x: 'Unknown Season'
    }
    
    return process_with_type_awareness(
        season_data, 
        processors, 
        default_processor=lambda x: str(x)
    )

def process_dict_season(season_dict):
    if 'type' in season_dict:
        return process_season_type(season_dict['type'])
    return season_dict.get('name', 'Regular Season')

def process_int_season(season_int):
    # ESPN often uses integers for season types
    season_map = {
        13682: 'Champions League',
        1: 'Regular Season',
        2: 'Playoffs'
    }
    return season_map.get(season_int, f'Season {season_int}')

def process_str_season(season_str):
    return season_str.replace('-', ' ').title()
```

### **PATTERN 3: THE RESILIENT API CLIENT**

```python
import asyncio
import aiohttp
from tenacity import retry, stop_after_attempt, wait_exponential

class ResilientAPIClient:
    """
    API client with comprehensive error handling and retry logic
    """
    
    def __init__(self, base_url, timeout=30, max_retries=3):
        self.base_url = base_url
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.max_retries = max_retries
        self.session = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def get_with_retry(self, endpoint, params=None):
        """
        Make GET request with comprehensive error handling
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        logger.debug(f"🌐 API Request: {url}")
        if params:
            logger.debug(f"🔍 Parameters: {params}")
        
        try:
            async with self.session.get(url, params=params) as response:
                
                # Log response status
                logger.debug(f"📡 Response Status: {response.status}")
                
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"✅ API Success: {url} ({len(str(data))} bytes)")
                    return self._validate_response_structure(data, url)
                
                elif response.status == 404:
                    logger.warning(f"⚠️ API Not Found: {url}")
                    return None
                
                elif response.status == 429:
                    logger.warning(f"⚠️ API Rate Limited: {url}")
                    await asyncio.sleep(5)  # Wait before retry
                    raise aiohttp.ClientResponseError(
                        request_info=response.request_info,
                        history=response.history,
                        status=response.status,
                        message="Rate limited"
                    )
                
                else:
                    error_text = await response.text()
                    logger.error(f"❌ API Error {response.status}: {url}")
                    logger.error(f"🔍 Error Response: {error_text[:200]}...")
                    
                    raise aiohttp.ClientResponseError(
                        request_info=response.request_info,
                        history=response.history,
                        status=response.status,
                        message=error_text
                    )
                    
        except asyncio.TimeoutError:
            logger.error(f"⏱️ API Timeout: {url}")
            raise
        
        except aiohttp.ClientError as e:
            logger.error(f"🌐 API Client Error: {url} - {e}")
            raise
        
        except Exception as e:
            logger.error(f"💥 Unexpected API Error: {url} - {e}")
            raise
    
    def _validate_response_structure(self, data, url):
        """
        Validate API response has expected structure
        """
        if not isinstance(data, dict):
            logger.warning(f"⚠️ API returned non-dict: {url} (type: {type(data)})")
            return data
        
        # Log structure for debugging
        logger.debug(f"🔍 Response keys: {list(data.keys())}")
        
        # Basic validation for sports APIs
        if 'events' in data:
            events = data['events']
            if isinstance(events, list):
                logger.debug(f"🎯 Found {len(events)} events")
            else:
                logger.warning(f"⚠️ Events is not a list: {type(events)}")
        
        return data
```

### **PATTERN 4: THE DEFENSIVE PARSER**

```python
class DefensiveDataParser:
    """
    Parser that handles multiple data format variations defensively
    """
    
    def __init__(self, sport_name):
        self.sport_name = sport_name
        self.logger = logging.getLogger(f"{sport_name}_parser")
        
        # Track parsing patterns for learning
        self.pattern_stats = {
            'total_parsed': 0,
            'format_variations': {},
            'error_patterns': {}
        }
    
    def parse_game_data(self, event_data):
        """
        Parse game data with defensive error handling
        """
        self.pattern_stats['total_parsed'] += 1
        
        try:
            # Extract core game information
            game_info = {
                'id': self._extract_game_id(event_data),
                'date_time': self._extract_datetime(event_data),
                'teams': self._extract_teams(event_data),
                'venue': self._extract_venue(event_data),
                'season_info': self._extract_season_info(event_data),
                'status': self._extract_status(event_data)
            }
            
            # Validate required fields
            if not self._validate_required_fields(game_info):
                return None
            
            # Track successful format
            format_key = self._identify_format(event_data)
            self.pattern_stats['format_variations'][format_key] = \
                self.pattern_stats['format_variations'].get(format_key, 0) + 1
            
            return game_info
            
        except Exception as e:
            self.logger.error(f"❌ Failed to parse game data: {e}")
            self._track_error_pattern(event_data, e)
            return None
    
    def _extract_game_id(self, event_data):
        """Extract game ID with fallbacks"""
        candidates = [
            lambda: event_data['id'],
            lambda: event_data['gameId'],
            lambda: event_data['event_id'],
            lambda: str(hash(str(event_data)[:100]))  # Last resort
        ]
        
        for candidate in candidates:
            try:
                game_id = candidate()
                if game_id:
                    return str(game_id)
            except (KeyError, TypeError):
                continue
        
        self.logger.warning("⚠️ No game ID found, generating fallback")
        return f"generated_{hash(str(event_data)[:50])}"
    
    def _extract_teams(self, event_data):
        """Extract team information with multiple format support"""
        teams = []
        
        # Try different path patterns
        team_paths = [
            ['competitions', 0, 'competitors'],
            ['competitors'],
            ['teams'],
            ['participants']
        ]
        
        for path in team_paths:
            try:
                competitors = safe_get_nested(event_data, path, [])
                if competitors and isinstance(competitors, list):
                    
                    for competitor in competitors:
                        team_info = self._extract_single_team(competitor)
                        if team_info:
                            teams.append(team_info)
                    
                    if len(teams) >= 2:  # Found sufficient teams
                        break
                        
            except Exception as e:
                self.logger.debug(f"🔍 Team extraction path {path} failed: {e}")
                continue
        
        if len(teams) < 2:
            self.logger.warning(f"⚠️ Only found {len(teams)} teams, expected 2+")
        
        return teams
    
    def _extract_single_team(self, competitor_data):
        """Extract single team with defensive handling"""
        try:
            team_data = competitor_data.get('team', competitor_data)
            
            # Handle different team name fields
            name_candidates = ['displayName', 'name', 'teamName', 'fullName']
            team_name = None
            
            for candidate in name_candidates:
                if candidate in team_data and team_data[candidate]:
                    team_name = team_data[candidate]
                    break
            
            if not team_name:
                return None
            
            return {
                'name': team_name,
                'short_name': team_data.get('abbreviation', team_name[:3].upper()),
                'logo': self._extract_team_logo(team_data),
                'home_away': competitor_data.get('homeAway', 'neutral'),
                'score': self._extract_score(competitor_data)
            }
            
        except Exception as e:
            self.logger.debug(f"🔍 Single team extraction failed: {e}")
            return None
    
    def _extract_season_info(self, event_data):
        """Extract season info handling format variations"""
        season_data = safe_get_nested(event_data, ['season'], {})
        
        if not season_data:
            return 'Regular Season'
        
        # Handle different season type formats
        season_type = season_data.get('type')
        
        if isinstance(season_type, dict):
            # Old format: {'name': 'Group Stage', 'id': '1'}
            return season_type.get('name', 'Regular Season')
        
        elif isinstance(season_type, int):
            # New ESPN format: integer ID
            slug = season_data.get('slug', '')
            if slug:
                return slug.replace('-', ' ').title()
            
            # Map known integer types
            type_map = {
                1: 'Regular Season',
                2: 'Playoffs',
                3: 'Championship',
                13682: 'Champions League'
            }
            return type_map.get(season_type, f'Season Type {season_type}')
        
        elif isinstance(season_type, str):
            return season_type
        
        else:
            # Fallback to season name or slug
            return season_data.get('name', 
                   season_data.get('slug', 'Regular Season').replace('-', ' ').title())
    
    def _validate_required_fields(self, game_info):
        """Validate that required fields are present and valid"""
        required_fields = ['id', 'teams']
        
        for field in required_fields:
            if not game_info.get(field):
                self.logger.warning(f"⚠️ Missing required field: {field}")
                return False
        
        if len(game_info['teams']) < 2:
            self.logger.warning(f"⚠️ Insufficient teams: {len(game_info['teams'])}")
            return False
        
        return True
    
    def _identify_format(self, event_data):
        """Identify data format for pattern tracking"""
        format_indicators = []
        
        # Check season format
        season_type = safe_get_nested(event_data, ['season', 'type'])
        if isinstance(season_type, dict):
            format_indicators.append('season_dict')
        elif isinstance(season_type, int):
            format_indicators.append('season_int')
        
        # Check competitors path
        if safe_get_nested(event_data, ['competitions', 0, 'competitors']):
            format_indicators.append('competitions_path')
        elif safe_get_nested(event_data, ['competitors']):
            format_indicators.append('direct_competitors')
        
        return '_'.join(format_indicators) or 'unknown_format'
    
    def _track_error_pattern(self, event_data, error):
        """Track error patterns for analysis"""
        error_type = type(error).__name__
        self.pattern_stats['error_patterns'][error_type] = \
            self.pattern_stats['error_patterns'].get(error_type, 0) + 1
        
        # Log structure of problematic data
        self.logger.debug(f"🔍 Error pattern data structure: {list(event_data.keys()) if isinstance(event_data, dict) else type(event_data)}")
    
    def get_parsing_stats(self):
        """Get parsing statistics for monitoring"""
        return {
            'total_parsed': self.pattern_stats['total_parsed'],
            'success_rate': self._calculate_success_rate(),
            'format_variations': self.pattern_stats['format_variations'],
            'error_patterns': self.pattern_stats['error_patterns']
        }
    
    def _calculate_success_rate(self):
        """Calculate parsing success rate"""
        total = self.pattern_stats['total_parsed']
        errors = sum(self.pattern_stats['error_patterns'].values())
        if total == 0:
            return 1.0
        return (total - errors) / total
```

---

## 🚨 **ERROR HANDLING STRATEGIES**

### **STRATEGY 1: LAYERED ERROR HANDLING**

```python
async def process_api_data_with_layers(api_client, endpoint):
    """
    Process API data with multiple error handling layers
    """
    
    # Layer 1: Network/API errors
    try:
        raw_data = await api_client.get_with_retry(endpoint)
    except aiohttp.ClientError as e:
        logger.error(f"🌐 Network error: {e}")
        return create_empty_result("Network error")
    except asyncio.TimeoutError:
        logger.error(f"⏱️ Request timeout")
        return create_empty_result("Timeout")
    
    # Layer 2: Data structure validation
    try:
        validated_data = validate_api_response(raw_data)
    except ValidationError as e:
        logger.error(f"🔍 Data validation error: {e}")
        return create_empty_result("Invalid data structure")
    
    # Layer 3: Business logic processing
    try:
        processed_data = process_business_logic(validated_data)
    except BusinessLogicError as e:
        logger.error(f"💼 Business logic error: {e}")
        return create_fallback_result(validated_data)
    
    # Layer 4: Result formatting
    try:
        formatted_result = format_for_output(processed_data)
        return formatted_result
    except FormattingError as e:
        logger.error(f"📝 Formatting error: {e}")
        return create_minimal_result(processed_data)

def create_empty_result(reason):
    """Create empty result with error information"""
    return {
        'games': [],
        'count': 0,
        'error': reason,
        'timestamp': datetime.utcnow().isoformat()
    }

def create_fallback_result(raw_data):
    """Create fallback result from raw data"""
    return {
        'games': extract_minimal_games(raw_data),
        'count': len(extract_minimal_games(raw_data)),
        'fallback_used': True,
        'timestamp': datetime.utcnow().isoformat()
    }
```

### **STRATEGY 2: CIRCUIT BREAKER PATTERN**

```python
class APICircuitBreaker:
    """
    Circuit breaker for API calls to prevent cascade failures
    """
    
    def __init__(self, failure_threshold=5, recovery_timeout=60, expected_exception=Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
    
    async def call(self, func, *args, **kwargs):
        """
        Execute function with circuit breaker protection
        """
        
        if self.state == 'OPEN':
            if self._should_attempt_reset():
                self.state = 'HALF_OPEN'
                logger.info("🔄 Circuit breaker HALF_OPEN - attempting reset")
            else:
                raise CircuitBreakerOpenError("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
            
        except self.expected_exception as e:
            self._on_failure()
            raise
    
    def _should_attempt_reset(self):
        """Check if enough time has passed to attempt reset"""
        if not self.last_failure_time:
            return True
        
        return (datetime.utcnow() - self.last_failure_time).seconds >= self.recovery_timeout
    
    def _on_success(self):
        """Handle successful call"""
        if self.state == 'HALF_OPEN':
            self.state = 'CLOSED'
            logger.info("✅ Circuit breaker CLOSED - service recovered")
        
        self.failure_count = 0
    
    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = datetime.utcnow()
        
        if self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'
            logger.error(f"🚨 Circuit breaker OPEN - {self.failure_count} failures")

class CircuitBreakerOpenError(Exception):
    """Exception raised when circuit breaker is open"""
    pass

# Usage example
espn_circuit_breaker = APICircuitBreaker(
    failure_threshold=3,
    recovery_timeout=30,
    expected_exception=(aiohttp.ClientError, asyncio.TimeoutError)
)

async def fetch_espn_data_with_breaker(endpoint):
    """Fetch ESPN data with circuit breaker protection"""
    try:
        return await espn_circuit_breaker.call(
            api_client.get_with_retry,
            endpoint
        )
    except CircuitBreakerOpenError:
        logger.warning("🚨 ESPN API circuit breaker is OPEN, using cached data")
        return get_cached_data(endpoint)
```

### **STRATEGY 3: PROGRESSIVE DEGRADATION**

```python
class ProgressiveDegradationHandler:
    """
    Handler that progressively degrades functionality when errors occur
    """
    
    def __init__(self):
        self.degradation_levels = [
            'FULL_FUNCTIONALITY',
            'REDUCED_FEATURES',
            'BASIC_FUNCTIONALITY',
            'MINIMAL_OPERATION',
            'EMERGENCY_MODE'
        ]
        self.current_level = 0
        self.error_counts = {}
        self.degradation_thresholds = {
            'network_errors': 3,
            'data_errors': 5,
            'processing_errors': 7
        }
    
    async def execute_with_degradation(self, operation_name, full_operation, degraded_operations):
        """
        Execute operation with progressive degradation
        
        Args:
            operation_name: Name of the operation
            full_operation: Function for full functionality
            degraded_operations: List of degraded operation functions
        """
        
        try:
            if self.current_level == 0:
                # Full functionality
                result = await full_operation()
                self._on_success(operation_name)
                return result
            
            else:
                # Use degraded operation based on current level
                degraded_func = degraded_operations[min(self.current_level - 1, len(degraded_operations) - 1)]
                result = await degraded_func()
                logger.warning(f"⚠️ Using degraded operation level {self.current_level} for {operation_name}")
                return result
                
        except Exception as e:
            self._on_error(operation_name, e)
            
            # Try progressively more degraded operations
            for i in range(self.current_level, len(degraded_operations)):
                try:
                    result = await degraded_operations[i]()
                    logger.warning(f"⚠️ Fell back to degradation level {i + 1} for {operation_name}")
                    return result
                except Exception as fallback_error:
                    logger.error(f"❌ Degradation level {i + 1} also failed: {fallback_error}")
                    continue
            
            # All operations failed
            logger.error(f"💥 All degradation levels failed for {operation_name}")
            raise
    
    def _on_success(self, operation_name):
        """Handle successful operation"""
        # Gradually recover degradation level
        if self.current_level > 0:
            self.current_level = max(0, self.current_level - 1)
            if self.current_level == 0:
                logger.info(f"✅ Fully recovered functionality for {operation_name}")
    
    def _on_error(self, operation_name, error):
        """Handle operation error"""
        error_type = self._classify_error(error)
        self.error_counts[error_type] = self.error_counts.get(error_type, 0) + 1
        
        # Check if degradation is needed
        for error_category, threshold in self.degradation_thresholds.items():
            if error_category in self.error_counts and self.error_counts[error_category] >= threshold:
                self._degrade_service(error_category)
                break
    
    def _classify_error(self, error):
        """Classify error type for degradation decisions"""
        if isinstance(error, (aiohttp.ClientError, asyncio.TimeoutError)):
            return 'network_errors'
        elif isinstance(error, (KeyError, TypeError, ValueError)):
            return 'data_errors'
        else:
            return 'processing_errors'
    
    def _degrade_service(self, error_category):
        """Degrade service level"""
        old_level = self.current_level
        self.current_level = min(self.current_level + 1, len(self.degradation_levels) - 1)
        
        if self.current_level > old_level:
            logger.warning(f"⬇️ Service degraded to level {self.current_level} ({self.degradation_levels[self.current_level]}) due to {error_category}")

# Usage example
degradation_handler = ProgressiveDegradationHandler()

async def fetch_game_analysis_with_degradation(game_data):
    """Fetch game analysis with progressive degradation"""
    
    # Full functionality: Complete 7D analysis
    async def full_analysis():
        return await perform_complete_7d_analysis(game_data)
    
    # Degraded operations in order of preference
    degraded_operations = [
        lambda: perform_basic_analysis(game_data),  # Level 1
        lambda: perform_statistical_analysis(game_data),  # Level 2
        lambda: perform_simple_analysis(game_data),  # Level 3
        lambda: create_minimal_analysis(game_data)  # Level 4
    ]
    
    return await degradation_handler.execute_with_degradation(
        'game_analysis',
        full_analysis,
        degraded_operations
    )
```

---

## 📊 **MONITORING & OBSERVABILITY**

### **METRICS COLLECTION**

```python
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class APIMetrics:
    """Metrics for API integration monitoring"""
    endpoint: str
    success_count: int = 0
    error_count: int = 0
    avg_response_time: float = 0.0
    last_success: datetime = None
    last_error: datetime = None
    recent_response_times: deque = None
    error_types: Dict[str, int] = None
    
    def __post_init__(self):
        if self.recent_response_times is None:
            self.recent_response_times = deque(maxlen=100)
        if self.error_types is None:
            self.error_types = defaultdict(int)

class APIMonitor:
    """Monitor API integration health and performance"""
    
    def __init__(self):
        self.metrics: Dict[str, APIMetrics] = {}
        self.global_stats = {
            'total_requests': 0,
            'total_errors': 0,
            'uptime_start': datetime.utcnow()
        }
    
    def record_request(self, endpoint: str, success: bool, response_time: float, error_type: str = None):
        """Record API request metrics"""
        
        if endpoint not in self.metrics:
            self.metrics[endpoint] = APIMetrics(endpoint=endpoint)
        
        metric = self.metrics[endpoint]
        self.global_stats['total_requests'] += 1
        
        if success:
            metric.success_count += 1
            metric.last_success = datetime.utcnow()
        else:
            metric.error_count += 1
            metric.last_error = datetime.utcnow()
            metric.error_types[error_type] += 1
            self.global_stats['total_errors'] += 1
        
        # Update response time
        metric.recent_response_times.append(response_time)
        metric.avg_response_time = sum(metric.recent_response_times) / len(metric.recent_response_times)
    
    def get_health_status(self) -> Dict:
        """Get overall health status"""
        now = datetime.utcnow()
        uptime = (now - self.global_stats['uptime_start']).total_seconds()
        
        total_requests = self.global_stats['total_requests']
        total_errors = self.global_stats['total_errors']
        
        success_rate = (total_requests - total_errors) / total_requests if total_requests > 0 else 1.0
        
        return {
            'status': 'healthy' if success_rate >= 0.95 else 'degraded' if success_rate >= 0.8 else 'unhealthy',
            'success_rate': success_rate,
            'total_requests': total_requests,
            'total_errors': total_errors,
            'uptime_seconds': uptime,
            'endpoints': {
                endpoint: {
                    'success_rate': metric.success_count / (metric.success_count + metric.error_count) if (metric.success_count + metric.error_count) > 0 else 1.0,
                    'avg_response_time': metric.avg_response_time,
                    'last_success': metric.last_success.isoformat() if metric.last_success else None,
                    'last_error': metric.last_error.isoformat() if metric.last_error else None,
                    'error_types': dict(metric.error_types)
                }
                for endpoint, metric in self.metrics.items()
            }
        }
    
    def get_alerts(self) -> List[Dict]:
        """Generate alerts based on metrics"""
        alerts = []
        now = datetime.utcnow()
        
        for endpoint, metric in self.metrics.items():
            total_requests = metric.success_count + metric.error_count
            
            if total_requests == 0:
                continue
            
            success_rate = metric.success_count / total_requests
            
            # Error rate alert
            if success_rate < 0.8:
                alerts.append({
                    'type': 'high_error_rate',
                    'endpoint': endpoint,
                    'success_rate': success_rate,
                    'severity': 'critical' if success_rate < 0.5 else 'warning'
                })
            
            # Response time alert
            if metric.avg_response_time > 10.0:
                alerts.append({
                    'type': 'slow_response',
                    'endpoint': endpoint,
                    'avg_response_time': metric.avg_response_time,
                    'severity': 'critical' if metric.avg_response_time > 30.0 else 'warning'
                })
            
            # Stale data alert
            if metric.last_success and (now - metric.last_success).total_seconds() > 300:  # 5 minutes
                alerts.append({
                    'type': 'stale_data',
                    'endpoint': endpoint,
                    'last_success': metric.last_success.isoformat(),
                    'severity': 'warning'
                })
        
        return alerts

# Global monitor instance
api_monitor = APIMonitor()

def track_api_call(endpoint: str):
    """Decorator to track API calls"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            success = False
            error_type = None
            
            try:
                result = await func(*args, **kwargs)
                success = True
                return result
            except Exception as e:
                error_type = type(e).__name__
                raise
            finally:
                response_time = time.time() - start_time
                api_monitor.record_request(endpoint, success, response_time, error_type)
        
        return wrapper
    return decorator

# Usage example
@track_api_call('espn_uefa_champions_league')
async def fetch_uefa_games():
    """Fetch UEFA games with monitoring"""
    # Your API call logic here
    pass
```

---

## 🎯 **TESTING STRATEGIES**

### **CONTRACT TESTING**

```python
import pytest
from unittest.mock import Mock, patch
from hypothesis import given, strategies as st

class APIContractTests:
    """Test API integration contracts"""
    
    def test_espn_response_structure_validation(self):
        """Test that ESPN API response validation works"""
        
        # Valid response structure
        valid_response = {
            'events': [
                {
                    'id': '12345',
                    'date': '2025-09-17T19:00:00Z',
                    'season': {
                        'type': 13682,
                        'slug': 'champions-league'
                    },
                    'competitions': [{
                        'competitors': [
                            {
                                'team': {'displayName': 'Real Madrid'},
                                'homeAway': 'home'
                            },
                            {
                                'team': {'displayName': 'Manchester City'},
                                'homeAway': 'away'
                            }
                        ]
                    }]
                }
            ]
        }
        
        is_valid, error_msg, events = validate_espn_response(valid_response)
        assert is_valid
        assert len(events) == 1
        
        # Invalid response structures
        invalid_responses = [
            {},  # Missing events
            {'events': 'not_a_list'},  # Events not a list
            {'events': []},  # Empty events (valid but should be noted)
            'not_a_dict',  # Not a dictionary
            None  # None response
        ]
        
        for invalid_response in invalid_responses:
            is_valid, error_msg, events = validate_espn_response(invalid_response)
            if invalid_response == {'events': []}:
                assert is_valid  # Empty is valid
                assert len(events) == 0
            else:
                assert not is_valid
                assert error_msg
    
    @given(st.dictionaries(
        st.text(min_size=1, max_size=20),
        st.one_of(st.integers(), st.text(), st.dictionaries(st.text(), st.text()))
    ))
    def test_safe_get_nested_with_random_data(self, random_data):
        """Test safe_get_nested with random data structures"""
        
        # Should never crash, always return default for invalid paths
        result = safe_get_nested(random_data, ['nonexistent', 'path'], 'default')
        assert result == 'default'
        
        # Should handle any structure gracefully
        result = safe_get_nested(random_data, [], 'default')
        assert result == random_data  # Empty path returns original data
    
    def test_season_info_extraction_variations(self):
        """Test season info extraction with known variations"""
        
        test_cases = [
            # New ESPN format
            {
                'input': {'season': {'type': 13682, 'slug': 'champions-league-2024-25'}},
                'expected': 'Champions League 2024 25'
            },
            # Old format
            {
                'input': {'season': {'type': {'name': 'Group Stage'}}},
                'expected': 'Group Stage'
            },
            # String type
            {
                'input': {'season': {'type': 'playoffs'}},
                'expected': 'playoffs'
            },
            # Missing season
            {
                'input': {},
                'expected': 'Regular Season'
            },
            # Null season
            {
                'input': {'season': None},
                'expected': 'Regular Season'
            },
            # Invalid season structure
            {
                'input': {'season': 'invalid'},
                'expected': 'Regular Season'
            }
        ]
        
        for test_case in test_cases:
            result = extract_season_info(test_case['input'])
            assert result == test_case['expected'], f"Failed for input: {test_case['input']}"

### **ERROR SIMULATION TESTING**

class ErrorSimulationTests:
    """Test error handling with simulated failures"""
    
    @pytest.mark.asyncio
    async def test_network_error_handling(self):
        """Test handling of various network errors"""
        
        with patch('aiohttp.ClientSession.get') as mock_get:
            # Simulate timeout
            mock_get.side_effect = asyncio.TimeoutError()
            
            client = ResilientAPIClient('https://api.espn.com')
            async with client:
                result = await client.get_with_retry('/test')
                assert result is None  # Should handle gracefully
            
            # Simulate connection error
            mock_get.side_effect = aiohttp.ClientConnectorError(
                connection_key=Mock(), os_error=OSError("Connection failed")
            )
            
            async with client:
                with pytest.raises(aiohttp.ClientConnectorError):
                    await client.get_with_retry('/test')
    
    @pytest.mark.asyncio
    async def test_data_structure_error_recovery(self):
        """Test recovery from data structure errors"""
        
        # Simulate malformed ESPN response
        malformed_responses = [
            {'events': 'not_a_list'},
            {'events': [{'id': None}]},  # Missing required fields
            {'events': [{}]},  # Empty event
            None,  # Null response
            'invalid_json'  # Invalid format
        ]
        
        parser = DefensiveDataParser('test_sport')
        
        for malformed_response in malformed_responses:
            if isinstance(malformed_response, dict) and 'events' in malformed_response:
                for event in malformed_response['events']:
                    result = parser.parse_game_data(event)
                    # Should either return valid data or None, never crash
                    assert result is None or isinstance(result, dict)
    
    @pytest.mark.asyncio
    async def test_progressive_degradation_flow(self):
        """Test progressive degradation under various failure scenarios"""
        
        degradation_handler = ProgressiveDegradationHandler()
        
        # Simulate increasing error rates
        async def failing_operation():
            raise ValueError("Simulated failure")
        
        async def degraded_operation_1():
            return {'result': 'degraded_level_1'}
        
        async def degraded_operation_2():
            return {'result': 'degraded_level_2'}
        
        degraded_ops = [degraded_operation_1, degraded_operation_2]
        
        # First few failures should trigger degradation
        for i in range(10):
            try:
                result = await degradation_handler.execute_with_degradation(
                    'test_operation',
                    failing_operation,
                    degraded_ops
                )
                # Should get progressively more degraded results
                assert 'result' in result
            except Exception:
                pass  # Some failures expected
        
        # Service should be degraded by now
        assert degradation_handler.current_level > 0
```

---

**🔥💀🔥 API INTEGRATION BEST PRACTICES COMPLETE! 🔥💀🔥**

*These practices ensure robust, production-ready API integrations that survive real-world variations and failures while maintaining system reliability and user experience.*