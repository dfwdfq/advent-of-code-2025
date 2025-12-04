#!/usr/bin/env python3
import sys

def print_mat(mat):
    lst = ["".join(x) for x in mat]    
    for el in lst:
        print(el)

with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")
data = [list(x) for x in data]


HEIGHT = len(data)
WIDTH  = len(data[0])

counter = 0
dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
poses = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        el = data[y][x]
        if el == "@":
            rc = 0
            for d in dirs:
                dx,dy = d
                nx,ny = x+dx,y+dy
                if nx >= 0 and ny >= 0 and nx < WIDTH and ny <HEIGHT:
                    if data[ny][nx] == "@":
                        rc+=1
            if rc < 4:
                counter+=1

        
print(counter)
