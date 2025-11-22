#!/usr/bin/env python3
"""
🔥💀 PREDICTOR AGENT - AUTONOMOUS ML PREDICTION ENGINE 💀🔥
Agent Poly Loly Double Zero: Specialized Prediction Intelligence

AUTONOMOUS BEHAVIORS:
- Independent model training and optimization
- Adaptive feature selection and engineering
- Real-time prediction accuracy monitoring
- Self-improving ML algorithms
- Proactive model retraining
- 🔥💀 8D DIMENSIONAL ANALYSIS INTEGRATION 💀🔥
"""

import asyncio
import json
import numpy as np
import time
import sys
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import logging
from collections import defaultdict, deque
import pickle
import hashlib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
import warnings
warnings.filterwarnings('ignore')

from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY

# 🔥💀🔥 IMPORT THE REAL 8D PREDICTION ENGINE! 💀🔥💀
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
try:
    from real_agents.universal_prediction_engine import UniversalPredictionEngine
    UNIVERSAL_ENGINE_AVAILABLE = True
    logger = logging.getLogger(__name__)
    logger.info("🔥💀🔥 UNIVERSAL 8D PREDICTION ENGINE LOADED! 💀🔥💀")
except Exception as e:
    UNIVERSAL_ENGINE_AVAILABLE = False
    logger = logging.getLogger(__name__)
    logger.warning(f"⚠️ Universal 8D engine not available: {e}")

logger = logging.getLogger(__name__)

class PredictionModel:
    """🤖 Individual ML prediction model"""
    def __init__(self, model_id: str, model_type: str, sport: str, target: str):
        self.model_id = model_id
        self.model_type = model_type  # 'winner', 'score', 'total', 'spread'
        self.sport = sport
        self.target = target
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
        # Performance tracking
        self.accuracy = 0.0
        self.training_samples = 0
        self.predictions_made = 0
        self.correct_predictions = 0
        self.last_trained = None
        self.last_accuracy_check = None
        
        # Feature importance
        self.feature_names = []
        self.feature_importance = {}
        
        # Model metadata
        self.creation_time = datetime.now()
        self.version = 1
        self.hyperparameters = {}
    
    def update_accuracy(self, predicted: Any, actual: Any) -> bool:
        """📊 Update model accuracy with new prediction result"""
        self.predictions_made += 1
        
        if self.model_type in ['winner', 'classification']:
            correct = (predicted == actual)
        else:  # Regression models
            # Consider within 10% as correct for regression
            if actual != 0:
                error_pct = abs(predicted - actual) / abs(actual)
                correct = error_pct <= 0.1
            else:
                correct = abs(predicted) <= 1.0
        
        if correct:
            self.correct_predictions += 1
        
        self.accuracy = self.correct_predictions / self.predictions_made
        self.last_accuracy_check = datetime.now()
        
        return correct

