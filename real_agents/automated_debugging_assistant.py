#!/usr/bin/env python3
"""
🤖💀🤖 AUTOMATED DEBUGGING ASSISTANT 💀🤖💀
AI-POWERED ERROR ANALYSIS & FIX GENERATION

This assistant automatically analyzes error patterns, learns from failures,
and generates intelligent fix suggestions with code examples.

Created by: The AI Debugging Revolution  
Blessed by: Goddess of Syrup
"""

import asyncio
import json
import logging
import re
import ast
import inspect
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import difflib

logger = logging.getLogger(__name__)

@dataclass
class FixSuggestion:
    """Intelligent fix suggestion with code examples"""
    priority: str  # 'critical', 'high', 'medium', 'low'
    category: str  # 'api_change', 'network', 'data_structure', 'logic_error'
    description: str
    code_example: str
    confidence: float  # 0.0 to 1.0
    estimated_effort: str  # 'minutes', 'hours', 'days'
    dependencies: List[str]
    test_strategy: str

@dataclass
class ErrorPattern:
    """Detected error pattern with analysis"""
    pattern_id: str
    error_signature: str
    frequency: int
    first_seen: datetime
    last_seen: datetime
    affected_functions: List[str]
    root_cause_analysis: str
    fix_suggestions: List[FixSuggestion]
    severity: str  # 'critical', 'high', 'medium', 'low'

