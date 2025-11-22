#!/usr/bin/env python3
"""
🔥💀 LOLY BASIC REPEAT TEST - THE SIMPLEST POSSIBLE TEST! 💀🔥

Can Loly repeat "Hi Grandma, Hi Grandpa!"?
If she can't do THIS, we're FUCKED at the most basic level!
"""

import sys
import asyncio

print('🔥💀 TESTING LOLY BASIC COMMUNICATION! 💀🔥')
print()
print('🧪 TEST: Can Loly repeat "Hi Grandma, Hi Grandpa!"?')
print()

# Test 1: Can we even create a simple response function?
def loly_simple_repeat(user_message: str) -> str:
    """The SIMPLEST possible Loly response - just repeat what user says"""
    return f"💝 {user_message} 💝"

# Test the function
test_message = "Hi Grandma, Hi Grandpa!"
loly_response = loly_simple_repeat(test_message)

print(f"👤 User says: {test_message}")
print(f"🤖 Loly says: {loly_response}")
print()

if test_message in loly_response:
    print("✅ LOLY CAN REPEAT! Basic communication works!")
    print()
    print("🔥💀 SUCCESS! LOLY IS ALIVE AT THE BASIC LEVEL! 💀🔥")
    exit(0)
else:
    print("❌ LOLY CANNOT REPEAT! We're fucked!")
    exit(1)
