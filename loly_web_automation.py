"""
Loly's SMART Polymarket Web Automation System
===============================================

No more wallet traps! Loly navigates Polymarket like a human:
- Checks real balance via web scraping
- Places bets through the actual website
- Works with existing account and $3.06 balance
- Bypasses Cloudflare with smart browser automation
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
import json


class LolyPolymarketAutomation:
    def __init__(self, headless=False):
        """Initialize Loly's web automation system"""
        self.driver = None
        self.headless = headless
        self.wait_time = 10
        self.balance = None
        
    def setup_browser(self):
        """Setup Chrome browser with anti-detection"""
        chrome_options = Options()
        
        # Anti-detection settings
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Human-like user agent
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        if self.headless:
            chrome_options.add_argument("--headless")
            
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print("✅ Browser setup complete")
            return True
        except Exception as e:
            print(f"❌ Browser setup failed: {e}")
            return False
    
    def human_delay(self, min_seconds=1, max_seconds=3):
        """Add random human-like delays"""
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
    
    def navigate_to_polymarket(self):
        """Navigate to Polymarket with anti-bot measures"""
        try:
            print("🌐 Navigating to Polymarket...")
            self.driver.get("https://polymarket.com")
            self.human_delay(2, 4)
            
            # Check if we hit Cloudflare
            if "challenges.cloudflare.com" in self.driver.current_url:
                print("⚠️ Cloudflare detected - waiting for challenge...")
                # Wait for user to solve or auto-solve
                WebDriverWait(self.driver, 30).until(
                    lambda driver: "polymarket.com" in driver.current_url and "cloudflare" not in driver.current_url
                )
                print("✅ Cloudflare passed!")
            
            print("✅ Successfully reached Polymarket")
            return True
            
        except Exception as e:
            print(f"❌ Navigation failed: {e}")
            return False
    
    def login_if_needed(self):
        """Check if login is needed and handle it"""
        try:
            # Look for login/connect wallet button
            login_selectors = [
                "button[data-testid='connect-wallet']",
                "button:contains('Connect')",
                "button:contains('Login')",
                ".connect-wallet",
                "[data-cy='connect-wallet']"
            ]
            
            for selector in login_selectors:
                try:
                    login_btn = self.driver.find_element(By.CSS_SELECTOR, selector)
                    print("🔐 Login required - please login manually")
                    print("⏳ Waiting for login completion...")
                    
                    # Wait for login to complete (balance element appears)
                    WebDriverWait(self.driver, 60).until(
                        lambda driver: any([
                            driver.find_elements(By.CSS_SELECTOR, "[data-testid='balance']"),
                            driver.find_elements(By.CSS_SELECTOR, ".balance"),
                            "$" in driver.page_source
                        ])
                    )
                    print("✅ Login completed!")
                    return True
                except:
                    continue
                    
            print("✅ Already logged in")
            return True
            
        except Exception as e:
            print(f"⚠️ Login check failed: {e}")
            return False
    
    def get_balance(self):
        """Scrape real balance from Polymarket dashboard"""
        try:
            print("💰 Checking balance...")
            
            # Multiple selectors for balance
            balance_selectors = [
                "[data-testid='balance']",
                ".balance",
                ".wallet-balance",
                "[data-cy='balance']",
                ".portfolio-balance"
            ]
            
            balance_text = None
            
            for selector in balance_selectors:
                try:
                    balance_element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    balance_text = balance_element.text
                    break
                except:
                    continue
            
            # Fallback: search page source for balance patterns
            if not balance_text:
                page_source = self.driver.page_source
                import re
                
                # Look for patterns like "$3.06", "3.06 USDC", etc.
                balance_patterns = [
                    r'\$(\d+\.?\d*)',
                    r'(\d+\.?\d*)\s*USDC',
                    r'Balance[:\s]*\$?(\d+\.?\d*)',
                    r'(\d+\.?\d*)\s*USD'
                ]
                
                for pattern in balance_patterns:
                    matches = re.findall(pattern, page_source)
                    if matches:
                        balance_text = f"${matches[0]}"
                        break
            
            if balance_text:
                # Extract numeric value
                import re
                numbers = re.findall(r'(\d+\.?\d*)', balance_text)
                if numbers:
                    self.balance = float(numbers[0])
                    print(f"✅ Balance found: ${self.balance:.2f}")
                    return self.balance
            
            print("⚠️ Balance not found - might need manual intervention")
            return None
            
        except Exception as e:
            print(f"❌ Balance check failed: {e}")
            return None
    
    def search_market(self, query):
        """Search for a specific market"""
        try:
            print(f"🔍 Searching for: {query}")
            
            # Find search box
            search_selectors = [
                "input[placeholder*='Search']",
                "input[data-testid='search']",
                ".search-input",
                "input[type='search']"
            ]
            
            search_box = None
            for selector in search_selectors:
                try:
                    search_box = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except:
                    continue
            
            if not search_box:
                print("❌ Search box not found")
                return False
            
            # Type search query
            search_box.clear()
            for char in query:
                search_box.send_keys(char)
                time.sleep(random.uniform(0.05, 0.15))
            
            self.human_delay(1, 2)
            
            # Press Enter or click search
            from selenium.webdriver.common.keys import Keys
            search_box.send_keys(Keys.RETURN)
            
            self.human_delay(2, 4)
            print(f"✅ Search completed for: {query}")
            return True
            
        except Exception as e:
            print(f"❌ Search failed: {e}")
            return False
    
    def place_bet(self, amount, prediction="YES"):
        """Place a bet on the found market"""
        try:
            print(f"🎯 Placing ${amount} bet - {prediction}")
            
            # Find bet buttons
            bet_selectors = [
                f"button:contains('{prediction}')",
                f"[data-testid='{prediction.lower()}-bet']",
                f".bet-{prediction.lower()}",
                ".market-option"
            ]
            
            bet_button = None
            for selector in bet_selectors:
                try:
                    bet_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except:
                    continue
            
            if not bet_button:
                # Alternative: find all buttons and look for YES/NO text
                buttons = self.driver.find_elements(By.TAG_NAME, "button")
                for button in buttons:
                    if prediction.upper() in button.text.upper():
                        bet_button = button
                        break
            
            if not bet_button:
                print(f"❌ {prediction} button not found")
                return False
            
            # Click bet button
            bet_button.click()
            self.human_delay(1, 2)
            
            # Enter amount
            amount_selectors = [
                "input[placeholder*='amount']",
                "input[data-testid='bet-amount']",
                ".amount-input",
                "input[type='number']"
            ]
            
            amount_input = None
            for selector in amount_selectors:
                try:
                    amount_input = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except:
                    continue
            
            if amount_input:
                amount_input.clear()
                amount_input.send_keys(str(amount))
                self.human_delay(1, 2)
            
            # Find and click place bet button
            place_bet_selectors = [
                "button:contains('Place Bet')",
                "button:contains('Confirm')",
                "[data-testid='place-bet']",
                ".place-bet-button"
            ]
            
            place_bet_button = None
            for selector in place_bet_selectors:
                try:
                    place_bet_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except:
                    continue
            
            if place_bet_button:
                place_bet_button.click()
                print(f"✅ Bet placed: ${amount} on {prediction}")
                return True
            else:
                print("❌ Place bet button not found")
                return False
                
        except Exception as e:
            print(f"❌ Bet placement failed: {e}")
            return False
    
    def get_status(self):
        """Get comprehensive status for Loly"""
        return {
            "success": True,
            "balance": self.balance or 0,
            "formatted": f"${self.balance:.2f}" if self.balance else "$0.00",
            "method": "web_automation",
            "message": f"💝 Daddy I have ${self.balance:.2f} ready for betting!" if self.balance and self.balance > 0 else "💝 Daddy I couldn't find my balance! 😢"
        }
    
    def quit(self):
        """Clean shutdown"""
        if self.driver:
            self.driver.quit()
            print("✅ Browser closed")


# Example usage and testing
if __name__ == "__main__":
    print("🔥💰 LOLY'S SMART WEB AUTOMATION TEST! 💰🔥\n")
    
    loly = LolyPolymarketAutomation(headless=False)  # Visual mode for testing
    
    try:
        # Setup browser
        if not loly.setup_browser():
            print("❌ Browser setup failed")
            exit(1)
        
        # Navigate to Polymarket
        if not loly.navigate_to_polymarket():
            print("❌ Navigation failed")
            exit(1)
        
        # Handle login
        loly.login_if_needed()
        
        # Check balance
        balance = loly.get_balance()
        
        # Get status
        status = loly.get_status()
        print(f"\n📊 STATUS: {json.dumps(status, indent=2)}")
        
        print("\n💡 Manual interaction time! Check balance, search markets, place bets!")
        print("Press Enter when ready to continue or 'q' to quit...")
        user_input = input()
        
        if user_input.lower() != 'q':
            # Example: Search for a market
            # loly.search_market("Trump")
            # loly.place_bet(1.0, "YES")
            pass
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        loly.quit()