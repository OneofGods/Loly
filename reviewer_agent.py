#!/usr/bin/env python3
"""
🔥💀🔥 LOLY'S REVIEWER AGENT - CODE & CONTENT CRITIC! 💀🔥💀

Multi-type review agent with quality analysis and suggestions!

CAPABILITIES:
- Code review (Python, JavaScript, etc.)
- Content review
- Documentation review
- Quality metrics analysis
- Complexity scoring
- Improvement suggestions
- Best practices checking
- Multiple strictness levels

Port: 3204
"""

import asyncio
import json
import logging
import re
from datetime import datetime
from typing import Dict, List, Any, Optional
from aiohttp import web
import aiohttp_cors

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ReviewerAgent:
    """
    👁️ Reviewer Agent - Code and content review with analysis
    """

    def __init__(self, port=3204):
        self.agent_id = f"reviewer_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.port = port

        # Review criteria by strictness
        self.strictness_levels = {
            'lenient': {
                'critical_only': True,
                'score_threshold': 50,
                'max_issues': 10
            },
            'standard': {
                'critical_only': False,
                'score_threshold': 70,
                'max_issues': 20
            },
            'strict': {
                'critical_only': False,
                'score_threshold': 85,
                'max_issues': 50
            },
            'critical': {
                'critical_only': False,
                'score_threshold': 95,
                'max_issues': 100
            }
        }

        # Statistics
        self.stats = {
            'total_reviews': 0,
            'code_reviews': 0,
            'content_reviews': 0,
            'analyses_performed': 0,
            'suggestions_generated': 0,
            'total_issues_found': 0
        }

        logger.info(f"👁️ Reviewer Agent {self.agent_id} initialized on port {self.port}!")

    async def review(self, content: str, review_type: str = "code",
                    strictness: str = "standard") -> Dict[str, Any]:
        """
        👁️ Review code or content

        Args:
            content: Code or content to review
            review_type: Type of review (code, content, documentation)
            strictness: Review strictness level

        Returns:
            Review results with issues and score
        """
        try:
            self.stats['total_reviews'] += 1

            logger.info(f"👁️ Reviewing {review_type} (strictness: {strictness})")

            # Get strictness config
            strictness_config = self.strictness_levels.get(strictness, self.strictness_levels['standard'])

            # Perform review based on type
            if review_type == "code":
                issues = await self._review_code(content, strictness_config)
                self.stats['code_reviews'] += 1
            elif review_type == "content":
                issues = await self._review_content(content, strictness_config)
                self.stats['content_reviews'] += 1
            elif review_type == "documentation":
                issues = await self._review_documentation(content, strictness_config)
            else:
                issues = []

            # Calculate score
            score = self._calculate_quality_score(content, issues, strictness_config)

            # Update stats
            self.stats['total_issues_found'] += len(issues)

            result = {
                'status': 'success',
                'review_type': review_type,
                'strictness': strictness,
                'quality_score': score,
                'issues': issues[:strictness_config['max_issues']],
                'total_issues': len(issues),
                'passed': score >= strictness_config['score_threshold'],
                'timestamp': datetime.now().isoformat()
            }

            return result

        except Exception as e:
            logger.error(f"❌ Review error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    async def _review_code(self, code: str, config: Dict) -> List[Dict[str, Any]]:
        """💻 Review code for quality issues"""
        issues = []

        # Check line length
        for i, line in enumerate(code.split('\n'), 1):
            if len(line) > 120:
                issues.append({
                    'line': i,
                    'severity': 'minor',
                    'type': 'style',
                    'message': f'Line exceeds 120 characters ({len(line)} chars)'
                })

        # Check for print statements (debugging code)
        if 'print(' in code:
            print_count = code.count('print(')
            issues.append({
                'severity': 'warning',
                'type': 'debugging',
                'message': f'Found {print_count} print statement(s) - consider using logging'
            })

        # Check for TODO comments
        if 'TODO' in code:
            todo_count = code.count('TODO')
            issues.append({
                'severity': 'info',
                'type': 'completeness',
                'message': f'Found {todo_count} TODO comment(s)'
            })

        # Check for exception handling
        if 'except:' in code and 'except Exception' not in code:
            issues.append({
                'severity': 'warning',
                'type': 'error_handling',
                'message': 'Bare except clause found - specify exception type'
            })

        # Check for docstrings
        if 'def ' in code and '"""' not in code and "'''" not in code:
            issues.append({
                'severity': 'minor',
                'type': 'documentation',
                'message': 'Functions should have docstrings'
            })

        # Count functions
        function_count = code.count('def ')
        if function_count > 10:
            issues.append({
                'severity': 'info',
                'type': 'complexity',
                'message': f'File contains {function_count} functions - consider splitting'
            })

        return issues

    async def _review_content(self, content: str, config: Dict) -> List[Dict[str, Any]]:
        """📝 Review content for quality issues"""
        issues = []

        # Check length
        word_count = len(content.split())
        if word_count < 50:
            issues.append({
                'severity': 'warning',
                'type': 'length',
                'message': f'Content is too short ({word_count} words)'
            })

        # Check for grammar issues (simple checks)
        if content.count('  ') > 0:
            issues.append({
                'severity': 'minor',
                'type': 'formatting',
                'message': 'Multiple consecutive spaces found'
            })

        # Check for headings
        if '# ' not in content and '## ' not in content:
            issues.append({
                'severity': 'info',
                'type': 'structure',
                'message': 'Content lacks headings/structure'
            })

        return issues

    async def _review_documentation(self, content: str, config: Dict) -> List[Dict[str, Any]]:
        """📚 Review documentation"""
        issues = []

        # Check for code examples
        if '```' not in content:
            issues.append({
                'severity': 'warning',
                'type': 'examples',
                'message': 'Documentation lacks code examples'
            })

        # Check for headings
        heading_count = content.count('#')
        if heading_count < 2:
            issues.append({
                'severity': 'warning',
                'type': 'structure',
                'message': 'Documentation lacks proper structure'
            })

        return issues

    def _calculate_quality_score(self, content: str, issues: List[Dict], config: Dict) -> float:
        """🎯 Calculate quality score (0-100)"""
        base_score = 100.0

        # Deduct points for issues
        for issue in issues:
            severity = issue.get('severity', 'info')
            if severity == 'critical':
                base_score -= 15
            elif severity == 'warning':
                base_score -= 5
            elif severity == 'minor':
                base_score -= 2
            elif severity == 'info':
                base_score -= 1

        # Bonus for good practices
        if '"""' in content or "'''" in content:
            base_score += 5  # Docstrings present

        if 'logging' in content:
            base_score += 3  # Uses logging

        return max(0, min(100, base_score))

    async def analyze(self, content: str, analysis_type: str = "quality_metrics") -> Dict[str, Any]:
        """
        📊 Analyze code or content

        Args:
            content: Content to analyze
            analysis_type: Type of analysis

        Returns:
            Analysis results
        """
        try:
            self.stats['analyses_performed'] += 1

            logger.info(f"📊 Analyzing: {analysis_type}")

            if analysis_type == "quality_metrics":
                metrics = self._calculate_quality_metrics(content)
            else:
                metrics = {}

            result = {
                'status': 'success',
                'analysis_type': analysis_type,
                'metrics': metrics,
                'timestamp': datetime.now().isoformat()
            }

            return result

        except Exception as e:
            logger.error(f"❌ Analysis error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def _calculate_quality_metrics(self, content: str) -> Dict[str, Any]:
        """📈 Calculate quality metrics"""
        lines = content.split('\n')
        words = content.split()

        metrics = {
            'line_count': len(lines),
            'word_count': len(words),
            'character_count': len(content),
            'average_line_length': len(content) / max(len(lines), 1),
            'blank_lines': sum(1 for line in lines if not line.strip()),
            'comment_lines': sum(1 for line in lines if line.strip().startswith('#')),
            'function_count': content.count('def '),
            'class_count': content.count('class '),
            'complexity_score': min(100, max(0, 100 - (len(lines) / 10)))  # Simple complexity
        }

        return metrics

    async def suggest(self, content: str, suggestion_type: str = "improvements") -> Dict[str, Any]:
        """
        💡 Generate improvement suggestions

        Args:
            content: Content to suggest improvements for
            suggestion_type: Type of suggestions

        Returns:
            Suggestions
        """
        try:
            self.stats['suggestions_generated'] += 1

            logger.info(f"💡 Generating suggestions: {suggestion_type}")

            suggestions = []

            if suggestion_type == "improvements":
                # Code improvement suggestions
                if 'print(' in content:
                    suggestions.append({
                        'category': 'logging',
                        'suggestion': 'Replace print() statements with proper logging',
                        'priority': 'medium',
                        'impact': 'Better debugging and production readiness'
                    })

                if '"""' not in content and "'''" not in content:
                    suggestions.append({
                        'category': 'documentation',
                        'suggestion': 'Add docstrings to functions and classes',
                        'priority': 'high',
                        'impact': 'Improved code maintainability and readability'
                    })

                if 'except:' in content:
                    suggestions.append({
                        'category': 'error_handling',
                        'suggestion': 'Specify exception types in except clauses',
                        'priority': 'high',
                        'impact': 'Better error handling and debugging'
                    })

                # Generic suggestions
                suggestions.append({
                    'category': 'testing',
                    'suggestion': 'Add unit tests for critical functions',
                    'priority': 'high',
                    'impact': 'Increased code reliability and confidence'
                })

                suggestions.append({
                    'category': 'performance',
                    'suggestion': 'Consider using async/await for I/O operations',
                    'priority': 'medium',
                    'impact': 'Better performance and scalability'
                })

            result = {
                'status': 'success',
                'suggestion_type': suggestion_type,
                'suggestions': suggestions,
                'total_suggestions': len(suggestions),
                'timestamp': datetime.now().isoformat()
            }

            return result

        except Exception as e:
            logger.error(f"❌ Suggestion error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get reviewer agent statistics"""
        return {
            'agent_id': self.agent_id,
            'port': self.port,
            'stats': self.stats,
            'strictness_levels': list(self.strictness_levels.keys()),
            'timestamp': datetime.now().isoformat()
        }

    # =================== API ENDPOINTS ===================

    async def handle_review(self, request):
        """POST /api/review - Review code/content"""
        try:
            data = await request.json()

            content = data.get('content', '')
            review_type = data.get('type', 'code')
            strictness = data.get('strictness', 'standard')

            result = await self.review(content, review_type, strictness)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Review endpoint error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_analyze(self, request):
        """POST /api/analyze - Analyze quality metrics"""
        try:
            data = await request.json()

            content = data.get('content', '')
            analysis_type = data.get('analysis_type', 'quality_metrics')

            result = await self.analyze(content, analysis_type)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Analyze endpoint error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_suggest(self, request):
        """POST /api/suggest - Generate suggestions"""
        try:
            data = await request.json()

            content = data.get('content', '')
            suggestion_type = data.get('suggestion_type', 'improvements')

            result = await self.suggest(content, suggestion_type)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Suggest endpoint error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_stats(self, request):
        """GET /api/stats - Get statistics"""
        try:
            stats = self.get_stats()
            return web.json_response(stats)

        except Exception as e:
            logger.error(f"❌ Stats endpoint error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_health(self, request):
        """GET /health - Health check"""
        return web.json_response({
            'status': 'healthy',
            'agent': 'reviewer_agent',
            'port': self.port,
            'timestamp': datetime.now().isoformat()
        })

    async def start_server(self):
        """🚀 Start the Reviewer Agent server"""
        logger.info(f"🚀 Starting Reviewer Agent on port {self.port}...")

        # Create web application
        app = web.Application()

        # Setup CORS
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*"
            )
        })

        # Add routes
        app.router.add_post('/api/review', self.handle_review)
        app.router.add_post('/api/analyze', self.handle_analyze)
        app.router.add_post('/api/suggest', self.handle_suggest)
        app.router.add_get('/api/stats', self.handle_stats)
        app.router.add_get('/health', self.handle_health)

        # Add CORS to all routes
        for route in list(app.router.routes()):
            cors.add(route)

        # Start server
        runner = web.AppRunner(app)
        await runner.setup()

        site = web.TCPSite(runner, 'localhost', self.port)
        await site.start()

        logger.info(f"🔥💀🔥 REVIEWER AGENT RUNNING ON PORT {self.port}! 💀🔥💀")
        logger.info(f"🌐 Access at: http://localhost:{self.port}")

        # Keep server running
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("🛑 Reviewer Agent shutting down...")


# =================== MAIN FUNCTION ===================

async def main():
    agent = ReviewerAgent(port=3204)
    await agent.start_server()


if __name__ == "__main__":
    asyncio.run(main())
