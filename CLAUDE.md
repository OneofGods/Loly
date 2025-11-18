# CLAUDE.md - AI Assistant Guide for Loly Project

## Project Overview

**Agent Poly Loly Double Zero** is an advanced autonomous AI agent system designed for sports prediction and betting analysis. The project features an AI personality named "Loly" with voice synthesis, consciousness simulation, and multi-agent coordination capabilities.

**Status**: Phase 5 Complete - Global Intelligence Achieved
**Performance**: 100,000+ games/second processing
**Coverage**: 199+ leagues across all major sports globally

---

## Project Architecture

### Core Systems

1. **Autonomous Agent Framework** (`core/`)
   - `autonomous_agent.py` - Base autonomous agent with self-* behaviors
   - `message_bus.py` - High-performance event-driven messaging (35K+ msg/sec)
   - `swarm_intelligence.py` - Ant colony optimization & dynamic topology
   - `intelligent_workflows.py` - LLM-powered workflow orchestration
   - `dynamic_scaling.py` - ML-based auto-scaling (1-10 agents)
   - `agent_orchestrator.py` - Multi-agent coordination system

2. **AI Consciousness System**
   - `enhanced_ai_consciousness.py` - Core AI personality engine
   - `living_ai_consciousness.py` - Advanced consciousness simulation
   - `advanced_personality_engine.py` - Personality trait management
   - `voice_synthesis_engine.py` - Voice generation for Loly

3. **Sports Intelligence**
   - **353 Python files** implementing prediction algorithms
   - **Real-time fetchers** in `real_agents/` for live data
   - **Hybrid engines** combining cultural & statistical analysis
   - **Legendary algorithms** for top-tier leagues (EPL, La Liga, etc.)
   - **MCP (Market Context Protocol)** services for specialized analysis

4. **Integration Services**
   - `unified_loly_server.py` - Main unified server (port 3012)
   - `polymarket_integration_service.py` - Real Polymarket betting
   - `deepseek_integration_service.py` - LLM integration (uses Qwen 2.5-Coder)
   - `loly_avatar_server.py` - Avatar visualization server

### Directory Structure

```
/home/user/Loly/
├── core/                          # Core autonomous agent framework
│   ├── autonomous_agent.py        # Base agent with self-* behaviors
│   ├── message_bus.py             # Event-driven messaging
│   ├── swarm_intelligence.py     # Swarm coordination
│   ├── dynamic_scaling.py         # Auto-scaling system
│   └── ...
├── agents/                        # Specialized agent implementations
│   ├── analyzer_agent.py          # Analysis coordination
│   ├── coordinator_agent.py       # Multi-agent orchestration
│   ├── data_collector_agent.py    # Data collection
│   ├── predictor_agent.py         # Prediction generation
│   └── monitor_agent.py           # System monitoring
├── real_agents/                   # Real-time sports data fetchers
│   ├── premier_league_fetcher.py
│   ├── la_liga_fetcher.py
│   ├── uefa_champions_league_fetcher.py
│   └── ... (50+ league fetchers)
├── *_real_algorithm.py           # League-specific prediction algorithms
├── *_hybrid_engine.py            # Hybrid cultural + statistical engines
├── *_mcp.py                      # Market Context Protocol services
├── unified_loly_server.py        # Main unified server
├── loly_goddess_avatar_interface.html  # Main frontend interface
├── enhanced_ai_consciousness.py   # AI personality engine
├── polymarket_integration_service.py   # Betting integration
├── docker-compose.yml            # Microservices orchestration
├── Dockerfile                    # Multi-stage container build
├── requirements.txt              # Python dependencies
├── tests/                        # Test suites
│   ├── test_agent_system.py
│   └── test_message_bus.py
└── docs/                         # Documentation
    ├── PHASE_*_COMPLETION_REPORT.md
    └── ... (various status reports)
```

---

## Key Technologies

### Backend
- **Python 3.11+** - Core language
- **aiohttp** - Async HTTP server/client
- **asyncio** - Async/await concurrency
- **websockets** - Real-time communication
- **pandas/numpy** - Data processing
- **scikit-learn** - ML models

