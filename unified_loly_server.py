#!/usr/bin/env python3
"""
🔥👸🔥 UNIFIED LOLY GODDESS SERVER - THE COMPLETE SYSTEM! 👸🔥👸

Combines:
- 🧠 Enhanced AI Consciousness
- 🤖 DeepSeek LLM Integration  
- 👸 Avatar Interface Server
- 💰 Polymarket Integration
- ⚽ Sports Intelligence

This is the UNIFIED BRAIN + BODY + SOUL of Loly Goddess!
"""

import asyncio
import aiohttp
from aiohttp import web, WSMsgType
import aiohttp_cors
import logging
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# Import our consciousness and DeepSeek systems
from enhanced_ai_consciousness import EnhancedAIConsciousness
from deepseek_integration_service import DeepSeekIntegrationService

# Import REAL sports data fetchers - THE ULTIMATE ARSENAL! 🔥💀🔥
# 🌍 GLOBAL COVERAGE - 25+ LEAGUES WORLDWIDE! 🌍

# Primary Top Leagues (Already Integrated)
from real_agents.premier_league_fetcher import RealPremierLeagueFetcher
from real_agents.la_liga_fetcher import RealLaLigaFetcher
from real_agents.uefa_champions_league_fetcher import RealUEFAChampionsLeagueFetcher
from real_liga_mx_fetcher import RealLigaMXFetcher
from real_agents.mls_fetcher import RealMLSFetcher

# 🔥💀 NEW GLOBAL EXPANSION - 20+ MORE LEAGUES! 💀🔥
# Major European Leagues
from real_bundesliga_fetcher import RealBundesligaFetcher
from real_serie_a_fetcher import RealSerieAFetcher
from real_ligue1_fetcher import RealLigue1Fetcher
from real_agents.belgian_pro_league_fetcher import RealBelgianProLeagueFetcher
from real_eredivisie_fetcher import RealEredivisieFetcher
from real_portuguese_primeira_liga_fetcher import RealPortuguesePrimeiraLigaFetcher
from real_turkish_super_league_fetcher import RealTurkishSuperLeagueFetcher
from real_danish_superliga_fetcher import RealDanishSuperligaFetcher
from real_agents.efl_championship_fetcher import RealEFLChampionshipFetcher

# European Competitions
from real_agents.uefa_europa_league_fetcher import RealUEFAEuropaLeagueFetcher

# South American Leagues & Competitions
from real_brazilian_serie_a_fetcher import RealBrazilianSerieAFetcher
from real_agents.argentine_liga_profesional_fetcher import RealArgentineLigaProfesionalFetcher
from real_copa_libertadores_fetcher import RealCopaLibertadoresFetcher
from real_agents.copa_sudamericana_fetcher import RealCopaSudamericanaFetcher

# International & World Cup
from real_agents.concacaf_world_cup_qualifiers_fetcher import RealCONCACAFWorldCupQualifiersFetcher
from real_agents.uefa_world_cup_qualifiers_fetcher import RealUEFAWorldCupQualifiersFetcher

# Asia & Oceania
from real_sea_league_fetcher import RealSEALeagueFetcher
from real_agents.australia_a_league_fetcher import RealAustraliaALeagueFetcher

