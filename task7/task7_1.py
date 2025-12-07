#!/usr/bin/env python3
import sys
import re
with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")


start_r, start_c = 0,data[0].index("S")

current_beams = {start_c}
split_count = 0

cols = len(data[0])
for r in range(start_r,len(data)-1):
    next_beams = set()
    for c in current_beams:
        cell_below = data[r + 1][c]
            
        if cell_below == '.':
            next_beams.add(c)
        elif cell_below == '^':
            split_count += 1
            
            if c > 0:
                next_beams.add(c - 1)
            if c < cols - 1:
                next_beams.add(c + 1)
        
    current_beams = next_beams
print(split_count)
