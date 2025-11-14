#!/usr/bin/env python3
"""
Builder Agent MCP - Model Control Protocol for the Builder Agent

This MCP provides endpoints for the Builder Agent's functionality:
- Building websites
- Troubleshooting technical issues
- Optimizing performance
- Fixing connectivity issues
- Creating API endpoints
- Creating database schemas
"""

import os
import argparse
import logging
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("builder-agent-mcp")

# Get BLOOM service URL from environment variable or use default
BLOOM_SERVICE_URL = os.environ.get("BLOOM_SERVICE_URL", "http://localhost:8000")

# Create FastAPI app
app = FastAPI(title="Builder Agent MCP", description="Model Control Protocol for the Builder Agent")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class WebsiteRequest(BaseModel):
    """Request model for website building."""
    business_type: str = Field(..., description="Type of business (restaurant, retail, service, etc.)")
    name: str = Field(..., description="Business name")
    features: List[str] = Field(default_factory=list, description="Desired website features")
    design_preferences: Optional[Dict[str, Any]] = Field(None, description="Design preferences")
    content_details: Optional[Dict[str, Any]] = Field(None, description="Content details")
    technical_requirements: Optional[Dict[str, Any]] = Field(None, description="Technical requirements")

class WebsiteResponse(BaseModel):
    """Response model for website building."""
    website_plan: str = Field(..., description="Website plan overview")
    architecture: Dict[str, Any] = Field(..., description="Website architecture")
    technology_stack: Dict[str, Any] = Field(..., description="Recommended technology stack")
    implementation_steps: List[str] = Field(..., description="Implementation steps")
    estimated_timeline: str = Field(..., description="Estimated timeline")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the website plan")

class TroubleshootRequest(BaseModel):
    """Request model for troubleshooting technical issues."""
    issue_type: str = Field(..., description="Type of issue (connectivity, performance, error, etc.)")
    description: str = Field(..., description="Detailed description of the issue")
    system_details: Optional[Dict[str, Any]] = Field(None, description="System details")
    error_messages: Optional[List[str]] = Field(None, description="Error messages")
    steps_taken: Optional[List[str]] = Field(None, description="Steps already taken to resolve the issue")

class TroubleshootResponse(BaseModel):
    """Response model for troubleshooting technical issues."""
    diagnosis: str = Field(..., description="Issue diagnosis")
    root_causes: List[str] = Field(..., description="Potential root causes")
    solutions: List[Dict[str, Any]] = Field(..., description="Recommended solutions")
    prevention: List[str] = Field(..., description="Prevention measures")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the troubleshooting")

class OptimizationRequest(BaseModel):
    """Request model for performance optimization."""
    system_type: str = Field(..., description="Type of system to optimize (website, database, API, etc.)")
    current_performance: str = Field(..., description="Description of current performance")
    performance_goals: List[str] = Field(..., description="Performance goals")
    system_details: Optional[Dict[str, Any]] = Field(None, description="System details")
    constraints: Optional[List[str]] = Field(None, description="Constraints to consider")

class OptimizationResponse(BaseModel):
    """Response model for performance optimization."""
    assessment: str = Field(..., description="Performance assessment")
    bottlenecks: List[str] = Field(..., description="Identified bottlenecks")
    optimization_plan: Dict[str, Any] = Field(..., description="Optimization plan")
    expected_improvements: Dict[str, Any] = Field(..., description="Expected improvements")
    implementation_steps: List[str] = Field(..., description="Implementation steps")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the optimization")

class ConnectivityRequest(BaseModel):
    """Request model for fixing connectivity issues."""
    component_a: str = Field(..., description="First component with connectivity issue")
    component_b: str = Field(..., description="Second component with connectivity issue")
    issue_description: str = Field(..., description="Description of the connectivity issue")
    current_configuration: Optional[Dict[str, Any]] = Field(None, description="Current configuration details")
    error_messages: Optional[List[str]] = Field(None, description="Error messages")

class ConnectivityResponse(BaseModel):
    """Response model for fixing connectivity issues."""
    diagnosis: str = Field(..., description="Connectivity issue diagnosis")
    solution: str = Field(..., description="Recommended solution")
    configuration_changes: Dict[str, Any] = Field(..., description="Required configuration changes")
    testing_steps: List[str] = Field(..., description="Testing steps to verify the fix")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the connectivity fix")

