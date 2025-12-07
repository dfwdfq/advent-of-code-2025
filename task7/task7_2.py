#!/usr/bin/env python3
import sys


with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")


start_r, start_c = 0,data[0].index("S")
rows, cols = len(data), len(data[0])

dp_below = [1] * cols 

for r in range(rows - 2, start_r - 1, -1):
    dp_current = [0] * cols
    
    for c in range(cols):
        cell_below = data[r + 1][c]
        
        if cell_below == '.':
            dp_current[c] = dp_below[c]
        elif cell_below == '^':
            left = dp_below[c - 1] if c > 0 else 0
            right = dp_below[c + 1] if c < cols - 1 else 0
            dp_current[c] = left + right
    
    dp_below = dp_current

print(dp_below[start_c])
