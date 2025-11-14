#!/usr/bin/env python3
"""
🔥💀 AGENT SYSTEM DEPLOYMENT - LIVE AUTONOMOUS EXECUTION 💀🔥
Agent Poly Loly Double Zero: Real Multi-Agent System Deployment

DEPLOYMENT FEATURES:
- Complete autonomous agent system launch
- Real-time sports data processing
- Multi-agent coordination and workflows
- System health monitoring and recovery
- Performance metrics and optimization
"""

import asyncio
import json
import logging
import signal
import sys
import time
from datetime import datetime
from typing import Dict, Any

# Import core system components
from core.agent_orchestrator import launch_multi_agent_system, AgentOrchestrator

# Configure system logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/agent_system.log')
    ]
)
logger = logging.getLogger(__name__)

class AgentSystemDeployment:
    """🚀 Complete agent system deployment manager"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or self._get_default_config()
        self.orchestrator = None
        self.running = False
        self.start_time = None
        
    def _get_default_config(self) -> Dict[str, Any]:
        """📋 Get default system configuration"""
        return {
            'system_name': 'Poly Loly Agent System',
            'max_agents': 8,
            'min_agents': 5,
            'auto_scaling': True,
            'scaling_threshold': 0.75,
            'health_check_interval': 30,
            'performance_monitoring': True,
            'fault_tolerance': True,
            'log_level': 'INFO'
        }
    
    async def deploy_system(self):
        """🚀 Deploy the complete agent system"""
        try:
            logger.info(f"🚀 Deploying {self.config['system_name']}")
            logger.info(f"📋 Configuration: {json.dumps(self.config, indent=2)}")
            
            # Launch multi-agent system
            self.orchestrator = await launch_multi_agent_system(self.config)
            
            if not self.orchestrator:
                raise Exception("Failed to launch multi-agent system")
            
            self.running = True
            self.start_time = datetime.now()
            
            logger.info("✅ Agent system deployed successfully!")
            logger.info(f"🎯 System ID: {self.orchestrator.system_id}")
            logger.info(f"🤖 Active agents: {len(self.orchestrator.active_agents)}")
            
            # Start deployment monitoring
            await self._start_deployment_monitoring()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ System deployment failed: {e}")
            return False
    
    async def _start_deployment_monitoring(self):
        """📊 Start deployment monitoring tasks"""
        # Start monitoring tasks
        monitoring_tasks = [
            asyncio.create_task(self._system_health_monitoring()),
            asyncio.create_task(self._performance_monitoring()),
            asyncio.create_task(self._status_reporting()),
            asyncio.create_task(self._workflow_demonstrations())
        ]
        
        logger.info("📊 Deployment monitoring started")
        
        # Wait for monitoring tasks
        await asyncio.gather(*monitoring_tasks, return_exceptions=True)
    
    async def _system_health_monitoring(self):
        """💚 Continuous system health monitoring"""
        while self.running:
            try:
                if self.orchestrator:
                    status = await self.orchestrator.get_system_status()
                    
                    # Log health summary
                    healthy_ratio = status['healthy_agents'] / max(status['active_agents'], 1)
                    
                    if healthy_ratio < 0.8:
                        logger.warning(f"⚠️ System health degraded: {healthy_ratio:.1%} healthy agents")
                    
                    # Check for critical issues
                    if status['system_state'] == 'error':
                        logger.critical("🚨 System in error state!")
                    elif status['system_state'] == 'degraded':
                        logger.warning("⚠️ System performance degraded")
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"❌ Health monitoring error: {e}")
                await asyncio.sleep(30)
    
    async def _performance_monitoring(self):
        """📈 Continuous performance monitoring"""
        while self.running:
            try:
                if self.orchestrator:
                    performance = await self.orchestrator.get_performance_metrics()
                    
                    if performance and 'current_performance' in performance:
                        current = performance['current_performance']
                        
                        # Safe performance metrics logging
                        try:
                            active_agents = current.get('active_agents', 0)
                            response_time = current.get('average_response_time', 0)
                            error_rate = current.get('error_rate', 0)
                            
                            # Ensure numeric values
                            response_time = float(response_time) if response_time is not None else 0.0
                            error_rate = float(error_rate) if error_rate is not None else 0.0
                            
                            logger.info(f"📈 Performance: {active_agents} agents, "
                                      f"response time: {response_time:.2f}s, "
                                      f"error rate: {error_rate:.1%}")
                        except (TypeError, ValueError) as e:
                            logger.debug(f"📈 Performance metrics formatting error: {e}")
                
                await asyncio.sleep(120)  # Check every 2 minutes
                
            except Exception as e:
                logger.error(f"❌ Performance monitoring error: {e}")
                await asyncio.sleep(120)
    
    async def _status_reporting(self):
        """📊 Periodic status reporting"""
        while self.running:
            try:
                if self.orchestrator:
                    # Get comprehensive status
                    system_status = await self.orchestrator.get_system_status()
                    agent_details = await self.orchestrator.get_agent_details()
                    
                    # Calculate uptime
                    uptime = datetime.now() - self.start_time if self.start_time else timedelta(0)
                    
                    # Generate status report
                    logger.info("=" * 60)
                    logger.info(f"🎯 AGENT SYSTEM STATUS REPORT")
                    logger.info(f"⏱️  Uptime: {uptime}")
                    logger.info(f"🤖 Active Agents: {system_status['active_agents']}")
                    logger.info(f"💚 Healthy Agents: {system_status['healthy_agents']}")
                    logger.info(f"🏃 System State: {system_status['system_state']}")
                    
                    # Agent breakdown
                    breakdown = system_status.get('agent_breakdown', {})
                    for agent_type, count in breakdown.items():
                        if count > 0:
                            logger.info(f"   {agent_type}: {count} agents")
                    
                    # Performance summary with safe formatting
                    perf = system_status.get('performance_summary', {})
                    try:
                        avg_time = float(perf.get('average_response_time', 0)) if perf.get('average_response_time') is not None else 0.0
                        error_rate = float(perf.get('error_rate', 0)) if perf.get('error_rate') is not None else 0.0
                        tasks = int(perf.get('total_tasks_processed', 0))
                        
                        logger.info(f"📈 Avg Response Time: {avg_time:.2f}s")
                        logger.info(f"❌ Error Rate: {error_rate:.1%}")
                        logger.info(f"📋 Tasks Processed: {tasks}")
                    except (TypeError, ValueError) as e:
                        logger.debug(f"📊 Status report formatting error: {e}")
                    logger.info("=" * 60)
                
                await asyncio.sleep(300)  # Report every 5 minutes
                
            except Exception as e:
                logger.error(f"❌ Status reporting error: {e}")
                await asyncio.sleep(300)
    
    async def _workflow_demonstrations(self):
        """🔄 Demonstrate system workflows"""
        demonstration_count = 0
        
        while self.running and demonstration_count < 3:  # Limit demonstrations
            try:
                await asyncio.sleep(60)  # Wait 1 minute before first demo
                
                if self.orchestrator:
                    logger.info(f"🎯 Starting workflow demonstration #{demonstration_count + 1}")
                    
                    # Trigger sports analysis workflow
                    workflow_id = await self.orchestrator.trigger_workflow('sports_analysis', {
                        'sport': 'NFL',
                        'analysis_depth': 'standard'
                    })
                    
                    if workflow_id:
                        logger.info(f"✅ Triggered sports analysis workflow: {workflow_id}")
                        
                        # Wait for workflow completion
                        await asyncio.sleep(30)
                        
                        # Check workflow status
                        logger.info(f"🔍 Workflow {workflow_id} processing...")
                        
                    demonstration_count += 1
                    
                    # Wait before next demonstration
                    await asyncio.sleep(180)  # 3 minutes between demos
                
            except Exception as e:
                logger.error(f"❌ Workflow demonstration error: {e}")
                await asyncio.sleep(60)
    
    async def shutdown_system(self):
        """🛑 Gracefully shutdown the system"""
        try:
            logger.info("🛑 Initiating system shutdown...")
            self.running = False
            
            if self.orchestrator:
                await self.orchestrator.shutdown_system()
                
            # Calculate final stats
            if self.start_time:
                total_uptime = datetime.now() - self.start_time
                logger.info(f"📊 Total system uptime: {total_uptime}")
            
            logger.info("✅ System shutdown completed successfully")
            
        except Exception as e:
            logger.error(f"❌ Error during shutdown: {e}")

# =================== SIGNAL HANDLING ===================

deployment = None

def signal_handler(signum, frame):
    """Handle shutdown signals"""
    logger.info(f"📡 Received signal {signum}, initiating graceful shutdown...")
    
    if deployment:
        # Schedule shutdown
        asyncio.create_task(deployment.shutdown_system())
    
    sys.exit(0)

# =================== MAIN DEPLOYMENT ===================

async def main():
    """🚀 Main deployment function"""
    global deployment
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create deployment configuration
    config = {
        'system_name': 'Poly Loly Agent System - Production',
        'max_agents': 10,
        'min_agents': 5,
        'auto_scaling': True,
        'scaling_threshold': 0.8,
        'health_check_interval': 30,
        'performance_monitoring': True,
        'fault_tolerance': True
    }
    
    # Create deployment instance
    deployment = AgentSystemDeployment(config)
    
    try:
        # Deploy the system
        success = await deployment.deploy_system()
        
        if success:
            logger.info("🎉 Agent system deployment successful!")
            logger.info("🔄 System running... Press Ctrl+C to shutdown")
            
            # Keep the system running
            while deployment.running:
                await asyncio.sleep(1)
        else:
            logger.error("❌ Agent system deployment failed!")
            return 1
    
    except KeyboardInterrupt:
        logger.info("📡 Keyboard interrupt received")
    except Exception as e:
        logger.error(f"❌ Deployment error: {e}")
        return 1
    finally:
        if deployment:
            await deployment.shutdown_system()
    
    return 0

if __name__ == "__main__":
    # Ensure logs directory exists
    import os
    os.makedirs('logs', exist_ok=True)
    
    logger.info("🔥💀 POLY LOLY AGENT SYSTEM - STARTING DEPLOYMENT 💀🔥")
    
    # Run the deployment
    exit_code = asyncio.run(main())
    
    logger.info(f"🏁 Agent system deployment finished with exit code: {exit_code}")
    sys.exit(exit_code)