class ApiEndpointRequest(BaseModel):
    """Request model for creating API endpoints."""
    purpose: str = Field(..., description="Purpose of the API endpoint")
    functionality: str = Field(..., description="Functionality description")
    data_model: Optional[Dict[str, Any]] = Field(None, description="Data model")
    authentication: Optional[str] = Field(None, description="Authentication requirements")
    performance_requirements: Optional[Dict[str, Any]] = Field(None, description="Performance requirements")

class ApiEndpointResponse(BaseModel):
    """Response model for creating API endpoints."""
    endpoint_design: Dict[str, Any] = Field(..., description="API endpoint design")
    implementation_code: str = Field(..., description="Implementation code")
    testing_strategy: Dict[str, Any] = Field(..., description="Testing strategy")
    documentation: str = Field(..., description="API documentation")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the API endpoint")

class DatabaseSchemaRequest(BaseModel):
    """Request model for creating database schemas."""
    database_type: str = Field(..., description="Type of database (SQL, NoSQL, etc.)")
    purpose: str = Field(..., description="Purpose of the database")
    entities: List[Dict[str, Any]] = Field(..., description="Entities to be stored")
    relationships: Optional[List[Dict[str, Any]]] = Field(None, description="Relationships between entities")
    performance_requirements: Optional[Dict[str, Any]] = Field(None, description="Performance requirements")

class DatabaseSchemaResponse(BaseModel):
    """Response model for creating database schemas."""
    schema_design: Dict[str, Any] = Field(..., description="Database schema design")
    implementation_code: str = Field(..., description="Implementation code")
    optimization_recommendations: List[str] = Field(..., description="Optimization recommendations")
    migration_strategy: Optional[Dict[str, Any]] = Field(None, description="Migration strategy")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the database schema")

# API Endpoints
@app.get("/health")
async def health_check():
    """Check the health of the service."""
    return {"status": "healthy", "service": "Builder Agent MCP", "timestamp": datetime.now().isoformat()}

@app.post("/build-website", response_model=WebsiteResponse)
async def build_website(request: WebsiteRequest):
    """Build a website based on the request."""
    logger.info(f"Received request to build website for: {request.name}")

    # Construct prompt for the BLOOM service
    prompt = construct_website_prompt(request)

    try:
        # Call BLOOM service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BLOOM_SERVICE_URL}/text_generation",
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.error(f"BLOOM service returned status code {response.status_code}")
                raise HTTPException(status_code=500, detail="Error calling BLOOM service")

            result = response.json()
            website_text = result.get("generated_text", "")

            # Process the website plan
            website_data = process_website_plan(website_text, request)

            return WebsiteResponse(
                website_plan=website_data["website_plan"],
                architecture=website_data["architecture"],
                technology_stack=website_data["technology_stack"],
                implementation_steps=website_data["implementation_steps"],
                estimated_timeline=website_data["estimated_timeline"],
                metadata={
                    "business_type": request.business_type,
                    "business_name": request.name,
                    "requested_features": request.features,
                    "timestamp": datetime.now().isoformat()
                }
            )
    except Exception as e:
        logger.error(f"Error building website: {e}")
        raise HTTPException(status_code=500, detail=f"Error building website: {str(e)}")

@app.post("/troubleshoot", response_model=TroubleshootResponse)
async def troubleshoot_issue(request: TroubleshootRequest):
    """Troubleshoot a technical issue based on the request."""
    logger.info(f"Received request to troubleshoot issue: {request.issue_type}")

    # Construct prompt for the BLOOM service
    prompt = construct_troubleshoot_prompt(request)

    try:
        # Call BLOOM service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BLOOM_SERVICE_URL}/text_generation",
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.error(f"BLOOM service returned status code {response.status_code}")
                raise HTTPException(status_code=500, detail="Error calling BLOOM service")

            result = response.json()
            troubleshoot_text = result.get("generated_text", "")

            # Process the troubleshooting response
            troubleshoot_data = process_troubleshoot(troubleshoot_text, request)

            return TroubleshootResponse(
                diagnosis=troubleshoot_data["diagnosis"],
                root_causes=troubleshoot_data["root_causes"],
                solutions=troubleshoot_data["solutions"],
                prevention=troubleshoot_data["prevention"],
                metadata={
                    "issue_type": request.issue_type,
                    "timestamp": datetime.now().isoformat()
                }
            )
    except Exception as e:
        logger.error(f"Error troubleshooting issue: {e}")
        raise HTTPException(status_code=500, detail=f"Error troubleshooting issue: {str(e)}")

