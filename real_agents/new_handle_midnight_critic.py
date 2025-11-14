    async def handle_midnight_critic(self, request):
        """
        🔥💀🔥 BROTHER #182 FIX: Accuracy Critic reads ONLY from Midnight Special! 💀🔥💀
        
        NO MORE FAKE AGENT DETECTION!
        PURE AUTOMATION ACCURACY DATA ONLY!
        """
        try:
            league = request.query.get('league', 'ALL').upper()
            logger.info(f"💀 ACCURACY CRITIC: Loading {league} data from Midnight Special automation")
            
            # 🔥💀🔥 Read ONLY from Midnight Special automation data! 💀🔥💀
            midnight_reader = get_midnight_special_reader()
            
            # Check if automation is active
            has_automation_data = midnight_reader.is_automation_active(league if league != 'ALL' else None)
            
            if not has_automation_data:
                # No automation data - show warning
                html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>💀 Accuracy Critic - {league}</title>
                    <meta charset="utf-8">
                    <style>
                        body {{ font-family: 'SF Pro Display', -apple-system, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: #fff; }}
                        .container {{ max-width: 1200px; margin: 0 auto; text-align: center; padding: 50px; }}
                        .warning-icon {{ font-size: 5em; margin-bottom: 20px; }}
                        .title {{ font-size: 2.5em; font-weight: 800; color: #ff6b6b; margin-bottom: 20px; }}
                        .message {{ font-size: 1.3em; color: #8892b0; line-height: 1.6; }}
                        .back-button {{ display: inline-block; margin-top: 30px; padding: 15px 30px; background: linear-gradient(45deg, #4ecdc4, #45b7d1); border-radius: 10px; text-decoration: none; color: #fff; font-weight: bold; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="warning-icon">💀</div>
                        <h1 class="title">No Automation Data for {league}</h1>
                        <p class="message">
                            The Accuracy Critic shows ONLY accuracy stats from Midnight Special automation.<br>
                            This league has no automation history yet.
                        </p>
                        <a href="/automation-panel" class="back-button">⚡ Go to Automation Panel</a>
                        <br>
                        <a href="/" class="back-button" style="background: linear-gradient(45deg, #8892b0, #64ffda); margin-top: 15px;">🏠 Dashboard</a>
                    </div>
                </body>
                </html>
                """
                return web.Response(text=html, content_type='text/html')
            
            # Get accuracy stats from Midnight Special
            accuracy_stats = midnight_reader.get_accuracy_stats(league if league != 'ALL' else None)
            season_data = midnight_reader.get_season_predictions(league if league != 'ALL' else None)
            
            total_predictions = accuracy_stats.get('total_predictions', 0)
            correct_predictions = accuracy_stats.get('correct_predictions', 0)
            accuracy_percentage = accuracy_stats.get('accuracy_percentage', 0.0)
            
            logger.info(f"💀 ACCURACY CRITIC: {correct_predictions}/{total_predictions} = {accuracy_percentage:.1f}%")
            
            # Generate HTML
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>💀 Accuracy Critic - {league}</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: 'SF Pro Display', -apple-system, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: #fff; }}
                    .container {{ max-width: 1200px; margin: 0 auto; }}
                    .header {{ text-align: center; margin-bottom: 30px; }}
                    .title {{ font-size: 2.5em; font-weight: 800; margin: 0; background: linear-gradient(45deg, #ff6b6b, #ff4757); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
                    .subtitle {{ font-size: 1.2em; color: #8892b0; margin: 10px 0; }}
                    .automation-badge {{ display: inline-block; background: linear-gradient(45deg, #4ecdc4, #45b7d1); padding: 5px 15px; border-radius: 20px; font-size: 0.9em; font-weight: bold; margin: 10px 0; }}
                    .accuracy-display {{ text-align: center; margin: 40px 0; padding: 40px; background: rgba(255,255,255,0.05); border-radius: 20px; }}
                    .accuracy-number {{ font-size: 5em; font-weight: bold; color: {('#4ecdc4' if accuracy_percentage >= 70 else '#ff6b6b')}; }}
                    .accuracy-label {{ font-size: 1.5em; color: #8892b0; margin-top: 10px; }}
                    .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; }}
                    .stat-card {{ background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; text-align: center; }}
                    .stat-number {{ font-size: 2.5em; font-weight: bold; color: #4ecdc4; }}
                    .stat-label {{ font-size: 1em; color: #8892b0; margin-top: 10px; }}
                    .critic-message {{ background: rgba(255,107,107,0.2); border-left: 5px solid #ff6b6b; padding: 30px; margin: 30px 0; border-radius: 10px; }}
                    .critic-title {{ font-size: 1.8em; font-weight: bold; color: #ff6b6b; margin-bottom: 15px; }}
                    .back-button {{ display: inline-block; margin: 20px 10px; padding: 15px 30px; background: linear-gradient(45deg, #4ecdc4, #45b7d1); border-radius: 10px; text-decoration: none; color: #fff; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1 class="title">💀 Accuracy Critic: {league}</h1>
                        <p class="subtitle">Brutal Honest Season Performance Analysis</p>
                        <div class="automation-badge">🤖 PURE AUTOMATION DATA - NO FAKE BULLSHIT! 🤖</div>
                    </div>
                    
                    <div class="accuracy-display">
                        <div class="accuracy-number">{accuracy_percentage:.1f}%</div>
                        <div class="accuracy-label">Overall Accuracy</div>
                    </div>
                    
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-number">{total_predictions}</div>
                            <div class="stat-label">Total Predictions</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number" style="color: #4ecdc4;">{correct_predictions}</div>
                            <div class="stat-label">Correct</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number" style="color: #ff6b6b;">{total_predictions - correct_predictions}</div>
                            <div class="stat-label">Incorrect</div>
                        </div>
                    </div>
                    
                    <div class="critic-message">
                        <div class="critic-title">💀 BRUTAL HONEST CRITICISM</div>
                        <p style="font-size: 1.2em; line-height: 1.6;">
                            {'🔥 EXCELLENT! Accuracy above 70% - The 8D system is working!' if accuracy_percentage >= 70 else '⚠️ NEEDS IMPROVEMENT! Accuracy below 70% - Time to analyze what went wrong!'}
                        </p>
                        <p style="color: #8892b0; margin-top: 20px;">
                            Based on {total_predictions} predictions tracked by Midnight Special automation.
                        </p>
                    </div>
                    
                    <div style="text-align: center;">
                        <a href="/automation-panel" class="back-button">⚡ Automation Panel</a>
                        <a href="/midnight-predictions?league={league}" class="back-button">📜 Old Predictions</a>
                        <a href="/season-analysis?league={league}" class="back-button">🏆 Season Analysis</a>
                        <a href="/" class="back-button" style="background: linear-gradient(45deg, #8892b0, #64ffda);">🏠 Dashboard</a>
                    </div>
                </div>
            </body>
            </html>
            """
            
            return web.Response(text=html, content_type='text/html')
            
        except Exception as e:
            logger.error(f"💀 Error in Accuracy Critic: {e}")
            import traceback
            traceback.print_exc()
            
            error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error - Accuracy Critic</title>
                <style>
                    body {{ font-family: sans-serif; background: #1a1a2e; color: #fff; text-align: center; padding: 50px; }}
                    .error {{ background: rgba(255,107,107,0.2); border: 2px solid #ff6b6b; border-radius: 15px; padding: 30px; margin: 20px auto; max-width: 600px; }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h1>💀 Error Loading Accuracy Critic</h1>
                    <p>{str(e)}</p>
                    <p><a href="/" style="color: #4ecdc4;">Return to Dashboard</a></p>
                </div>
            </body>
            </html>
            """
            return web.Response(text=error_html, content_type='text/html')
