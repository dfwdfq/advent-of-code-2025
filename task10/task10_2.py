#!/usr/bin/env python3
import sys
import pulp

with open(sys.argv[1], "r") as f:
    data = f.read().strip().split("\n")

def prep(entry):
    return [int(x) for x in entry.replace("(", "").replace(")", "").split(",")]

S = 0

for v in data:
    joltage_start = v.index("{")
    
    buttons_part = v[:joltage_start].strip()
    parts = buttons_part.split()
    
    _, *button_strs = parts
    
    buttons = list(map(prep, button_strs))
    
    joltage_str = v[joltage_start+1:v.index("}")]
    target = [int(x) for x in joltage_str.split(",")]
    
    n = len(target)  
    m = len(buttons) 
    
    problem = pulp.LpProblem("Joltage_Configuration", pulp.LpMinimize)
    
    x_vars = [pulp.LpVariable(f'x_{j}', lowBound=0, cat='Integer') for j in range(m)]
    
    problem += pulp.lpSum(x_vars), "Total_Presses"
    
    for i in range(n):
        constraint_expr = pulp.lpSum(x_vars[j] for j in range(m) if i in buttons[j])
        problem += constraint_expr == target[i], f"Counter_{i}"
    
    solver = pulp.PULP_CBC_CMD(msg=False)
    problem.solve(solver)
    
    if pulp.LpStatus[problem.status] == 'Optimal':
        S += sum(int(pulp.value(var)) for var in x_vars)

print(S)