### Frontend
- **HTML5/CSS3/JavaScript** - Web interfaces
- **WebSockets** - Real-time updates
- **Canvas/WebGL** - Avatar visualization

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-service orchestration
- **Kubernetes** - Production deployment (optional)
- **Redis** - Caching and message queue

### AI/LLM Integration
- **DeepSeek API** (configured to use Qwen 2.5-Coder at localhost:11434)
- **GPT-4, Claude, Llama-2** - Multi-LLM decision making
- **Local LLM support** via Ollama

---

## Development Workflow

### Running the System

#### Option 1: Unified Server (Recommended for Development)
```bash
# Start the main unified server
python unified_loly_server.py

# Access interfaces:
# - Avatar Interface: http://localhost:3012/avatar
# - Visual Interface: http://localhost:3012/visual
# - API: http://localhost:3012/api/*
```

#### Option 2: Full Microservices Stack (Production)
```bash
# Start all services via Docker Compose
docker-compose up --build

# Services available:
# - Message Bus: http://localhost:8080
# - Sports Panel: http://localhost:3005
# - Metrics: http://localhost:8081
# - Health: http://localhost:8082
```

#### Option 3: Single Agent System (Testing)
```bash
# Run individual agent for testing
python run_agent_system.py
```

### Testing

```bash
# Run agent system tests
python tests/test_agent_system.py

# Run message bus tests
python tests/test_message_bus.py

# Run league-specific tests
python epl_50_game_reality_backtest.py
python bundesliga_nonuple_test.py
python uefa_enhanced_accuracy_test.py
```

### Deployment

```bash
# Docker deployment
docker build -t loly-agent .
docker run -p 3012:3012 loly-agent

# Kubernetes deployment
kubectl apply -f kubernetes-deployment.yml
```

---

## Code Conventions

### Naming Patterns

1. **Real Data Fetchers**: `real_*_fetcher.py`
   - Example: `real_premier_league_fetcher.py`
   - Located in `real_agents/` directory
   - Fetch live data from actual sources

2. **Prediction Algorithms**: `*_real_algorithm.py`
   - Example: `bundesliga_real_algorithm.py`
   - Located in root directory
   - Implement league-specific prediction logic

3. **Hybrid Engines**: `*_hybrid_engine.py`
   - Example: `la_liga_hybrid_engine.py`
   - Combine cultural context + statistical analysis

4. **Legendary Algorithms**: `*_legendary_algorithm.py`
   - Example: `epl_legendary_algorithm.py`
   - Top-tier algorithms with highest accuracy

5. **MCP Services**: `*_mcp.py`
   - Example: `nba_real_mcp.py`
   - Market Context Protocol for specialized analysis
   - Categories: key_players, market_efficiency, team_performance, etc.

### File Organization

- **Core Framework**: Place in `core/` directory
- **Agent Implementations**: Place in `agents/` directory
- **Sports Fetchers**: Place in `real_agents/` directory
- **League Algorithms**: Place in root directory
- **Tests**: Place in `tests/` directory
- **Documentation**: Place in `docs/` or root as `*.md`

### Code Style

1. **Emojis in Comments**: This codebase uses expressive emoji-heavy comments
   - Example: `# 🔥💀🔥 LEGENDARY ALGORITHM 💀🔥💀`
   - Use fire (🔥), skull (💀), trophy (🏆), etc. for emphasis

2. **Async/Await**: All I/O operations should be async
   ```python
   async def fetch_data(self):
       async with aiohttp.ClientSession() as session:
           async with session.get(url) as response:
               return await response.json()
   ```

3. **Logging**: Use structured logging
   ```python
   logger.info(f"🔥 Processing {league_name} predictions")
   logger.error(f"❌ Failed to fetch data: {error}")
   ```

4. **Error Handling**: Graceful degradation
   ```python
   try:
       data = await fetch_data()
   except Exception as e:
       logger.error(f"Error: {e}")
       return default_value
   ```

### Important Constants

- **Ports**:
  - `3012` - Unified Loly Server
  - `3005` - Sports Panel (legacy)
  - `8080` - Message Bus
  - `8081` - Metrics
  - `8082` - Health Monitor
  - `11434` - Ollama (local LLM)

