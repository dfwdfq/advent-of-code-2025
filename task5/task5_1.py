#!/usr/bin/env python3
import sys

with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")

sep = data.index("")
ranges_s = data[:sep]
ids    = [int(x) for x in data[sep+1:]]

ranges = []
for r in ranges_s:
    a,b = r.split("-")
    ranges.append(range(int(a),int(b)+1))

counter = 0
for i in ids:
    for r in ranges:
        if i in r:
            counter += 1
            break

print(counter)



        
