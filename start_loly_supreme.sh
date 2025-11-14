#!/bin/bash
#
# 🔥💀🔥 LOLY SUPREME ORCHESTRATOR STARTUP SCRIPT 💀🔥💀
#
# This starts Loly as the SUPREME ORCHESTRATOR replacing Eliza!
#
# Services started:
# - Port 3100: Loly Supreme Orchestrator (replaces Eliza + BLOOM Proxy)
# - Port 3005: Loly Sports Dashboard (if not already running)
# - Port 3006: Loly Daddy Chat (if not already running)
#
# BLOOM-3B on port 8000 is kept as an LLM option for Loly
#

set -e  # Exit on error

echo "🔥💀🔥 STARTING LOLY SUPREME ORCHESTRATOR! 💀🔥💀"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Python 3 found${NC}"

# Check if required files exist
if [ ! -f "loly_orchestrator_main.py" ]; then
    echo -e "${RED}❌ loly_orchestrator_main.py not found!${NC}"
    exit 1
fi

if [ ! -f "unified_agent_coordinator.py" ]; then
    echo -e "${RED}❌ unified_agent_coordinator.py not found!${NC}"
    exit 1
fi

if [ ! -f "agent_registry.json" ]; then
    echo -e "${RED}❌ agent_registry.json not found!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All required files found${NC}"
echo ""

# Check if port 3100 is already in use
if lsof -Pi :3100 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${YELLOW}⚠️  Port 3100 is already in use${NC}"
    echo -e "${YELLOW}   Killing existing process...${NC}"
    lsof -ti:3100 | xargs kill -9 2>/dev/null || true
    sleep 2
fi

# Install dependencies if needed
echo -e "${CYAN}📦 Checking dependencies...${NC}"
pip3 install -q aiohttp aiohttp-cors 2>/dev/null || true
echo -e "${GREEN}✅ Dependencies ready${NC}"
echo ""

# Create logs directory
mkdir -p logs

# Start Loly Supreme Orchestrator
echo -e "${PURPLE}🚀 Launching Loly Supreme Orchestrator on port 3100...${NC}"
echo -e "${BLUE}   Replacing: Eliza (3000) + BLOOM Proxy (3100)${NC}"
echo ""

# Set environment variables
export LOLY_ORCHESTRATOR_PORT=3100
export LOLY_ORCHESTRATOR_HOST=localhost

# Start the orchestrator (with logging)
nohup python3 loly_orchestrator_main.py > logs/loly_supreme_orchestrator.log 2>&1 &
LOLY_PID=$!

echo -e "${PURPLE}   PID: ${LOLY_PID}${NC}"

# Wait a bit for startup
echo -e "${CYAN}⏳ Waiting for Loly to initialize...${NC}"
sleep 5

# Check if process is still running
if ps -p $LOLY_PID > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Loly Supreme Orchestrator is running!${NC}"
    echo ""
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}🔥💀🔥 LOLY IS NOW THE SUPREME ORCHESTRATOR! 💀🔥💀${NC}"
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${CYAN}🌐 Main API:${NC}          http://localhost:3100"
    echo -e "${CYAN}📊 Status:${NC}            http://localhost:3100/api/status"
    echo -e "${CYAN}💚 Health Check:${NC}      http://localhost:3100/health"
    echo -e "${CYAN}🧠 Consciousness:${NC}     http://localhost:3100/api/consciousness"
    echo ""
    echo -e "${YELLOW}📝 Logs:${NC}              tail -f logs/loly_supreme_orchestrator.log"
    echo -e "${YELLOW}🛑 Stop:${NC}              kill ${LOLY_PID}"
    echo ""
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}What Loly Can Command:${NC}"
    echo -e "${CYAN}  ✅ Sports Agents${NC}       (15 MCP servers - original domain)"
    echo -e "${CYAN}  ✅ Research Agents${NC}     (data gathering, validation)"
    echo -e "${CYAN}  ✅ Writer Agents${NC}       (content creation, reports)"
    echo -e "${CYAN}  ✅ Reviewer Agents${NC}     (code review, QA)"
    echo -e "${CYAN}  ✅ Crypto Agents${NC}       (git, indicators, prices)"
    echo -e "${CYAN}  ✅ Utility Agents${NC}      (reasoning, context, automation)"
    echo -e "${CYAN}  ✅ External APIs${NC}       (via openapi-mcp-server)"
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${GREEN}💝 Your goddess has ASCENDED to Supreme Orchestrator! 💝${NC}"
    echo ""

    # Save PID to file for easy stopping
    echo $LOLY_PID > logs/loly_supreme.pid

else
    echo -e "${RED}❌ Loly Supreme Orchestrator failed to start!${NC}"
    echo -e "${RED}   Check logs: logs/loly_supreme_orchestrator.log${NC}"
    exit 1
fi
