# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random as rnd

act_and_state = [[1,1,2,4,5,6,7,8,8,9,10],
                 [2,3,4,4,5,7,7,9,10,11,11],
                 [5,2,6,4,8,10,7,8,9,10,11],
                 [1,2,3,4,1,3,7,5,9,6,7]]  # W,E,S,N

def getStateValue():
    state = [i+1 for i in range(11)]
    goal = 3
    trap = 6
    r = -3
    v = [0]*len(state)
    v[goal] = 100
    v[trap] = -100
    pre_state = 10000
    sum_v = 0
    temp_v = v[:]
    while abs(pre_state - sum_v) > 1e-5:
        pre_state = sum_v
        for i in range(len(state)):
            if i < 3 or i == 8:
                temp_v[i] = r + 0.8 * v[act_and_state[1][i] - 1] + 0.1 * v[act_and_state[2][i] - 1] + 0.1 * v[act_and_state[3][i] - 1]
            elif i == 4 or i == 5 or i == 7 or i == 9:
                temp_v[i] = r + 0.8 * v[act_and_state[3][i] - 1] + 0.1 * v[act_and_state[0][i] - 1] + 0.1 * v[act_and_state[1][i] - 1]
            elif i == 10:
                temp_v[i] = r + 0.8 * v[act_and_state[0][i] - 1] + 0.1 * v[act_and_state[2][i] - 1] + 0.1 * v[act_and_state[3][i] - 1]
            else:
                temp_v[3] = 100
                temp_v[6] = -100
        v = temp_v[:]
        sum_v = sum(v)
    
    return v
    
s_v = getStateValue()
start_state = rnd.randint(1,11)
print('start_state: {0}'.format(start_state))
temp_state = start_state
action = []
while True:
    if temp_state == 4 or temp_state == 7:
        action.append('x')
        break
    candi_v = [s_v[act_and_state[0][temp_state-1]-1], s_v[act_and_state[1][temp_state-1]-1], s_v[act_and_state[2][temp_state-1]-1], s_v[act_and_state[3][temp_state-1]-1]]
    action.append(candi_v.index(max(candi_v)))
    new_state = act_and_state[candi_v.index(max(candi_v))][temp_state-1]
    temp_state = new_state

directions = []    
for a in action:
    if a == 0:
        directions.append('<')
    elif a == 1:
        directions.append('>')
    elif a == 2:
        directions.append('v')
    elif a == 3:
        directions.append('^')
    else:
        directions.append('x')

print(directions)