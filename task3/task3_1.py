#!/usr/bin/env python3

with open("input","r") as f:
    data = f.read().strip().split("\n")

def listify_s(s):
    return [int(x) for x in list(s)]
def find_max(lst):    
    m1,m2 = max(lst), None
    pos = lst.index(m1)
    #search backward
    if pos == len(lst)-1:
        del(lst[-1])
        lst = lst[::-1]
        m2 = max(lst)
        return int(f"{m2}{m1}")
    else:#search forward
        lst = lst[pos+1:]
        m2 = max(lst)
        return int(f"{m1}{m2}")            

S = 0
for v in data:
    S+=find_max(listify_s(v))

print(S)
