#!/usr/bin/env python3
import sys
from functools import reduce

with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")

data = [list(x) for x in data]

for _ in range(len(data[0])-len(data[-1])):
    data[-1].append(" ")

data = [list(row) for row in zip(*data)]
fluff = []
for _ in range(len(data[0])):
    fluff.append(" ")
data.append(fluff)

for v in data:
    print(v)
    

op = None
vals = []
take_op = True
S = 0
for entry in data:
    if take_op:
        op = entry[-1]
        entry.pop(-1)
        take_op = False
    val = "".join(entry)
    if entry.count(" ") == len(entry):
        vals = [int(x) for x in vals]
        print(vals,op)
        if op == "+":
            S+=reduce(lambda a,b:a+b,vals)
        else:
            S+=reduce(lambda a,b:a*b,vals)
        vals.clear()
        take_op = True
    else:
        vals.append(val)

print(S)
