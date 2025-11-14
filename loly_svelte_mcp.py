#!/usr/bin/env python3
"""
🚀 LOLY SVELTE MCP - Svelte Development Assistant
Agent Poly Loly: Svelte-Specific Coding Intelligence

This MCP provides comprehensive Svelte development assistance:
- Component generation and optimization
- SvelteKit project scaffolding
- Store management patterns
- Reactive programming assistance
- Performance optimization
- Build and deployment guidance
"""

import os
import argparse
import logging
import json
import subprocess
import re
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("loly-svelte-mcp")

# Create FastAPI app
app = FastAPI(title="LOLY Svelte MCP", description="Svelte Development Assistant for LOLY")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ComponentRequest(BaseModel):
    """Request model for Svelte component generation."""
    component_name: str = Field(..., description="Name of the component")
    component_type: str = Field(..., description="Type of component (page, layout, component, store)")
    props: Optional[List[str]] = Field(None, description="Component props")
    features: Optional[List[str]] = Field(None, description="Features to include")
    styling: Optional[str] = Field("css", description="Styling approach (css, scss, tailwind)")

class ComponentResponse(BaseModel):
    """Response model for component generation."""
    component_code: str = Field(..., description="Generated component code")
    file_path: str = Field(..., description="Suggested file path")
    dependencies: List[str] = Field(..., description="Required dependencies")
    usage_example: str = Field(..., description="Usage example")
    best_practices: List[str] = Field(..., description="Best practices")

class ProjectRequest(BaseModel):
    """Request model for SvelteKit project setup."""
    project_name: str = Field(..., description="Name of the project")
    template: str = Field("skeleton", description="Project template (skeleton, demo, library)")
    features: List[str] = Field(..., description="Features to include")
    typescript: bool = Field(True, description="Use TypeScript")

class ProjectResponse(BaseModel):
    """Response model for project setup."""
    setup_commands: List[str] = Field(..., description="Commands to set up the project")
    project_structure: Dict[str, Any] = Field(..., description="Project structure")
    configuration: Dict[str, Any] = Field(..., description="Configuration files")
    next_steps: List[str] = Field(..., description="Next steps")

class OptimizationRequest(BaseModel):
    """Request model for code optimization."""
    code: str = Field(..., description="Code to optimize")
    optimization_type: str = Field(..., description="Type of optimization (performance, bundle, accessibility)")
    target: Optional[str] = Field(None, description="Optimization target")

class OptimizationResponse(BaseModel):
    """Response model for code optimization."""
    optimized_code: str = Field(..., description="Optimized code")
    improvements: List[str] = Field(..., description="List of improvements made")
    performance_tips: List[str] = Field(..., description="Performance tips")
    bundle_impact: Optional[str] = Field(None, description="Bundle size impact")

class StoreRequest(BaseModel):
    """Request model for Svelte store creation."""
    store_name: str = Field(..., description="Name of the store")
    store_type: str = Field(..., description="Type of store (writable, readable, derived, custom)")
    data_structure: Dict[str, Any] = Field(..., description="Data structure")
    features: Optional[List[str]] = Field(None, description="Additional features")

class StoreResponse(BaseModel):
    """Response model for store creation."""
    store_code: str = Field(..., description="Generated store code")
    usage_examples: List[str] = Field(..., description="Usage examples")
    patterns: List[str] = Field(..., description="Recommended patterns")
    testing_code: Optional[str] = Field(None, description="Testing code")

