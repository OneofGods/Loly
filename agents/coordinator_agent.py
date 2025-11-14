#!/usr/bin/env python3
"""
🔥💀 COORDINATOR AGENT - AUTONOMOUS TASK ORCHESTRATION 💀🔥
Agent Poly Loly Double Zero: Specialized Coordination Intelligence

AUTONOMOUS BEHAVIORS:
- Independent task decomposition and assignment
- Adaptive load balancing across agents
- Real-time workflow optimization
- Proactive bottleneck detection and resolution
- Self-organizing agent coordination
"""

import asyncio
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Set
import logging
from collections import defaultdict, deque
from enum import Enum
import uuid
import heapq

from core.autonomous_agent import AutonomousAgent, AGENT_REGISTRY

logger = logging.getLogger(__name__)

class TaskPriority(Enum):
    """📋 Task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    URGENT = 5

class TaskStatus(Enum):
    """📊 Task status tracking"""
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class WorkflowTask:
    """📋 Individual workflow task"""
    def __init__(self, task_id: str, task_type: str, priority: TaskPriority, 
                 data: Dict[str, Any], dependencies: List[str] = None):
        self.task_id = task_id
        self.task_type = task_type
        self.priority = priority
        self.data = data
        self.dependencies = dependencies or []
        
        # Status tracking
        self.status = TaskStatus.PENDING
        self.assigned_agent = None
        self.created_time = datetime.now()
        self.assigned_time = None
        self.started_time = None
        self.completed_time = None
        
        # Results and metrics
        self.result = None
        self.error = None
        self.execution_time = 0.0
        self.retry_count = 0
        self.max_retries = 3
        
        # Workflow context
        self.workflow_id = None
        self.parent_task_id = None
        self.child_task_ids = []

class Workflow:
    """🔄 Complete workflow orchestration"""
    def __init__(self, workflow_id: str, workflow_type: str, description: str):
        self.workflow_id = workflow_id
        self.workflow_type = workflow_type
        self.description = description
        
        # Task management
        self.tasks = {}  # task_id -> WorkflowTask
        self.task_dependencies = {}  # task_id -> set of dependency task_ids
        self.ready_tasks = set()  # tasks ready for execution
        self.completed_tasks = set()
        self.failed_tasks = set()
        
        # Workflow state
        self.status = TaskStatus.PENDING
        self.created_time = datetime.now()
        self.started_time = None
        self.completed_time = None
        
        # Metrics
        self.total_tasks = 0
        self.completed_count = 0
        self.failed_count = 0
        self.success_rate = 0.0

class CoordinatorAgent(AutonomousAgent):
    """
    🎯 AUTONOMOUS COORDINATION AGENT
    
    Specializes in:
    - Multi-agent task orchestration
    - Workflow management and optimization
    - Load balancing and resource allocation
    - Agent discovery and capability matching
    - Performance monitoring and optimization
    """
    
    def __init__(self, agent_id: str = None, config: Dict[str, Any] = None):
        super().__init__(agent_id, config)
        
        # Agent registry and capabilities
        self.discovered_agents = {}  # agent_id -> agent_info
        self.agent_capabilities = defaultdict(set)  # agent_id -> set of capabilities
        self.agent_workload = defaultdict(int)  # agent_id -> current task count
        self.agent_performance = defaultdict(dict)  # agent_id -> performance_metrics
        
        # Task and workflow management
        self.active_workflows = {}  # workflow_id -> Workflow
        self.task_queue = []  # Priority queue of (priority, task)
        self.assigned_tasks = {}  # task_id -> agent_id
        self.task_history = deque(maxlen=1000)  # Historical task data
        
        # Orchestration state
        self.orchestration_metrics = {
            'total_workflows': 0,
            'completed_workflows': 0,
            'failed_workflows': 0,
            'total_tasks_orchestrated': 0,
            'average_task_completion_time': 0.0,
            'agent_utilization': {},
            'bottlenecks_detected': 0,
            'optimizations_applied': 0
        }
        
        # Configuration
        self.max_concurrent_workflows = 10
        self.max_agent_workload = 5
        self.agent_discovery_interval = 30  # seconds
        self.load_balancing_interval = 60  # seconds
        self.optimization_interval = 300  # 5 minutes
        
        # Coordination patterns
        self.coordination_patterns = {
            'sports_analysis': {
                'steps': ['data_collection', 'analysis', 'prediction'],
                'agent_types': ['DataCollectorAgent', 'AnalyzerAgent', 'PredictorAgent']
            },
            'prediction_pipeline': {
                'steps': ['data_prep', 'feature_extraction', 'model_training', 'prediction'],
                'agent_types': ['DataCollectorAgent', 'AnalyzerAgent', 'PredictorAgent']
            },
            'real_time_analysis': {
                'steps': ['data_stream', 'live_analysis', 'alert_generation'],
                'agent_types': ['DataCollectorAgent', 'AnalyzerAgent', 'MonitorAgent']
            }
        }
        
        logger.info(f"🎯 CoordinatorAgent {self.agent_id} initialized with {len(self.coordination_patterns)} patterns")
    
    async def _initialize_systems(self):
        """⚙️ Initialize coordination systems"""
        # Discover existing agents
        await self._discover_agents()
        
        # Start periodic coordination tasks
        asyncio.create_task(self._agent_discovery_loop())
        asyncio.create_task(self._load_balancing_loop())
        asyncio.create_task(self._optimization_loop())
        
        # Subscribe to agent lifecycle events
        await self.send_message('*', 'subscribe', {
            'agent_id': self.agent_id,
            'message_types': ['agent_spawned', 'agent_terminated', 'task_request', 'workflow_request']
        })
        
        logger.info("⚙️ Coordination systems initialized")
    
    async def _agent_behavior(self):
        """🎯 Core coordination autonomous behavior"""
        # Process task queue
        await self._process_task_queue()
        
        # Update workflow states
        await self._update_workflow_states()
        
        # Monitor agent performance
        await self._monitor_agent_performance()
        
        # Detect and resolve bottlenecks
        await self._detect_bottlenecks()
        
        # Optimize resource allocation
        await self._optimize_resource_allocation()
        
        await asyncio.sleep(0.5)
    
    async def _agent_specific_adaptation(self):
        """🧠 Adapt coordination strategies based on performance"""
        # Analyze workflow success rates
        workflow_success_rate = (
            self.orchestration_metrics['completed_workflows'] / 
            max(self.orchestration_metrics['total_workflows'], 1)
        )
        
        if workflow_success_rate < 0.8:
            # Poor workflow success - adapt coordination strategy
            self.max_agent_workload = max(self.max_agent_workload - 1, 2)
            logger.info(f"🧠 Reduced max agent workload to {self.max_agent_workload} due to poor success rate")
        
        elif workflow_success_rate > 0.95:
            # Excellent success - can increase load
            self.max_agent_workload = min(self.max_agent_workload + 1, 8)
            logger.info(f"🧠 Increased max agent workload to {self.max_agent_workload} due to excellent success rate")
        
        # Adapt based on agent performance patterns
        await self._adapt_agent_assignment_strategy()
    
    async def _handle_message(self, message):
        """📨 Handle messages from other agents"""
        await super()._handle_message(message)
        
        if message.message_type == "workflow_request":
            await self._handle_workflow_request(message)
        elif message.message_type == "task_complete":
            await self._handle_task_complete(message)
        elif message.message_type == "task_failed":
            await self._handle_task_failed(message)
        elif message.message_type == "agent_status":
            await self._handle_agent_status_update(message)
        elif message.message_type == "capability_announcement":
            await self._handle_capability_announcement(message)
    
    async def _handle_workflow_request(self, message):
        """🔄 Handle workflow creation request"""
        payload = message.payload
        workflow_type = payload.get('workflow_type')
        workflow_data = payload.get('workflow_data', {})
        requester = message.sender_id
        
        if workflow_type:
            workflow_id = await self._create_workflow(workflow_type, workflow_data, requester)
            
            await self.send_message(requester, 'workflow_created', {
                'workflow_id': workflow_id,
                'workflow_type': workflow_type,
                'coordinator': self.agent_id,
                'estimated_completion': await self._estimate_workflow_completion(workflow_id)
            })
            
            logger.info(f"🔄 Created workflow {workflow_id} ({workflow_type}) for {requester}")
    
    async def _handle_task_complete(self, message):
        """✅ Handle task completion"""
        payload = message.payload
        task_id = payload.get('task_id')
        result = payload.get('result')
        
        if task_id in self.assigned_tasks:
            await self._complete_task(task_id, result)
            
            # Update agent performance
            agent_id = self.assigned_tasks[task_id]
            await self._update_agent_performance(agent_id, 'task_completed', payload)
    
    async def _handle_task_failed(self, message):
        """❌ Handle task failure"""
        payload = message.payload
        task_id = payload.get('task_id')
        error = payload.get('error')
        
        if task_id in self.assigned_tasks:
            await self._fail_task(task_id, error)
            
            # Update agent performance
            agent_id = self.assigned_tasks[task_id]
            await self._update_agent_performance(agent_id, 'task_failed', payload)
    
    async def _create_workflow(self, workflow_type: str, workflow_data: Dict[str, Any], requester: str) -> str:
        """🔄 Create and orchestrate new workflow"""
        workflow_id = f"wf_{workflow_type}_{int(time.time())}_{uuid.uuid4().hex[:8]}"
        
        # Create workflow
        workflow = Workflow(
            workflow_id=workflow_id,
            workflow_type=workflow_type,
            description=f"{workflow_type} workflow requested by {requester}"
        )
        
        # Generate tasks based on workflow type
        tasks = await self._generate_workflow_tasks(workflow_type, workflow_data, workflow_id)
        
        # Add tasks to workflow
        for task in tasks:
            task.workflow_id = workflow_id
            workflow.tasks[task.task_id] = task
            workflow.total_tasks += 1
            
            # Build dependency graph
            if task.dependencies:
                workflow.task_dependencies[task.task_id] = set(task.dependencies)
            else:
                workflow.ready_tasks.add(task.task_id)
        
        # Store workflow
        self.active_workflows[workflow_id] = workflow
        workflow.status = TaskStatus.IN_PROGRESS
        workflow.started_time = datetime.now()
        
        # Update metrics
        self.orchestration_metrics['total_workflows'] += 1
        
        # Schedule initial tasks
        await self._schedule_ready_tasks(workflow_id)
        
        return workflow_id
    
    async def _generate_workflow_tasks(self, workflow_type: str, workflow_data: Dict[str, Any], workflow_id: str) -> List[WorkflowTask]:
        """📋 Generate tasks for workflow"""
        tasks = []
        
        if workflow_type == 'sports_analysis':
            tasks = await self._generate_sports_analysis_tasks(workflow_data, workflow_id)
        elif workflow_type == 'prediction_pipeline':
            tasks = await self._generate_prediction_pipeline_tasks(workflow_data, workflow_id)
        elif workflow_type == 'real_time_analysis':
            tasks = await self._generate_real_time_analysis_tasks(workflow_data, workflow_id)
        else:
            # Generic workflow
            tasks = await self._generate_generic_workflow_tasks(workflow_data, workflow_id)
        
        return tasks
    
    async def _generate_sports_analysis_tasks(self, workflow_data: Dict[str, Any], workflow_id: str) -> List[WorkflowTask]:
        """⚽ Generate sports analysis workflow tasks"""
        sport = workflow_data.get('sport', 'NFL')
        analysis_depth = workflow_data.get('analysis_depth', 'standard')
        
        tasks = []
        
        # Task 1: Data Collection
        data_task = WorkflowTask(
            task_id=f"{workflow_id}_data_collection",
            task_type='data_collection',
            priority=TaskPriority.HIGH,
            data={
                'sport': sport,
                'collection_type': 'recent_games',
                'max_games': 20,
                'include_live': True
            }
        )
        tasks.append(data_task)
        
        # Task 2: Analysis (depends on data collection)
        analysis_task = WorkflowTask(
            task_id=f"{workflow_id}_analysis",
            task_type='sports_analysis',
            priority=TaskPriority.HIGH,
            data={
                'sport': sport,
                'analysis_type': 'full_analysis' if analysis_depth == 'deep' else 'standard_analysis',
                'include_patterns': True,
                'include_trends': True
            },
            dependencies=[data_task.task_id]
        )
        tasks.append(analysis_task)
        
        # Task 3: Prediction (depends on analysis)
        prediction_task = WorkflowTask(
            task_id=f"{workflow_id}_prediction",
            task_type='prediction',
            priority=TaskPriority.MEDIUM,
            data={
                'sport': sport,
                'prediction_types': ['winner', 'total_score'],
                'confidence_threshold': 0.7
            },
            dependencies=[analysis_task.task_id]
        )
        tasks.append(prediction_task)
        
        return tasks
    
    async def _generate_prediction_pipeline_tasks(self, workflow_data: Dict[str, Any], workflow_id: str) -> List[WorkflowTask]:
        """🎯 Generate prediction pipeline tasks"""
        sport = workflow_data.get('sport', 'NFL')
        target_games = workflow_data.get('target_games', [])
        
        tasks = []
        
        # Task 1: Data Preparation
        prep_task = WorkflowTask(
            task_id=f"{workflow_id}_data_prep",
            task_type='data_preparation',
            priority=TaskPriority.HIGH,
            data={
                'sport': sport,
                'target_games': target_games,
                'preparation_type': 'prediction_ready'
            }
        )
        tasks.append(prep_task)
        
        # Task 2: Feature Engineering
        feature_task = WorkflowTask(
            task_id=f"{workflow_id}_feature_engineering",
            task_type='feature_engineering',
            priority=TaskPriority.HIGH,
            data={
                'sport': sport,
                'feature_types': ['team_performance', 'recent_form', 'head_to_head'],
                'target_games': target_games
            },
            dependencies=[prep_task.task_id]
        )
        tasks.append(feature_task)
        
        # Task 3: Model Training/Update
        training_task = WorkflowTask(
            task_id=f"{workflow_id}_model_training",
            task_type='model_training',
            priority=TaskPriority.MEDIUM,
            data={
                'sport': sport,
                'training_type': 'incremental',
                'targets': ['winner', 'total_score']
            },
            dependencies=[feature_task.task_id]
        )
        tasks.append(training_task)
        
        # Task 4: Generate Predictions
        prediction_task = WorkflowTask(
            task_id=f"{workflow_id}_generate_predictions",
            task_type='batch_prediction',
            priority=TaskPriority.HIGH,
            data={
                'sport': sport,
                'target_games': target_games,
                'prediction_types': ['winner', 'total_score', 'spread']
            },
            dependencies=[training_task.task_id]
        )
        tasks.append(prediction_task)
        
        return tasks
    
    async def _generate_real_time_analysis_tasks(self, workflow_data: Dict[str, Any], workflow_id: str) -> List[WorkflowTask]:
        """⚡ Generate real-time analysis tasks"""
        sports = workflow_data.get('sports', ['NFL', 'NBA'])
        monitoring_duration = workflow_data.get('duration_minutes', 60)
        
        tasks = []
        
        for sport in sports:
            # Data streaming task
            stream_task = WorkflowTask(
                task_id=f"{workflow_id}_stream_{sport}",
                task_type='data_streaming',
                priority=TaskPriority.CRITICAL,
                data={
                    'sport': sport,
                    'stream_type': 'live_games',
                    'duration_minutes': monitoring_duration,
                    'update_frequency': 30
                }
            )
            tasks.append(stream_task)
            
            # Live analysis task
            analysis_task = WorkflowTask(
                task_id=f"{workflow_id}_live_analysis_{sport}",
                task_type='live_analysis',
                priority=TaskPriority.HIGH,
                data={
                    'sport': sport,
                    'analysis_type': 'real_time',
                    'alert_thresholds': {'anomaly': 0.8, 'trend_change': 0.7}
                },
                dependencies=[stream_task.task_id]
            )
            tasks.append(analysis_task)
        
        return tasks
    
    async def _generate_generic_workflow_tasks(self, workflow_data: Dict[str, Any], workflow_id: str) -> List[WorkflowTask]:
        """📋 Generate generic workflow tasks"""
        task_specs = workflow_data.get('tasks', [])
        tasks = []
        
        for i, task_spec in enumerate(task_specs):
            task = WorkflowTask(
                task_id=f"{workflow_id}_task_{i}",
                task_type=task_spec.get('type', 'generic'),
                priority=TaskPriority(task_spec.get('priority', 2)),
                data=task_spec.get('data', {}),
                dependencies=task_spec.get('dependencies', [])
            )
            tasks.append(task)
        
        return tasks
    
    async def _process_tasks(self):
        """📋 Override base class task processing for coordinator-specific logic"""
        await self._process_task_queue()
        
    async def _process_task_queue(self):
        """📋 Process the task assignment queue"""
        while self.task_queue and len(self.assigned_tasks) < self.max_concurrent_workflows * 10:
            # Get highest priority task
            priority, task_data = heapq.heappop(self.task_queue)
            task_id = task_data['task_id']
            
            # Find best agent for task
            best_agent = await self._find_best_agent_for_task(task_data)
            
            if best_agent:
                await self._assign_task_to_agent(task_id, best_agent, task_data)
            else:
                # No suitable agent available - requeue with lower priority
                heapq.heappush(self.task_queue, (priority + 1, task_data))
                break  # Stop processing until agents become available
    
    async def _find_best_agent_for_task(self, task_data: Dict[str, Any]) -> Optional[str]:
        """🎯 Find best agent for specific task"""
        task_type = task_data.get('task_type')
        required_capabilities = self._get_required_capabilities(task_type)
        
        # Find agents with required capabilities
        candidate_agents = []
        for agent_id, capabilities in self.agent_capabilities.items():
            if required_capabilities.issubset(capabilities):
                # Check agent workload
                current_workload = self.agent_workload[agent_id]
                if current_workload < self.max_agent_workload:
                    # Calculate agent score
                    performance = self.agent_performance.get(agent_id, {})
                    success_rate = performance.get('success_rate', 0.5)
                    avg_completion_time = performance.get('avg_completion_time', 60.0)
                    
                    # Score based on success rate, low workload, and fast completion
                    score = (success_rate * 0.5 + 
                           (1 - current_workload / self.max_agent_workload) * 0.3 +
                           (1 / max(avg_completion_time, 1.0)) * 0.2)
                    
                    candidate_agents.append((agent_id, score))
        
        if candidate_agents:
            # Select agent with highest score
            candidate_agents.sort(key=lambda x: x[1], reverse=True)
            return candidate_agents[0][0]
        
        return None
    
    def _get_required_capabilities(self, task_type: str) -> Set[str]:
        """🔍 Get required capabilities for task type"""
        capability_map = {
            'data_collection': {'data_collection', 'api_access'},
            'sports_analysis': {'analysis', 'pattern_recognition'},
            'prediction': {'machine_learning', 'prediction'},
            'data_preparation': {'data_processing', 'feature_engineering'},
            'feature_engineering': {'feature_engineering', 'statistics'},
            'model_training': {'machine_learning', 'model_training'},
            'batch_prediction': {'prediction', 'batch_processing'},
            'data_streaming': {'data_collection', 'real_time_processing'},
            'live_analysis': {'analysis', 'real_time_processing'},
            'monitoring': {'monitoring', 'health_checks'}
        }
        
        return capability_map.get(task_type, {'general'})
    
    async def _assign_task_to_agent(self, task_id: str, agent_id: str, task_data: Dict[str, Any]):
        """📤 Assign task to specific agent"""
        # Update tracking
        self.assigned_tasks[task_id] = agent_id
        self.agent_workload[agent_id] += 1
        
        # Send task to agent
        await self.send_message(agent_id, 'task_assignment', {
            'task_id': task_id,
            'task_type': task_data['task_type'],
            'task_data': task_data.get('data', {}),
            'priority': task_data.get('priority', 2),
            'coordinator': self.agent_id,
            'deadline': task_data.get('deadline')
        })
        
        # Update task status in workflow
        workflow_id = task_data.get('workflow_id')
        if workflow_id in self.active_workflows:
            workflow = self.active_workflows[workflow_id]
            if task_id in workflow.tasks:
                task = workflow.tasks[task_id]
                task.status = TaskStatus.ASSIGNED
                task.assigned_agent = agent_id
                task.assigned_time = datetime.now()
        
        # Update metrics
        self.orchestration_metrics['total_tasks_orchestrated'] += 1
        
        logger.info(f"📤 Assigned task {task_id} to agent {agent_id}")
    
    async def _complete_task(self, task_id: str, result: Any):
        """✅ Mark task as completed and handle workflow progression"""
        if task_id not in self.assigned_tasks:
            return
        
        agent_id = self.assigned_tasks[task_id]
        
        # Update agent workload
        self.agent_workload[agent_id] = max(0, self.agent_workload[agent_id] - 1)
        
        # Find and update task in workflow
        workflow_id = None
        for wf_id, workflow in self.active_workflows.items():
            if task_id in workflow.tasks:
                workflow_id = wf_id
                task = workflow.tasks[task_id]
                task.status = TaskStatus.COMPLETED
                task.completed_time = datetime.now()
                task.result = result
                
                if task.assigned_time:
                    task.execution_time = (task.completed_time - task.assigned_time).total_seconds()
                
                workflow.completed_tasks.add(task_id)
                workflow.completed_count += 1
                
                break
        
        # Remove from assigned tasks
        del self.assigned_tasks[task_id]
        
        # Check for newly ready tasks
        if workflow_id:
            await self._update_ready_tasks(workflow_id, task_id)
            await self._check_workflow_completion(workflow_id)
        
        # Add to history
        self.task_history.append({
            'task_id': task_id,
            'agent_id': agent_id,
            'status': 'completed',
            'completion_time': datetime.now(),
            'execution_time': getattr(task, 'execution_time', 0.0) if 'task' in locals() else 0.0
        })
        
        logger.info(f"✅ Task {task_id} completed by {agent_id}")
    
    async def _fail_task(self, task_id: str, error: str):
        """❌ Handle task failure"""
        if task_id not in self.assigned_tasks:
            return
        
        agent_id = self.assigned_tasks[task_id]
        
        # Update agent workload
        self.agent_workload[agent_id] = max(0, self.agent_workload[agent_id] - 1)
        
        # Find and update task in workflow
        workflow_id = None
        for wf_id, workflow in self.active_workflows.items():
            if task_id in workflow.tasks:
                workflow_id = wf_id
                task = workflow.tasks[task_id]
                task.status = TaskStatus.FAILED
                task.error = error
                task.retry_count += 1
                
                workflow.failed_tasks.add(task_id)
                workflow.failed_count += 1
                
                # Check if task can be retried
                if task.retry_count < task.max_retries:
                    logger.info(f"🔄 Retrying task {task_id} (attempt {task.retry_count + 1})")
                    await self._retry_task(task)
                else:
                    logger.error(f"❌ Task {task_id} failed permanently: {error}")
                
                break
        
        # Remove from assigned tasks
        del self.assigned_tasks[task_id]
        
        # Add to history
        self.task_history.append({
            'task_id': task_id,
            'agent_id': agent_id,
            'status': 'failed',
            'error': error,
            'completion_time': datetime.now()
        })
        
        # Check workflow status
        if workflow_id:
            await self._check_workflow_completion(workflow_id)
    
    async def _retry_task(self, task: WorkflowTask):
        """🔄 Retry failed task"""
        task.status = TaskStatus.PENDING
        task.assigned_agent = None
        task.assigned_time = None
        
        # Add back to queue with higher priority
        priority = max(1, task.priority.value - 1)  # Increase priority for retry
        task_data = {
            'task_id': task.task_id,
            'task_type': task.task_type,
            'data': task.data,
            'priority': priority,
            'workflow_id': task.workflow_id,
            'retry_count': task.retry_count
        }
        
        heapq.heappush(self.task_queue, (priority, task_data))
    
    async def _update_ready_tasks(self, workflow_id: str, completed_task_id: str):
        """🔄 Update ready tasks after task completion"""
        workflow = self.active_workflows[workflow_id]
        
        # Check all tasks to see if any became ready
        for task_id, task in workflow.tasks.items():
            if (task.status == TaskStatus.PENDING and 
                task_id not in workflow.ready_tasks and
                task.dependencies):
                
                # Check if all dependencies are completed
                dependencies_completed = all(
                    dep_id in workflow.completed_tasks 
                    for dep_id in task.dependencies
                )
                
                if dependencies_completed:
                    workflow.ready_tasks.add(task_id)
                    
                    # Add to task queue
                    task_data = {
                        'task_id': task_id,
                        'task_type': task.task_type,
                        'data': task.data,
                        'priority': task.priority.value,
                        'workflow_id': workflow_id
                    }
                    
                    heapq.heappush(self.task_queue, (task.priority.value, task_data))
                    
                    logger.info(f"🔄 Task {task_id} became ready in workflow {workflow_id}")
    
    async def _schedule_ready_tasks(self, workflow_id: str):
        """📅 Schedule all ready tasks in workflow"""
        workflow = self.active_workflows[workflow_id]
        
        for task_id in list(workflow.ready_tasks):
            task = workflow.tasks[task_id]
            
            task_data = {
                'task_id': task_id,
                'task_type': task.task_type,
                'data': task.data,
                'priority': task.priority.value,
                'workflow_id': workflow_id
            }
            
            heapq.heappush(self.task_queue, (task.priority.value, task_data))
        
        logger.info(f"📅 Scheduled {len(workflow.ready_tasks)} ready tasks for workflow {workflow_id}")
    
    async def _check_workflow_completion(self, workflow_id: str):
        """✅ Check if workflow is completed"""
        workflow = self.active_workflows[workflow_id]
        
        total_tasks = len(workflow.tasks)
        completed_tasks = len(workflow.completed_tasks)
        failed_tasks = len(workflow.failed_tasks)
        
        if completed_tasks + failed_tasks == total_tasks:
            # Workflow finished
            workflow.completed_time = datetime.now()
            workflow.success_rate = completed_tasks / total_tasks if total_tasks > 0 else 0.0
            
            if failed_tasks == 0:
                workflow.status = TaskStatus.COMPLETED
                self.orchestration_metrics['completed_workflows'] += 1
                logger.info(f"✅ Workflow {workflow_id} completed successfully")
            else:
                workflow.status = TaskStatus.FAILED
                self.orchestration_metrics['failed_workflows'] += 1
                logger.warning(f"❌ Workflow {workflow_id} completed with {failed_tasks} failed tasks")
            
            # Broadcast workflow completion
            await self.broadcast_message('workflow_completed', {
                'workflow_id': workflow_id,
                'status': workflow.status.value,
                'total_tasks': total_tasks,
                'completed_tasks': completed_tasks,
                'failed_tasks': failed_tasks,
                'success_rate': workflow.success_rate,
                'execution_time': (workflow.completed_time - workflow.started_time).total_seconds() if workflow.started_time else 0,
                'coordinator': self.agent_id
            })
            
            # Clean up completed workflow after delay
            asyncio.create_task(self._cleanup_workflow(workflow_id, delay=300))  # 5 minutes
    
    async def _cleanup_workflow(self, workflow_id: str, delay: int = 0):
        """🧹 Clean up completed workflow"""
        if delay > 0:
            await asyncio.sleep(delay)
        
        if workflow_id in self.active_workflows:
            del self.active_workflows[workflow_id]
            logger.info(f"🧹 Cleaned up workflow {workflow_id}")
    
    async def _update_workflow_states(self):
        """🔄 Update all active workflow states"""
        for workflow_id, workflow in list(self.active_workflows.items()):
            # Check for stuck workflows
            if workflow.started_time:
                elapsed_time = (datetime.now() - workflow.started_time).total_seconds()
                if elapsed_time > 3600:  # 1 hour timeout
                    logger.warning(f"⏰ Workflow {workflow_id} has been running for {elapsed_time:.0f}s")
            
            # Update workflow metrics
            total_tasks = len(workflow.tasks)
            if total_tasks > 0:
                workflow.success_rate = len(workflow.completed_tasks) / total_tasks
    
    async def _monitor_agent_performance(self):
        """📊 Monitor performance of all agents"""
        current_time = time.time()
        
        for agent_id in self.discovered_agents:
            # Calculate performance metrics
            agent_tasks = [
                task for task in self.task_history 
                if task.get('agent_id') == agent_id and 
                task.get('completion_time', datetime.min).timestamp() > current_time - 3600  # Last hour
            ]
            
            if agent_tasks:
                completed_tasks = [t for t in agent_tasks if t['status'] == 'completed']
                failed_tasks = [t for t in agent_tasks if t['status'] == 'failed']
                
                success_rate = len(completed_tasks) / len(agent_tasks)
                avg_completion_time = np.mean([t.get('execution_time', 60) for t in completed_tasks]) if completed_tasks else 60.0
                
                self.agent_performance[agent_id] = {
                    'success_rate': success_rate,
                    'avg_completion_time': avg_completion_time,
                    'tasks_completed': len(completed_tasks),
                    'tasks_failed': len(failed_tasks),
                    'last_updated': current_time
                }
                
                # Update orchestration metrics
                self.orchestration_metrics['agent_utilization'][agent_id] = {
                    'current_workload': self.agent_workload[agent_id],
                    'success_rate': success_rate,
                    'avg_completion_time': avg_completion_time
                }
    
    async def _detect_bottlenecks(self):
        """🔍 Detect performance bottlenecks"""
        # Check for overloaded agents
        overloaded_agents = [
            agent_id for agent_id, workload in self.agent_workload.items()
            if workload >= self.max_agent_workload
        ]
        
        if overloaded_agents:
            self.orchestration_metrics['bottlenecks_detected'] += 1
            logger.warning(f"🔍 Detected overloaded agents: {overloaded_agents}")
            
            # Attempt to rebalance load
            await self._rebalance_load(overloaded_agents)
        
        # Check for slow-performing agents
        slow_agents = [
            agent_id for agent_id, perf in self.agent_performance.items()
            if perf.get('avg_completion_time', 0) > 300  # 5 minutes
        ]
        
        if slow_agents:
            logger.warning(f"🐌 Detected slow agents: {slow_agents}")
    
    async def _rebalance_load(self, overloaded_agents: List[str]):
        """⚖️ Rebalance load across agents"""
        # This would implement intelligent load rebalancing
        # For now, just log the need for rebalancing
        logger.info(f"⚖️ Rebalancing load for agents: {overloaded_agents}")
        
        # Could implement:
        # - Task migration
        # - Priority adjustment
        # - Agent capability reassignment
        
        self.orchestration_metrics['optimizations_applied'] += 1
    
    async def _optimize_resource_allocation(self):
        """🎯 Optimize resource allocation"""
        # Analyze agent utilization patterns
        total_agents = len(self.discovered_agents)
        if total_agents == 0:
            return
        
        total_workload = sum(self.agent_workload.values())
        avg_workload = total_workload / total_agents
        
        # If average workload is low, could increase task assignment rate
        if avg_workload < self.max_agent_workload * 0.5:
            # Underutilized - could be more aggressive with task assignment
            pass
        elif avg_workload > self.max_agent_workload * 0.8:
            # High utilization - might need more conservative assignment
            pass
    
    async def _discover_agents(self):
        """🔍 Discover available agents"""
        # Broadcast discovery request
        await self.broadcast_message('agent_discovery', {
            'coordinator_id': self.agent_id,
            'request_capabilities': True
        })
        
        logger.info("🔍 Broadcasting agent discovery request")
    
    async def _agent_discovery_loop(self):
        """🔄 Periodic agent discovery"""
        while self.state != 'terminated':
            try:
                await self._discover_agents()
                await asyncio.sleep(self.agent_discovery_interval)
            except Exception as e:
                logger.error(f"❌ Agent discovery error: {e}")
                await asyncio.sleep(self.agent_discovery_interval)
    
    async def _load_balancing_loop(self):
        """⚖️ Periodic load balancing"""
        while self.state != 'terminated':
            try:
                await self._monitor_agent_performance()
                await self._detect_bottlenecks()
                await asyncio.sleep(self.load_balancing_interval)
            except Exception as e:
                logger.error(f"❌ Load balancing error: {e}")
                await asyncio.sleep(self.load_balancing_interval)
    
    async def _optimization_loop(self):
        """🎯 Periodic optimization"""
        while self.state != 'terminated':
            try:
                await self._optimize_resource_allocation()
                await self._update_orchestration_metrics()
                await asyncio.sleep(self.optimization_interval)
            except Exception as e:
                logger.error(f"❌ Optimization error: {e}")
                await asyncio.sleep(self.optimization_interval)
    
    async def _update_orchestration_metrics(self):
        """📊 Update orchestration metrics"""
        if self.task_history:
            recent_tasks = [
                t for t in self.task_history 
                if t.get('completion_time', datetime.min).timestamp() > time.time() - 3600
            ]
            
            if recent_tasks:
                completed_tasks = [t for t in recent_tasks if t['status'] == 'completed']
                if completed_tasks:
                    avg_completion = np.mean([t.get('execution_time', 60) for t in completed_tasks])
                    self.orchestration_metrics['average_task_completion_time'] = avg_completion
    
    async def _update_agent_performance(self, agent_id: str, event_type: str, event_data: Dict[str, Any]):
        """📊 Update agent performance metrics"""
        if agent_id not in self.agent_performance:
            self.agent_performance[agent_id] = {
                'success_rate': 0.5,
                'avg_completion_time': 60.0,
                'tasks_completed': 0,
                'tasks_failed': 0
            }
        
        perf = self.agent_performance[agent_id]
        
        if event_type == 'task_completed':
            perf['tasks_completed'] += 1
        elif event_type == 'task_failed':
            perf['tasks_failed'] += 1
        
        total_tasks = perf['tasks_completed'] + perf['tasks_failed']
        if total_tasks > 0:
            perf['success_rate'] = perf['tasks_completed'] / total_tasks
    
    async def _handle_capability_announcement(self, message):
        """📢 Handle agent capability announcements"""
        payload = message.payload
        agent_id = message.sender_id
        capabilities = set(payload.get('capabilities', []))
        
        self.agent_capabilities[agent_id] = capabilities
        self.discovered_agents[agent_id] = {
            'agent_id': agent_id,
            'capabilities': list(capabilities),
            'last_seen': time.time()
        }
        
        logger.info(f"📢 Updated capabilities for {agent_id}: {capabilities}")
    
    async def _handle_agent_status_update(self, message):
        """📊 Handle agent status updates"""
        payload = message.payload
        agent_id = message.sender_id
        
        # Update agent information
        if agent_id in self.discovered_agents:
            self.discovered_agents[agent_id].update({
                'status': payload.get('status'),
                'workload': payload.get('workload', 0),
                'last_seen': time.time()
            })
    
    async def _adapt_agent_assignment_strategy(self):
        """🧠 Adapt agent assignment strategy based on performance"""
        # Analyze which agents perform best for which task types
        task_type_performance = defaultdict(lambda: defaultdict(list))
        
        for task in self.task_history[-100:]:  # Last 100 tasks
            if 'agent_id' in task and 'execution_time' in task:
                agent_id = task['agent_id']
                task_type = task.get('task_type', 'unknown')
                execution_time = task['execution_time']
                
                task_type_performance[task_type][agent_id].append(execution_time)
        
        # Update assignment preferences
        for task_type, agent_performance in task_type_performance.items():
            if len(agent_performance) > 1:
                # Find the best performing agent for this task type
                best_agent = min(
                    agent_performance.items(),
                    key=lambda x: np.mean(x[1])
                )
                
                logger.info(f"🧠 Best agent for {task_type}: {best_agent[0]} (avg: {np.mean(best_agent[1]):.1f}s)")
    
    async def _estimate_workflow_completion(self, workflow_id: str) -> Optional[datetime]:
        """⏱️ Estimate workflow completion time"""
        if workflow_id not in self.active_workflows:
            return None
        
        workflow = self.active_workflows[workflow_id]
        remaining_tasks = len(workflow.tasks) - len(workflow.completed_tasks) - len(workflow.failed_tasks)
        
        if remaining_tasks == 0:
            return datetime.now()
        
        # Estimate based on average task completion time
        avg_completion_time = self.orchestration_metrics.get('average_task_completion_time', 60.0)
        estimated_seconds = remaining_tasks * avg_completion_time
        
        return datetime.now() + timedelta(seconds=estimated_seconds)
    
    # =================== PUBLIC API ===================
    
    async def get_coordination_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive coordination status"""
        return {
            'agent_id': self.agent_id,
            'timestamp': time.time(),
            'discovered_agents': len(self.discovered_agents),
            'active_workflows': len(self.active_workflows),
            'queued_tasks': len(self.task_queue),
            'assigned_tasks': len(self.assigned_tasks),
            'orchestration_metrics': self.orchestration_metrics,
            'agent_workload': dict(self.agent_workload),
            'agent_performance': dict(self.agent_performance)
        }
    
    async def create_sports_analysis_workflow(self, sport: str, analysis_depth: str = 'standard') -> str:
        """⚽ Create sports analysis workflow"""
        workflow_data = {
            'sport': sport,
            'analysis_depth': analysis_depth
        }
        
        return await self._create_workflow('sports_analysis', workflow_data, self.agent_id)
    
    async def create_prediction_pipeline(self, sport: str, target_games: List[Dict]) -> str:
        """🎯 Create prediction pipeline workflow"""
        workflow_data = {
            'sport': sport,
            'target_games': target_games
        }
        
        return await self._create_workflow('prediction_pipeline', workflow_data, self.agent_id)
    
    async def get_workflow_status(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """📊 Get status of specific workflow"""
        if workflow_id not in self.active_workflows:
            return None
        
        workflow = self.active_workflows[workflow_id]
        
        return {
            'workflow_id': workflow_id,
            'workflow_type': workflow.workflow_type,
            'status': workflow.status.value,
            'total_tasks': workflow.total_tasks,
            'completed_tasks': len(workflow.completed_tasks),
            'failed_tasks': len(workflow.failed_tasks),
            'success_rate': workflow.success_rate,
            'created_time': workflow.created_time.isoformat(),
            'started_time': workflow.started_time.isoformat() if workflow.started_time else None,
            'completed_time': workflow.completed_time.isoformat() if workflow.completed_time else None,
            'estimated_completion': (await self._estimate_workflow_completion(workflow_id)).isoformat() if await self._estimate_workflow_completion(workflow_id) else None
        }

if __name__ == "__main__":
    async def test_coordinator():
        agent = CoordinatorAgent("coordinator_001")
        AGENT_REGISTRY.register_agent(agent)
        
        await agent.spawn()
        await asyncio.sleep(2)
        
        # Create test workflow
        workflow_id = await agent.create_sports_analysis_workflow('NFL', 'deep')
        print(f"🔄 Created workflow: {workflow_id}")
        
        # Check status
        status = await agent.get_coordination_status()
        print(f"📊 Coordination Status: {json.dumps(status, indent=2, default=str)}")
        
        await asyncio.sleep(5)
        
        # Check workflow status
        workflow_status = await agent.get_workflow_status(workflow_id)
        print(f"📊 Workflow Status: {json.dumps(workflow_status, indent=2, default=str)}")
        
        await agent.terminate()
    
    asyncio.run(test_coordinator())