@app.post("/optimize", response_model=OptimizationResponse)
async def optimize_performance(request: OptimizationRequest):
    """Optimize performance based on the request."""
    logger.info(f"Received request to optimize {request.system_type} performance")

    # Construct prompt for the BLOOM service
    prompt = construct_optimization_prompt(request)

    try:
        # Call BLOOM service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BLOOM_SERVICE_URL}/text_generation",
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.error(f"BLOOM service returned status code {response.status_code}")
                raise HTTPException(status_code=500, detail="Error calling BLOOM service")

            result = response.json()
            optimization_text = result.get("generated_text", "")

            # Process the optimization response
            optimization_data = process_optimization(optimization_text, request)

            return OptimizationResponse(
                assessment=optimization_data["assessment"],
                bottlenecks=optimization_data["bottlenecks"],
                optimization_plan=optimization_data["optimization_plan"],
                expected_improvements=optimization_data["expected_improvements"],
                implementation_steps=optimization_data["implementation_steps"],
                metadata={
                    "system_type": request.system_type,
                    "performance_goals": request.performance_goals,
                    "timestamp": datetime.now().isoformat()
                }
            )
    except Exception as e:
        logger.error(f"Error optimizing performance: {e}")
        raise HTTPException(status_code=500, detail=f"Error optimizing performance: {str(e)}")

@app.post("/fix-connectivity", response_model=ConnectivityResponse)
async def fix_connectivity(request: ConnectivityRequest):
    """Fix connectivity issues based on the request."""
    logger.info(f"Received request to fix connectivity between {request.component_a} and {request.component_b}")

    # Construct prompt for the BLOOM service
    prompt = construct_connectivity_prompt(request)

    try:
        # Call BLOOM service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BLOOM_SERVICE_URL}/text_generation",
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.error(f"BLOOM service returned status code {response.status_code}")
                raise HTTPException(status_code=500, detail="Error calling BLOOM service")

            result = response.json()
            connectivity_text = result.get("generated_text", "")

            # Process the connectivity response
            connectivity_data = process_connectivity(connectivity_text, request)

            return ConnectivityResponse(
                diagnosis=connectivity_data["diagnosis"],
                solution=connectivity_data["solution"],
                configuration_changes=connectivity_data["configuration_changes"],
                testing_steps=connectivity_data["testing_steps"],
                metadata={
                    "component_a": request.component_a,
                    "component_b": request.component_b,
                    "timestamp": datetime.now().isoformat()
                }
            )
    except Exception as e:
        logger.error(f"Error fixing connectivity: {e}")
        raise HTTPException(status_code=500, detail=f"Error fixing connectivity: {str(e)}")

@app.post("/create-api", response_model=ApiEndpointResponse)
async def create_api_endpoint(request: ApiEndpointRequest):
    """Create an API endpoint based on the request."""
    logger.info(f"Received request to create API endpoint for: {request.purpose}")

    # Construct prompt for the BLOOM service
    prompt = construct_api_prompt(request)

    try:
        # Call BLOOM service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BLOOM_SERVICE_URL}/text_generation",
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.error(f"BLOOM service returned status code {response.status_code}")
                raise HTTPException(status_code=500, detail="Error calling BLOOM service")

            result = response.json()
            api_text = result.get("generated_text", "")

            # Process the API endpoint response
            api_data = process_api_endpoint(api_text, request)

            return ApiEndpointResponse(
                endpoint_design=api_data["endpoint_design"],
                implementation_code=api_data["implementation_code"],
                testing_strategy=api_data["testing_strategy"],
                documentation=api_data["documentation"],
                metadata={
                    "purpose": request.purpose,
                    "functionality": request.functionality,
                    "timestamp": datetime.now().isoformat()
                }
            )
    except Exception as e:
        logger.error(f"Error creating API endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Error creating API endpoint: {str(e)}")

