#!/usr/bin/env python3
import functools

with open("input","r") as f:
    data = f.read().strip().split("\n")

@functools.cache
def find_max(val,digits):
    if digits == 0:
        return 0

    if len(val) == digits:
        return int(val)

    a = (int(val[0]) * 10 ** (digits - 1)) + find_max(val[1:], digits-1)

    b = find_max(val[1:], digits)

    return max(a, b)

S = 0
for v in data:
    S+= find_max(v,12)

print(S)
