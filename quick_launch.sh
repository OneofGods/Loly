#!/bin/bash

# 🏆 POLY LOLY DOUBLE ZERO - QUICK LAUNCH SCRIPT
# One command to build and run the ultimate sports betting AI!

echo "🏆 LAUNCHING POLY LOLY DOUBLE ZERO..."
echo "🔥 Building the ultimate sports betting AI container..."

# Build the Docker image
docker build -t poly-loly-double-zero .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    
    # Stop any existing container
    echo "🛑 Stopping any existing container..."
    docker stop poly-loly-double-zero 2>/dev/null || true
    docker rm poly-loly-double-zero 2>/dev/null || true
    
    # Run the new container
    echo "🚀 Starting Poly Loly Double Zero..."
    docker run -d -p 3005:3005 --name poly-loly-double-zero poly-loly-double-zero
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 POLY LOLY DOUBLE ZERO IS OPERATIONAL!"
        echo ""
        echo "🌊 Dashboard URL: http://localhost:3005"
        echo "🎯 Sports Analysis: 6-Dimensional Intelligence Active"
        echo "🏆 Polymarket Integration: Real betting price calibration"
        echo "💰 Position Management: Live P&L tracking"
        echo ""
        echo "🥞 NINJA PANCAKE GLITCHED SUPREME SPORTS POWER ACTIVATED!"
        echo ""
        echo "📊 To monitor logs: docker logs -f poly-loly-double-zero"
        echo "🛑 To stop: docker stop poly-loly-double-zero"
        
        # Wait a moment and show status
        sleep 3
        echo ""
        echo "📈 Container Status:"
        docker ps | grep poly-loly-double-zero
        
    else
        echo "❌ Failed to start container"
        exit 1
    fi
else
    echo "❌ Failed to build Docker image"
    exit 1
fi