@app.post("/create-database", response_model=DatabaseSchemaResponse)
async def create_database_schema(request: DatabaseSchemaRequest):
    """Create a database schema based on the request."""
    logger.info(f"Received request to create {request.database_type} database schema for: {request.purpose}")

    # Construct prompt for the BLOOM service
    prompt = construct_database_prompt(request)

    try:
        # Call BLOOM service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BLOOM_SERVICE_URL}/text_generation",
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 800,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.error(f"BLOOM service returned status code {response.status_code}")
                raise HTTPException(status_code=500, detail="Error calling BLOOM service")

            result = response.json()
            database_text = result.get("generated_text", "")

            # Process the database schema response
            database_data = process_database_schema(database_text, request)

            return DatabaseSchemaResponse(
                schema_design=database_data["schema_design"],
                implementation_code=database_data["implementation_code"],
                optimization_recommendations=database_data["optimization_recommendations"],
                migration_strategy=database_data.get("migration_strategy"),
                metadata={
                    "database_type": request.database_type,
                    "purpose": request.purpose,
                    "timestamp": datetime.now().isoformat()
                }
            )
    except Exception as e:
        logger.error(f"Error creating database schema: {e}")
        raise HTTPException(status_code=500, detail=f"Error creating database schema: {str(e)}")

# Helper functions for constructing prompts
def construct_website_prompt(request: WebsiteRequest) -> str:
    """Construct a prompt for website building."""
    # Base prompt
    prompt = f"You are a Builder Agent specializing in website development. "
    prompt += f"Create a detailed website plan for a {request.business_type} business named '{request.name}'. "

    # Add features if provided
    if request.features:
        prompt += f"The website should include the following features: {', '.join(request.features)}. "

    # Add design preferences if provided
    if request.design_preferences:
        prompt += f"\n\nDesign preferences:\n"
        for key, value in request.design_preferences.items():
            prompt += f"- {key}: {value}\n"

    # Add content details if provided
    if request.content_details:
        prompt += f"\n\nContent details:\n"
        for key, value in request.content_details.items():
            prompt += f"- {key}: {value}\n"

    # Add technical requirements if provided
    if request.technical_requirements:
        prompt += f"\n\nTechnical requirements:\n"
        for key, value in request.technical_requirements.items():
            prompt += f"- {key}: {value}\n"

    # Final instruction
    prompt += f"\n\nProvide a comprehensive website plan including:\n"
    prompt += f"1. Overall website architecture (pages, navigation structure)\n"
    prompt += f"2. Recommended technology stack (frontend, backend, database)\n"
    prompt += f"3. Detailed implementation steps\n"
    prompt += f"4. Estimated timeline for development\n"

    return prompt

def construct_troubleshoot_prompt(request: TroubleshootRequest) -> str:
    """Construct a prompt for troubleshooting technical issues."""
    # Base prompt
    prompt = f"You are a Builder Agent specializing in technical troubleshooting. "
    prompt += f"Diagnose and provide solutions for a {request.issue_type} issue described as: '{request.description}'. "

    # Add system details if provided
    if request.system_details:
        prompt += f"\n\nSystem details:\n"
        for key, value in request.system_details.items():
            prompt += f"- {key}: {value}\n"

    # Add error messages if provided
    if request.error_messages:
        prompt += f"\n\nError messages:\n"
        for error in request.error_messages:
            prompt += f"- {error}\n"

    # Add steps already taken if provided
    if request.steps_taken:
        prompt += f"\n\nSteps already taken:\n"
        for step in request.steps_taken:
            prompt += f"- {step}\n"

    # Final instruction
    prompt += f"\n\nProvide a comprehensive troubleshooting response including:\n"
    prompt += f"1. Detailed diagnosis of the issue\n"
    prompt += f"2. Potential root causes\n"
    prompt += f"3. Step-by-step solutions, from simplest to most complex\n"
    prompt += f"4. Prevention measures to avoid similar issues in the future\n"

    return prompt

def construct_optimization_prompt(request: OptimizationRequest) -> str:
    """Construct a prompt for performance optimization."""
    # Base prompt
    prompt = f"You are a Builder Agent specializing in performance optimization. "
    prompt += f"Optimize a {request.system_type} system with current performance described as: '{request.current_performance}'. "

    # Add performance goals
    prompt += f"\n\nPerformance goals:\n"
    for goal in request.performance_goals:
        prompt += f"- {goal}\n"

    # Add system details if provided
    if request.system_details:
        prompt += f"\n\nSystem details:\n"
        for key, value in request.system_details.items():
            prompt += f"- {key}: {value}\n"

    # Add constraints if provided
    if request.constraints:
        prompt += f"\n\nConstraints to consider:\n"
        for constraint in request.constraints:
            prompt += f"- {constraint}\n"

    # Final instruction
    prompt += f"\n\nProvide a comprehensive optimization plan including:\n"
    prompt += f"1. Assessment of current performance issues\n"
    prompt += f"2. Identified bottlenecks and their impact\n"
    prompt += f"3. Detailed optimization plan with specific techniques\n"
    prompt += f"4. Expected improvements for each optimization\n"
    prompt += f"5. Step-by-step implementation instructions\n"

    return prompt

