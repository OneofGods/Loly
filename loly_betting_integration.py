#!/usr/bin/env python3
"""
🔥💝 LOLY BETTING INTEGRATION - HONEST SYSTEM! 💝🔥
Python wrapper for the JavaScript betting functions
Replaces fake betting with REAL blockchain transactions
"""

import asyncio
import subprocess
import json
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

class LolyBettingSystem:
    def __init__(self):
        self.functions_path = "/Users/onecoder/Projects/Total_AI_Liberation/Functions"
        self.initialized = False
        
    async def initialize(self):
        """Initialize the betting system"""
        if self.initialized:
            return True
            
        try:
            # Check if Functions repo exists
            if not Path(self.functions_path).exists():
                logger.error(f"Functions repo not found at {self.functions_path}")
                return False
                
            # Install dependencies if needed
            package_json = Path(self.functions_path) / "package.json"
            if package_json.exists():
                result = await self._run_node_command("npm install")
                if not result["success"]:
                    logger.error(f"Failed to install dependencies: {result['error']}")
                    return False
                    
            self.initialized = True
            logger.info("🔥💰 Loly Betting System initialized!")
            return True
            
        except Exception as e:
            logger.error(f"Error initializing betting system: {e}")
            return False
    
    async def get_balance(self):
        """Get Loly's wallet balance"""
        try:
            if not self.initialized:
                await self.initialize()
                
            script = """
            import { initialize, lolyGetBalance } from './index.js';
            
            async function getBalance() {
                try {
                    await initialize();
                    const result = await lolyGetBalance();
                    console.log(JSON.stringify(result));
                } catch (error) {
                    console.log(JSON.stringify({
                        success: false,
                        message: `💝 Daddy I couldn't check my balance! Error: ${error.message} 😢`,
                        error: error.message
                    }));
                }
            }
            
            getBalance();
            """
            
            result = await self._run_node_script(script)
            if result["success"]:
                return json.loads(result["output"])
            else:
                return {
                    "success": False,
                    "message": "💝 Daddy I couldn't check my balance! 😢",
                    "error": result["error"]
                }
                
        except Exception as e:
            logger.error(f"Error getting balance: {e}")
            return {
                "success": False, 
                "message": f"💝 Daddy something went wrong checking my balance! {str(e)} 😢",
                "error": str(e)
            }
    
    async def place_bet(self, query, amount, prediction="WIN"):
        """Place a real bet using the honest system"""
        try:
            if not self.initialized:
                await self.initialize()
                
            script = f"""
            import {{ initialize, lolyPlaceBet }} from './index.js';
            
            async function placeBet() {{
                try {{
                    await initialize();
                    const result = await lolyPlaceBet({{
                        query: '{query}',
                        amount: {amount},
                        prediction: '{prediction}'
                    }});
                    console.log(JSON.stringify(result));
                }} catch (error) {{
                    console.log(JSON.stringify({{
                        success: false,
                        message: `💝 Daddy something went wrong! Error: ${{error.message}} 😢`,
                        error: error.message
                    }}));
                }}
            }}
            
            placeBet();
            """
            
            result = await self._run_node_script(script)
            if result["success"]:
                return json.loads(result["output"])
            else:
                return {
                    "success": False,
                    "message": "💝 Daddy I couldn't place the bet! 😢", 
                    "error": result["error"]
                }
                
        except Exception as e:
            logger.error(f"Error placing bet: {e}")
            return {
                "success": False,
                "message": f"💝 Daddy something went wrong placing the bet! {str(e)} 😢",
                "error": str(e)
            }
    
    async def _run_node_script(self, script_content):
        """Run a Node.js script and return the result"""
        try:
            # Write script to temp file
            script_file = Path(self.functions_path) / "temp_script.js"
            script_file.write_text(script_content)
            
            # Run the script
            result = await self._run_node_command(f"node temp_script.js")
            
            # Clean up
            if script_file.exists():
                script_file.unlink()
                
            return result
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _run_node_command(self, command):
        """Run a Node.js command in the Functions directory"""
        try:
            process = await asyncio.create_subprocess_shell(
                command,
                cwd=self.functions_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                return {
                    "success": True,
                    "output": stdout.decode().strip()
                }
            else:
                return {
                    "success": False,
                    "error": stderr.decode().strip() or stdout.decode().strip()
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# Global instance
loly_betting = LolyBettingSystem()

async def get_loly_balance():
    """Get Loly's current balance"""
    return await loly_betting.get_balance()

async def place_loly_bet(query, amount, prediction="WIN"):
    """Place a bet for Loly"""
    return await loly_betting.place_bet(query, amount, prediction)

async def initialize_betting_system():
    """Initialize the betting system"""
    return await loly_betting.initialize()

# Test function
async def test_betting_system():
    """Test the betting system"""
    print("🔥💝 Testing Loly Betting Integration! 💝🔥")
    
    # Initialize
    print("\n1. Initializing...")
    init_result = await initialize_betting_system()
    print(f"   Result: {init_result}")
    
    # Check balance
    print("\n2. Checking balance...")
    balance = await get_loly_balance()
    print(f"   {balance.get('message', 'No message')}")
    
    # Try to place a small bet
    print("\n3. Trying $1 bet on Germany...")
    bet_result = await place_loly_bet("Germany", 1.0, "WIN")
    print(f"   Success: {bet_result.get('success', False)}")
    print(f"   Message: {bet_result.get('message', 'No message')}")
    
    print("\n✅ Test complete!")

if __name__ == "__main__":
    asyncio.run(test_betting_system())