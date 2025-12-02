#!/usr/bin/env python3

with open("input2","r") as f:
    data = f.read().strip()

data = data.split("\n")


start = 50
counter = 0
for r in data:
    rotation = r[0]
    points   = int(r[1:])
    while points != 0:
        if rotation == "L":
            start-=1
            if start < 0:
                start = 99
        else:
            start+=1
            if start > 99:
                start = 0
        points -= 1

        if start == 0:
            counter+=1
        
                

    print("normalised value:{}".format(start))

print(counter)
  
