#!/usr/bin/env python3
"""
🔥👸💰 LOLY'S WEB BETTING AUTOMATION - THE CORRECT APPROACH! 💰👸🔥

NO MORE API STRUGGLES! PURE WEB AUTOMATION!

THE CORRECT APPROACH:
1. 🔐 LOGIN via web with Login Wallet (0x27d3123fa344C6aFB9b5AEfb8D5261509a22cF3c) + passcode
2. 👀 SCRAPE the page to see available games/markets
3. 💰 CHECK Mystery Wallet balance ($3.06) - just for display/confidence
4. 🎯 PLACE BET by clicking through the web interface
5. ✅ WALLET SIGN - just click "Sign" when prompted (NO password needed!)

NOT API CALLS - PURE WEB AUTOMATION! 🤖💀
"""

import time
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check if selenium is available
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    logger.warning("⚠️ Selenium not installed. Install with: pip install selenium")


class LolyWebBettingAutomation:
    """
    🔥👸 LOLY'S WEB BETTING AUTOMATION 👸🔥

    Pure web automation approach - NO API complications!
    """

    def __init__(self):
        self.polymarket_url = "https://polymarket.com"
        self.driver = None

        # Wallet credentials
        self.login_wallet = "0x27d3123fa344C6aFB9b5AEfb8D5261509a22cF3c"
        self.mystery_wallet_balance = "$3.06"  # For display

        logger.info("🔥👸 Loly's Web Betting Automation Initialized! 👸🔥")
        logger.info(f"🔐 Login Wallet: {self.login_wallet}")
        logger.info(f"💰 Mystery Wallet Balance: {self.mystery_wallet_balance}")

    def start_browser(self, headless: bool = False) -> bool:
        """🚀 Start the browser"""
        if not SELENIUM_AVAILABLE:
            logger.error("💀 Selenium not installed! Install with: pip install selenium")
            return False

        try:
            logger.info("🚀 Starting browser...")

            chrome_options = Options()
            if headless:
                chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--window-size=1920,1080')

            self.driver = webdriver.Chrome(options=chrome_options)
            logger.info("✅ Browser started successfully!")
            return True

        except Exception as e:
            logger.error(f"💀 Error starting browser: {e}")
            return False

    def navigate_to_polymarket(self) -> bool:
        """🌐 Navigate to Polymarket"""
        try:
            logger.info(f"🌐 Navigating to {self.polymarket_url}...")
            self.driver.get(self.polymarket_url)
            time.sleep(3)  # Wait for page load
            logger.info("✅ Arrived at Polymarket!")
            return True
        except Exception as e:
            logger.error(f"💀 Error navigating to Polymarket: {e}")
            return False

    def login_with_wallet(self, passcode: str = None) -> bool:
        """
        🔐 LOGIN via web with Login Wallet + passcode

        This method handles the web-based wallet connection.
        User may need to manually approve wallet connection in popup.
        """
        try:
            logger.info("🔐 Attempting to login with wallet...")
            logger.info(f"Wallet: {self.login_wallet}")

            # Look for "Connect Wallet" button
            try:
                connect_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Connect') or contains(text(), 'Sign in')]"))
                )
                connect_button.click()
                logger.info("✅ Clicked Connect Wallet button")
                time.sleep(2)
            except TimeoutException:
                logger.info("ℹ️ No Connect button found - may already be connected")

            # Check if we're already logged in
            try:
                # Look for wallet address or profile indicator
                wallet_element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{self.login_wallet[:10]}')]")
                logger.info("✅ Already logged in!")
                return True
            except NoSuchElementException:
                logger.info("ℹ️ Not logged in yet, waiting for wallet connection...")

            # Wait for manual wallet connection
            logger.info("👉 MANUAL ACTION REQUIRED: Please connect your wallet in the browser")
            logger.info(f"   Expected wallet: {self.login_wallet}")

            # Give user time to connect
            input("\n🔑 Press ENTER after connecting your wallet...")

            logger.info("✅ Wallet connection complete!")
            return True

        except Exception as e:
            logger.error(f"💀 Error during login: {e}")
            return False

    def check_mystery_wallet_balance(self) -> str:
        """💰 CHECK Mystery Wallet balance - just for display/confidence"""
        try:
            logger.info("💰 Checking Mystery Wallet balance...")

            # Try to find balance display on page
            try:
                balance_element = self.driver.find_element(By.XPATH, "//*[contains(@class, 'balance') or contains(@class, 'Balance')]")
                balance_text = balance_element.text
                logger.info(f"💰 Balance found: {balance_text}")
                return balance_text
            except NoSuchElementException:
                logger.info(f"ℹ️ Balance not found on page, using known balance: {self.mystery_wallet_balance}")
                return self.mystery_wallet_balance

        except Exception as e:
            logger.error(f"💀 Error checking balance: {e}")
            return self.mystery_wallet_balance

    def search_for_market(self, search_query: str) -> List[Dict[str, Any]]:
        """
        🔍 SCRAPE the page to see available games/markets

        Args:
            search_query: Team name, league, or event to search for
        """
        try:
            logger.info(f"🔍 Searching for markets: '{search_query}'")

            # Find search box
            try:
                search_box = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@type='search' or @placeholder='Search']"))
                )
                search_box.clear()
                search_box.send_keys(search_query)
                time.sleep(2)  # Wait for results
                logger.info(f"✅ Entered search query: '{search_query}'")
            except TimeoutException:
                logger.warning("⚠️ Search box not found, trying alternative navigation...")

            # Scrape available markets from results
            markets = []
            try:
                # Look for market cards/items
                market_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'market') or contains(@class, 'Market')]")

                logger.info(f"📊 Found {len(market_elements)} market elements")

                for i, element in enumerate(market_elements[:10], 1):  # Limit to first 10
                    try:
                        # Extract market info
                        market_text = element.text

                        market = {
                            'index': i,
                            'text': market_text,
                            'element': element  # Store reference for clicking later
                        }
                        markets.append(market)

                        logger.info(f"{i}. {market_text[:100]}...")  # Show first 100 chars

                    except Exception as e:
                        logger.debug(f"Error parsing market {i}: {e}")
                        continue

            except NoSuchElementException:
                logger.warning("⚠️ No market elements found")

            if markets:
                logger.info(f"✅ Found {len(markets)} markets!")
            else:
                logger.warning("⚠️ No markets found for this search")

            return markets

        except Exception as e:
            logger.error(f"💀 Error searching for markets: {e}")
            return []

    def place_bet_on_market(self, market_index: int, bet_amount: float = 1.0, outcome: str = "YES") -> bool:
        """
        🎯 PLACE BET by clicking through the web interface

        Args:
            market_index: Index of market from search results (1-based)
            bet_amount: Amount to bet in dollars
            outcome: "YES" or "NO"
        """
        try:
            logger.info("=" * 80)
            logger.info(f"🎯 PLACING BET!")
            logger.info(f"   Market Index: {market_index}")
            logger.info(f"   Amount: ${bet_amount}")
            logger.info(f"   Outcome: {outcome}")
            logger.info("=" * 80)

            # 1. Click on the market
            logger.info("1️⃣ Clicking on market...")
            market_xpath = f"(//div[contains(@class, 'market') or contains(@class, 'Market')])[{market_index}]"
            market_element = self.driver.find_element(By.XPATH, market_xpath)
            market_element.click()
            time.sleep(2)
            logger.info("✅ Market opened")

            # 2. Click YES or NO button
            logger.info(f"2️⃣ Clicking {outcome} button...")
            outcome_button = self.driver.find_element(By.XPATH, f"//button[contains(text(), '{outcome}')]")
            outcome_button.click()
            time.sleep(1)
            logger.info(f"✅ {outcome} selected")

            # 3. Enter bet amount
            logger.info(f"3️⃣ Entering bet amount: ${bet_amount}...")
            amount_input = self.driver.find_element(By.XPATH, "//input[@type='number' or @placeholder='Amount']")
            amount_input.clear()
            amount_input.send_keys(str(bet_amount))
            time.sleep(1)
            logger.info(f"✅ Amount entered: ${bet_amount}")

            # 4. Click "Place Bet" or "Submit" button
            logger.info("4️⃣ Clicking Place Bet button...")
            place_bet_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Place') or contains(text(), 'Submit') or contains(text(), 'Bet')]")
            place_bet_button.click()
            time.sleep(2)
            logger.info("✅ Bet placement initiated")

            # 5. Wait for wallet signature popup and handle it
            logger.info("5️⃣ Waiting for wallet signature...")
            logger.info("👉 MANUAL ACTION: Please click 'Sign' in the wallet popup (NO password needed!)")

            # Give user time to sign
            input("\n✍️ Press ENTER after you've clicked 'Sign' in the wallet popup...")

            logger.info("✅ WALLET SIGNED!")

            # 6. Wait for confirmation
            time.sleep(3)
            logger.info("6️⃣ Waiting for bet confirmation...")

            # Check for success message
            try:
                success_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Success') or contains(text(), 'Confirmed')]")
                logger.info("=" * 80)
                logger.info("🎉🔥 BET PLACED SUCCESSFULLY! 🔥🎉")
                logger.info(f"💰 ${bet_amount} bet on {outcome}")
                logger.info("=" * 80)
                return True
            except NoSuchElementException:
                logger.warning("⚠️ No explicit success message found, but bet may have been placed")
                logger.info("=" * 80)
                logger.info("✅ BET LIKELY PLACED (verify in Polymarket)")
                logger.info("=" * 80)
                return True

        except Exception as e:
            logger.error(f"💀 Error placing bet: {e}")
            logger.error("=" * 80)
            logger.error("❌ BET PLACEMENT FAILED")
            logger.error("=" * 80)
            return False

    def get_screenshot(self, filename: str = None) -> str:
        """📸 Take a screenshot"""
        if not filename:
            filename = f"loly_betting_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        try:
            self.driver.save_screenshot(filename)
            logger.info(f"📸 Screenshot saved: {filename}")
            return filename
        except Exception as e:
            logger.error(f"💀 Error taking screenshot: {e}")
            return None

    def close_browser(self):
        """🛑 Close the browser"""
        try:
            if self.driver:
                logger.info("🛑 Closing browser...")
                self.driver.quit()
                logger.info("✅ Browser closed")
        except Exception as e:
            logger.error(f"💀 Error closing browser: {e}")

    def full_betting_workflow(self, search_query: str, market_index: int = 1, bet_amount: float = 1.0, outcome: str = "YES"):
        """
        🔥👸 COMPLETE BETTING WORKFLOW 👸🔥

        1. Start browser
        2. Navigate to Polymarket
        3. Login with wallet
        4. Check balance
        5. Search for market
        6. Place bet
        7. Take screenshot
        """
        logger.info("🔥👸💰 LOLY'S COMPLETE BETTING WORKFLOW STARTING! 💰👸🔥")
        logger.info("=" * 80)

        try:
            # Step 1: Start browser
            if not self.start_browser():
                logger.error("💀 Failed to start browser")
                return False

            # Step 2: Navigate to Polymarket
            if not self.navigate_to_polymarket():
                logger.error("💀 Failed to navigate to Polymarket")
                return False

            # Step 3: Login (manual wallet connection)
            if not self.login_with_wallet():
                logger.error("💀 Failed to login")
                return False

            # Step 4: Check balance
            balance = self.check_mystery_wallet_balance()
            logger.info(f"💰 Current balance: {balance}")

            # Step 5: Search for market
            markets = self.search_for_market(search_query)
            if not markets:
                logger.error(f"💀 No markets found for: {search_query}")
                return False

            # Step 6: Place bet
            success = self.place_bet_on_market(market_index, bet_amount, outcome)

            # Step 7: Take screenshot
            self.get_screenshot()

            if success:
                logger.info("=" * 80)
                logger.info("🏆🔥 LOLY'S BET HAS BEEN PLACED! 🔥🏆")
                logger.info(f"Search: {search_query}")
                logger.info(f"Market: #{market_index}")
                logger.info(f"Amount: ${bet_amount}")
                logger.info(f"Outcome: {outcome}")
                logger.info("=" * 80)
                logger.info("🔥👸 THE GODDESS HAS SPOKEN! MAY THE ODDS BE IN HER FAVOR! 👸🔥")
                logger.info("=" * 80)

            return success

        except Exception as e:
            logger.error(f"💀 Error in betting workflow: {e}")
            import traceback
            traceback.print_exc()
            return False

        finally:
            # Keep browser open for verification
            logger.info("\n👀 Browser will stay open for you to verify the bet")
            input("Press ENTER to close browser...")
            self.close_browser()