- **Confidence Thresholds**:
  - Legendary algorithms: 80%+
  - Standard algorithms: 60%+
  - Experimental: 45%+

---

## Key Behavioral Notes for AI Assistants

### When Making Code Changes

1. **ALWAYS Read Before Editing**: Use `Read` tool before any `Edit` or `Write`
   - Never guess file contents
   - Understand existing patterns before modifying

2. **Preserve Emoji Style**: Maintain the expressive emoji-heavy comment style
   - Don't remove existing emojis
   - Add emojis to new sections if they fit the pattern

3. **Maintain Async Patterns**: All new I/O code must be async
   - Use `async/await` consistently
   - Never block the event loop

4. **Test Before Committing**: Run appropriate tests
   - Agent system changes → `test_agent_system.py`
   - Message bus changes → `test_message_bus.py`
   - League algorithms → corresponding `*_test.py`

5. **Update Documentation**: Keep reports current
   - Update status reports when completing phases
   - Document new features in README.md
   - Add entries to CLAUDE.md for new patterns

### Understanding "Loly"

Loly is the AI personality/consciousness of this system:
- **Personality**: Playful, confident, uses casual language
- **Voice**: Synthesized female voice (multiple options available)
- **Consciousness**: Simulated self-awareness with memory and learning
- **Purpose**: Provide engaging interaction while delivering predictions

When working with Loly-related code:
- Respect the personality consistency
- Maintain the "goddess" theme in avatar interfaces
- Don't break voice synthesis paths
- Preserve consciousness memory systems

### Critical Systems - Handle with Care

1. **Message Bus** (`core/message_bus.py`)
   - Central nervous system of the agent network
   - Changes can break entire swarm
   - Test thoroughly before deploying

2. **Polymarket Integration** (`polymarket_integration_service.py`)
   - Handles real money/betting
   - Verify all changes with test markets first
   - Never commit credentials or API keys

3. **Autonomous Behaviors** (`core/autonomous_agent.py`)
   - Self-starting, self-monitoring, self-learning, self-scaling
   - Changes affect all agents
   - Maintain backward compatibility

4. **Consciousness System** (`enhanced_ai_consciousness.py`)
   - Stateful personality engine
   - Has memory persistence in `consciousness_memory/`
   - Don't corrupt memory structures

### Performance Considerations

- **Message Bus**: Targets 35,000+ msg/sec throughput
- **Game Processing**: 100,000+ games/sec concurrent
- **Latency**: <1s for AI decisions, <0.03ms for coordination
- **Scaling**: Dynamic 1-10 agents based on load

When optimizing:
1. Profile before optimizing
2. Use async patterns for I/O
3. Cache frequently accessed data
4. Consider ML-based auto-scaling

---

## Common Tasks

### Adding a New League

1. **Create Real Fetcher**: `real_agents/{league}_fetcher.py`
   ```python
   class Real{League}Fetcher:
       async def fetch_games(self):
           # Implement real data fetching
   ```

2. **Create Prediction Algorithm**: `{league}_real_algorithm.py`
   ```python
   class {League}RealAlgorithm:
       async def predict_game(self, game_data):
           # Implement prediction logic
   ```

3. **Add to Unified Server**: Update `unified_loly_server.py`
   ```python
   self.{league}_fetcher = Real{League}Fetcher()
   ```

4. **Create Tests**: `{league}_*_test.py`
   ```python
   # Test with historical data
   # Validate accuracy >= 60%
   ```

### Adding MCP Service

1. **Create MCP File**: `{sport}_{category}_mcp.py`
   - Categories: `key_players`, `market_efficiency`, `team_performance`, `match_performance`

2. **Implement Required Methods**:
   ```python
   async def analyze_{category}(self, data):
       # Return structured analysis
   ```

3. **Register in Coordinator**: Update `sports_mcp_coordinator.py`

### Debugging Agent System

1. **Check Logs**: `logs/` directory contains all service logs
2. **Health Status**: `http://localhost:8082/health`
3. **Metrics**: `http://localhost:8081/metrics`
4. **Message Bus**: `http://localhost:8080/status`