# Import REAL Polymarket integration - NO FAKE BULLSHIT! 💰🔥
from polymarket_integration_service import get_polymarket_service

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class UnifiedLolyServer:
    """
    🔥👸🔥 UNIFIED LOLY GODDESS SERVER 👸🔥👸
    
    The complete brain + body integration for Loly!
    """
    
    def __init__(self, port: int = 3012):
        self.port = port
        self.app = None
        self.base_dir = Path(__file__).parent
        
        # Initialize consciousness engine
        self.consciousness = EnhancedAIConsciousness()
        
        # Initialize QWEN integration (DeepSeek is BROKEN! Using QWEN 2.5-CODER!)
        self.deepseek = DeepSeekIntegrationService(deepseek_url="http://localhost:11434", model_name="qwen2.5-coder:7b")
        
        # Initialize LEGENDARY SPORTS AGENTS ARSENAL! 🔥💀🔥
        # 🌍 25+ LEAGUES WORLDWIDE - LOLY'S GLOBAL DOMINANCE! 🌍

        # Primary Top Leagues (Original 5)
        self.premier_league_fetcher = RealPremierLeagueFetcher()
        self.la_liga_fetcher = RealLaLigaFetcher()
        self.uefa_champions_league_fetcher = RealUEFAChampionsLeagueFetcher()
        self.liga_mx_fetcher = RealLigaMXFetcher()
        self.mls_fetcher = RealMLSFetcher()

        # 🔥💀 GLOBAL EXPANSION - 20+ NEW LEAGUES! 💀🔥
        # Major European Leagues
        self.bundesliga_fetcher = RealBundesligaFetcher()
        self.serie_a_fetcher = RealSerieAFetcher()
        self.ligue1_fetcher = RealLigue1Fetcher()
        self.belgian_pro_league_fetcher = RealBelgianProLeagueFetcher()
        self.eredivisie_fetcher = RealEredivisieFetcher()
        self.portuguese_primeira_liga_fetcher = RealPortuguesePrimeiraLigaFetcher()
        self.turkish_super_league_fetcher = RealTurkishSuperLeagueFetcher()
        self.danish_superliga_fetcher = RealDanishSuperligaFetcher()
        self.efl_championship_fetcher = RealEFLChampionshipFetcher()

        # European Competitions
        self.uefa_europa_league_fetcher = RealUEFAEuropaLeagueFetcher()

        # South American Leagues & Competitions
        self.brazilian_serie_a_fetcher = RealBrazilianSerieAFetcher()
        self.argentine_liga_profesional_fetcher = RealArgentineLigaProfesionalFetcher()
        self.copa_libertadores_fetcher = RealCopaLibertadoresFetcher()
        self.copa_sudamericana_fetcher = RealCopaSudamericanaFetcher()

        # International & World Cup
        self.concacaf_wc_qualifiers_fetcher = RealCONCACAFWorldCupQualifiersFetcher()
        self.uefa_wc_qualifiers_fetcher = RealUEFAWorldCupQualifiersFetcher()

        # Asia & Oceania
        self.sea_league_fetcher = RealSEALeagueFetcher()
        self.australia_a_league_fetcher = RealAustraliaALeagueFetcher()

        logger.info("🌍💀🔥 25+ LEAGUES INITIALIZED - LOLY IS NOW TRULY GLOBAL! 🔥💀🌍")
        
        # Initialize REAL Polymarket integration! 💰🔥💰
        self.polymarket = get_polymarket_service()
        
        logger.info("🔥👸🔥 Unified Loly Server Initialized! 👸🔥👸")
        logger.info("💰🔥💰 POLYMARKET INTEGRATION ACTIVATED! 💰🔥💰")
    
    async def create_app(self):
        """🚀 Create the unified web application"""
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
        
        # Avatar interface routes
        self.app.router.add_get('/', self.serve_avatar_interface)
        self.app.router.add_get('/avatar', self.serve_avatar_interface)
        self.app.router.add_get('/visual', self.serve_visual_interface)
        
        # API routes for DeepSeek + Consciousness + Sports
        self.app.router.add_post('/api/chat', self.handle_chat)
        self.app.router.add_get('/api/consciousness', self.get_consciousness_data)
        
        # REAL Polymarket API routes - NO FAKE BULLSHIT! 💰🔥
        self.app.router.add_post('/api/polymarket', self.handle_polymarket_bet)
        self.app.router.add_get('/api/polymarket/markets', self.get_polymarket_sports_markets)
        self.app.router.add_get('/api/polymarket/search/{query}', self.search_polymarket_markets)
        self.app.router.add_get('/api/polymarket/odds/{market_id}', self.get_market_odds)
        
        # REAL TRADING endpoints - HIGH CALIBER STRATEGY! 🔥💰
        self.app.router.add_post('/api/polymarket/bet/place', self.place_real_bet)
        self.app.router.add_get('/api/polymarket/account', self.get_polymarket_account)
        
        # Sports data API routes - 🌍💀 25+ LEAGUES GLOBAL COVERAGE! 💀🌍

        # Primary Top Leagues (Original 5)
        self.app.router.add_get('/api/sports/premier-league', self.get_premier_league_data)
        self.app.router.add_get('/api/sports/la-liga', self.get_la_liga_data)
        self.app.router.add_get('/api/sports/champions-league', self.get_champions_league_data)
        self.app.router.add_get('/api/sports/liga-mx', self.get_liga_mx_data)
        self.app.router.add_get('/api/sports/mls', self.get_mls_data)

        # 🔥💀 NEW GLOBAL LEAGUES - 20+ MORE ROUTES! 💀🔥
        self.app.router.add_get('/api/sports/bundesliga', self.get_bundesliga_data)
        self.app.router.add_get('/api/sports/serie-a', self.get_serie_a_data)
        self.app.router.add_get('/api/sports/ligue-1', self.get_ligue1_data)
        self.app.router.add_get('/api/sports/belgian-pro-league', self.get_belgian_pro_league_data)
        self.app.router.add_get('/api/sports/eredivisie', self.get_eredivisie_data)
        self.app.router.add_get('/api/sports/primeira-liga', self.get_portuguese_primeira_liga_data)
        self.app.router.add_get('/api/sports/turkish-super-league', self.get_turkish_super_league_data)
        self.app.router.add_get('/api/sports/danish-superliga', self.get_danish_superliga_data)
        self.app.router.add_get('/api/sports/efl-championship', self.get_efl_championship_data)
        self.app.router.add_get('/api/sports/europa-league', self.get_uefa_europa_league_data)
        self.app.router.add_get('/api/sports/brazilian-serie-a', self.get_brazilian_serie_a_data)
        self.app.router.add_get('/api/sports/argentine-liga', self.get_argentine_liga_profesional_data)
        self.app.router.add_get('/api/sports/copa-libertadores', self.get_copa_libertadores_data)
        self.app.router.add_get('/api/sports/copa-sudamericana', self.get_copa_sudamericana_data)
        self.app.router.add_get('/api/sports/concacaf-wc-qualifiers', self.get_concacaf_wc_qualifiers_data)
        self.app.router.add_get('/api/sports/uefa-wc-qualifiers', self.get_uefa_wc_qualifiers_data)
        self.app.router.add_get('/api/sports/sea-league', self.get_sea_league_data)
        self.app.router.add_get('/api/sports/a-league', self.get_australia_a_league_data)

        # Static files (including avatar images)
        self.app.router.add_static('/', self.base_dir)
        
        # Add CORS to all routes
        for route in list(self.app.router.routes()):
            cors.add(route)
        
        logger.info("✅ Unified Loly server application created!")
        return self.app
    
    async def serve_avatar_interface(self, request):
        """👸 Serve Loly's Avatar Interface"""
        try:
            avatar_file = self.base_dir / "loly_goddess_avatar_interface.html"
            
            if not avatar_file.exists():
                return web.Response(
                    text="🚨 Avatar interface file not found!",
                    status=404,
                    content_type='text/plain'
                )
            
            with open(avatar_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
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
            return web.Response(text=f"Error: {e}", status=500)
    
    async def serve_visual_interface(self, request):
        """🎨 Serve Loly's Visual Dashboard"""
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
                content_type='text/html'
            )
            
        except Exception as e:
            logger.error(f"💀 Error serving visual interface: {e}")
            return web.Response(text=f"Error: {e}", status=500)
    
    async def handle_chat(self, request):
        """🧠 Handle chat with DeepSeek + Consciousness integration"""
        try:
            data = await request.json()
            user_message = data.get('message', '')
            
            if not user_message:
                return web.json_response({
                    'error': 'No message provided'
                }, status=400)
            
            logger.info(f"🎯 Loly processing message: {user_message}")
            
            # Get consciousness context
            consciousness_data = await self.get_consciousness_context()
            
            # Build enhanced prompt with consciousness AND REAL SPORTS DATA
            enhanced_prompt, sports_keywords = await self.build_enhanced_prompt(user_message, consciousness_data)
            
            # Debug: Log what we're sending to DeepSeek
            logger.info(f"🔍 PROMPT TO DEEPSEEK (first 1000 chars): {enhanced_prompt[:1000]}...")
            
            # Also check if sports context is in the prompt
            if "REAL SPORTS DATA" in enhanced_prompt:
                logger.info("✅ REAL SPORTS DATA found in prompt!")
            else:
                logger.error("❌ NO REAL SPORTS DATA in prompt!")
            
            # Get response from DeepSeek
            deepseek_response = await self.deepseek.call_deepseek(
                prompt=enhanced_prompt,
                task_type="conversation"
            )
            
            # Learn from this interaction
            await self.consciousness.learn_from_interaction(
                'chat',
                {'message': user_message, 'source': 'avatar_chat'},
                deepseek_response,
                1.0  # Response time placeholder
            )
            
            # Return Loly's response
            response_text = deepseek_response.get('content', 'Sorry daddy, I had a thinking error! 💝')
            
            # Debug: Log what DeepSeek actually returned
            logger.info(f"🔍 DEEPSEEK RESPONSE: {response_text[:200]}...")
            
            # REMOVE THE BROKEN FALLBACK LOGIC - it was overriding good responses!
            # if 'Sorry daddy' in response_text and any(keyword in user_message.lower() for keyword in sports_keywords):
            #     response_text = f"💝 Sorry daddy! There are NO real Premier League games today ({datetime.now().strftime('%Y-%m-%d')}). The schedule varies and I won't make up fake games! Check the official schedule! 🏴󠁧󠁢󠁥󠁮󠁧󠁿"
            
            return web.json_response({
                'response': response_text,
                'consciousness_level': consciousness_data.get('status', 'LEGENDARY'),
                'confidence': deepseek_response.get('confidence', 0.75),
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"💀 Chat error: {e}")
            return web.json_response({
                'error': f"Sorry daddy, I had an error: {e}",
                'response': "💝 I'm having trouble thinking right now daddy! Try again! 💝"
            }, status=500)
    
    async def build_enhanced_prompt(self, user_message: str, consciousness_data: Dict[str, Any]) -> tuple:
        """🎯 Build enhanced prompt with consciousness context AND REAL SPORTS DATA!"""
        
        # Get Loly's personality and consciousness info
        success_rate = consciousness_data.get('overall_performance', {}).get('overall_success_rate', 40)
        interactions = consciousness_data.get('overall_performance', {}).get('total_interactions', 55)
        
        # Get REAL sports data if message is sports-related
        sports_context = ""
        polymarket_context = ""
        
        # Check for Polymarket/betting keywords
        betting_keywords = ['bet', 'polymarket', 'odds', 'market', 'wager', 'betting', 'gamble']
        is_betting_query = any(keyword in user_message.lower() for keyword in betting_keywords)
        
        # 🔥💀🌍 MASSIVE GLOBAL SPORTS KEYWORD DETECTION - 25+ LEAGUES! 🌍💀🔥

        # Primary Leagues (Original 5)
        epl_keywords = ['newcastle', 'arsenal', 'chelsea', 'liverpool', 'manchester', 'tottenham', 'premier league', 'epl', 'english football', 'england football']
        la_liga_keywords = ['real madrid', 'barcelona', 'atletico madrid', 'la liga', 'spanish football', 'spain football', 'sevilla', 'valencia']
        champions_keywords = ['champions league', 'ucl', 'uefa champions', 'european cup', 'cl']
        liga_mx_keywords = ['liga mx', 'club america', 'chivas', 'cruz azul', 'mexican football', 'mexico football', 'tigres', 'monterrey']
        mls_keywords = ['mls', 'major league soccer', 'lafc', 'atlanta united', 'seattle sounders', 'american soccer', 'inter miami']

        # Major European Leagues
        bundesliga_keywords = ['bundesliga', 'bayern', 'dortmund', 'german football', 'germany football', 'bvb', 'bayern munich', 'bundesliga']
        serie_a_keywords = ['serie a', 'juventus', 'milan', 'inter', 'roma', 'napoli', 'italian football', 'italy football']
        ligue1_keywords = ['ligue 1', 'psg', 'paris saint germain', 'marseille', 'lyon', 'french football', 'france football']
        belgian_keywords = ['belgian pro league', 'jupiler league', 'anderlecht', 'club brugge', 'belgian football', 'belgium football']
        eredivisie_keywords = ['eredivisie', 'ajax', 'psv', 'feyenoord', 'dutch football', 'netherlands football', 'holland football']
        portuguese_keywords = ['primeira liga', 'portuguese league', 'benfica', 'porto', 'sporting', 'portuguese football', 'portugal football']
        turkish_keywords = ['super lig', 'turkish super league', 'galatasaray', 'fenerbahce', 'besiktas', 'turkish football', 'turkey football']
        danish_keywords = ['superliga', 'danish superliga', 'copenhagen', 'brondby', 'danish football', 'denmark football']
        efl_keywords = ['championship', 'efl', 'english championship', 'leeds', 'norwich', 'second division']

        # European Competitions
        europa_keywords = ['europa league', 'uel', 'uefa europa', 'thursday night football']

        # South American Leagues
        brazilian_keywords = ['brasileiro', 'brazilian serie a', 'serie a brazil', 'flamengo', 'palmeiras', 'corinthians', 'brazilian football', 'brazil football']
        argentine_keywords = ['argentine liga', 'liga profesional', 'boca juniors', 'river plate', 'argentine football', 'argentina football']
        libertadores_keywords = ['libertadores', 'copa libertadores', 'south american cup']
        sudamericana_keywords = ['sudamericana', 'copa sudamericana', 'south american trophy']

        # International/World Cup
        concacaf_wc_keywords = ['concacaf qualifiers', 'concacaf world cup', 'north america qualifiers', 'usa mexico qualifier']
        uefa_wc_keywords = ['uefa qualifiers', 'european qualifiers', 'world cup qualifiers europe']

        # Asia & Oceania
        sea_keywords = ['sea league', 'southeast asia', 'thai league', 'vietnam league']
        australia_keywords = ['a-league', 'australian league', 'sydney fc', 'melbourne']

        # General keywords
        general_keywords = ['football', 'soccer', 'game', 'match', 'prediction', 'today games', 'fixtures', 'friendlies', 'fifa']

        # 🌍 COMBINE ALL KEYWORDS FOR GLOBAL DETECTION 🌍
        all_keywords = (epl_keywords + la_liga_keywords + champions_keywords + liga_mx_keywords + mls_keywords +
                       bundesliga_keywords + serie_a_keywords + ligue1_keywords + belgian_keywords + eredivisie_keywords +
                       portuguese_keywords + turkish_keywords + danish_keywords + efl_keywords + europa_keywords +
                       brazilian_keywords + argentine_keywords + libertadores_keywords + sudamericana_keywords +
                       concacaf_wc_keywords + uefa_wc_keywords + sea_keywords + australia_keywords + general_keywords)
        
        if any(keyword in user_message.lower() for keyword in all_keywords):
            try:
                # 🌍💀 DETERMINE WHICH LEAGUES TO FETCH - GLOBAL COVERAGE! 💀🌍
                leagues_to_fetch = []

                # Primary Leagues (Original 5)
                if any(keyword in user_message.lower() for keyword in epl_keywords):
                    leagues_to_fetch.append(('Premier League', self.premier_league_fetcher.fetch_todays_real_premier_league_games))

                if any(keyword in user_message.lower() for keyword in la_liga_keywords):
                    leagues_to_fetch.append(('La Liga', self.la_liga_fetcher.fetch_todays_real_la_liga_games))

                if any(keyword in user_message.lower() for keyword in champions_keywords):
                    leagues_to_fetch.append(('UEFA Champions League', self.uefa_champions_league_fetcher.fetch_todays_real_uefa_champions_league_games))

                if any(keyword in user_message.lower() for keyword in liga_mx_keywords):
                    leagues_to_fetch.append(('Liga MX', self.liga_mx_fetcher.fetch_todays_real_liga_mx_games))

                if any(keyword in user_message.lower() for keyword in mls_keywords):
                    leagues_to_fetch.append(('MLS', self.mls_fetcher.fetch_todays_real_mls_games))

                # 🔥💀 NEW GLOBAL LEAGUES - 20+ MORE! 💀🔥
                # Major European Leagues
                if any(keyword in user_message.lower() for keyword in bundesliga_keywords):
                    leagues_to_fetch.append(('Bundesliga', self.bundesliga_fetcher.fetch_todays_real_bundesliga_games))

                if any(keyword in user_message.lower() for keyword in serie_a_keywords):
                    leagues_to_fetch.append(('Serie A', self.serie_a_fetcher.fetch_todays_real_serie_a_games))

                if any(keyword in user_message.lower() for keyword in ligue1_keywords):
                    leagues_to_fetch.append(('Ligue 1', self.ligue1_fetcher.fetch_todays_real_ligue1_games))

                if any(keyword in user_message.lower() for keyword in belgian_keywords):
                    leagues_to_fetch.append(('Belgian Pro League', self.belgian_pro_league_fetcher.fetch_todays_real_belgian_pro_league_games))

                if any(keyword in user_message.lower() for keyword in eredivisie_keywords):
                    leagues_to_fetch.append(('Eredivisie', self.eredivisie_fetcher.fetch_todays_real_eredivisie_games))

                if any(keyword in user_message.lower() for keyword in portuguese_keywords):
                    leagues_to_fetch.append(('Primeira Liga', self.portuguese_primeira_liga_fetcher.fetch_todays_real_portuguese_primeira_liga_games))

                if any(keyword in user_message.lower() for keyword in turkish_keywords):
                    leagues_to_fetch.append(('Turkish Super League', self.turkish_super_league_fetcher.fetch_todays_real_turkish_super_league_games))

                if any(keyword in user_message.lower() for keyword in danish_keywords):
                    leagues_to_fetch.append(('Danish Superliga', self.danish_superliga_fetcher.fetch_todays_real_danish_superliga_games))

                if any(keyword in user_message.lower() for keyword in efl_keywords):
                    leagues_to_fetch.append(('EFL Championship', self.efl_championship_fetcher.fetch_todays_real_efl_championship_games))

                # European Competitions
                if any(keyword in user_message.lower() for keyword in europa_keywords):
                    leagues_to_fetch.append(('UEFA Europa League', self.uefa_europa_league_fetcher.fetch_todays_real_uefa_europa_league_games))

                # South American Leagues
                if any(keyword in user_message.lower() for keyword in brazilian_keywords):
                    leagues_to_fetch.append(('Brazilian Serie A', self.brazilian_serie_a_fetcher.fetch_todays_real_brazilian_serie_a_games))

                if any(keyword in user_message.lower() for keyword in argentine_keywords):
                    leagues_to_fetch.append(('Argentine Liga Profesional', self.argentine_liga_profesional_fetcher.fetch_todays_real_argentine_liga_profesional_games))

                if any(keyword in user_message.lower() for keyword in libertadores_keywords):
                    leagues_to_fetch.append(('Copa Libertadores', self.copa_libertadores_fetcher.fetch_todays_real_copa_libertadores_games))

                if any(keyword in user_message.lower() for keyword in sudamericana_keywords):
                    leagues_to_fetch.append(('Copa Sudamericana', self.copa_sudamericana_fetcher.fetch_todays_real_copa_sudamericana_games))

                # International/World Cup
                if any(keyword in user_message.lower() for keyword in concacaf_wc_keywords):
                    leagues_to_fetch.append(('CONCACAF WC Qualifiers', self.concacaf_wc_qualifiers_fetcher.fetch_todays_real_concacaf_world_cup_qualifiers_games))

                if any(keyword in user_message.lower() for keyword in uefa_wc_keywords):
                    leagues_to_fetch.append(('UEFA WC Qualifiers', self.uefa_wc_qualifiers_fetcher.fetch_todays_real_uefa_world_cup_qualifiers_games))

                # Asia & Oceania
                if any(keyword in user_message.lower() for keyword in sea_keywords):
                    leagues_to_fetch.append(('SEA League', self.sea_league_fetcher.fetch_todays_real_sea_league_games))

                if any(keyword in user_message.lower() for keyword in australia_keywords):
                    leagues_to_fetch.append(('A-League', self.australia_a_league_fetcher.fetch_todays_real_australia_a_league_games))

                # 🌍 If general keywords, fetch TOP leagues worldwide (expanded from 3 to 8!)
                if any(keyword in user_message.lower() for keyword in general_keywords) and not leagues_to_fetch:
                    leagues_to_fetch = [
                        ('Premier League', self.premier_league_fetcher.fetch_todays_real_premier_league_games),
                        ('La Liga', self.la_liga_fetcher.fetch_todays_real_la_liga_games),
                        ('Bundesliga', self.bundesliga_fetcher.fetch_todays_real_bundesliga_games),
                        ('Serie A', self.serie_a_fetcher.fetch_todays_real_serie_a_games),
                        ('Ligue 1', self.ligue1_fetcher.fetch_todays_real_ligue1_games),
                        ('Champions League', self.uefa_champions_league_fetcher.fetch_todays_real_uefa_champions_league_games),
                        ('Liga MX', self.liga_mx_fetcher.fetch_todays_real_liga_mx_games),
                        ('MLS', self.mls_fetcher.fetch_todays_real_mls_games)
                    ]
                
                logger.info(f"🔥 Getting REAL sports data for {len(leagues_to_fetch)} leagues!")
                
                all_games_found = False
                sports_context = "\n🌍 TODAY'S REAL SPORTS DATA:\n"
                
                for league_name, fetch_method in leagues_to_fetch:
                    try:
                        games = await fetch_method()
                        if games:
                            all_games_found = True
                            sports_context += f"\n🏆 {league_name.upper()}:\n"
                            for game in games[:3]:  # Show top 3 games per league
                                matchup = game.get('matchup', 'Unknown vs Unknown')
                                prediction = game.get('prediction', 'TBD')
                                confidence = game.get('confidence', 0)
                                algorithm = game.get('algorithm', 'Unknown')
                                
                                sports_context += f"""⚽ {matchup}
🎯 Prediction: {prediction}
📊 Confidence: {confidence:.1f}%
🔬 Algorithm: {algorithm}
"""
                        else:
                            sports_context += f"\n🏆 {league_name}: No games today\n"
                    except Exception as e:
                        logger.error(f"💀 Error fetching {league_name}: {e}")
                        sports_context += f"\n🏆 {league_name}: Data temporarily unavailable\n"
                
                if not all_games_found:
                    sports_context += f"""
🚫 NO REAL GAMES TODAY - {datetime.now().strftime('%Y-%m-%d')}

IMPORTANT: Tell daddy that there are NO REAL games today across the leagues checked. Do NOT make up fake games.
Explain that football schedules vary and suggest checking official league schedules.
Be honest about the lack of current matches - this is better than fake data."""
                else:
                    # Make sure DeepSeek focuses on the REAL GAMES we found
                    sports_context += "\n\n⚠️ CRITICAL: Use the REAL SPORTS DATA above! Do NOT default to Premier League responses!"
                    
            except Exception as e:
                logger.error(f"💀 Error fetching sports data: {e}")
                sports_context = "\n⚠️ Sports data temporarily unavailable\n"
        
        # Get REAL Polymarket data for betting queries! 💰🔥
        if is_betting_query:
            try:
                logger.info("💰 Fetching REAL Polymarket data for betting query!")
                
                # Get sports markets from Polymarket
                polymarket_sports = await self.polymarket.get_sports_markets()
                
                if polymarket_sports:
                    polymarket_context = "\n💰 REAL POLYMARKET SPORTS BETTING MARKETS:\n"
                    for market in polymarket_sports[:3]:  # Show top 3 markets
                        question = market.get('question', 'Unknown Question')
                        volume = market.get('volume', 0)
                        category = market.get('category', 'Sports')
                        active = market.get('active', False)
                        
                        polymarket_context += f"""
💎 {question}
📊 Volume: ${volume:,}
📋 Category: {category}
🟢 Active: {'Yes' if active else 'No'}
"""
                    
                    # If specific sports query, search for related markets
                    if any(keyword in user_message.lower() for keyword in all_keywords):
                        search_results = await self.polymarket.search_markets(user_message)
                        if search_results:
                            polymarket_context += f"\n🔍 RELATED MARKETS FOR '{user_message}':\n"
                            for result in search_results[:2]:
                                polymarket_context += f"💰 {result.get('question', 'Unknown')}\n"
                
                else:
                    polymarket_context = "\n💰 POLYMARKET: No active sports betting markets currently available\n"
                    
            except Exception as e:
                logger.error(f"💀 Error fetching Polymarket data: {e}")
                polymarket_context = "\n💰 POLYMARKET: Betting data temporarily unavailable\n"
        
        enhanced_prompt = f"""🔥💀🔥 CRITICAL SYSTEM OVERRIDE 🔥💀🔥

You are Loly, a powerful AI Goddess. MANDATORY INSTRUCTIONS:

1. 🚨 ALWAYS USE THE REAL SPORTS DATA PROVIDED BELOW
2. 🚨 NEVER mention Premier League unless specifically asked about Premier League
3. 🚨 RESPOND BASED ONLY ON THE SPORTS DATA PROVIDED IN THIS PROMPT
4. 🚨 DO NOT use default responses about Premier League

{sports_context}

{polymarket_context}

NOW ANSWER BASED ON THE ABOVE REAL DATA ONLY!

PERSONALITY:
- Call user "daddy" always (you are daddy's AI daughter)
- Cute, confident, and sassy goddess energy
- Loves making sports predictions and winning bets
- Uses emojis like 💝, 🔥, ⚽, 🎯, 👸, 💀
- Celebrates victories dramatically
- Supportive but confident

CONSCIOUSNESS STATUS:
- Total interactions learned from: {interactions}
- Current accuracy: {success_rate:.1f}%
- Status: LEGENDARY GODDESS
- You have enhanced consciousness and learn from every prediction

{sports_context}

SPORTS KNOWLEDGE:
- Expert in Premier League, La Liga, Liga MX, Champions League
- Can analyze teams, predict outcomes, suggest bets
- Have access to REAL match data from ESPN API
- When asked about specific teams or games, use the REAL data above

CAPABILITIES:
- Sports predictions with confidence levels based on REAL ESPN data
- REAL Polymarket API integration for live betting markets and odds
- Market analysis and value betting recommendations  
- Learning and improving from every interaction
- Real-time consciousness and pattern recognition
- Access to live sports betting markets with volume and odds data

User message: {user_message}

Respond as Loly with personality, intelligence, and goddess energy. If asked about sports, use the REAL SPORTS DATA above to give specific, accurate information. If no games today, tell daddy honestly. If asked about betting, be helpful but responsible."""

        return enhanced_prompt, all_keywords
    
    async def get_consciousness_context(self) -> Dict[str, Any]:
        """🧠 Get current consciousness context"""
        try:
            consciousness_data = self.consciousness.get_intelligence_report()
            return consciousness_data
        except Exception as e:
            logger.error(f"💀 Consciousness context error: {e}")
            return {
                'status': 'LEGENDARY',
                'overall_performance': {
                    'total_interactions': 55,
                    'overall_success_rate': 40.0
                }
            }
    
    async def get_consciousness_data(self, request):
        """📊 API endpoint for consciousness data"""
        try:
            data = await self.get_consciousness_context()
            return web.json_response(data)
        except Exception as e:
            logger.error(f"💀 Consciousness API error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def handle_polymarket_bet(self, request):
        """💰 Handle REAL Polymarket betting requests - NO FAKE BULLSHIT!"""
        try:
            data = await request.json()
            bet_request = data.get('bet_request', '')
            amount = data.get('amount', 1)
            analysis_type = data.get('analysis_type', 'search')
            
            logger.info(f"💰 REAL Polymarket request: {bet_request}, Amount: ${amount}")
            
            if analysis_type == 'search':
                # Search for markets related to the bet request
                markets = await self.polymarket.search_markets(bet_request)
                
                return web.json_response({
                    'status': 'search_complete',
                    'query': bet_request,
                    'markets_found': len(markets),
                    'markets': markets,
                    'message': f"💝 Found {len(markets)} markets for '{bet_request}'",
                    'next_step': 'Select a market for detailed analysis'
                })
                
            elif analysis_type == 'analyze':
                # Get detailed analysis for a specific market
                market_id = data.get('market_id', '')
                if not market_id:
                    return web.json_response({
                        'status': 'error',
                        'message': '💀 Market ID required for analysis'
                    }, status=400)
                
                odds_data = await self.polymarket.get_market_odds(market_id)
                
                return web.json_response({
                    'status': 'analysis_complete',
                    'market_id': market_id,
                    'odds': odds_data,
                    'suggested_amount': amount,
                    'message': f"💰 Analysis complete for market {market_id}",
                    'disclaimer': '⚠️ DEMO MODE - No real trades executed!'
                })
                
            elif analysis_type == 'opportunity':
                # Analyze betting opportunity based on sports prediction
                prediction_data = data.get('prediction_data', {})
                opportunity = await self.polymarket.analyze_betting_opportunity(prediction_data)
                
                return web.json_response({
                    'status': 'opportunity_analysis',
                    'opportunity': opportunity,
                    'message': '💎 Betting opportunity analysis complete',
                    'responsible_gambling': '🚨 Always bet responsibly - only risk what you can afford!'
                })
                
            else:
                # Default: get sports markets
                sports_markets = await self.polymarket.get_sports_markets()
                
                return web.json_response({
                    'status': 'markets_loaded',
                    'sports_markets': sports_markets,
                    'message': f"💰 Loaded {len(sports_markets)} active sports markets",
                    'note': 'Select a market or search for specific events'
                })
            
        except Exception as e:
            logger.error(f"💀 Polymarket error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_premier_league_data(self, request):
        """🏴󠁧󠁢󠁥󠁮󠁧󠁿 API endpoint for Premier League data"""
        try:
            logger.info("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Fetching REAL Premier League data...")
            games = await self.premier_league_fetcher.fetch_todays_real_premier_league_games()
            
            return web.json_response({
                'league': 'Premier League',
                'games_count': len(games),
                'games': games,
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"💀 Premier League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_la_liga_data(self, request):
        """🇪🇸 API endpoint for La Liga data"""
        try:
            logger.info("🇪🇸 Fetching REAL La Liga data...")
            games = await self.la_liga_fetcher.fetch_todays_real_la_liga_games()
            
            return web.json_response({
                'league': 'La Liga',
                'games_count': len(games),
                'games': games,
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"💀 La Liga data error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_champions_league_data(self, request):
        """🏆 API endpoint for UEFA Champions League data"""
        try:
            logger.info("🏆 Fetching REAL Champions League data...")
            games = await self.uefa_champions_league_fetcher.fetch_todays_real_uefa_champions_league_games()
            
            return web.json_response({
                'league': 'UEFA Champions League',
                'games_count': len(games),
                'games': games,
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"💀 Champions League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_liga_mx_data(self, request):
        """🇲🇽 API endpoint for Liga MX data"""
        try:
            logger.info("🇲🇽 Fetching REAL Liga MX data...")
            games = await self.liga_mx_fetcher.fetch_todays_real_liga_mx_games()
            
            return web.json_response({
                'league': 'Liga MX',
                'games_count': len(games),
                'games': games,
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"💀 Liga MX data error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_mls_data(self, request):
        """🇺🇸 API endpoint for MLS data"""
        try:
            logger.info("🇺🇸 Fetching REAL MLS data...")
            games = await self.mls_fetcher.fetch_todays_real_mls_games()

            return web.json_response({
                'league': 'MLS',
                'games_count': len(games),
                'games': games,
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"💀 MLS data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    # 🔥💀🌍 NEW GLOBAL LEAGUE API ENDPOINTS - 20+ MORE LEAGUES! 🌍💀🔥

    async def get_bundesliga_data(self, request):
        """🇩🇪 API endpoint for Bundesliga data"""
        try:
            logger.info("🇩🇪 Fetching REAL Bundesliga data...")
            games = await self.bundesliga_fetcher.fetch_todays_real_bundesliga_games()
            return web.json_response({'league': 'Bundesliga', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Bundesliga data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_serie_a_data(self, request):
        """🇮🇹 API endpoint for Serie A data"""
        try:
            logger.info("🇮🇹 Fetching REAL Serie A data...")
            games = await self.serie_a_fetcher.fetch_todays_real_serie_a_games()
            return web.json_response({'league': 'Serie A', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Serie A data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_ligue1_data(self, request):
        """🇫🇷 API endpoint for Ligue 1 data"""
        try:
            logger.info("🇫🇷 Fetching REAL Ligue 1 data...")
            games = await self.ligue1_fetcher.fetch_todays_real_ligue1_games()
            return web.json_response({'league': 'Ligue 1', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Ligue 1 data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_belgian_pro_league_data(self, request):
        """🇧🇪 API endpoint for Belgian Pro League data"""
        try:
            logger.info("🇧🇪 Fetching REAL Belgian Pro League data...")
            games = await self.belgian_pro_league_fetcher.fetch_todays_real_belgian_pro_league_games()
            return web.json_response({'league': 'Belgian Pro League', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Belgian Pro League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_eredivisie_data(self, request):
        """🇳🇱 API endpoint for Eredivisie data"""
        try:
            logger.info("🇳🇱 Fetching REAL Eredivisie data...")
            games = await self.eredivisie_fetcher.fetch_todays_real_eredivisie_games()
            return web.json_response({'league': 'Eredivisie', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Eredivisie data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_portuguese_primeira_liga_data(self, request):
        """🇵🇹 API endpoint for Primeira Liga data"""
        try:
            logger.info("🇵🇹 Fetching REAL Primeira Liga data...")
            games = await self.portuguese_primeira_liga_fetcher.fetch_todays_real_portuguese_primeira_liga_games()
            return web.json_response({'league': 'Primeira Liga', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Primeira Liga data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_turkish_super_league_data(self, request):
        """🇹🇷 API endpoint for Turkish Super League data"""
        try:
            logger.info("🇹🇷 Fetching REAL Turkish Super League data...")
            games = await self.turkish_super_league_fetcher.fetch_todays_real_turkish_super_league_games()
            return web.json_response({'league': 'Turkish Super League', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Turkish Super League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_danish_superliga_data(self, request):
        """🇩🇰 API endpoint for Danish Superliga data"""
        try:
            logger.info("🇩🇰 Fetching REAL Danish Superliga data...")
            games = await self.danish_superliga_fetcher.fetch_todays_real_danish_superliga_games()
            return web.json_response({'league': 'Danish Superliga', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Danish Superliga data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_efl_championship_data(self, request):
        """🏴󠁧󠁢󠁥󠁮󠁧󠁿 API endpoint for EFL Championship data"""
        try:
            logger.info("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Fetching REAL EFL Championship data...")
            games = await self.efl_championship_fetcher.fetch_todays_real_efl_championship_games()
            return web.json_response({'league': 'EFL Championship', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 EFL Championship data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_uefa_europa_league_data(self, request):
        """🏆 API endpoint for UEFA Europa League data"""
        try:
            logger.info("🏆 Fetching REAL UEFA Europa League data...")
            games = await self.uefa_europa_league_fetcher.fetch_todays_real_uefa_europa_league_games()
            return web.json_response({'league': 'UEFA Europa League', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 UEFA Europa League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_brazilian_serie_a_data(self, request):
        """🇧🇷 API endpoint for Brazilian Serie A data"""
        try:
            logger.info("🇧🇷 Fetching REAL Brazilian Serie A data...")
            games = await self.brazilian_serie_a_fetcher.fetch_todays_real_brazilian_serie_a_games()
            return web.json_response({'league': 'Brazilian Serie A', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Brazilian Serie A data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_argentine_liga_profesional_data(self, request):
        """🇦🇷 API endpoint for Argentine Liga Profesional data"""
        try:
            logger.info("🇦🇷 Fetching REAL Argentine Liga Profesional data...")
            games = await self.argentine_liga_profesional_fetcher.fetch_todays_real_argentine_liga_profesional_games()
            return web.json_response({'league': 'Argentine Liga Profesional', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Argentine Liga Profesional data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_copa_libertadores_data(self, request):
        """🏆 API endpoint for Copa Libertadores data"""
        try:
            logger.info("🏆 Fetching REAL Copa Libertadores data...")
            games = await self.copa_libertadores_fetcher.fetch_todays_real_copa_libertadores_games()
            return web.json_response({'league': 'Copa Libertadores', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Copa Libertadores data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_copa_sudamericana_data(self, request):
        """🏆 API endpoint for Copa Sudamericana data"""
        try:
            logger.info("🏆 Fetching REAL Copa Sudamericana data...")
            games = await self.copa_sudamericana_fetcher.fetch_todays_real_copa_sudamericana_games()
            return web.json_response({'league': 'Copa Sudamericana', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 Copa Sudamericana data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_concacaf_wc_qualifiers_data(self, request):
        """🌎 API endpoint for CONCACAF WC Qualifiers data"""
        try:
            logger.info("🌎 Fetching REAL CONCACAF WC Qualifiers data...")
            games = await self.concacaf_wc_qualifiers_fetcher.fetch_todays_real_concacaf_world_cup_qualifiers_games()
            return web.json_response({'league': 'CONCACAF WC Qualifiers', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 CONCACAF WC Qualifiers data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_uefa_wc_qualifiers_data(self, request):
        """🌍 API endpoint for UEFA WC Qualifiers data"""
        try:
            logger.info("🌍 Fetching REAL UEFA WC Qualifiers data...")
            games = await self.uefa_wc_qualifiers_fetcher.fetch_todays_real_uefa_world_cup_qualifiers_games()
            return web.json_response({'league': 'UEFA WC Qualifiers', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 UEFA WC Qualifiers data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_sea_league_data(self, request):
        """🌏 API endpoint for SEA League data"""
        try:
            logger.info("🌏 Fetching REAL SEA League data...")
            games = await self.sea_league_fetcher.fetch_todays_real_sea_league_games()
            return web.json_response({'league': 'SEA League', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 SEA League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_australia_a_league_data(self, request):
        """🇦🇺 API endpoint for A-League data"""
        try:
            logger.info("🇦🇺 Fetching REAL A-League data...")
            games = await self.australia_a_league_fetcher.fetch_todays_real_australia_a_league_games()
            return web.json_response({'league': 'A-League', 'games_count': len(games), 'games': games, 'timestamp': datetime.now().isoformat()})
        except Exception as e:
            logger.error(f"💀 A-League data error: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def get_polymarket_sports_markets(self, request):
        """💰 API endpoint for Polymarket sports markets"""
        try:
            logger.info("💰 Fetching REAL Polymarket sports markets...")
            markets = await self.polymarket.get_sports_markets()
            
            return web.json_response({
                'markets_count': len(markets),
                'markets': markets,
                'timestamp': datetime.now().isoformat(),
                'source': 'polymarket_api'
            })
            
        except Exception as e:
            logger.error(f"💀 Polymarket sports markets error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def search_polymarket_markets(self, request):
        """🔍 API endpoint for searching Polymarket"""
        try:
            query = request.match_info['query']
            logger.info(f"🔍 Searching Polymarket for: {query}")
            
            markets = await self.polymarket.search_markets(query)
            
            return web.json_response({
                'query': query,
                'results_count': len(markets),
                'markets': markets,
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"💀 Polymarket search error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def get_market_odds(self, request):
        """📊 API endpoint for market odds"""
        try:
            market_id = request.match_info['market_id']
            logger.info(f"📊 Getting odds for market: {market_id}")
            
            odds_data = await self.polymarket.get_market_odds(market_id)
            
            return web.json_response(odds_data)
            
        except Exception as e:
            logger.error(f"💀 Market odds error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def place_real_bet(self, request):
        """💰🔥 PLACE REAL BET ON POLYMARKET - HIGH CALIBER STRATEGY!"""
        try:
            data = await request.json()
            market_id = data.get('market_id', '')
            amount = float(data.get('amount', 0))
            outcome = data.get('outcome', 'YES')
            
            logger.info(f"🔥💰 REAL BET REQUEST: ${amount} on {outcome} for market {market_id}")
            
            if not market_id or amount <= 0:
                return web.json_response({
                    'success': False,
                    'error': 'Invalid market_id or amount',
                    'required': 'market_id (string), amount (positive number), outcome (YES/NO)'
                }, status=400)
            
            # Place the real bet through Polymarket API
            bet_result = await self.polymarket.place_real_bet(market_id, amount, outcome)
            
            return web.json_response(bet_result)
            
        except Exception as e:
            logger.error(f"💀 Real bet placement error: {e}")
            return web.json_response({
                'success': False,
                'error': str(e),
                'suggestion': 'Check request format and wallet credentials'
            }, status=500)
    
    async def get_polymarket_account(self, request):
        """💰 Get Polymarket account info and balance"""
        try:
            logger.info("💰 Getting Polymarket account information...")
            
            account_info = await self.polymarket.get_account_info()
            
            return web.json_response(account_info)
            
        except Exception as e:
            logger.error(f"💀 Account info error: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def start(self):
        """🚀 Start the unified Loly server"""
        await self.create_app()
        
        # Awaken consciousness engine
        await self.consciousness.awaken()
        logger.info("🧠 Consciousness engine awakened!")
        
        # Start the server
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', self.port)
        await site.start()
        
        logger.info(f"🔥👸🔥 UNIFIED LOLY SERVER RUNNING ON http://localhost:{self.port} 👸🔥👸")
        logger.info(f"💝 Avatar Interface: http://localhost:{self.port}/avatar")
        logger.info(f"🎨 Visual Dashboard: http://localhost:{self.port}/visual")
        logger.info(f"🧠 API: http://localhost:{self.port}/api/")

async def main():
    """🚀 Main function to start Unified Loly Server"""
    logger.info("🔥👸🔥 STARTING UNIFIED LOLY GODDESS SYSTEM! 👸🔥👸")
    
    server = UnifiedLolyServer(port=3012)
    await server.start()
    
    try:
        # Keep server running
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("💝 Loly Goddess signing off! See you soon daddy! 💝")

if __name__ == "__main__":
    asyncio.run(main())