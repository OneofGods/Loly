#!/usr/bin/env python3
"""
🔥💀 PHASE 2: ML ANALYTICS COORDINATOR 💀🔥
Machine Learning model coordination and predictive intelligence
"""

import asyncio
import logging
import numpy as np
import pickle
import time
import json
from typing import Dict, List, Set, Any, Optional, Tuple, Union
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, accuracy_score
import joblib

logger = logging.getLogger(__name__)

class ModelType(Enum):
    """🤖 ML model types"""
    PERFORMANCE_PREDICTOR = "performance_predictor"
    ANOMALY_DETECTOR = "anomaly_detector"
    LOAD_FORECASTER = "load_forecaster"
    FAILURE_PREDICTOR = "failure_predictor"
    OPTIMIZATION_RECOMMENDER = "optimization_recommender"

class TrainingStatus(Enum):
    """📊 Model training status"""
    UNTRAINED = "untrained"
    TRAINING = "training"
    TRAINED = "trained"
    UPDATING = "updating"
    FAILED = "failed"

@dataclass
class MLModel:
    """🧠 ML model container"""
    model_id: str
    model_type: ModelType
    model: Any = None
    scaler: StandardScaler = None
    training_status: TrainingStatus = TrainingStatus.UNTRAINED
    accuracy: float = 0.0
    last_trained: Optional[datetime] = None
    training_data_size: int = 0
    feature_names: List[str] = field(default_factory=list)
    hyperparameters: Dict[str, Any] = field(default_factory=dict)

@dataclass
class PredictionResult:
    """📈 ML prediction result"""
    model_id: str
    prediction: Union[float, List[float], str]
    confidence: float
    timestamp: datetime
    input_features: Dict[str, Any]
    model_accuracy: float