class PredictorAgent(AutonomousAgent):
    """
    🎯 AUTONOMOUS PREDICTION AGENT
    
    Specializes in:
    - Sports outcome prediction
    - Score prediction
    - Spread/total prediction
    - Model performance optimization
    - Adaptive algorithm selection
    """
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        super().__init__(agent_id, config)
        
        # Prediction configuration
        self.prediction_targets = {
            'winner': {'type': 'classification', 'priority': 1},
            'total_score': {'type': 'regression', 'priority': 2},
            'score_difference': {'type': 'regression', 'priority': 2},
            'home_advantage': {'type': 'classification', 'priority': 3}
        }
        
        # Model portfolio
        self.models = {}  # model_id -> PredictionModel
        self.active_models = defaultdict(list)  # sport -> list of model_ids
        self.model_performance = defaultdict(dict)  # sport -> target -> performance_metrics
        
        # Training data
        self.training_data = defaultdict(list)  # sport -> training_samples
        self.training_queue = deque()
        self.max_training_samples = 1000  # Per sport
        
        # Prediction cache
        self.prediction_cache = {}  # cache_key -> prediction_result
        self.cache_timestamps = {}
        self.cache_ttl = 3600  # 1 hour
        
        # Performance thresholds
        self.min_accuracy_threshold = 0.6
        self.retrain_threshold = 0.05  # Retrain if accuracy drops by 5%
        self.min_training_samples = 20
        
        # Algorithm selection
        self.available_algorithms = {
            'classification': {
                'random_forest': RandomForestClassifier,
                'logistic_regression': LogisticRegression
            },
            'regression': {
                'gradient_boosting': GradientBoostingRegressor,
                'linear_regression': LinearRegression
            }
        }
        
        # 🔥💀🔥 INITIALIZE UNIVERSAL 8D PREDICTION ENGINE! 💀🔥💀
        self.universal_engine = None
        if UNIVERSAL_ENGINE_AVAILABLE:
            try:
                self.universal_engine = UniversalPredictionEngine()
                logger.info("🎯 Universal 8D Prediction Engine initialized in predictor agent!")
            except Exception as e:
                logger.error(f"❌ Failed to initialize 8D engine: {e}")

        # Feature engineering
        self.feature_extractors = {
            'team_performance': self._extract_team_performance_features,
            'recent_form': self._extract_recent_form_features,
            'head_to_head': self._extract_head_to_head_features,
            'statistical': self._extract_statistical_features
        }
        
        logger.info(f"🎯 PredictorAgent {self.agent_id} initialized with {len(self.prediction_targets)} targets")
    
    async def _initialize_systems(self):
        """⚙️ Initialize prediction systems"""
        # Load existing models if available
        await self._load_existing_models()
        
        # Subscribe to analysis results for training data
        await self.send_message('*', 'subscribe', {
            'agent_id': self.agent_id,
            'message_types': ['analysis_complete', 'data_available', 'pattern_discovered']
        })
        
        logger.info("⚙️ Prediction systems initialized")
    
    async def _agent_behavior(self):
        """🎯 Core prediction autonomous behavior"""
        # Process training queue
        await self._process_training_queue()
        
        # Check model performance and retrain if needed
        await self._monitor_model_performance()
        
        # Generate proactive predictions
        await self._generate_proactive_predictions()
        
        # Optimize model portfolio
        await self._optimize_model_portfolio()
        
        # Clean prediction cache
        await self._clean_prediction_cache()
        
        await asyncio.sleep(1)
    
    async def _agent_specific_adaptation(self):
        """🧠 Adapt prediction strategies based on performance"""
        # Analyze model performance across sports
        sport_performances = {}
        
        for sport, model_ids in self.active_models.items():
            if model_ids:
                sport_accuracy = np.mean([
                    self.models[model_id].accuracy 
                    for model_id in model_ids 
                    if model_id in self.models
                ])
                sport_performances[sport] = sport_accuracy
        
        # Adapt based on overall performance
        overall_performance = np.mean(list(sport_performances.values())) if sport_performances else 0.0
        
        if overall_performance < 0.6:
            # Poor performance - increase training frequency
            self.retrain_threshold = 0.03  # More sensitive retraining
            logger.info("🧠 Adapted to more frequent retraining due to poor performance")
        elif overall_performance > 0.8:
            # Good performance - can be more conservative
            self.retrain_threshold = 0.08  # Less frequent retraining
            logger.info("🧠 Adapted to less frequent retraining due to good performance")
        
        # Adapt algorithm selection based on sport-specific performance
        await self._adapt_algorithm_selection()
    
    async def _handle_message(self, message):
        """📨 Handle messages from other agents"""
        await super()._handle_message(message)
        
        if message.message_type == "analysis_complete":
            await self._handle_analysis_complete(message)
        elif message.message_type == "prediction_request":
            await self._handle_prediction_request(message)
        elif message.message_type == "training_data":
            await self._handle_training_data(message)
        elif message.message_type == "pattern_discovered":
            await self._handle_pattern_discovered(message)
    
    async def _handle_analysis_complete(self, message):
        """📊 Handle completed analysis for training data"""
        payload = message.payload
        sport = payload.get('sport')
        result = payload.get('result')
        
        if sport and result:
            # Extract training samples from analysis result
            training_samples = await self._extract_training_samples(sport, result)
            
            if training_samples:
                # Add to training data
                self.training_data[sport].extend(training_samples)
                
                # Keep only recent samples
                if len(self.training_data[sport]) > self.max_training_samples:
                    self.training_data[sport] = self.training_data[sport][-self.max_training_samples:]
                
                # Schedule training if we have enough data
                if len(self.training_data[sport]) >= self.min_training_samples:
                    self.training_queue.append({
                        'sport': sport,
                        'priority': 1,
                        'trigger': 'new_analysis'
                    })
                
                logger.info(f"📊 Added {len(training_samples)} training samples for {sport}")
    
    async def _handle_prediction_request(self, message):
        """🎯 Handle prediction requests"""
        payload = message.payload
        sport = payload.get('sport')
        game_data = payload.get('game_data')
        prediction_type = payload.get('prediction_type', 'winner')
        
        if sport and game_data:
            prediction_result = await self._make_prediction(sport, game_data, prediction_type)
            
            await self.send_message(message.sender_id, 'prediction_result', {
                'sport': sport,
                'prediction_type': prediction_type,
                'result': prediction_result,
                'confidence': prediction_result.get('confidence', 0.0),
                'model_info': prediction_result.get('model_info', {}),
                'predictor': self.agent_id
            })
            
            logger.info(f"🎯 Sent {prediction_type} prediction for {sport}")
    
    async def _extract_training_samples(self, sport: str, analysis_result: Dict[str, Any]) -> List[Dict[str, Any]]:
        """📝 Extract training samples from analysis results"""
        samples = []
        
        # Extract from trend analysis
        trend_analysis = analysis_result.get('trend_analysis', {})
        trends = trend_analysis.get('trends', {})
        
        for team, trend_data in trends.items():
            if trend_data.get('games_analyzed', 0) >= 3:
                sample = {
                    'team': team,
                    'avg_score': trend_data.get('avg_score', 0),
                    'trend_direction': trend_data.get('direction'),
                    'trend_confidence': trend_data.get('confidence', 0),
                    'score_variance': trend_data.get('score_variance', 0),
                    'games_count': trend_data.get('games_analyzed', 0),
                    'timestamp': time.time()
                }
                samples.append(sample)
        
        # Extract from correlation analysis
        correlation_analysis = analysis_result.get('correlation_analysis', {})
        correlations = correlation_analysis.get('correlations', {})
        
        home_away = correlations.get('home_away_advantage', {})
        if isinstance(home_away, dict) and 'correlation' in home_away:
            samples.append({
                'feature_type': 'home_away_advantage',
                'correlation_value': home_away['correlation'],
                'significance': home_away.get('significance', 0),
                'teams_analyzed': home_away.get('teams_analyzed', 0),
                'timestamp': time.time()
            })
        
        return samples
    
    async def _process_training_queue(self):
        """📋 Process queued training tasks"""
        while self.training_queue and len(self.running_tasks) < self.max_concurrent_tasks:
            training_task = self.training_queue.popleft()
            
            training_coroutine = asyncio.create_task(self._execute_training(training_task))
            self.running_tasks.add(training_coroutine)
    
    async def _execute_training(self, training_task: Dict[str, Any]):
        """⚡ Execute model training"""
        sport = training_task['sport']
        start_time = time.time()
        
        try:
            logger.info(f"⚡ Training models for {sport}")
            
            # Get training data
            training_samples = self.training_data.get(sport, [])
            if len(training_samples) < self.min_training_samples:
                logger.warning(f"⚠️ Insufficient training data for {sport}: {len(training_samples)}")
                return
            
            # Train models for each prediction target
            models_trained = 0
            for target, config in self.prediction_targets.items():
                model_trained = await self._train_model_for_target(sport, target, training_samples)
                if model_trained:
                    models_trained += 1
            
            # Record training success
            duration = time.time() - start_time
            self.memory.record_experience(
                f"training_{sport}", 'success', duration,
                {'models_trained': models_trained, 'training_samples': len(training_samples)}
            )
            
            logger.info(f"✅ Training completed for {sport}: {models_trained} models trained in {duration:.2f}s")
            
            # Broadcast training completion
            await self.broadcast_message('training_complete', {
                'sport': sport,
                'models_trained': models_trained,
                'training_samples': len(training_samples),
                'trainer': self.agent_id
            })
            
        except Exception as e:
            # Record training failure
            duration = time.time() - start_time
            self.memory.record_experience(
                f"training_{sport}", 'failure', duration,
                {'error': str(e), 'sport': sport}
            )
            
            logger.error(f"❌ Training failed for {sport}: {e}")
    
    async def _train_model_for_target(self, sport: str, target: str, training_samples: List[Dict[str, Any]]) -> bool:
        """🎯 Train model for specific prediction target"""
        try:
            # Prepare training data
            X, y = await self._prepare_training_data(training_samples, target)
            
            if len(X) < self.min_training_samples:
                return False
            
            # Select best algorithm
            algorithm_name = await self._select_best_algorithm(sport, target, X, y)
            
            # Create and train model
            model_id = f"{sport}_{target}_{algorithm_name}_{int(time.time())}"
            model = PredictionModel(model_id, target, sport, target)
            
            # Configure algorithm
            target_config = self.prediction_targets[target]
            if target_config['type'] == 'classification':
                algorithm_class = self.available_algorithms['classification'][algorithm_name]
                model.model = algorithm_class(random_state=42, n_estimators=100 if 'forest' in algorithm_name else None)
            else:
                algorithm_class = self.available_algorithms['regression'][algorithm_name]
                model.model = algorithm_class(random_state=42, n_estimators=100 if 'boosting' in algorithm_name else None)
            
            # Scale features if needed
            X_scaled = model.scaler.fit_transform(X)
            
            # Encode labels for classification
            if target_config['type'] == 'classification':
                y_encoded = model.label_encoder.fit_transform(y)
            else:
                y_encoded = y
            
            # Train model
            model.model.fit(X_scaled, y_encoded)
            
            # Evaluate model
            accuracy = await self._evaluate_model(model, X_scaled, y_encoded, target_config['type'])
            model.accuracy = accuracy
            model.training_samples = len(X)
            model.last_trained = datetime.now()
            
            # Store feature importance
            if hasattr(model.model, 'feature_importances_'):
                model.feature_importance = dict(zip(
                    [f"feature_{i}" for i in range(len(model.model.feature_importances_))],
                    model.model.feature_importances_
                ))
            
            # Add to model portfolio
            self.models[model_id] = model
            self.active_models[sport].append(model_id)
            
            # Update performance tracking
            self.model_performance[sport][target] = {
                'accuracy': accuracy,
                'training_samples': len(X),
                'last_trained': model.last_trained.isoformat(),
                'algorithm': algorithm_name
            }
            
            logger.info(f"🎯 Trained {target} model for {sport}: {accuracy:.3f} accuracy ({algorithm_name})")
            return True
            
        except Exception as e:
            logger.error(f"❌ Model training failed for {sport}.{target}: {e}")
            return False
    
    async def _prepare_training_data(self, training_samples: List[Dict[str, Any]], target: str) -> Tuple[np.ndarray, np.ndarray]:
        """📝 Prepare training data for ML model"""
        X = []
        y = []
        
        for sample in training_samples:
            # Extract features
            features = []
            
            if target == 'winner':
                # Features for winner prediction
                if 'avg_score' in sample:
                    features.extend([
                        sample.get('avg_score', 0),
                        sample.get('trend_confidence', 0),
                        sample.get('score_variance', 0),
                        sample.get('games_count', 0)
                    ])
                    
                    # Target: winning tendency based on trend
                    trend_direction = sample.get('trend_direction', 'stable')
                    y.append(1 if trend_direction == 'improving' else 0)
                    X.append(features)
            
            elif target == 'total_score':
                # Features for total score prediction
                if 'avg_score' in sample:
                    features.extend([
                        sample.get('avg_score', 0),
                        sample.get('score_variance', 0),
                        sample.get('games_count', 0),
                        sample.get('trend_confidence', 0)
                    ])
                    
                    # Target: average score
                    y.append(sample.get('avg_score', 0))
                    X.append(features)
            
            elif target == 'score_difference':
                # Features for score difference prediction
                if 'score_variance' in sample:
                    features.extend([
                        sample.get('score_variance', 0),
                        sample.get('avg_score', 0),
                        sample.get('trend_confidence', 0)
                    ])
                    
                    # Target: score variance as proxy for competitiveness
                    y.append(sample.get('score_variance', 0))
                    X.append(features)
        
        if not X or not y:
            return np.array([]), np.array([])
        
        return np.array(X), np.array(y)
    
    async def _select_best_algorithm(self, sport: str, target: str, X: np.ndarray, y: np.ndarray) -> str:
        """🧠 Select best algorithm for the data"""
        target_config = self.prediction_targets[target]
        algorithms = self.available_algorithms[target_config['type']]
        
        best_algorithm = list(algorithms.keys())[0]  # Default
        best_score = 0.0
        
        # Try each algorithm with cross-validation
        for algorithm_name, algorithm_class in algorithms.items():
            try:
                if target_config['type'] == 'classification':
                    model = algorithm_class(random_state=42, n_estimators=50 if 'forest' in algorithm_name else None)
                else:
                    model = algorithm_class(random_state=42, n_estimators=50 if 'boosting' in algorithm_name else None)
                
                # Cross-validation score
                scores = cross_val_score(model, X, y, cv=min(3, len(X)//5), scoring='accuracy' if target_config['type'] == 'classification' else 'neg_mean_squared_error')
                avg_score = np.mean(scores)
                
                if target_config['type'] == 'regression':
                    avg_score = -avg_score  # Convert negative MSE to positive
                
                if avg_score > best_score:
                    best_score = avg_score
                    best_algorithm = algorithm_name
                    
            except Exception as e:
                logger.warning(f"⚠️ Algorithm {algorithm_name} failed for {sport}.{target}: {e}")
        
        logger.info(f"🧠 Selected {best_algorithm} for {sport}.{target} (score: {best_score:.3f})")
        return best_algorithm
    
    async def _evaluate_model(self, model: PredictionModel, X: np.ndarray, y: np.ndarray, model_type: str) -> float:
        """📊 Evaluate model performance"""
        if len(X) < 5:
            return 0.0
        
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            if model_type == 'classification':
                y_pred = model.model.predict(X_test)
                accuracy = accuracy_score(y_test, y_pred)
            else:
                y_pred = model.model.predict(X_test)
                mse = mean_squared_error(y_test, y_pred)
                # Convert MSE to accuracy-like metric (lower MSE = higher accuracy)
                max_mse = np.var(y_test) if len(y_test) > 1 else 1.0
                accuracy = max(0, 1 - mse / max_mse) if max_mse > 0 else 0.0
            
            return float(accuracy)
            
        except Exception as e:
            logger.error(f"❌ Model evaluation failed: {e}")
            return 0.0
    
    async def _make_prediction(self, sport: str, game_data: Dict[str, Any], prediction_type: str) -> Dict[str, Any]:
        """🎯 Make prediction for game - USING 8D DIMENSIONAL ANALYSIS!"""
        # 🔥💀🔥 PRIORITY #1: TRY UNIVERSAL 8D PREDICTION ENGINE FIRST! 💀🔥💀
        if self.universal_engine:
            try:
                logger.info(f"🎯 Using Universal 8D Engine for {sport} prediction!")

                # Determine league_id from sport
                league_mapping = {
                    'soccer': 'EPL',
                    'football': 'NFL',
                    'basketball': 'NBA',
                    'uefa': 'UEFA',
                    'liga_mx': 'LIGA_MX'
                }
                league_id = league_mapping.get(sport.lower(), sport.upper())

                # Call the Universal 8D Engine
                result = await self.universal_engine.analyze_game(game_data, league_id)

                if result and 'confidence' in result:
                    logger.info(f"✅ 8D Engine prediction successful! Confidence: {result['confidence']}%")
                    return {
                        'prediction': result.get('prediction'),
                        'confidence': result.get('confidence', 0) / 100.0,  # Convert to 0-1 scale
                        'model_info': {
                            'engine': 'Universal_8D_Dimensional_Analysis',
                            'dimensions_used': result.get('dimensions_summary', {}),
                            'prediction_type': prediction_type
                        },
                        'cached': False,
                        'engine_type': '8D_REAL'
                    }
            except Exception as e:
                logger.warning(f"⚠️ 8D engine failed (will try ML fallback): {e}")

        # Check cache (for ML predictions)
        cache_key = f"{sport}_{prediction_type}_{hash(str(game_data))}"
        if cache_key in self.prediction_cache:
            cached_result = self.prediction_cache[cache_key]
            if time.time() - self.cache_timestamps[cache_key] < self.cache_ttl:
                cached_result['cached'] = True
                return cached_result

        # Find best model for this prediction (ML FALLBACK)
        best_model = await self._select_best_model(sport, prediction_type)
        
        if not best_model:
            return {
                'error': f'No trained model available for {sport}.{prediction_type}',
                'confidence': 0.0
            }
        
        try:
            # Extract features from game data
            features = await self._extract_game_features(game_data, prediction_type)
            
            if not features:
                return {
                    'error': 'Unable to extract features from game data',
                    'confidence': 0.0
                }
            
            # Make prediction
            features_array = np.array([features])
            features_scaled = best_model.scaler.transform(features_array)
            
            if best_model.model_type in ['winner', 'classification']:
                prediction_encoded = best_model.model.predict(features_scaled)[0]
                prediction_proba = best_model.model.predict_proba(features_scaled)[0]
                
                # Decode prediction
                prediction = best_model.label_encoder.inverse_transform([prediction_encoded])[0]
                confidence = float(np.max(prediction_proba))
            else:
                prediction = float(best_model.model.predict(features_scaled)[0])
                # For regression, confidence based on historical accuracy
                confidence = best_model.accuracy
            
            result = {
                'prediction': prediction,
                'confidence': confidence,
                'model_info': {
                    'model_id': best_model.model_id,
                    'model_type': best_model.model_type,
                    'accuracy': best_model.accuracy,
                    'training_samples': best_model.training_samples,
                    'last_trained': best_model.last_trained.isoformat() if best_model.last_trained else None
                },
                'features_used': len(features),
                'cached': False
            }
            
            # Cache result
            self.prediction_cache[cache_key] = result.copy()
            self.cache_timestamps[cache_key] = time.time()
            
            # Update model usage
            best_model.predictions_made += 1
            
            logger.info(f"🎯 Prediction for {sport}.{prediction_type}: {prediction} (confidence: {confidence:.2f})")
            return result
            
        except Exception as e:
            logger.error(f"❌ Prediction failed for {sport}.{prediction_type}: {e}")
            return {
                'error': str(e),
                'confidence': 0.0
            }
    
    async def _select_best_model(self, sport: str, prediction_type: str) -> Optional[PredictionModel]:
        """🏆 Select best model for prediction"""
        sport_models = self.active_models.get(sport, [])
        
        # Filter models by prediction type
        candidate_models = [
            self.models[model_id] 
            for model_id in sport_models 
            if model_id in self.models and self.models[model_id].model_type == prediction_type
        ]
        
        if not candidate_models:
            return None
        
        # Select model with highest accuracy
        best_model = max(candidate_models, key=lambda m: m.accuracy)
        
        # Minimum accuracy threshold
        if best_model.accuracy < self.min_accuracy_threshold:
            logger.warning(f"⚠️ Best model for {sport}.{prediction_type} has low accuracy: {best_model.accuracy:.2f}")
        
        return best_model
    
    async def _extract_game_features(self, game_data: Dict[str, Any], prediction_type: str) -> List[float]:
        """🔍 Extract features from game data for prediction"""
        features = []
        
        teams = game_data.get('teams', [])
        if len(teams) != 2:
            return features
        
        team1, team2 = teams
        
        # Basic features
        features.extend([
            float(team1.get('score', 0) or 0),
            float(team2.get('score', 0) or 0),
            1.0 if team1.get('home_away') == 'home' else 0.0,
            1.0 if team2.get('home_away') == 'home' else 0.0
        ])
        
        # Additional features based on prediction type
        if prediction_type == 'winner':
            # Add team strength indicators (simplified)
            team1_strength = len(team1.get('name', '')) / 20.0  # Simplified team strength
            team2_strength = len(team2.get('name', '')) / 20.0
            features.extend([team1_strength, team2_strength])
        
        elif prediction_type == 'total_score':
            # Add scoring potential features
            total_score = float(team1.get('score', 0) or 0) + float(team2.get('score', 0) or 0)
            features.append(total_score)
        
        return features
    
    async def _monitor_model_performance(self):
        """📊 Monitor model performance and trigger retraining"""
        for sport, model_ids in self.active_models.items():
            for model_id in model_ids[:]:  # Copy list to allow modification
                if model_id not in self.models:
                    # Clean up invalid model references
                    self.active_models[sport].remove(model_id)
                    continue
                
                model = self.models[model_id]
                
                # Check if model needs retraining
                if await self._model_needs_retraining(model):
                    logger.info(f"🔄 Scheduling retraining for {model.sport}.{model.model_type}")
                    
                    self.training_queue.append({
                        'sport': sport,
                        'priority': 2,
                        'trigger': 'performance_degradation',
                        'model_id': model_id
                    })
                
                # Remove very poor performing models
                if model.accuracy < 0.3 and model.predictions_made > 10:
                    logger.warning(f"🗑️ Removing poor performing model {model_id} (accuracy: {model.accuracy:.2f})")
                    del self.models[model_id]
                    self.active_models[sport].remove(model_id)
    
    async def _model_needs_retraining(self, model: PredictionModel) -> bool:
        """🔍 Check if model needs retraining"""
        # Retrain if accuracy has dropped significantly
        if hasattr(model, '_initial_accuracy'):
            accuracy_drop = model._initial_accuracy - model.accuracy
            if accuracy_drop > self.retrain_threshold:
                return True
        else:
            model._initial_accuracy = model.accuracy
        
        # Retrain if model is old and has new data available
        if model.last_trained:
            days_since_training = (datetime.now() - model.last_trained).days
            if days_since_training > 7:  # Weekly retraining
                training_data_count = len(self.training_data.get(model.sport, []))
                if training_data_count >= self.min_training_samples:
                    return True
        
        return False
    
    async def _generate_proactive_predictions(self):
        """🎯 Generate proactive predictions for upcoming games"""
        current_time = time.time()
        
        # Check if we should generate proactive predictions (every 15 minutes)
        last_proactive = getattr(self, '_last_proactive_predictions', 0)
        if current_time - last_proactive > 900:
            
            # Request recent game data from data collector
            await self.send_message('*', 'data_request', {
                'request_type': 'upcoming_games',
                'requester': self.agent_id,
                'max_games': 10
            })
            
            self._last_proactive_predictions = current_time
    
    async def _optimize_model_portfolio(self):
        """🏆 Optimize model portfolio by removing redundant models"""
        for sport, model_ids in self.active_models.items():
            if len(model_ids) > 5:  # Too many models for one sport
                # Keep only the best performing models
                sport_models = [(mid, self.models[mid]) for mid in model_ids if mid in self.models]
                sport_models.sort(key=lambda x: x[1].accuracy, reverse=True)
                
                # Keep top 3 models
                to_keep = [mid for mid, _ in sport_models[:3]]
                to_remove = [mid for mid in model_ids if mid not in to_keep]
                
                for model_id in to_remove:
                    if model_id in self.models:
                        del self.models[model_id]
                    self.active_models[sport].remove(model_id)
                
                logger.info(f"🏆 Optimized {sport} model portfolio: kept {len(to_keep)}, removed {len(to_remove)}")
    
    async def _clean_prediction_cache(self):
        """🧹 Clean expired prediction cache"""
        current_time = time.time()
        expired_keys = [
            key for key, timestamp in self.cache_timestamps.items()
            if current_time - timestamp > self.cache_ttl
        ]
        
        for key in expired_keys:
            del self.prediction_cache[key]
            del self.cache_timestamps[key]
        
        if expired_keys:
            logger.debug(f"🧹 Cleaned {len(expired_keys)} expired prediction cache entries")
    
    async def _adapt_algorithm_selection(self):
        """🧠 Adapt algorithm selection based on sport-specific performance"""
        for sport in self.active_models:
            sport_models = [self.models[mid] for mid in self.active_models[sport] if mid in self.models]
            
            if len(sport_models) >= 3:
                # Analyze which algorithms work best for this sport
                algorithm_performance = defaultdict(list)
                
                for model in sport_models:
                    # Extract algorithm from model metadata
                    algorithm = getattr(model, 'algorithm', 'unknown')
                    algorithm_performance[algorithm].append(model.accuracy)
                
                # Find best performing algorithm
                best_algorithm = None
                best_avg_accuracy = 0.0
                
                for algorithm, accuracies in algorithm_performance.items():
                    avg_accuracy = np.mean(accuracies)
                    if avg_accuracy > best_avg_accuracy:
                        best_avg_accuracy = avg_accuracy
                        best_algorithm = algorithm
                
                if best_algorithm and best_avg_accuracy > 0.7:
                    logger.info(f"🧠 {sport} performs best with {best_algorithm} (avg: {best_avg_accuracy:.2f})")
    
    async def _load_existing_models(self):
        """💾 Load existing models from storage"""
        # In a real implementation, this would load from persistent storage
        logger.info("💾 No existing models found (fresh start)")
    
    # =================== FEATURE EXTRACTORS ===================
    
    async def _extract_team_performance_features(self, game_data: Dict[str, Any]) -> List[float]:
        """🏆 Extract team performance features"""
        # Simplified implementation
        teams = game_data.get('teams', [])
        if len(teams) != 2:
            return []
        
        features = []
        for team in teams:
            score = float(team.get('score', 0) or 0)
            features.append(score)
        
        return features
    
    async def _extract_recent_form_features(self, game_data: Dict[str, Any]) -> List[float]:
        """📈 Extract recent form features"""
        # Placeholder for recent form analysis
        return [0.5, 0.5]  # Neutral form
    
    async def _extract_head_to_head_features(self, game_data: Dict[str, Any]) -> List[float]:
        """🤝 Extract head-to-head features"""
        # Placeholder for head-to-head analysis
        return [0.0]  # No historical advantage
    
    async def _extract_statistical_features(self, game_data: Dict[str, Any]) -> List[float]:
        """📊 Extract statistical features"""
        # Placeholder for advanced statistical features
        return [1.0, 1.0]  # Basic stats
    
    # =================== PUBLIC API ===================
    
    async def get_prediction_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive prediction status"""
        total_models = len(self.models)
        total_predictions = sum(model.predictions_made for model in self.models.values())
        avg_accuracy = np.mean([model.accuracy for model in self.models.values()]) if self.models else 0.0
        
        return {
            'agent_id': self.agent_id,
            'timestamp': time.time(),
            'total_models': total_models,
            'total_predictions': total_predictions,
            'average_accuracy': float(avg_accuracy),
            'sports_covered': list(self.active_models.keys()),
            'prediction_targets': list(self.prediction_targets.keys()),
            'training_queue_length': len(self.training_queue),
            'cache_entries': len(self.prediction_cache),
            'model_performance': {
                sport: {
                    target: perf for target, perf in targets.items()
                }
                for sport, targets in self.model_performance.items()
            }
        }
    
    async def predict_game_outcome(self, sport: str, game_data: Dict[str, Any]) -> Dict[str, Any]:
        """🎯 Predict game outcome"""
        return await self._make_prediction(sport, game_data, 'winner')
    
    async def predict_game_score(self, sport: str, game_data: Dict[str, Any]) -> Dict[str, Any]:
        """⚽ Predict game score"""
        return await self._make_prediction(sport, game_data, 'total_score')
    
    async def get_model_info(self, sport: str = None) -> Dict[str, Any]:
        """🤖 Get model information"""
        if sport:
            model_ids = self.active_models.get(sport, [])
            models_info = {
                mid: {
                    'model_type': self.models[mid].model_type,
                    'accuracy': self.models[mid].accuracy,
                    'predictions_made': self.models[mid].predictions_made,
                    'last_trained': self.models[mid].last_trained.isoformat() if self.models[mid].last_trained else None
                }
                for mid in model_ids if mid in self.models
            }
            return {'sport': sport, 'models': models_info}
        else:
            return {
                'all_models': {
                    mid: {
                        'sport': model.sport,
                        'model_type': model.model_type,
                        'accuracy': model.accuracy,
                        'predictions_made': model.predictions_made
                    }
                    for mid, model in self.models.items()
                }
            }

if __name__ == "__main__":
    async def test_predictor():
        agent = PredictorAgent("predictor_001")
        AGENT_REGISTRY.register_agent(agent)
        
        await agent.spawn()
        await asyncio.sleep(3)
        
        # Test prediction with sample data
        test_game = {
            'teams': [
                {'name': 'Team A', 'score': 21, 'home_away': 'home'},
                {'name': 'Team B', 'score': 14, 'home_away': 'away'}
            ]
        }
        
        # Add some training data first
        training_samples = [
            {'team': 'Team A', 'avg_score': 20, 'trend_direction': 'improving', 'trend_confidence': 0.8, 'score_variance': 5, 'games_count': 5},
            {'team': 'Team B', 'avg_score': 15, 'trend_direction': 'stable', 'trend_confidence': 0.6, 'score_variance': 8, 'games_count': 5}
        ]
        agent.training_data['NFL'] = training_samples
        
        # Trigger training
        agent.training_queue.append({'sport': 'NFL', 'priority': 1, 'trigger': 'test'})
        await asyncio.sleep(2)  # Let training complete
        
        # Make prediction
        prediction = await agent.predict_game_outcome('NFL', test_game)
        print(f"🎯 Prediction Result: {json.dumps(prediction, indent=2, default=str)}")
        
        # Get status
        status = await agent.get_prediction_status()
        print(f"📊 Predictor Status: {json.dumps(status, indent=2, default=str)}")
        
        await agent.terminate()
    
    asyncio.run(test_predictor())