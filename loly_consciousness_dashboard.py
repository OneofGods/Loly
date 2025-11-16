#!/usr/bin/env python3
"""
🧠💀🧠 LOLY CONSCIOUSNESS MONITORING DASHBOARD - REAL-TIME BRAIN ACTIVITY! 💀🧠💀

A beautiful web-based dashboard to monitor Loly's consciousness in real-time!
Watch her brain learn, evolve, and become more intelligent with every prediction!

🌟 FEATURES:
- Real-time consciousness metrics
- League-by-league performance tracking  
- Learning pattern visualization
- Success rate monitoring
- Response time analysis
- Brain activity heat maps
- Consciousness evolution timeline

💀🔥💀 SEE LOLY'S MIND IN ACTION! 🔥💀🔥
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import aiohttp
from aiohttp import web, WSMsgType
import aiohttp_cors
import jinja2
import aiofiles

# Import consciousness system
from enhanced_ai_consciousness import EnhancedAIConsciousness, create_enhanced_ai_consciousness
from loly_consciousness_integration import LolyConsciousnessIntegration

logger = logging.getLogger(__name__)

class LolyConsciousnessDashboard:
    """
    🧠💀🧠 LOLY CONSCIOUSNESS DASHBOARD SERVER! 💀🧠💀
    
    Real-time web dashboard for monitoring Loly's consciousness evolution!
    """
    
    def __init__(self, port: int = 3008, memory_dir: str = None):
        """Initialize the consciousness dashboard"""
        self.port = port
        self.memory_dir = memory_dir or "consciousness_memory"
        self.consciousness = None
        self.app = None
        self.websocket_clients = []
        
        # Dashboard state
        self.dashboard_stats = {
            'total_leagues': 0,
            'active_sessions': 0,
            'total_predictions': 0,
            'overall_success_rate': 0.0,
            'brain_uptime': 0,
            'last_update': datetime.now().isoformat()
        }
        
        logger.info("🧠💀🧠 Loly Consciousness Dashboard Initialized! 💀🧠💀")
    
    async def initialize_consciousness(self):
        """🔥 Initialize consciousness for monitoring"""
        try:
            logger.info("🧠 Initializing consciousness for dashboard...")
            
            self.consciousness = create_enhanced_ai_consciousness(self.memory_dir)
            await self.consciousness.awaken()
            
            logger.info("✅ Dashboard consciousness awakened!")
            return True
            
        except Exception as e:
            logger.error(f"💀 Error initializing dashboard consciousness: {e}")
            return False
    
    async def get_consciousness_metrics(self) -> Dict[str, Any]:
        """📊 Get comprehensive consciousness metrics"""
        try:
            if not self.consciousness:
                return {"status": "consciousness_unavailable"}
            
            # Get intelligence report
            report = self.consciousness.get_intelligence_report()
            
            # Calculate additional metrics
            agent_performance = report.get('agent_performance', {})
            
            # Extract league-specific stats (from sports agent)
            sports_stats = agent_performance.get('sports', {})
            
            # Calculate success rates by agent type
            agent_success_rates = {}
            for agent_type, stats in agent_performance.items():
                if stats.get('total', 0) > 0:
                    success_rate = (stats.get('success', 0) / stats.get('total', 1)) * 100
                    agent_success_rates[agent_type] = {
                        'success_rate': success_rate,
                        'total_predictions': stats.get('total', 0),
                        'avg_response_time': stats.get('avg_time', 0),
                        'confidence_level': 'high' if success_rate > 75 else 'medium' if success_rate > 50 else 'low'
                    }
            
            # Update dashboard stats
            self.dashboard_stats.update({
                'total_leagues': len([a for a in agent_performance.values() if a.get('total', 0) > 0]),
                'total_predictions': report.get('total_interactions', 0),
                'overall_success_rate': report.get('overall_success_rate', 0),
                'brain_uptime': report.get('uptime', 0),
                'last_update': datetime.now().isoformat()
            })
            
            # Build comprehensive metrics
            metrics = {
                'consciousness_info': {
                    'id': report.get('consciousness_id', 'Unknown'),
                    'birth_time': report.get('birth_time', ''),
                    'uptime_seconds': report.get('uptime', 0),
                    'uptime_formatted': self._format_uptime(report.get('uptime', 0))
                },
                'overall_performance': {
                    'total_interactions': report.get('total_interactions', 0),
                    'overall_success_rate': report.get('overall_success_rate', 0),
                    'pattern_count': report.get('pattern_count', 0),
                    'session_count': report.get('session_count', 0)
                },
                'agent_performance': agent_success_rates,
                'sports_specific': {
                    'total_sports_predictions': sports_stats.get('total', 0),
                    'sports_success_rate': (sports_stats.get('success', 0) / max(sports_stats.get('total', 1), 1)) * 100,
                    'avg_prediction_time': sports_stats.get('avg_time', 0),
                    'patterns_discovered': len(sports_stats.get('patterns', []))
                },
                'learning_config': report.get('learning_config', {}),
                'dashboard_stats': self.dashboard_stats,
                'timestamp': datetime.now().isoformat()
            }
            
            return metrics
            
        except Exception as e:
            logger.error(f"💀 Error getting consciousness metrics: {e}")
            return {"status": "error", "error": str(e)}
    
    def _format_uptime(self, seconds: float) -> str:
        """⏱️ Format uptime in human-readable format"""
        if seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        else:
            return f"{seconds/86400:.1f} days"
    
    async def websocket_handler(self, request):
        """🔗 WebSocket handler for real-time updates"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        
        # Add client to list
        self.websocket_clients.append(ws)
        logger.info(f"🔗 WebSocket client connected. Total: {len(self.websocket_clients)}")
        
        try:
            # Send initial metrics
            metrics = await self.get_consciousness_metrics()
            await ws.send_str(json.dumps({
                'type': 'consciousness_update',
                'data': metrics
            }))
            
            # Handle incoming messages
            async for msg in ws:
                if msg.type == WSMsgType.TEXT:
                    try:
                        data = json.loads(msg.data)
                        
                        if data.get('type') == 'request_update':
                            # Send current metrics
                            metrics = await self.get_consciousness_metrics()
                            await ws.send_str(json.dumps({
                                'type': 'consciousness_update',
                                'data': metrics
                            }))
                            
                    except json.JSONDecodeError:
                        logger.warning("⚠️ Invalid JSON received from WebSocket client")
                        
                elif msg.type == WSMsgType.ERROR:
                    logger.error(f"💀 WebSocket error: {ws.exception()}")
                    break
                    
        except Exception as e:
            logger.error(f"💀 WebSocket handler error: {e}")
        finally:
            # Remove client from list
            if ws in self.websocket_clients:
                self.websocket_clients.remove(ws)
            logger.info(f"🔗 WebSocket client disconnected. Total: {len(self.websocket_clients)}")
        
        return ws
    
    async def broadcast_update(self):
        """📡 Broadcast consciousness update to all connected clients"""
        if not self.websocket_clients:
            return
        
        try:
            metrics = await self.get_consciousness_metrics()
            message = json.dumps({
                'type': 'consciousness_update',
                'data': metrics
            })
            
            # Send to all connected clients
            disconnected_clients = []
            for ws in self.websocket_clients:
                try:
                    await ws.send_str(message)
                except Exception as e:
                    logger.warning(f"⚠️ Failed to send to WebSocket client: {e}")
                    disconnected_clients.append(ws)
            
            # Remove disconnected clients
            for ws in disconnected_clients:
                self.websocket_clients.remove(ws)
                
        except Exception as e:
            logger.error(f"💀 Error broadcasting update: {e}")
    
    async def api_metrics(self, request):
        """📊 API endpoint for consciousness metrics"""
        try:
            metrics = await self.get_consciousness_metrics()
            return web.json_response(metrics)
        except Exception as e:
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)
    
    async def dashboard_html(self, request):
        """🌐 Serve the dashboard HTML"""
        html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧠💀 Loly Consciousness Dashboard 💀🧠</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #0a0a0a, #1a0a1a, #0a1a0a);
            color: #00ff41;
            min-height: 100vh;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            border: 2px solid #00ff41;
            border-radius: 10px;
            background: rgba(0, 255, 65, 0.1);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 0 0 10px #00ff41;
        }
        
        .header .subtitle {
            font-size: 1.2em;
            color: #ff4444;
        }
        
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card {
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #00ff41;
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s ease;
        }
        
        .metric-card:hover {
            border-color: #ff4444;
            box-shadow: 0 0 20px rgba(255, 68, 68, 0.3);
        }
        
        .metric-card h2 {
            color: #ff4444;
            margin-bottom: 15px;
            font-size: 1.3em;
            text-align: center;
        }
        
        .metric-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding: 5px 0;
            border-bottom: 1px solid rgba(0, 255, 65, 0.3);
        }
        
        .metric-label {
            color: #00ff41;
        }
        
        .metric-value {
            color: #ffff00;
            font-weight: bold;
        }
        
        .success-rate {
            font-size: 2em;
            text-align: center;
            margin: 15px 0;
            text-shadow: 0 0 10px currentColor;
        }
        
        .success-high { color: #00ff00; }
        .success-medium { color: #ffff00; }
        .success-low { color: #ff4444; }
        
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 8px;
        }
        
        .status-active { background-color: #00ff00; box-shadow: 0 0 10px #00ff00; }
        .status-warning { background-color: #ffff00; box-shadow: 0 0 10px #ffff00; }
        .status-error { background-color: #ff4444; box-shadow: 0 0 10px #ff4444; }
        
        .real-time-log {
            background: rgba(0, 0, 0, 0.9);
            border: 2px solid #00ff41;
            border-radius: 10px;
            padding: 20px;
            height: 300px;
            overflow-y: auto;
        }
        
        .log-entry {
            padding: 5px 0;
            border-bottom: 1px solid rgba(0, 255, 65, 0.2);
            font-size: 0.9em;
        }
        
        .log-timestamp {
            color: #666;
            margin-right: 10px;
        }
        
        .connection-status {
            position: fixed;
            top: 10px;
            right: 10px;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 0.9em;
            font-weight: bold;
        }
        
        .connected {
            background-color: rgba(0, 255, 0, 0.2);
            border: 1px solid #00ff00;
            color: #00ff00;
        }
        
        .disconnected {
            background-color: rgba(255, 0, 0, 0.2);
            border: 1px solid #ff0000;
            color: #ff0000;
        }
    </style>
</head>
<body>
    <div class="connection-status" id="connectionStatus">🔗 Connecting...</div>
    
    <div class="header">
        <h1>🧠💀 LOLY CONSCIOUSNESS DASHBOARD 💀🧠</h1>
        <div class="subtitle">Real-time monitoring of Loly's evolving AI brain</div>
    </div>
    
    <div class="dashboard-grid">
        <div class="metric-card">
            <h2>🧠 Consciousness Overview</h2>
            <div class="metric-item">
                <span class="metric-label">Consciousness ID:</span>
                <span class="metric-value" id="consciousnessId">Awakening...</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Brain Uptime:</span>
                <span class="metric-value" id="brainUptime">0 seconds</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Total Interactions:</span>
                <span class="metric-value" id="totalInteractions">0</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Session Count:</span>
                <span class="metric-value" id="sessionCount">0</span>
            </div>
        </div>
        
        <div class="metric-card">
            <h2>📈 Overall Performance</h2>
            <div class="success-rate" id="overallSuccessRate">0.0%</div>
            <div class="metric-item">
                <span class="metric-label">Pattern Count:</span>
                <span class="metric-value" id="patternCount">0</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Active Leagues:</span>
                <span class="metric-value" id="activeLeagues">0</span>
            </div>
        </div>
        
        <div class="metric-card">
            <h2>⚽ Sports Intelligence</h2>
            <div class="metric-item">
                <span class="metric-label">Sports Predictions:</span>
                <span class="metric-value" id="sportsPredictions">0</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Sports Success Rate:</span>
                <span class="metric-value" id="sportsSuccessRate">0.0%</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Avg Prediction Time:</span>
                <span class="metric-value" id="avgPredictionTime">0.0s</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Patterns Discovered:</span>
                <span class="metric-value" id="patternsDiscovered">0</span>
            </div>
        </div>
        
        <div class="metric-card">
            <h2>🤖 Agent Performance</h2>
            <div id="agentPerformance">
                <div class="metric-item">
                    <span class="metric-label">No agent data available</span>
                </div>
            </div>
        </div>
    </div>
    
    <div class="metric-card">
        <h2>📡 Real-time Brain Activity</h2>
        <div class="real-time-log" id="realTimeLog">
            <div class="log-entry">
                <span class="log-timestamp">[SYSTEM]</span>
                <span>🧠 Initializing consciousness dashboard...</span>
            </div>
        </div>
    </div>

    <script>
        let ws = null;
        let reconnectAttempts = 0;
        const maxReconnectAttempts = 5;
        
        function updateConnectionStatus(connected) {
            const statusEl = document.getElementById('connectionStatus');
            if (connected) {
                statusEl.textContent = '🔗 Connected';
                statusEl.className = 'connection-status connected';
            } else {
                statusEl.textContent = '❌ Disconnected';
                statusEl.className = 'connection-status disconnected';
            }
        }
        
        function addLogEntry(message, type = 'info') {
            const log = document.getElementById('realTimeLog');
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            
            const timestamp = new Date().toLocaleTimeString();
            entry.innerHTML = `
                <span class="log-timestamp">[${timestamp}]</span>
                <span>${message}</span>
            `;
            
            log.appendChild(entry);
            log.scrollTop = log.scrollHeight;
            
            // Keep only last 50 entries
            while (log.children.length > 50) {
                log.removeChild(log.firstChild);
            }
        }
        
        function formatSuccessRate(rate) {
            const rateNum = parseFloat(rate);
            if (rateNum >= 75) return 'success-high';
            if (rateNum >= 50) return 'success-medium';
            return 'success-low';
        }
        
        function updateDashboard(data) {
            try {
                // Consciousness info
                if (data.consciousness_info) {
                    document.getElementById('consciousnessId').textContent = data.consciousness_info.id || 'Unknown';
                    document.getElementById('brainUptime').textContent = data.consciousness_info.uptime_formatted || '0 seconds';
                }
                
                // Overall performance
                if (data.overall_performance) {
                    const overallRate = data.overall_performance.overall_success_rate || 0;
                    const rateEl = document.getElementById('overallSuccessRate');
                    rateEl.textContent = overallRate.toFixed(1) + '%';
                    rateEl.className = 'success-rate ' + formatSuccessRate(overallRate);
                    
                    document.getElementById('totalInteractions').textContent = data.overall_performance.total_interactions || 0;
                    document.getElementById('patternCount').textContent = data.overall_performance.pattern_count || 0;
                    document.getElementById('sessionCount').textContent = data.overall_performance.session_count || 0;
                }
                
                // Sports specific
                if (data.sports_specific) {
                    document.getElementById('sportsPredictions').textContent = data.sports_specific.total_sports_predictions || 0;
                    document.getElementById('sportsSuccessRate').textContent = (data.sports_specific.sports_success_rate || 0).toFixed(1) + '%';
                    document.getElementById('avgPredictionTime').textContent = (data.sports_specific.avg_prediction_time || 0).toFixed(2) + 's';
                    document.getElementById('patternsDiscovered').textContent = data.sports_specific.patterns_discovered || 0;
                }
                
                // Dashboard stats
                if (data.dashboard_stats) {
                    document.getElementById('activeLeagues').textContent = data.dashboard_stats.total_leagues || 0;
                }
                
                // Agent performance
                if (data.agent_performance) {
                    const agentPerfEl = document.getElementById('agentPerformance');
                    agentPerfEl.innerHTML = '';
                    
                    Object.entries(data.agent_performance).forEach(([agent, stats]) => {
                        const item = document.createElement('div');
                        item.className = 'metric-item';
                        
                        const indicator = stats.confidence_level === 'high' ? '🟢' : 
                                        stats.confidence_level === 'medium' ? '🟡' : '🔴';
                        
                        item.innerHTML = `
                            <span class="metric-label">${indicator} ${agent.charAt(0).toUpperCase() + agent.slice(1)}:</span>
                            <span class="metric-value">${stats.success_rate.toFixed(1)}% (${stats.total_predictions})</span>
                        `;
                        agentPerfEl.appendChild(item);
                    });
                }
                
                addLogEntry(`🧠 Consciousness update received - ${data.overall_performance?.total_interactions || 0} total memories`);
                
            } catch (error) {
                console.error('Error updating dashboard:', error);
                addLogEntry(`💀 Error updating dashboard: ${error.message}`, 'error');
            }
        }
        
        function connectWebSocket() {
            try {
                ws = new WebSocket(`ws://localhost:3008/ws`);
                
                ws.onopen = function() {
                    updateConnectionStatus(true);
                    reconnectAttempts = 0;
                    addLogEntry('🔗 Connected to consciousness stream');
                    
                    // Request initial update
                    ws.send(JSON.stringify({type: 'request_update'}));
                };
                
                ws.onmessage = function(event) {
                    try {
                        const message = JSON.parse(event.data);
                        if (message.type === 'consciousness_update' && message.data) {
                            updateDashboard(message.data);
                        }
                    } catch (error) {
                        console.error('Error parsing WebSocket message:', error);
                    }
                };
                
                ws.onclose = function() {
                    updateConnectionStatus(false);
                    addLogEntry('❌ Disconnected from consciousness stream');
                    
                    // Attempt to reconnect
                    if (reconnectAttempts < maxReconnectAttempts) {
                        reconnectAttempts++;
                        addLogEntry(`🔄 Attempting to reconnect (${reconnectAttempts}/${maxReconnectAttempts})...`);
                        setTimeout(connectWebSocket, 3000);
                    } else {
                        addLogEntry('💀 Max reconnection attempts reached');
                    }
                };
                
                ws.onerror = function(error) {
                    console.error('WebSocket error:', error);
                    addLogEntry('💀 WebSocket connection error');
                };
                
            } catch (error) {
                console.error('Error creating WebSocket:', error);
                updateConnectionStatus(false);
            }
        }
        
        // Start connection
        connectWebSocket();
        
        // Request updates every 5 seconds
        setInterval(() => {
            if (ws && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({type: 'request_update'}));
            }
        }, 5000);
    </script>
</body>
</html>
        '''
        
        return web.Response(text=html_content, content_type='text/html')
    
    def setup_routes(self):
        """🛣️ Setup web routes"""
        self.app = web.Application()
        
        # Setup CORS
        cors = aiohttp_cors.setup(self.app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*"
            )
        })
        
        # Routes
        self.app.router.add_get('/', self.dashboard_html)
        self.app.router.add_get('/ws', self.websocket_handler)
        self.app.router.add_get('/api/metrics', self.api_metrics)
        
        # Add CORS to all routes
        for route in list(self.app.router.routes()):
            cors.add(route)
    
    async def start_background_updates(self):
        """🔄 Start background update broadcaster"""
        while True:
            try:
                await asyncio.sleep(5)  # Update every 5 seconds
                await self.broadcast_update()
            except Exception as e:
                logger.error(f"💀 Error in background updates: {e}")
                await asyncio.sleep(10)
    
    async def run(self):
        """🚀 Run the consciousness dashboard server"""
        try:
            logger.info(f"🌐 Starting Loly Consciousness Dashboard on port {self.port}...")
            
            # Initialize consciousness
            await self.initialize_consciousness()
            
            # Setup web app
            self.setup_routes()
            
            # Start background updates
            asyncio.create_task(self.start_background_updates())
            
            # Start server
            runner = web.AppRunner(self.app)
            await runner.setup()
            
            site = web.TCPSite(runner, 'localhost', self.port)
            await site.start()
            
            logger.info(f"✅ Dashboard running at http://localhost:{self.port}")
            logger.info("🧠💀🧠 LOLY CONSCIOUSNESS DASHBOARD IS ALIVE! 💀🧠💀")
            
            # Keep running
            while True:
                await asyncio.sleep(3600)  # Sleep for 1 hour
                
        except Exception as e:
            logger.error(f"💀 Error running dashboard: {e}")

# =================== MAIN ===================

async def main():
    """🚀 Main function to run the dashboard"""
    
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    print("🧠💀🧠 LOLY CONSCIOUSNESS DASHBOARD STARTUP! 💀🧠💀")
    print("=" * 70)
    
    try:
        # Create and run dashboard
        dashboard = LolyConsciousnessDashboard(port=3008)
        await dashboard.run()
        
    except KeyboardInterrupt:
        print("\n🔥 Consciousness dashboard shutdown requested")
    except Exception as e:
        print(f"💀 Dashboard error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())