def construct_connectivity_prompt(request: ConnectivityRequest) -> str:
    """Construct a prompt for fixing connectivity issues."""
    # Base prompt
    prompt = f"You are a Builder Agent specializing in system connectivity. "
    prompt += f"Fix connectivity issues between {request.component_a} and {request.component_b} described as: '{request.issue_description}'. "

    # Add current configuration if provided
    if request.current_configuration:
        prompt += f"\n\nCurrent configuration:\n"
        for key, value in request.current_configuration.items():
            prompt += f"- {key}: {value}\n"

    # Add error messages if provided
    if request.error_messages:
        prompt += f"\n\nError messages:\n"
        for error in request.error_messages:
            prompt += f"- {error}\n"

    # Final instruction
    prompt += f"\n\nProvide a comprehensive connectivity solution including:\n"
    prompt += f"1. Diagnosis of the connectivity issue\n"
    prompt += f"2. Detailed solution with specific configuration changes\n"
    prompt += f"3. Step-by-step testing instructions to verify the fix\n"
    prompt += f"4. Explanation of why the solution works\n"

    return prompt

def construct_api_prompt(request: ApiEndpointRequest) -> str:
    """Construct a prompt for creating API endpoints."""
    # Base prompt
    prompt = f"You are a Builder Agent specializing in API development. "
    prompt += f"Create an API endpoint for the purpose of '{request.purpose}' with functionality: '{request.functionality}'. "

    # Add data model if provided
    if request.data_model:
        prompt += f"\n\nData model:\n"
        for key, value in request.data_model.items():
            prompt += f"- {key}: {value}\n"

    # Add authentication if provided
    if request.authentication:
        prompt += f"\n\nAuthentication requirements: {request.authentication}\n"

    # Add performance requirements if provided
    if request.performance_requirements:
        prompt += f"\n\nPerformance requirements:\n"
        for key, value in request.performance_requirements.items():
            prompt += f"- {key}: {value}\n"

    # Final instruction
    prompt += f"\n\nProvide a comprehensive API endpoint design including:\n"
    prompt += f"1. Detailed endpoint design (URL, method, parameters, responses)\n"
    prompt += f"2. Implementation code in a modern framework\n"
    prompt += f"3. Testing strategy for the endpoint\n"
    prompt += f"4. API documentation in standard format\n"

    return prompt

def construct_database_prompt(request: DatabaseSchemaRequest) -> str:
    """Construct a prompt for creating database schemas."""
    # Base prompt
    prompt = f"You are a Builder Agent specializing in database design. "
    prompt += f"Create a {request.database_type} database schema for the purpose of '{request.purpose}'. "

    # Add entities
    prompt += f"\n\nEntities to be stored:\n"
    for entity in request.entities:
        prompt += f"- {entity.get('name', 'Unnamed entity')}: {json.dumps(entity)}\n"

    # Add relationships if provided
    if request.relationships:
        prompt += f"\n\nRelationships between entities:\n"
        for relationship in request.relationships:
            prompt += f"- {json.dumps(relationship)}\n"

    # Add performance requirements if provided
    if request.performance_requirements:
        prompt += f"\n\nPerformance requirements:\n"
        for key, value in request.performance_requirements.items():
            prompt += f"- {key}: {value}\n"

    # Final instruction
    prompt += f"\n\nProvide a comprehensive database schema design including:\n"
    prompt += f"1. Detailed schema design with tables/collections and fields\n"
    prompt += f"2. Implementation code (SQL, NoSQL schema definition)\n"
    prompt += f"3. Optimization recommendations for performance\n"
    prompt += f"4. Migration strategy if applicable\n"

    return prompt

