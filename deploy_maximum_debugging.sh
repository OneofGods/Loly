#!/bin/bash

echo "🔥💀🔥 DEPLOYING LOLY MAXIMUM DEBUGGING EMPIRE 💀🔥💀"
echo ""

# Check if logs directory exists
if [ ! -d "logs" ]; then
    echo "📁 Creating logs directory..."
    mkdir -p logs
fi

# Check Python dependencies
echo "🔍 Checking Python dependencies..."
python3 -c "import aiohttp, aiohttp_cors, asyncio" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing required packages..."
    pip3 install aiohttp aiohttp-cors
fi

echo ""
echo "🚀 DEPLOYMENT OPTIONS:"
echo "1. 🔥 Start LOLY Maximum Debugging Monitoring"
echo "2. 💖 Launch LOLY Debug Dashboard (localhost:3007)"  
echo "3. 🏆 Deploy Complete MAXIMUM DEBUGGING EMPIRE"
echo "4. 📊 Check System Status"
echo ""

read -p "Select option (1-4): " choice

case $choice in
    1)
        echo "🔥💀🔥 Starting LOLY Maximum Debugging Monitoring..."
        python3 loly_maximum_debugging_minion_control.py
        ;;
    2)
        echo "💖 Launching LOLY Debug Dashboard..."
        echo "🌐 Dashboard will be available at: http://localhost:3007"
        python3 loly_minion_debug_dashboard.py
        ;;
    3)
        echo "🏆💀🏆 DEPLOYING COMPLETE MAXIMUM DEBUGGING EMPIRE! 💀🏆💀"
        echo ""
        echo "🔥 Starting monitoring system in background..."
        python3 loly_maximum_debugging_minion_control.py &
        MONITOR_PID=$!
        
        sleep 3
        
        echo "💖 Starting debug dashboard..."
        echo "🌐 Dashboard available at: http://localhost:3007"
        echo "💀 Monitoring PID: $MONITOR_PID"
        echo ""
        echo "📋 EMPIRE STATUS:"
        echo "   ✅ Maximum Debugging Monitoring: ACTIVE"
        echo "   ✅ Interactive Debug Dashboard: RUNNING"
        echo "   ✅ Real-time Minion Control: ONLINE"
        echo "   ✅ Emergency Recovery Protocols: ARMED"
        echo ""
        echo "💖 LOLY is now ready with MAXIMUM DEBUGGING POWER!"
        echo "🛑 Press Ctrl+C to shutdown the empire"
        
        python3 loly_minion_debug_dashboard.py
        
        # Cleanup on exit
        echo ""
        echo "🛑 Shutting down MAXIMUM DEBUGGING EMPIRE..."
        kill $MONITOR_PID 2>/dev/null
        echo "✅ Empire shutdown complete"
        ;;
    4)
        echo "📊 Checking LOLY System Status..."
        echo ""
        
        # Check if processes are running
        MONITOR_RUNNING=$(pgrep -f "loly_maximum_debugging_minion_control.py" | wc -l)
        DASHBOARD_RUNNING=$(pgrep -f "loly_minion_debug_dashboard.py" | wc -l)
        
        echo "🔍 SYSTEM STATUS:"
        echo "   🔥 Maximum Debugging Monitor: $([ $MONITOR_RUNNING -gt 0 ] && echo '🟢 RUNNING' || echo '🔴 STOPPED')"
        echo "   💖 Debug Dashboard: $([ $DASHBOARD_RUNNING -gt 0 ] && echo '🟢 RUNNING' || echo '🔴 STOPPED')"
        
        # Check ports
        echo ""
        echo "🌐 PORT STATUS:"
        netstat -an | grep :3007 > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "   💖 Dashboard (3007): 🟢 ACTIVE"
        else
            echo "   💖 Dashboard (3007): 🔴 INACTIVE"
        fi
        
        netstat -an | grep :3005 > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "   🌍 Main Dashboard (3005): 🟢 ACTIVE"
        else
            echo "   🌍 Main Dashboard (3005): 🔴 INACTIVE"
        fi
        
        # Check log files
        echo ""
        echo "📋 LOG STATUS:"
        if [ -f "logs/loly_maximum_debugging.log" ]; then
            LOG_SIZE=$(wc -l < logs/loly_maximum_debugging.log)
            echo "   📄 Debug Log: $LOG_SIZE lines"
        else
            echo "   📄 Debug Log: Not found"
        fi
        
        echo ""
        echo "💡 QUICK ACCESS:"
        echo "   🌐 Debug Dashboard: http://localhost:3007"
        echo "   🌐 Main Dashboard: http://localhost:3005"
        ;;
    *)
        echo "❌ Invalid option. Please select 1-4."
        exit 1
        ;;
esac

echo ""
echo "🔥💀🔥 LOLY MAXIMUM DEBUGGING DEPLOYMENT COMPLETE! 💀🔥💀"