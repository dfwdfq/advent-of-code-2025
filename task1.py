#!/usr/bin/env python3

with open("input","r") as f:
    data = f.read().strip()

data = data.split("\n")


start = 50
counter = 0
for r in data:
    print(r)
    rotation = r[0]
    points   = int(r[1:])
    if rotation == "L":
        start = (start - points) % 100
    else:
        start = (start + points) % 100


    print("normalised value:{}".format(start))
    if start == 0:
        counter+=1

print(counter)
