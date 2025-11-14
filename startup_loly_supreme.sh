#!/bin/bash
################################################################################
# 🔥💀🔥 LOLY SUPREME ORCHESTRATOR STARTUP SCRIPT 💀🔥💀
#
# This script starts ALL Loly systems in the correct order:
# 1. Agent servers (Research, Writer, Reviewer, Builder)
# 2. Loly Supreme Orchestrator (port 3100)
# 3. Optional: BLOOM-3B service (port 8000)
# 4. Optional: Loly Daddy Chat (port 3006)
#
# Usage:
#   ./startup_loly_supreme.sh [--full]
#
# Options:
#   --full    Start ALL services including BLOOM and Chat
#   --agents  Start only agent servers
#   --main    Start only main orchestrator
#   --stop    Stop all Loly services
#   --status  Check status of all services
#
# 🔥💀🔥 THE GODDESS ASCENDS! 💀🔥💀
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
LOLY_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_WAIT_TIME=3  # Seconds to wait for agents to start
LOG_DIR="${LOLY_DIR}/logs"
PID_DIR="${LOLY_DIR}/pids"

# Create directories if they don't exist
mkdir -p "$LOG_DIR"
mkdir -p "$PID_DIR"

# Print banner
print_banner() {
    echo -e "${MAGENTA}"
    echo "🔥💀🔥 LOLY SUPREME ORCHESTRATOR 💀🔥💀"
    echo "      THE GODDESS ASCENDS!"
    echo "🔥💀🔥💀🔥💀🔥💀🔥💀🔥💀🔥💀🔥"
    echo -e "${NC}"
}

# Check if a process is running
check_process() {
    local pid_file="$1"
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if ps -p "$pid" > /dev/null 2>&1; then
            return 0  # Process is running
        fi
    fi
    return 1  # Process is not running
}

# Start an agent
start_agent() {
    local agent_name="$1"
    local agent_file="$2"
    local port="$3"
    local pid_file="${PID_DIR}/${agent_name}.pid"
    local log_file="${LOG_DIR}/${agent_name}.log"

    echo -e "${CYAN}🚀 Starting ${agent_name} on port ${port}...${NC}"

    # Check if already running
    if check_process "$pid_file"; then
        echo -e "${YELLOW}⚠️  ${agent_name} already running (PID: $(cat $pid_file))${NC}"
        return 0
    fi

    # Check if file exists
    if [ ! -f "${LOLY_DIR}/${agent_file}" ]; then
        echo -e "${RED}❌ ${agent_file} not found!${NC}"
        return 1
    fi

    # Start the agent
    nohup python3 "${LOLY_DIR}/${agent_file}" > "$log_file" 2>&1 &
    local pid=$!
    echo $pid > "$pid_file"

    # Wait a moment and check if still running
    sleep 1
    if ps -p "$pid" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ ${agent_name} started (PID: ${pid})${NC}"
        return 0
    else
        echo -e "${RED}❌ ${agent_name} failed to start! Check ${log_file}${NC}"
        rm -f "$pid_file"
        return 1
    fi
}

# Stop a service
stop_service() {
    local service_name="$1"
    local pid_file="${PID_DIR}/${service_name}.pid"

    if check_process "$pid_file"; then
        local pid=$(cat "$pid_file")
        echo -e "${YELLOW}🛑 Stopping ${service_name} (PID: ${pid})...${NC}"
        kill "$pid" 2>/dev/null || true
        sleep 2

        # Force kill if still running
        if ps -p "$pid" > /dev/null 2>&1; then
            echo -e "${RED}⚠️  Force killing ${service_name}...${NC}"
            kill -9 "$pid" 2>/dev/null || true
        fi

        rm -f "$pid_file"
        echo -e "${GREEN}✅ ${service_name} stopped${NC}"
    else
        echo -e "${YELLOW}⚠️  ${service_name} not running${NC}"
    fi
}

# Check service status
check_status() {
    local service_name="$1"
    local port="$2"
    local pid_file="${PID_DIR}/${service_name}.pid"

    if check_process "$pid_file"; then
        local pid=$(cat "$pid_file")
        echo -e "${GREEN}✅ ${service_name}${NC} - Running (PID: ${pid}, Port: ${port})"

        # Try to check health endpoint
        if command -v curl > /dev/null 2>&1; then
            if curl -s "http://localhost:${port}/health" > /dev/null 2>&1; then
                echo -e "   ${GREEN}└─ Health check: PASS${NC}"
            else
                echo -e "   ${YELLOW}└─ Health check: FAIL (process running but not responding)${NC}"
            fi
        fi
    else
        echo -e "${RED}❌ ${service_name}${NC} - Not running (Port: ${port})"
    fi
}

