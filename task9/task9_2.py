#!/usr/bin/env python3
import sys
from collections import deque

with open(sys.argv[1]) as f:
    data = f.read().strip().split("\n")

tiles = [tuple(map(int,x.split(","))) for x in data]

x_coords = {0}
y_coords = {0}
x_max = max(x for x, _ in tiles)
y_max = max(y for _, y in tiles)

for x, y in tiles:
    x_coords.add(x)
    y_coords.add(y)

x_coords.add(x_max + 1)
y_coords.add(y_max + 1)

sorted_x = sorted(x_coords)
sorted_y = sorted(y_coords)

x_map = {x: i for i, x in enumerate(sorted_x)}
y_map = {y: i for i, y in enumerate(sorted_y)}


compressed_grid = [[0] * len(y_map) for _ in range(len(x_map))]

num_tiles = len(tiles)
for i in range(num_tiles):
    (x1, y1) = tiles[i]
    (x2, y2) = tiles[(i + 1) % num_tiles]
    
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    if y1 == y2:  
        y_idx = y_map[y1]
        x_idx_min = x_map[x_min]
        x_idx_max = x_map[x_max]
        
        for x_idx in range(x_idx_min, x_idx_max + 1):
            compressed_grid[x_idx][y_idx] = 1
    elif x1 == x2:
        x_idx = x_map[x1]
        y_idx_min = y_map[y_min]
        y_idx_max = y_map[y_max]
        
        for y_idx in range(y_idx_min, y_idx_max + 1):
            compressed_grid[x_idx][y_idx] = 1

mx = len(compressed_grid)
my = len(compressed_grid[0])
queue = deque([(0, 0)])

if compressed_grid[0][0] == 0:
    compressed_grid[0][0] = 2

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while queue:
    cx, cy = queue.popleft()
    for dx, dy in neighbors:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < mx and 0 <= ny < my and compressed_grid[nx][ny] == 0:
            compressed_grid[nx][ny] = 2
            queue.append((nx, ny))

largest_size = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        
        if size > largest_size:
            x_min = x_map[min(x1, x2)]
            x_max = x_map[max(x1, x2)]
            y_min = y_map[min(y1, y2)]
            y_max = y_map[max(y1, y2)]
            
            inside = True
            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    if compressed_grid[x][y] == 2:
                        inside = False
                        break
                if not inside:
                    break
            
            if inside:
                largest_size = size

print(largest_size)