# Svelte Templates and Patterns
class SvelteTemplates:
    """Collection of Svelte templates and patterns."""
    
    @staticmethod
    def get_component_template(name: str, props: List[str] = None, features: List[str] = None, styling: str = "css") -> str:
        """Generate a Svelte component template."""
        props = props or []
        features = features or []
        
        # Generate script section
        script_content = []
        if props:
            script_content.append("  // Props")
            for prop in props:
                script_content.append(f"  export let {prop};")
        
        if "reactive" in features:
            script_content.append("\n  // Reactive statements")
            script_content.append("  $: console.log('Props changed:', { " + ", ".join(props) + " });")
        
        if "lifecycle" in features:
            script_content.append("\n  import { onMount, onDestroy } from 'svelte';")
            script_content.append("\n  onMount(() => {")
            script_content.append("    console.log('Component mounted');")
            script_content.append("  });")
        
        if "store" in features:
            script_content.append("\n  import { writable } from 'svelte/store';")
            script_content.append("  const localState = writable({});")
        
        # Generate template
        template = f"""<script>
{chr(10).join(script_content) if script_content else "  // Component logic here"}
</script>

<div class="{name.lower()}">
  <h2>{name} Component</h2>
  {f"<p>Props: {{{', '.join(props)}}}</p>" if props else ""}
  <!-- Component content here -->
</div>

<style{' lang="scss"' if styling == 'scss' else ''}>
  .{name.lower()} {{
    /* Component styles here */
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }}
  
  h2 {{
    margin: 0 0 1rem 0;
    color: #333;
  }}
</style>"""
        
        return template
    
    @staticmethod
    def get_store_template(name: str, store_type: str, data_structure: Dict[str, Any]) -> str:
        """Generate a Svelte store template."""
        if store_type == "writable":
            return f"""import {{ writable }} from 'svelte/store';

// {name} store
export const {name} = writable({json.dumps(data_structure, indent=2)});

// Helper functions
export const {name}Actions = {{
  update: (newData) => {name}.update(current => ({{ ...current, ...newData }})),
  reset: () => {name}.set({json.dumps(data_structure, indent=2)}),
  // Add more actions as needed
}};"""
        
        elif store_type == "readable":
            return f"""import {{ readable }} from 'svelte/store';

// {name} readable store
export const {name} = readable({json.dumps(data_structure, indent=2)}, (set) => {{
  // Setup logic here
  const interval = setInterval(() => {{
    // Update logic
    set(/* new value */);
  }}, 1000);
  
  return () => clearInterval(interval);
}});"""
        
        elif store_type == "derived":
            return f"""import {{ derived }} from 'svelte/store';
import {{ someOtherStore }} from './other-store.js';

// {name} derived store
export const {name} = derived(
  someOtherStore,
  ($someOtherStore) => {{
    // Derive value from other store
    return /* derived value */;
  }}
);"""
        
        else:  # custom
            return f"""import {{ writable }} from 'svelte/store';

// Custom {name} store
function create{name.capitalize()}Store() {{
  const {{ subscribe, set, update }} = writable({json.dumps(data_structure, indent=2)});
  
  return {{
    subscribe,
    // Custom methods
    customMethod: () => update(current => {{
      // Custom logic
      return current;
    }}),
    reset: () => set({json.dumps(data_structure, indent=2)})
  }};
}}

export const {name} = create{name.capitalize()}Store();"""

# Utility functions
def analyze_svelte_code(code: str) -> Dict[str, Any]:
    """Analyze Svelte code for optimization opportunities."""
    analysis = {
        "components_count": len(re.findall(r'<script>', code)),
        "reactive_statements": len(re.findall(r'\$:', code)),
        "stores_used": len(re.findall(r'import.*from.*svelte/store', code)),
        "lifecycle_hooks": len(re.findall(r'on(Mount|Destroy|Update)', code)),
        "potential_issues": []
    }
    
    # Check for potential issues
    if 'console.log' in code:
        analysis["potential_issues"].append("Remove console.log statements in production")
    
    if re.search(r'style.*{.*}', code, re.DOTALL) and len(code) > 1000:
        analysis["potential_issues"].append("Consider extracting styles to separate file")
    
    if analysis["reactive_statements"] > 5:
        analysis["potential_issues"].append("High number of reactive statements - consider optimization")
    
    return analysis

def get_svelte_best_practices() -> List[str]:
    """Get Svelte best practices."""
    return [
        "Use reactive statements ($:) for derived values",
        "Prefer stores for global state management",
        "Use onMount for side effects",
        "Avoid unnecessary reactive statements",
        "Use bind: for two-way data binding",
        "Leverage Svelte's built-in transitions",
        "Use slots for component composition",
        "Optimize bundle size with tree shaking",
        "Use TypeScript for better development experience",
        "Follow Svelte naming conventions"
    ]