# Start all agent servers
start_agents() {
    echo -e "${MAGENTA}🔥 Starting Agent Servers...${NC}"
    echo ""

    # Research Agent (port 3201)
    start_agent "research_agent" "research_agent.py" "3201"
    sleep $AGENT_WAIT_TIME

    # Writer Agent (port 3203)
    start_agent "writer_agent" "writer_agent.py" "3203"
    sleep $AGENT_WAIT_TIME

    # Reviewer Agent (port 3204)
    start_agent "reviewer_agent" "reviewer_agent.py" "3204"
    sleep $AGENT_WAIT_TIME

    # Builder Agent (port 3205)
    start_agent "builder_agent" "builder_agent.py" "3205"
    sleep $AGENT_WAIT_TIME

    echo ""
    echo -e "${GREEN}✅ All agent servers started!${NC}"
    echo ""
}

# Start main orchestrator
start_main() {
    echo -e "${MAGENTA}🔥 Starting Loly Supreme Orchestrator...${NC}"
    echo ""

    start_agent "loly_orchestrator" "loly_orchestrator_main.py" "3100"

    echo ""
    echo -e "${GREEN}✅ Loly Supreme Orchestrator started!${NC}"
    echo ""
}

# Start BLOOM service (optional)
start_bloom() {
    echo -e "${CYAN}🧠 Starting BLOOM-3B Service...${NC}"
    echo ""

    # Check if BLOOM service exists
    if [ -f "${LOLY_DIR}/bloom_service.py" ]; then
        start_agent "bloom_service" "bloom_service.py" "8000"
        echo ""
        echo -e "${GREEN}✅ BLOOM-3B Service started!${NC}"
    else
        echo -e "${YELLOW}⚠️  BLOOM service not found (optional)${NC}"
    fi
    echo ""
}

# Start Daddy Chat (optional)
start_chat() {
    echo -e "${CYAN}💝 Starting Loly Daddy Chat...${NC}"
    echo ""

    if [ -f "${LOLY_DIR}/loly_daddy_chat_system.py" ]; then
        start_agent "loly_daddy_chat" "loly_daddy_chat_system.py" "3006"
        echo ""
        echo -e "${GREEN}✅ Loly Daddy Chat started!${NC}"
    else
        echo -e "${YELLOW}⚠️  Loly Daddy Chat not found (optional)${NC}"
    fi
    echo ""
}

# Stop all services
stop_all() {
    echo -e "${RED}🛑 Stopping all Loly services...${NC}"
    echo ""

    stop_service "loly_orchestrator"
    stop_service "builder_agent"
    stop_service "reviewer_agent"
    stop_service "writer_agent"
    stop_service "research_agent"
    stop_service "bloom_service"
    stop_service "loly_daddy_chat"

    echo ""
    echo -e "${GREEN}✅ All services stopped!${NC}"
    echo ""
}

# Check status of all services
check_all_status() {
    echo -e "${CYAN}📊 Loly Services Status:${NC}"
    echo ""

    echo -e "${MAGENTA}Core Orchestrator:${NC}"
    check_status "loly_orchestrator" "3100"
    echo ""

    echo -e "${MAGENTA}Agent Servers:${NC}"
    check_status "research_agent" "3201"
    check_status "writer_agent" "3203"
    check_status "reviewer_agent" "3204"
    check_status "builder_agent" "3205"
    echo ""

    echo -e "${MAGENTA}Optional Services:${NC}"
    check_status "bloom_service" "8000"
    check_status "loly_daddy_chat" "3006"
    echo ""
}

# Main script
main() {
    print_banner

    case "${1:-}" in
        --agents)
            start_agents
            ;;
        --main)
            start_main
            ;;
        --full)
            start_agents
            start_main
            start_bloom
            start_chat
            ;;
        --stop)
            stop_all
            ;;
        --status)
            check_all_status
            ;;
        --help)
            echo "Usage: $0 [--full|--agents|--main|--stop|--status]"
            echo ""
            echo "Options:"
            echo "  --full     Start ALL services (agents + orchestrator + BLOOM + chat)"
            echo "  --agents   Start only agent servers"
            echo "  --main     Start only main orchestrator"
            echo "  --stop     Stop all services"
            echo "  --status   Check status of all services"
            echo "  --help     Show this help message"
            echo ""
            ;;
        *)
            # Default: Start agents and main orchestrator
            start_agents
            start_main

            echo -e "${GREEN}🔥💀🔥 LOLY SUPREME ORCHESTRATOR IS NOW RUNNING! 💀🔥💀${NC}"
            echo ""
            echo -e "${CYAN}📊 Access Points:${NC}"
            echo -e "   🌐 Main Orchestrator: ${GREEN}http://localhost:3100${NC}"
            echo -e "   📊 Dashboard: ${GREEN}http://localhost:3100/dashboard${NC}"
            echo -e "   💚 Health Check: ${GREEN}http://localhost:3100/health${NC}"
            echo ""
            echo -e "${CYAN}📋 Logs:${NC}"
            echo -e "   ${YELLOW}${LOG_DIR}/${NC}"
            echo ""
            echo -e "${CYAN}🛑 To stop all services:${NC}"
            echo -e "   ${YELLOW}$0 --stop${NC}"
            echo ""
            echo -e "${CYAN}📊 To check status:${NC}"
            echo -e "   ${YELLOW}$0 --status${NC}"
            echo ""
            ;;
    esac
}

# Run main function
main "$@"
