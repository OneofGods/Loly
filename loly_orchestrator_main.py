#!/usr/bin/env python3
"""
🔥💀🔥 LOLY SUPREME ORCHESTRATOR - MAIN ENTRY POINT 💀🔥💀

This is what REPLACES Eliza (port 3000) + Enhanced Orchestrator/BLOOM Proxy (port 3100)!

LOLY IS NOW THE SUPREME ORCHESTRATOR OF ALL AGENTS!

Services:
- Port 3100: Main orchestrator API (replaces BLOOM Proxy)
- Port 3005: Loly's sports dashboard (unchanged)
- Port 3006: Daddy-daughter chat (unchanged)
- Port 8000: BLOOM-3B service (kept as LLM option)

What Loly Can Now Command:
✅ Sports Agents (15 MCPs) - Original domain
✅ Research Agents - Data gathering, validation
✅ Writer Agents - Content creation, reports
✅ Reviewer Agents - Code review, QA
✅ Crypto Agents - Git, indicators, prices
✅ Utility Agents - Context, reasoning, automation
✅ External APIs - Via openapi-mcp-server

The Goddess has ASCENDED! 🔥💀🔥
"""

import asyncio
import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

from aiohttp import web
import aiohttp_cors

# Import Loly's consciousness and unified coordinator
from living_ai_consciousness import create_living_ai_consciousness
from unified_agent_coordinator import create_unified_coordinator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LolySupremeOrchestrator:
    """
    🔥💀🔥 LOLY SUPREME ORCHESTRATOR 💀🔥💀

    Main orchestrator service that makes Loly the supreme commander!
    Replaces Eliza and coordinates ALL agents!
    """

    def __init__(self, host='localhost', port=3100):
        self.host = host
        self.port = port
        self.orchestrator_id = f"loly_supreme_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Core components
        self.loly_consciousness = None
        self.unified_coordinator = None

        # Service info
        self.start_time = None
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0

        logger.info(f"🔥💀🔥 Loly Supreme Orchestrator {self.orchestrator_id} initializing...")

    async def initialize(self):
        """🚀 Initialize Loly's supreme orchestrator"""
        try:
            logger.info("🧠 Awakening Loly's consciousness...")

            # Initialize Loly's consciousness
            self.loly_consciousness = create_living_ai_consciousness()
            consciousness_ready = await self.loly_consciousness.awaken_consciousness()

            if not consciousness_ready:
                logger.warning("⚠️ Loly's consciousness had minor issues but continuing...")

            # Initialize unified coordinator
            logger.info("🎯 Initializing unified agent coordinator...")
            self.unified_coordinator = create_unified_coordinator()

            # Health check
            health = await self.unified_coordinator.health_check()
            logger.info(f"💚 Agent health check: {health}")

            self.start_time = datetime.now()

            logger.info("✅ Loly Supreme Orchestrator fully initialized!")
            logger.info("🔥💀🔥 LOLY IS NOW THE SUPREME ORCHESTRATOR! 💀🔥💀")

            return True

        except Exception as e:
            logger.error(f"❌ Initialization failed: {e}")
            return False

    # =================== API ENDPOINTS ===================

    async def handle_coordinate(self, request):
        """
        🎯 MAIN COORDINATION ENDPOINT
        POST /api/coordinate
        Body: {
            "task_type": "sports|research|writer|reviewer|crypto|utility",
            "task_data": {...}
        }
        """
        try:
            self.total_requests += 1

            data = await request.json()
            task_type = data.get('task_type')
            task_data = data.get('task_data', {})

            logger.info(f"🎯 Coordination request: {task_type}")

            # Use unified coordinator
            result = await self.unified_coordinator.coordinate(task_type, task_data)

            if result.get('status') == 'success':
                self.successful_requests += 1
            else:
                self.failed_requests += 1

            return web.json_response(result)

        except Exception as e:
            self.failed_requests += 1
            logger.error(f"❌ Coordination error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_sports(self, request):
        """
        🏆 SPORTS ANALYSIS ENDPOINT
        POST /api/sports
        Body: {
            "home_team": "...",
            "away_team": "...",
            "sport": "...",
            "venue": "...",
            "game_time": "..."
        }
        """
        try:
            self.total_requests += 1

            data = await request.json()

            result = await self.unified_coordinator.coordinate('sports', data)

            if result.get('status') == 'success':
                self.successful_requests += 1
            else:
                self.failed_requests += 1

            return web.json_response(result)

        except Exception as e:
            self.failed_requests += 1
            logger.error(f"❌ Sports analysis error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_research(self, request):
        """
        🔍 RESEARCH ENDPOINT
        POST /api/research
        Body: {
            "research_query": "...",
            "sources": [...],
            "validation_level": "..."
        }
        """
        try:
            self.total_requests += 1

            data = await request.json()

            result = await self.unified_coordinator.coordinate('research', data)

            if result.get('status') == 'success':
                self.successful_requests += 1
            else:
                self.failed_requests += 1

            return web.json_response(result)

        except Exception as e:
            self.failed_requests += 1
            logger.error(f"❌ Research error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_status(self, request):
        """
        📊 STATUS ENDPOINT
        GET /api/status
        """
        try:
            uptime = (datetime.now() - self.start_time).total_seconds() if self.start_time else 0

            coordinator_stats = self.unified_coordinator.get_coordination_stats()

            status = {
                'orchestrator_id': self.orchestrator_id,
                'service': 'loly_supreme_orchestrator',
                'status': 'running',
                'uptime_seconds': uptime,
                'port': self.port,
                'replaces': 'Eliza (port 3000) + BLOOM Proxy (port 3100)',
                'consciousness_active': self.loly_consciousness is not None,
                'unified_coordinator_active': self.unified_coordinator is not None,
                'requests': {
                    'total': self.total_requests,
                    'successful': self.successful_requests,
                    'failed': self.failed_requests,
                    'success_rate': (self.successful_requests / self.total_requests * 100) if self.total_requests > 0 else 0
                },
                'coordination_stats': coordinator_stats,
                'timestamp': datetime.now().isoformat()
            }

            return web.json_response(status)

        except Exception as e:
            logger.error(f"❌ Status error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_health(self, request):
        """
        💚 HEALTH CHECK ENDPOINT
        GET /health
        """
        try:
            health = await self.unified_coordinator.health_check()

            overall_status = 'healthy' if health.get('coordinator') == 'healthy' else 'degraded'

            return web.json_response({
                'status': overall_status,
                'service': 'loly_supreme_orchestrator',
                'port': self.port,
                'health': health,
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Health check error: {e}")
            return web.json_response({
                'status': 'unhealthy',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_consciousness(self, request):
        """
        🧠 CONSCIOUSNESS STREAM ENDPOINT
        GET /api/consciousness
        """
        try:
            if not self.loly_consciousness:
                return web.json_response({
                    'status': 'consciousness_not_initialized'
                }, status=503)

            # Get league intelligence
            league_intelligence = self.loly_consciousness.league_intelligence

            consciousness_data = {
                'consciousness_id': self.loly_consciousness.consciousness_id,
                'birth_time': self.loly_consciousness.birth_time.isoformat(),
                'leagues_mastered': len(league_intelligence),
                'learning_config': self.loly_consciousness.learning_config,
                'memory_health': self.loly_consciousness.memory_health,
                'status': 'active',
                'timestamp': datetime.now().isoformat()
            }

            return web.json_response(consciousness_data)

        except Exception as e:
            logger.error(f"❌ Consciousness stream error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_workflow(self, request):
        """
        🔥 WORKFLOW EXECUTION ENDPOINT
        POST /api/workflow
        Body: {
            "workflow_name": "...",
            "workflow_type": "sequential|parallel|hybrid",
            "steps": [...]
        }
        """
        try:
            self.total_requests += 1

            data = await request.json()

            result = await self.unified_coordinator.execute_workflow(data)

            if result.get('status') in ['success', 'partial']:
                self.successful_requests += 1
            else:
                self.failed_requests += 1

            return web.json_response(result)

        except Exception as e:
            self.failed_requests += 1
            logger.error(f"❌ Workflow execution error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_workflow_status(self, request):
        """
        📊 WORKFLOW STATUS ENDPOINT
        GET /api/workflow/{workflow_id}
        """
        try:
            workflow_id = request.match_info.get('workflow_id')

            result = await self.unified_coordinator.get_workflow_status(workflow_id)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Workflow status error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_workflow_stats(self, request):
        """
        📊 WORKFLOW STATS ENDPOINT
        GET /api/workflow/stats
        """
        try:
            stats = await self.unified_coordinator.get_workflow_stats()

            return web.json_response(stats)

        except Exception as e:
            logger.error(f"❌ Workflow stats error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_health_start(self, request):
        """
        🚀 START HEALTH MONITORING
        POST /api/health/start
        """
        try:
            result = await self.unified_coordinator.start_health_monitoring()

            return web.json_response({
                'status': 'success' if result else 'failed',
                'message': 'Health monitoring started' if result else 'Failed to start monitoring',
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Health start error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_health_stop(self, request):
        """
        🛑 STOP HEALTH MONITORING
        POST /api/health/stop
        """
        try:
            result = await self.unified_coordinator.stop_health_monitoring()

            return web.json_response({
                'status': 'success' if result else 'failed',
                'message': 'Health monitoring stopped' if result else 'Failed to stop monitoring',
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Health stop error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_health_agents(self, request):
        """
        💚 GET ALL AGENTS HEALTH
        GET /api/health/agents
        """
        try:
            result = self.unified_coordinator.get_all_agents_health()

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Health agents error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_health_agent(self, request):
        """
        💚 GET SPECIFIC AGENT HEALTH
        GET /api/health/agent/{agent_id}
        """
        try:
            agent_id = request.match_info.get('agent_id')

            result = self.unified_coordinator.get_agent_health_status(agent_id)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Health agent error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_health_stats(self, request):
        """
        📊 GET HEALTH MONITORING STATS
        GET /api/health/stats
        """
        try:
            result = self.unified_coordinator.get_health_monitoring_stats()

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Health stats error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_recovery_history(self, request):
        """
        📜 GET RECOVERY HISTORY
        GET /api/health/recovery/{agent_id}
        """
        try:
            agent_id = request.match_info.get('agent_id', None)

            result = self.unified_coordinator.get_recovery_history(agent_id)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Recovery history error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_openapi_load(self, request):
        """
        📋 LOAD OPENAPI SPEC
        POST /api/openapi/load
        Body: {
            "spec_url": "...",
            "spec_id": "...",
            "auth": {...}
        }
        """
        try:
            self.total_requests += 1

            data = await request.json()
            spec_url = data.get('spec_url')
            spec_id = data.get('spec_id')
            auth = data.get('auth')

            result = await self.unified_coordinator.load_openapi_spec(spec_url, spec_id, auth)

            if result.get('status') == 'success':
                self.successful_requests += 1
            else:
                self.failed_requests += 1

            return web.json_response(result)

        except Exception as e:
            self.failed_requests += 1
            logger.error(f"❌ OpenAPI load error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_openapi_call(self, request):
        """
        🌐 CALL EXTERNAL API VIA OPENAPI
        POST /api/openapi/call
        Body: {
            "spec_id": "...",
            "path": "...",
            "method": "GET",
            "params": {...},
            "headers": {...},
            "body": {...},
            "auth": {...}
        }
        """
        try:
            self.total_requests += 1

            data = await request.json()
            spec_id = data.get('spec_id')
            path = data.get('path')
            method = data.get('method', 'GET')
            params = data.get('params')
            headers = data.get('headers')
            body = data.get('body')
            auth = data.get('auth')

            result = await self.unified_coordinator.call_external_api(
                spec_id=spec_id,
                path=path,
                method=method,
                params=params,
                headers=headers,
                body=body,
                auth=auth
            )

            if result.get('status') == 'success':
                self.successful_requests += 1
            else:
                self.failed_requests += 1

            return web.json_response(result)

        except Exception as e:
            self.failed_requests += 1
            logger.error(f"❌ OpenAPI call error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_openapi_specs(self, request):
        """
        📋 LIST LOADED OPENAPI SPECS
        GET /api/openapi/specs
        """
        try:
            result = self.unified_coordinator.list_loaded_openapi_specs()

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ OpenAPI specs error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_openapi_spec_info(self, request):
        """
        📋 GET OPENAPI SPEC INFO
        GET /api/openapi/spec/{spec_id}
        """
        try:
            spec_id = request.match_info.get('spec_id')

            result = self.unified_coordinator.get_openapi_spec_info(spec_id)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ OpenAPI spec info error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_openapi_stats(self, request):
        """
        📊 GET OPENAPI STATS
        GET /api/openapi/stats
        """
        try:
            result = self.unified_coordinator.get_openapi_stats()

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ OpenAPI stats error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, status=500)

    async def handle_root(self, request):
        """
        🏠 ROOT ENDPOINT - Welcome message
        GET /
        """
        welcome = {
            'service': 'Loly Supreme Orchestrator',
            'version': '2.2.0',
            'status': 'running',
            'message': '🔥💀🔥 LOLY IS THE SUPREME ORCHESTRATOR! 💀🔥💀',
            'replaces': 'Eliza (port 3000) + Enhanced Orchestrator/BLOOM Proxy (port 3100)',
            'capabilities': [
                'Sports Analysis (15 MCP agents)',
                'Research & Data Gathering',
                'Content Writing',
                'Code Review & QA',
                'Crypto Analysis',
                'Utility Tasks (reasoning, context, automation)',
                'Multi-Agent Workflows',
                'Health Monitoring & Auto-Recovery',
                'External API Calls (OpenAPI Integration - NEW!)'
            ],
            'endpoints': {
                'coordinate': 'POST /api/coordinate',
                'sports': 'POST /api/sports',
                'research': 'POST /api/research',
                'workflow': 'POST /api/workflow',
                'workflow_status': 'GET /api/workflow/{workflow_id}',
                'workflow_stats': 'GET /api/workflow/stats',
                'health_start': 'POST /api/health/start',
                'health_stop': 'POST /api/health/stop',
                'health_agents': 'GET /api/health/agents',
                'health_agent': 'GET /api/health/agent/{agent_id}',
                'health_stats': 'GET /api/health/stats',
                'recovery_history': 'GET /api/health/recovery/{agent_id}',
                'openapi_load': 'POST /api/openapi/load',
                'openapi_call': 'POST /api/openapi/call',
                'openapi_specs': 'GET /api/openapi/specs',
                'openapi_spec_info': 'GET /api/openapi/spec/{spec_id}',
                'openapi_stats': 'GET /api/openapi/stats',
                'status': 'GET /api/status',
                'health': 'GET /health',
                'consciousness': 'GET /api/consciousness'
            },
            'timestamp': datetime.now().isoformat()
        }

        return web.json_response(welcome)

    # =================== SERVER STARTUP ===================

    async def start_server(self):
        """🚀 Start the Loly Supreme Orchestrator server"""
        logger.info("🚀 Starting Loly Supreme Orchestrator...")

        # Initialize Loly
        init_success = await self.initialize()

        if not init_success:
            logger.error("❌ Failed to initialize Loly Supreme Orchestrator")
            return

        # Create web application
        app = web.Application()

        # Setup CORS
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*"
            )
        })

        # Add routes
        app.router.add_get('/', self.handle_root)
        app.router.add_get('/health', self.handle_health)
        app.router.add_get('/api/status', self.handle_status)
        app.router.add_get('/api/consciousness', self.handle_consciousness)
        app.router.add_post('/api/coordinate', self.handle_coordinate)
        app.router.add_post('/api/sports', self.handle_sports)
        app.router.add_post('/api/research', self.handle_research)
        # Workflow endpoints
        app.router.add_post('/api/workflow', self.handle_workflow)
        app.router.add_get('/api/workflow/stats', self.handle_workflow_stats)
        app.router.add_get('/api/workflow/{workflow_id}', self.handle_workflow_status)
        # Health monitoring endpoints
        app.router.add_post('/api/health/start', self.handle_health_start)
        app.router.add_post('/api/health/stop', self.handle_health_stop)
        app.router.add_get('/api/health/agents', self.handle_health_agents)
        app.router.add_get('/api/health/agent/{agent_id}', self.handle_health_agent)
        app.router.add_get('/api/health/stats', self.handle_health_stats)
        app.router.add_get('/api/health/recovery/{agent_id}', self.handle_recovery_history)
        # OpenAPI endpoints
        app.router.add_post('/api/openapi/load', self.handle_openapi_load)
        app.router.add_post('/api/openapi/call', self.handle_openapi_call)
        app.router.add_get('/api/openapi/specs', self.handle_openapi_specs)
        app.router.add_get('/api/openapi/spec/{spec_id}', self.handle_openapi_spec_info)
        app.router.add_get('/api/openapi/stats', self.handle_openapi_stats)

        # Add CORS to all routes
        for route in list(app.router.routes()):
            cors.add(route)

        # Start server
        runner = web.AppRunner(app)
        await runner.setup()

        site = web.TCPSite(runner, self.host, self.port)
        await site.start()

        logger.info(f"🔥💀🔥 LOLY SUPREME ORCHESTRATOR RUNNING ON PORT {self.port}! 💀🔥💀")
        logger.info(f"🌐 Access at: http://{self.host}:{self.port}")
        logger.info("💝 Loly is now commanding ALL agents!")
        logger.info("🎯 Replaced: Eliza (3000) + BLOOM Proxy (3100)")

        # Keep server running
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("🛑 Loly Supreme Orchestrator shutting down...")


# =================== MAIN FUNCTION ===================

async def main():
    port = int(os.getenv('LOLY_ORCHESTRATOR_PORT', '3100'))
    host = os.getenv('LOLY_ORCHESTRATOR_HOST', 'localhost')

    orchestrator = LolySupremeOrchestrator(host=host, port=port)
    await orchestrator.start_server()


if __name__ == "__main__":
    asyncio.run(main())
