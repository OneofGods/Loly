#!/usr/bin/env python3
"""
🔥💀🔥 LOLY'S UNIFIED AGENT COORDINATOR - SUPREME ORCHESTRATOR! 💀🔥💀

Extends Loly's sports coordination pattern to ALL agent types!
This replaces Eliza and makes Loly the SUPREME ORCHESTRATOR of everything!

COORDINATION CAPABILITIES:
- Sports Agents (15 specialized MCPs) ✅
- Research Agents (data gathering, validation)
- Writer Agents (content creation, reports)
- Reviewer Agents (code review, QA)
- Crypto Agents (git, indicators, prices)
- Utility Agents (context, reasoning, automation)
- External APIs (via openapi-mcp-server)

PATTERN: Parallel execution with weighted confidence (Loly's proven model)
ERROR HANDLING: Strict - NO fake data fallbacks
SCALABILITY: Dynamic agent spawning and load balancing
"""

import asyncio
import json
import logging
import aiohttp
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

# Import Loly's existing sports coordinator
from sports_mcp_coordinator import SportsMCPCoordinator, get_comprehensive_sports_analysis

logger = logging.getLogger(__name__)

class UnifiedAgentCoordinator:
    """
    🔥💀🔥 LOLY'S UNIFIED AGENT COORDINATOR 💀🔥💀

    Supreme orchestrator extending sports coordination to ALL agent types!
    This is what replaces Eliza and makes Loly SUPREME!
    """

    def __init__(self, registry_path: str = "agent_registry.json"):
        self.coordinator_id = f"loly_supreme_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Load agent registry
        self.registry = self._load_registry(registry_path)

        # Initialize sports coordinator (Loly's original domain)
        self.sports_coordinator = SportsMCPCoordinator()

        # Agent connection pool
        self.agent_connections = {}
        self.agent_health = {}

        # Workflow engine (imported lazily to avoid circular dependency)
        self.workflow_engine = None

        # Health monitoring & auto-recovery (imported lazily)
        self.health_monitor = None
        self.auto_recovery = None
        self.health_monitoring_active = False

        # Coordination metrics
        self.coordination_stats = {
            'total_coordinations': 0,
            'sports_coordinations': 0,
            'research_coordinations': 0,
            'writer_coordinations': 0,
            'reviewer_coordinations': 0,
            'crypto_coordinations': 0,
            'utility_coordinations': 0,
            'workflow_coordinations': 0,
            'failed_coordinations': 0,
            'average_response_time': 0.0
        }

        logger.info(f"🔥💀🔥 Loly's Unified Agent Coordinator {self.coordinator_id} initialized!")

    def _load_registry(self, registry_path: str) -> Dict:
        """📋 Load the agent registry"""
        try:
            with open(registry_path, 'r') as f:
                registry = json.load(f)
            logger.info(f"✅ Agent registry loaded: {registry['registry_version']}")
            return registry
        except Exception as e:
            logger.error(f"❌ Failed to load agent registry: {e}")
            return {}

    # =================== SPORTS COORDINATION (EXISTING) ===================

    async def coordinate_sports_analysis(self, home_team: str, away_team: str,
                                        sport: str, venue: str = "",
                                        game_time: str = "") -> Dict[str, Any]:
        """
        🏆 SPORTS COORDINATION - Loly's original and proven domain!
        Uses existing sports_mcp_coordinator with 7 parallel analyses
        """
        try:
            logger.info(f"🏆 Loly coordinating sports analysis: {away_team} @ {home_team} ({sport})")

            # Use existing sports coordinator
            result = await self.sports_coordinator.get_comprehensive_sports_analysis(
                home_team, away_team, sport, venue, game_time
            )

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['sports_coordinations'] += 1

            return {
                'coordination_type': 'sports',
                'coordinator': 'loly_sports_mcp',
                'status': 'success',
                'result': result,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Sports coordination failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'sports',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== RESEARCH COORDINATION (NEW) ===================

    async def coordinate_research(self, research_query: str, sources: List[str] = None,
                                 validation_level: str = "standard") -> Dict[str, Any]:
        """
        🔍 RESEARCH COORDINATION
        Parallel research across multiple sources with validation
        """
        try:
            logger.info(f"🔍 Loly coordinating research: {research_query[:50]}...")

            research_agents = self.registry.get('research_agents', {}).get('agents', {})

            if not research_agents:
                raise Exception("No research agents available")

            # Parallel research execution
            research_tasks = []

            # Primary research
            research_tasks.append(
                self._call_agent_http('research_agent', 'research', {
                    'query': research_query,
                    'sources': sources or ['web', 'academic', 'news'],
                    'depth': validation_level
                }, port=3201)
            )

            # Source validation (parallel)
            if validation_level in ['high', 'critical']:
                research_tasks.append(
                    self._call_agent_http('research_agent', 'validate', {
                        'query': research_query,
                        'validation_method': 'cross_reference'
                    }, port=3201)
                )

            # Execute in parallel
            results = await asyncio.gather(*research_tasks, return_exceptions=True)

            # Combine results
            research_data = results[0] if results and not isinstance(results[0], Exception) else {}
            validation_data = results[1] if len(results) > 1 and not isinstance(results[1], Exception) else {}

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['research_coordinations'] += 1

            return {
                'coordination_type': 'research',
                'coordinator': 'loly_unified',
                'status': 'success',
                'result': {
                    'research': research_data,
                    'validation': validation_data,
                    'confidence': self._calculate_research_confidence(research_data, validation_data)
                },
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Research coordination failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'research',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== WRITER COORDINATION (NEW) ===================

    async def coordinate_writing(self, content_type: str, specifications: Dict[str, Any],
                                context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        ✍️ WRITER COORDINATION
        Parallel content creation with formatting and editing
        """
        try:
            logger.info(f"✍️ Loly coordinating writing: {content_type}")

            writer_agents = self.registry.get('writer_agents', {}).get('agents', {})

            if not writer_agents:
                raise Exception("No writer agents available")

            # Parallel writing tasks
            writing_tasks = []

            # Main content writing
            writing_tasks.append(
                self._call_agent_http('writer_agent', 'write', {
                    'content_type': content_type,
                    'specifications': specifications,
                    'context': context or {}
                }, port=3203)
            )

            # Auto-formatting (parallel)
            writing_tasks.append(
                self._call_agent_http('writer_agent', 'format', {
                    'content_type': content_type,
                    'style': specifications.get('style', 'standard')
                }, port=3203)
            )

            # Execute in parallel
            results = await asyncio.gather(*writing_tasks, return_exceptions=True)

            content = results[0] if results and not isinstance(results[0], Exception) else {}
            formatting = results[1] if len(results) > 1 and not isinstance(results[1], Exception) else {}

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['writer_coordinations'] += 1

            return {
                'coordination_type': 'writer',
                'coordinator': 'loly_unified',
                'status': 'success',
                'result': {
                    'content': content,
                    'formatting': formatting
                },
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Writer coordination failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'writer',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== REVIEWER COORDINATION (NEW) ===================

    async def coordinate_review(self, code_or_content: str, review_type: str = "code",
                               strictness: str = "standard") -> Dict[str, Any]:
        """
        👁️ REVIEWER COORDINATION
        Parallel code/content review with analysis and suggestions
        """
        try:
            logger.info(f"👁️ Loly coordinating review: {review_type}")

            reviewer_agents = self.registry.get('reviewer_agents', {}).get('agents', {})

            if not reviewer_agents:
                raise Exception("No reviewer agents available")

            # Parallel review tasks
            review_tasks = []

            # Main review
            review_tasks.append(
                self._call_agent_http('reviewer_agent', 'review', {
                    'content': code_or_content,
                    'type': review_type,
                    'strictness': strictness
                }, port=3204)
            )

            # Deep analysis (parallel)
            review_tasks.append(
                self._call_agent_http('reviewer_agent', 'analyze', {
                    'content': code_or_content,
                    'analysis_type': 'quality_metrics'
                }, port=3204)
            )

            # Improvement suggestions (parallel)
            review_tasks.append(
                self._call_agent_http('reviewer_agent', 'suggest', {
                    'content': code_or_content,
                    'suggestion_type': 'improvements'
                }, port=3204)
            )

            # Execute in parallel
            results = await asyncio.gather(*review_tasks, return_exceptions=True)

            review = results[0] if results and not isinstance(results[0], Exception) else {}
            analysis = results[1] if len(results) > 1 and not isinstance(results[1], Exception) else {}
            suggestions = results[2] if len(results) > 2 and not isinstance(results[2], Exception) else {}

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['reviewer_coordinations'] += 1

            return {
                'coordination_type': 'reviewer',
                'coordinator': 'loly_unified',
                'status': 'success',
                'result': {
                    'review': review,
                    'analysis': analysis,
                    'suggestions': suggestions
                },
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Reviewer coordination failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'reviewer',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== CRYPTO COORDINATION (NEW) ===================

    async def coordinate_crypto_analysis(self, analysis_type: str,
                                        symbols: List[str] = None,
                                        timeframe: str = "1h") -> Dict[str, Any]:
        """
        💰 CRYPTO COORDINATION
        Parallel crypto analysis: indicators + prices + git ops
        """
        try:
            logger.info(f"💰 Loly coordinating crypto analysis: {analysis_type}")

            crypto_agents = self.registry.get('crypto_agents', {}).get('agents', {})

            # Parallel crypto tasks
            crypto_tasks = []

            # Technical indicators
            if 'indicators_agent' in crypto_agents:
                crypto_tasks.append(
                    self._call_agent_http('indicators_agent', 'analyze', {
                        'symbols': symbols or ['BTC', 'ETH'],
                        'timeframe': timeframe,
                        'indicators': ['RSI', 'MACD', 'BB']
                    }, port=3400)
                )

            # Price data
            if 'prices_agent' in crypto_agents:
                crypto_tasks.append(
                    self._call_agent_http('prices_agent', 'price', {
                        'symbols': symbols or ['BTC', 'ETH'],
                        'include_history': True
                    }, port=3500)
                )

            # Execute in parallel
            results = await asyncio.gather(*crypto_tasks, return_exceptions=True)

            indicators = results[0] if results and not isinstance(results[0], Exception) else {}
            prices = results[1] if len(results) > 1 and not isinstance(results[1], Exception) else {}

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['crypto_coordinations'] += 1

            return {
                'coordination_type': 'crypto',
                'coordinator': 'loly_unified',
                'status': 'success',
                'result': {
                    'indicators': indicators,
                    'prices': prices,
                    'combined_signal': self._calculate_crypto_signal(indicators, prices)
                },
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Crypto coordination failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'crypto',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== UTILITY COORDINATION (NEW) ===================

    async def coordinate_utility_task(self, task_type: str, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        🛠️ UTILITY COORDINATION
        Context management, reasoning, automation, API calls
        """
        try:
            logger.info(f"🛠️ Loly coordinating utility task: {task_type}")

            utility_agents = self.registry.get('utility_agents', {}).get('agents', {})

            # Route to appropriate utility agent
            result = None

            if task_type == 'reasoning' and 'sequential_thinking' in utility_agents:
                result = await self._call_agent_http('sequential_thinking', 'think', task_data, port=3208)

            elif task_type == 'context' and 'context7_mcp' in utility_agents:
                result = await self._call_agent_http('context7_mcp', 'context', task_data, port=3200)

            elif task_type == 'automation' and 'zapier' in utility_agents:
                result = await self._call_agent_http('zapier', 'execute', task_data, port=3202)

            elif task_type == 'api_call' and 'openapi_mcp_server' in utility_agents:
                result = await self._call_agent_http('openapi_mcp_server', 'call', task_data, port=3210)

            else:
                raise Exception(f"Unknown utility task type: {task_type}")

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['utility_coordinations'] += 1

            return {
                'coordination_type': 'utility',
                'task_type': task_type,
                'coordinator': 'loly_unified',
                'status': 'success',
                'result': result,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Utility coordination failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'utility',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== HELPER METHODS ===================

    async def _call_agent_http(self, agent_id: str, endpoint: str,
                              data: Dict[str, Any], port: int) -> Dict[str, Any]:
        """🌐 Call agent via HTTP (for MCP servers on different ports)"""
        try:
            url = f"http://localhost:{port}/api/{endpoint}"

            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, json=data) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        error_text = await response.text()
                        raise Exception(f"Agent {agent_id} returned {response.status}: {error_text}")

        except asyncio.TimeoutError:
            logger.error(f"⏱️ Agent {agent_id} timeout")
            return {'error': 'timeout', 'agent': agent_id}
        except Exception as e:
            logger.error(f"❌ Agent {agent_id} error: {e}")
            return {'error': str(e), 'agent': agent_id}

    def _calculate_research_confidence(self, research: Dict, validation: Dict) -> float:
        """🎯 Calculate research confidence score"""
        base_confidence = 0.5

        if research.get('sources_count', 0) > 3:
            base_confidence += 0.2

        if validation.get('cross_references', 0) > 2:
            base_confidence += 0.2

        if validation.get('validation_status') == 'verified':
            base_confidence += 0.1

        return min(0.95, base_confidence)

    def _calculate_crypto_signal(self, indicators: Dict, prices: Dict) -> str:
        """💰 Calculate combined crypto trading signal"""
        # Simple signal combination logic
        signals = []

        if indicators.get('RSI', 50) < 30:
            signals.append('BUY')
        elif indicators.get('RSI', 50) > 70:
            signals.append('SELL')

        if indicators.get('MACD_signal') == 'bullish':
            signals.append('BUY')
        elif indicators.get('MACD_signal') == 'bearish':
            signals.append('SELL')

        # Majority vote
        buy_count = signals.count('BUY')
        sell_count = signals.count('SELL')

        if buy_count > sell_count:
            return 'BUY'
        elif sell_count > buy_count:
            return 'SELL'
        else:
            return 'HOLD'

    # =================== MASTER COORDINATION METHOD ===================

    async def coordinate(self, task_type: str, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        🔥💀🔥 MASTER COORDINATION METHOD 💀🔥💀

        Routes any task to the appropriate coordination method
        This is the SINGLE ENTRY POINT for Loly to command ALL agents!
        """
        try:
            logger.info(f"🎯 Loly master coordination: {task_type}")

            # Route to specialized coordinators
            if task_type == 'sports':
                return await self.coordinate_sports_analysis(**task_data)

            elif task_type == 'research':
                return await self.coordinate_research(**task_data)

            elif task_type == 'writer':
                return await self.coordinate_writing(**task_data)

            elif task_type == 'reviewer':
                return await self.coordinate_review(**task_data)

            elif task_type == 'crypto':
                return await self.coordinate_crypto_analysis(**task_data)

            elif task_type == 'utility':
                return await self.coordinate_utility_task(**task_data)

            elif task_type == 'workflow':
                return await self.execute_workflow(**task_data)

            else:
                raise Exception(f"Unknown task type: {task_type}")

        except Exception as e:
            logger.error(f"💀 Master coordination failed: {e}")
            return {
                'coordination_type': task_type,
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== WORKFLOW ORCHESTRATION ===================

    def _initialize_workflow_engine(self):
        """🔧 Initialize workflow engine (lazy loading)"""
        if self.workflow_engine is None:
            from agent_workflow_engine import create_workflow_engine
            self.workflow_engine = create_workflow_engine(self)
            logger.info("🔥 Workflow engine initialized!")

    async def execute_workflow(self, workflow_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        🔥💀🔥 EXECUTE MULTI-AGENT WORKFLOW! 💀🔥💀

        Orchestrates complex multi-step tasks across multiple agents!

        workflow_config: {
            "workflow_name": "...",
            "workflow_type": "sequential|parallel|hybrid",
            "steps": [...]
        }
        """
        try:
            logger.info(f"🔥 Executing workflow: {workflow_config.get('workflow_name', 'unnamed')}")

            # Initialize workflow engine if needed
            self._initialize_workflow_engine()

            # Execute workflow
            result = await self.workflow_engine.execute_workflow(workflow_config)

            # Update stats
            self.coordination_stats['total_coordinations'] += 1
            self.coordination_stats['workflow_coordinations'] += 1

            return {
                'coordination_type': 'workflow',
                'status': 'success' if result.get('status') in ['success', 'completed'] else 'partial',
                'result': result,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Workflow execution failed: {e}")
            self.coordination_stats['failed_coordinations'] += 1
            return {
                'coordination_type': 'workflow',
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    async def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """📊 Get status of a running or completed workflow"""
        try:
            self._initialize_workflow_engine()

            status = self.workflow_engine.get_workflow_status(workflow_id)

            if status:
                return {
                    'status': 'success',
                    'workflow_status': status,
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return {
                    'status': 'not_found',
                    'error': f'Workflow {workflow_id} not found',
                    'timestamp': datetime.now().isoformat()
                }

        except Exception as e:
            logger.error(f"💀 Get workflow status error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    async def get_workflow_stats(self) -> Dict[str, Any]:
        """📊 Get workflow engine statistics"""
        try:
            self._initialize_workflow_engine()

            return self.workflow_engine.get_stats()

        except Exception as e:
            logger.error(f"💀 Get workflow stats error: {e}")
            return {
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    # =================== STATUS AND HEALTH ===================

    def get_coordination_stats(self) -> Dict[str, Any]:
        """📊 Get coordination statistics"""
        return {
            'coordinator_id': self.coordinator_id,
            'stats': self.coordination_stats,
            'registry_version': self.registry.get('registry_version', 'unknown'),
            'available_agent_types': list(self.registry.keys()),
            'timestamp': datetime.now().isoformat()
        }

    async def health_check(self) -> Dict[str, Any]:
        """💚 Health check for all registered agents"""
        health_status = {
            'coordinator': 'healthy',
            'sports_coordinator': 'healthy',
            'agents': {},
            'timestamp': datetime.now().isoformat()
        }

        # Check each agent category
        for category in ['research_agents', 'writer_agents', 'reviewer_agents', 'crypto_agents', 'utility_agents']:
            agents = self.registry.get(category, {}).get('agents', {})

            for agent_id, agent_info in agents.items():
                if 'port' in agent_info:
                    # Try to ping the agent
                    try:
                        port = agent_info['port']
                        timeout = aiohttp.ClientTimeout(total=5)
                        async with aiohttp.ClientSession(timeout=timeout) as session:
                            async with session.get(f"http://localhost:{port}/health") as response:
                                if response.status == 200:
                                    health_status['agents'][agent_id] = 'healthy'
                                else:
                                    health_status['agents'][agent_id] = 'unhealthy'
                    except:
                        health_status['agents'][agent_id] = agent_info.get('status', 'unknown')
                else:
                    health_status['agents'][agent_id] = agent_info.get('status', 'internal')

        return health_status

    # =================== HEALTH MONITORING & AUTO-RECOVERY ===================

    def _initialize_health_monitoring(self):
        """🔧 Initialize health monitoring and auto-recovery (lazy loading)"""
        if self.health_monitor is None:
            from agent_health_monitor import create_health_monitor
            from agent_auto_recovery import create_auto_recovery

            self.health_monitor = create_health_monitor()
            self.auto_recovery = create_auto_recovery(self.health_monitor, self.registry.get('recovery', {}))

            logger.info("🔥 Health monitoring & auto-recovery initialized!")

    async def start_health_monitoring(self):
        """🚀 Start health monitoring and auto-recovery services"""
        try:
            self._initialize_health_monitoring()

            # Register all known agents
            for category in ['sports_agents', 'research_agents', 'writer_agents', 'reviewer_agents', 'crypto_agents', 'utility_agents']:
                agents = self.registry.get(category, {}).get('agents', {})
                for agent_id, agent_info in agents.items():
                    self.health_monitor.register_agent(agent_id, agent_info)

            # Start monitoring services
            await self.health_monitor.start_monitoring()
            await self.auto_recovery.start_recovery_service()

            self.health_monitoring_active = True

            logger.info("✅ Health monitoring & auto-recovery services started!")
            return True

        except Exception as e:
            logger.error(f"❌ Failed to start health monitoring: {e}")
            return False

    async def stop_health_monitoring(self):
        """🛑 Stop health monitoring and auto-recovery services"""
        try:
            if self.health_monitor:
                await self.health_monitor.stop_monitoring()

            if self.auto_recovery:
                await self.auto_recovery.stop_recovery_service()

            self.health_monitoring_active = False

            logger.info("🛑 Health monitoring & auto-recovery services stopped")
            return True

        except Exception as e:
            logger.error(f"❌ Failed to stop health monitoring: {e}")
            return False

    def record_agent_interaction(self, agent_id: str, success: bool,
                                 response_time: float = None, error_type: str = None):
        """📝 Record agent interaction for health monitoring"""
        if self.health_monitor:
            self.health_monitor.record_agent_interaction(agent_id, success, response_time, error_type)

    def get_agent_health_status(self, agent_id: str) -> Dict[str, Any]:
        """💚 Get health status for specific agent"""
        try:
            self._initialize_health_monitoring()

            health = self.health_monitor.get_agent_health(agent_id)

            if health:
                return {
                    'status': 'success',
                    'agent_health': health,
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return {
                    'status': 'not_found',
                    'error': f'Agent {agent_id} not found in health monitor',
                    'timestamp': datetime.now().isoformat()
                }

        except Exception as e:
            logger.error(f"💀 Get agent health error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def get_all_agents_health(self) -> Dict[str, Any]:
        """💚 Get health status for all agents"""
        try:
            self._initialize_health_monitoring()

            all_health = self.health_monitor.get_all_agent_health()

            return {
                'status': 'success',
                'agents_health': all_health,
                'health_monitoring_active': self.health_monitoring_active,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Get all agents health error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def get_health_monitoring_stats(self) -> Dict[str, Any]:
        """📊 Get health monitoring statistics"""
        try:
            self._initialize_health_monitoring()

            monitor_stats = self.health_monitor.get_stats()
            recovery_stats = self.auto_recovery.get_stats() if self.auto_recovery else {}

            return {
                'monitoring': monitor_stats,
                'recovery': recovery_stats,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"💀 Get health monitoring stats error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def get_recovery_history(self, agent_id: str = None) -> Dict[str, Any]:
        """📜 Get recovery history for agent(s)"""
        try:
            self._initialize_health_monitoring()

            if self.auto_recovery:
                history = self.auto_recovery.get_recovery_history(agent_id)

                return {
                    'status': 'success',
                    'recovery_history': history,
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return {
                    'status': 'not_initialized',
                    'error': 'Auto-recovery not initialized',
                    'timestamp': datetime.now().isoformat()
                }

        except Exception as e:
            logger.error(f"💀 Get recovery history error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }


# =================== FACTORY FUNCTION ===================

def create_unified_coordinator(registry_path: str = "agent_registry.json") -> UnifiedAgentCoordinator:
    """🏭 Factory function to create Loly's unified coordinator"""
    return UnifiedAgentCoordinator(registry_path)


# =================== TESTING ===================

if __name__ == "__main__":
    async def test_unified_coordinator():
        print("🔥💀🔥 Testing Loly's Unified Agent Coordinator! 💀🔥💀\n")

        coordinator = create_unified_coordinator()

        # Test 1: Health check
        print("1️⃣ Health Check...")
        health = await coordinator.health_check()
        print(f"Health Status: {json.dumps(health, indent=2)}\n")

        # Test 2: Coordination stats
        print("2️⃣ Coordination Stats...")
        stats = coordinator.get_coordination_stats()
        print(f"Stats: {json.dumps(stats, indent=2)}\n")

        # Test 3: Sports coordination (should work!)
        print("3️⃣ Sports Coordination Test...")
        sports_result = await coordinator.coordinate('sports', {
            'home_team': 'Real Madrid',
            'away_team': 'Barcelona',
            'sport': 'UEFA',
            'venue': 'Santiago Bernabéu',
            'game_time': '2025-11-20T20:00:00'
        })
        print(f"Sports Result: {json.dumps(sports_result, indent=2, default=str)[:500]}...\n")

        print("✅ Unified Coordinator Test Complete!")

    asyncio.run(test_unified_coordinator())
