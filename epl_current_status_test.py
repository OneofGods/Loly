#!/usr/bin/env python3
"""
🏴󠁧󠁢󠁥󠁮󠁧󠁿💀 EPL CURRENT STATUS TEST - UNDERSTANDING THE BASELINE! 💀🏴󠁧󠁢󠁥󠁮󠁧󠁿
Before enhancing, we need to understand current EPL performance
"""

import asyncio
import sys
sys.path.append('real_agents')

async def comprehensive_epl_status_test():
    print('🏴󠁧󠁢󠁥󠁮󠁧󠁿💀 EPL COMPREHENSIVE STATUS TEST! 💀🏴󠁧󠁢󠁥󠁮󠁧󠁿')
    print('======================================================================')
    
    try:
        from premier_league_fetcher import RealPremierLeagueFetcher
        
        # Test EPL data quality and algorithm performance
        fetcher = RealPremierLeagueFetcher()
        games = await fetcher.fetch_todays_real_premier_league_games()
        
        print(f'📊 EPL GAMES AVAILABLE: {len(games)}')
        print()
        
        if games:
            print('🎯 ANALYZING EPL ALGORITHM STRUCTURE:')
            print('======================================================================')
            
            sample_games = games[:5]  # Test first 5 games
            
            for i, game in enumerate(sample_games):
                home_team = game.get('home_team', 'Unknown')
                away_team = game.get('away_team', 'Unknown')
                prediction = game.get('prediction', 'NO PREDICTION')
                confidence = game.get('confidence', 0)
                algorithm = game.get('algorithm_used', 'UNKNOWN')
                
                print(f'🏴󠁧󠁢󠁥󠁮󠁧󠁿 Game {i+1}: {away_team} @ {home_team}')
                print(f'   🎯 Prediction: {prediction}')
                print(f'   📊 Confidence: {confidence}%')
                print(f'   🔬 Algorithm: {algorithm}')
                
                # Check for detailed analysis
                analysis_keys = [k for k in game.keys() if 'analysis' in k.lower() or 'factor' in k.lower()]
                if analysis_keys:
                    print(f'   📋 Analysis Available: {len(analysis_keys)} factors')
                    for key in analysis_keys[:3]:  # Show first 3
                        value = game.get(key, 'N/A')
                        print(f'      • {key}: {value}')
                else:
                    print(f'   ❌ Limited Analysis Available')
                
                print()
            
            # Analyze overall EPL characteristics
            print('🔍 EPL LEAGUE CHARACTERISTICS DETECTED:')
            print('======================================================================')
            
            home_predictions = sum(1 for g in games if g.get('home_team', '').upper() in g.get('prediction', '').upper())
            away_predictions = sum(1 for g in games if g.get('away_team', '').upper() in g.get('prediction', '').upper())
            draw_predictions = sum(1 for g in games if 'DRAW' in g.get('prediction', '').upper())
            total_predictions = len([g for g in games if g.get('prediction')])
            
            if total_predictions > 0:
                home_pct = (home_predictions / total_predictions) * 100
                away_pct = (away_predictions / total_predictions) * 100
                draw_pct = (draw_predictions / total_predictions) * 100
                
                print(f'🏠 HOME PREDICTIONS: {home_pct:.1f}% ({home_predictions}/{total_predictions})')
                print(f'✈️ AWAY PREDICTIONS: {away_pct:.1f}% ({away_predictions}/{total_predictions})')
                print(f'🎲 DRAW PREDICTIONS: {draw_pct:.1f}% ({draw_predictions}/{total_predictions})')
                print()
            
            # Check confidence distribution
            confidences = [g.get('confidence', 0) for g in games if g.get('confidence')]
            if confidences:
                avg_confidence = sum(confidences) / len(confidences)
                max_confidence = max(confidences)
                min_confidence = min(confidences)
                
                print(f'📈 CONFIDENCE ANALYSIS:')
                print(f'   Average: {avg_confidence:.1f}%')
                print(f'   Range: {min_confidence:.1f}% - {max_confidence:.1f}%')
                print()
            
            # EPL-specific team analysis
            big_6_teams = ['ARSENAL', 'CHELSEA', 'LIVERPOOL', 'MANCHESTER CITY', 'MANCHESTER UNITED', 'TOTTENHAM']
            big_6_games = []
            
            for game in games:
                home = game.get('home_team', '').upper()
                away = game.get('away_team', '').upper()
                
                home_is_big6 = any(team in home for team in big_6_teams)
                away_is_big6 = any(team in away for team in big_6_teams)
                
                if home_is_big6 or away_is_big6:
                    big_6_games.append({
                        'game': f"{away} @ {home}",
                        'prediction': game.get('prediction', 'NO PREDICTION'),
                        'confidence': game.get('confidence', 0),
                        'both_big6': home_is_big6 and away_is_big6
                    })
            
            print(f'⭐ BIG 6 ANALYSIS:')
            print(f'   Games involving Big 6: {len(big_6_games)}/{len(games)}')
            
            if big_6_games:
                for bg in big_6_games[:3]:  # Show first 3
                    print(f'   🏆 {bg["game"]}: {bg["prediction"]} ({bg["confidence"]}%)')
                print()
            
            # Algorithm readiness assessment
            print('🎯 EPL ALGORITHM READINESS ASSESSMENT:')
            print('======================================================================')
            
            # Check for key components
            has_predictions = all(g.get('prediction') for g in games[:3])
            has_confidence = all(g.get('confidence', 0) > 0 for g in games[:3])
            has_analysis = any('analysis' in str(g.keys()).lower() for g in games[:3])
            
            readiness_score = 0
            if has_predictions:
                readiness_score += 40
                print('✅ Predictions: Working')
            else:
                print('❌ Predictions: Missing')
            
            if has_confidence:
                readiness_score += 30
                print('✅ Confidence: Working')
            else:
                print('❌ Confidence: Missing')
            
            if has_analysis:
                readiness_score += 30
                print('✅ Analysis: Available')
            else:
                print('⚠️ Analysis: Limited')
            
            print(f'📊 EPL READINESS SCORE: {readiness_score}/100')
            print()
            
            if readiness_score >= 70:
                print('🚀 EPL STATUS: READY FOR ENHANCEMENT!')
                print('🎯 NEXT STEP: Apply EPL-specific improvements')
            elif readiness_score >= 50:
                print('⚡ EPL STATUS: NEEDS TUNING')
                print('🔧 NEXT STEP: Fix core components first')
            else:
                print('🔨 EPL STATUS: NEEDS MAJOR WORK')
                print('🚧 NEXT STEP: Rebuild core algorithm')
            
        return len(games)
        
    except Exception as e:
        print(f'💀 Critical EPL analysis error: {e}')
        import traceback
        traceback.print_exc()
        return 0

if __name__ == "__main__":
    games = asyncio.run(comprehensive_epl_status_test())
    print(f'\\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 EPL COMPREHENSIVE ANALYSIS COMPLETE: {games} games analyzed')
    print('🔥💀🔥 READY TO PROCEED WITH EPL ENHANCEMENT! 💀🔥💀')