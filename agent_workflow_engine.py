#!/usr/bin/env python3
"""
🔥💀🔥 LOLY'S AGENT WORKFLOW ENGINE - LEGENDARY ORCHESTRATOR! 💀🔥💀

This enables Loly to orchestrate complex multi-step workflows where agents
work together to accomplish sophisticated tasks!

WORKFLOW CAPABILITIES:
- Sequential Workflows: A → B → C (one after another)
- Parallel Workflows: A + B + C (all at once)
- Conditional Workflows: if/else logic based on results
- Data Passing: Output of step 1 → Input of step 2
- Rollback: Undo previous steps if something fails
- Retry Logic: Auto-retry failed steps
- Timeouts: Don't wait forever for slow agents

EXAMPLE WORKFLOWS:
1. Research → Write → Review (content pipeline)
2. Sports Analysis + Weather + Sentiment (parallel data gathering)
3. Code Review → If bugs found → Auto-fix → Re-review (conditional)
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Union
from enum import Enum
import uuid

logger = logging.getLogger(__name__)


class WorkflowStepType(Enum):
    """🎯 Types of workflow steps"""
    SEQUENTIAL = "sequential"      # Execute one after another
    PARALLEL = "parallel"          # Execute all at once
    CONDITIONAL = "conditional"    # If/else logic
    LOOP = "loop"                 # Repeat N times or until condition


class WorkflowStepStatus(Enum):
    """📊 Status of workflow steps"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ROLLED_BACK = "rolled_back"


class WorkflowStatus(Enum):
    """🎯 Overall workflow status"""
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    ROLLED_BACK = "rolled_back"


