#!/usr/bin/env python3
"""
🔥💀 PHASE 2: INTELLIGENT WORKFLOW ORCHESTRATOR 💀🔥
Complex multi-agent workflow orchestration with dynamic adaptation
"""

import asyncio
import logging
import time
import json
from typing import Dict, List, Set, Any, Optional, Callable, Union
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
import networkx as nx

logger = logging.getLogger(__name__)

class WorkflowStatus(Enum):
    """📊 Workflow execution status"""
    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TaskStatus(Enum):
    """📋 Individual task status"""
    WAITING = "waiting"
    READY = "ready"
    ASSIGNED = "assigned"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

class TaskType(Enum):
    """🔧 Task execution types"""
    SEQUENTIAL = "sequential"      # Must execute in order
    PARALLEL = "parallel"         # Can execute simultaneously
    CONDITIONAL = "conditional"    # Execute based on conditions
    LOOP = "loop"                 # Repeat until condition met
    BRANCH = "branch"             # Split into multiple paths
    MERGE = "merge"               # Combine multiple paths

@dataclass
class WorkflowTask:
    """📋 Individual workflow task definition"""
    task_id: str
    task_type: TaskType
    agent_requirements: Set[str] = field(default_factory=set)
    dependencies: Set[str] = field(default_factory=set)
    
    # Execution parameters
    payload: Dict[str, Any] = field(default_factory=dict)
    timeout_seconds: int = 300
    retry_count: int = 3
    priority: int = 1
    
    # Conditional execution
    condition: Optional[str] = None
    condition_params: Dict[str, Any] = field(default_factory=dict)
    
    # Loop parameters
    loop_condition: Optional[str] = None
    max_iterations: int = 10
    
    # Status tracking
    status: TaskStatus = TaskStatus.WAITING
    assigned_agent: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    result: Dict[str, Any] = field(default_factory=dict)
    error_message: Optional[str] = None
    attempts: int = 0

@dataclass
class WorkflowDefinition:
    """📈 Complete workflow definition"""
    workflow_id: str
    name: str
    description: str
    tasks: Dict[str, WorkflowTask]
    
    # Workflow metadata
    created_at: datetime = field(default_factory=datetime.now)
    version: str = "1.0"
    tags: Set[str] = field(default_factory=set)
    
    # Execution settings
    parallel_limit: int = 5
    global_timeout: int = 3600
    failure_strategy: str = "stop"  # stop, continue, retry
    
    # Success criteria
    success_conditions: List[str] = field(default_factory=list)
    completion_threshold: float = 1.0  # % of tasks that must complete

