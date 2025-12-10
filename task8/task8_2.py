#!/usr/bin/env python3

import time
from collections import deque

def split(s, delimiter):
    return s.split(delimiter)

def squared_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

def complete(connectivity_list):
    n = len(connectivity_list)
    if n == 0:
        return True
    visited = [False] * n
    queue = deque([0])
    visit_count = 0
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        visit_count += 1
        for neighbor in connectivity_list[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
    return visit_count == n


with open('input', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

start = time.perf_counter_ns()

posns = []
for line in lines:
    vals = split(line, ',')
    posns.append([int(vals[0]), int(vals[1]), int(vals[2])])


squareddists = []
n = len(posns)
for i in range(n):
    for j in range(i + 1, n):
        d2 = squared_dist(posns[i], posns[j])
        squareddists.append((d2, (i, j)))


squareddists.sort(key=lambda x: x[0])

connectivity_list = [[] for _ in range(n)]
out = 0

for d2, (i, j) in squareddists:
    connectivity_list[i].append(j)
    connectivity_list[j].append(i)
    if complete(connectivity_list):
        out = posns[i][0] * posns[j][0]
        print(posns[i][0], posns[j][0])
        break

end = time.perf_counter_ns()
elapsed_us = (end - start) // 1000
print(f"elapsed time: {elapsed_us}")
print(out)