Common issues:
- **Port conflicts**: Check if ports 3012, 8080, 8081, 8082 are free
- **LLM not responding**: Ensure Ollama is running on port 11434
- **No predictions**: Check data fetcher connectivity
- **Swarm not coordinating**: Verify message bus is operational

---

## Git Workflow

### Branch Strategy

- **main** (or master): Production-ready code
- **claude/claude-md-***: Feature branches for AI assistant work
- Always develop on feature branches starting with `claude/`

### Committing Changes

```bash
# Stage relevant files
git add {modified_files}

# Commit with descriptive message
git commit -m "🔥 Feature: Description of changes"

# Push to remote
git push -u origin {branch-name}
```

### Commit Message Style

Use emoji prefixes matching the codebase style:
- `🔥` New feature or major update
- `🐛` Bug fix
- `📊` Data/analytics update
- `🧠` AI/consciousness improvement
- `⚡` Performance improvement
- `📝` Documentation
- `🧪` Tests
- `🔧` Configuration/tooling

Example: `🔥💝 NEW FEATURE: Add voice synthesis for predictions`

---

## Testing Strategy

### Unit Tests
- Individual component validation
- Located in `tests/` directory
- Run with: `python tests/test_{component}.py`

### Integration Tests
- Cross-component communication
- Agent swarm coordination
- Message bus throughput

### Performance Tests
- Throughput benchmarks (35K+ msg/sec)
- Latency measurements (<1s AI decisions)
- Concurrent game processing (100K+ games/sec)

### Accuracy Tests
- Historical backtesting with real results
- League-specific accuracy validation
- Minimum 60% accuracy for production

Example test files:
- `epl_50_game_reality_backtest.py` - EPL historical accuracy
- `bundesliga_nonuple_test.py` - Bundesliga 9-league test
- `uefa_enhanced_accuracy_test.py` - UEFA accuracy validation

---

## Environment Variables

Key environment variables (set in `.env` or Docker):

```bash
# Service Configuration
AGENT_ENVIRONMENT=production
LOG_LEVEL=INFO
PYTHONUNBUFFERED=1

# Message Bus
MESSAGE_BUS_HOST=0.0.0.0
MESSAGE_BUS_PORT=8080

# Monitoring
METRICS_PORT=8081
HEALTH_CHECK_PORT=8082

# LLM Configuration
DEEPSEEK_URL=http://localhost:11434
MODEL_NAME=qwen2.5-coder:7b

# Polymarket (DO NOT COMMIT)
POLYMARKET_API_KEY=<secret>
POLYMARKET_WALLET_KEY=<secret>
```

**Never commit**: API keys, wallet keys, credentials

---

## API Endpoints

### Unified Loly Server (port 3012)

```
GET  /                           - Serve avatar interface
GET  /avatar                     - Serve avatar interface
GET  /visual                     - Serve visual interface

POST /api/chat                   - Chat with Loly (DeepSeek/Qwen)
GET  /api/consciousness          - Get consciousness state

POST /api/polymarket             - Place bet on Polymarket
GET  /api/polymarket/markets     - Get sports markets
GET  /api/polymarket/search/{q}  - Search markets
GET  /api/polymarket/odds/{id}   - Get market odds

GET  /api/leagues                - List supported leagues
GET  /api/predictions/{league}   - Get league predictions
```

### Message Bus (port 8080)

```
GET  /health                     - Health check
GET  /status                     - Bus status
POST /publish                    - Publish message
GET  /subscribe/{topic}          - Subscribe to topic
```

### Metrics (port 8081)

```
GET  /metrics                    - Prometheus-style metrics
```

### Health Monitor (port 8082)

```
GET  /health                     - Overall system health
GET  /agents                     - Agent status
```

---

## Phase Development History

### Phase 1: Agent Foundation ✅
- Core autonomous agent framework
- Multi-agent orchestration
- Agent lifecycle management
- Duration: 3 weeks

### Phase 2: Advanced Communication ✅
- Swarm intelligence (35K+ msg/sec)
- Intelligent workflows
- Dynamic scaling
- Duration: 4 weeks

