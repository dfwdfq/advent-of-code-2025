#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as f:
    data = f.read().strip().split("\n")

data = [tuple(map(int,x.split(","))) for x in data]

squares = []
for x1,y1 in data:
    for x2,y2 in data:
        if x1 == x2 and y1 == y2:
            continue

        S = (abs(x1-x2)+1)*(abs(y1-y2)+1)
        p1 = (x1,y1)
        p2 = (x2,y2)
        squares.append((p1,p2,S))

p1,p2,S = max(squares,key=lambda x:x[2])
print(p1,p2,S)
