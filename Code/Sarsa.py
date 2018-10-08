import random as rnd

class sarsa():
    def __init__(self):
        self.stateaction = [[1,1,2,4,5,5,7,7,9,10,10,12,12],
                            [2,3,3,4,6,6,8,8,9,11,12,12,13],
                            [4,2,5,7,5,9,10,11,13,10,11,12,13],
                            [1,2,3,1,3,6,4,8,6,7,8,12,9]]  # W,E,S,N

        self.actions = {0:'w',1:'e', 2:'s', 3:'n'}
        self.states = [i + 1 for i in range(13)]

    def initialize_QandE(self):
        Q = {}
        E = {}
        for a in range(len(self.stateaction)):
            for s in range(len(self.stateaction[0])):
                key = str(s+1) + "_" + str(self.actions[a])
                Q[key] = 0.0
                E[key] = 0.0

        return Q, E

    def transform(self, state, action):
        actions = ['w', 'e', 's', 'n']
        new_state = self.stateaction[actions.index(action)][state-1]

        terminal = False
        if new_state == 12:
            terminal = True

        if new_state == 12:
            reward = 100
        else:
            reward = -1

        return terminal, new_state, reward

    def epsilon_greedy(self, qfunc, s, epsilon=0.1):
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

    def gen_randompi_sample(self, num):
        action = ['e', 's', 'w', 'n']
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
                a = action[int(rnd.random() * len(action))]
                t, new_s, r = self.transform(s, a)
                s_tmp.append(new_s)
                a_tmp.append(a)
                r_tmp.append(r)
                s = new_s

            state_sample.append(s_tmp)
            action_sample.append(a_tmp)
            reward_sample.append(r_tmp)

        return state_sample, action_sample, reward_sample
