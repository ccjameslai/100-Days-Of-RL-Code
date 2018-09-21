"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random as rnd

def transform(state, action):
    s_a_table = [[2,3,3,5,5,7,8,8],
                 [4,5,3,6,7,6,7,8],
                 [1,1,2,4,4,6,6,8],
                 [1,2,3,1,2,4,5,8]]

    dict_action = {'e':0,'s':1, 'w':2, 'n':3}

    new_state = s_a_table[dict_action[action]][state-1]

    terminal = False
    if new_state == 8:
        terminal = True

    return terminal, new_state, -1

class MonteCarlo(object):
    def __init__(self):
        self.states = [i+1 for i in range(8)]
        self.action = ['e', 's', 'w', 'n']
        self.terminal = 8

    def gen_randompi_sample(self, num):
        state_sample = []
        action_sample = []
        reward_sample = []

        for i in range(num):
            s_tmp = []
            a_tmp = []
            r_tmp = []
            s = self.states[int(rnd.random() * len(self.states))]
            t = False
            while t == False:
                a = self.action[int(rnd.random() * len(self.action))]
                t, new_s, r = transform(s, a)
                s_tmp.append(new_s)
                a_tmp.append(a)
                r_tmp.append(r)
                s = new_s

            state_sample.append(s_tmp)
            action_sample.append(a_tmp)
            reward_sample.append(r_tmp)

        return state_sample, action_sample, reward_sample

    def mc(self, gamma, state_sample, action_sample, reward_sample):
        vfunc = dict()
        nfunc = dict()
        for s in self.states:
            vfunc[s] = 0.0
            nfunc[s] = 0.0

        for iterl in range(len(state_sample)):
            G = 0.0

            for step in range(len(state_sample[iterl])-1, -1, -1):
                G *= gamma
                G += reward_sample[iterl][step]

            for step in range(len(state_sample[iterl])):
                s = state_sample[iterl][step]
                vfunc[s] += G
                nfunc[s] += 1.0
                G -= reward_sample[iterl][step]
                G /= gamma

        for s in self.states:
            if nfunc[s] > 0.000001:
                vfunc[s] /= nfunc[s]

        print('mc')
        print(vfunc)
        print(nfunc)
