#!/usr/bin/env python3
"""
🤖💀🤖 DEEPSEEK INTEGRATION SERVICE - LOLY'S LLM BRAIN! 💀🤖💀

Phase 3D: DeepSeek LLM Integration

This service connects Loly to the local DeepSeek model for advanced reasoning:
- 🤖 Connect to local DeepSeek instance
- 🧠 Advanced reasoning for complex tasks
- 🎯 Prompt optimization for DeepSeek
- 📊 Response quality assessment
- 🔄 Fallback handling

🔥 LOLY'S REAL BRAIN - NO BLOOM, JUST DEEPSEEK POWER! 🔥
"""

import asyncio
import aiohttp
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import json

logger = logging.getLogger(__name__)


class DeepSeekIntegrationService:
    """
    🤖💀🤖 DEEPSEEK INTEGRATION SERVICE 💀🤖💀

    Connects Loly to local DeepSeek model for advanced reasoning!
    """

    def __init__(self, deepseek_url: str = "http://localhost:8000", model_name: str = "deepseek-coder"):
        self.service_id = f"deepseek_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.deepseek_url = deepseek_url
        self.model_name = model_name

        # DeepSeek configuration
        self.config = {
            'temperature': 0.7,          # Creativity level (0.0-1.0)
            'max_tokens': 2048,          # Maximum response length
            'top_p': 0.9,                # Nucleus sampling
            'frequency_penalty': 0.0,    # Reduce repetition
            'presence_penalty': 0.0,     # Encourage new topics
            'timeout': 60                # Request timeout in seconds
        }

        # Task-specific settings
        self.task_configs = {
            'code': {
                'temperature': 0.3,      # More deterministic for code
                'max_tokens': 4096,      # Longer for code
                'system_prompt': 'You are an expert programmer. Provide clean, efficient, well-documented code.'
            },
            'reasoning': {
                'temperature': 0.5,      # Balanced for reasoning
                'max_tokens': 2048,
                'system_prompt': 'You are a logical reasoning expert. Think step-by-step and provide clear explanations.'
            },
            'creative': {
                'temperature': 0.9,      # More creative
                'max_tokens': 2048,
                'system_prompt': 'You are a creative writer. Be imaginative and engaging.'
            },
            'analysis': {
                'temperature': 0.4,      # Analytical and precise
                'max_tokens': 3072,
                'system_prompt': 'You are a data analyst. Provide thorough, accurate analysis with insights.'
            }
        }

        # Statistics
        self.stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'total_tokens_used': 0,
            'average_response_time': 0.0,
            'requests_by_task_type': {}
        }

        # Cache for responses (optional optimization)
        self.response_cache = {}
        self.cache_enabled = False

        logger.info(f"🤖💀🤖 {self.service_id}: DeepSeek Integration Service initialized!")
        logger.info(f"   DeepSeek URL: {self.deepseek_url}")
        logger.info(f"   Model: {self.model_name}")

    async def call_deepseek(self, prompt: str, task_type: str = 'reasoning',
                           system_prompt: Optional[str] = None,
                           temperature: Optional[float] = None,
                           max_tokens: Optional[int] = None) -> Dict[str, Any]:
        """
        🤖 Call DeepSeek model for completion

        Args:
            prompt: The prompt to send to DeepSeek
            task_type: Type of task (code, reasoning, creative, analysis)
            system_prompt: Optional custom system prompt
            temperature: Optional temperature override
            max_tokens: Optional max tokens override

        Returns:
            Response from DeepSeek with status and content
        """
        try:
            self.stats['total_requests'] += 1
            start_time = datetime.now()

            # Track requests by task type
            if task_type not in self.stats['requests_by_task_type']:
                self.stats['requests_by_task_type'][task_type] = 0
            self.stats['requests_by_task_type'][task_type] += 1

            # Check cache
            if self.cache_enabled:
                cache_key = f"{task_type}:{prompt[:100]}"
                if cache_key in self.response_cache:
                    logger.info(f"✅ Cache hit for {task_type} task")
                    return self.response_cache[cache_key]

            # Get task-specific config
            task_config = self.task_configs.get(task_type, self.task_configs['reasoning'])

            # Build request payload
            request_data = {
                'model': self.model_name,
                'messages': [
                    {
                        'role': 'system',
                        'content': system_prompt or task_config['system_prompt']
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                'temperature': temperature if temperature is not None else task_config['temperature'],
                'max_tokens': max_tokens if max_tokens is not None else task_config['max_tokens'],
                'top_p': self.config['top_p'],
                'frequency_penalty': self.config['frequency_penalty'],
                'presence_penalty': self.config['presence_penalty']
            }

            # Call DeepSeek API
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.deepseek_url}/v1/chat/completions",
                    json=request_data,
                    timeout=aiohttp.ClientTimeout(total=self.config['timeout'])
                ) as response:

                    if response.status == 200:
                        result = await response.json()

                        # Extract response
                        content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
                        tokens_used = result.get('usage', {}).get('total_tokens', 0)

                        # Update stats
                        self.stats['successful_requests'] += 1
                        self.stats['total_tokens_used'] += tokens_used

                        response_time = (datetime.now() - start_time).total_seconds()
                        self._update_avg_response_time(response_time)

                        response_data = {
                            'status': 'success',
                            'content': content,
                            'tokens_used': tokens_used,
                            'response_time': response_time,
                            'model': self.model_name,
                            'task_type': task_type,
                            'timestamp': datetime.now().isoformat()
                        }

                        # Cache if enabled
                        if self.cache_enabled:
                            cache_key = f"{task_type}:{prompt[:100]}"
                            self.response_cache[cache_key] = response_data

                        logger.info(f"✅ DeepSeek {task_type} request successful ({tokens_used} tokens, {response_time:.2f}s)")

                        return response_data

                    else:
                        # DeepSeek returned error
                        error_text = await response.text()
                        self.stats['failed_requests'] += 1

                        logger.error(f"❌ DeepSeek error: {response.status} - {error_text}")

                        return {
                            'status': 'error',
                            'error': f'DeepSeek API error: {response.status}',
                            'error_details': error_text,
                            'timestamp': datetime.now().isoformat()
                        }

        except asyncio.TimeoutError:
            self.stats['failed_requests'] += 1
            logger.error(f"❌ DeepSeek request timeout ({self.config['timeout']}s)")

            return {
                'status': 'error',
                'error': 'DeepSeek request timeout',
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            self.stats['failed_requests'] += 1
            logger.error(f"❌ DeepSeek request failed: {e}")

            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    async def code_generation(self, task_description: str, language: str = 'python',
                             context: Optional[str] = None) -> Dict[str, Any]:
        """
        💻 Generate code using DeepSeek

        Args:
            task_description: What code to generate
            language: Programming language
            context: Optional context/requirements

        Returns:
            Generated code from DeepSeek
        """
        prompt = f"Generate {language} code for the following task:\n\n{task_description}"

        if context:
            prompt += f"\n\nContext:\n{context}"

        prompt += "\n\nProvide clean, well-documented, production-ready code."

        return await self.call_deepseek(prompt, task_type='code')

    async def code_review(self, code: str, language: str = 'python') -> Dict[str, Any]:
        """
        👁️ Review code using DeepSeek

        Args:
            code: Code to review
            language: Programming language

        Returns:
            Code review from DeepSeek
        """
        prompt = f"Review the following {language} code and provide:\n"
        prompt += "1. Issues and bugs\n"
        prompt += "2. Code quality assessment\n"
        prompt += "3. Suggestions for improvement\n"
        prompt += "4. Security concerns\n\n"
        prompt += f"Code:\n```{language}\n{code}\n```"

        return await self.call_deepseek(prompt, task_type='code')

    async def bug_fixing(self, code: str, error_description: str,
                        language: str = 'python') -> Dict[str, Any]:
        """
        🐛 Fix bugs using DeepSeek

        Args:
            code: Buggy code
            error_description: Description of the bug/error
            language: Programming language

        Returns:
            Fixed code from DeepSeek
        """
        prompt = f"Fix the following {language} code that has this error:\n\n"
        prompt += f"Error: {error_description}\n\n"
        prompt += f"Code:\n```{language}\n{code}\n```\n\n"
        prompt += "Provide the fixed code with explanations of what was wrong and how you fixed it."

        return await self.call_deepseek(prompt, task_type='code')

    async def complex_reasoning(self, question: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        🧠 Complex reasoning using DeepSeek

        Args:
            question: Question or problem to reason about
            context: Optional context

        Returns:
            Reasoning from DeepSeek
        """
        prompt = f"Question: {question}"

        if context:
            prompt += f"\n\nContext:\n{context}"

        prompt += "\n\nProvide step-by-step reasoning and a clear conclusion."

        return await self.call_deepseek(prompt, task_type='reasoning')

    async def data_analysis(self, data_description: str, analysis_goal: str) -> Dict[str, Any]:
        """
        📊 Data analysis using DeepSeek

        Args:
            data_description: Description of the data
            analysis_goal: What to analyze/find

        Returns:
            Analysis from DeepSeek
        """
        prompt = f"Analyze the following data:\n\n{data_description}\n\n"
        prompt += f"Analysis Goal: {analysis_goal}\n\n"
        prompt += "Provide insights, patterns, and actionable recommendations."

        return await self.call_deepseek(prompt, task_type='analysis')

    async def creative_writing(self, topic: str, style: str = 'professional',
                              length: str = 'medium') -> Dict[str, Any]:
        """
        ✍️ Creative writing using DeepSeek

        Args:
            topic: What to write about
            style: Writing style
            length: Desired length

        Returns:
            Written content from DeepSeek
        """
        prompt = f"Write about: {topic}\n"
        prompt += f"Style: {style}\n"
        prompt += f"Length: {length}\n\n"
        prompt += "Create engaging, well-structured content."

        return await self.call_deepseek(prompt, task_type='creative')

    def _update_avg_response_time(self, response_time: float):
        """Update average response time"""
        total_requests = self.stats['successful_requests']
        if total_requests > 0:
            current_avg = self.stats['average_response_time']
            self.stats['average_response_time'] = (
                (current_avg * (total_requests - 1) + response_time) / total_requests
            )

    async def health_check(self) -> Dict[str, Any]:
        """💚 Check if DeepSeek is available and responding"""
        try:
            # Simple test request
            result = await self.call_deepseek(
                "Reply with 'OK' if you can read this.",
                task_type='reasoning',
                max_tokens=10
            )

            if result['status'] == 'success':
                return {
                    'status': 'healthy',
                    'deepseek_url': self.deepseek_url,
                    'model': self.model_name,
                    'response_time': result.get('response_time', 0),
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return {
                    'status': 'unhealthy',
                    'error': result.get('error', 'Unknown error'),
                    'timestamp': datetime.now().isoformat()
                }

        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def get_stats(self) -> Dict[str, Any]:
        """📊 Get DeepSeek integration statistics"""
        success_rate = (
            (self.stats['successful_requests'] / max(self.stats['total_requests'], 1)) * 100
        )

        return {
            'service_id': self.service_id,
            'deepseek_url': self.deepseek_url,
            'model': self.model_name,
            'total_requests': self.stats['total_requests'],
            'successful_requests': self.stats['successful_requests'],
            'failed_requests': self.stats['failed_requests'],
            'success_rate': success_rate,
            'total_tokens_used': self.stats['total_tokens_used'],
            'average_response_time': self.stats['average_response_time'],
            'requests_by_task_type': self.stats['requests_by_task_type']
        }

    def enable_cache(self):
        """🔄 Enable response caching"""
        self.cache_enabled = True
        logger.info("✅ Response caching enabled")

    def disable_cache(self):
        """🔄 Disable response caching"""
        self.cache_enabled = False
        self.response_cache.clear()
        logger.info("🛑 Response caching disabled")

    def clear_cache(self):
        """🧹 Clear response cache"""
        self.response_cache.clear()
        logger.info("🧹 Response cache cleared")


# =================== FACTORY FUNCTION ===================

def create_deepseek_service(deepseek_url: str = "http://localhost:8000",
                           model_name: str = "deepseek-coder") -> DeepSeekIntegrationService:
    """🏭 Factory function to create DeepSeek integration service"""
    return DeepSeekIntegrationService(deepseek_url=deepseek_url, model_name=model_name)
