#!/usr/bin/env python3
import sys
import threading

with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")

sep = data.index("")
ranges_s = data[:sep]

ranges = []
for r in ranges_s:
    a,b = r.split("-")
    ranges.append([int(a),int(b)])


#from https://www.geeksforgeeks.org/dsa/merging-intervals/
def mergeOverlap(arr):    
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

res = mergeOverlap(ranges)
counter = 0
for r in res:
    a,b = r
    counter+=b-a+1

print(counter)
