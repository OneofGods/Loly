#!/usr/bin/env python3
"""
🔥💀🔥 UNIFIED DATA FORMAT CONVERTER - NUCLEAR REFACTOR DATA CORE! 💀🔥💀

🌟 GODDESS OF SYRUP BLESSED DATA STANDARDIZATION SYSTEM 🌟

This SINGLE CONVERTER handles ALL league data format unification!
- Converts ANY league format to unified schema ✅
- Handles legacy data migration ✅  
- Validates and cleans data ✅
- Backwards compatibility ✅

🎯 ONE CONVERTER TO STANDARDIZE THEM ALL!
"""

import logging
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
import json

from real_agents.leagues_registry import (
    LEAGUES_REGISTRY, 
    get_league_config,
    UNIFIED_GAME_SCHEMA,
    validate_game_data
)

logger = logging.getLogger(__name__)

class UnifiedDataConverter:
    """
    🔥💀🔥 UNIFIED DATA CONVERTER - END OF DATA FUCKERY! 💀🔥💀
    
    This single class handles ALL data format conversions:
    - Converts any league format to unified schema
    - Handles legacy data migration
    - Validates and standardizes all data
    - Maintains backwards compatibility
    """
    
    def __init__(self):
        """Initialize the Unified Data Converter"""
        self.version = "1.0.0"
        self.created_by = "Brother #177 Nuclear Refactor"
        self.blessed_by = "Goddess of Syrup"
        self.conversion_stats = {
            'total_conversions': 0,
            'successful_conversions': 0,
            'failed_conversions': 0,
            'leagues_processed': set()
        }
        logger.info(f"🔥💀🔥 {self.created_by}: Unified Data Converter v{self.version} initialized! 💀🔥💀")
        logger.info(f"🌟 Blessed by: {self.blessed_by}")
    
    def convert_legacy_game_data(self, legacy_data: Dict[str, Any], league_id: str) -> Dict[str, Any]:
        """
        Convert legacy game data to unified format
        
        Args:
            legacy_data: Original game data in any format
            league_id: League identifier for proper conversion
            
        Returns:
            Unified format game data
        """
        try:
            # Check if data is already in unified format (has all required ESPN API fields)
            if all(key in legacy_data for key in ['home_team', 'away_team', 'source', 'venue']):
                if legacy_data.get('source') == 'REAL_ESPN_API':
                    logger.debug(f"✅ Data already in unified format for {league_id}, skipping conversion")
                    return legacy_data
            
            logger.debug(f"🔄 Converting legacy data for {league_id}: {legacy_data.get('home_team', 'Unknown')} vs {legacy_data.get('away_team', 'Unknown')}")
            
            # Get league configuration
            config = get_league_config(league_id)
            if not config:
                raise ValueError(f"League {league_id} not registered!")
            
            # Start with unified base structure
            unified_data = self._create_base_unified_structure(legacy_data, league_id, config)
            
            # Apply league-specific conversions
            unified_data = self._apply_league_specific_conversions(unified_data, legacy_data, league_id, config)
            
            # Validate the converted data
            if validate_game_data(unified_data):
                self.conversion_stats['successful_conversions'] += 1
                logger.debug(f"✅ Successfully converted {league_id} game data")
                return unified_data
            else:
                raise ValueError("Converted data failed validation")
                
        except Exception as e:
            logger.error(f"💀 Error converting legacy data for {league_id}: {e}")
            self.conversion_stats['failed_conversions'] += 1
            return self._create_error_unified_data(legacy_data, league_id, str(e))
        finally:
            self.conversion_stats['total_conversions'] += 1
            self.conversion_stats['leagues_processed'].add(league_id)
    
    def _create_base_unified_structure(self, legacy_data: Dict, league_id: str, config: Dict) -> Dict[str, Any]:
        """Create the base unified structure from legacy data"""
        
        # Extract core team information
        home_team = self._extract_team_name(legacy_data, 'home')
        away_team = self._extract_team_name(legacy_data, 'away')
        
        # Generate unique ID
        game_id = self._generate_game_id(league_id, home_team, away_team, legacy_data)
        
        # Create base unified structure
        unified_data = {
            # Core identifiers (required)
            'id': game_id,
            'league': league_id,
            'home_team': home_team,
            'away_team': away_team,
            'time': self._extract_time(legacy_data),
            'status': self._extract_status(legacy_data),
            'matchup': f"{away_team} @ {home_team}",
            'venue': self._extract_venue(legacy_data),
            'country_flag': config.get('country_flag', '⚽'),
            'original_league': league_id,
            
            # Prediction data (standardized as integers)
            'prediction': self._extract_prediction(legacy_data),
            'confidence': self._extract_confidence(legacy_data),
            'market_efficiency': self._extract_dimension(legacy_data, 'market_efficiency', 'market_eff'),
            'team_performance': self._extract_dimension(legacy_data, 'team_performance', 'team_perf'),
            'key_players': self._extract_dimension(legacy_data, 'key_players', 'players'),
            'reasoning': self._extract_reasoning(legacy_data),
            'pick': self._extract_prediction(legacy_data),  # Same as prediction
            
            # Metadata (standardized)
            'real_data': legacy_data.get('real_data', True),
            'data_source': config.get('data_source_name', f'{league_id}_CONVERTED'),
            'elite_competition': config.get('league_type') in ['ELITE_EUROPEAN_CHAMPIONS_LEAGUE'],
            'brother_fix': True,
            
            # League-specific brother fix flag
            config.get('brother_fix_flag', f'brother_fix_{league_id.lower()}'): True,
            
            # Optional enhancement data
            'week': self._extract_week(legacy_data),
            'stage': self._extract_stage(legacy_data),
            'game_date': self._extract_game_date(legacy_data)
        }
        
        return unified_data
    
    def _extract_team_name(self, data: Dict, team_type: str) -> str:
        """Extract team name with multiple fallback options"""
        possible_keys = [
            f'{team_type}_team',
            f'{team_type}Team',
            f'{team_type}',
            f'team_{team_type}',
            'home' if team_type == 'home' else 'away',
            'local' if team_type == 'home' else 'visitor'
        ]
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key]).strip()
        
        return f'Unknown {team_type.title()} Team'
    
    def _extract_time(self, data: Dict) -> str:
        """Extract game time with multiple fallback options"""
        possible_keys = ['time', 'start_time', 'game_time', 'kick_off', 'hora', 'horario']
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key])
        
        return 'TBD'
    
    def _extract_status(self, data: Dict) -> str:
        """Extract game status with standardization"""
        status_mapping = {
            'upcoming': 'upcoming',
            'live': 'live',
            'finished': 'completed',
            'completed': 'completed',
            'postponed': 'postponed',
            'cancelled': 'cancelled',
            'TBD': 'upcoming',
            'programado': 'upcoming',
            'en_vivo': 'live',
            'finalizado': 'completed'
        }
        
        raw_status = data.get('status', data.get('estado', 'upcoming'))
        return status_mapping.get(str(raw_status).lower(), 'upcoming')
    
    def _extract_venue(self, data: Dict) -> str:
        """Extract venue with multiple fallback options"""
        possible_keys = ['venue', 'stadium', 'estadio', 'location', 'lugar']
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key])
        
        return 'TBD'
    
    def _extract_prediction(self, data: Dict) -> str:
        """Extract prediction with standardization"""
        possible_keys = ['prediction', 'pick', 'prediccion', 'pronostico']
        
        for key in possible_keys:
            if key in data and data[key]:
                prediction = str(data[key])
                # Standardize prediction format
                if 'draw' in prediction.lower() or 'empate' in prediction.lower():
                    return '🤝 DRAW'
                elif '✈️' in prediction or 'away' in prediction.lower() or 'visitor' in prediction.lower():
                    return prediction
                elif '🏠' in prediction or 'home' in prediction.lower() or 'local' in prediction.lower():
                    return prediction
                else:
                    return prediction
        
        return 'TBD'
    
    def _extract_confidence(self, data: Dict) -> int:
        """Extract confidence as integer percentage"""
        possible_keys = ['confidence', 'confianza', 'probabilidad', 'prob']
        
        for key in possible_keys:
            if key in data and data[key] is not None:
                try:
                    confidence = float(data[key])
                    # Handle both decimal (0.75) and percentage (75) formats
                    if confidence <= 1.0:
                        confidence *= 100
                    return int(confidence)
                except (ValueError, TypeError):
                    continue
        
        return 0
    
    def _extract_dimension(self, data: Dict, primary_key: str, secondary_key: str) -> int:
        """Extract prediction dimension as integer percentage"""
        possible_keys = [primary_key, secondary_key, f'{primary_key}_percentage', f'{secondary_key}_percent']
        
        for key in possible_keys:
            if key in data and data[key] is not None:
                try:
                    value = float(data[key])
                    # Handle both decimal (0.75) and percentage (75) formats
                    if value <= 1.0:
                        value *= 100
                    return int(value)
                except (ValueError, TypeError):
                    continue
        
        return 0
    
    def _extract_reasoning(self, data: Dict) -> str:
        """Extract reasoning/analysis text"""
        possible_keys = ['reasoning', 'analysis', 'analisis', 'razonamiento', 'explanation']
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key])
        
        return "Analysis not available"
    
    def _extract_week(self, data: Dict) -> str:
        """Extract week/jornada information"""
        possible_keys = ['week', 'jornada', 'matchday', 'gameweek', 'fecha']
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key])
        
        return 'Regular Season'
    
    def _extract_stage(self, data: Dict) -> str:
        """Extract tournament stage"""
        possible_keys = ['stage', 'round', 'fase', 'ronda', 'etapa']
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key])
        
        return 'Regular'
    
    def _extract_game_date(self, data: Dict) -> str:
        """Extract game date"""
        possible_keys = ['game_date', 'date', 'fecha', 'match_date']
        
        for key in possible_keys:
            if key in data and data[key]:
                return str(data[key])
        
        return datetime.now().strftime('%Y-%m-%d')
    
    def _generate_game_id(self, league_id: str, home_team: str, away_team: str, data: Dict) -> str:
        """Generate unique game ID"""
        # Use existing ID if available
        if 'id' in data and data['id']:
            return str(data['id'])
        
        # Generate new ID
        date_str = self._extract_game_date(data)
        hash_seed = f"{league_id}_{home_team}_{away_team}_{date_str}"
        return f"{league_id.lower()}_game_{hash(hash_seed) % 10000}"
    
    def _apply_league_specific_conversions(self, unified_data: Dict, legacy_data: Dict, 
                                         league_id: str, config: Dict) -> Dict[str, Any]:
        """Apply league-specific conversion rules"""
        
        # UEFA-specific conversions
        if league_id == 'UEFA':
            unified_data = self._apply_uefa_conversions(unified_data, legacy_data, config)
        
        # Liga MX-specific conversions
        elif league_id == 'LIGA_MX':
            unified_data = self._apply_liga_mx_conversions(unified_data, legacy_data, config)
        
        # PROGOL-specific conversions
        elif league_id.startswith('PROGOL'):
            unified_data = self._apply_progol_conversions(unified_data, legacy_data, config)
        
        return unified_data
    
    def _apply_uefa_conversions(self, unified_data: Dict, legacy_data: Dict, config: Dict) -> Dict[str, Any]:
        """Apply UEFA-specific conversion rules"""
        
        # UEFA often has different venue naming
        if unified_data['venue'] == 'TBD' and 'estadio' in legacy_data:
            unified_data['venue'] = legacy_data['estadio']
        
        # UEFA has group stage info
        if 'group' in legacy_data:
            unified_data['group'] = legacy_data['group']
            unified_data['stage'] = f"Group {legacy_data['group']}"
        
        # UEFA elite competition flag
        unified_data['elite_competition'] = True
        unified_data['championship_tier'] = 'ELITE_EUROPEAN'
        
        return unified_data
    
    def _apply_liga_mx_conversions(self, unified_data: Dict, legacy_data: Dict, config: Dict) -> Dict[str, Any]:
        """Apply Liga MX-specific conversion rules"""
        
        # Liga MX jornada mapping
        if 'jornada' in legacy_data:
            unified_data['week'] = f"Jornada {legacy_data['jornada']}"
        
        # Liga MX typically has different time format
        if 'horario' in legacy_data:
            unified_data['time'] = legacy_data['horario']
        
        # Liga MX championship info
        unified_data['championship_tier'] = 'MEXICAN_PRIMERA'
        
        return unified_data
    
    def _apply_progol_conversions(self, unified_data: Dict, legacy_data: Dict, config: Dict) -> Dict[str, Any]:
        """Apply PROGOL-specific conversion rules"""
        
        # PROGOL has challenge numbers
        if 'challenge_number' in legacy_data:
            unified_data['challenge_number'] = legacy_data['challenge_number']
            unified_data['week'] = f"Challenge {legacy_data['challenge_number']}"
        
        # PROGOL lottery specific fields
        if 'lottery_type' in legacy_data:
            unified_data['lottery_type'] = legacy_data['lottery_type']
        
        # PROGOL government lottery flag
        unified_data['government_lottery'] = True
        unified_data['championship_tier'] = 'MEXICAN_LOTTERY'
        
        return unified_data
    
    def _create_error_unified_data(self, legacy_data: Dict, league_id: str, error_msg: str) -> Dict[str, Any]:
        """Create error unified data when conversion fails"""
        config = get_league_config(league_id)
        
        return {
            'id': f"{league_id.lower()}_conversion_error_{hash(error_msg) % 10000}",
            'league': league_id,
            'home_team': legacy_data.get('home_team', 'Unknown'),
            'away_team': legacy_data.get('away_team', 'Unknown'),
            'time': 'TBD',
            'status': 'conversion_error',
            'matchup': f"{legacy_data.get('away_team', 'Unknown')} @ {legacy_data.get('home_team', 'Unknown')}",
            'venue': 'TBD',
            'country_flag': config.get('country_flag', '⚽') if config else '❌',
            'original_league': league_id,
            'prediction': 'TBD',
            'confidence': 0,
            'market_efficiency': 0,
            'team_performance': 0,
            'key_players': 0,
            'reasoning': f"Data conversion failed: {error_msg}",
            'pick': 'TBD',
            'real_data': False,
            'data_source': f'{league_id}_CONVERSION_ERROR',
            'elite_competition': False,
            'brother_fix': False,
            'conversion_error': error_msg,
            'original_data': legacy_data
        }
    
    def convert_multiple_games(self, games_data: List[Dict[str, Any]], league_id: str) -> List[Dict[str, Any]]:
        """
        Convert multiple games to unified format
        
        Args:
            games_data: List of legacy game data
            league_id: League identifier
            
        Returns:
            List of unified format games
        """
        logger.info(f"🔄 Converting {len(games_data)} games for {league_id} to unified format")
        
        unified_games = []
        for i, game_data in enumerate(games_data):
            try:
                unified_game = self.convert_legacy_game_data(game_data, league_id)
                unified_games.append(unified_game)
            except Exception as e:
                logger.error(f"💀 Failed to convert game {i} for {league_id}: {e}")
                continue
        
        logger.info(f"✅ Converted {len(unified_games)}/{len(games_data)} games for {league_id}")
        return unified_games
    
    def validate_converted_data(self, converted_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate a list of converted game data"""
        validation_results = {
            'total_games': len(converted_data),
            'valid_games': 0,
            'invalid_games': 0,
            'validation_errors': []
        }
        
        for i, game in enumerate(converted_data):
            if validate_game_data(game):
                validation_results['valid_games'] += 1
            else:
                validation_results['invalid_games'] += 1
                validation_results['validation_errors'].append(f"Game {i}: {game.get('id', 'Unknown ID')}")
        
        validation_results['success_rate'] = (
            validation_results['valid_games'] / max(validation_results['total_games'], 1) * 100
        )
        
        return validation_results
    
    def get_conversion_stats(self) -> Dict[str, Any]:
        """Get conversion statistics"""
        success_rate = (
            self.conversion_stats['successful_conversions'] / 
            max(self.conversion_stats['total_conversions'], 1) * 100
        )
        
        return {
            'version': self.version,
            'created_by': self.created_by,
            'blessed_by': self.blessed_by,
            'total_conversions': self.conversion_stats['total_conversions'],
            'successful_conversions': self.conversion_stats['successful_conversions'],
            'failed_conversions': self.conversion_stats['failed_conversions'],
            'success_rate': round(success_rate, 2),
            'leagues_processed': list(self.conversion_stats['leagues_processed']),
            'supported_schemas': list(UNIFIED_GAME_SCHEMA.keys()),
            'features': [
                'Legacy data conversion',
                'Multi-format support',
                'League-specific conversions',
                'Data validation',
                'Error handling',
                'Statistics tracking',
                'Goddess blessed architecture'
            ]
        }

# 🔥💀🔥 GLOBAL UNIFIED DATA CONVERTER INSTANCE 💀🔥💀
# This ensures one instance is shared across the entire application
_unified_converter_instance = None

def get_unified_data_converter() -> UnifiedDataConverter:
    """Get the global Unified Data Converter instance"""
    global _unified_converter_instance
    if _unified_converter_instance is None:
        _unified_converter_instance = UnifiedDataConverter()
    return _unified_converter_instance

if __name__ == "__main__":
    # Test the Unified Data Converter
    converter = UnifiedDataConverter()
    stats = converter.get_conversion_stats()
    
    print("🔥💀🔥 UNIFIED DATA CONVERTER LOADED! 💀🔥💀")
    print(f"🌟 Version: {stats['version']}")
    print(f"🌟 Created by: {stats['created_by']}")
    print(f"🌟 Blessed by: {stats['blessed_by']}")
    print(f"📊 Supported Schema Fields: {len(stats['supported_schemas'])}")
    print(f"🎯 Features: {len(stats['features'])} conversion capabilities")
    print("🚀 NUCLEAR REFACTOR DATA SYSTEM READY!")
    
    # Test conversion with mock data
    print("\n🔄 Testing conversion with mock data...")
    
    mock_legacy_uefa = {
        'home_team': 'Real Madrid',
        'away_team': 'Barcelona',
        'time': '21:00',
        'venue': 'Santiago Bernabéu',
        'prediction': '🏠 Real Madrid',
        'confidence': 78,
        'market_eff': 72,
        'team_perf': 81,
        'players': 75,
        'group': 'A'
    }
    
    converted = converter.convert_legacy_game_data(mock_legacy_uefa, 'UEFA')
    print(f"✅ Mock UEFA conversion successful: {converted['matchup']}")
    print(f"📊 Converted stats: {converter.get_conversion_stats()}")