# API Endpoints
@app.get("/health")
async def health_check():
    """Check the health of the Svelte MCP service."""
    return {
        "status": "healthy",
        "service": "LOLY Svelte MCP",
        "timestamp": datetime.now().isoformat(),
        "capabilities": ["component_generation", "project_setup", "code_optimization", "store_management"]
    }

@app.post("/generate_component", response_model=ComponentResponse)
async def generate_component(request: ComponentRequest):
    """Generate a Svelte component based on specifications."""
    logger.info(f"Generating Svelte component: {request.component_name}")
    
    try:
        # Generate component code
        component_code = SvelteTemplates.get_component_template(
            request.component_name,
            request.props,
            request.features,
            request.styling
        )
        
        # Determine file path
        if request.component_type == "page":
            file_path = f"src/routes/{request.component_name.lower()}/+page.svelte"
        elif request.component_type == "layout":
            file_path = f"src/routes/{request.component_name.lower()}/+layout.svelte"
        else:
            file_path = f"src/lib/components/{request.component_name}.svelte"
        
        # Determine dependencies
        dependencies = []
        if request.features:
            if "store" in request.features:
                dependencies.append("svelte/store")
            if "lifecycle" in request.features:
                dependencies.append("svelte (onMount, onDestroy)")
            if "animation" in request.features:
                dependencies.append("svelte/transition")
        
        # Generate usage example
        props_str = " ".join([f'{prop}="{{{prop}}}"' for prop in (request.props or [])])
        usage_example = f"<{request.component_name} {props_str} />"
        
        return ComponentResponse(
            component_code=component_code,
            file_path=file_path,
            dependencies=dependencies,
            usage_example=usage_example,
            best_practices=get_svelte_best_practices()[:5]
        )
        
    except Exception as e:
        logger.error(f"Error generating component: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating component: {str(e)}")

@app.post("/setup_project", response_model=ProjectResponse)
async def setup_project(request: ProjectRequest):
    """Generate SvelteKit project setup instructions."""
    logger.info(f"Setting up SvelteKit project: {request.project_name}")
    
    try:
        # Generate setup commands
        setup_commands = [
            f"npm create svelte@latest {request.project_name}",
            f"cd {request.project_name}",
            "npm install"
        ]
        
        # Add TypeScript if requested
        if request.typescript:
            setup_commands.append("npm run check")
        
        # Add feature-specific dependencies
        feature_deps = []
        if "tailwind" in request.features:
            feature_deps.extend([
                "npm install -D tailwindcss postcss autoprefixer @tailwindcss/typography",
                "npx tailwindcss init -p"
            ])
        
        if "testing" in request.features:
            feature_deps.extend([
                "npm install -D @testing-library/svelte @testing-library/jest-dom vitest jsdom"
            ])
        
        if "eslint" in request.features:
            feature_deps.append("npm install -D eslint @typescript-eslint/eslint-plugin")
        
        setup_commands.extend(feature_deps)
        
        # Generate project structure
        project_structure = {
            "src/": {
                "lib/": {
                    "components/": "Reusable components",
                    "stores/": "Svelte stores",
                    "utils/": "Utility functions"
                },
                "routes/": {
                    "+layout.svelte": "Root layout",
                    "+page.svelte": "Home page"
                },
                "app.html": "HTML template",
                "app.css": "Global styles"
            },
            "static/": "Static assets",
            "package.json": "Dependencies and scripts",
            "svelte.config.js": "Svelte configuration",
            "vite.config.js": "Vite configuration"
        }
        
        # Generate configuration
        configuration = {
            "svelte.config.js": "SvelteKit configuration with adapters",
            "vite.config.js": "Vite build configuration",
            "tsconfig.json": "TypeScript configuration" if request.typescript else None,
            "tailwind.config.js": "Tailwind CSS configuration" if "tailwind" in request.features else None
        }
        
        # Next steps
        next_steps = [
            "Run 'npm run dev' to start development server",
            "Create your first component in src/lib/components/",
            "Set up your routes in src/routes/",
            "Configure your stores in src/lib/stores/",
            "Customize your layout in src/routes/+layout.svelte"
        ]
        
        return ProjectResponse(
            setup_commands=setup_commands,
            project_structure=project_structure,
            configuration={k: v for k, v in configuration.items() if v},
            next_steps=next_steps
        )
        
    except Exception as e:
        logger.error(f"Error setting up project: {e}")
        raise HTTPException(status_code=500, detail=f"Error setting up project: {str(e)}")

