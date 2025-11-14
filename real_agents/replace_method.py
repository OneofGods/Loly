#!/usr/bin/env python3
"""
🔥💀🔥 BROTHER #182: Replace handle_midnight_predictions method! 💀🔥💀
"""

import sys

# Read the dashboard file
with open('complete_real_dashboard.py', 'r') as f:
    lines = f.readlines()

# Read the new method
with open('new_midnight_predictions_method.py', 'r') as f:
    new_method = f.read()

# Find the method boundaries
# Line 6210 starts the method (index 6209)
# Line 7302 starts next method (index 7301)
start_line = 6209  # 0-indexed
end_line = 7301     # 0-indexed (this line should be kept)

print(f"🔥 Replacing lines {start_line+1} to {end_line} (old method)")
print(f"📊 Old method: {end_line - start_line} lines")
print(f"📊 New method: {len(new_method.splitlines())} lines")

# Replace the method
new_lines = lines[:start_line] + [new_method + '\n'] + lines[end_line:]

# Write back
with open('complete_real_dashboard.py', 'w') as f:
    f.writelines(new_lines)

print("✅ Method replaced successfully!")
print(f"📊 New file has {len(new_lines)} lines (was {len(lines)} lines)")
