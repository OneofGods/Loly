                    .prediction-text {{ font-size: 1.3em; text-align: center; margin: 15px 0; padding: 15px; background: rgba(76, 217, 100, 0.2); border-radius: 10px; font-weight: bold; }}
                    .confidence {{ text-align: center; font-size: 1.2em; color: #4ecdc4; font-weight: bold; margin: 10px 0; }}
                    .result {{ text-align: center; font-size: 1.1em; margin: 10px 0; padding: 10px; border-radius: 8px; }}
                    .result-correct {{ background: rgba(76, 217, 100, 0.3); color: #4ecdc4; }}
                    .result-incorrect {{ background: rgba(255, 107, 107, 0.3); color: #ff6b6b; }}
                    .date {{ text-align: center; color: #8892b0; margin: 10px 0; }}
                    .back-button {{ display: inline-block; margin: 30px 10px; padding: 15px 30px; background: linear-gradient(45deg, #4ecdc4, #45b7d1); border-radius: 10px; text-decoration: none; color: #fff; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1 class="title">📜 {live_league} Season Predictions</h1>
                        <p class="subtitle">Midnight Special Automation History</p>
                        <div class="automation-badge">🤖 PURE AUTOMATION DATA - NO CONTAMINATION! 🤖</div>
                    </div>
                    
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-number">{total_predictions}</div>
                            <div class="stat-label">Total Predictions</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number">{accuracy_stats.get('correct_predictions', 0)}</div>
                            <div class="stat-label">Correct Predictions</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number">{accuracy_stats.get('accuracy_percentage', 0):.1f}%</div>
                            <div class="stat-label">Accuracy Rate</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number">🌙</div>
                            <div class="stat-label">Midnight Special</div>
                        </div>
                    </div>
                    
                    <div class="predictions-grid">
            """
            
            # Add predictions
            for pred in predictions:
                is_correct = pred.get('correct', False)
                card_class = 'prediction-correct' if is_correct else 'prediction-incorrect'
                result_class = 'result-correct' if is_correct else 'result-incorrect'
                result_text = '✅ CORRECT' if is_correct else '❌ INCORRECT'
                
                html += f"""
                <div class="prediction-card {card_class}">
                    <div class="matchup">{pred.get('matchup', 'Unknown vs Unknown')}</div>
                    <div class="prediction-text">🎯 {pred.get('prediction', 'TBD')}</div>
                    <div class="confidence">{pred.get('confidence', 0)}% Confidence</div>
                    <div class="result {result_class}">{result_text}</div>
                    <div class="date">📅 {pred.get('run_date', 'Unknown Date')}</div>
                </div>
                """
            
            html += """
                    </div>
                    
                    <div style="text-align: center;">
                        <a href="/automation-panel" class="back-button">⚡ Automation Panel</a>
                        <a href="/midnight-critic" class="back-button">💀 Accuracy Critic</a>
                        <a href="/season-analysis" class="back-button">🏆 Season Analysis</a>
                        <a href="/" class="back-button" style="background: linear-gradient(45deg, #8892b0, #64ffda);">🏠 Dashboard</a>
                    </div>
                </div>
            </body>
            </html>
            """
            
            return web.Response(text=html, content_type='text/html')
            
        except Exception as e:
            logger.error(f"💀 Error in Old Predictions panel: {e}")
            import traceback
            traceback.print_exc()
            
            error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error - Old Predictions</title>
                <style>
                    body {{ font-family: sans-serif; background: #1a1a2e; color: #fff; text-align: center; padding: 50px; }}
                    .error {{ background: rgba(255,107,107,0.2); border: 2px solid #ff6b6b; border-radius: 15px; padding: 30px; margin: 20px auto; max-width: 600px; }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h1>💀 Error Loading Old Predictions</h1>
                    <p>{str(e)}</p>
                    <p><a href="/" style="color: #4ecdc4;">Return to Dashboard</a></p>
                </div>
            </body>
            </html>
            """
            return web.Response(text=error_html, content_type='text/html')
