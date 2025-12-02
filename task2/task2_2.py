#!/usr/bin/env python3
import re

def is_invalid(s):
    match = re.match(r"^(\d+)\1+$",s)
    return True if match else False


with open("input","r") as f:
    data = f.read().strip().split(",")


S = 0
for r in data:
    a,b = r.split("-")
    a,b = int(a),int(b)
    for val in range(a,b+1):
        if is_invalid(str(val)):
            S+=val

print(S)