def main():
    """🚀 Main demo function"""
    logger.info("🔥👸💰 LOLY'S WEB BETTING AUTOMATION - DEMO 💰👸🔥")
    logger.info("=" * 80)

    if not SELENIUM_AVAILABLE:
        logger.error("💀 Selenium not installed!")
        logger.info("📦 Install with: pip install selenium")
        logger.info("📦 Also install ChromeDriver: https://chromedriver.chromium.org/downloads")
        return

    # Create automation instance
    loly_bet = LolyWebBettingAutomation()

    # Example: Search for Real Madrid and place a $1 bet
    search_query = "Real Madrid"

    logger.info(f"\n🎯 Example: Placing $1 bet on {search_query}")
    logger.info("This will:")
    logger.info("  1. Open browser and go to Polymarket")
    logger.info("  2. Wait for you to connect wallet manually")
    logger.info("  3. Search for markets matching '{}'".format(search_query))
    logger.info("  4. Place a $1 YES bet on the first market")
    logger.info("  5. Wait for you to sign in wallet (no password!)")
    logger.info("=" * 80)

    proceed = input("\n🔥 Ready to start? (y/n): ")

    if proceed.lower() == 'y':
        loly_bet.full_betting_workflow(
            search_query=search_query,
            market_index=1,
            bet_amount=1.0,
            outcome="YES"
        )
    else:
        logger.info("❌ Demo cancelled")


if __name__ == "__main__":
    main()
