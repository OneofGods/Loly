#!/usr/bin/env python3
"""
LOLY Troubleshoot MCP - Standalone troubleshooting system for LOLY

This MCP provides troubleshooting capabilities without external dependencies:
- League addition troubleshooting
- MCP server connectivity issues
- Port conflicts resolution
- Service health checks
- Configuration validation
"""

import os
import argparse
import logging
import json
import subprocess
import socket
from datetime import datetime
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("loly-troubleshoot-mcp")

# Create FastAPI app
app = FastAPI(title="LOLY Troubleshoot MCP", description="Standalone troubleshooting system for LOLY")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class TroubleshootRequest(BaseModel):
    """Request model for troubleshooting."""
    issue_type: str = Field(..., description="Type of issue (connectivity, league, mcp, port, config)")
    description: str = Field(..., description="Description of the issue")
    component: Optional[str] = Field(None, description="Component having issues")
    port: Optional[int] = Field(None, description="Port number if relevant")
    service_name: Optional[str] = Field(None, description="Service name if relevant")
    error_messages: Optional[List[str]] = Field(None, description="Error messages")

class TroubleshootResponse(BaseModel):
    """Response model for troubleshooting."""
    diagnosis: str = Field(..., description="Diagnosis of the issue")
    solutions: List[str] = Field(..., description="List of solutions")
    commands: Optional[List[str]] = Field(None, description="Commands to run")
    status: str = Field(..., description="Status of troubleshooting")

class HealthCheckRequest(BaseModel):
    """Request model for health checks."""
    services: List[str] = Field(..., description="List of services to check")
    ports: Optional[List[int]] = Field(None, description="List of ports to check")

class HealthCheckResponse(BaseModel):
    """Response model for health checks."""
    results: Dict[str, Any] = Field(..., description="Health check results")
    overall_status: str = Field(..., description="Overall health status")

class LeagueAddRequest(BaseModel):
    """Request model for adding new leagues."""
    league_name: str = Field(..., description="Name of the league to add")
    sport_type: str = Field(..., description="Type of sport")
    api_endpoint: Optional[str] = Field(None, description="API endpoint for league data")
    data_format: Optional[str] = Field(None, description="Expected data format")

class LeagueAddResponse(BaseModel):
    """Response model for league addition."""
    status: str = Field(..., description="Status of league addition")
    steps: List[str] = Field(..., description="Steps taken")
    mcp_file: Optional[str] = Field(None, description="Generated MCP file path")
    recommendations: List[str] = Field(..., description="Recommendations")

