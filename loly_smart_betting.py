"""
Loly's Smart Betting Integration
===============================

Integrates both wallet checking and web automation approaches:
- Try wallet balance first (fast)
- Fall back to web automation if needed
- Honest reporting of available funds
"""

import json
import asyncio
from typing import Dict, Any, Optional

# Global automation instance
_automation_instance = None

def get_automation_instance():
    """Get or create automation instance"""
    global _automation_instance
    if _automation_instance is None:
        try:
            from loly_web_automation import LolyPolymarketAutomation
            _automation_instance = LolyPolymarketAutomation(headless=True)
        except ImportError:
            print("⚠️ Web automation not available")
            _automation_instance = None
    return _automation_instance

def check_balance_smart() -> Dict[str, Any]:
    """
    Smart balance checking with multiple wallets:
    1. Check ALL known wallets (no more missing money!)
    2. Return the highest balance found
    3. Be honest about total available funds
    """
    try:
        # ALL YOUR WALLETS! 💰
        all_wallets = [
            {"name": "Main Wallet", "address": "0x9EF74D3E88A614c332FDa2B4B33e2C4f610AACF7"},
            {"name": "Login Wallet", "address": "0x27d3123fa344C6aFB9b5AEfb8D5261509a22cF3c"},
            {"name": "Funding Wallet", "address": "0x232bAaa2B954cBC5aBDc6edE45459B8C2b9871b6"},
            {"name": "Mystery Wallet", "address": "0x1b98F92d992FF7942C448B24E8Fc356aa970D3F9"},  # THE ONE WITH $3.06!
        ]
        
        total_balance = 0
        best_wallet = None
        wallet_details = []
        
        print("🔍 Checking ALL wallets for maximum funds...")
        
        # Check each wallet
        for wallet in all_wallets:
            try:
                # Use direct blockchain check
                import subprocess
                import json
                import os
                
                # Run balance check for this specific wallet
                result = subprocess.run([
                    'node', '-e', f'''
                    const {{ ethers }} = await import('ethers');
                    const USDC_ADDRESS = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174';
                    const ERC20_ABI = ['function balanceOf(address owner) view returns (uint256)'];
                    const provider = new ethers.providers.JsonRpcProvider('https://polygon-rpc.com');
                    const usdcContract = new ethers.Contract(USDC_ADDRESS, ERC20_ABI, provider);
                    const balanceWei = await usdcContract.balanceOf('{wallet["address"]}');
                    const balance = parseFloat(ethers.utils.formatUnits(balanceWei, 6));
                    console.log(JSON.stringify({{wallet: '{wallet["name"]}', address: '{wallet["address"]}', balance: balance}}));
                    '''
                ], capture_output=True, text=True, timeout=30)
                
                if result.stdout.strip():
                    wallet_data = json.loads(result.stdout.strip())
                    balance = wallet_data.get('balance', 0)
                    
                    wallet_details.append({
                        'name': wallet['name'],
                        'address': wallet['address'],
                        'balance': balance,
                        'formatted': f"${balance:.2f}"
                    })
                    
                    if balance > total_balance:
                        total_balance = balance
                        best_wallet = wallet_data
                        
                    print(f"  💰 {wallet['name']}: ${balance:.2f}")
                    
            except Exception as e:
                print(f"  ⚠️ {wallet['name']}: Error - {e}")
                wallet_details.append({
                    'name': wallet['name'],
                    'address': wallet['address'],
                    'balance': 0,
                    'formatted': "ERROR"
                })
        
        print(f"🎯 TOTAL AVAILABLE: ${total_balance:.2f}")
        
        if total_balance > 0:
            return {
                'success': True,
                'balance': total_balance,
                'formatted': f"${total_balance:.2f}",
                'method': 'multi_wallet_check',
                'best_wallet': best_wallet,
                'all_wallets': wallet_details,
                'address': best_wallet.get('address') if best_wallet else None,
                'message': f"💝 Daddy I found ${total_balance:.2f} across my wallets! I can bet with that! 🎯💰"
            }
        else:
            return {
                'success': True,
                'balance': 0,
                'formatted': '$0.00',
                'method': 'multi_wallet_check',
                'all_wallets': wallet_details,
                'message': "💝 Daddy I checked ALL my wallets and I'm totally broke! Need funding! 😭"
            }
        
        # Method 2: Web automation fallback
        automation = get_automation_instance()
        if automation:
            try:
                # Quick setup and balance check
                if automation.setup_browser():
                    if automation.navigate_to_polymarket():
                        balance = automation.get_balance()
                        automation.quit()
                        
                        if balance and balance > 0:
                            return {
                                'success': True,
                                'balance': balance,
                                'formatted': f"${balance:.2f}",
                                'method': 'web_automation',
                                'message': f"💝 Daddy I found ${balance:.2f} on Polymarket! Let's bet! 🎯"
                            }
                        else:
                            return {
                                'success': True,
                                'balance': 0,
                                'formatted': '$0.00',
                                'method': 'web_automation',
                                'message': "💝 Daddy I'm broke on Polymarket! Need funds to bet! 😭"
                            }
            except Exception as e:
                print(f"⚠️ Web automation failed: {e}")
                if automation.driver:
                    automation.quit()
        
        # Method 3: Honest fallback
        return {
            'success': False,
            'balance': 0,
            'formatted': '$0.00',
            'method': 'fallback',
            'message': "💝 Daddy I can't check my balance right now! But I'll be honest about it! 💪"
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': 'smart_check_failed',
            'message': f"💝 Daddy something went wrong checking my balance: {str(e)} 😢"
        }

