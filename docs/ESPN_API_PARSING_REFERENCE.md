# 📊 **ESPN API PARSING TECHNICAL REFERENCE**

## **🔧 COMPREHENSIVE GUIDE TO ESPN API DATA STRUCTURE HANDLING**

### **🎯 PURPOSE**
This reference provides technical guidance for handling ESPN API data structure variations, based on the UEFA Champions League connectivity breakthrough of September 17, 2025.

---

## 🔥 **ESPN API DATA STRUCTURE PATTERNS**

### **PATTERN 1: Season Type Variations**

#### **Old Format (Dictionary)**
```json
{
  "season": {
    "type": {
      "name": "Group Stage",
      "id": "1"
    }
  }
}
```

#### **New ESPN Format (Integer)**
```json
{
  "season": {
    "type": 13682,
    "slug": "champions-league-2024-25",
    "name": "UEFA Champions League"
  }
}
```

#### **Robust Parsing Implementation**
```python
def extract_season_info(event_data):
    """
    Extract season information handling both old and new ESPN formats
    
    Args:
        event_data (dict): ESPN API event data
        
    Returns:
        str: Formatted season/round information
    """
    season_info = event_data.get('season', {})
    
    # Handle missing or invalid season data
    if not isinstance(season_info, dict):
        return 'Regular Season'
    
    season_type = season_info.get('type', 'Regular Season')
    
    if isinstance(season_type, dict):
        # Old format: type is dictionary with name
        round_info = season_type.get('name', 'Regular Season')
    elif isinstance(season_type, int):
        # New ESPN format: type is integer, use slug for details
        slug = season_info.get('slug', 'regular-season')
        round_info = slug.replace('-', ' ').title()
    else:
        # Fallback for any other format
        round_info = str(season_type) if season_type else 'Regular Season'
    
    return round_info
```

### **PATTERN 2: Team Information Extraction**

#### **Standard Team Format**
```json
{
  "competitions": [{
    "competitors": [{
      "team": {
        "displayName": "Real Madrid",
        "abbreviation": "RM",
        "logos": [{"href": "logo_url"}]
      },
      "homeAway": "home"
    }]
  }]
}
```

#### **Robust Team Parsing**
```python
def extract_team_info(competitor_data):
    """
    Extract team information with fallback handling
    
    Args:
        competitor_data (dict): ESPN competitor data
        
    Returns:
        dict: Standardized team information
    """
    team_data = competitor_data.get('team', {})
    
    return {
        'name': team_data.get('displayName', 'Unknown Team'),
        'short_name': team_data.get('abbreviation', 'UNK'),
        'logo': _extract_logo_url(team_data.get('logos', [])),
        'home_away': competitor_data.get('homeAway', 'neutral')
    }

def _extract_logo_url(logos_list):
    """Extract first available logo URL"""
    if logos_list and isinstance(logos_list, list):
        return logos_list[0].get('href', '') if logos_list[0] else ''
    return ''
```

### **PATTERN 3: Date/Time Handling**

#### **ESPN Date Format**
```json
{
  "date": "2025-09-17T19:00:00Z",
  "status": {
    "type": {
      "name": "STATUS_SCHEDULED"
    }
  }
}
```

#### **Robust Date Parsing**
```python
from datetime import datetime
import pytz

def extract_game_datetime(event_data):
    """
    Extract and format game date/time
    
    Args:
        event_data (dict): ESPN event data
        
    Returns:
        dict: Formatted date/time information
    """
    date_str = event_data.get('date', '')
    
    try:
        # Parse ESPN's ISO format
        utc_dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        
        return {
            'utc_datetime': utc_dt,
            'formatted_date': utc_dt.strftime('%Y-%m-%d'),
            'formatted_time': utc_dt.strftime('%H:%M UTC'),
            'timestamp': int(utc_dt.timestamp())
        }
    except (ValueError, AttributeError):
        # Fallback for invalid date formats
        return {
            'utc_datetime': None,
            'formatted_date': 'TBD',
            'formatted_time': 'TBD',
            'timestamp': 0
        }
```

---

## 🛡️ **ERROR HANDLING PATTERNS**

### **PATTERN 1: Type Validation**
```python
def safe_get_nested(data, keys, default=None):
    """
    Safely extract nested dictionary values with type checking
    
    Args:
        data (dict): Source data
        keys (list): List of keys for nested access
        default: Default value if any key fails
        
    Returns:
        Any: Extracted value or default
    """
    current = data
    
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
        if current is None:
            return default
    
    return current

# Usage example
venue_name = safe_get_nested(event_data, ['venue', 'fullName'], 'TBD')
```

