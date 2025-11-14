#!/usr/bin/env python3
"""
🔥💀🔥 PROGOL RESULT CHECKER - AUTOMATIC RESULT TRACKING SYSTEM 🔥💀🔥
Automatically fetches PROGOL results and updates prediction tracking
"""

import asyncio
import json
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional
import aiohttp
from pathlib import Path

logger = logging.getLogger(__name__)

class ProgolResultChecker:
    """
    🎰 PROGOL RESULT CHECKER 🎰
    
    Automatically checks PROGOL results and updates predictions
    """
    
    def __init__(self):
        # 🔥💀🔥 USE MIDNIGHT SPECIAL PREDICTIONS FILE FOR PROPER INTEGRATION! 💀🔥💀
        self.predictions_file = Path('/tmp/midnight_predictions.json')
        self.results_cache_file = Path('/tmp/progol_results_cache.json')
        
        # Also check daily predictions as fallback
        self.daily_predictions_file = Path('/Users/onecoder/Projects/Total_AI_Liberation/dockerized_decentralized_agent_poly_loly/data/daily_predictions.json')
        self.progol_url = "https://www.loterianacional.gob.mx/Progol"
        self.quinielaposible_url = "https://quinielaposible.com"
        logger.info("🎰 PROGOL RESULT CHECKER INITIALIZED")
    
    async def check_and_update_all_results(self) -> Dict:
        """
        🔥 CHECK AND UPDATE ALL RESULTS
        
        Main function to check all pending PROGOL predictions and update results
        """
        try:
            logger.info("🔥💀🔥 STARTING AUTOMATIC PROGOL RESULT CHECK 💀🔥💀")
            
            # Load current predictions
            predictions = self._load_predictions()
            if not predictions:
                logger.warning("⚠️ No predictions found to check")
                return {"status": "no_predictions", "updated": 0}
            
            # Get pending PROGOL predictions
            pending_progol = self._get_pending_progol_predictions(predictions)
            if not pending_progol:
                logger.info("✅ No pending PROGOL predictions to check")
                return {"status": "no_pending", "updated": 0}
            
            logger.info(f"🎯 Found {len(pending_progol)} pending PROGOL predictions to check")
            
            # Fetch latest PROGOL results
            progol_results = await self._fetch_progol_results()
            if not progol_results:
                logger.warning("⚠️ Could not fetch PROGOL results")
                return {"status": "no_results", "updated": 0}
            
            # Update predictions with results
            updates_made = 0
            for prediction in pending_progol:
                if await self._update_prediction_result(prediction, progol_results):
                    updates_made += 1
            
            if updates_made > 0:
                # Save updated predictions
                self._save_predictions(predictions)
                logger.info(f"🎯 AUTOMATION SUCCESS: Updated {updates_made} PROGOL predictions!")
            
            return {
                "status": "success",
                "checked": len(pending_progol),
                "updated": updates_made,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"💀 ERROR IN AUTOMATIC RESULT CHECK: {e}")
            return {"status": "error", "error": str(e)}
    
    def _load_predictions(self) -> List[Dict]:
        """Load predictions from midnight_predictions.json with daily fallback"""
        try:
            # 🔥💀🔥 PRIMARY: Load from midnight special predictions file! 💀🔥💀
            if self.predictions_file.exists():
                with open(self.predictions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Handle both list and dict formats
                    if isinstance(data, list):
                        logger.info(f"📊 Loaded {len(data)} predictions from midnight_predictions.json")
                        return data
                    elif isinstance(data, dict):
                        # Check if it's the daily_predictions.json format with 'games' key
                        if 'games' in data and isinstance(data['games'], list):
                            logger.info(f"📊 Loaded {len(data['games'])} predictions from midnight_predictions.json (games format)")
                            return data['games']
                        else:
                            # If it's a dict with dates as keys, flatten to list
                            predictions = []
                            for date_predictions in data.values():
                                if isinstance(date_predictions, list):
                                    predictions.extend(date_predictions)
                                elif isinstance(date_predictions, dict) and 'games' in date_predictions:
                                    predictions.extend(date_predictions['games'])
                            logger.info(f"📊 Loaded {len(predictions)} predictions from midnight_predictions.json (flattened format)")
                            return predictions
                    else:
                        logger.warning(f"Unexpected data format in midnight predictions file: {type(data)}")
            
            # 🔄 FALLBACK: Load from daily predictions if midnight file not available
            logger.info("⚠️ Midnight predictions not found, checking daily predictions fallback...")
            if self.daily_predictions_file.exists():
                with open(self.daily_predictions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        logger.info(f"📊 Loaded {len(data)} predictions from daily_predictions.json fallback")
                        return data
                    elif isinstance(data, dict) and 'games' in data:
                        logger.info(f"📊 Loaded {len(data['games'])} predictions from daily_predictions.json fallback (games format)")
                        return data['games']
            
            logger.warning("⚠️ No predictions found in either midnight or daily files")
            return []
            
        except Exception as e:
            logger.error(f"Error loading predictions: {e}")
            return []
    
    def _save_predictions(self, predictions: List[Dict]) -> bool:
        """Save updated predictions to midnight file - maintain original format"""
        try:
            saved_to_midnight = False
            
            # 🔥💀🔥 PRIMARY: Save to midnight special predictions file! 💀🔥💀
            # Try to maintain the original format
            if self.predictions_file.exists():
                with open(self.predictions_file, 'r', encoding='utf-8') as f:
                    original_data = json.load(f)
                
                # If original was dict format with 'games' key, maintain it
                if isinstance(original_data, dict) and 'games' in original_data:
                    original_data['games'] = predictions
                    original_data['timestamp'] = datetime.now().isoformat()
                    with open(self.predictions_file, 'w', encoding='utf-8') as f:
                        json.dump(original_data, f, indent=2, ensure_ascii=False)
                    logger.info(f"✅ Updated midnight_predictions.json with {len(predictions)} predictions (games format)")
                    saved_to_midnight = True
                else:
                    # Save as list format
                    with open(self.predictions_file, 'w', encoding='utf-8') as f:
                        json.dump(predictions, f, indent=2, ensure_ascii=False)
                    logger.info(f"✅ Updated midnight_predictions.json with {len(predictions)} predictions (list format)")
                    saved_to_midnight = True
            else:
                # Create new file as list
                with open(self.predictions_file, 'w', encoding='utf-8') as f:
                    json.dump(predictions, f, indent=2, ensure_ascii=False)
                logger.info(f"✅ Created midnight_predictions.json with {len(predictions)} predictions")
                saved_to_midnight = True
            
            # 🔄 ALSO UPDATE DAILY FILE FOR BACKUP/CONSISTENCY
            try:
                if self.daily_predictions_file.exists():
                    with open(self.daily_predictions_file, 'r', encoding='utf-8') as f:
                        daily_data = json.load(f)
                    
                    if isinstance(daily_data, dict) and 'games' in daily_data:
                        daily_data['games'] = predictions
                        daily_data['timestamp'] = datetime.now().isoformat()
                        with open(self.daily_predictions_file, 'w', encoding='utf-8') as f:
                            json.dump(daily_data, f, indent=2, ensure_ascii=False)
                        logger.info("🔄 Also updated daily_predictions.json for consistency")
            except Exception as e:
                logger.warning(f"Failed to update daily predictions backup: {e}")
            
            return saved_to_midnight
            
        except Exception as e:
            logger.error(f"Error saving predictions: {e}")
            return False
    
    def _get_pending_progol_predictions(self, predictions: List[Dict]) -> List[Dict]:
        """Get all pending PROGOL predictions that need result checking"""
        pending = []
        for prediction in predictions:
            # Check for PROGOL leagues and not yet completed
            league = prediction.get('league', '').upper()
            sport = prediction.get('sport', '').upper()
            game_completed = prediction.get('game_completed', False)
            
            if ('PROGOL' in league or 'PROGOL' in sport) and not game_completed:
                # Check if game time has passed (should be finished)
                game_time_str = prediction.get('game_time', '')
                if game_time_str:
                    try:
                        # Parse game time
                        game_time = datetime.fromisoformat(game_time_str.replace('Z', '+00:00'))
                        current_time = datetime.now(timezone.utc)
                        
                        # If game was more than 3 hours ago, it should be finished
                        if current_time > game_time + timedelta(hours=3):
                            pending.append(prediction)
                            logger.info(f"🎯 Pending PROGOL: {prediction.get('away_team', 'Unknown')} @ {prediction.get('home_team', 'Unknown')}")
                    except Exception as e:
                        logger.warning(f"Error parsing game time for {prediction.get('game_id', 'unknown')}: {e}")
                        # Add anyway if time parsing fails
                        pending.append(prediction)
        
        return pending
    
    async def _fetch_progol_results(self) -> Optional[Dict]:
        """
        🎰 FETCH PROGOL RESULTS
        
        Fetches latest PROGOL results from Mexican Government and quinielaposible
        """
        try:
            # Try multiple sources for PROGOL results
            results = {}
            
            # Source 1: Official Mexican Government
            logger.info("🎰 Fetching PROGOL results from Mexican Government...")
            gov_results = await self._fetch_government_progol_results()
            if gov_results:
                results.update(gov_results)
            
            # Source 2: Quinielaposible.com
            logger.info("🎰 Fetching PROGOL results from quinielaposible.com...")
            quinielaposible_results = await self._fetch_quinielaposible_results()
            if quinielaposible_results:
                results.update(quinielaposible_results)
            
            # Cache results
            if results:
                self._cache_results(results)
                logger.info(f"✅ PROGOL results fetched: {len(results)} games found")
            
            return results if results else None
            
        except Exception as e:
            logger.error(f"Error fetching PROGOL results: {e}")
            return None
    
    async def _fetch_government_progol_results(self) -> Optional[Dict]:
        """Fetch results from official Mexican Government PROGOL site"""
        try:
            # Create SSL context that ignores certificate verification for Mexican government site
            import ssl
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            connector = aiohttp.TCPConnector(ssl=ssl_context)
            
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(self.progol_url, timeout=15) as response:
                    if response.status == 200:
                        html_content = await response.text()
                        return self._parse_government_results(html_content)
            return None
        except Exception as e:
            logger.warning(f"Error fetching government PROGOL results: {e}")
            return None
    
    async def _fetch_quinielaposible_results(self) -> Optional[Dict]:
        """Fetch results from quinielaposible.com"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.quinielaposible_url}/resultados", timeout=10) as response:
                    if response.status == 200:
                        html_content = await response.text()
                        return self._parse_quinielaposible_results(html_content)
            return None
        except Exception as e:
            logger.warning(f"Error fetching quinielaposible results: {e}")
            return None
    
    def _parse_government_results(self, html_content: str) -> Dict:
        """Parse PROGOL results from government HTML"""
        results = {}
        try:
            # Look for completed games with scores
            # Pattern: Team1 vs Team2 (score1-score2)
            score_patterns = [
                r'([A-ZÑÁÉÍÓÚ\s\.]+)\s+vs\s+([A-ZÑÁÉÍÓÚ\s\.]+)\s+\((\d+)-(\d+)\)',
                r'([A-ZÑÁÉÍÓÚ\s\.]+)\s+(\d+)-(\d+)\s+([A-ZÑÁÉÍÓÚ\s\.]+)',
                r'([A-ZÑÁÉÍÓÚ\s\.]+)\s*:\s*(\d+)\s*-\s*([A-ZÑÁÉÍÓÚ\s\.]+)\s*:\s*(\d+)'
            ]
            
            for pattern in score_patterns:
                matches = re.finditer(pattern, html_content, re.IGNORECASE)
                for match in matches:
                    if len(match.groups()) == 4:
                        team1, score1, team2, score2 = match.groups()
                        self._add_result_to_dict(results, team1.strip(), team2.strip(), 
                                               int(score1), int(score2))
            
            logger.info(f"🎰 Parsed {len(results)} results from government site")
            
        except Exception as e:
            logger.warning(f"Error parsing government results: {e}")
        
        return results
    
    def _parse_quinielaposible_results(self, html_content: str) -> Dict:
        """Parse PROGOL results from quinielaposible.com"""
        results = {}
        try:
            # Look for score patterns in quinielaposible format
            patterns = [
                r'([A-ZÑÁÉÍÓÚ\s\.]+)\s+(\d+)\s*-\s*(\d+)\s+([A-ZÑÁÉÍÓÚ\s\.]+)',
                r'<td[^>]*>([^<]+)</td>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>([^<]+)</td>'
            ]
            
            for pattern in patterns:
                matches = re.finditer(pattern, html_content, re.IGNORECASE)
                for match in matches:
                    if len(match.groups()) == 4:
                        team1, score1, score2, team2 = match.groups()
                        self._add_result_to_dict(results, team1.strip(), team2.strip(), 
                                               int(score1), int(score2))
            
            logger.info(f"🎰 Parsed {len(results)} results from quinielaposible.com")
            
        except Exception as e:
            logger.warning(f"Error parsing quinielaposible results: {e}")
        
        return results
    
    def _add_result_to_dict(self, results: Dict, team1: str, team2: str, score1: int, score2: int):
        """Add a game result to the results dictionary"""
        try:
            # Clean team names
            team1 = self._clean_team_name(team1)
            team2 = self._clean_team_name(team2)
            
            # Determine winner
            if score1 > score2:
                winner = team1
                result_type = "home_win"
            elif score2 > score1:
                winner = team2
                result_type = "away_win"
            else:
                winner = "DRAW"
                result_type = "draw"
            
            # Create unique game key
            game_key = f"{team1}_vs_{team2}".upper()
            
            results[game_key] = {
                "home_team": team1,
                "away_team": team2,
                "home_score": score1,
                "away_score": score2,
                "winner": winner,
                "result_type": result_type,
                "found_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.warning(f"Error adding result {team1} vs {team2}: {e}")
    
    def _clean_team_name(self, team_name: str) -> str:
        """Clean and standardize team names"""
        # Remove extra whitespace and common prefixes/suffixes
        cleaned = team_name.strip()
        cleaned = re.sub(r'\s+', ' ', cleaned)  # Multiple spaces to single
        cleaned = cleaned.upper()
        
        # Common team name mappings for PROGOL
        mappings = {
            'CRUZ AZUL': 'C. AZUL',
            'ATLÉTICO DE SAN LUIS': 'SAN LUIS',
            'PUMAS UNAM': 'PUMAS',
            'FC JUÁREZ': 'JUÁREZ',
            'MAZATLÁN FC': 'MAZATLÁN',
            'PACHUCA CF': 'PACHUCA'
        }
        
        for full_name, short_name in mappings.items():
            if full_name in cleaned:
                cleaned = short_name
                break
        
        return cleaned
    
    async def _update_prediction_result(self, prediction: Dict, progol_results: Dict) -> bool:
        """Update a prediction with its actual result"""
        try:
            home_team = prediction.get('home_team', '').upper()
            away_team = prediction.get('away_team', '').upper()
            predicted_winner = prediction.get('predicted_winner', '').upper()
            
            # Try different game key formats
            possible_keys = [
                f"{away_team}_vs_{home_team}",
                f"{home_team}_vs_{away_team}",
                f"{away_team}_{home_team}",
                f"{home_team}_{away_team}"
            ]
            
            result_found = None
            for key in possible_keys:
                if key in progol_results:
                    result_found = progol_results[key]
                    break
            
            if not result_found:
                # Try fuzzy matching
                for game_key, game_result in progol_results.items():
                    if (home_team in game_key and away_team in game_key) or \
                       (away_team in game_key and home_team in game_key):
                        result_found = game_result
                        break
            
            if result_found:
                # Update prediction with actual result
                actual_winner = result_found['winner']
                prediction['actual_winner'] = actual_winner
                prediction['game_completed'] = True
                prediction['result_checked'] = True
                prediction['actual_scores'] = {
                    'home': result_found['home_score'],
                    'away': result_found['away_score']
                }
                
                # Check if prediction was correct - handle draw comparisons properly
                def normalize_draw(winner_text):
                    """Normalize draw text for comparison"""
                    if not winner_text:
                        return ""
                    text = str(winner_text).upper().strip()
                    # Remove emojis and standardize draw text
                    if 'DRAW' in text or '🤝' in text:
                        return "DRAW"
                    return text
                
                normalized_predicted = normalize_draw(predicted_winner)
                normalized_actual = normalize_draw(actual_winner)
                prediction_correct = (normalized_predicted == normalized_actual)
                prediction['prediction_correct'] = prediction_correct
                
                # Add result timestamp
                prediction['result_updated'] = datetime.now().isoformat()
                
                logger.info(f"✅ RESULT UPDATED: {away_team} @ {home_team} - Predicted: {predicted_winner}, Actual: {actual_winner}, Correct: {prediction_correct}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error updating prediction result: {e}")
            return False
    
    def _cache_results(self, results: Dict):
        """Cache fetched results for debugging"""
        try:
            cache_data = {
                "timestamp": datetime.now().isoformat(),
                "results": results
            }
            with open(self.results_cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.warning(f"Error caching results: {e}")

async def main():
    """Test the PROGOL result checker"""
    print("🎰🔥🎰 TESTING PROGOL RESULT CHECKER 🎰🔥🎰")
    
    checker = ProgolResultChecker()
    result = await checker.check_and_update_all_results()
    
    print(f"📊 Result Check Complete: {result}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())