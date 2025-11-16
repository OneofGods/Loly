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
from aiohttp import web, WSMsgType
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
        
        logger.info("🎤💝🎤 Loly Avatar Server Initialized! 💝🎤💝")
    
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