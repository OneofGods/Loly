#!/usr/bin/env python3
"""
🔥💀🔥 BROTHER #182: Replace BOTH Midnight Critic AND Season Analysis! 💀🔥💀
"""

# Read the dashboard file
with open('complete_real_dashboard.py', 'r') as f:
    lines = f.readlines()

# Read the new methods
with open('new_handle_midnight_critic.py', 'r') as f:
    new_critic_method = f.read()

with open('new_handle_season_analysis.py', 'r') as f:
    new_season_method = f.read()

print("🔥💀🔥 REPLACING MIDNIGHT CRITIC AND SEASON ANALYSIS! 💀🔥💀\n")

# Find handle_midnight_critic boundaries
critic_start = None
critic_end = None
season_start = None
season_end = None

for i, line in enumerate(lines):
    if 'async def handle_midnight_critic(self, request):' in line:
        critic_start = i
        print(f"✅ Found handle_midnight_critic at line {i+1}")
    elif 'async def handle_season_analysis(self, request):' in line:
        season_start = i
        critic_end = i - 1  # End of critic method is line before season starts
        print(f"✅ Found handle_season_analysis at line {i+1}")
    elif season_start and 'async def' in line and i > season_start:
        season_end = i - 1  # Next method starts, so season ends here
        print(f"✅ Season analysis ends at line {i}")
        break

if not all([critic_start, critic_end, season_start, season_end]):
    print("❌ Could not find method boundaries!")
    print(f"critic_start: {critic_start}, critic_end: {critic_end}")
    print(f"season_start: {season_start}, season_end: {season_end}")
    exit(1)

print(f"\n📊 CRITIC METHOD:")
print(f"   Lines {critic_start+1} to {critic_end+1} ({critic_end - critic_start + 1} lines)")
print(f"\n📊 SEASON METHOD:")
print(f"   Lines {season_start+1} to {season_end+1} ({season_end - season_start + 1} lines)")

# Build new file
new_lines = (
    lines[:critic_start] +  # Everything before critic
    [new_critic_method + '\n'] +  # New critic method
    ['\n'] +  # Blank line
    [new_season_method + '\n'] +  # New season method
    lines[season_end+1:]  # Everything after season
)

# Write back
with open('complete_real_dashboard.py', 'w') as f:
    f.writelines(new_lines)

old_critic_size = critic_end - critic_start + 1
old_season_size = season_end - season_start + 1
old_total = old_critic_size + old_season_size

new_critic_size = len(new_critic_method.split('\n'))
new_season_size = len(new_season_method.split('\n'))
new_total = new_critic_size + new_season_size

print(f"\n✅ REPLACEMENT COMPLETE!")
print(f"\n📝 OLD SIZES:")
print(f"   Critic: {old_critic_size} lines")
print(f"   Season: {old_season_size} lines")
print(f"   Total: {old_total} lines")
print(f"\n📝 NEW SIZES:")
print(f"   Critic: {new_critic_size} lines")
print(f"   Season: {new_season_size} lines")
print(f"   Total: {new_total} lines")
print(f"\n📉 REDUCED BY: {old_total - new_total} lines")
print(f"\n🔥💀🔥 ELIMINATED ALL FAKE DATA BULLSHIT! 💀🔥💀")
