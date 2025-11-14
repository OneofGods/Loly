#!/usr/bin/env python3
"""
🔥💀🔥 LOLY'S WRITER AGENT - CONTENT CREATOR! 💀🔥💀

Multi-format content writing agent with templates and styles!

CAPABILITIES:
- Article writing
- Report generation
- Email composition
- Documentation
- Technical writing
- Marketing copy
- Multiple styles (formal, casual, technical)
- Template-based generation
- Auto-formatting

Port: 3203
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from aiohttp import web
import aiohttp_cors

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class WriterAgent:
    """
    ✍️ Writer Agent - Multi-format content generation
    """

    def __init__(self, port=3203):
        self.agent_id = f"writer_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.port = port

        # Content templates
        self.templates = self._load_templates()

        # Style configurations
        self.styles = {
            'standard': {
                'tone': 'professional',
                'formality': 'medium',
                'sentence_length': 'medium'
            },
            'formal': {
                'tone': 'formal',
                'formality': 'high',
                'sentence_length': 'long'
            },
            'casual': {
                'tone': 'friendly',
                'formality': 'low',
                'sentence_length': 'short'
            },
            'technical': {
                'tone': 'precise',
                'formality': 'high',
                'sentence_length': 'varied'
            },
            'marketing': {
                'tone': 'engaging',
                'formality': 'medium',
                'sentence_length': 'short'
            }
        }

        # Statistics
        self.stats = {
            'total_write_requests': 0,
            'successful_writes': 0,
            'failed_writes': 0,
            'articles_written': 0,
            'reports_written': 0,
            'emails_written': 0,
            'formats_applied': 0
        }

        logger.info(f"✍️ Writer Agent {self.agent_id} initialized on port {self.port}!")

    def _load_templates(self) -> Dict[str, str]:
        """📄 Load content templates"""
        return {
            'article': """# {title}

## Introduction
{introduction}

## Main Content
{main_content}

## Conclusion
{conclusion}

---
Written on {timestamp}
""",
            'report': """# {title}

**Date:** {timestamp}
**Author:** Loly Writer Agent

## Executive Summary
{executive_summary}

## Findings
{findings}

## Recommendations
{recommendations}

## Conclusion
{conclusion}
""",
            'email': """Subject: {subject}

Dear {recipient},

{opening}

{body}

{closing}

Best regards,
{sender}
""",
            'documentation': """# {title}

## Overview
{overview}

## Usage
{usage}

## Examples
{examples}

## Notes
{notes}
""",
            'technical': """# {title}

## Technical Specification

**Version:** {version}
**Date:** {timestamp}

### Description
{description}

### Implementation
{implementation}

### Requirements
{requirements}