class WorkflowStep:
    """
    📋 Individual step in a workflow
    """

    def __init__(self, step_config: Dict[str, Any]):
        self.step_id = step_config.get('step_id', str(uuid.uuid4()))
        self.name = step_config.get('name', f"step_{self.step_id[:8]}")
        self.agent_type = step_config['agent_type']  # sports, research, writer, etc.
        self.task_data = step_config.get('task_data', {})
        self.depends_on = step_config.get('depends_on', [])  # List of step_ids
        self.use_previous_output = step_config.get('use_previous_output', False)
        self.retry_count = step_config.get('retry_count', 3)
        self.timeout_seconds = step_config.get('timeout_seconds', 120)
        self.rollback_on_failure = step_config.get('rollback_on_failure', False)

        # Conditional logic
        self.condition = step_config.get('condition')  # Optional: {"field": "...", "operator": "...", "value": "..."}

        # Runtime state
        self.status = WorkflowStepStatus.PENDING
        self.result = None
        self.error = None
        self.started_at = None
        self.completed_at = None
        self.retries_attempted = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert step to dict for serialization"""
        return {
            'step_id': self.step_id,
            'name': self.name,
            'agent_type': self.agent_type,
            'status': self.status.value,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'retries_attempted': self.retries_attempted,
            'result': self.result,
            'error': self.error
        }


class AgentWorkflowEngine:
    """
    🔥💀🔥 LOLY'S WORKFLOW ENGINE - ORCHESTRATES MULTI-AGENT TASKS! 💀🔥💀

    This is what makes Loly a TRUE orchestrator, not just a coordinator!
    """

    def __init__(self, unified_coordinator):
        self.unified_coordinator = unified_coordinator
        self.engine_id = f"workflow_engine_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Active workflows
        self.active_workflows = {}  # workflow_id -> Workflow
        self.completed_workflows = {}  # workflow_id -> Workflow

        # Workflow execution stats
        self.stats = {
            'total_workflows_created': 0,
            'total_workflows_completed': 0,
            'total_workflows_failed': 0,
            'total_steps_executed': 0,
            'total_steps_failed': 0,
            'total_rollbacks': 0
        }

        logger.info(f"🔥💀🔥 Workflow Engine {self.engine_id} initialized!")

    async def execute_workflow(self, workflow_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        🚀 MAIN WORKFLOW EXECUTION METHOD

        workflow_config: {
            "workflow_name": "...",
            "workflow_type": "sequential|parallel|hybrid",
            "steps": [
                {
                    "step_id": "step1",
                    "name": "Research Phase",
                    "agent_type": "research",
                    "task_data": {...},
                    "retry_count": 3,
                    "timeout_seconds": 120
                },
                {
                    "step_id": "step2",
                    "name": "Writing Phase",
                    "agent_type": "writer",
                    "task_data": {...},
                    "depends_on": ["step1"],  # Wait for step1
                    "use_previous_output": True  # Use step1's output
                },
                ...
            ],
            "rollback_on_failure": True
        }
        """
        try:
            workflow_id = str(uuid.uuid4())
            workflow_name = workflow_config.get('workflow_name', f'workflow_{workflow_id[:8]}')
            workflow_type = workflow_config.get('workflow_type', 'sequential')

            logger.info(f"🚀 Starting workflow: {workflow_name} ({workflow_id})")

            # Create workflow
            workflow = {
                'workflow_id': workflow_id,
                'workflow_name': workflow_name,
                'workflow_type': workflow_type,
                'status': WorkflowStatus.RUNNING,
                'steps': [],
                'created_at': datetime.now(),
                'started_at': datetime.now(),
                'completed_at': None,
                'rollback_on_failure': workflow_config.get('rollback_on_failure', False)
            }

            # Create workflow steps
            steps = []
            for step_config in workflow_config.get('steps', []):
                step = WorkflowStep(step_config)
                steps.append(step)

            workflow['steps'] = steps
            self.active_workflows[workflow_id] = workflow
            self.stats['total_workflows_created'] += 1

            # Execute based on workflow type
            if workflow_type == 'sequential':
                result = await self._execute_sequential_workflow(workflow)
            elif workflow_type == 'parallel':
                result = await self._execute_parallel_workflow(workflow)
            elif workflow_type == 'hybrid':
                result = await self._execute_hybrid_workflow(workflow)
            else:
                raise ValueError(f"Unknown workflow type: {workflow_type}")

            # Mark workflow complete
            workflow['completed_at'] = datetime.now()
            workflow['status'] = WorkflowStatus.COMPLETED if result['status'] == 'success' else WorkflowStatus.FAILED

            # Move to completed
            self.completed_workflows[workflow_id] = workflow
            del self.active_workflows[workflow_id]

            if result['status'] == 'success':
                self.stats['total_workflows_completed'] += 1
            else:
                self.stats['total_workflows_failed'] += 1

            logger.info(f"✅ Workflow {workflow_name} completed: {result['status']}")

            return {
                'workflow_id': workflow_id,
                'workflow_name': workflow_name,
                'status': result['status'],
                'result': result,
                'execution_time_seconds': (workflow['completed_at'] - workflow['started_at']).total_seconds(),
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Workflow execution error: {e}")
            self.stats['total_workflows_failed'] += 1

            return {
                'workflow_id': workflow_id if 'workflow_id' in locals() else 'unknown',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    async def _execute_sequential_workflow(self, workflow: Dict) -> Dict[str, Any]:
        """
        📋 Execute steps one after another (A → B → C)
        """
        logger.info(f"📋 Executing sequential workflow: {workflow['workflow_name']}")

        steps = workflow['steps']
        results = []
        previous_output = None

        for i, step in enumerate(steps):
            logger.info(f"  Step {i+1}/{len(steps)}: {step.name} ({step.agent_type})")

            # Execute step
            step_result = await self._execute_step(step, previous_output)
            results.append(step_result)

            # Check if step failed
            if step.status == WorkflowStepStatus.FAILED:
                logger.error(f"  ❌ Step {step.name} failed: {step.error}")

                # Rollback if configured
                if workflow['rollback_on_failure']:
                    await self._rollback_workflow(workflow, i)

                return {
                    'status': 'failed',
                    'failed_step': step.name,
                    'error': step.error,
                    'results': results
                }

            # Pass output to next step if requested
            if step.use_previous_output:
                previous_output = step.result

        return {
            'status': 'success',
            'results': results,
            'final_output': results[-1] if results else None
        }

    async def _execute_parallel_workflow(self, workflow: Dict) -> Dict[str, Any]:
        """
        ⚡ Execute all steps at once (A + B + C simultaneously)
        """
        logger.info(f"⚡ Executing parallel workflow: {workflow['workflow_name']}")

        steps = workflow['steps']

        # Execute all steps in parallel
        step_tasks = [self._execute_step(step, None) for step in steps]
        results = await asyncio.gather(*step_tasks, return_exceptions=True)

        # Check for failures
        failures = []
        successes = []

        for i, (step, result) in enumerate(zip(steps, results)):
            if isinstance(result, Exception) or step.status == WorkflowStepStatus.FAILED:
                failures.append({
                    'step_name': step.name,
                    'error': str(result) if isinstance(result, Exception) else step.error
                })
            else:
                successes.append(result)

        if failures:
            logger.error(f"  ❌ {len(failures)} parallel steps failed")

            # Rollback if configured
            if workflow['rollback_on_failure']:
                await self._rollback_workflow(workflow, len(steps))

            return {
                'status': 'partial_success' if successes else 'failed',
                'successes': successes,
                'failures': failures,
                'results': results
            }

        return {
            'status': 'success',
            'results': results
        }

    async def _execute_hybrid_workflow(self, workflow: Dict) -> Dict[str, Any]:
        """
        🔀 Execute based on dependencies (some parallel, some sequential)
        """
        logger.info(f"🔀 Executing hybrid workflow: {workflow['workflow_name']}")

        steps = workflow['steps']
        step_results = {}  # step_id -> result
        completed_steps = set()

        # Build dependency graph
        step_map = {step.step_id: step for step in steps}

        # Execute steps respecting dependencies
        while len(completed_steps) < len(steps):
            # Find steps that can run now (all dependencies completed)
            ready_steps = []

            for step in steps:
                if step.step_id in completed_steps:
                    continue

                # Check if all dependencies are complete
                deps_complete = all(dep_id in completed_steps for dep_id in step.depends_on)

                if deps_complete:
                    ready_steps.append(step)

            if not ready_steps:
                # No steps ready - check for circular dependencies
                if len(completed_steps) < len(steps):
                    remaining = [s.name for s in steps if s.step_id not in completed_steps]
                    logger.error(f"  ❌ Circular dependency detected! Remaining steps: {remaining}")
                    return {
                        'status': 'failed',
                        'error': 'Circular dependency in workflow',
                        'remaining_steps': remaining
                    }
                break

            # Execute ready steps in parallel
            logger.info(f"  Executing {len(ready_steps)} parallel steps...")

            # Get previous outputs if needed
            step_inputs = []
            for step in ready_steps:
                if step.use_previous_output and step.depends_on:
                    # Use output from first dependency
                    dep_id = step.depends_on[0]
                    previous_output = step_results.get(dep_id, {}).get('result')
                else:
                    previous_output = None
                step_inputs.append(previous_output)

            # Execute in parallel
            tasks = [self._execute_step(step, prev_out) for step, prev_out in zip(ready_steps, step_inputs)]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Process results
            for step, result in zip(ready_steps, results):
                step_results[step.step_id] = result
                completed_steps.add(step.step_id)

                # Check for failure
                if isinstance(result, Exception) or step.status == WorkflowStepStatus.FAILED:
                    logger.error(f"  ❌ Step {step.name} failed")

                    # Rollback if configured
                    if workflow['rollback_on_failure']:
                        await self._rollback_workflow(workflow, len(completed_steps))

                    return {
                        'status': 'failed',
                        'failed_step': step.name,
                        'error': str(result) if isinstance(result, Exception) else step.error,
                        'partial_results': step_results
                    }

        return {
            'status': 'success',
            'results': [step_results[step.step_id] for step in steps]
        }

    async def _execute_step(self, step: WorkflowStep, previous_output: Any = None) -> Dict[str, Any]:
        """
        🎯 Execute a single workflow step with retry logic
        """
        step.status = WorkflowStepStatus.IN_PROGRESS
        step.started_at = datetime.now()

        # Prepare task data
        task_data = step.task_data.copy()

        # Add previous output if requested
        if previous_output is not None and step.use_previous_output:
            task_data['previous_step_output'] = previous_output

        # Retry logic
        for attempt in range(step.retry_count):
            try:
                step.retries_attempted = attempt

                # Call unified coordinator with timeout
                result = await asyncio.wait_for(
                    self.unified_coordinator.coordinate(step.agent_type, task_data),
                    timeout=step.timeout_seconds
                )

                # Check if successful
                if result.get('status') == 'success':
                    step.status = WorkflowStepStatus.COMPLETED
                    step.result = result
                    step.completed_at = datetime.now()
                    self.stats['total_steps_executed'] += 1

                    logger.info(f"    ✅ Step {step.name} completed")
                    return result
                else:
                    # Agent returned error
                    error_msg = result.get('error', 'Unknown error')
                    logger.warning(f"    ⚠️  Step {step.name} attempt {attempt+1} failed: {error_msg}")

                    if attempt < step.retry_count - 1:
                        await asyncio.sleep(2 ** attempt)  # Exponential backoff
                        continue
                    else:
                        # Final attempt failed
                        step.status = WorkflowStepStatus.FAILED
                        step.error = error_msg
                        step.completed_at = datetime.now()
                        self.stats['total_steps_failed'] += 1
                        return result

            except asyncio.TimeoutError:
                logger.warning(f"    ⏱️  Step {step.name} attempt {attempt+1} timed out")

                if attempt < step.retry_count - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                else:
                    step.status = WorkflowStepStatus.FAILED
                    step.error = f"Timeout after {step.timeout_seconds}s"
                    step.completed_at = datetime.now()
                    self.stats['total_steps_failed'] += 1
                    return {'status': 'error', 'error': step.error}

            except Exception as e:
                logger.error(f"    ❌ Step {step.name} attempt {attempt+1} error: {e}")

                if attempt < step.retry_count - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                else:
                    step.status = WorkflowStepStatus.FAILED
                    step.error = str(e)
                    step.completed_at = datetime.now()
                    self.stats['total_steps_failed'] += 1
                    return {'status': 'error', 'error': str(e)}

        # Should never reach here
        step.status = WorkflowStepStatus.FAILED
        step.error = "Max retries exceeded"
        return {'status': 'error', 'error': 'Max retries exceeded'}

    async def _rollback_workflow(self, workflow: Dict, failed_at_step: int):
        """
        🔄 Rollback workflow by undoing previous steps
        """
        logger.warning(f"🔄 Rolling back workflow {workflow['workflow_name']} from step {failed_at_step}")

        # Mark all steps as rolled back
        for step in workflow['steps'][:failed_at_step]:
            step.status = WorkflowStepStatus.ROLLED_BACK

        workflow['status'] = WorkflowStatus.ROLLED_BACK
        self.stats['total_rollbacks'] += 1

        # TODO: Implement actual rollback logic for each agent type
        # For now, just mark as rolled back

    def get_workflow_status(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """📊 Get status of a workflow"""
        workflow = self.active_workflows.get(workflow_id) or self.completed_workflows.get(workflow_id)

        if not workflow:
            return None

        return {
            'workflow_id': workflow['workflow_id'],
            'workflow_name': workflow['workflow_name'],
            'status': workflow['status'].value,
            'created_at': workflow['created_at'].isoformat(),
            'started_at': workflow['started_at'].isoformat() if workflow['started_at'] else None,
            'completed_at': workflow['completed_at'].isoformat() if workflow['completed_at'] else None,
            'steps': [step.to_dict() for step in workflow['steps']]
        }

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get workflow engine statistics"""
        return {
            'engine_id': self.engine_id,
            'stats': self.stats,
            'active_workflows': len(self.active_workflows),
            'completed_workflows': len(self.completed_workflows),
            'timestamp': datetime.now().isoformat()
        }


# =================== FACTORY FUNCTION ===================

def create_workflow_engine(unified_coordinator):
    """🏭 Create workflow engine instance"""
    return AgentWorkflowEngine(unified_coordinator)


# =================== TESTING ===================

if __name__ == "__main__":
    print("🔥💀🔥 Agent Workflow Engine - Standalone test mode 💀🔥💀")
    print("This requires unified_agent_coordinator to run full tests.")
    print("Run test_workflows.py for comprehensive testing!")