class MLAnalyticsCoordinator:
    """
    🧠 ML ANALYTICS COORDINATOR
    
    Provides intelligent ML-powered analytics:
    - Performance prediction and optimization
    - Anomaly detection and alerting
    - Load forecasting and capacity planning
    - Failure prediction and prevention
    - Real-time model updates and learning
    - Distributed model coordination
    """
    
    def __init__(self, message_bus, swarm_coordinator, scaling_manager):
        self.message_bus = message_bus
        self.swarm_coordinator = swarm_coordinator
        self.scaling_manager = scaling_manager
        
        # Model registry
        self.models: Dict[str, MLModel] = {}
        self.model_performance_history: Dict[str, List[Dict[str, Any]]] = {}
        
        # Training data management
        self.training_data: Dict[str, List[Dict[str, Any]]] = {}
        self.feature_extractors: Dict[ModelType, callable] = {}
        self.data_collection_window = timedelta(hours=24)
        
        # Prediction cache
        self.prediction_cache: Dict[str, Dict[str, PredictionResult]] = {}
        self.cache_ttl = 300  # 5 minutes
        
        # Model ensemble
        self.ensemble_weights: Dict[str, float] = {}
        self.ensemble_predictions: Dict[str, List[PredictionResult]] = {}
        
        # Training configuration
        self.min_training_samples = 100
        self.retrain_threshold = 0.1  # Retrain if accuracy drops by 10%
        self.update_frequency = timedelta(hours=6)
        
        # Initialize ML models
        self._initialize_models()
        self._setup_feature_extractors()
        
        logger.info("🧠 MLAnalyticsCoordinator initialized")
    
    def _initialize_models(self):
        """🤖 Initialize ML models"""
        
        # Performance predictor
        perf_model = MLModel(
            model_id="agent_performance_predictor",
            model_type=ModelType.PERFORMANCE_PREDICTOR,
            model=RandomForestRegressor(
                n_estimators=100,
                max_depth=10,
                random_state=42
            ),
            scaler=StandardScaler(),
            hyperparameters={
                'n_estimators': 100,
                'max_depth': 10,
                'min_samples_split': 5
            }
        )
        self.models[perf_model.model_id] = perf_model
        
        # Anomaly detector
        anomaly_model = MLModel(
            model_id="system_anomaly_detector",
            model_type=ModelType.ANOMALY_DETECTOR,
            model=IsolationForest(
                contamination=0.1,
                random_state=42
            ),
            scaler=StandardScaler(),
            hyperparameters={
                'contamination': 0.1,
                'n_estimators': 100
            }
        )
        self.models[anomaly_model.model_id] = anomaly_model
        
        # Load forecaster
        load_model = MLModel(
            model_id="load_forecaster",
            model_type=ModelType.LOAD_FORECASTER,
            model=LinearRegression(),
            scaler=StandardScaler(),
            hyperparameters={}
        )
        self.models[load_model.model_id] = load_model
        
        # Failure predictor
        failure_model = MLModel(
            model_id="failure_predictor",
            model_type=ModelType.FAILURE_PREDICTOR,
            model=RandomForestRegressor(
                n_estimators=50,
                max_depth=8,
                random_state=42
            ),
            scaler=StandardScaler(),
            hyperparameters={
                'n_estimators': 50,
                'max_depth': 8
            }
        )
        self.models[failure_model.model_id] = failure_model
        
        logger.info(f"🤖 Initialized {len(self.models)} ML models")
    
    def _setup_feature_extractors(self):
        """🔧 Setup feature extraction functions"""
        
        self.feature_extractors[ModelType.PERFORMANCE_PREDICTOR] = self._extract_performance_features
        self.feature_extractors[ModelType.ANOMALY_DETECTOR] = self._extract_anomaly_features
        self.feature_extractors[ModelType.LOAD_FORECASTER] = self._extract_load_features
        self.feature_extractors[ModelType.FAILURE_PREDICTOR] = self._extract_failure_features
    
    async def start_analytics_loop(self):
        """🔄 Start ML analytics processing loop"""
        logger.info("🔄 Starting ML analytics loop")
        
        # Start data collection
        data_task = asyncio.create_task(self._data_collection_loop())
        
        # Start model training
        training_task = asyncio.create_task(self._model_training_loop())
        
        # Start prediction service
        prediction_task = asyncio.create_task(self._prediction_service_loop())
        
        # Start model monitoring
        monitoring_task = asyncio.create_task(self._model_monitoring_loop())
        
        # Run all analytics tasks
        await asyncio.gather(
            data_task, training_task, prediction_task, monitoring_task,
            return_exceptions=True
        )
    
    async def _data_collection_loop(self):
        """📊 Continuous data collection for ML training"""
        while True:
            try:
                # Collect data from various sources
                await self._collect_agent_performance_data()
                await self._collect_system_metrics_data()
                await self._collect_load_data()
                await self._collect_failure_data()
                
                await asyncio.sleep(30)  # Collect every 30 seconds
                
            except Exception as e:
                logger.error(f"❌ Data collection error: {e}")
                await asyncio.sleep(10)
    
    async def _collect_agent_performance_data(self):
        """📊 Collect agent performance data"""
        swarm_status = await self.swarm_coordinator.get_swarm_status()
        
        for agent_id, agent_info in swarm_status.get('agents', {}).items():
            performance_data = {
                'timestamp': datetime.now(),
                'agent_id': agent_id,
                'cpu_usage': agent_info.get('cpu_usage', 0.0),
                'memory_usage': agent_info.get('memory_usage', 0.0),
                'active_tasks': agent_info.get('active_tasks', 0),
                'completed_tasks': agent_info.get('completed_tasks', 0),
                'failed_tasks': agent_info.get('failed_tasks', 0),
                'response_time': agent_info.get('avg_response_time', 0.0),
                'throughput': agent_info.get('throughput', 0.0),
                'error_rate': agent_info.get('error_rate', 0.0),
                'health_score': agent_info.get('health_score', 1.0)
            }
            
            # Store for training
            if ModelType.PERFORMANCE_PREDICTOR not in self.training_data:
                self.training_data[ModelType.PERFORMANCE_PREDICTOR] = []
            
            self.training_data[ModelType.PERFORMANCE_PREDICTOR].append(performance_data)
            
            # Limit data size
            max_samples = 10000
            if len(self.training_data[ModelType.PERFORMANCE_PREDICTOR]) > max_samples:
                self.training_data[ModelType.PERFORMANCE_PREDICTOR] = \
                    self.training_data[ModelType.PERFORMANCE_PREDICTOR][-max_samples:]
    
    async def _collect_system_metrics_data(self):
        """📊 Collect system-level metrics"""
        scaling_status = await self.scaling_manager.get_scaling_status()
        
        system_data = {
            'timestamp': datetime.now(),
            'total_agents': scaling_status.get('current_agents', 0),
            'healthy_agents': scaling_status['agent_health']['healthy'],
            'degraded_agents': scaling_status['agent_health']['degraded'],
            'unhealthy_agents': scaling_status['agent_health']['unhealthy'],
            'avg_cpu_usage': scaling_status['resource_utilization']['avg_cpu_usage'],
            'avg_memory_usage': scaling_status['resource_utilization']['avg_memory_usage'],
            'total_active_tasks': scaling_status['resource_utilization']['total_active_tasks'],
            'scaling_in_progress': scaling_status['scaling_in_progress']
        }
        
        # Store for anomaly detection
        if ModelType.ANOMALY_DETECTOR not in self.training_data:
            self.training_data[ModelType.ANOMALY_DETECTOR] = []
        
        self.training_data[ModelType.ANOMALY_DETECTOR].append(system_data)
    
    async def _collect_load_data(self):
        """📊 Collect load forecasting data"""
        # This would collect historical load patterns
        # For now, simulate load data collection
        pass
    
    async def _collect_failure_data(self):
        """📊 Collect failure prediction data"""
        # This would collect failure indicators and patterns
        # For now, simulate failure data collection
        pass
    
    async def _model_training_loop(self):
        """🎓 Continuous model training and updates"""
        while True:
            try:
                for model_id, model in self.models.items():
                    if await self._should_train_model(model):
                        await self._train_model(model)
                
                await asyncio.sleep(3600)  # Check every hour
                
            except Exception as e:
                logger.error(f"❌ Model training loop error: {e}")
                await asyncio.sleep(300)
    
    async def _should_train_model(self, model: MLModel) -> bool:
        """🤔 Determine if model should be trained"""
        model_type = model.model_type
        
        # Check if we have enough training data
        if model_type not in self.training_data:
            return False
        
        data_size = len(self.training_data[model_type])
        if data_size < self.min_training_samples:
            return False
        
        # Check if model is untrained
        if model.training_status == TrainingStatus.UNTRAINED:
            return True
        
        # Check if it's time for retraining
        if model.last_trained:
            time_since_training = datetime.now() - model.last_trained
            if time_since_training > self.update_frequency:
                return True
        
        # Check if model accuracy has degraded
        if model.accuracy > 0 and await self._check_model_degradation(model):
            return True
        
        return False
    
    async def _train_model(self, model: MLModel):
        """🎓 Train ML model"""
        try:
            model.training_status = TrainingStatus.TRAINING
            logger.info(f"🎓 Training model {model.model_id}")
            
            # Extract features and targets
            features, targets = await self._prepare_training_data(model)
            
            if len(features) < self.min_training_samples:
                logger.warning(f"⚠️ Insufficient training data for {model.model_id}")
                return
            
            # Split data for training and validation
            split_idx = int(len(features) * 0.8)
            X_train, X_val = features[:split_idx], features[split_idx:]
            y_train, y_val = targets[:split_idx], targets[split_idx:]
            
            # Scale features
            X_train_scaled = model.scaler.fit_transform(X_train)
            X_val_scaled = model.scaler.transform(X_val)
            
            # Train model
            if model.model_type == ModelType.ANOMALY_DETECTOR:
                # Unsupervised training for anomaly detection
                model.model.fit(X_train_scaled)
                predictions = model.model.predict(X_val_scaled)
                # For anomaly detection, we'll use a simple metric
                model.accuracy = np.mean(predictions == 1)  # Normal samples ratio
            else:
                # Supervised training
                model.model.fit(X_train_scaled, y_train)
                predictions = model.model.predict(X_val_scaled)
                
                # Calculate accuracy/error
                if model.model_type in [ModelType.PERFORMANCE_PREDICTOR, ModelType.LOAD_FORECASTER]:
                    mse = mean_squared_error(y_val, predictions)
                    model.accuracy = 1.0 / (1.0 + mse)  # Convert MSE to accuracy-like metric
                else:
                    model.accuracy = accuracy_score(y_val, predictions)
            
            # Update model status
            model.training_status = TrainingStatus.TRAINED
            model.last_trained = datetime.now()
            model.training_data_size = len(features)
            
            logger.info(f"✅ Model {model.model_id} trained successfully (accuracy: {model.accuracy:.3f})")
            
            # Save model
            await self._save_model(model)
            
        except Exception as e:
            logger.error(f"❌ Model training failed for {model.model_id}: {e}")
            model.training_status = TrainingStatus.FAILED
    
    async def _prepare_training_data(self, model: MLModel) -> Tuple[np.ndarray, np.ndarray]:
        """📊 Prepare training data for ML model"""
        model_type = model.model_type
        raw_data = self.training_data.get(model_type, [])
        
        if not raw_data:
            return np.array([]), np.array([])
        
        # Extract features using appropriate extractor
        feature_extractor = self.feature_extractors.get(model_type)
        if not feature_extractor:
            raise ValueError(f"No feature extractor for {model_type}")
        
        features = []
        targets = []
        
        for data_point in raw_data:
            feature_vector, target_value = await feature_extractor(data_point)
            if feature_vector is not None and target_value is not None:
                features.append(feature_vector)
                targets.append(target_value)
        
        return np.array(features), np.array(targets)
    
    async def _extract_performance_features(self, data_point: Dict[str, Any]) -> Tuple[Optional[List[float]], Optional[float]]:
        """🔧 Extract features for performance prediction"""
        try:
            features = [
                data_point.get('cpu_usage', 0.0),
                data_point.get('memory_usage', 0.0),
                data_point.get('active_tasks', 0),
                data_point.get('completed_tasks', 0),
                data_point.get('failed_tasks', 0),
                data_point.get('response_time', 0.0),
                data_point.get('error_rate', 0.0)
            ]
            
            # Target: throughput (performance metric)
            target = data_point.get('throughput', 0.0)
            
            return features, target
            
        except Exception as e:
            logger.error(f"❌ Feature extraction failed: {e}")
            return None, None
    
    async def _extract_anomaly_features(self, data_point: Dict[str, Any]) -> Tuple[Optional[List[float]], Optional[float]]:
        """🔧 Extract features for anomaly detection"""
        try:
            features = [
                data_point.get('total_agents', 0),
                data_point.get('healthy_agents', 0),
                data_point.get('degraded_agents', 0),
                data_point.get('unhealthy_agents', 0),
                data_point.get('avg_cpu_usage', 0.0),
                data_point.get('avg_memory_usage', 0.0),
                data_point.get('total_active_tasks', 0),
                float(data_point.get('scaling_in_progress', False))
            ]
            
            # For anomaly detection, target is typically not used
            return features, 1.0  # Normal behavior
            
        except Exception as e:
            logger.error(f"❌ Anomaly feature extraction failed: {e}")
            return None, None
    
    async def _extract_load_features(self, data_point: Dict[str, Any]) -> Tuple[Optional[List[float]], Optional[float]]:
        """🔧 Extract features for load forecasting"""
        # This would extract time-series features for load prediction
        # For now, return dummy data
        return [1.0, 2.0, 3.0], 1.0
    
    async def _extract_failure_features(self, data_point: Dict[str, Any]) -> Tuple[Optional[List[float]], Optional[float]]:
        """🔧 Extract features for failure prediction"""
        # This would extract failure indicator features
        # For now, return dummy data
        return [1.0, 2.0, 3.0], 0.0
    
    async def _check_model_degradation(self, model: MLModel) -> bool:
        """📉 Check if model performance has degraded"""
        # This would implement model performance monitoring
        # For now, return False (no degradation)
        return False
    
    async def _save_model(self, model: MLModel):
        """💾 Save trained model to disk"""
        try:
            model_path = f"/tmp/ml_models/{model.model_id}.pkl"
            
            # Create directory if it doesn't exist
            import os
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            
            # Save model and scaler
            model_data = {
                'model': model.model,
                'scaler': model.scaler,
                'metadata': {
                    'model_id': model.model_id,
                    'model_type': model.model_type.value,
                    'accuracy': model.accuracy,
                    'last_trained': model.last_trained.isoformat() if model.last_trained else None,
                    'training_data_size': model.training_data_size,
                    'hyperparameters': model.hyperparameters
                }
            }
            
            joblib.dump(model_data, model_path)
            logger.info(f"💾 Model {model.model_id} saved to {model_path}")
            
        except Exception as e:
            logger.error(f"❌ Model saving failed for {model.model_id}: {e}")
    
    async def _prediction_service_loop(self):
        """🔮 Continuous prediction service"""
        while True:
            try:
                # Generate predictions for all trained models
                for model_id, model in self.models.items():
                    if model.training_status == TrainingStatus.TRAINED:
                        await self._generate_predictions(model)
                
                await asyncio.sleep(60)  # Generate predictions every minute
                
            except Exception as e:
                logger.error(f"❌ Prediction service error: {e}")
                await asyncio.sleep(30)
    
    async def _generate_predictions(self, model: MLModel):
        """🔮 Generate predictions using trained model"""
        try:
            # Get current system state for prediction
            current_features = await self._get_current_features(model.model_type)
            
            if current_features is None:
                return
            
            # Scale features
            features_scaled = model.scaler.transform([current_features])
            
            # Make prediction
            prediction = model.model.predict(features_scaled)[0]
            
            # Calculate confidence (simplified)
            confidence = min(0.95, model.accuracy + np.random.normal(0, 0.05))
            confidence = max(0.0, confidence)
            
            # Create prediction result
            prediction_result = PredictionResult(
                model_id=model.model_id,
                prediction=prediction,
                confidence=confidence,
                timestamp=datetime.now(),
                input_features={f"feature_{i}": v for i, v in enumerate(current_features)},
                model_accuracy=model.accuracy
            )
            
            # Cache prediction
            if model.model_id not in self.prediction_cache:
                self.prediction_cache[model.model_id] = {}
            
            self.prediction_cache[model.model_id]['latest'] = prediction_result
            
            # Process prediction
            await self._process_prediction(prediction_result)
            
        except Exception as e:
            logger.error(f"❌ Prediction generation failed for {model.model_id}: {e}")
    
    async def _get_current_features(self, model_type: ModelType) -> Optional[List[float]]:
        """📊 Get current features for prediction"""
        try:
            if model_type == ModelType.PERFORMANCE_PREDICTOR:
                # Get average agent performance features
                swarm_status = await self.swarm_coordinator.get_swarm_status()
                agents = swarm_status.get('agents', {})
                
                if not agents:
                    return None
                
                avg_cpu = np.mean([a.get('cpu_usage', 0) for a in agents.values()])
                avg_memory = np.mean([a.get('memory_usage', 0) for a in agents.values()])
                total_active = sum(a.get('active_tasks', 0) for a in agents.values())
                total_completed = sum(a.get('completed_tasks', 0) for a in agents.values())
                total_failed = sum(a.get('failed_tasks', 0) for a in agents.values())
                avg_response = np.mean([a.get('avg_response_time', 0) for a in agents.values()])
                avg_error = np.mean([a.get('error_rate', 0) for a in agents.values()])
                
                return [avg_cpu, avg_memory, total_active, total_completed, total_failed, avg_response, avg_error]
            
            elif model_type == ModelType.ANOMALY_DETECTOR:
                # Get system-level features
                scaling_status = await self.scaling_manager.get_scaling_status()
                
                return [
                    scaling_status.get('current_agents', 0),
                    scaling_status['agent_health']['healthy'],
                    scaling_status['agent_health']['degraded'],
                    scaling_status['agent_health']['unhealthy'],
                    scaling_status['resource_utilization']['avg_cpu_usage'],
                    scaling_status['resource_utilization']['avg_memory_usage'],
                    scaling_status['resource_utilization']['total_active_tasks'],
                    float(scaling_status['scaling_in_progress'])
                ]
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Feature extraction failed for {model_type}: {e}")
            return None
    
    async def _process_prediction(self, prediction_result: PredictionResult):
        """🔄 Process prediction and take actions"""
        try:
            model_type = None
            for model in self.models.values():
                if model.model_id == prediction_result.model_id:
                    model_type = model.model_type
                    break
            
            if not model_type:
                return
            
            # Process based on model type
            if model_type == ModelType.PERFORMANCE_PREDICTOR:
                await self._process_performance_prediction(prediction_result)
            elif model_type == ModelType.ANOMALY_DETECTOR:
                await self._process_anomaly_prediction(prediction_result)
            elif model_type == ModelType.LOAD_FORECASTER:
                await self._process_load_prediction(prediction_result)
            elif model_type == ModelType.FAILURE_PREDICTOR:
                await self._process_failure_prediction(prediction_result)
            
        except Exception as e:
            logger.error(f"❌ Prediction processing failed: {e}")
    
    async def _process_performance_prediction(self, prediction: PredictionResult):
        """📈 Process performance prediction"""
        predicted_throughput = prediction.prediction
        
        if prediction.confidence > 0.8 and predicted_throughput < 10.0:  # Low predicted performance
            logger.warning(f"⚠️ Low performance predicted: {predicted_throughput:.2f}")
            
            # Send optimization recommendation
            await self.message_bus.broadcast(
                event_name="performance_alert",
                payload={
                    'type': 'low_performance_predicted',
                    'predicted_throughput': predicted_throughput,
                    'confidence': prediction.confidence,
                    'recommendation': 'consider_scaling_up'
                }
            )
    
    async def _process_anomaly_prediction(self, prediction: PredictionResult):
        """🚨 Process anomaly detection"""
        # In isolation forest, -1 indicates anomaly, 1 indicates normal
        if prediction.prediction == -1 and prediction.confidence > 0.7:
            logger.warning("🚨 System anomaly detected!")
            
            await self.message_bus.broadcast(
                event_name="anomaly_alert",
                payload={
                    'type': 'system_anomaly',
                    'confidence': prediction.confidence,
                    'timestamp': prediction.timestamp.isoformat(),
                    'recommendation': 'investigate_system_health'
                }
            )
    
    async def _process_load_prediction(self, prediction: PredictionResult):
        """📊 Process load forecasting"""
        # Process load predictions for capacity planning
        pass
    
    async def _process_failure_prediction(self, prediction: PredictionResult):
        """💥 Process failure prediction"""
        # Process failure predictions for preventive maintenance
        pass
    
    async def _model_monitoring_loop(self):
        """👁️ Monitor model performance and health"""
        while True:
            try:
                for model_id, model in self.models.items():
                    await self._monitor_model_health(model)
                
                await asyncio.sleep(300)  # Monitor every 5 minutes
                
            except Exception as e:
                logger.error(f"❌ Model monitoring error: {e}")
                await asyncio.sleep(60)
    
    async def _monitor_model_health(self, model: MLModel):
        """💚 Monitor individual model health"""
        # Check model performance trends
        # Check prediction quality
        # Alert if model needs attention
        pass
    
    async def get_ml_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive ML analytics status"""
        model_statuses = {}
        
        for model_id, model in self.models.items():
            latest_prediction = None
            if model_id in self.prediction_cache and 'latest' in self.prediction_cache[model_id]:
                pred = self.prediction_cache[model_id]['latest']
                latest_prediction = {
                    'prediction': pred.prediction,
                    'confidence': pred.confidence,
                    'timestamp': pred.timestamp.isoformat()
                }
            
            model_statuses[model_id] = {
                'model_type': model.model_type.value,
                'training_status': model.training_status.value,
                'accuracy': model.accuracy,
                'last_trained': model.last_trained.isoformat() if model.last_trained else None,
                'training_data_size': model.training_data_size,
                'latest_prediction': latest_prediction
            }
        
        # Training data summary
        training_data_summary = {}
        for model_type, data in self.training_data.items():
            training_data_summary[model_type.value] = {
                'sample_count': len(data),
                'last_sample': data[-1]['timestamp'].isoformat() if data else None
            }
        
        return {
            'models': model_statuses,
            'training_data': training_data_summary,
            'prediction_cache_size': sum(len(cache) for cache in self.prediction_cache.values()),
            'ml_analytics_status': 'active',
            'models_trained': sum(1 for m in self.models.values() if m.training_status == TrainingStatus.TRAINED),
            'models_training': sum(1 for m in self.models.values() if m.training_status == TrainingStatus.TRAINING)
        }
    
    async def get_predictions(self, model_type: Optional[ModelType] = None) -> Dict[str, PredictionResult]:
        """🔮 Get latest predictions"""
        predictions = {}
        
        for model_id, model in self.models.items():
            if model_type is None or model.model_type == model_type:
                if model_id in self.prediction_cache and 'latest' in self.prediction_cache[model_id]:
                    predictions[model_id] = self.prediction_cache[model_id]['latest']
        
        return predictions
    
    async def force_model_retrain(self, model_id: str) -> bool:
        """🔄 Force retrain specific model"""
        if model_id not in self.models:
            return False
        
        model = self.models[model_id]
        await self._train_model(model)
        
        return model.training_status == TrainingStatus.TRAINED