class IntelligentWorkflowOrchestrator:
    """
    🧠 INTELLIGENT WORKFLOW ORCHESTRATOR
    
    Manages complex multi-agent workflows with:
    - Dynamic task scheduling and optimization
    - Parallel execution with dependency management
    - Adaptive resource allocation
    - Real-time workflow modification
    - Failure recovery and retry logic
    - Performance optimization and learning
    """
    
    def __init__(self, message_bus, swarm_coordinator):
        self.message_bus = message_bus
        self.swarm_coordinator = swarm_coordinator
        
        # Workflow state
        self.active_workflows: Dict[str, WorkflowDefinition] = {}
        self.workflow_history: List[Dict[str, Any]] = []
        self.workflow_templates: Dict[str, WorkflowDefinition] = {}
        
        # Execution engine
        self.task_scheduler = TaskScheduler(self)
        self.dependency_resolver = DependencyResolver()
        self.condition_evaluator = ConditionEvaluator()
        
        # Performance optimization
        self.execution_stats: Dict[str, Dict[str, float]] = {}
        self.agent_performance: Dict[str, Dict[str, float]] = {}
        self.optimization_rules: List[Callable] = []
        
        # Real-time monitoring
        self.workflow_monitors: Dict[str, asyncio.Task] = {}
        
        logger.info("🧠 IntelligentWorkflowOrchestrator initialized")
    
    async def create_workflow(self, workflow_def: WorkflowDefinition) -> str:
        """📝 Create and validate new workflow"""
        workflow_id = workflow_def.workflow_id
        
        # Validate workflow definition
        validation_result = await self._validate_workflow(workflow_def)
        if not validation_result['valid']:
            raise ValueError(f"Invalid workflow: {validation_result['errors']}")
        
        # Build dependency graph
        dependency_graph = self.dependency_resolver.build_graph(workflow_def.tasks)
        if not nx.is_directed_acyclic_graph(dependency_graph):
            raise ValueError("Workflow contains circular dependencies")
        
        # Optimize workflow for performance
        optimized_workflow = await self._optimize_workflow(workflow_def)
        
        # Store workflow
        self.active_workflows[workflow_id] = optimized_workflow
        
        logger.info(f"📝 Workflow {workflow_id} created with {len(optimized_workflow.tasks)} tasks")
        
        return workflow_id
    
    async def execute_workflow(self, workflow_id: str, 
                             execution_params: Dict[str, Any] = None) -> str:
        """🚀 Execute workflow with intelligent orchestration"""
        if workflow_id not in self.active_workflows:
            raise ValueError(f"Workflow {workflow_id} not found")
        
        workflow = self.active_workflows[workflow_id]
        execution_params = execution_params or {}
        
        # Create execution context
        execution_id = f"{workflow_id}_{int(time.time())}"
        execution_context = {
            'execution_id': execution_id,
            'workflow_id': workflow_id,
            'started_at': datetime.now(),
            'params': execution_params,
            'status': WorkflowStatus.RUNNING,
            'completed_tasks': 0,
            'total_tasks': len(workflow.tasks),
            'agent_assignments': {},
            'task_results': {}
        }
        
        # Start workflow monitor
        monitor_task = asyncio.create_task(
            self._monitor_workflow_execution(execution_context)
        )
        self.workflow_monitors[execution_id] = monitor_task
        
        # Initialize task scheduler
        await self.task_scheduler.initialize_execution(workflow, execution_context)
        
        # Start execution engine
        execution_task = asyncio.create_task(
            self._execute_workflow_engine(workflow, execution_context)
        )
        
        logger.info(f"🚀 Workflow {workflow_id} execution started: {execution_id}")
        
        return execution_id
    
    async def _execute_workflow_engine(self, workflow: WorkflowDefinition, 
                                     execution_context: Dict[str, Any]):
        """⚙️ Core workflow execution engine"""
        try:
            while execution_context['status'] == WorkflowStatus.RUNNING:
                # Get ready tasks
                ready_tasks = await self.task_scheduler.get_ready_tasks(
                    workflow, execution_context
                )
                
                if not ready_tasks:
                    # Check if workflow is complete
                    if await self._check_workflow_completion(workflow, execution_context):
                        execution_context['status'] = WorkflowStatus.COMPLETED
                        break
                    
                    # Wait for running tasks to complete
                    await asyncio.sleep(1)
                    continue
                
                # Schedule tasks for execution
                scheduling_tasks = []
                for task in ready_tasks:
                    scheduling_tasks.append(
                        self._schedule_task_execution(task, workflow, execution_context)
                    )
                
                # Execute task scheduling in parallel
                await asyncio.gather(*scheduling_tasks, return_exceptions=True)
                
                # Brief pause to prevent busy waiting
                await asyncio.sleep(0.1)
            
            # Finalize workflow execution
            await self._finalize_workflow_execution(workflow, execution_context)
            
        except Exception as e:
            logger.error(f"❌ Workflow execution engine failed: {e}")
            execution_context['status'] = WorkflowStatus.FAILED
            execution_context['error'] = str(e)
            
        finally:
            # Cleanup
            execution_id = execution_context['execution_id']
            if execution_id in self.workflow_monitors:
                self.workflow_monitors[execution_id].cancel()
                del self.workflow_monitors[execution_id]
    
    async def _schedule_task_execution(self, task: WorkflowTask, 
                                     workflow: WorkflowDefinition,
                                     execution_context: Dict[str, Any]):
        """📋 Schedule individual task for execution"""
        try:
            # Find optimal agent for task
            optimal_agent = await self._find_optimal_agent(task, execution_context)
            
            if not optimal_agent:
                logger.warning(f"⚠️ No suitable agent found for task {task.task_id}")
                task.status = TaskStatus.FAILED
                task.error_message = "No suitable agent available"
                return
            
            # Assign task to agent
            task.assigned_agent = optimal_agent
            task.status = TaskStatus.ASSIGNED
            task.started_at = datetime.now()
            task.attempts += 1
            
            execution_context['agent_assignments'][task.task_id] = optimal_agent
            
            # Prepare task payload
            task_payload = {
                'workflow_id': workflow.workflow_id,
                'execution_id': execution_context['execution_id'],
                'task_id': task.task_id,
                'task_type': task.task_type.value,
                'payload': task.payload,
                'timeout': task.timeout_seconds,
                'dependencies_results': await self._get_dependency_results(
                    task, execution_context
                )
            }
            
            # Send task to agent
            await self.message_bus.publish_to_agent(
                target_agent=optimal_agent,
                event_name="workflow_task",
                payload=task_payload
            )
            
            task.status = TaskStatus.RUNNING
            
            logger.info(f"📋 Task {task.task_id} assigned to {optimal_agent}")
            
        except Exception as e:
            logger.error(f"❌ Task scheduling failed for {task.task_id}: {e}")
            task.status = TaskStatus.FAILED
            task.error_message = str(e)
    
    async def _find_optimal_agent(self, task: WorkflowTask, 
                                execution_context: Dict[str, Any]) -> Optional[str]:
        """🎯 Find optimal agent for task execution"""
        # Get available agents from swarm
        swarm_status = await self.swarm_coordinator.get_swarm_status()
        available_agents = []
        
        for agent_id, agent_info in swarm_status.get('agents', {}).items():
            # Check agent requirements
            if task.agent_requirements:
                agent_capabilities = set(agent_info.get('capabilities', []))
                if not task.agent_requirements.issubset(agent_capabilities):
                    continue
            
            # Check agent availability
            if agent_info.get('status') == 'busy':
                continue
            
            available_agents.append(agent_id)
        
        if not available_agents:
            return None
        
        # Select optimal agent based on performance history
        best_agent = None
        best_score = -1
        
        for agent_id in available_agents:
            score = await self._calculate_agent_score(agent_id, task.task_type.value)
            if score > best_score:
                best_score = score
                best_agent = agent_id
        
        return best_agent
    
    async def _calculate_agent_score(self, agent_id: str, task_type: str) -> float:
        """📊 Calculate agent performance score for task type"""
        agent_stats = self.agent_performance.get(agent_id, {})
        task_stats = agent_stats.get(task_type, {})
        
        # Default scores for new agents
        success_rate = task_stats.get('success_rate', 0.8)
        avg_duration = task_stats.get('avg_duration', 60.0)
        reliability = task_stats.get('reliability', 0.9)
        
        # Calculate composite score
        duration_score = max(0, 1.0 - (avg_duration / 300.0))  # Penalize slow agents
        composite_score = (0.5 * success_rate + 
                          0.3 * duration_score + 
                          0.2 * reliability)
        
        return composite_score
    
    async def _get_dependency_results(self, task: WorkflowTask, 
                                    execution_context: Dict[str, Any]) -> Dict[str, Any]:
        """🔗 Get results from task dependencies"""
        dependency_results = {}
        
        for dep_task_id in task.dependencies:
            if dep_task_id in execution_context['task_results']:
                dependency_results[dep_task_id] = execution_context['task_results'][dep_task_id]
        
        return dependency_results
    
    async def handle_task_completion(self, task_id: str, workflow_id: str,
                                   execution_id: str, result: Dict[str, Any],
                                   success: bool = True):
        """✅ Handle task completion notification"""
        if workflow_id not in self.active_workflows:
            logger.warning(f"⚠️ Task completion for unknown workflow: {workflow_id}")
            return
        
        workflow = self.active_workflows[workflow_id]
        
        if task_id not in workflow.tasks:
            logger.warning(f"⚠️ Task completion for unknown task: {task_id}")
            return
        
        task = workflow.tasks[task_id]
        
        if success:
            task.status = TaskStatus.COMPLETED
            task.result = result
            task.completed_at = datetime.now()
            
            # Store result for dependent tasks
            execution_context = self._get_execution_context(execution_id)
            if execution_context:
                execution_context['task_results'][task_id] = result
                execution_context['completed_tasks'] += 1
            
            # Update agent performance stats
            await self._update_agent_performance(task)
            
            logger.info(f"✅ Task {task_id} completed successfully")
            
        else:
            # Handle task failure
            await self._handle_task_failure(task, result.get('error', 'Unknown error'))
    
    async def _handle_task_failure(self, task: WorkflowTask, error_message: str):
        """❌ Handle task failure with retry logic"""
        task.error_message = error_message
        
        if task.attempts < task.retry_count:
            # Retry task
            task.status = TaskStatus.READY
            task.assigned_agent = None
            logger.warning(f"🔄 Retrying task {task.task_id} (attempt {task.attempts + 1})")
        else:
            # Mark as failed
            task.status = TaskStatus.FAILED
            logger.error(f"❌ Task {task.task_id} failed permanently: {error_message}")
    
    async def _update_agent_performance(self, task: WorkflowTask):
        """📊 Update agent performance statistics"""
        if not task.assigned_agent or not task.started_at or not task.completed_at:
            return
        
        agent_id = task.assigned_agent
        task_type = task.task_type.value
        duration = (task.completed_at - task.started_at).total_seconds()
        
        # Initialize stats if needed
        if agent_id not in self.agent_performance:
            self.agent_performance[agent_id] = {}
        
        if task_type not in self.agent_performance[agent_id]:
            self.agent_performance[agent_id][task_type] = {
                'success_rate': 0.8,
                'avg_duration': 60.0,
                'reliability': 0.9,
                'total_tasks': 0,
                'successful_tasks': 0
            }
        
        stats = self.agent_performance[agent_id][task_type]
        
        # Update statistics
        stats['total_tasks'] += 1
        if task.status == TaskStatus.COMPLETED:
            stats['successful_tasks'] += 1
        
        stats['success_rate'] = stats['successful_tasks'] / stats['total_tasks']
        
        # Exponential moving average for duration
        alpha = 0.2
        stats['avg_duration'] = (alpha * duration + 
                               (1 - alpha) * stats['avg_duration'])
        
        # Update reliability based on recent performance
        recent_success_rate = min(1.0, stats['success_rate'] + 0.1)
        stats['reliability'] = recent_success_rate
    
    def _get_execution_context(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """📋 Get execution context by ID"""
        # This would typically be stored in a database or memory store
        # For now, implement as a simple lookup
        # In production, this should be properly implemented
        return None
    
    async def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """📊 Get detailed workflow status"""
        if workflow_id not in self.active_workflows:
            return {'error': 'Workflow not found'}
        
        workflow = self.active_workflows[workflow_id]
        
        # Task status summary
        task_status_counts = {}
        for status in TaskStatus:
            task_status_counts[status.value] = sum(
                1 for task in workflow.tasks.values()
                if task.status == status
            )
        
        # Calculate progress
        total_tasks = len(workflow.tasks)
        completed_tasks = task_status_counts.get('completed', 0)
        progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        
        return {
            'workflow_id': workflow_id,
            'name': workflow.name,
            'description': workflow.description,
            'total_tasks': total_tasks,
            'task_status': task_status_counts,
            'progress_percent': progress,
            'created_at': workflow.created_at.isoformat(),
            'version': workflow.version,
            'tags': list(workflow.tags)
        }
    
    async def _validate_workflow(self, workflow_def: WorkflowDefinition) -> Dict[str, Any]:
        """✅ Validate workflow definition"""
        errors = []
        warnings = []
        
        # Check for empty tasks
        if not workflow_def.tasks:
            errors.append("Workflow has no tasks defined")
        
        # Validate task dependencies
        task_ids = set(workflow_def.tasks.keys())
        for task_id, task in workflow_def.tasks.items():
            for dep_id in task.dependencies:
                if dep_id not in task_ids:
                    errors.append(f"Task {task_id} depends on non-existent task {dep_id}")
        
        # Check for circular dependencies using DFS
        visited = set()
        rec_stack = set()
        
        def has_cycle(task_id: str) -> bool:
            if task_id in rec_stack:
                return True
            if task_id in visited:
                return False
            
            visited.add(task_id)
            rec_stack.add(task_id)
            
            for dep_id in workflow_def.tasks[task_id].dependencies:
                if dep_id in workflow_def.tasks and has_cycle(dep_id):
                    return True
            
            rec_stack.remove(task_id)
            return False
        
        for task_id in workflow_def.tasks.keys():
            if task_id not in visited and has_cycle(task_id):
                errors.append(f"Circular dependency detected involving task {task_id}")
                break
        
        # Validate parallel limits
        if workflow_def.parallel_limit <= 0:
            errors.append("Parallel limit must be greater than 0")
        elif workflow_def.parallel_limit > 50:
            warnings.append("Parallel limit is very high (>50), consider reducing for stability")
        
        # Validate task timeouts
        for task_id, task in workflow_def.tasks.items():
            if task.timeout_seconds <= 0:
                warnings.append(f"Task {task_id} has invalid timeout ({task.timeout_seconds}s)")
            elif task.timeout_seconds > 3600:  # 1 hour
                warnings.append(f"Task {task_id} has very long timeout ({task.timeout_seconds}s)")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    async def _optimize_workflow(self, workflow_def: WorkflowDefinition) -> WorkflowDefinition:
        """⚡ Optimize workflow for performance"""
        try:
            # Create optimized copy
            optimized_workflow = WorkflowDefinition(
                workflow_id=workflow_def.workflow_id,
                name=workflow_def.name,
                description=workflow_def.description,
                tasks=workflow_def.tasks.copy(),
                created_at=workflow_def.created_at,
                version=workflow_def.version,
                tags=workflow_def.tags.copy(),
                parallel_limit=workflow_def.parallel_limit,
                global_timeout=workflow_def.global_timeout,
                failure_strategy=workflow_def.failure_strategy,
                success_conditions=workflow_def.success_conditions.copy(),
                completion_threshold=workflow_def.completion_threshold
            )
            
            # Optimization 1: Adjust parallel limits based on task count
            task_count = len(optimized_workflow.tasks)
            if task_count < 5 and optimized_workflow.parallel_limit > task_count:
                optimized_workflow.parallel_limit = task_count
                logger.info(f"🔧 Optimized parallel limit: {optimized_workflow.parallel_limit}")
            
            # Optimization 2: Optimize task priorities based on dependencies
            dependency_counts = {}
            for task_id, task in optimized_workflow.tasks.items():
                dependency_counts[task_id] = len(task.dependencies)
            
            # Tasks with fewer dependencies get higher priority
            for task_id, task in optimized_workflow.tasks.items():
                dep_count = dependency_counts[task_id]
                if dep_count == 0:
                    task.priority = min(task.priority + 2, 5)  # Higher priority for independent tasks
                elif dep_count > 3:
                    task.priority = max(task.priority - 1, 1)  # Lower priority for highly dependent tasks
            
            # Optimization 3: Set reasonable timeout defaults
            for task_id, task in optimized_workflow.tasks.items():
                if task.timeout_seconds <= 0:
                    task.timeout_seconds = 300  # 5 minute default
                
                # Adjust timeout based on task type
                if task.task_type == TaskType.PARALLEL:
                    task.timeout_seconds = min(task.timeout_seconds, 600)  # Max 10 minutes for parallel
                elif task.task_type == TaskType.SEQUENTIAL:
                    task.timeout_seconds = min(task.timeout_seconds, 1800)  # Max 30 minutes for sequential
            
            logger.info(f"⚡ Workflow optimized: {task_count} tasks, {optimized_workflow.parallel_limit} parallel limit")
            
            return optimized_workflow
            
        except Exception as e:
            logger.error(f"❌ Workflow optimization failed: {e}")
            return workflow_def  # Return original if optimization fails

class TaskScheduler:
    """📅 Intelligent task scheduler"""
    
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.dependency_resolver = DependencyResolver()
    
    async def initialize_execution(self, workflow: WorkflowDefinition,
                                 execution_context: Dict[str, Any]):
        """🚀 Initialize workflow execution"""
        # Mark tasks with no dependencies as ready
        for task in workflow.tasks.values():
            if not task.dependencies:
                task.status = TaskStatus.READY
    
    async def get_ready_tasks(self, workflow: WorkflowDefinition,
                            execution_context: Dict[str, Any]) -> List[WorkflowTask]:
        """📋 Get tasks ready for execution"""
        ready_tasks = []
        
        for task in workflow.tasks.values():
            if task.status == TaskStatus.WAITING:
                # Check if dependencies are completed
                if await self._dependencies_completed(task, workflow):
                    task.status = TaskStatus.READY
            
            if task.status == TaskStatus.READY:
                ready_tasks.append(task)
        
        # Limit parallel execution
        max_parallel = workflow.parallel_limit
        running_tasks = sum(1 for t in workflow.tasks.values() 
                          if t.status in [TaskStatus.ASSIGNED, TaskStatus.RUNNING])
        
        available_slots = max_parallel - running_tasks
        return ready_tasks[:available_slots]
    
    async def _dependencies_completed(self, task: WorkflowTask,
                                    workflow: WorkflowDefinition) -> bool:
        """🔗 Check if task dependencies are completed"""
        for dep_id in task.dependencies:
            if dep_id in workflow.tasks:
                dep_task = workflow.tasks[dep_id]
                if dep_task.status != TaskStatus.COMPLETED:
                    return False
        return True

class DependencyResolver:
    """🔗 Workflow dependency resolution"""
    
    def build_graph(self, tasks: Dict[str, WorkflowTask]) -> nx.DiGraph:
        """📈 Build dependency graph"""
        graph = nx.DiGraph()
        
        # Add all tasks as nodes
        for task_id in tasks.keys():
            graph.add_node(task_id)
        
        # Add dependency edges
        for task_id, task in tasks.items():
            for dep_id in task.dependencies:
                if dep_id in tasks:
                    graph.add_edge(dep_id, task_id)
        
        return graph

class ConditionEvaluator:
    """⚖️ Task condition evaluation"""
    
    def evaluate(self, condition: str, context: Dict[str, Any]) -> bool:
        """⚖️ Evaluate conditional expression"""
        try:
            # Simple condition evaluation
            # In production, use a proper expression evaluator
            return eval(condition, {"__builtins__": {}}, context)
        except Exception as e:
            logger.error(f"❌ Condition evaluation failed: {e}")
            return False