### **PATTERN 2: List Processing**
```python
def safe_process_list(data_list, processor_func, default_list=None):
    """
    Safely process lists with error handling
    
    Args:
        data_list (list): List to process
        processor_func (callable): Function to apply to each item
        default_list (list): Default return if processing fails
        
    Returns:
        list: Processed results or default
    """
    if not isinstance(data_list, list):
        return default_list or []
    
    results = []
    for item in data_list:
        try:
            processed = processor_func(item)
            if processed is not None:
                results.append(processed)
        except Exception as e:
            logger.warning(f"Failed to process list item: {e}")
            continue
    
    return results
```

### **PATTERN 3: API Response Validation**
```python
def validate_espn_response(response_data):
    """
    Validate ESPN API response structure
    
    Args:
        response_data (dict): ESPN API response
        
    Returns:
        tuple: (is_valid, error_message, events_list)
    """
    if not isinstance(response_data, dict):
        return False, "Response is not a dictionary", []
    
    events = response_data.get('events', [])
    if not isinstance(events, list):
        return False, "Events field is not a list", []
    
    if len(events) == 0:
        return True, "No events found", []
    
    # Validate first event structure
    first_event = events[0]
    required_fields = ['id', 'date', 'competitions']
    
    for field in required_fields:
        if field not in first_event:
            return False, f"Missing required field: {field}", []
    
    return True, "Valid response", events
```

---

## 🔧 **INTEGRATION PATTERNS**

### **PATTERN 1: MCP Integration**
```python
class SportsMCP:
    def __init__(self, sport_name, api_endpoint):
        self.sport_name = sport_name
        self.api_endpoint = api_endpoint
        self.logger = logging.getLogger(f"{sport_name}_mcp")
    
    async def fetch_games(self):
        """Fetch and parse games with comprehensive error handling"""
        try:
            # API call
            response = await self._make_api_call()
            
            # Validate response
            is_valid, error_msg, events = validate_espn_response(response)
            if not is_valid:
                self.logger.error(f"Invalid API response: {error_msg}")
                return []
            
            # Process events
            games = []
            for event in events:
                try:
                    game = self._process_single_event(event)
                    if game:
                        games.append(game)
                except Exception as e:
                    self.logger.warning(f"Failed to process event {event.get('id', 'unknown')}: {e}")
                    continue
            
            self.logger.info(f"Successfully processed {len(games)} games")
            return games
            
        except Exception as e:
            self.logger.error(f"Failed to fetch games: {e}")
            return []
    
    def _process_single_event(self, event):
        """Process single event with all parsing patterns"""
        game_data = {
            'id': event.get('id'),
            'season_info': extract_season_info(event),
            'date_time': extract_game_datetime(event),
            'teams': self._extract_teams(event),
            'venue': safe_get_nested(event, ['venue', 'fullName'], 'TBD')
        }
        
        # Validate required fields
        if not game_data['id'] or not game_data['teams']:
            return None
            
        return game_data
```

### **PATTERN 2: Dashboard Integration**
```python
def format_for_dashboard(game_analysis):
    """
    Format analysis results for dashboard consumption
    
    Args:
        game_analysis (dict): Raw analysis results
        
    Returns:
        dict: Dashboard-formatted results
    """
    # Ensure all required dashboard keys exist
    dashboard_result = {
        # Primary keys (dashboard expects these)
        'confidence': game_analysis.get('consensus_confidence', 0),
        'pick': game_analysis.get('consensus_pick', 'TBD'),
        
        # Secondary keys (internal use)
        'consensus_confidence': game_analysis.get('consensus_confidence', 0),
        'consensus_pick': game_analysis.get('consensus_pick', 'TBD'),
        'consensus_strength': game_analysis.get('consensus_strength', 'MEDIUM'),
        
        # Analysis details
        'active_dimensions': game_analysis.get('active_dimensions', 0),
        'dimensional_results': game_analysis.get('dimensional_results', {}),
        
        # Error handling
        'error': game_analysis.get('error'),
        'fallback_used': game_analysis.get('fallback_used', False)
    }
    
    return dashboard_result
```

---

## 📋 **TESTING PATTERNS**

