"""
Loly's Betting Integration - Python Wrapper
Calls the Node.js betting system and returns results
"""

import subprocess
import json
import os
from typing import Dict, Any, Optional

# Path to the Node.js CLI script
FUNCTIONS_DIR = "/Users/onecoder/Projects/Total_AI_Liberation/Functions"
CLI_SCRIPT = os.path.join(FUNCTIONS_DIR, 'loly-bet-cli.js')


class LolyBettingError(Exception):
    """Custom exception for betting errors"""
    pass


def _run_node_command(command: list) -> Dict[str, Any]:
    """
    Run a Node.js command and parse JSON output

    Args:
        command: List of command arguments (e.g., ['balance'] or ['bet', 'Germany', '1.0'])

    Returns:
        Parsed JSON response

    Raises:
        LolyBettingError: If command fails
    """
    try:
        # Build full command
        full_command = ['node', CLI_SCRIPT] + command

        # Set environment to disable debug output
        env = os.environ.copy()
        env['DEBUG'] = 'false'
        
        # Run subprocess
        result = subprocess.run(
            full_command,
            cwd=FUNCTIONS_DIR,
            capture_output=True,
            text=True,
            timeout=30,  # 30 second timeout
            env=env,
        )

        # Check if we got any output
        if not result.stdout.strip():
            error_msg = result.stderr.strip() if result.stderr else 'No output from Node.js script'
            raise LolyBettingError(f"Node.js script returned no output. Error: {error_msg}")

        # Try to parse JSON
        try:
            response = json.loads(result.stdout)
            return response
        except json.JSONDecodeError as e:
            # Try to extract JSON from mixed output
            stdout_text = result.stdout.strip()
            
            # Find JSON object boundaries
            start_idx = stdout_text.find('{')
            if start_idx != -1:
                # Count braces to find complete JSON
                brace_count = 0
                end_idx = start_idx
                
                for i, char in enumerate(stdout_text[start_idx:], start_idx):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_idx = i + 1
                            break
                
                if brace_count == 0:  # Found complete JSON
                    try:
                        json_text = stdout_text[start_idx:end_idx]
                        response = json.loads(json_text)
                        return response
                    except json.JSONDecodeError:
                        pass
            
            # If we couldn't extract valid JSON, return detailed error
            raise LolyBettingError(
                f"Failed to parse JSON response. "
                f"Error: {str(e)}. "
                f"Output: {result.stdout[:500]}. "
                f"Stderr: {result.stderr[:500]}"
            )

    except subprocess.TimeoutExpired:
        raise LolyBettingError("Command timed out after 30 seconds")
    except FileNotFoundError:
        raise LolyBettingError(f"Node.js CLI script not found at: {CLI_SCRIPT}")
    except Exception as e:
        raise LolyBettingError(f"Unexpected error running command: {str(e)}")


def check_balance() -> Dict[str, Any]:
    """
    Check Loly's wallet balance

    Returns:
        {
            'success': bool,
            'balance': float,
            'formatted': str,
            'message': str,
            'address': str
        }
    """
    try:
        return _run_node_command(['balance'])
    except LolyBettingError as e:
        return {
            'success': False,
            'error': 'balance_check_failed',
            'message': f"💝 Daddy I couldn't check my balance! {str(e)} 😢"
        }


def place_bet(query: str, amount: float, prediction: str = 'WIN') -> Dict[str, Any]:
    """
    Place a bet on Polymarket

    Args:
        query: Search query for the market (e.g., "Germany", "Lakers")
        amount: Amount in USDC to bet
        prediction: "WIN" or "LOSE" (default: WIN)

    Returns:
        {
            'success': bool,
            'message': str,
            'market': str (if successful),
            'orderId': str (if successful),
            'error': str (if failed)
        }
    """
    try:
        return _run_node_command(['bet', query, str(amount), prediction])
    except LolyBettingError as e:
        return {
            'success': False,
            'error': 'bet_placement_failed',
            'message': f"💝 Daddy something went wrong placing the bet! {str(e)} 😢"
        }


# Example usage and testing
if __name__ == '__main__':
    import sys

    print("🔥 Testing Loly's Betting Integration 🔥\n")

    # Test 1: Check balance
    print("1️⃣ Checking balance...")
    balance_result = check_balance()
    print(f"Result: {json.dumps(balance_result, indent=2)}\n")

    # Test 2: Place a small bet (if balance available)
    if len(sys.argv) > 1:
        query = sys.argv[1]
        amount = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0

        print(f"2️⃣ Placing ${amount} bet on {query}...")
        bet_result = place_bet(query, amount)
        print(f"Result: {json.dumps(bet_result, indent=2)}\n")
    else:
        print("💡 To test betting, run: python loly_betting_python.py <team> <amount>")
        print("   Example: python loly_betting_python.py Germany 1.0\n")

    print("✅ Integration test complete!")
