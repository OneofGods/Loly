#!/usr/bin/env python3
"""
🔥💀🔥 LEGENDARY ALGORITHM BACK TESTER - TRUTH SEEKER 💀🔥💀

CRITICAL VALIDATION SYSTEM
Tests if our legendary cultural mastery algorithms actually perform better
or if we just inflated confidence numbers without improving accuracy.

🚨 BRUTALLY HONEST ACCURACY TESTING! 🚨

Back tests last 20+ games for:
- MLS (American Soccer Cultural Mastery v2.0)
- Ligue 1 (French Football Cultural Mastery v2.0) 
- UEFA Europa League (European Cultural Mastery v2.0)

Created: November 1, 2025
Purpose: Validate legendary status claims with REAL results
"""

import asyncio
import aiohttp
import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import sys
import os

# Import our legendary algorithms
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from mls_real_algorithm import RealMLSAlgorithm
from ligue1_real_algorithm import RealLigue1Algorithm
from uefa_europa_league_real_algorithm import RealUEFAEuropaLeagueAlgorithm

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

class LegendaryBackTester:
    """
    🔥💀🔥 LEGENDARY ALGORITHM BACK TESTER
    
    Tests if our cultural mastery algorithms actually improve accuracy
    or if we just made confidence numbers higher without substance.
    """
    
    def __init__(self):
        """Initialize the brutal truth seeker"""
        self.espn_api_base = "https://site.api.espn.com/apis/site/v2/sports/soccer"
        
        # Initialize our legendary algorithms
        self.mls_algorithm = RealMLSAlgorithm()
        self.ligue1_algorithm = RealLigue1Algorithm() 
        self.europa_algorithm = RealUEFAEuropaLeagueAlgorithm()
        
        # League configurations for ESPN API
        self.leagues = {
            'MLS': {
                'espn_id': 'usa.1',
                'algorithm': self.mls_algorithm,
                'algorithm_method': 'apply_real_mls_algorithm',
                'name': 'MLS American Soccer Cultural Mastery v2.0'
            },
            'LIGUE1': {
                'espn_id': 'fra.1', 
                'algorithm': self.ligue1_algorithm,
                'algorithm_method': 'apply_real_ligue1_algorithm',
                'name': 'Ligue 1 French Football Cultural Mastery v2.0'
            },
            'UEFA_EUROPA': {
                'espn_id': 'uefa.europa',
                'algorithm': self.europa_algorithm, 
                'algorithm_method': 'apply_real_uefa_europa_league_algorithm',
                'name': 'UEFA Europa League European Cultural Mastery v2.0'
            }
        }
        
        logger.info("🔥💀🔥 Legendary Back Tester initialized - TRUTH SEEKER MODE ACTIVATED! 💀🔥💀")
    
    async def back_test_all_leagues(self, days_back: int = 30) -> Dict[str, Any]:
        """
        🎯 MAIN BACK TEST: Test all legendary algorithms against real results
        
        Args:
            days_back: How many days back to test (default 30 for good sample size)
            
        Returns:
            Comprehensive accuracy report for all leagues
        """
        print("🔥💀🔥 LEGENDARY ALGORITHM BACK TESTING INITIATED! 💀🔥💀")
        print("=" * 80)
        print(f"📅 Testing Period: Last {days_back} days")
        print(f"🎯 Target: Validate legendary status claims")
        print(f"⚠️ BRUTAL HONESTY MODE: No fake inflation allowed!")
        print("=" * 80)
        
        all_results = {}
        
        for league_code, league_config in self.leagues.items():
            print(f"\n🏆 TESTING {league_code}: {league_config['name']}")
            print("-" * 60)
            
            try:
                league_results = await self._back_test_league(
                    league_code, 
                    league_config, 
                    days_back
                )
                all_results[league_code] = league_results
                
                # Show immediate results
                accuracy = league_results.get('accuracy_percentage', 0)
                avg_confidence = league_results.get('average_confidence', 0)
                games_tested = league_results.get('games_tested', 0)
                
                print(f"📊 RESULTS for {league_code}:")
                print(f"   🎮 Games Tested: {games_tested}")
                print(f"   🎯 Accuracy: {accuracy:.1f}%")
                print(f"   📈 Avg Confidence: {avg_confidence:.1f}%")
                
                # Truth assessment
                if accuracy >= avg_confidence * 0.9:  # Within 10% of claimed confidence
                    print(f"   ✅ LEGENDARY STATUS: VALIDATED")
                elif accuracy >= avg_confidence * 0.8:  # Within 20% 
                    print(f"   ⚠️ LEGENDARY STATUS: QUESTIONABLE")
                else:
                    print(f"   ❌ LEGENDARY STATUS: INFLATED CLAIMS")
                    
            except Exception as e:
                logger.error(f"💀 Back test failed for {league_code}: {e}")
                all_results[league_code] = {'error': str(e)}
        
        # Generate final report
        final_report = self._generate_final_report(all_results)
        print(f"\n🏆 FINAL LEGENDARY VALIDATION REPORT:")
        print("=" * 80)
        print(final_report)
        
        return all_results
    
    async def _back_test_league(self, league_code: str, league_config: Dict, days_back: int) -> Dict[str, Any]:
        """
        🔍 Back test a specific league's legendary algorithm
        """
        completed_games = await self._fetch_completed_games(league_config['espn_id'], days_back)
        
        if not completed_games:
            return {
                'error': 'No completed games found',
                'games_tested': 0,
                'accuracy_percentage': 0,
                'average_confidence': 0
            }
        
        print(f"📋 Found {len(completed_games)} completed games for back testing")
        
        # Test each game with our legendary algorithm
        predictions = []
        correct_predictions = 0
        total_confidence = 0
        
        algorithm = league_config['algorithm']
        method_name = league_config['algorithm_method']
        
        for i, game in enumerate(completed_games[:20]):  # Test last 20 games max
            try:
                # Create game data for our algorithm
                game_data = {
                    'home_team': game['home_team'],
                    'away_team': game['away_team'],
                    'venue': game.get('venue', 'Unknown')
                }
                
                # Apply our legendary algorithm
                method = getattr(algorithm, method_name)
                prediction_result = await method(game_data)
                
                # Extract prediction and confidence
                algorithm_prediction = prediction_result.get('prediction', 'Unknown')
                confidence = prediction_result.get('confidence', 50)
                
                # Determine actual winner
                actual_winner = self._determine_actual_winner(game)
                
                # Check if our prediction was correct
                is_correct = self._is_prediction_correct(algorithm_prediction, actual_winner, game)
                
                if is_correct:
                    correct_predictions += 1
                
                total_confidence += confidence
                
                predictions.append({
                    'game_number': i + 1,
                    'matchup': f"{game['away_team']} @ {game['home_team']}",
                    'algorithm_prediction': algorithm_prediction,
                    'confidence': confidence,
                    'actual_winner': actual_winner,
                    'correct': is_correct,
                    'home_score': game.get('home_score', 0),
                    'away_score': game.get('away_score', 0)
                })
                
                # Show progress
                status = "✅" if is_correct else "❌"
                print(f"   {status} Game {i+1}: {game['away_team']} @ {game['home_team']} - {confidence:.1f}% confidence")
                
            except Exception as e:
                logger.error(f"💀 Error testing game {i+1}: {e}")
                continue
        
        # Calculate final metrics
        games_tested = len(predictions)
        accuracy_percentage = (correct_predictions / games_tested * 100) if games_tested > 0 else 0
        average_confidence = total_confidence / games_tested if games_tested > 0 else 0
        
        return {
            'league': league_code,
            'algorithm_name': league_config['name'],
            'games_tested': games_tested,
            'correct_predictions': correct_predictions,
            'accuracy_percentage': accuracy_percentage,
            'average_confidence': average_confidence,
            'predictions': predictions,
            'legendary_validated': accuracy_percentage >= average_confidence * 0.9
        }
    
    async def _fetch_completed_games(self, league_id: str, days_back: int) -> List[Dict[str, Any]]:
        """
        📅 Fetch completed games from ESPN API for back testing
        """
        completed_games = []
        
        async with aiohttp.ClientSession() as session:
            # Search through recent dates for completed games
            for days_ago in range(1, days_back + 1):
                target_date = datetime.now() - timedelta(days=days_ago)
                date_str = target_date.strftime("%Y%m%d")
                
                url = f"{self.espn_api_base}/{league_id}/scoreboard?dates={date_str}"
                
                try:
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()
                            events = data.get('events', [])
                            
                            for event in events:
                                # Only include completed games with final scores
                                status = event.get('status', {})
                                if status.get('type', {}).get('completed', False):
                                    game = self._parse_completed_game(event)
                                    if game:
                                        completed_games.append(game)
                                        
                except Exception as e:
                    logger.debug(f"Error fetching date {date_str}: {e}")
                    continue
                
                # Limit to avoid too many API calls
                if len(completed_games) >= 25:
                    break
        
        logger.info(f"📊 Fetched {len(completed_games)} completed games for back testing")
        return completed_games
    
    def _parse_completed_game(self, event: Dict) -> Dict[str, Any]:
        """
        🔍 Parse completed game from ESPN API data
        """
        try:
            competitions = event.get('competitions', [{}])
            if not competitions:
                return None
                
            competition = competitions[0]
            competitors = competition.get('competitors', [])
            
            if len(competitors) != 2:
                return None
            
            # Find home and away teams
            home_competitor = next((c for c in competitors if c.get('homeAway') == 'home'), None)
            away_competitor = next((c for c in competitors if c.get('homeAway') == 'away'), None)
            
            if not home_competitor or not away_competitor:
                return None
            
            home_team = home_competitor.get('team', {}).get('displayName', 'Unknown')
            away_team = away_competitor.get('team', {}).get('displayName', 'Unknown')
            home_score = int(home_competitor.get('score', '0') or '0')
            away_score = int(away_competitor.get('score', '0') or '0')
            
            venue = competition.get('venue', {}).get('fullName', 'Unknown')
            game_date = event.get('date', '')
            
            return {
                'home_team': home_team,
                'away_team': away_team,
                'home_score': home_score,
                'away_score': away_score,
                'venue': venue,
                'date': game_date,
                'espn_id': event.get('id', 'unknown')
            }
            
        except Exception as e:
            logger.error(f"💀 Error parsing completed game: {e}")
            return None
    
    def _determine_actual_winner(self, game: Dict) -> str:
        """
        🎯 Determine who actually won the game
        """
        home_score = game.get('home_score', 0)
        away_score = game.get('away_score', 0)
        home_team = game.get('home_team', 'Home')
        away_team = game.get('away_team', 'Away')
        
        if home_score > away_score:
            return f"🏠 {home_team}"
        elif away_score > home_score:
            return f"✈️ {away_team}"
        else:
            return "🤝 DRAW"
    
    def _is_prediction_correct(self, algorithm_prediction: str, actual_winner: str, game: Dict) -> bool:
        """
        ✅ Check if our algorithm prediction was correct
        """
        home_team = game.get('home_team', '').upper()
        away_team = game.get('away_team', '').upper()
        
        # Normalize predictions for comparison
        prediction_upper = algorithm_prediction.upper()
        actual_upper = actual_winner.upper()
        
        # Check for home team win
        if any(team_part in prediction_upper for team_part in home_team.split() if len(team_part) > 2):
            return any(team_part in actual_upper for team_part in home_team.split() if len(team_part) > 2)
        
        # Check for away team win  
        if any(team_part in prediction_upper for team_part in away_team.split() if len(team_part) > 2):
            return any(team_part in actual_upper for team_part in away_team.split() if len(team_part) > 2)
        
        # Check for draw
        if 'DRAW' in prediction_upper or '🤝' in prediction_upper:
            return 'DRAW' in actual_upper or '🤝' in actual_upper
        
        # Default to false if we can't determine
        return False
    
    def _generate_final_report(self, all_results: Dict) -> str:
        """
        📊 Generate comprehensive final validation report
        """
        report = []
        report.append("🏆 LEGENDARY ALGORITHM VALIDATION SUMMARY")
        report.append("=" * 60)
        
        total_games = 0
        total_correct = 0
        total_claimed_confidence = 0
        leagues_tested = 0
        
        for league_code, results in all_results.items():
            if 'error' in results:
                report.append(f"❌ {league_code}: {results['error']}")
                continue
            
            games = results.get('games_tested', 0)
            correct = results.get('correct_predictions', 0)
            accuracy = results.get('accuracy_percentage', 0)
            confidence = results.get('average_confidence', 0)
            validated = results.get('legendary_validated', False)
            
            total_games += games
            total_correct += correct
            total_claimed_confidence += confidence
            leagues_tested += 1
            
            status = "✅ VALIDATED" if validated else "❌ INFLATED"
            report.append(f"🏆 {league_code}:")
            report.append(f"   📊 Accuracy: {accuracy:.1f}% | Claimed: {confidence:.1f}% | {status}")
        
        # Overall metrics
        if leagues_tested > 0:
            overall_accuracy = (total_correct / total_games * 100) if total_games > 0 else 0
            avg_claimed_confidence = total_claimed_confidence / leagues_tested
            
            report.append("")
            report.append("🎯 OVERALL LEGENDARY STATUS:")
            report.append(f"   🎮 Total Games Tested: {total_games}")
            report.append(f"   🎯 Overall Accuracy: {overall_accuracy:.1f}%")
            report.append(f"   📈 Avg Claimed Confidence: {avg_claimed_confidence:.1f}%")
            
            if overall_accuracy >= avg_claimed_confidence * 0.9:
                report.append("   🏆👑 LEGENDARY STATUS: FULLY VALIDATED! ✅")
            elif overall_accuracy >= avg_claimed_confidence * 0.8:
                report.append("   ⚠️ LEGENDARY STATUS: NEEDS MINOR ADJUSTMENT")
            else:
                report.append("   ❌ LEGENDARY STATUS: CLAIMS INFLATED - NEEDS MAJOR REVISION")
        
        return "\n".join(report)


async def main():
    """Run the legendary algorithm back test"""
    print("🔥💀🔥 LEGENDARY ALGORITHM BACK TESTING SYSTEM 💀🔥💀")
    print("🎯 MISSION: Validate our cultural mastery claims with REAL results!")
    print()
    
    tester = LegendaryBackTester()
    results = await tester.back_test_all_leagues(days_back=21)  # 3 weeks back test
    
    # Save results to file for analysis
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"legendary_back_test_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\n💾 Detailed results saved to: {results_file}")
    print("🎯 LEGENDARY VALIDATION COMPLETE!")


if __name__ == "__main__":
    asyncio.run(main())