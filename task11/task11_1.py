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
def count_paths(node):
    if node == "out":
        return 1
    if node not in graph:
        return 0
    return sum(count_paths(neighbor) for neighbor in graph[node])

print(count_paths("you"))