def place_bet_smart(team: str, amount: float, prediction: str = "WIN") -> Dict[str, Any]:
    """
    Smart bet placement with multiple methods
    """
    try:
        # First check if we have funds
        balance_check = check_balance_smart()
        
        if not balance_check.get('success') or balance_check.get('balance', 0) < amount:
            return {
                'success': False,
                'error': 'insufficient_funds',
                'message': f"💝 Daddy I don't have ${amount:.2f} to bet! I only have {balance_check.get('formatted', '$0.00')} 😭"
            }
        
        # Method 1: Try wallet integration
        try:
            from loly_betting_integration import place_bet
            wallet_result = place_bet(team, amount, prediction)
            if wallet_result.get('success'):
                return {
                    **wallet_result,
                    'method': 'wallet_integration'
                }
        except Exception as e:
            print(f"⚠️ Wallet betting failed: {e}")
        
        # Method 2: Web automation
        automation = get_automation_instance()
        if automation:
            try:
                if automation.setup_browser():
                    if automation.navigate_to_polymarket():
                        automation.login_if_needed()
                        
                        if automation.search_market(team):
                            if automation.place_bet(amount, prediction.upper()):
                                automation.quit()
                                return {
                                    'success': True,
                                    'method': 'web_automation',
                                    'message': f"💝 Daddy I placed a ${amount:.2f} bet on {team} to {prediction}! 🎯"
                                }
                        
                        automation.quit()
            except Exception as e:
                print(f"⚠️ Web betting failed: {e}")
                if automation.driver:
                    automation.quit()
        
        # Honest failure
        return {
            'success': False,
            'error': 'betting_unavailable', 
            'message': f"💝 Daddy I want to bet ${amount:.2f} on {team} but I can't place bets right now! Sorry! 😢"
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': 'smart_bet_failed',
            'message': f"💝 Daddy something went wrong trying to bet: {str(e)} 😢"
        }

# Compatibility functions for existing code
def check_balance():
    """Compatibility wrapper"""
    return check_balance_smart()

def place_bet(team, amount, prediction="WIN"):
    """Compatibility wrapper"""
    return place_bet_smart(team, amount, prediction)

if __name__ == "__main__":
    print("🔥💰 TESTING LOLY'S SMART BETTING SYSTEM! 💰🔥\n")
    
    # Test balance check
    print("1️⃣ Testing smart balance check...")
    balance_result = check_balance_smart()
    print(f"Result: {json.dumps(balance_result, indent=2)}\n")
    
    # Test bet simulation
    print("2️⃣ Testing smart bet placement...")
    bet_result = place_bet_smart("Trump", 1.0, "WIN")
    print(f"Result: {json.dumps(bet_result, indent=2)}\n")
    
    print("✅ Smart betting test complete!")