### Testing
{testing}
"""
        }

    async def write(self, content_type: str, specifications: Dict[str, Any],
                   context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        ✍️ Write content based on type and specifications

        Args:
            content_type: Type of content (article, report, email, etc.)
            specifications: Content specifications (title, length, topics, etc.)
            context: Additional context for content

        Returns:
            Generated content
        """
        try:
            self.stats['total_write_requests'] += 1

            logger.info(f"✍️ Writing {content_type}: {specifications.get('title', 'Untitled')}")

            # Get template
            template = self.templates.get(content_type, self.templates['article'])

            # Generate content based on specifications
            content = await self._generate_content(content_type, specifications, context or {})

            # Apply template
            formatted_content = template.format(**content)

            # Update stats
            self.stats['successful_writes'] += 1
            if content_type == 'article':
                self.stats['articles_written'] += 1
            elif content_type == 'report':
                self.stats['reports_written'] += 1
            elif content_type == 'email':
                self.stats['emails_written'] += 1

            result = {
                'status': 'success',
                'content_type': content_type,
                'content': formatted_content,
                'word_count': len(formatted_content.split()),
                'specifications': specifications,
                'timestamp': datetime.now().isoformat()
            }

            return result

        except Exception as e:
            self.stats['failed_writes'] += 1
            logger.error(f"❌ Write error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    async def _generate_content(self, content_type: str, specs: Dict[str, Any],
                                context: Dict[str, Any]) -> Dict[str, str]:
        """🎨 Generate content based on specifications"""

        title = specs.get('title', 'Untitled')
        topic = specs.get('topic', title)
        style = specs.get('style', 'standard')

        # Base content generation
        content = {
            'title': title,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'version': '1.0'
        }

        if content_type == 'article':
            content.update({
                'introduction': f"This article explores {topic}. "
                               f"We will examine key aspects and provide insights based on current understanding.",
                'main_content': f"The primary focus of this piece is {topic}. "
                               f"Key considerations include various perspectives and practical applications. "
                               f"Through careful analysis, we can better understand the implications.",
                'conclusion': f"In summary, {topic} represents an important area of focus. "
                             f"Continued exploration and understanding will yield valuable insights."
            })

        elif content_type == 'report':
            content.update({
                'executive_summary': f"This report provides analysis of {topic}. "
                                    f"Key findings and recommendations are presented below.",
                'findings': f"Primary findings regarding {topic}:\n"
                           f"- Comprehensive analysis completed\n"
                           f"- Multiple data sources evaluated\n"
                           f"- Patterns and trends identified",
                'recommendations': f"Based on findings:\n"
                                  f"- Continue monitoring developments\n"
                                  f"- Implement suggested improvements\n"
                                  f"- Review progress quarterly",
                'conclusion': f"This report establishes a foundation for understanding {topic}."
            })

        elif content_type == 'email':
            recipient = specs.get('recipient', 'Team')
            sender = specs.get('sender', 'Loly Writer Agent')
            subject = specs.get('subject', f'Regarding {topic}')

            content.update({
                'subject': subject,
                'recipient': recipient,
                'sender': sender,
                'opening': f"I hope this message finds you well.",
                'body': f"I am writing to discuss {topic}. "
                       f"Please find the relevant information and considerations below.",
                'closing': f"Please let me know if you have any questions or need additional information."
            })

        elif content_type == 'documentation':
            content.update({
                'overview': f"Documentation for {topic}.",
                'usage': f"To use this feature, follow the guidelines provided in this documentation.",
                'examples': f"Example usage:\n```\n# Example code or usage here\n```",
                'notes': f"Additional notes and considerations for {topic}."
            })

        elif content_type == 'technical':
            content.update({
                'description': f"Technical specification for {topic}.",
                'implementation': f"Implementation details and architecture overview.",
                'requirements': f"- System requirements\n- Dependencies\n- Configuration",
                'testing': f"Testing procedures and validation methods."
            })

        else:
            # Default content
            content.update({
                'introduction': f"Content regarding {topic}.",
                'main_content': f"Main information about {topic}.",
                'conclusion': f"Summary of {topic}."
            })

        return content

    async def format(self, content_type: str, style: str = "standard") -> Dict[str, Any]:
        """
        🎨 Get formatting guidelines for content

        Args:
            content_type: Type of content
            style: Formatting style

        Returns:
            Formatting guidelines
        """
        try:
            self.stats['formats_applied'] += 1

            style_config = self.styles.get(style, self.styles['standard'])

            formatting = {
                'status': 'success',
                'content_type': content_type,
                'style': style,
                'configuration': style_config,
                'guidelines': {
                    'font_family': 'sans-serif',
                    'line_spacing': 1.5,
                    'margins': '1 inch',
                    'heading_style': 'bold',
                    'paragraph_indent': 'first-line' if style == 'formal' else 'none'
                },
                'timestamp': datetime.now().isoformat()
            }

            return formatting

        except Exception as e:
            logger.error(f"❌ Format error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get writer agent statistics"""
        return {
            'agent_id': self.agent_id,
            'port': self.port,
            'stats': self.stats,
            'available_templates': list(self.templates.keys()),
            'available_styles': list(self.styles.keys()),
            'timestamp': datetime.now().isoformat()
        }

    # =================== API ENDPOINTS ===================

    async def handle_write(self, request):
        """POST /api/write - Write content"""
        try:
            data = await request.json()

            content_type = data.get('content_type', 'article')
            specifications = data.get('specifications', {})
            context = data.get('context', {})

            result = await self.write(content_type, specifications, context)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Write endpoint error: {e}")
            return web.json_response({
                'status': 'error',
                'error': str(e)
            }, status=500)

    async def handle_format(self, request):
        """POST /api/format - Get formatting guidelines"""
        try:
            data = await request.json()

            content_type = data.get('content_type', 'article')
            style = data.get('style', 'standard')

            result = await self.format(content_type, style)

            return web.json_response(result)

        except Exception as e:
            logger.error(f"❌ Format endpoint error: {e}")
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
            'agent': 'writer_agent',
            'port': self.port,
            'timestamp': datetime.now().isoformat()
        })

    async def start_server(self):
        """🚀 Start the Writer Agent server"""
        logger.info(f"🚀 Starting Writer Agent on port {self.port}...")

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
        app.router.add_post('/api/write', self.handle_write)
        app.router.add_post('/api/format', self.handle_format)
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

        logger.info(f"🔥💀🔥 WRITER AGENT RUNNING ON PORT {self.port}! 💀🔥💀")
        logger.info(f"🌐 Access at: http://localhost:{self.port}")

        # Keep server running
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("🛑 Writer Agent shutting down...")


# =================== MAIN FUNCTION ===================

async def main():
    agent = WriterAgent(port=3203)
    await agent.start_server()


if __name__ == "__main__":
    asyncio.run(main())
