#!/usr/bin/env python3
import sys
from itertools import combinations

with open(sys.argv[1],"r") as f:
    data = f.read().strip().split("\n")

def prep(entry):
    return [int(x) for x in entry.replace("(","").replace(")","").split(",")]
def prep_light(light):
    return tuple(light.replace("[","").replace("]",""))

def apply_card(length, acts, light):
    min_presses = float('inf')
    target = list(light)
    
    for num_buttons in range(1, len(acts) + 1):
        for button_combo in combinations(acts, num_buttons):
            current_state = ['.'] * length
            
            for button in button_combo:
                for light_idx in button:
                    current_state[light_idx] = '#' if current_state[light_idx] == '.' else '.'
            
            if current_state == list(target):
                min_presses = num_buttons
                return min_presses
    
    return min_presses if min_presses != float('inf') else 0    
    

trimmed = []
for v in data:
    value = v[:v.index("{")]
    lights, *keys = value.strip().split(" ")
    keys = list(map(prep,keys))
    trimmed.append((prep_light(lights),keys))

S = 0
for light, acts in trimmed:
    S+=apply_card(len(light),acts,light)

print(S)
