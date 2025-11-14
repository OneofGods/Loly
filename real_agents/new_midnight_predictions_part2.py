            
            # Get season data from Midnight Special
            season_data = midnight_reader.get_season_predictions(live_league)
            accuracy_stats = midnight_reader.get_accuracy_stats(live_league)
            
            predictions = season_data.get('predictions', [])
            total_predictions = len(predictions)
            
            logger.info(f"📊 OLD PREDICTIONS: {total_predictions} predictions from Midnight Special automation")
            
            # Generate HTML
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>📜 Old Predictions - {live_league} Season</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: 'SF Pro Display', -apple-system, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: #fff; }}
                    .container {{ max-width: 1200px; margin: 0 auto; }}
                    .header {{ text-align: center; margin-bottom: 30px; }}
                    .title {{ font-size: 2.5em; font-weight: 800; margin: 0; background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
                    .subtitle {{ font-size: 1.2em; color: #8892b0; margin: 10px 0; }}
                    .automation-badge {{ display: inline-block; background: linear-gradient(45deg, #4ecdc4, #45b7d1); padding: 5px 15px; border-radius: 20px; font-size: 0.9em; font-weight: bold; margin: 10px 0; }}
                    .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 30px 0; }}
                    .stat-card {{ background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.2); }}
                    .stat-number {{ font-size: 2em; font-weight: bold; color: #4ecdc4; }}
                    .stat-label {{ font-size: 0.9em; color: #8892b0; margin-top: 5px; }}
                    .predictions-grid {{ display: grid; gap: 20px; }}
                    .prediction-card {{ background: rgba(255,255,255,0.05); border-radius: 15px; padding: 25px; border: 1px solid rgba(255,255,255,0.1); }}
                    .prediction-correct {{ border-left: 5px solid #4ecdc4; }}
                    .prediction-incorrect {{ border-left: 5px solid #ff6b6b; }}
                    .matchup {{ font-size: 1.4em; font-weight: bold; margin-bottom: 15px; text-align: center; }}
