#!/usr/bin/env python3
import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

with open(sys.argv[1], "r") as f:
    data = f.read().strip().split("\n")

graph = {}
for line in data:
    device, outputs = line.split(": ")
    graph[device] = outputs.split()

@lru_cache(maxsize=None)
def count_paths(node, mask):
    new_mask = mask
    
    if node == "dac":
        new_mask |= 1
    if node == "fft":
        new_mask |= 2
    
    if node == "out":
        return 1 if new_mask == 3 else 0
    
    if node not in graph:
        return 0
    
    total = 0
    for neighbor in graph[node]:
        total += count_paths(neighbor, new_mask)
    
    return total

print(count_paths("svr", 0))
