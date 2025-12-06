#!/usr/bin/env python3
import sys
from functools import reduce

with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")

table = [x.split(" ") for x in data]
for i,t in enumerate(table):
    table[i] = [x for x in t if x != ""]


blobs = []
sup = len(table[0])
for i in range(sup):
    entry = []
    for j in range(len(table)):
        val = table[j][i]
        if val not in "+*":
            val = int(val)
        entry.append(val)
    blobs.append(entry)

operation = {
    "+":lambda a,b:a+b,
    "*":lambda a,b:a*b
    }
results = []
for entry in blobs:
    op, *tail = entry[::-1]
    results.append(reduce(operation[op],tail)) 

print(sum(results))