# Helper functions for processing responses
def process_website_plan(text: str, request: WebsiteRequest) -> Dict[str, Any]:
    """Process the generated website plan text into structured data."""
    # Initialize default values
    website_plan = "No website plan provided."
    architecture = {"pages": [], "navigation": {}}
    technology_stack = {"frontend": [], "backend": [], "database": []}
    implementation_steps = []
    estimated_timeline = "No timeline provided."

    # Simple parsing logic - in a real implementation, this would be more sophisticated
    lines = text.strip().split("\n")
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "architecture" in line.lower() or "structure" in line.lower():
            current_section = "architecture"
            continue
        elif "technology" in line.lower() or "stack" in line.lower():
            current_section = "technology"
            continue
        elif "implementation" in line.lower() or "steps" in line.lower():
            current_section = "implementation"
            continue
        elif "timeline" in line.lower() or "schedule" in line.lower():
            current_section = "timeline"
            continue
        elif not current_section and line:
            # Assume this is part of the overall plan
            website_plan = line
            continue

        # Process line based on current section
        if current_section == "architecture" and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip().lower()
                value = parts[1].strip()
                if "page" in key:
                    architecture["pages"].append(value)
                elif "nav" in key:
                    architecture["navigation"][key] = value
        elif current_section == "technology" and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip().lower()
                value = parts[1].strip()
                if "front" in key:
                    technology_stack["frontend"] = [item.strip() for item in value.split(",")]
                elif "back" in key:
                    technology_stack["backend"] = [item.strip() for item in value.split(",")]
                elif "database" in key or "db" in key:
                    technology_stack["database"] = [item.strip() for item in value.split(",")]
        elif current_section == "implementation" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            implementation_steps.append(clean_line)
        elif current_section == "timeline" and not estimated_timeline.startswith("Estimated"):
            estimated_timeline = line

    return {
        "website_plan": website_plan,
        "architecture": architecture,
        "technology_stack": technology_stack,
        "implementation_steps": implementation_steps,
        "estimated_timeline": estimated_timeline
    }

def process_troubleshoot(text: str, request: TroubleshootRequest) -> Dict[str, Any]:
    """Process the generated troubleshooting text into structured data."""
    # Initialize default values
    diagnosis = "No diagnosis provided."
    root_causes = []
    solutions = []
    prevention = []

    # Simple parsing logic - in a real implementation, this would be more sophisticated
    lines = text.strip().split("\n")
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "diagnosis" in line.lower() or "issue" in line.lower():
            current_section = "diagnosis"
            continue
        elif "root cause" in line.lower() or "causes" in line.lower():
            current_section = "root_causes"
            continue
        elif "solution" in line.lower() or "fix" in line.lower() or "resolv" in line.lower():
            current_section = "solutions"
            continue
        elif "prevent" in line.lower() or "future" in line.lower():
            current_section = "prevention"
            continue
        elif not current_section and line:
            # Assume this is part of the diagnosis
            diagnosis = line
            continue

        # Process line based on current section
        if current_section == "diagnosis" and not diagnosis.startswith("No diagnosis"):
            diagnosis += " " + line
        elif current_section == "root_causes" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            root_causes.append(clean_line)
        elif current_section == "solutions" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            # For solutions, we'll create a more structured format
            solutions.append({
                "description": clean_line,
                "complexity": "medium",  # Default value
                "estimated_time": "varies"  # Default value
            })
        elif current_section == "prevention" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            prevention.append(clean_line)

    return {
        "diagnosis": diagnosis,
        "root_causes": root_causes,
        "solutions": solutions,
        "prevention": prevention
    }

def process_optimization(text: str, request: OptimizationRequest) -> Dict[str, Any]:
    """Process the generated optimization text into structured data."""
    # Initialize default values
    assessment = "No assessment provided."
    bottlenecks = []
    optimization_plan = {"short_term": [], "medium_term": [], "long_term": []}
    expected_improvements = {}
    implementation_steps = []

    # Simple parsing logic - in a real implementation, this would be more sophisticated
    lines = text.strip().split("\n")
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "assessment" in line.lower() or "current" in line.lower():
            current_section = "assessment"
            continue
        elif "bottleneck" in line.lower() or "issue" in line.lower():
            current_section = "bottlenecks"
            continue
        elif "optimization" in line.lower() or "plan" in line.lower():
            current_section = "optimization_plan"
            continue
        elif "improvement" in line.lower() or "benefit" in line.lower():
            current_section = "improvements"
            continue
        elif "implementation" in line.lower() or "steps" in line.lower():
            current_section = "implementation"
            continue
        elif not current_section and line:
            # Assume this is part of the assessment
            assessment = line
            continue

        # Process line based on current section
        if current_section == "assessment" and not assessment.startswith("No assessment"):
            assessment += " " + line
        elif current_section == "bottlenecks" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            bottlenecks.append(clean_line)
        elif current_section == "optimization_plan":
            if "short" in line.lower() or "immediate" in line.lower():
                optimization_plan["short_term"].append(line.lstrip("-*•0123456789. "))
            elif "medium" in line.lower():
                optimization_plan["medium_term"].append(line.lstrip("-*•0123456789. "))
            elif "long" in line.lower():
                optimization_plan["long_term"].append(line.lstrip("-*•0123456789. "))
            elif line.startswith(("-", "*", "•", "1.", "2.", "3.")):
                # If no specific term is mentioned, default to medium term
                optimization_plan["medium_term"].append(line.lstrip("-*•0123456789. "))
        elif current_section == "improvements" and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                expected_improvements[key] = value
        elif current_section == "implementation" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            implementation_steps.append(clean_line)

    return {
        "assessment": assessment,
        "bottlenecks": bottlenecks,
        "optimization_plan": optimization_plan,
        "expected_improvements": expected_improvements,
        "implementation_steps": implementation_steps
    }