# Utility functions
def check_port_availability(port: int) -> bool:
    """Check if a port is available."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return True
    except OSError:
        return False

def get_process_on_port(port: int) -> Optional[str]:
    """Get the process running on a specific port."""
    try:
        result = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                return lines[1]  # First process line
    except Exception:
        pass
    return None

def check_service_health(port: int) -> Dict[str, Any]:
    """Check if a service is healthy on a given port."""
    try:
        import requests
        response = requests.get(f'http://localhost:{port}/health', timeout=5)
        return {
            'status': 'healthy' if response.status_code == 200 else 'unhealthy',
            'response_code': response.status_code,
            'response_data': response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
        }
    except Exception as e:
        return {
            'status': 'unreachable',
            'error': str(e)
        }

def find_available_port(start_port: int = 3210) -> int:
    """Find an available port starting from start_port."""
    port = start_port
    while port < start_port + 100:
        if check_port_availability(port):
            return port
        port += 1
    return -1

# API Endpoints
@app.get("/health")
async def health_check():
    """Check the health of the troubleshooting service."""
    return {
        "status": "healthy", 
        "service": "LOLY Troubleshoot MCP", 
        "timestamp": datetime.now().isoformat(),
        "capabilities": ["troubleshoot", "health_check", "league_add", "port_scan"]
    }

@app.post("/troubleshoot", response_model=TroubleshootResponse)
async def troubleshoot_issue(request: TroubleshootRequest):
    """Troubleshoot various types of issues."""
    logger.info(f"Troubleshooting {request.issue_type} issue: {request.description}")
    
    diagnosis = ""
    solutions = []
    commands = []
    
    if request.issue_type == "connectivity":
        diagnosis = f"Connectivity issue detected: {request.description}"
        if request.port:
            port_available = check_port_availability(request.port)
            process_info = get_process_on_port(request.port)
            
            if not port_available and process_info:
                diagnosis += f" Port {request.port} is occupied by: {process_info}"
                solutions.extend([
                    f"Stop the process using port {request.port}",
                    f"Use a different port for your service",
                    f"Check if the service on port {request.port} is the one you expect"
                ])
                commands.extend([
                    f"lsof -i :{request.port}",
                    f"kill -9 $(lsof -t -i:{request.port})"
                ])
            elif port_available:
                diagnosis += f" Port {request.port} is available"
                solutions.extend([
                    "Start your service on this port",
                    "Check if your service configuration is correct"
                ])
    
    elif request.issue_type == "league":
        diagnosis = f"League addition issue: {request.description}"
        solutions.extend([
            "Check if the league API endpoint is accessible",
            "Verify the data format matches expected structure",
            "Create a new MCP server for the league",
            "Add the league to the registry",
            "Test the MCP server endpoints"
        ])
        commands.extend([
            "curl -s [API_ENDPOINT]/health",
            "python3 new_league_mcp.py --port [PORT]"
        ])
    
    elif request.issue_type == "mcp":
        diagnosis = f"MCP server issue: {request.description}"
        if request.service_name:
            # Check if MCP service is running
            available_port = find_available_port()
            solutions.extend([
                f"Restart the {request.service_name} MCP server",
                f"Check MCP server logs for errors",
                f"Use port {available_port} if current port is occupied",
                "Verify MCP server dependencies are installed"
            ])
            commands.extend([
                f"python3 {request.service_name}.py --port {available_port}",
                f"curl http://localhost:{available_port}/health"
            ])
    
    elif request.issue_type == "port":
        diagnosis = f"Port conflict issue: {request.description}"
        if request.port:
            available_port = find_available_port(request.port + 1)
            solutions.extend([
                f"Use port {available_port} instead of {request.port}",
                f"Stop the service using port {request.port}",
                "Check port allocation in your configuration"
            ])
            commands.extend([
                f"lsof -i :{request.port}",
                f"netstat -tulpn | grep {request.port}"
            ])
    
    else:
        diagnosis = f"General issue: {request.description}"
        solutions.extend([
            "Check service logs for detailed error information",
            "Verify all dependencies are installed",
            "Restart the affected service",
            "Check configuration files for syntax errors"
        ])
    
    return TroubleshootResponse(
        diagnosis=diagnosis,
        solutions=solutions,
        commands=commands,
        status="analyzed"
    )

@app.post("/health_check", response_model=HealthCheckResponse)
async def perform_health_check(request: HealthCheckRequest):
    """Perform health checks on specified services."""
    logger.info(f"Performing health check on services: {request.services}")
    
    results = {}
    overall_healthy = True
    
    # Check ports if provided
    if request.ports:
        for port in request.ports:
            port_available = check_port_availability(port)
            process_info = get_process_on_port(port) if not port_available else None
            health_info = check_service_health(port) if not port_available else None
            
            results[f"port_{port}"] = {
                "available": port_available,
                "process": process_info,
                "health": health_info
            }
            
            if port_available and f"port_{port}" in request.services:
                overall_healthy = False
    
    # Check known LOLY services
    loly_services = {
        "loly_chat": 3008,
        "loly_builder": 3209,
        "loly_troubleshoot": 3210
    }
    
    for service in request.services:
        if service in loly_services:
            port = loly_services[service]
            health_info = check_service_health(port)
            results[service] = health_info
            
            if health_info.get('status') != 'healthy':
                overall_healthy = False
    
    return HealthCheckResponse(
        results=results,
        overall_status="healthy" if overall_healthy else "issues_detected"
    )

@app.post("/add_league", response_model=LeagueAddResponse)
async def add_new_league(request: LeagueAddRequest):
    """Help add a new league to LOLY's capabilities."""
    logger.info(f"Adding new league: {request.league_name} ({request.sport_type})")
    
    steps = []
    recommendations = []
    mcp_file = None
    
    # Generate MCP filename
    safe_name = request.league_name.lower().replace(' ', '_').replace('-', '_')
    mcp_file = f"{safe_name}_mcp.py"
    
    steps.extend([
        f"Generated MCP filename: {mcp_file}",
        f"Identified sport type: {request.sport_type}",
        "Ready to create MCP server template"
    ])
    
    if request.api_endpoint:
        steps.append(f"API endpoint provided: {request.api_endpoint}")
        recommendations.extend([
            f"Test API endpoint accessibility: curl {request.api_endpoint}",
            "Verify API response format matches expected structure",
            "Check API rate limits and authentication requirements"
        ])
    
    recommendations.extend([
        f"Create {mcp_file} using existing MCP templates",
        f"Add {request.league_name} to leagues_registry.py",
        f"Test the new MCP server on an available port",
        "Update LOLY's configuration to include the new league",
        "Verify integration with existing sports data pipeline"
    ])
    
    return LeagueAddResponse(
        status="ready_to_implement",
        steps=steps,
        mcp_file=mcp_file,
        recommendations=recommendations
    )

# Main function
def main():
    parser = argparse.ArgumentParser(description="LOLY Troubleshoot MCP")
    parser.add_argument("--host", type=str, default="localhost", help="Host to bind to")
    parser.add_argument("--port", type=int, default=3210, help="Port to bind to")
    parser.add_argument("--log-level", type=str, default="INFO", help="Logging level")

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Start the server
    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port)

if __name__ == "__main__":
    main()