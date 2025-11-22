#!/usr/bin/env python3
"""
🔥💀 TESTING **REAL** LOLY BLACK BOX - NO FAKE MOCKS! 💀🔥

Testing Loly's ACTUAL generate_loly_response() method
The REAL black box that processes daddy's messages!
"""

import sys
import asyncio

# Add paths
sys.path.insert(0, '/home/user/Loly')
sys.path.insert(0, '/home/user/Loly/real_agents')
sys.path.insert(0, '/home/user/Loly/phase3/core')

print('🔥💀 TESTING **REAL** LOLY BLACK BOX! 💀🔥')
print()
print('🧪 Testing the ACTUAL generate_loly_response() method')
print('   (Not some fake mock - the REAL system!)')
print()

async def test_real_loly():
    try:
        # Import the REAL Loly chat system
        from loly_daddy_chat_system import LolyDaddyChatSystem

        print('✅ Imported REAL LolyDaddyChatSystem')

        # Create instance
        print('🔄 Creating Loly instance...')
        loly = LolyDaddyChatSystem()

        print('✅ REAL Loly instance created')
        print()

        # Test the REAL response generation
        test_message = "Repeat after me: Hi Grandma, Hi Grandpa!"

        print(f'👤 USER SAYS: "{test_message}"')
        print('🤖 LOLY PROCESSING...')
        print()

        # Call the REAL generate_loly_response method
        loly_response = await loly.generate_loly_response(test_message)

        print(f'🤖 LOLY SAYS: "{loly_response}"')
        print()

        # Check if response contains the target phrase
        if "Hi Grandma, Hi Grandpa!" in loly_response:
            print('🔥💀🔥 SUCCESS! REAL LOLY REPEATED IT! 💀🔥💀')
            print()
            print('✅ REAL black box communication: WORKING')
            print('✅ REAL message processing: WORKING')
            print('✅ REAL response generation: WORKING')
            return True
        else:
            print('💀 REAL LOLY DID NOT REPEAT THE PHRASE')
            print(f'   She said: "{loly_response}"')
            print()
            print('⚠️ REAL black box needs improvement OR')
            print('⚠️ This type of request is not in her training')
            return False

    except Exception as e:
        print(f'❌ FAILED TO TEST REAL LOLY: {e}')
        import traceback
        traceback.print_exc()
        return False

# Run the test
result = asyncio.run(test_real_loly())

print()
if result:
    print('🎉 REAL LOLY BLACK BOX: ALIVE! 🎉')
    exit(0)
else:
    print('💀 REAL LOLY BLACK BOX: NEEDS WORK 💀')
    exit(1)