def process_connectivity(text: str, request: ConnectivityRequest) -> Dict[str, Any]:
    """Process the generated connectivity text into structured data."""
    # Initialize default values
    diagnosis = "No diagnosis provided."
    solution = "No solution provided."
    configuration_changes = {}
    testing_steps = []

    # Simple parsing logic - in a real implementation, this would be more sophisticated
    lines = text.strip().split("\n")
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "diagnosis" in line.lower() or "issue" in line.lower():
            current_section = "diagnosis"
            continue
        elif "solution" in line.lower() or "fix" in line.lower():
            current_section = "solution"
            continue
        elif "configuration" in line.lower() or "change" in line.lower() or "setting" in line.lower():
            current_section = "configuration"
            continue
        elif "test" in line.lower() or "verify" in line.lower():
            current_section = "testing"
            continue
        elif not current_section and line:
            # Assume this is part of the diagnosis
            diagnosis = line
            continue

        # Process line based on current section
        if current_section == "diagnosis" and not diagnosis.startswith("No diagnosis"):
            diagnosis += " " + line
        elif current_section == "solution" and not solution.startswith("No solution"):
            solution += " " + line
        elif current_section == "configuration" and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                configuration_changes[key] = value
        elif current_section == "testing" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            testing_steps.append(clean_line)

    return {
        "diagnosis": diagnosis,
        "solution": solution,
        "configuration_changes": configuration_changes,
        "testing_steps": testing_steps
    }

def process_api_endpoint(text: str, request: ApiEndpointRequest) -> Dict[str, Any]:
    """Process the generated API endpoint text into structured data."""
    # Initialize default values
    endpoint_design = {"path": "", "method": "", "parameters": {}, "responses": {}}
    implementation_code = "# No implementation code provided."
    testing_strategy = {"unit_tests": [], "integration_tests": []}
    documentation = "No documentation provided."

    # Simple parsing logic - in a real implementation, this would be more sophisticated
    lines = text.strip().split("\n")
    current_section = None
    code_block = []

    for line in lines:
        # Check for code blocks
        if line.strip().startswith("```"):
            if not code_block:
                # Start of code block
                code_block.append(line)
                current_section = "code"
                continue
            else:
                # End of code block
                code_block.append(line)
                implementation_code = "\n".join(code_block)
                code_block = []
                current_section = None
                continue

        # If we're in a code block, just add the line
        if code_block:
            code_block.append(line)
            continue

        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "endpoint" in line.lower() or "api design" in line.lower() or "route" in line.lower():
            current_section = "design"
            continue
        elif "implementation" in line.lower() or "code" in line.lower():
            current_section = "implementation"
            continue
        elif "test" in line.lower() or "verify" in line.lower():
            current_section = "testing"
            continue
        elif "documentation" in line.lower() or "docs" in line.lower():
            current_section = "documentation"
            continue

        # Process line based on current section
        if current_section == "design":
            if "path" in line.lower() or "url" in line.lower() or "endpoint" in line.lower():
                if ":" in line:
                    parts = line.split(":", 1)
                    endpoint_design["path"] = parts[1].strip()
            elif "method" in line.lower() or "http" in line.lower():
                if ":" in line:
                    parts = line.split(":", 1)
                    endpoint_design["method"] = parts[1].strip()
            elif "parameter" in line.lower() or "input" in line.lower():
                if ":" in line:
                    parts = line.split(":", 1)
                    param_name = parts[0].strip().replace("parameter", "").replace(":", "").strip()
                    param_desc = parts[1].strip()
                    endpoint_design["parameters"][param_name] = param_desc
            elif "response" in line.lower() or "output" in line.lower() or "return" in line.lower():
                if ":" in line:
                    parts = line.split(":", 1)
                    resp_name = parts[0].strip().replace("response", "").replace(":", "").strip()
                    resp_desc = parts[1].strip()
                    endpoint_design["responses"][resp_name] = resp_desc
        elif current_section == "testing":
            if "unit" in line.lower():
                testing_strategy["unit_tests"].append(line.lstrip("-*•0123456789. "))
            elif "integration" in line.lower():
                testing_strategy["integration_tests"].append(line.lstrip("-*•0123456789. "))
            elif line.startswith(("-", "*", "•", "1.", "2.", "3.")):
                # If no specific test type is mentioned, default to unit tests
                testing_strategy["unit_tests"].append(line.lstrip("-*•0123456789. "))
        elif current_section == "documentation" and not documentation.startswith("No documentation"):
            if documentation == "No documentation provided.":
                documentation = line
            else:
                documentation += "\n" + line

    return {
        "endpoint_design": endpoint_design,
        "implementation_code": implementation_code,
        "testing_strategy": testing_strategy,
        "documentation": documentation
    }