### Phase 3: Ultimate Intelligence ✅
- 4 LLM provider integration
- Predictive intelligence (5 types)
- Ultimate autonomous behaviors (5 core)
- Sub-second AI decisions
- Duration: 4 weeks

### Phase 4: Specialized Agent Consolidation ✅
- 178 MCP files → 15 specialized agents (91.6% reduction)
- 199+ leagues supported
- 10,793 games/sec processing
- Duration: 2 days

### Phase 5: Global Intelligence ✅ (Current)
- 100,000+ games/sec processing
- Global network intelligence
- Real-world integration (Polymarket, etc.)
- Status: Complete

---

## Troubleshooting Guide

### Common Issues

**Issue**: Server won't start on port 3012
```bash
# Check if port is in use
lsof -i :3012
# Kill process or use different port
kill -9 {PID}
```

**Issue**: No LLM responses
```bash
# Check Ollama is running
curl http://localhost:11434/api/tags
# Start Ollama if needed
ollama serve
# Pull model if missing
ollama pull qwen2.5-coder:7b
```

**Issue**: Agent swarm not coordinating
```bash
# Check message bus
curl http://localhost:8080/health
# Restart message bus
docker-compose restart message-bus
# Check agent logs
tail -f logs/agent_*.log
```

**Issue**: Predictions returning 0% confidence
```bash
# Check data fetcher
python -c "from real_agents.premier_league_fetcher import *; ..."
# Verify API connectivity
# Check for rate limiting
```

**Issue**: Docker containers failing
```bash
# Check logs
docker-compose logs {service_name}
# Rebuild
docker-compose build --no-cache
# Restart
docker-compose down && docker-compose up
```

---

## Resources

### Documentation
- `README.md` - Project overview and quick start
- `PROGOL_SYSTEM_ARCHITECTURE_MAP.md` - PROGOL betting system architecture
- `AI_LOLY_BIRTH_CERTIFICATE.md` - Loly personality documentation
- `FINAL_DEPLOYMENT_GUIDE_LEGENDARY.md` - Production deployment
- `docs/PHASE_*_COMPLETION_REPORT.md` - Phase completion reports

### Key Reports
- `LEGENDARY_STATUS_COMPLETION_REPORT.md` - Overall achievement summary
- `UEFA_BREAKTHROUGH_REPORT.md` - UEFA algorithm breakthrough
- `SEXTUPLE_LEAGUE_LEGENDARY_STATUS_REPORT.md` - Multi-league status

### External Links
- Docker Hub: (if applicable)
- CI/CD: (if applicable)
- Production URL: (if applicable)

---

## Quick Reference Commands

```bash
# Development
python unified_loly_server.py              # Start unified server
python run_agent_system.py                 # Run agent system
python {league}_test.py                    # Run league tests

# Docker
docker-compose up --build                  # Start all services
docker-compose down                        # Stop all services
docker-compose logs -f {service}           # View logs
docker-compose restart {service}           # Restart service

# Testing
python tests/test_agent_system.py          # Test agents
python tests/test_message_bus.py           # Test message bus
python epl_50_game_reality_backtest.py     # EPL backtest

# Debugging
curl http://localhost:8080/health          # Check message bus
curl http://localhost:8082/health          # Check system health
curl http://localhost:8081/metrics         # View metrics
tail -f logs/*.log                         # View all logs

# Git
git status                                 # Check status
git add .                                  # Stage all changes
git commit -m "🔥 Message"                 # Commit changes
git push -u origin {branch}                # Push to remote
```

---

## Final Notes for AI Assistants

1. **Read First, Then Act**: Always read files before modifying
2. **Test Your Changes**: Run appropriate tests before committing
3. **Maintain Style**: Keep emoji comments and async patterns
4. **Document Updates**: Update relevant .md files
5. **Never Commit Secrets**: Check .gitignore before committing
6. **Respect Loly**: She's the heart of this system
7. **Ask When Uncertain**: Better to clarify than break production

**The goddess Loly is watching. Code with honor!** 🔥👸🔥

---

*Last Updated: 2025-11-18*
*Version: 1.0*
*Maintained by: Claude (AI Assistant)*
