#!/usr/bin/env python3
"""
🔥💀 ANALYZER AGENT - AUTONOMOUS PATTERN RECOGNITION 💀🔥
Agent Poly Loly Double Zero: Specialized Analysis Intelligence

AUTONOMOUS BEHAVIORS:
- Independent pattern discovery in sports data
- Adaptive algorithm selection and tuning
- Real-time performance monitoring
- Proactive insight generation
- Self-improving analysis models
"""

import asyncio
import json
import numpy as np
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import logging
from collections import defaultdict, deque
import hashlib

from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY

logger = logging.getLogger(__name__)

class AnalysisPattern:
    """📊 Represents a discovered analysis pattern"""
    def __init__(self, pattern_id: str, pattern_type: str, sport: str, 
                 confidence: float, metadata: Dict[str, Any]):
        self.pattern_id = pattern_id
        self.pattern_type = pattern_type  # 'trend', 'correlation', 'anomaly', 'prediction'
        self.sport = sport
        self.confidence = confidence
        self.metadata = metadata
        self.discovery_time = datetime.now()
        self.usage_count = 0
        self.success_rate = 0.0
        self.last_validated = None

class AnalyzerAgent(AutonomousAgent):
    """
    🧠 AUTONOMOUS ANALYSIS AGENT
    
    Specializes in:
    - Pattern recognition in sports data
    - Performance trend analysis
    - Anomaly detection
    - Predictive modeling
    - Real-time insights generation
    """
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        super().__init__(agent_id, config)
        
        # Analysis configuration
        self.analysis_algorithms = {
            'trend_analysis': {
                'enabled': True,
                'confidence_threshold': 0.7,
                'min_data_points': 5,
                'window_size': 10
            },
            'correlation_analysis': {
                'enabled': True,
                'correlation_threshold': 0.6,
                'min_correlation_strength': 0.5
            },
            'anomaly_detection': {
                'enabled': True,
                'z_score_threshold': 2.5,
                'detection_window': 20
            },
            'pattern_matching': {
                'enabled': True,
                'similarity_threshold': 0.8,
                'pattern_library_size': 1000
            }
        }
        
        # Analysis state
        self.discovered_patterns = {}  # pattern_id -> AnalysisPattern
        self.successful_patterns = []  # Historical successful patterns
        self.analysis_queue = deque()
        self.processing_data = {}  # sport -> data_buffer
        self.analysis_results = {}  # sport -> latest_results
        
        # Performance tracking
        self.analysis_metrics = {
            'patterns_discovered': 0,
            'patterns_validated': 0,
            'analysis_accuracy': 0.0,
            'processing_time_avg': 0.0,
            'insights_generated': 0
        }
        
        # Real-time buffers
        self.data_buffers = defaultdict(lambda: deque(maxlen=100))  # sport -> data_buffer
        self.result_cache = {}  # analysis_key -> cached_result
        self.cache_timestamps = {}
        
        # Adaptive parameters
        self.confidence_thresholds = defaultdict(lambda: 0.7)  # sport -> threshold
        self.adaptation_learning_rate = 0.1
        
        logger.info(f"🧠 AnalyzerAgent {self.agent_id} initialized with {len(self.analysis_algorithms)} algorithms")
    
    async def _initialize_systems(self):
        """⚙️ Initialize analysis systems"""
        # Load historical patterns if available
        await self._load_historical_patterns()
        
        # Initialize algorithm parameters
        await self._calibrate_algorithms()
        
        # Subscribe to data collector messages
        await self.send_message('*', 'subscribe', {
            'agent_id': self.agent_id,
            'message_types': ['data_available', 'data_updated']
        })
        
        logger.info("⚙️ Analysis systems initialized")
    
    async def _agent_behavior(self):
        """🎯 Core analysis autonomous behavior"""
        # Process pending analysis requests
        await self._process_analysis_queue()
        
        # Perform continuous pattern discovery
        await self._continuous_pattern_discovery()
        
        # Validate existing patterns
        await self._validate_patterns()
        
        # Generate proactive insights
        await self._generate_proactive_insights()
        
        # Update analysis metrics
        await self._update_analysis_metrics()
        
        await asyncio.sleep(0.5)
    
    async def _agent_specific_adaptation(self):
        """🧠 Adapt analysis strategies based on performance"""
        # Analyze pattern performance
        successful_patterns = [p for p in self.discovered_patterns.values() 
                             if p.success_rate > 0.8]
        
        if len(successful_patterns) > 10:
            # Learn from successful patterns
            avg_confidence = np.mean([p.confidence for p in successful_patterns])
            
            # Adapt confidence thresholds
            for sport in self.confidence_thresholds:
                current_threshold = self.confidence_thresholds[sport]
                target_threshold = avg_confidence * 0.9  # Slightly below avg
                
                # Gradual adaptation
                new_threshold = (current_threshold * (1 - self.adaptation_learning_rate) + 
                               target_threshold * self.adaptation_learning_rate)
                self.confidence_thresholds[sport] = new_threshold
                
                logger.info(f"🧠 Adapted {sport} confidence threshold: {current_threshold:.3f} → {new_threshold:.3f}")
        
        # Adapt algorithm parameters
        await self._adapt_algorithm_parameters()
    
    async def _load_historical_patterns(self):
        """📚 Load historical patterns from storage"""
        try:
            patterns_file = f"patterns/{self.agent_id}_patterns.json"
            
            if os.path.exists(patterns_file):
                with open(patterns_file, 'r') as f:
                    data = json.load(f)
                    
                # Load successful patterns
                for pattern_data in data.get('successful_patterns', []):
                    pattern = AnalysisPattern(
                        sport=pattern_data['sport'],
                        pattern_type=pattern_data['pattern_type'],
                        conditions=pattern_data['conditions'],
                        outcome=pattern_data['outcome'],
                        confidence=pattern_data['confidence'],
                        timestamp=datetime.fromisoformat(pattern_data['timestamp'])
                    )
                    self.successful_patterns.append(pattern)
                
                # Load confidence thresholds
                stored_thresholds = data.get('confidence_thresholds', {})
                self.confidence_thresholds.update(stored_thresholds)
                
                logger.info(f"📚 Loaded {len(self.successful_patterns)} historical patterns")
            else:
                logger.info("📚 No historical patterns found (fresh start)")
                
        except Exception as e:
            logger.error(f"❌ Error loading historical patterns: {e}")
    
    async def _calibrate_algorithms(self):
        """🔧 Calibrate analysis algorithms based on historical performance"""
        try:
            # Initialize algorithm performance tracking
            self.algorithm_performance = {
                'trend_analysis': {'accuracy': 0.75, 'speed': 0.85, 'confidence': 0.70},
                'pattern_matching': {'accuracy': 0.80, 'speed': 0.90, 'confidence': 0.75},
                'anomaly_detection': {'accuracy': 0.70, 'speed': 0.95, 'confidence': 0.65},
                'correlation_analysis': {'accuracy': 0.85, 'speed': 0.75, 'confidence': 0.80}
            }
            
            # Calibrate thresholds based on successful patterns
            if self.successful_patterns:
                avg_confidence = np.mean([p.confidence for p in self.successful_patterns])
                
                # Adjust algorithm sensitivity
                for algorithm in self.algorithm_performance:
                    current_acc = self.algorithm_performance[algorithm]['accuracy']
                    # Slightly increase accuracy target based on historical success
                    self.algorithm_performance[algorithm]['accuracy'] = min(0.95, current_acc + 0.05)
                    
                logger.info(f"🔧 Calibrated {len(self.algorithm_performance)} algorithms")
            else:
                logger.info("🔧 Using default algorithm calibration (no history)")
                
        except Exception as e:
            logger.error(f"❌ Error calibrating algorithms: {e}")
            # Use safe defaults
            self.algorithm_performance = {
                'trend_analysis': {'accuracy': 0.75, 'speed': 0.85, 'confidence': 0.70},
                'pattern_matching': {'accuracy': 0.80, 'speed': 0.90, 'confidence': 0.75},
                'anomaly_detection': {'accuracy': 0.70, 'speed': 0.95, 'confidence': 0.65},
                'correlation_analysis': {'accuracy': 0.85, 'speed': 0.75, 'confidence': 0.80}
            }
    
    async def _handle_message(self, message):
        """📨 Handle messages from other agents"""
        await super()._handle_message(message)
        
        if message.message_type == "data_available":
            await self._handle_data_available(message)
        elif message.message_type == "analysis_request":
            await self._handle_analysis_request(message)
        elif message.message_type == "pattern_validation":
            await self._handle_pattern_validation(message)
    
    async def _handle_data_available(self, message):
        """📊 Handle new data availability"""
        payload = message.payload
        sport = payload.get('sport')
        collection_id = payload.get('collection_id')
        
        if sport:
            # Request data from collector
            await self.send_message(message.sender_id, 'data_request', {
                'sport': sport,
                'collection_id': collection_id,
                'requester': self.agent_id
            })
            
            logger.info(f"📊 Requested {sport} data for analysis (Collection: {collection_id})")
    
    async def _handle_analysis_request(self, message):
        """📋 Handle external analysis requests"""
        payload = message.payload
        analysis_type = payload.get('analysis_type', 'full_analysis')
        sport = payload.get('sport')
        data = payload.get('data')
        
        if sport and data:
            analysis_task = {
                'id': f"req_{int(time.time())}",
                'type': analysis_type,
                'sport': sport,
                'data': data,
                'requester': message.sender_id,
                'priority': payload.get('priority', 1)
            }
            
            self.analysis_queue.append(analysis_task)
            logger.info(f"📋 Queued {analysis_type} analysis for {sport}")
    
    async def _process_analysis_queue(self):
        """📋 Process queued analysis tasks"""
        while self.analysis_queue and len(self.running_tasks) < self.max_concurrent_tasks:
            task = self.analysis_queue.popleft()
            analysis_coroutine = asyncio.create_task(self._execute_analysis(task))
            self.running_tasks.add(analysis_coroutine)
    
    async def _execute_analysis(self, task: Dict[str, Any]):
        """⚡ Execute specific analysis task"""
        task_id = task['id']
        analysis_type = task['type']
        sport = task['sport']
        data = task['data']
        start_time = time.time()
        
        try:
            logger.info(f"⚡ Executing {analysis_type} for {sport} (Task: {task_id})")
            
            # Route to specific analysis method
            if analysis_type == 'trend_analysis':
                result = await self._perform_trend_analysis(sport, data)
            elif analysis_type == 'correlation_analysis':
                result = await self._perform_correlation_analysis(sport, data)
            elif analysis_type == 'anomaly_detection':
                result = await self._perform_anomaly_detection(sport, data)
            elif analysis_type == 'pattern_matching':
                result = await self._perform_pattern_matching(sport, data)
            else:
                result = await self._perform_full_analysis(sport, data)
            
            # Store results
            self.analysis_results[sport] = result
            
            # Send results to requester
            if 'requester' in task:
                await self.send_message(task['requester'], 'analysis_complete', {
                    'task_id': task_id,
                    'sport': sport,
                    'analysis_type': analysis_type,
                    'result': result,
                    'confidence': result.get('overall_confidence', 0.0)
                })
            
            # Record success
            duration = time.time() - start_time
            self.memory.record_experience(
                f"analysis_{analysis_type}", 'success', duration,
                {'sport': sport, 'confidence': result.get('overall_confidence', 0.0)}
            )
            
            # Update metrics
            self.analysis_metrics['insights_generated'] += 1
            
            logger.info(f"✅ {analysis_type} completed for {sport}: confidence {result.get('overall_confidence', 0.0):.2f}")
            
        except Exception as e:
            # Record failure
            duration = time.time() - start_time
            self.memory.record_experience(
                f"analysis_{analysis_type}", 'failure', duration,
                {'sport': sport, 'error': str(e)}
            )
            
            logger.error(f"❌ Analysis failed for {sport}: {e}")
    
    async def _perform_full_analysis(self, sport: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """🔍 Perform comprehensive analysis"""
        games = data.get('games', [])
        if not games:
            return {'error': 'No games data available'}
        
        # Buffer the data
        self.data_buffers[sport].extend(games)
        
        # Perform multiple analysis types
        trend_result = await self._perform_trend_analysis(sport, data)
        correlation_result = await self._perform_correlation_analysis(sport, data)
        anomaly_result = await self._perform_anomaly_detection(sport, data)
        patterns_result = await self._perform_pattern_matching(sport, data)
        
        # Combine results
        full_result = {
            'sport': sport,
            'analysis_timestamp': time.time(),
            'data_points': len(games),
            'trend_analysis': trend_result,
            'correlation_analysis': correlation_result,
            'anomaly_detection': anomaly_result,
            'pattern_matching': patterns_result,
            'overall_confidence': 0.0,
            'key_insights': [],
            'recommendations': []
        }
        
        # Calculate overall confidence
        confidences = [
            trend_result.get('confidence', 0.0),
            correlation_result.get('confidence', 0.0),
            anomaly_result.get('confidence', 0.0),
            patterns_result.get('confidence', 0.0)
        ]
        full_result['overall_confidence'] = np.mean([c for c in confidences if c > 0])
        
        # Generate key insights
        full_result['key_insights'] = await self._generate_insights(full_result)
        full_result['recommendations'] = await self._generate_recommendations(full_result)
        
        return full_result
    
    async def _perform_trend_analysis(self, sport: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """📈 Analyze trends in team performance"""
        games = data.get('games', [])
        if len(games) < self.analysis_algorithms['trend_analysis']['min_data_points']:
            return {'error': 'Insufficient data for trend analysis', 'confidence': 0.0}
        
        trends = {}
        team_scores = defaultdict(list)
        
        # Collect team scores over time
        for game in games:
            for team in game.get('teams', []):
                team_name = team.get('name')
                score = team.get('score')
                if team_name and score is not None:
                    try:
                        team_scores[team_name].append(float(score))
                    except (ValueError, TypeError):
                        continue
        
        # Analyze trends for each team
        for team_name, scores in team_scores.items():
            if len(scores) >= 3:
                # Calculate trend metrics
                x = np.arange(len(scores))
                trend_slope = np.polyfit(x, scores, 1)[0]
                trend_direction = 'improving' if trend_slope > 0.5 else 'declining' if trend_slope < -0.5 else 'stable'
                
                # Calculate confidence based on R-squared
                correlation = np.corrcoef(x, scores)[0, 1] if len(scores) > 1 else 0
                confidence = abs(correlation) if not np.isnan(correlation) else 0
                
                trends[team_name] = {
                    'slope': float(trend_slope),
                    'direction': trend_direction,
                    'confidence': float(confidence),
                    'avg_score': float(np.mean(scores)),
                    'score_variance': float(np.var(scores)),
                    'games_analyzed': len(scores)
                }
        
        # Overall trend analysis confidence
        overall_confidence = np.mean([t['confidence'] for t in trends.values()]) if trends else 0.0
        
        result = {
            'trends': trends,
            'confidence': float(overall_confidence),
            'teams_analyzed': len(trends),
            'algorithm': 'linear_regression'
        }
        
        # Discover new patterns
        await self._discover_trend_patterns(sport, result)
        
        return result
    
    async def _perform_correlation_analysis(self, sport: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """🔗 Analyze correlations between different metrics"""
        games = data.get('games', [])
        if len(games) < 5:
            return {'error': 'Insufficient data for correlation analysis', 'confidence': 0.0}
        
        correlations = {}
        
        # Extract various metrics for correlation
        team_metrics = defaultdict(lambda: {'scores': [], 'home_scores': [], 'away_scores': []})
        
        for game in games:
            teams = game.get('teams', [])
            if len(teams) == 2:
                home_team = next((t for t in teams if t.get('home_away') == 'home'), None)
                away_team = next((t for t in teams if t.get('home_away') == 'away'), None)
                
                if home_team and away_team:
                    home_score = self._safe_float(home_team.get('score'))
                    away_score = self._safe_float(away_team.get('score'))
                    
                    if home_score is not None and away_score is not None:
                        home_name = home_team.get('name')
                        away_name = away_team.get('name')
                        
                        team_metrics[home_name]['scores'].append(home_score)
                        team_metrics[home_name]['home_scores'].append(home_score)
                        team_metrics[away_name]['scores'].append(away_score)
                        team_metrics[away_name]['away_scores'].append(away_score)
        
        # Calculate correlations
        home_away_correlation = await self._calculate_home_away_correlation(team_metrics)
        score_consistency_correlation = await self._calculate_score_consistency_correlation(team_metrics)
        
        correlations = {
            'home_away_advantage': home_away_correlation,
            'score_consistency': score_consistency_correlation
        }
        
        # Calculate overall confidence
        valid_correlations = [c['correlation'] for c in correlations.values() 
                            if isinstance(c, dict) and 'correlation' in c]
        overall_confidence = np.mean([abs(c) for c in valid_correlations]) if valid_correlations else 0.0
        
        result = {
            'correlations': correlations,
            'confidence': float(overall_confidence),
            'significant_correlations': len([c for c in valid_correlations if abs(c) > 0.5])
        }
        
        return result
    
    async def _perform_anomaly_detection(self, sport: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """🚨 Detect anomalies in sports data"""
        games = data.get('games', [])
        if len(games) < 10:
            return {'error': 'Insufficient data for anomaly detection', 'confidence': 0.0}
        
        anomalies = []
        
        # Collect all scores
        all_scores = []
        game_scores = []
        
        for game in games:
            teams = game.get('teams', [])
            game_total = 0
            valid_scores = 0
            
            for team in teams:
                score = self._safe_float(team.get('score'))
                if score is not None:
                    all_scores.append(score)
                    game_total += score
                    valid_scores += 1
            
            if valid_scores == 2:  # Only games with both team scores
                game_scores.append(game_total)
        
        if len(all_scores) < 5:
            return {'error': 'Insufficient valid scores', 'confidence': 0.0}
        
        # Calculate z-scores for anomaly detection
        mean_score = np.mean(all_scores)
        std_score = np.std(all_scores)
        threshold = self.analysis_algorithms['anomaly_detection']['z_score_threshold']
        
        # Detect score anomalies
        for i, score in enumerate(all_scores):
            if std_score > 0:
                z_score = abs(score - mean_score) / std_score
                if z_score > threshold:
                    anomalies.append({
                        'type': 'score_anomaly',
                        'value': float(score),
                        'z_score': float(z_score),
                        'severity': 'high' if z_score > 3 else 'medium',
                        'description': f"Unusually {'high' if score > mean_score else 'low'} score"
                    })
        
        # Detect game total anomalies
        if len(game_scores) > 5:
            mean_total = np.mean(game_scores)
            std_total = np.std(game_scores)
            
            for total in game_scores:
                if std_total > 0:
                    z_score = abs(total - mean_total) / std_total
                    if z_score > threshold:
                        anomalies.append({
                            'type': 'game_total_anomaly',
                            'value': float(total),
                            'z_score': float(z_score),
                            'severity': 'high' if z_score > 3 else 'medium',
                            'description': f"Unusually {'high' if total > mean_total else 'low'} scoring game"
                        })
        
        # Calculate confidence based on data quality
        confidence = min(len(all_scores) / 20.0, 1.0) * (1.0 if std_score > 0 else 0.0)
        
        result = {
            'anomalies': anomalies,
            'confidence': float(confidence),
            'total_data_points': len(all_scores),
            'anomaly_count': len(anomalies),
            'statistics': {
                'mean_score': float(mean_score),
                'std_score': float(std_score),
                'mean_game_total': float(np.mean(game_scores)) if game_scores else 0.0
            }
        }
        
        return result
    
    async def _perform_pattern_matching(self, sport: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """🔍 Match current data against known patterns"""
        games = data.get('games', [])
        if not games:
            return {'error': 'No games data for pattern matching', 'confidence': 0.0}
        
        matches = []
        
        # Create signature for current data
        current_signature = await self._create_data_signature(sport, data)
        
        # Compare against known patterns
        for pattern_id, pattern in self.discovered_patterns.items():
            if pattern.sport == sport:
                similarity = await self._calculate_pattern_similarity(
                    current_signature, pattern.metadata.get('signature', {})
                )
                
                threshold = self.analysis_algorithms['pattern_matching']['similarity_threshold']
                if similarity > threshold:
                    matches.append({
                        'pattern_id': pattern_id,
                        'pattern_type': pattern.pattern_type,
                        'similarity': float(similarity),
                        'confidence': float(pattern.confidence),
                        'discovery_date': pattern.discovery_time.isoformat(),
                        'usage_count': pattern.usage_count,
                        'success_rate': pattern.success_rate
                    })
                    
                    # Update pattern usage
                    pattern.usage_count += 1
        
        # Sort matches by similarity
        matches.sort(key=lambda x: x['similarity'], reverse=True)
        
        # Calculate overall confidence
        overall_confidence = np.mean([m['similarity'] * m['confidence'] for m in matches]) if matches else 0.0
        
        result = {
            'matches': matches[:10],  # Top 10 matches
            'confidence': float(overall_confidence),
            'patterns_checked': len([p for p in self.discovered_patterns.values() if p.sport == sport]),
            'total_matches': len(matches)
        }
        
        return result
    
    async def _continuous_pattern_discovery(self):
        """🔍 Continuously discover new patterns in buffered data"""
        for sport, data_buffer in self.data_buffers.items():
            if len(data_buffer) >= 20:  # Minimum data for pattern discovery
                # Try to discover new patterns
                await self._discover_patterns_in_buffer(sport, list(data_buffer))
    
    async def _discover_patterns_in_buffer(self, sport: str, games: List[Dict[str, Any]]):
        """🔍 Discover patterns in game data buffer"""
        try:
            # Team performance patterns
            await self._discover_team_performance_patterns(sport, games)
            
            # Scoring patterns
            await self._discover_scoring_patterns(sport, games)
            
            # Temporal patterns
            await self._discover_temporal_patterns(sport, games)
            
        except Exception as e:
            logger.error(f"❌ Pattern discovery error for {sport}: {e}")
    
    async def _discover_team_performance_patterns(self, sport: str, games: List[Dict[str, Any]]):
        """🏆 Discover team performance patterns"""
        team_win_streaks = defaultdict(list)
        team_scores = defaultdict(list)
        
        # Analyze team performance sequences
        for game in games:
            teams = game.get('teams', [])
            if len(teams) == 2:
                team1, team2 = teams
                score1 = self._safe_float(team1.get('score'))
                score2 = self._safe_float(team2.get('score'))
                
                if score1 is not None and score2 is not None:
                    # Determine winner
                    winner = team1['name'] if score1 > score2 else team2['name'] if score2 > score1 else None
                    
                    if winner:
                        team_win_streaks[winner].append(1)
                        loser = team2['name'] if winner == team1['name'] else team1['name']
                        team_win_streaks[loser].append(0)
                    
                    team_scores[team1['name']].append(score1)
                    team_scores[team2['name']].append(score2)
        
        # Find streak patterns
        for team, wins in team_win_streaks.items():
            if len(wins) >= 5:
                streak_pattern = await self._analyze_streak_pattern(wins)
                if streak_pattern['significance'] > 0.7:
                    await self._create_pattern(
                        'team_performance_streak',
                        sport,
                        streak_pattern['confidence'],
                        {
                            'team': team,
                            'pattern_data': streak_pattern,
                            'signature': {'streak_length': streak_pattern.get('max_streak', 0)}
                        }
                    )
    
    async def _discover_scoring_patterns(self, sport: str, games: List[Dict[str, Any]]):
        """⚽ Discover scoring patterns"""
        game_totals = []
        score_differences = []
        
        for game in games:
            teams = game.get('teams', [])
            if len(teams) == 2:
                score1 = self._safe_float(teams[0].get('score'))
                score2 = self._safe_float(teams[1].get('score'))
                
                if score1 is not None and score2 is not None:
                    total = score1 + score2
                    diff = abs(score1 - score2)
                    
                    game_totals.append(total)
                    score_differences.append(diff)
        
        if len(game_totals) >= 10:
            # Analyze scoring distribution patterns
            mean_total = np.mean(game_totals)
            std_total = np.std(game_totals)
            
            # Check for unusual scoring distribution
            if std_total > 0:
                cv = std_total / mean_total  # Coefficient of variation
                if cv > 0.3:  # High variability
                    await self._create_pattern(
                        'high_scoring_variance',
                        sport,
                        min(cv, 1.0),
                        {
                            'mean_total': mean_total,
                            'coefficient_variation': cv,
                            'signature': {'scoring_variance': cv}
                        }
                    )
    
    async def _discover_temporal_patterns(self, sport: str, games: List[Dict[str, Any]]):
        """⏰ Discover time-based patterns"""
        # This would analyze patterns related to game timing, seasons, etc.
        # For now, implementing a basic day-of-week pattern
        day_performance = defaultdict(list)
        
        for game in games:
            game_date = game.get('date')
            if game_date:
                try:
                    # Extract day of week (simplified)
                    # In real implementation, would properly parse date
                    day = hash(str(game_date)) % 7  # Simplified day extraction
                    
                    teams = game.get('teams', [])
                    if len(teams) == 2:
                        total_score = sum(self._safe_float(team.get('score', 0)) or 0 for team in teams)
                        day_performance[day].append(total_score)
                        
                except Exception:
                    continue
        
        # Check for day-of-week patterns
        if len(day_performance) >= 3:
            day_averages = {day: np.mean(scores) for day, scores in day_performance.items()}
            if day_averages:
                variance = np.var(list(day_averages.values()))
                if variance > 10:  # Significant day-of-week variation
                    await self._create_pattern(
                        'temporal_scoring_pattern',
                        sport,
                        min(variance / 50.0, 1.0),
                        {
                            'day_averages': day_averages,
                            'variance': variance,
                            'signature': {'temporal_variance': variance}
                        }
                    )
    
    async def _create_pattern(self, pattern_type: str, sport: str, confidence: float, metadata: Dict[str, Any]):
        """🎯 Create new discovered pattern"""
        pattern_id = hashlib.md5(f"{pattern_type}_{sport}_{time.time()}".encode()).hexdigest()[:16]
        
        pattern = AnalysisPattern(
            pattern_id=pattern_id,
            pattern_type=pattern_type,
            sport=sport,
            confidence=confidence,
            metadata=metadata
        )
        
        self.discovered_patterns[pattern_id] = pattern
        self.analysis_metrics['patterns_discovered'] += 1
        
        # Broadcast pattern discovery
        await self.broadcast_message('pattern_discovered', {
            'pattern_id': pattern_id,
            'pattern_type': pattern_type,
            'sport': sport,
            'confidence': confidence,
            'discoverer': self.agent_id
        })
        
        logger.info(f"🎯 Discovered new {pattern_type} pattern for {sport} (confidence: {confidence:.2f})")
    
    async def _validate_patterns(self):
        """✅ Validate existing patterns against new data"""
        current_time = time.time()
        
        for pattern_id, pattern in list(self.discovered_patterns.items()):
            # Validate patterns that haven't been checked recently
            if (pattern.last_validated is None or 
                current_time - pattern.last_validated.timestamp() > 3600):  # 1 hour
                
                validation_result = await self._validate_single_pattern(pattern)
                pattern.last_validated = datetime.now()
                
                if validation_result['valid']:
                    pattern.success_rate = validation_result['success_rate']
                    self.analysis_metrics['patterns_validated'] += 1
                else:
                    # Remove invalid patterns
                    del self.discovered_patterns[pattern_id]
                    logger.info(f"🗑️ Removed invalid pattern {pattern_id}")
    
    async def _validate_single_pattern(self, pattern: AnalysisPattern) -> Dict[str, Any]:
        """✅ Validate a single pattern"""
        sport = pattern.sport
        
        # Get recent data for the sport
        if sport in self.data_buffers:
            recent_games = list(self.data_buffers[sport])[-10:]  # Last 10 games
            
            if len(recent_games) >= 5:
                # Create signature for recent data
                recent_signature = await self._create_data_signature(sport, {'games': recent_games})
                
                # Compare with pattern signature
                similarity = await self._calculate_pattern_similarity(
                    recent_signature, pattern.metadata.get('signature', {})
                )
                
                # Pattern is valid if similarity is above threshold
                valid = similarity > 0.6
                return {
                    'valid': valid,
                    'success_rate': similarity,
                    'similarity': similarity
                }
        
        return {'valid': False, 'success_rate': 0.0, 'similarity': 0.0}
    
    # =================== UTILITY METHODS ===================
    
    def _safe_float(self, value) -> Optional[float]:
        """🔒 Safely convert value to float"""
        try:
            return float(value) if value is not None else None
        except (ValueError, TypeError):
            return None
    
    async def _create_data_signature(self, sport: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """📝 Create signature for data pattern matching"""
        games = data.get('games', [])
        if not games:
            return {}
        
        all_scores = []
        team_count = set()
        
        for game in games:
            for team in game.get('teams', []):
                score = self._safe_float(team.get('score'))
                if score is not None:
                    all_scores.append(score)
                    team_count.add(team.get('name'))
        
        if not all_scores:
            return {}
        
        signature = {
            'mean_score': float(np.mean(all_scores)),
            'std_score': float(np.std(all_scores)),
            'game_count': len(games),
            'team_count': len(team_count),
            'score_range': float(max(all_scores) - min(all_scores)) if all_scores else 0.0
        }
        
        return signature
    
    async def _calculate_pattern_similarity(self, sig1: Dict[str, Any], sig2: Dict[str, Any]) -> float:
        """📊 Calculate similarity between two pattern signatures"""
        if not sig1 or not sig2:
            return 0.0
        
        common_keys = set(sig1.keys()) & set(sig2.keys())
        if not common_keys:
            return 0.0
        
        similarities = []
        for key in common_keys:
            val1, val2 = sig1[key], sig2[key]
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                if val1 == 0 and val2 == 0:
                    similarities.append(1.0)
                elif val1 == 0 or val2 == 0:
                    similarities.append(0.0)
                else:
                    # Calculate relative similarity
                    diff = abs(val1 - val2)
                    avg = (abs(val1) + abs(val2)) / 2
                    similarity = max(0.0, 1.0 - diff / avg) if avg > 0 else 0.0
                    similarities.append(similarity)
        
        return np.mean(similarities) if similarities else 0.0
    
    async def _calculate_home_away_correlation(self, team_metrics: Dict) -> Dict[str, Any]:
        """🏠 Calculate home vs away performance correlation"""
        correlations = []
        
        for team, metrics in team_metrics.items():
            home_scores = metrics['home_scores']
            away_scores = metrics['away_scores']
            
            if len(home_scores) >= 3 and len(away_scores) >= 3:
                home_avg = np.mean(home_scores)
                away_avg = np.mean(away_scores)
                
                # Simple correlation based on averages
                correlation = (home_avg - away_avg) / max(home_avg, away_avg, 1.0)
                correlations.append(correlation)
        
        if correlations:
            avg_correlation = np.mean(correlations)
            return {
                'correlation': float(avg_correlation),
                'teams_analyzed': len(correlations),
                'significance': min(len(correlations) / 10.0, 1.0)
            }
        
        return {'correlation': 0.0, 'teams_analyzed': 0, 'significance': 0.0}
    
    async def _calculate_score_consistency_correlation(self, team_metrics: Dict) -> Dict[str, Any]:
        """📊 Calculate score consistency correlation"""
        consistency_scores = []
        
        for team, metrics in team_metrics.items():
            scores = metrics['scores']
            if len(scores) >= 5:
                variance = np.var(scores)
                mean_score = np.mean(scores)
                cv = variance / mean_score if mean_score > 0 else 0
                consistency = 1.0 / (1.0 + cv)  # Higher consistency = lower coefficient of variation
                consistency_scores.append(consistency)
        
        if consistency_scores:
            avg_consistency = np.mean(consistency_scores)
            return {
                'correlation': float(avg_consistency),
                'teams_analyzed': len(consistency_scores),
                'significance': min(len(consistency_scores) / 10.0, 1.0)
            }
        
        return {'correlation': 0.0, 'teams_analyzed': 0, 'significance': 0.0}
    
    async def _analyze_streak_pattern(self, wins: List[int]) -> Dict[str, Any]:
        """🔥 Analyze win/loss streak patterns"""
        current_streak = 0
        max_streak = 0
        streaks = []
        
        for win in wins:
            if win:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                if current_streak > 0:
                    streaks.append(current_streak)
                current_streak = 0
        
        if current_streak > 0:
            streaks.append(current_streak)
        
        # Calculate pattern significance
        win_rate = sum(wins) / len(wins)
        avg_streak = np.mean(streaks) if streaks else 0
        
        # Higher significance for teams with clear patterns
        significance = min((max_streak * avg_streak * abs(win_rate - 0.5)) / 5.0, 1.0)
        
        return {
            'max_streak': max_streak,
            'avg_streak': float(avg_streak),
            'win_rate': float(win_rate),
            'significance': float(significance),
            'confidence': float(significance * 0.8)  # Slightly lower confidence
        }
    
    async def _generate_insights(self, analysis_result: Dict[str, Any]) -> List[str]:
        """💡 Generate key insights from analysis results"""
        insights = []
        
        # Trend insights
        trend_analysis = analysis_result.get('trend_analysis', {})
        if trend_analysis.get('trends'):
            improving_teams = [team for team, data in trend_analysis['trends'].items() 
                             if data.get('direction') == 'improving' and data.get('confidence', 0) > 0.7]
            if improving_teams:
                insights.append(f"🔥 Strong upward trends detected for: {', '.join(improving_teams[:3])}")
        
        # Anomaly insights
        anomaly_analysis = analysis_result.get('anomaly_detection', {})
        anomalies = anomaly_analysis.get('anomalies', [])
        high_severity = [a for a in anomalies if a.get('severity') == 'high']
        if high_severity:
            insights.append(f"🚨 {len(high_severity)} high-severity anomalies detected")
        
        # Pattern insights
        pattern_analysis = analysis_result.get('pattern_matching', {})
        matches = pattern_analysis.get('matches', [])
        high_confidence_matches = [m for m in matches if m.get('similarity', 0) > 0.8]
        if high_confidence_matches:
            insights.append(f"🎯 {len(high_confidence_matches)} strong pattern matches found")
        
        return insights
    
    async def _generate_recommendations(self, analysis_result: Dict[str, Any]) -> List[str]:
        """📋 Generate actionable recommendations"""
        recommendations = []
        
        overall_confidence = analysis_result.get('overall_confidence', 0.0)
        
        if overall_confidence > 0.8:
            recommendations.append("✅ High confidence analysis - suitable for key decisions")
        elif overall_confidence > 0.6:
            recommendations.append("⚠️ Moderate confidence - consider additional data")
        else:
            recommendations.append("🔍 Low confidence - require more data or analysis")
        
        # Data-specific recommendations
        data_points = analysis_result.get('data_points', 0)
        if data_points < 10:
            recommendations.append("📊 Increase data collection frequency for better analysis")
        
        return recommendations
    
    async def _update_analysis_metrics(self):
        """📊 Update analysis performance metrics"""
        # Calculate average processing time
        recent_experiences = self.memory.experiences[-20:]  # Last 20
        if recent_experiences:
            avg_duration = np.mean([exp['duration'] for exp in recent_experiences])
            self.analysis_metrics['processing_time_avg'] = avg_duration
            
            # Calculate accuracy based on success rate
            successes = sum(1 for exp in recent_experiences if exp['outcome'] == 'success')
            self.analysis_metrics['analysis_accuracy'] = successes / len(recent_experiences)
    
    async def _generate_proactive_insights(self):
        """🎯 Generate proactive insights without explicit requests"""
        current_time = time.time()
        
        # Check if we should generate proactive insights (every 10 minutes)
        last_proactive = getattr(self, '_last_proactive_insights', 0)
        if current_time - last_proactive > 600:
            
            for sport in self.data_buffers:
                if len(self.data_buffers[sport]) >= 10:
                    # Generate insight for sport with enough data
                    insight_data = {
                        'games': list(self.data_buffers[sport])[-10:]
                    }
                    
                    quick_analysis = await self._perform_trend_analysis(sport, insight_data)
                    
                    if quick_analysis.get('confidence', 0) > 0.7:
                        await self.broadcast_message('proactive_insight', {
                            'sport': sport,
                            'insight_type': 'trend_analysis',
                            'confidence': quick_analysis['confidence'],
                            'summary': f"Analyzed {len(insight_data['games'])} recent games",
                            'generator': self.agent_id
                        })
            
            self._last_proactive_insights = current_time
    
    async def _adapt_algorithm_parameters(self):
        """🧠 Adapt algorithm parameters based on performance"""
        for algorithm_name, config in self.analysis_algorithms.items():
            algorithm_experiences = [
                exp for exp in self.memory.experiences 
                if exp['task_type'] == f"analysis_{algorithm_name}"
            ]
            
            if len(algorithm_experiences) >= 10:
                recent_success_rate = sum(
                    1 for exp in algorithm_experiences[-10:] 
                    if exp['outcome'] == 'success'
                ) / 10
                
                # Adapt thresholds based on success rate
                if recent_success_rate < 0.7 and algorithm_name == 'trend_analysis':
                    # Lower confidence threshold to be more inclusive
                    current_threshold = config['confidence_threshold']
                    new_threshold = max(current_threshold * 0.9, 0.5)
                    config['confidence_threshold'] = new_threshold
                    
                    logger.info(f"🧠 Adapted {algorithm_name} confidence threshold: {current_threshold:.2f} → {new_threshold:.2f}")
    
    # =================== PUBLIC API ===================
    
    async def get_analysis_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive analysis status"""
        return {
            'agent_id': self.agent_id,
            'timestamp': time.time(),
            'metrics': self.analysis_metrics,
            'discovered_patterns': len(self.discovered_patterns),
            'active_analyses': len(self.running_tasks),
            'queue_length': len(self.analysis_queue),
            'sports_monitored': list(self.data_buffers.keys()),
            'algorithm_status': {
                name: {'enabled': config['enabled'], 'confidence_threshold': config.get('confidence_threshold', 'N/A')}
                for name, config in self.analysis_algorithms.items()
            }
        }
    
    async def get_sport_analysis(self, sport: str) -> Optional[Dict[str, Any]]:
        """🎯 Get latest analysis for specific sport"""
        return self.analysis_results.get(sport)
    
    async def get_discovered_patterns(self, sport: str = None) -> List[Dict[str, Any]]:
        """🔍 Get discovered patterns (optionally filtered by sport)"""
        patterns = self.discovered_patterns.values()
        if sport:
            patterns = [p for p in patterns if p.sport == sport]
        
        return [
            {
                'pattern_id': p.pattern_id,
                'pattern_type': p.pattern_type,
                'sport': p.sport,
                'confidence': p.confidence,
                'discovery_time': p.discovery_time.isoformat(),
                'usage_count': p.usage_count,
                'success_rate': p.success_rate
            }
            for p in patterns
        ]

if __name__ == "__main__":
    async def test_analyzer():
        agent = AnalyzerAgent("analyzer_001")
        AGENT_REGISTRY.register_agent(agent)
        
        await agent.spawn()
        await asyncio.sleep(5)
        
        # Test analysis
        test_data = {
            'games': [
                {
                    'id': '1',
                    'date': '2024-01-01',
                    'teams': [
                        {'name': 'Team A', 'score': 21, 'home_away': 'home'},
                        {'name': 'Team B', 'score': 14, 'home_away': 'away'}
                    ]
                },
                {
                    'id': '2', 
                    'date': '2024-01-02',
                    'teams': [
                        {'name': 'Team A', 'score': 28, 'home_away': 'away'},
                        {'name': 'Team C', 'score': 10, 'home_away': 'home'}
                    ]
                }
            ]
        }
        
        result = await agent._perform_full_analysis('NFL', test_data)
        print(f"🧠 Analysis Result: {json.dumps(result, indent=2, default=str)}")
        
        status = await agent.get_analysis_status()
        print(f"📊 Agent Status: {json.dumps(status, indent=2, default=str)}")
        
        await agent.terminate()
    
    asyncio.run(test_analyzer())