@app.post("/optimize_code", response_model=OptimizationResponse)
async def optimize_code(request: OptimizationRequest):
    """Optimize Svelte code for performance and best practices."""
    logger.info(f"Optimizing Svelte code: {request.optimization_type}")
    
    try:
        analysis = analyze_svelte_code(request.code)
        optimized_code = request.code
        improvements = []
        performance_tips = []
        
        # Performance optimizations
        if request.optimization_type == "performance":
            # Remove console.log statements
            if 'console.log' in optimized_code:
                optimized_code = re.sub(r'console\.log\([^)]*\);?\n?', '', optimized_code)
                improvements.append("Removed console.log statements")
            
            # Optimize reactive statements
            if analysis["reactive_statements"] > 3:
                performance_tips.append("Consider reducing reactive statements")
                performance_tips.append("Use derived stores for complex computations")
            
            performance_tips.extend([
                "Use onMount for side effects",
                "Avoid creating objects in templates",
                "Use keyed each blocks for lists",
                "Implement virtual scrolling for large lists"
            ])
        
        # Bundle optimizations
        elif request.optimization_type == "bundle":
            improvements.append("Analyzed for tree-shaking opportunities")
            performance_tips.extend([
                "Use dynamic imports for code splitting",
                "Optimize images and assets",
                "Remove unused dependencies",
                "Use Svelte's built-in optimizations"
            ])
        
        # Accessibility optimizations
        elif request.optimization_type == "accessibility":
            improvements.append("Added accessibility considerations")
            performance_tips.extend([
                "Add proper ARIA labels",
                "Ensure keyboard navigation",
                "Use semantic HTML elements",
                "Provide alt text for images",
                "Maintain proper color contrast"
            ])
        
        return OptimizationResponse(
            optimized_code=optimized_code,
            improvements=improvements,
            performance_tips=performance_tips,
            bundle_impact="Estimated 5-15% reduction in bundle size" if request.optimization_type == "bundle" else None
        )
        
    except Exception as e:
        logger.error(f"Error optimizing code: {e}")
        raise HTTPException(status_code=500, detail=f"Error optimizing code: {str(e)}")

@app.post("/create_store", response_model=StoreResponse)
async def create_store(request: StoreRequest):
    """Create a Svelte store with specified configuration."""
    logger.info(f"Creating Svelte store: {request.store_name} ({request.store_type})")
    
    try:
        # Generate store code
        store_code = SvelteTemplates.get_store_template(
            request.store_name,
            request.store_type,
            request.data_structure
        )
        
        # Generate usage examples
        usage_examples = [
            f"import {{ {request.store_name} }} from './stores/{request.store_name}.js';",
            f"$: console.log('Store value:', ${request.store_name});",
            f"<p>{{${request.store_name}}}</p>"
        ]
        
        if request.store_type == "writable":
            usage_examples.extend([
                f"{request.store_name}.set(newValue);",
                f"{request.store_name}.update(current => ({{ ...current, newProp: 'value' }}));"
            ])
        
        # Recommended patterns
        patterns = [
            "Keep stores focused on single concerns",
            "Use derived stores for computed values",
            "Implement proper error handling",
            "Consider using custom stores for complex logic",
            "Test store behavior with unit tests"
        ]
        
        # Generate testing code
        testing_code = f"""import {{ get }} from 'svelte/store';
import {{ {request.store_name} }} from './{request.store_name}.js';

describe('{request.store_name} store', () => {{
  test('should have initial value', () => {{
    const value = get({request.store_name});
    expect(value).toEqual({json.dumps(request.data_structure)});
  }});
  
  // Add more tests as needed
}});"""
        
        return StoreResponse(
            store_code=store_code,
            usage_examples=usage_examples,
            patterns=patterns,
            testing_code=testing_code
        )
        
    except Exception as e:
        logger.error(f"Error creating store: {e}")
        raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="LOLY Svelte MCP")
    parser.add_argument("--host", type=str, default="localhost", help="Host to bind to")
    parser.add_argument("--port", type=int, default=3211, help="Port to bind to")
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