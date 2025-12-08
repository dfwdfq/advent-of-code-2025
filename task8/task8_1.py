#!/usr/bin/env python3
import time
from collections import deque

def split(s, delimiter):
    return s.split(delimiter)

def squared_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

# Read input
with open('input', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

start = time.perf_counter_ns()

# Parse positions
posns = []
for line in lines:
    vals = split(line, ',')
    posns.append([int(vals[0]), int(vals[1]), int(vals[2])])

# Compute all pairwise squared distances
squared_dists = []
n = len(posns)
for i in range(n):
    for j in range(i + 1, n):
        d2 = squared_dist(posns[i], posns[j])
        squared_dists.append((d2, (i, j)))

# Sort by distance
squared_dists.sort(key=lambda x: x[0])

# Build graph from the first n smallest edges
links = [[] for _ in range(n)]
for i in range(min(len(squared_dists), n)):
    _, (u, v) = squared_dists[i]
    links[u].append(v)
    links[v].append(u)

# Find connected components (BFS)
box_vals = [0] * n
cycle_num = 1
circuits = []

for i in range(n):
    if not links[i] or box_vals[i] != 0:
        continue
    queue = deque([i])
    cycle_size = 0
    while queue:
        node = queue.popleft()
        if box_vals[node] != 0:
            continue
        box_vals[node] = cycle_num
        cycle_size += 1
        for neighbor in links[node]:
            if box_vals[neighbor] == 0:
                queue.append(neighbor)
    circuits.append(cycle_size)
    cycle_num += 1

# Compute result
circuits.sort(reverse=True)
while len(circuits) < 3:
    circuits.append(0)
out = circuits[0] * circuits[1] * circuits[2]

# Output
end = time.perf_counter_ns()
elapsed_us = (end - start) // 1000
print(f"{elapsed_us}us")
print(out)