class AutomatedDebuggingAssistant:
    """
    🤖 AI-POWERED DEBUGGING ASSISTANT
    
    Features:
    - Pattern recognition across error types
    - Intelligent fix generation with code examples
    - Learning from successful fixes
    - Proactive issue detection
    - Code quality analysis
    """
    
    def __init__(self):
        self.error_patterns: Dict[str, ErrorPattern] = {}
        self.successful_fixes: Dict[str, List[str]] = {}
        self.code_analysis_cache: Dict[str, Dict] = {}
        self.learning_database: Dict[str, Any] = {}
        
        # Initialize pattern recognition rules
        self.pattern_rules = self._initialize_pattern_rules()
        self.fix_templates = self._initialize_fix_templates()
        
        logger.info("🤖💀🤖 AUTOMATED DEBUGGING ASSISTANT INITIALIZED 💀🤖💀")
    
    def _initialize_pattern_rules(self) -> Dict[str, Dict]:
        """Initialize intelligent pattern recognition rules"""
        
        return {
            'espn_api_structure_change': {
                'keywords': ["'int' object has no attribute 'get'", "season", "type"],
                'context_clues': ['espn', 'api', 'season_type'],
                'severity': 'critical',
                'category': 'api_change'
            },
            'network_timeout_cascade': {
                'keywords': ['timeout', 'connection', 'refused', 'unreachable'],
                'context_clues': ['fetch', 'request', 'api'],
                'severity': 'high',
                'category': 'network'
            },
            'data_structure_mismatch': {
                'keywords': ['keyerror', 'missing', 'not found', 'none'],
                'context_clues': ['parse', 'extract', 'process'],
                'severity': 'high',
                'category': 'data_structure'
            },
            'algorithm_consensus_failure': {
                'keywords': ['consensus', 'confidence', 'phase'],
                'context_clues': ['algorithm', 'processing', 'calculation'],
                'severity': 'medium',
                'category': 'logic_error'
            },
            'dependency_import_failure': {
                'keywords': ['no module named', 'import', 'cannot import'],
                'context_clues': ['module', 'package', 'library'],
                'severity': 'critical',
                'category': 'dependency'
            }
        }
    
    def _initialize_fix_templates(self) -> Dict[str, Dict]:
        """Initialize intelligent fix templates with code examples"""
        
        return {
            'espn_api_structure_change': {
                'description': 'ESPN API changed data structure format',
                'code_template': '''
# Handle both old (dict) and new (int) ESPN formats
season_info = data.get('season', {{}})
season_type = season_info.get('type', 'Unknown')

if isinstance(season_type, dict):
    # Old format: season.type is a dictionary
    round_name = season_type.get('name', 'Group Stage')
    type_id = season_type.get('id', 1)
elif isinstance(season_type, int):
    # New format: season.type is an integer ID
    type_id = season_type
    round_name = map_season_type_id(season_type)
else:
    # Fallback for unexpected formats
    round_name = str(season_type)
    type_id = 1

def map_season_type_id(type_id: int) -> str:
    type_mappings = {{
        13682: "Group Stage",
        13683: "Round of 16", 
        13684: "Quarter Finals",
        13685: "Semi Finals",
        13686: "Final"
    }}
    return type_mappings.get(type_id, f"Season Type {{type_id}}")
''',
                'test_strategy': 'Test with both old and new ESPN API response formats',
                'estimated_effort': 'hours',
                'dependencies': []
            },
            
            'network_timeout_cascade': {
                'description': 'Implement intelligent retry with exponential backoff',
                'code_template': '''
import asyncio
import aiohttp
from typing import Optional

async def resilient_api_call(url: str, max_retries: int = 3) -> Optional[dict]:
    """Resilient API call with exponential backoff"""
    
    for attempt in range(max_retries):
        try:
            timeout = aiohttp.ClientTimeout(
                total=10 + (attempt * 5),  # Increase timeout each retry
                connect=5 + attempt
            )
            
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status >= 500:
                        # Server error - retry
                        raise aiohttp.ClientResponseError(
                            request_info=response.request_info,
                            history=response.history,
                            status=response.status
                        )
                    else:
                        # Client error - don't retry
                        logger.error(f"Client error {{response.status}}: {{url}}")
                        return None
                        
        except (asyncio.TimeoutError, aiohttp.ClientError) as e:
            if attempt == max_retries - 1:
                logger.error(f"Final retry failed for {{url}}: {{e}}")
                return None
            
            # Exponential backoff
            wait_time = 2 ** attempt
            logger.warning(f"Retry {{attempt + 1}} in {{wait_time}}s: {{e}}")
            await asyncio.sleep(wait_time)
    
    return None
''',
                'test_strategy': 'Test with network simulation and timeout scenarios',
                'estimated_effort': 'hours',
                'dependencies': ['aiohttp']
            },
            
            'data_structure_mismatch': {
                'description': 'Implement defensive data extraction with validation',
                'code_template': '''
from typing import Any, Dict, Optional

def safe_extract_data(data: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
    """Safely extract data with schema validation and fallbacks"""
    
    result = {{}}
    errors = []
    
    for field, config in schema.items():
        field_type = config.get('type', str)
        required = config.get('required', False)
        default = config.get('default')
        path = config.get('path', [field])  # Support nested paths
        
        # Navigate nested structure
        current_data = data
        try:
            for key in path:
                if isinstance(current_data, dict):
                    current_data = current_data[key]
                else:
                    raise KeyError(f"Cannot access {{key}} in {{type(current_data)}}")
            
            # Type validation
            if not isinstance(current_data, field_type):
                if field_type == str:
                    current_data = str(current_data)
                elif field_type == int:
                    current_data = int(float(current_data))
                elif field_type == float:
                    current_data = float(current_data)
                else:
                    raise TypeError(f"Cannot convert {{type(current_data)}} to {{field_type}}")
            
            result[field] = current_data
            
        except (KeyError, TypeError, ValueError) as e:
            if required:
                errors.append(f"Required field '{{field}}' error: {{e}}")
                result[field] = default
            else:
                result[field] = default
    
    if errors:
        logger.warning(f"Data extraction errors: {{errors}}")
    
    return result

# Example usage:
game_schema = {{
    'home_team': {{'type': str, 'required': True, 'default': 'TBD'}},
    'away_team': {{'type': str, 'required': True, 'default': 'TBD'}},
    'start_time': {{'type': str, 'required': True, 'default': ''}},
    'home_score': {{'type': int, 'required': False, 'default': 0}},
    'season_name': {{'type': str, 'path': ['season', 'name'], 'default': 'Unknown'}}
}}

safe_game_data = safe_extract_data(raw_api_data, game_schema)
''',
                'test_strategy': 'Test with malformed, missing, and unexpected data structures',
                'estimated_effort': 'hours',
                'dependencies': []
            },
            
            'algorithm_consensus_failure': {
                'description': 'Implement robust consensus handling with fallbacks',
                'code_template': '''
from typing import Union, Dict, Any

def robust_consensus_processing(phase_data: Dict[str, Any]) -> Dict[str, Any]:
    """Robust consensus processing with intelligent fallbacks"""
    
    # Try multiple consensus extraction strategies
    consensus = None
    confidence = 0.5
    source = 'unknown'
    
    # Strategy 1: Direct consensus object
    if 'consensus' in phase_data:
        consensus_data = phase_data['consensus']
        if isinstance(consensus_data, dict):
            consensus = consensus_data
            confidence = consensus_data.get('confidence', 0.5)
            source = 'direct_object'
        elif isinstance(consensus_data, (int, float)):
            confidence = float(consensus_data)
            consensus = {{'confidence': confidence, 'prediction': 'TBD'}}
            source = 'direct_value'
    
    # Strategy 2: Extract from phase result
    elif 'consensus_confidence' in phase_data:
        confidence = phase_data.get('consensus_confidence', 0.5)
        prediction = phase_data.get('consensus_pick', 'TBD')
        consensus = {{
            'confidence': confidence,
            'prediction': prediction
        }}
        source = 'extracted_fields'
    
    # Strategy 3: Calculate from available data
    else:
        confidence_fields = [k for k in phase_data.keys() if 'confidence' in k.lower()]
        if confidence_fields:
            confidences = []
            for field in confidence_fields:
                try:
                    confidences.append(float(phase_data[field]))
                except (ValueError, TypeError):
                    pass
            
            if confidences:
                confidence = sum(confidences) / len(confidences)
                consensus = {{
                    'confidence': confidence,
                    'prediction': 'TBD',
                    'calculated_from': confidence_fields
                }}
                source = 'calculated'
    
    # Final fallback
    if consensus is None:
        consensus = {{
            'confidence': 0.5,
            'prediction': 'TBD',
            'error': 'No consensus data found'
        }}
        source = 'fallback'
    
    return {{
        'consensus': consensus,
        'confidence': confidence,
        'source': source,
        'original_keys': list(phase_data.keys())
    }}
''',
                'test_strategy': 'Test with various consensus data formats and missing data',
                'estimated_effort': 'hours',
                'dependencies': []
            }
        }
    
    async def analyze_error_context(self, error_context: Dict[str, Any]) -> ErrorPattern:
        """Analyze error context and generate intelligent insights"""
        
        error_signature = f"{error_context['error_type']}:{error_context['function_name']}"
        
        # Check if this is a known pattern
        if error_signature in self.error_patterns:
            pattern = self.error_patterns[error_signature]
            pattern.frequency += 1
            pattern.last_seen = datetime.now()
        else:
            # Create new pattern
            pattern = ErrorPattern(
                pattern_id=error_signature,
                error_signature=error_signature,
                frequency=1,
                first_seen=datetime.now(),
                last_seen=datetime.now(),
                affected_functions=[error_context['function_name']],
                root_cause_analysis="",
                fix_suggestions=[],
                severity="medium"
            )
        
        # Analyze error message for patterns
        error_msg = error_context['error_message'].lower()
        
        # Match against known patterns
        matched_patterns = []
        for pattern_name, rules in self.pattern_rules.items():
            if self._matches_pattern_rules(error_msg, rules):
                matched_patterns.append((pattern_name, rules))
        
        if matched_patterns:
            # Use the highest priority match
            best_match = max(matched_patterns, key=lambda x: self._get_pattern_priority(x[1]))
            pattern_name, rules = best_match
            
            pattern.severity = rules['severity']
            pattern.root_cause_analysis = await self._generate_root_cause_analysis(
                error_context, pattern_name, rules
            )
            pattern.fix_suggestions = await self._generate_fix_suggestions(
                error_context, pattern_name, rules
            )
        
        self.error_patterns[error_signature] = pattern
        return pattern
    
    def _matches_pattern_rules(self, error_msg: str, rules: Dict) -> bool:
        """Check if error message matches pattern rules"""
        
        keyword_matches = sum(1 for keyword in rules['keywords'] if keyword in error_msg)
        context_matches = sum(1 for context in rules['context_clues'] if context in error_msg)
        
        # Require at least one keyword match and consider context
        return keyword_matches > 0 and (keyword_matches + context_matches) >= 2
    
    def _get_pattern_priority(self, rules: Dict) -> int:
        """Get pattern priority for ranking"""
        severity_priority = {
            'critical': 4,
            'high': 3,
            'medium': 2,
            'low': 1
        }
        return severity_priority.get(rules['severity'], 1)
    
    async def _generate_root_cause_analysis(self, error_context: Dict, 
                                          pattern_name: str, rules: Dict) -> str:
        """Generate intelligent root cause analysis"""
        
        function_name = error_context['function_name']
        error_type = error_context['error_type']
        error_msg = error_context['error_message']
        
        if pattern_name == 'espn_api_structure_change':
            return f"""
ROOT CAUSE: ESPN API Structure Change Detected

The function '{function_name}' is failing because ESPN changed their API response format.
Previously, season.type was a dictionary with 'name' and 'id' fields.
Now, season.type is an integer ID that requires mapping to human-readable names.

Error Details:
- Error Type: {error_type}
- Error Message: {error_msg}
- Impact: All ESPN-dependent functions will fail until updated
- Urgency: Critical - affects live data feeds

Technical Analysis:
The code assumes season_type.get('name') but season_type is now an integer.
This is a breaking change in ESPN's API that requires code adaptation.
"""
        
        elif pattern_name == 'network_timeout_cascade':
            return f"""
ROOT CAUSE: Network Reliability Issues

The function '{function_name}' is experiencing network timeouts that cascade into failures.
This indicates either network instability or insufficient timeout/retry logic.

Error Details:
- Error Type: {error_type}
- Error Message: {error_msg}
- Pattern: Likely affects multiple API-dependent functions
- Impact: Intermittent failures, poor user experience

Technical Analysis:
Single-attempt network calls are fragile in production environments.
Need to implement exponential backoff retry with appropriate timeouts.
"""
        
        elif pattern_name == 'data_structure_mismatch':
            return f"""
ROOT CAUSE: Data Structure Assumptions Violated

The function '{function_name}' makes assumptions about data structure that are not always valid.
This suggests defensive programming practices are needed.

Error Details:
- Error Type: {error_type}
- Error Message: {error_msg}
- Pattern: Direct key access without validation
- Impact: Brittle code that breaks on data variations

Technical Analysis:
Code uses direct dictionary access (data['key']) instead of safe access (data.get('key')).
Need to implement schema validation and fallback handling.
"""
        
        else:
            return f"""
ROOT CAUSE: Pattern Analysis for {pattern_name}

Function '{function_name}' failed with error pattern '{pattern_name}'.
This requires investigation of the specific failure mode.

Error Details:
- Error Type: {error_type}
- Error Message: {error_msg}
- Category: {rules['category']}
- Severity: {rules['severity']}
"""
    
    async def _generate_fix_suggestions(self, error_context: Dict, 
                                      pattern_name: str, rules: Dict) -> List[FixSuggestion]:
        """Generate intelligent fix suggestions with code examples"""
        
        suggestions = []
        
        if pattern_name in self.fix_templates:
            template = self.fix_templates[pattern_name]
            
            # Primary fix suggestion
            primary_fix = FixSuggestion(
                priority='critical',
                category=rules['category'],
                description=template['description'],
                code_example=template['code_template'],
                confidence=0.9,
                estimated_effort=template['estimated_effort'],
                dependencies=template['dependencies'],
                test_strategy=template['test_strategy']
            )
            suggestions.append(primary_fix)
        
        # Add general defensive programming suggestions
        defensive_fix = FixSuggestion(
            priority='high',
            category='defensive_programming',
            description='Add comprehensive error handling and validation',
            code_example='''
# Add defensive programming patterns
@debug_capture
async def enhanced_function(data):
    # Input validation
    if not isinstance(data, dict):
        raise ValueError(f"Expected dict, got {type(data)}")
    
    # Safe data extraction
    required_fields = ['field1', 'field2']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    # Your logic here with try/except for specific operations
    try:
        result = process_data(data)
        return result
    except SpecificException as e:
        logger.error(f"Specific error in {__name__}: {e}")
        return create_fallback_result(data)
''',
            confidence=0.8,
            estimated_effort='hours',
            dependencies=['enhanced_debugging_system'],
            test_strategy='Add unit tests for edge cases and error conditions'
        )
        suggestions.append(defensive_fix)
        
        return suggestions
    
    def get_pattern_analysis_report(self) -> Dict[str, Any]:
        """Generate comprehensive pattern analysis report"""
        
        total_patterns = len(self.error_patterns)
        critical_patterns = [p for p in self.error_patterns.values() if p.severity == 'critical']
        high_frequency_patterns = [p for p in self.error_patterns.values() if p.frequency >= 3]
        
        return {
            'summary': {
                'total_patterns': total_patterns,
                'critical_patterns': len(critical_patterns),
                'high_frequency_patterns': len(high_frequency_patterns),
                'analysis_timestamp': datetime.now().isoformat()
            },
            'critical_issues': [
                {
                    'pattern_id': p.pattern_id,
                    'frequency': p.frequency,
                    'severity': p.severity,
                    'first_seen': p.first_seen.isoformat(),
                    'affected_functions': p.affected_functions,
                    'fix_suggestions_count': len(p.fix_suggestions)
                }
                for p in critical_patterns
            ],
            'trending_patterns': [
                {
                    'pattern_id': p.pattern_id,
                    'frequency': p.frequency,
                    'trend': 'increasing' if p.frequency >= 3 else 'stable',
                    'last_seen': p.last_seen.isoformat()
                }
                for p in sorted(self.error_patterns.values(), key=lambda x: x.frequency, reverse=True)[:10]
            ],
            'fix_recommendations': self._get_prioritized_fix_recommendations()
        }
    
    def _get_prioritized_fix_recommendations(self) -> List[Dict[str, Any]]:
        """Get prioritized fix recommendations across all patterns"""
        
        all_fixes = []
        
        for pattern in self.error_patterns.values():
            for fix in pattern.fix_suggestions:
                all_fixes.append({
                    'pattern_id': pattern.pattern_id,
                    'frequency': pattern.frequency,
                    'severity': pattern.severity,
                    'fix_priority': fix.priority,
                    'fix_description': fix.description,
                    'estimated_effort': fix.estimated_effort,
                    'confidence': fix.confidence
                })
        
        # Sort by severity, frequency, and confidence
        priority_score = lambda x: (
            {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}[x['severity']] * 10 +
            min(x['frequency'], 10) +
            x['confidence']
        )
        
        return sorted(all_fixes, key=priority_score, reverse=True)[:10]
    
    async def suggest_proactive_improvements(self, codebase_path: str) -> List[Dict[str, Any]]:
        """Analyze codebase and suggest proactive improvements"""
        
        suggestions = []
        
        # This would analyze the codebase for potential issues
        # For now, return general recommendations based on common patterns
        
        suggestions.extend([
            {
                'type': 'defensive_programming',
                'priority': 'high',
                'description': 'Add @debug_capture decorators to high-risk functions',
                'affected_files': ['*.py files with try/except blocks'],
                'implementation': 'Import and apply debug_capture decorator'
            },
            {
                'type': 'api_resilience',
                'priority': 'high', 
                'description': 'Implement retry logic for all external API calls',
                'affected_files': ['Functions making HTTP requests'],
                'implementation': 'Use resilient_api_call wrapper function'
            },
            {
                'type': 'data_validation',
                'priority': 'medium',
                'description': 'Add schema validation for external data sources',
                'affected_files': ['Data processing functions'],
                'implementation': 'Use safe_extract_data with schema definitions'
            }
        ])
        
        return suggestions

