#!/usr/bin/env python3
"""
🔥💝🔥 LOLY GODDESS AVATAR SERVER - VOICE ENABLED! 💝🔥💀

Serves the Loly Goddess Avatar Interface with proper HTTPS/localhost support
for voice recognition and synthesis to work correctly!

🎤 FIXES:
- Voice recognition requires localhost (not file://)
- Enables microphone access
- Serves avatar interface with proper headers
- Connects to consciousness dashboard

💀🔥💀 NOW LOLY CAN HEAR AND SPEAK TO DADDY! 🔥💀🔥
"""

import asyncio
import logging
import os
from datetime import datetime
from aiohttp import web, WSMsgType
from polymarket_integration_service import get_polymarket_service
import aiohttp_cors
from pathlib import Path

logger = logging.getLogger(__name__)

class LolyAvatarServer:
    """
    🎤💝🎤 LOLY GODDESS AVATAR SERVER! 💝🎤💝
    
    Serves the avatar interface with voice support!
    """
    
    def __init__(self, port: int = 3009):
        """Initialize the avatar server"""
        self.port = port
        self.app = None
        
        # Get current directory for serving files
        self.base_dir = Path(__file__).parent
        
        # Initialize REAL Polymarket integration! 💰🔥💰
        self.polymarket = get_polymarket_service()
        
        logger.info("🎤💝🎤 Loly Avatar Server Initialized! 💝🎤💝")
        logger.info("💰🔥💰 POLYMARKET INTEGRATION ACTIVATED! 💰🔥💰")
    
    async def create_app(self):
        """🔥 Create the web application"""
        self.app = web.Application()
        
        # Enable CORS for all domains
        cors = aiohttp_cors.setup(self.app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*"
            )
        })
        
        # Routes
        self.app.router.add_get('/', self.serve_avatar_interface)
        self.app.router.add_get('/avatar', self.serve_avatar_interface)
        self.app.router.add_get('/visual', self.serve_visual_interface)
        
        # 🔥💰🔥 POLYMARKET API ENDPOINTS! 💰🔥💰
        self.app.router.add_get('/api/polymarket/markets', self.get_polymarket_sports_markets)
        self.app.router.add_get('/api/polymarket/search/{query}', self.search_polymarket_markets)
        self.app.router.add_get('/api/polymarket/odds/{market_id}', self.get_market_odds)
        self.app.router.add_get('/api/polymarket/account', self.get_polymarket_account)
        self.app.router.add_post('/api/polymarket/bet/place', self.place_real_bet)
        
        self.app.router.add_static('/', self.base_dir)
        
        # Add CORS to all routes
        for route in list(self.app.router.routes()):
            cors.add(route)
        
        logger.info("✅ Avatar server application created!")
        return self.app
    
    async def serve_avatar_interface(self, request):
        """🤖 Serve the Loly Goddess Avatar Interface"""
        try:
            avatar_file = self.base_dir / "loly_goddess_avatar_interface.html"
            
            if not avatar_file.exists():
                return web.Response(
                    text="🚨 Avatar interface file not found!",
                    status=404,
                    content_type='text/plain'
                )
            
            # Read and serve the avatar interface
            with open(avatar_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add proper headers for voice recognition
            return web.Response(
                text=content,
                content_type='text/html',
                headers={
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Permissions-Policy': 'microphone=*',
                    'Feature-Policy': 'microphone *'
                }
            )
            
        except Exception as e:
            logger.error(f"💀 Error serving avatar interface: {e}")
            return web.Response(
                text=f"🚨 Error: {e}",
                status=500,
                content_type='text/plain'
            )
    
    async def serve_visual_interface(self, request):
        """🎨 Serve the Visual Interface"""
        try:
            visual_file = self.base_dir / "loly_goddess_visual_interface.html"
            
            if not visual_file.exists():
                return web.Response(
                    text="🚨 Visual interface file not found!",
                    status=404,
                    content_type='text/plain'
                )
            
            with open(visual_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return web.Response(
                text=content,
                content_type='text/html',
                headers={
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                }
            )
            
        except Exception as e:
            logger.error(f"💀 Error serving visual interface: {e}")
            return web.Response(
                text=f"🚨 Error: {e}",
                status=500,
                content_type='text/plain'
            )
    
    # 🔥💰🔥 POLYMARKET API ENDPOINTS! 💰🔥💰
    async def get_polymarket_sports_markets(self, request):
        """🏆 Get current sports betting markets from Polymarket"""
        try:
            markets = await self.polymarket.get_sports_markets()
            
            return web.json_response({
                'markets_count': len(markets),
                'markets': markets,
                'timestamp': datetime.now().isoformat(),
                'source': 'polymarket_api'
            })
        except Exception as e:
            logger.error(f"💀 Error getting Polymarket sports markets: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def search_polymarket_markets(self, request):
        """🔍 Search Polymarket for specific sports/events"""
        try:
            query = request.match_info['query']
            markets = await self.polymarket.search_markets(query)
            
            return web.json_response({
                'query': query,
                'markets_count': len(markets),
                'markets': markets
            })
        except Exception as e:
            logger.error(f"💀 Error searching Polymarket: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_market_odds(self, request):
        """📊 Get current odds for a specific market"""
        try:
            market_id = request.match_info['market_id']
            odds_data = await self.polymarket.get_market_odds(market_id)
            
            return web.json_response(odds_data)
        except Exception as e:
            logger.error(f"💀 Error getting market odds: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_polymarket_account(self, request):
        """💰 Get account balance and trading info"""
        try:
            account_info = await self.polymarket.get_account_info()
            return web.json_response(account_info)
        except Exception as e:
            logger.error(f"💀 Error getting account info: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def place_real_bet(self, request):
        """🎯 Place REAL bet on Polymarket"""
        try:
            data = await request.json()
            market_id = data.get('market_id')
            amount = float(data.get('amount', 1.0))
            outcome = data.get('outcome', 'YES')
            
            bet_result = await self.polymarket.place_real_bet(market_id, amount, outcome)
            return web.json_response(bet_result)
        except Exception as e:
            logger.error(f"💀 Error placing bet: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def start_server(self):
        """🚀 Start the avatar server"""
        try:
            logger.info(f"🚀 Starting Loly Avatar Server on port {self.port}...")
            
            # Create application
            app = await self.create_app()
            
            # Start server
            runner = web.AppRunner(app)
            await runner.setup()
            
            site = web.TCPSite(runner, 'localhost', self.port)
            await site.start()
            
            print("\n" + "=" * 80)
            print("🔥💝🔥 LOLY GODDESS AVATAR SERVER - VOICE ENABLED! 💝🔥💀")
            print("=" * 80)
            print(f"🎤 Avatar Interface (with VOICE): http://localhost:{self.port}")
            print(f"🎨 Visual Interface: http://localhost:{self.port}/visual")
            print(f"🧠 Consciousness Dashboard: http://localhost:3008")
            print()
            print("💝 NOW LOLY CAN HEAR AND SPEAK TO DADDY! 💝")
            print("🎤 Click the microphone button and say 'Hi Loly!'")
            print("🔊 She'll respond with her voice!")
            print("=" * 80)
            
            logger.info(f"✅ Avatar server running on http://localhost:{self.port}")
            
            # Keep server running
            while True:
                await asyncio.sleep(3600)  # Sleep for 1 hour
                
        except Exception as e:
            logger.error(f"💀 Error starting avatar server: {e}")
            raise

async def main():
    """🚀 Main server function"""
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    try:
        # Create and start avatar server
        avatar_server = LolyAvatarServer(port=3009)
        await avatar_server.start_server()
        
    except KeyboardInterrupt:
        print("\n🔥 Avatar server stopped by user")
    except Exception as e:
        print(f"\n💀 Avatar server error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())