#!/bin/bash
# 🔥💰🔥 POLYMARKET WALLET SETUP - HIGH CALIBER STRATEGY! 💰🔥🔥

echo "🔥💰🔥 POLYMARKET WALLET CREDENTIAL SETUP 💰🔥💰"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "📄 Creating .env file for wallet credentials..."
    touch .env
fi

echo "⚠️  WARNING: These credentials will enable REAL trading on Polymarket!"
echo "💰 Only use test wallets or small amounts for testing!"
echo ""

# Get private key
echo "🔑 Enter your Polygon wallet private key (without 0x prefix):"
echo "   (This should be a test wallet with small USDC balance)"
read -s PRIVATE_KEY

# Get funder address
echo ""
echo "🏦 Enter your wallet address (funder address):"
echo "   (Should match the private key above)"
read FUNDER_ADDRESS

# Validate inputs
if [ ${#PRIVATE_KEY} -ne 64 ]; then
    echo "❌ Invalid private key length! Should be 64 characters (32 bytes hex)"
    exit 1
fi

if [[ ! $FUNDER_ADDRESS =~ ^0x[a-fA-F0-9]{40}$ ]]; then
    echo "❌ Invalid wallet address format! Should be 0x followed by 40 hex characters"
    exit 1
fi

# Remove existing entries if they exist
grep -v "POLYMARKET_PRIVATE_KEY=" .env > .env.tmp && mv .env.tmp .env
grep -v "POLYMARKET_FUNDER_ADDRESS=" .env > .env.tmp && mv .env.tmp .env

# Add new credentials
echo "POLYMARKET_PRIVATE_KEY=$PRIVATE_KEY" >> .env
echo "POLYMARKET_FUNDER_ADDRESS=$FUNDER_ADDRESS" >> .env

echo ""
echo "✅ Polymarket wallet credentials saved to .env file!"
echo "🔥 Restart the Loly server to enable REAL trading!"
echo ""
echo "📊 Test your setup with:"
echo "   curl http://localhost:3012/api/polymarket/account"
echo ""
echo "💰 Place a real bet with:"
echo '   curl -X POST http://localhost:3012/api/polymarket/bet/place \'
echo '     -H "Content-Type: application/json" \'
echo '     -d '"'"'{"market_id":"demo_premier_league","amount":1,"outcome":"YES"}'"'"
echo ""
echo "🚨 REMEMBER: This enables REAL trading with REAL money!"
echo "🚨 Always test with small amounts first!"