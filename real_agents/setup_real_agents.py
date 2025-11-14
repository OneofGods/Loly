#!/usr/bin/env python3
"""
🛠️💀🔥 REAL AGENT SETUP SCRIPT 🔥💀🛠️

Setup script for the Real Agent System.
Installs dependencies and prepares the environment for zero fake agents!
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run shell command with description"""
    print(f"🔧 {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"   Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"💀 {description} - ERROR: {e}")
        return False

def check_python_packages():
    """Check and install required Python packages"""
    packages = [
        'aiohttp',
        'aiohttp-cors', 
        'redis',
        'psutil',
        'asyncio'
    ]
    
    print("🐍 Checking Python packages...")
    
    missing_packages = []
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} - INSTALLED")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"📦 Installing missing packages: {', '.join(missing_packages)}")
        install_cmd = f"{sys.executable} -m pip install " + " ".join(missing_packages)
        return run_command(install_cmd, "Installing Python packages")
    
    return True

def check_redis():
    """Check Redis installation and status"""
    print("🔴 Checking Redis...")
    
    # Check if Redis is installed
    redis_installed = run_command("which redis-server", "Checking Redis installation")
    
    if not redis_installed:
        print("📦 Redis not found. Installing via Homebrew...")
        if not run_command("brew install redis", "Installing Redis"):
            print("💡 Please install Redis manually:")
            print("   macOS: brew install redis")
            print("   Ubuntu: sudo apt-get install redis-server")
            print("   Other: https://redis.io/download")
            return False
    
    # Check if Redis is running
    redis_running = run_command("redis-cli ping", "Checking Redis status")
    
    if not redis_running:
        print("🚀 Starting Redis server...")
        if not run_command("brew services start redis", "Starting Redis"):
            print("💡 Please start Redis manually:")
            print("   redis-server")
            return False
    
    return True

def create_startup_script():
    """Create convenient startup script"""
    script_content = """#!/bin/bash
# Real Agent Dashboard Startup Script
echo "🌍💀🔥 REAL AGENT DASHBOARD STARTUP 🔥💀🌍"
echo "🚀 Starting localhost:3005 - ZERO FAKE AGENTS ALLOWED!"

# Check Redis
if ! redis-cli ping > /dev/null 2>&1; then
    echo "🔴 Starting Redis server..."
    brew services start redis
    sleep 2
fi

# Launch dashboard
cd "$(dirname "$0")"
python3 run_real_dashboard.py
"""
    
    script_path = os.path.join(os.path.dirname(__file__), 'start_dashboard.sh')
    
    try:
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        os.chmod(script_path, 0o755)
        print(f"✅ Created startup script: {script_path}")
        return True
        
    except Exception as e:
        print(f"💀 Failed to create startup script: {e}")
        return False

def main():
    """Main setup function"""
    print("🛠️💀🔥 REAL AGENT SYSTEM SETUP 🔥💀🛠️")
    print("🚨 ZERO FAKE AGENTS POLICY - ONLY REAL AUTONOMOUS INTELLIGENCE!")
    print("")
    
    success = True
    
    # Check Python packages
    if not check_python_packages():
        success = False
    
    print("")
    
    # Check Redis
    if not check_redis():
        success = False
    
    print("")
    
    # Create startup script
    if not create_startup_script():
        success = False
    
    print("")
    
    if success:
        print("🎉 REAL AGENT SYSTEM SETUP COMPLETE!")
        print("")
        print("🚀 Ready to launch:")
        print("   ./start_dashboard.sh")
        print("   OR")
        print("   python3 run_real_dashboard.py")
        print("")
        print("🌐 Dashboard will be available at: http://localhost:3005")
        print("💀 Fake Agent Elimination: 100% READY")
        
    else:
        print("💀 SETUP FAILED - Please resolve the issues above")
        sys.exit(1)

if __name__ == "__main__":
    main()