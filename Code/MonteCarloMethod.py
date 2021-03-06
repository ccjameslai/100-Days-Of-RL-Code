"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random as rnd
from matplotlib import pyplot as plt

def transform(state, action):
    s_a_table = [[2,3,3,5,5,7,8,8],
                 [4,5,3,6,7,6,7,8],
                 [1,1,2,4,4,6,6,8],
                 [1,2,3,1,2,4,5,8]]

    dict_action = {'e':0, 's':1, 'w':2, 'n':3}

    new_state = s_a_table[dict_action[action]][state-1]

    terminal = False
    if new_state == 8:
        terminal = True

    if new_state == 8:
        reward = 10
    else:
        reward = -1

    return terminal, new_state, reward

def epsilon_greedy(qfunc, s, epsilon):
    action = ['e', 's', 'w', 'n']
    pi = 1 - epsilon + float(epsilon / len(action))
    temp = 0.0
    max_a = ''
    for a in action:
        if temp < qfunc[str(s) + "_" + a]:
            temp = qfunc[str(s) + "_" + a]
            max_a = a
        else:
            max_a = action[rnd.randint(0, 3)]

    other_action = action[:]
    other_action.remove(max_a)
    prob = rnd.random()

    if prob <= pi:
        return max_a
    else:
        idx = rnd.randint(0, 2)
        return other_action[idx]

def encode_state(cur_s, states):
    den = max(states) - min(states)
    return (float(cur_s - min(states)) + 0.1) / float(den)


class MonteCarlo(object):
    def __init__(self):
        self.states = [i+1 for i in range(8)]
        self.action = ['e', 's', 'w', 'n']
        self.terminal = 8
        self.s_a_table = [[2, 3, 3, 5, 5, 7, 8, 8],
                          [4, 5, 3, 6, 7, 6, 7, 8],
                          [1, 1, 2, 4, 4, 6, 6, 8],
                          [1, 2, 3, 1, 2, 4, 5, 8]]

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

    def mc_policy_evaluation(self, gamma, state_sample, action_sample, reward_sample):
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

        return vfunc

    def gradiant_based_policy_evaluation(self, func, gd_func, gamma=0.5):
        sum_theta = 0.0
        theta = [0] * 4
        diff = 1000000
        cnt = 0
        delta_list = []
        while diff > 10e-5 and cnt <= 1000:
            state_sample, action_sample, reward_sample = self.gen_randompi_sample(1)
            #print('state_sample', state_sample)
            #print('reward_sample', reward_sample)
            for iterl in range(len(state_sample)):
                G = 0.0
                for step in range(len(state_sample[iterl])-1, -1, -1):
                    G *= gamma
                    G += reward_sample[iterl][step]
                #print('G', G)

                for step in range(len(state_sample[iterl])):
                    cur_s = state_sample[iterl][step]
                    if cur_s == 8:
                        continue
                    #print('func', func(s, theta))
                    #print('gd_func', gd_func(s))
                    en_s = encode_state(cur_s, state_sample[iterl])
                    #print('encoded s', en_s)
                    delta_theta = 0.01 * (G - func(en_s, theta)) * np.array(gd_func(en_s))

                    #print('delta_theta', delta_theta)
                    theta += delta_theta

                    G -= reward_sample[iterl][step]
                    G /= gamma

            diff = abs(sum(theta) - sum_theta)
            delta_list.append(diff)
            #print('theta', theta)
            cnt+=1

        print('iteration times: ', cnt)

        v_func = []
        for s in range(1, 9):
            v = func(s, theta)
            v_func.append(v)

        plt.plot([d for d in range(len(delta_list))], delta_list, 'g-')
        plt.show()

        return v_func

    def mc_for_Q(self, num_iterl, epsilon):
        n = dict()
        qfunc = dict()
        gamma = 1

        for s in self.states:
            for a in self.action:
                qfunc["%d_%s"%(s, a)] = 0.0
                n["%d_%s"%(s, a)] = 0.00001

        for iterl in range(num_iterl):
            s_sample = []
            a_sample = []
            r_sample = []
            s = self.states[int(rnd.random() * len(self.states))]
            t = False
            count = 0

            while t == False and count <= 100:
                a = epsilon_greedy(qfunc, s, epsilon)
                t, new_s, r = transform(s, a)
                s_sample.append(s)
                a_sample.append(a)
                r_sample.append(r)
                s = new_s
                count+=1

            g = 0.0
            for i in range(len(s_sample)-1, -1, -1):
                g *= gamma
                g += r_sample[i]

            for i in range(len(s_sample)):
                key = "%d_%s"%(s_sample[i], a_sample[i])
                n[key] += 1.0
                qfunc[key] = round((qfunc[key] * (n[key]-1) + g) / n[key], 2)
                g -= r_sample[i]
                g /= gamma

        return qfunc

    def mc(self, start_position, qfunc):
        state_flow = ''
        while True:
            k_list = []
            v_list = []
            for k, v in qfunc.items():
                if str(start_position) == k.split('_')[0]:
                    k_list.append(k)
                    v_list.append(v)

            idx = v_list.index(max(v_list))
            a = k_list[idx].split('_')[1]
            a_idx = self.action.index(a)
            new_s = str(self.s_a_table[a_idx][int(start_position) - 1])
            state_flow += new_s + ', '
            start_position = new_s
            if start_position == '8':
                state_flow.strip(', ')
                break

        return state_flow
