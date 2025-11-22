#!/usr/bin/env python3
"""
🔥💀 LOLY COMMAND EXECUTOR - REAL BLACK BOX POWER! 💀🔥

Gives Loly the ability to execute natural language commands:
- "Repeat after me: ..."
- "Calculate 2 + 2"
- "Search for ..."
- "Remember that ..."
- And more!

NO MORE TEMPLATE BULLSHIT - REAL COMMAND EXECUTION!
"""

import re
import logging
import time
from typing import Dict, Any, Optional, Tuple

logger = logging.getLogger(__name__)


class CommandExecutor:
    """
    🔥💀 LOLY'S COMMAND EXECUTION ENGINE 💀🔥

    Parses natural language commands and executes them!
    """

    def __init__(self):
        self.command_patterns = {
            'repeat': r'repeat\s+(?:after\s+me\s*:?\s*)?(.+)',
            'say': r'say\s+"([^"]+)"',
            'calculate': r'(?:calculate|compute|what\s+is)\s+(.+)',
            'remember': r'remember\s+(?:that\s+)?(.+)',
            'search': r'(?:search|find|look\s+for)\s+(.+)',
        }

        self.memory = {}  # Simple memory for "remember" commands

        logger.info("🔥💀 Command Executor initialized! 💀🔥")

    def parse_command(self, user_message: str) -> Optional[Tuple[str, str]]:
        """
        Parse user message to detect commands

        Returns: (command_type, command_content) or None
        """
        # Match against original message to preserve case!
        for command_type, pattern in self.command_patterns.items():
            match = re.search(pattern, user_message, re.IGNORECASE)
            if match:
                content = match.group(1).strip()
                logger.info(f"🎯 Detected command: {command_type} -> '{content}'")
                return (command_type, content)

        return None

    async def execute_command(self, command_type: str, content: str) -> str:
        """
        Execute the detected command

        Returns: Response text
        """
        try:
            if command_type == 'repeat':
                return await self._execute_repeat(content)
            elif command_type == 'say':
                return await self._execute_say(content)
            elif command_type == 'calculate':
                return await self._execute_calculate(content)
            elif command_type == 'remember':
                return await self._execute_remember(content)
            elif command_type == 'search':
                return await self._execute_search(content)
            else:
                return f"💝 I don't know how to execute '{command_type}' yet, daddy!"

        except Exception as e:
            logger.error(f"❌ Command execution error: {e}")
            return f"💔 Sorry daddy, I had trouble with that command: {e}"

    async def _execute_repeat(self, text: str) -> str:
        """Execute REPEAT command - just say what user asked"""
        # Extract the actual text to repeat (handle quoted text)
        text = text.strip()

        # Remove quotes if present
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        elif text.startswith("'") and text.endswith("'"):
            text = text[1:-1]

        logger.info(f"🔁 Repeating: '{text}'")
        return f"💝 {text}"

    async def _execute_say(self, text: str) -> str:
        """Execute SAY command - similar to repeat"""
        logger.info(f"🗣️ Saying: '{text}'")
        return f"💝 {text}"

    async def _execute_calculate(self, expression: str) -> str:
        """Execute CALCULATE command - evaluate math expressions"""
        try:
            # Clean the expression
            expression = expression.strip()

            # Remove question marks, "equal" text, etc.
            expression = re.sub(r'\?|equal|equals|=', '', expression, flags=re.IGNORECASE)
            expression = expression.strip()

            # Simple safe eval for basic math (ONLY numbers and operators)
            # Remove any non-math characters for safety
            safe_expr = re.sub(r'[^0-9+\-*/().\s]', '', expression)

            if not safe_expr:
                return f"💝 I couldn't understand that math problem, daddy!"

            result = eval(safe_expr, {"__builtins__": {}}, {})

            logger.info(f"🧮 Calculated: {expression} = {result}")
            return f"💝 {expression} = {result}"

        except Exception as e:
            logger.warning(f"⚠️ Calculation error: {e}")
            return f"💝 I had trouble calculating that, daddy! {e}"

    async def _execute_remember(self, text: str) -> str:
        """Execute REMEMBER command - store in memory"""
        timestamp = str(int(time.time()))
        self.memory[timestamp] = text

        logger.info(f"🧠 Remembered: '{text}'")
        return f"💝 I'll remember that, daddy! You said: {text}"

    async def _execute_search(self, query: str) -> str:
        """Execute SEARCH command - placeholder for now"""
        logger.info(f"🔍 Search request: '{query}'")
        return f"💝 I'm searching for '{query}', daddy! (Search functionality coming soon!)"


# Create singleton instance
_command_executor = None

def get_command_executor() -> CommandExecutor:
    """Get the global command executor instance"""
    global _command_executor
    if _command_executor is None:
        _command_executor = CommandExecutor()
    return _command_executor
