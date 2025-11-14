#!/usr/bin/env python3
"""
💀🔥💀 HARDCORE ACCURACY CRITIC - NO BULLSHIT PERFORMANCE ANALYSIS
The most brutal and honest analysis system for BUILD TO WIN mentality!

MISSION:
- Absolutely DESTROY our ego with honest criticism
- Find EVERY weakness and failure pattern
- Provide BRUTAL but constructive feedback
- Force SYSTEMATIC improvement or we're fucked!
"""

import json
import asyncio
from datetime import datetime, timedelta
from pathlib import Path
import statistics
import logging
from typing import Dict, List, Any

class HardcoreAccuracyCritic:
    def __init__(self):
        self.predictions_file = Path("/tmp/midnight_predictions.json")
        self.learning_db = Path("/tmp/midnight_learning_db.json")
        self.critic_reports = Path("/tmp/hardcore_critic_reports")
        
        # Create reports directory
        self.critic_reports.mkdir(exist_ok=True)
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Accuracy standards - WE DEMAND EXCELLENCE!
        self.standards = {
            "ELITE": 85,      # Professional level
            "GOOD": 70,       # Acceptable
            "MEDIOCRE": 55,   # Needs improvement  
            "TERRIBLE": 45,   # Fucking embarrassing
            "DISASTER": 0     # Complete failure
        }
    
    async def brutal_accuracy_analysis(self, days_back: int = 7, league: str = 'ALL', centralized_data: dict = None):
        """
        🔥💀 BRUTAL ACCURACY ANALYSIS - NO MERCY, NO EXCUSES!
        
        This function will DESTROY our confidence and rebuild it properly!
        🔥💀🔥 BROTHER #161: NOW SUPPORTS CENTRALIZED DATA FROM AUTOMATION PANEL! 💀🔥💀
        """
        try:
            print("💀🔥💀 INITIATING HARDCORE ACCURACY CRITICISM 💀🔥💀")
            print("⚠️  WARNING: This analysis shows NO MERCY!")
            print("🎯 GET READY FOR SOME HARD TRUTHS...\n")
            
            # 🔥💀🔥 BROTHER #161: USE CENTRALIZED DATA FROM AUTOMATION PANEL! 💀🔥💀
            if centralized_data and league != 'ALL':
                print(f"🎰 USING CENTRALIZED AUTOMATION PANEL DATA FOR {league}!")
                predictions = centralized_data
                learning_db = {}  # Use centralized data instead of independent files
            else:
                # Fallback to independent files for backwards compatibility
                predictions = self._load_json(self.predictions_file)
                learning_db = self._load_json(self.learning_db)
            
            # Analyze recent performance
            analysis = await self._perform_deep_analysis(predictions, days_back)
            
            # Generate brutal criticism
            criticism = self._generate_brutal_criticism(analysis)
            
            # Create improvement demands
            demands = self._create_improvement_demands(analysis)
            
            # Compile hardcore report
            report = {
                "analysis_date": datetime.now().isoformat(),
                "period_analyzed": f"Last {days_back} days",
                "raw_analysis": analysis,
                "brutal_criticism": criticism,
                "improvement_demands": demands,
                "verdict": self._render_final_verdict(analysis)
            }
            
            # Save report
            report_file = self.critic_reports / f"hardcore_criticism_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            self._save_json(report_file, report)
            
            # Display brutal feedback
            await self._display_brutal_feedback(report)
            
            return report
            
        except Exception as e:
            print(f"💀 CRITIC SYSTEM ERROR: {e}")
            return None
    
    async def _perform_deep_analysis(self, predictions: dict, days_back: int):
        """Perform deep statistical analysis of recent predictions"""
        
        analysis = {
            "time_period": {
                "days_analyzed": days_back,
                "start_date": (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d'),
                "end_date": datetime.now().strftime('%Y-%m-%d')
            },
            "overall_stats": {},
            "league_performance": {},
            "confidence_calibration": {},
            "pick_type_analysis": {},
            "temporal_trends": {},
            "failure_patterns": {},
            "red_flags": []
        }
        
        # Collect recent predictions
        recent_predictions = []
        cutoff_date = datetime.now() - timedelta(days=days_back)
        
        for date_str, date_predictions in predictions.items():
            try:
                pred_date = datetime.strptime(date_str, '%Y-%m-%d')
                if pred_date >= cutoff_date:
                    for game_id, prediction in date_predictions.items():
                        if prediction.get('status') in ['correct', 'incorrect']:
                            recent_predictions.append({
                                'date': date_str,
                                'game_id': game_id,
                                **prediction
                            })
            except:
                continue
        
        if not recent_predictions:
            analysis["red_flags"].append("🚨 NO RECENT PREDICTIONS FOUND - SYSTEM NOT WORKING!")
            return analysis
        
        # Overall statistics
        total_predictions = len(recent_predictions)
        correct_predictions = sum(1 for p in recent_predictions if p['status'] == 'correct')
        accuracy = (correct_predictions / total_predictions * 100) if total_predictions > 0 else 0
        
        analysis["overall_stats"] = {
            "total_predictions": total_predictions,
            "correct_predictions": correct_predictions,
            "incorrect_predictions": total_predictions - correct_predictions,
            "accuracy_percentage": round(accuracy, 2),
            "performance_grade": self._get_performance_grade(accuracy),
            "predictions_per_day": round(total_predictions / days_back, 2)
        }
        
        # League performance analysis
        league_stats = {}
        for prediction in recent_predictions:
            league = prediction.get('league', 'Unknown')
            if league not in league_stats:
                league_stats[league] = {'total': 0, 'correct': 0, 'accuracies': []}
            
            league_stats[league]['total'] += 1
            if prediction['status'] == 'correct':
                league_stats[league]['correct'] += 1
        
        for league, stats in league_stats.items():
            accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
            league_stats[league]['accuracy'] = round(accuracy, 2)
            league_stats[league]['grade'] = self._get_performance_grade(accuracy)
        
        analysis["league_performance"] = league_stats
        
        # Confidence calibration analysis
        confidence_buckets = {
            "90-100%": [],
            "80-89%": [],
            "70-79%": [],
            "60-69%": [],
            "50-59%": [],
            "below_50%": []
        }
        
        for prediction in recent_predictions:
            confidence = prediction['prediction']['confidence']
            is_correct = prediction['status'] == 'correct'
            
            if confidence >= 90:
                confidence_buckets["90-100%"].append(is_correct)
            elif confidence >= 80:
                confidence_buckets["80-89%"].append(is_correct)
            elif confidence >= 70:
                confidence_buckets["70-79%"].append(is_correct)
            elif confidence >= 60:
                confidence_buckets["60-69%"].append(is_correct)
            elif confidence >= 50:
                confidence_buckets["50-59%"].append(is_correct)
            else:
                confidence_buckets["below_50%"].append(is_correct)
        
        # Calculate calibration accuracy
        calibration = {}
        for bucket, results in confidence_buckets.items():
            if results:
                actual_accuracy = sum(results) / len(results) * 100
                calibration[bucket] = {
                    "predictions": len(results),
                    "actual_accuracy": round(actual_accuracy, 2),
                    "expected_range": bucket
                }
        
        analysis["confidence_calibration"] = calibration
        
        # Pick type analysis (Home/Away/Draw)
        pick_stats = {"home": [], "away": [], "draw": []}
        
        for prediction in recent_predictions:
            pick = prediction['prediction']['pick']
            is_correct = prediction['status'] == 'correct'
            
            if pick in ['🏠', 'HOME']:
                pick_stats["home"].append(is_correct)
            elif pick in ['✈️', 'AWAY']:
                pick_stats["away"].append(is_correct)
            elif pick in ['🤝', 'DRAW']:
                pick_stats["draw"].append(is_correct)
        
        pick_analysis = {}
        for pick_type, results in pick_stats.items():
            if results:
                accuracy = sum(results) / len(results) * 100
                pick_analysis[pick_type] = {
                    "predictions": len(results),
                    "accuracy": round(accuracy, 2),
                    "grade": self._get_performance_grade(accuracy)
                }
        
        analysis["pick_type_analysis"] = pick_analysis
        
        # Identify failure patterns and red flags
        analysis["failure_patterns"] = self._identify_failure_patterns(recent_predictions)
        analysis["red_flags"] = self._identify_red_flags(analysis)
        
        return analysis
    
    def _generate_brutal_criticism(self, analysis: dict):
        """Generate absolutely brutal but constructive criticism"""
        
        criticism = {
            "overall_performance": [],
            "league_disasters": [],
            "confidence_delusions": [],
            "systematic_failures": [],
            "embarrassing_patterns": []
        }
        
        overall_accuracy = analysis["overall_stats"]["accuracy_percentage"]
        
        # Overall performance criticism
        if overall_accuracy < self.standards["TERRIBLE"]:
            criticism["overall_performance"].append(
                f"💀 ABSOLUTELY FUCKING TERRIBLE: {overall_accuracy}% accuracy is a complete disgrace!"
            )
            criticism["overall_performance"].append(
                "🚨 You're basically flipping a coin and losing! This is embarrassing!"
            )
        elif overall_accuracy < self.standards["MEDIOCRE"]:
            criticism["overall_performance"].append(
                f"😤 MEDIOCRE BULLSHIT: {overall_accuracy}% is barely acceptable amateur hour!"
            )
            criticism["overall_performance"].append(
                "⚠️ You need to get your shit together IMMEDIATELY!"
            )
        elif overall_accuracy < self.standards["GOOD"]:
            criticism["overall_performance"].append(
                f"🙄 AVERAGE PERFORMANCE: {overall_accuracy}% - you're not terrible but not impressive either."
            )
        elif overall_accuracy < self.standards["ELITE"]:
            criticism["overall_performance"].append(
                f"👍 GOOD WORK: {overall_accuracy}% is respectable but there's room for improvement."
            )
        else:
            criticism["overall_performance"].append(
                f"🔥 ELITE PERFORMANCE: {overall_accuracy}% - now THIS is what we're talking about!"
            )
        
        # League-specific disasters
        for league, stats in analysis["league_performance"].items():
            if stats["accuracy"] < self.standards["TERRIBLE"]:
                criticism["league_disasters"].append(
                    f"💀 {league}: {stats['accuracy']}% - COMPLETE DISASTER! You know NOTHING about this league!"
                )
            elif stats["accuracy"] < self.standards["MEDIOCRE"]:
                criticism["league_disasters"].append(
                    f"😠 {league}: {stats['accuracy']}% - Embarrassingly bad performance!"
                )
        
        # Confidence calibration criticism
        for bucket, data in analysis["confidence_calibration"].items():
            expected_min = int(bucket.split('-')[0].replace('%', '')) if '-' in bucket else 50
            actual = data["actual_accuracy"]
            
            if actual < expected_min - 20:
                criticism["confidence_delusions"].append(
                    f"🤡 {bucket} confidence: {actual}% actual - you're DELUSIONAL about your abilities!"
                )
            elif actual < expected_min - 10:
                criticism["confidence_delusions"].append(
                    f"😬 {bucket} confidence: {actual}% actual - significant overconfidence detected!"
                )
        
        # Systematic failure identification
        pick_analysis = analysis["pick_type_analysis"]
        for pick_type, data in pick_analysis.items():
            if data["accuracy"] < self.standards["TERRIBLE"]:
                criticism["systematic_failures"].append(
                    f"💀 {pick_type.upper()} picks: {data['accuracy']}% - SYSTEMATIC FAILURE detected!"
                )
        
        return criticism
    
    def _create_improvement_demands(self, analysis: dict):
        """Create specific, actionable improvement demands"""
        
        demands = {
            "immediate_actions": [],
            "systematic_changes": [],
            "learning_priorities": [],
            "performance_targets": {},
            "deadline": (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        }
        
        overall_accuracy = analysis["overall_stats"]["accuracy_percentage"]
        
        # Immediate actions based on performance
        if overall_accuracy < self.standards["MEDIOCRE"]:
            demands["immediate_actions"].extend([
                "🚨 STOP making predictions until you fix your methodology!",
                "📚 RESEARCH your worst-performing leagues EXTENSIVELY!",
                "🔍 ANALYZE every single failed prediction from this week!",
                "⚠️ REDUCE confidence levels by 20% across the board!"
            ])
        
        # League-specific demands
        for league, stats in analysis["league_performance"].items():
            if stats["accuracy"] < self.standards["MEDIOCRE"]:
                demands["learning_priorities"].append(
                    f"📚 URGENT: Master {league} fundamentals - current {stats['accuracy']}% is unacceptable!"
                )
        
        # Confidence calibration fixes
        for bucket, data in analysis["confidence_calibration"].items():
            if data["actual_accuracy"] < int(bucket.split('-')[0].replace('%', '')) - 15:
                demands["systematic_changes"].append(
                    f"🎯 FIX confidence calibration for {bucket} - you're overconfident!"
                )
        
        # Performance targets
        target_accuracy = min(overall_accuracy + 10, 85)  # Reasonable improvement
        demands["performance_targets"] = {
            "overall_accuracy": f"{target_accuracy}% minimum within 7 days",
            "league_minimums": "60% minimum for ALL leagues",
            "confidence_calibration": "Within 10% of stated confidence levels",
            "consistency": "No more than 15% accuracy variation between leagues"
        }
        
        return demands
    
    def _render_final_verdict(self, analysis: dict):
        """Render the final verdict on performance"""
        
        overall_accuracy = analysis["overall_stats"]["accuracy_percentage"]
        
        if overall_accuracy >= self.standards["ELITE"]:
            return {
                "verdict": "ELITE PERFORMANCE",
                "emoji": "🔥👑🔥",
                "message": "You're operating at professional level! Keep this shit up!",
                "action": "MAINTAIN EXCELLENCE"
            }
        elif overall_accuracy >= self.standards["GOOD"]:
            return {
                "verdict": "GOOD PERFORMANCE", 
                "emoji": "👍✅👍",
                "message": "Solid work but there's room for improvement.",
                "action": "PUSH FOR ELITE STATUS"
            }
        elif overall_accuracy >= self.standards["MEDIOCRE"]:
            return {
                "verdict": "MEDIOCRE PERFORMANCE",
                "emoji": "😐⚠️😐", 
                "message": "You're average. Average is the enemy of great.",
                "action": "IMMEDIATE IMPROVEMENT REQUIRED"
            }
        elif overall_accuracy >= self.standards["TERRIBLE"]:
            return {
                "verdict": "TERRIBLE PERFORMANCE",
                "emoji": "💀😠💀",
                "message": "This is fucking embarrassing. Get your shit together!",
                "action": "EMERGENCY INTERVENTION NEEDED"
            }
        else:
            return {
                "verdict": "COMPLETE DISASTER",
                "emoji": "🚨💀🚨",
                "message": "You're worse than random chance. Stop immediately and rebuild from scratch!",
                "action": "TOTAL SYSTEM OVERHAUL"
            }
    
    async def _display_brutal_feedback(self, report: dict):
        """Display the brutal feedback in an intimidating format"""
        
        print("\n" + "="*80)
        print("💀🔥💀 HARDCORE ACCURACY CRITIC REPORT 💀🔥💀")
        print("="*80)
        
        # Overall verdict
        verdict = report["verdict"]
        print(f"\n{verdict['emoji']} FINAL VERDICT: {verdict['verdict']} {verdict['emoji']}")
        print(f"📝 {verdict['message']}")
        print(f"⚡ ACTION REQUIRED: {verdict['action']}\n")
        
        # Statistics
        stats = report["raw_analysis"]["overall_stats"]
        print("📊 BRUTAL STATISTICS:")
        print(f"   🎯 Accuracy: {stats['accuracy_percentage']}%")
        print(f"   ✅ Correct: {stats['correct_predictions']}")
        print(f"   ❌ Wrong: {stats['incorrect_predictions']}")
        print(f"   📈 Grade: {stats['performance_grade']}")
        
        # Brutal criticism
        criticism = report["brutal_criticism"]
        if criticism["overall_performance"]:
            print("\n💀 OVERALL PERFORMANCE CRITICISM:")
            for critic in criticism["overall_performance"]:
                print(f"   {critic}")
        
        if criticism["league_disasters"]:
            print("\n🚨 LEAGUE DISASTERS:")
            for disaster in criticism["league_disasters"]:
                print(f"   {disaster}")
        
        if criticism["confidence_delusions"]:
            print("\n🤡 CONFIDENCE DELUSIONS:")
            for delusion in criticism["confidence_delusions"]:
                print(f"   {delusion}")
        
        # Improvement demands
        demands = report["improvement_demands"]
        if demands["immediate_actions"]:
            print("\n⚡ IMMEDIATE ACTIONS REQUIRED:")
            for action in demands["immediate_actions"]:
                print(f"   {action}")
        
        print(f"\n⏰ DEADLINE FOR IMPROVEMENT: {demands['deadline']}")
        print("\n" + "="*80)
        print("💀 END OF BRUTAL CRITICISM - NOW GET TO WORK! 💀")
        print("="*80 + "\n")
    
    def _get_performance_grade(self, accuracy: float):
        """Get performance grade based on accuracy"""
        if accuracy >= self.standards["ELITE"]:
            return "A+ (ELITE)"
        elif accuracy >= self.standards["GOOD"]:
            return "B+ (GOOD)"
        elif accuracy >= self.standards["MEDIOCRE"]:
            return "C (MEDIOCRE)"
        elif accuracy >= self.standards["TERRIBLE"]:
            return "D (TERRIBLE)"
        else:
            return "F (DISASTER)"
    
    def _identify_failure_patterns(self, predictions: List[dict]):
        """Identify systematic failure patterns"""
        patterns = {
            "overconfidence_failures": 0,
            "league_specific_failures": {},
            "temporal_patterns": {},
            "pick_type_biases": {}
        }
        
        for prediction in predictions:
            if prediction['status'] == 'incorrect':
                confidence = prediction['prediction']['confidence']
                league = prediction.get('league', 'Unknown')
                pick = prediction['prediction']['pick']
                
                # Overconfidence failures (high confidence but wrong)
                if confidence >= 80:
                    patterns["overconfidence_failures"] += 1
                
                # League-specific failures
                patterns["league_specific_failures"][league] = patterns["league_specific_failures"].get(league, 0) + 1
                
                # Pick type failures
                if pick in ['🏠', 'HOME']:
                    pick_type = 'home'
                elif pick in ['✈️', 'AWAY']:
                    pick_type = 'away'
                elif pick in ['🤝', 'DRAW']:
                    pick_type = 'draw'
                else:
                    pick_type = 'unknown'
                
                patterns["pick_type_biases"][pick_type] = patterns["pick_type_biases"].get(pick_type, 0) + 1
        
        return patterns
    
    def _identify_red_flags(self, analysis: dict):
        """Identify critical red flags in performance"""
        red_flags = []
        
        overall_accuracy = analysis["overall_stats"]["accuracy_percentage"]
        
        # Critical accuracy red flags
        if overall_accuracy < 45:
            red_flags.append("🚨 CRITICAL: Below random chance performance!")
        
        if overall_accuracy < 55:
            red_flags.append("⚠️ WARNING: Consistently poor performance!")
        
        # League-specific red flags
        terrible_leagues = [
            league for league, stats in analysis["league_performance"].items() 
            if stats["accuracy"] < 40
        ]
        if terrible_leagues:
            red_flags.append(f"💀 DISASTER LEAGUES: {', '.join(terrible_leagues)}")
        
        # Confidence calibration red flags
        for bucket, data in analysis["confidence_calibration"].items():
            if bucket.startswith("90-") and data["actual_accuracy"] < 70:
                red_flags.append("🤡 SEVERE overconfidence in 90%+ predictions!")
        
        return red_flags
    
    def _load_json(self, file_path: Path):
        """Load JSON file safely"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def _save_json(self, file_path: Path, data: dict):
        """Save JSON file safely"""
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            self.logger.error(f"💀 ERROR SAVING JSON: {e}")

async def main():
    """Test the hardcore accuracy critic"""
    print("💀🔥💀 TESTING HARDCORE ACCURACY CRITIC 💀🔥💀")
    
    critic = HardcoreAccuracyCritic()
    
    # Perform brutal analysis
    report = await critic.brutal_accuracy_analysis(days_back=7)
    
    if report:
        print("🚀 HARDCORE CRITICISM COMPLETE!")
        print(f"📁 Report saved to: {critic.critic_reports}")
    else:
        print("💀 CRITIC SYSTEM FAILED!")

if __name__ == "__main__":
    asyncio.run(main())