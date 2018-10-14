import random as rnd
import numpy as np

class Action_Policy():
    def __init__(self, alpha=0.1, epsilon=0.1, gamma=0.5):
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.actions = ['w', 'e', 's', 'n']
        self.state_action = [[1, 1, 2, 4, 5, 5, 7, 7, 9, 10, 10, 12, 12],
                             [2, 3, 3, 4, 6, 6, 8, 8, 9, 11, 12, 12, 13],
                             [4, 2, 5, 7, 5, 9, 10, 11, 13, 10, 11, 12, 13],
                             [1, 2, 3, 1, 3, 6, 4, 8, 6, 7, 8, 12, 9]]  # W,E,S,N

    def greedy(self, vfunc, state):
        v_list = []
        for i in range(len(self.actions)):
            new_s = self.state_action[i][state - 1]
            v_list.append(vfunc[new_s])

        max_a = self.actions[v_list.index(max(v_list))]

        return max_a

    def epsilon_greedy(self, qfunc, state):
        pi = 1 - self.epsilon + float(self.epsilon / len(self.actions))
        temp = 0.0
        max_a = ''
        for a in self.actions:
            if temp < qfunc[str(state) + "_" + a]:
                temp = qfunc[str(state) + "_" + a]
                max_a = a
            else:
                max_a = self.actions[rnd.randint(0, 3)]

        prob = rnd.random()

        if prob <= pi:
            return max_a
        else:
            idx = rnd.randint(0, 3)
            return self.actions[idx]

    def get_best_policy(self, qfunc):
        best_policy = []
        for i in range(1, 14):
            if i == 12:
                continue
            q_temp = []
            a_temp = []
            for k in qfunc.keys():
                if k.split('_')[0] == str(i):
                    q_temp.append(qfunc[k])
                    a_temp.append(k)
            indx = q_temp.index(max(q_temp))
            best_policy.append(a_temp[indx])
        return best_policy