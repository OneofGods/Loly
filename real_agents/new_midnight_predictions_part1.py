    async def handle_midnight_predictions(self, request):
        """
        🔥💀🔥 BROTHER #182 FIX: Old Predictions reads ONLY from Midnight Special! 💀🔥💀
        
        NO MORE CONTAMINATION FROM GAMES & PREDICTIONS!
        PURE AUTOMATION SEASON DATA ONLY!
        """
        try:
            # Get league from request
            live_league = request.query.get('league', 'LIGA_MX').upper()
            logger.info(f"📜 OLD PREDICTIONS: Loading {live_league} season data from Midnight Special automation")
            
            # 🔥💀🔥 SPECIAL CASE: UEFA shows RESULTS analysis 💀🔥💀
            if live_league == 'UEFA':
                return await self._handle_uefa_results_analysis(request)
            
            # 🔥💀🔥 BROTHER #182: Read ONLY from Midnight Special automation data! 💀🔥💀
            midnight_reader = get_midnight_special_reader()
            
            # Check if automation is active for this league
            has_automation_data = midnight_reader.is_automation_active(live_league)
            
            if not has_automation_data:
                # No automation data - show warning
                html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>📜 Old Predictions - {live_league}</title>
                    <meta charset="utf-8">
                    <style>
                        body {{ font-family: 'SF Pro Display', -apple-system, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: #fff; }}
                        .container {{ max-width: 1200px; margin: 0 auto; text-align: center; padding: 50px; }}
                        .warning-icon {{ font-size: 5em; margin-bottom: 20px; }}
                        .title {{ font-size: 2.5em; font-weight: 800; color: #ff6b6b; margin-bottom: 20px; }}
                        .message {{ font-size: 1.3em; color: #8892b0; line-height: 1.6; margin-bottom: 30px; }}
                        .automation-box {{ background: rgba(255,255,255,0.05); border: 2px solid #ff6b6b; border-radius: 15px; padding: 30px; margin: 30px 0; }}
                        .automation-title {{ font-size: 1.5em; color: #4ecdc4; margin-bottom: 15px; }}
                        .automation-steps {{ text-align: left; margin: 20px auto; max-width: 600px; }}
                        .step {{ padding: 15px; margin: 10px 0; background: rgba(255,255,255,0.02); border-left: 3px solid #4ecdc4; }}
                        .back-button {{ display: inline-block; margin-top: 30px; padding: 15px 30px; background: linear-gradient(45deg, #4ecdc4, #45b7d1); border-radius: 10px; text-decoration: none; color: #fff; font-weight: bold; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="warning-icon">⚠️</div>
                        <h1 class="title">No Automation Data for {live_league}</h1>
                        <p class="message">
                            The Old Predictions panel shows ONLY season data from Midnight Special automation.<br>
                            This league has no automation history yet.
                        </p>
                        
                        <div class="automation-box">
                            <div class="automation-title">🤖 How to Enable Automation</div>
                            <div class="automation-steps">
                                <div class="step">
                                    1. Go to <strong>Automation Panel</strong>
                                </div>
                                <div class="step">
                                    2. Click <strong>"🚀 Start Automation"</strong> for {live_league}
                                </div>
                                <div class="step">
                                    3. Automation will track predictions and results
                                </div>
                                <div class="step">
                                    4. Season data will appear here automatically
                                </div>
                            </div>
                        </div>
                        
                        <a href="/automation-panel" class="back-button">
                            ⚡ Go to Automation Panel
                        </a>
                        <br>
                        <a href="/" class="back-button" style="background: linear-gradient(45deg, #8892b0, #64ffda); margin-top: 15px;">
                            🏠 Return to Dashboard
                        </a>
                    </div>
                </body>
                </html>
                """
                return web.Response(text=html, content_type='text/html')