### **Test Data Generation**
```python
def create_test_espn_event(event_type='new_format'):
    """Create test ESPN event data for different format types"""
    
    base_event = {
        'id': '12345',
        'date': '2025-09-17T19:00:00Z',
        'venue': {
            'fullName': 'Santiago Bernabéu Stadium'
        },
        'competitions': [{
            'competitors': [
                {
                    'team': {
                        'displayName': 'Real Madrid',
                        'abbreviation': 'RM'
                    },
                    'homeAway': 'home'
                },
                {
                    'team': {
                        'displayName': 'Manchester City',
                        'abbreviation': 'MCI'
                    },
                    'homeAway': 'away'
                }
            ]
        }]
    }
    
    if event_type == 'new_format':
        base_event['season'] = {
            'type': 13682,
            'slug': 'champions-league-2024-25'
        }
    elif event_type == 'old_format':
        base_event['season'] = {
            'type': {
                'name': 'Group Stage',
                'id': '1'
            }
        }
    
    return base_event
```

### **Unit Tests Example**
```python
import pytest

class TestESPNParsing:
    def test_season_info_new_format(self):
        event = create_test_espn_event('new_format')
        result = extract_season_info(event)
        assert result == 'Champions League 2024 25'
    
    def test_season_info_old_format(self):
        event = create_test_espn_event('old_format')
        result = extract_season_info(event)
        assert result == 'Group Stage'
    
    def test_invalid_season_data(self):
        event = {'season': 'invalid_data'}
        result = extract_season_info(event)
        assert result == 'Regular Season'
    
    def test_missing_season_data(self):
        event = {}
        result = extract_season_info(event)
        assert result == 'Regular Season'
```

---

## 🚀 **PERFORMANCE OPTIMIZATION**

### **Caching Strategy**
```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=128)
def cached_team_processing(team_data_hash, team_json):
    """Cache team processing results"""
    import json
    team_data = json.loads(team_json)
    return extract_team_info(team_data)

def process_team_with_cache(team_data):
    """Process team data with caching"""
    team_json = json.dumps(team_data, sort_keys=True)
    team_hash = hashlib.md5(team_json.encode()).hexdigest()
    return cached_team_processing(team_hash, team_json)
```

### **Batch Processing**
```python
async def process_events_batch(events, batch_size=10):
    """Process events in batches for better performance"""
    results = []
    
    for i in range(0, len(events), batch_size):
        batch = events[i:i + batch_size]
        
        # Process batch concurrently
        batch_tasks = [process_single_event_async(event) for event in batch]
        batch_results = await asyncio.gather(*batch_tasks, return_exceptions=True)
        
        # Filter successful results
        for result in batch_results:
            if not isinstance(result, Exception) and result:
                results.append(result)
    
    return results
```

---

## 📚 **REFERENCE IMPLEMENTATIONS**

### **Complete ESPN MCP Class**
```python
class ESPNSportsMCP:
    """Complete ESPN API integration with all patterns implemented"""
    
    def __init__(self, sport_config):
        self.sport_name = sport_config['name']
        self.api_endpoint = sport_config['endpoint']
        self.logger = logging.getLogger(f"{self.sport_name}_mcp")
        self.session = aiohttp.ClientSession()
    
    async def fetch_and_analyze_games(self):
        """Main entry point - fetch, parse, and analyze games"""
        try:
            # Step 1: Fetch raw data
            raw_data = await self._fetch_espn_data()
            
            # Step 2: Validate and parse
            games = await self._parse_games(raw_data)
            
            # Step 3: Analyze each game
            analyzed_games = []
            for game in games:
                analysis = await self._analyze_single_game(game)
                if analysis:
                    analyzed_games.append(analysis)
            
            return analyzed_games
            
        except Exception as e:
            self.logger.error(f"Complete process failed: {e}")
            return []
    
    async def _fetch_espn_data(self):
        """Fetch data with retry logic"""
        for attempt in range(3):
            try:
                async with self.session.get(self.api_endpoint) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        self.logger.warning(f"API returned status {response.status}")
            except Exception as e:
                self.logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == 2:
                    raise
                await asyncio.sleep(2 ** attempt)
        
        return None
    
    async def _parse_games(self, raw_data):
        """Parse raw ESPN data into structured games"""
        is_valid, error_msg, events = validate_espn_response(raw_data)
        if not is_valid:
            self.logger.error(f"Invalid ESPN response: {error_msg}")
            return []
        
        return await process_events_batch(events)
    
    async def _analyze_single_game(self, game_data):
        """Analyze single game with comprehensive error handling"""
        try:
            # Your analysis logic here
            analysis_result = await perform_game_analysis(game_data)
            return format_for_dashboard(analysis_result)
            
        except Exception as e:
            self.logger.error(f"Game analysis failed for {game_data.get('id')}: {e}")
            return None
```

---

**🔥💀🔥 ESPN API PARSING REFERENCE COMPLETE! 🔥💀🔥**

*This reference ensures robust handling of ESPN API variations and prevents future connectivity issues across all sports integrations.*