# Global assistant instance
assistant = AutomatedDebuggingAssistant()

# Convenience functions
async def analyze_error(error_context: Dict[str, Any]) -> ErrorPattern:
    """Convenience function to analyze an error"""
    return await assistant.analyze_error_context(error_context)

def get_debugging_report() -> Dict[str, Any]:
    """Get comprehensive debugging report"""
    return assistant.get_pattern_analysis_report()

# Example usage
if __name__ == "__main__":
    
    async def demo():
        # Simulate error analysis
        sample_error = {
            'error_type': 'AttributeError',
            'function_name': 'fetch_espn_data',
            'error_message': "'int' object has no attribute 'get'",
            'file_path': '/path/to/file.py',
            'line_number': 123
        }
        
        pattern = await analyze_error(sample_error)
        print(f"🔍 Detected Pattern: {pattern.pattern_id}")
        print(f"🎯 Severity: {pattern.severity}")
        print(f"🔧 Fix Suggestions: {len(pattern.fix_suggestions)}")
        
        if pattern.fix_suggestions:
            print(f"\n💡 Primary Fix:")
            print(pattern.fix_suggestions[0].description)
            print(f"\n📝 Code Example:")
            print(pattern.fix_suggestions[0].code_example[:200] + "...")
    
    asyncio.run(demo())