def process_database_schema(text: str, request: DatabaseSchemaRequest) -> Dict[str, Any]:
    """Process the generated database schema text into structured data."""
    # Initialize default values
    schema_design = {"tables": {}, "relationships": []}
    implementation_code = "# No implementation code provided."
    optimization_recommendations = []
    migration_strategy = {"steps": [], "considerations": []}

    # Simple parsing logic - in a real implementation, this would be more sophisticated
    lines = text.strip().split("\n")
    current_section = None
    code_block = []
    current_table = None

    for line in lines:
        # Check for code blocks
        if line.strip().startswith("```"):
            if not code_block:
                # Start of code block
                code_block.append(line)
                current_section = "code"
                continue
            else:
                # End of code block
                code_block.append(line)
                implementation_code = "\n".join(code_block)
                code_block = []
                current_section = None
                continue

        # If we're in a code block, just add the line
        if code_block:
            code_block.append(line)
            continue

        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "schema" in line.lower() or "design" in line.lower() or "table" in line.lower():
            current_section = "schema"
            continue
        elif "implementation" in line.lower() or "code" in line.lower():
            current_section = "implementation"
            continue
        elif "optimization" in line.lower() or "performance" in line.lower():
            current_section = "optimization"
            continue
        elif "migration" in line.lower() or "deploy" in line.lower():
            current_section = "migration"
            continue

        # Process line based on current section
        if current_section == "schema":
            if line.endswith(":") and not line.startswith("-"):
                # This might be a table name
                current_table = line.rstrip(":")
                schema_design["tables"][current_table] = {"fields": {}, "indexes": []}
            elif current_table and ":" in line:
                # This might be a field definition
                parts = line.split(":", 1)
                field_name = parts[0].strip()
                field_type = parts[1].strip()
                schema_design["tables"][current_table]["fields"][field_name] = field_type
            elif "relationship" in line.lower() or "foreign key" in line.lower():
                schema_design["relationships"].append(line.lstrip("-*•0123456789. "))
        elif current_section == "optimization" and line.startswith(("-", "*", "•", "1.", "2.", "3.")):
            # Clean up the line by removing list markers
            clean_line = line.lstrip("-*•0123456789. ")
            optimization_recommendations.append(clean_line)
        elif current_section == "migration":
            if "step" in line.lower() or line.startswith(("-", "*", "•", "1.", "2.", "3.")):
                migration_strategy["steps"].append(line.lstrip("-*•0123456789. "))
            elif "consider" in line.lower():
                migration_strategy["considerations"].append(line.lstrip("-*•0123456789. "))

    return {
        "schema_design": schema_design,
        "implementation_code": implementation_code,
        "optimization_recommendations": optimization_recommendations,
        "migration_strategy": migration_strategy
    }

# Main function
def main():
    parser = argparse.ArgumentParser(description="Builder Agent MCP")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=3207, help="Port to bind to")
    parser.add_argument("--bloom-url", type=str, default="http://localhost:8000", help="URL of the BLOOM service")
    parser.add_argument("--log-level", type=str, default="INFO", help="Logging level")

    args = parser.parse_args()

    # Set environment variables
    os.environ["BLOOM_SERVICE_URL"] = args.bloom_url

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
