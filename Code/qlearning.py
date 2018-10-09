class Qlearning():
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

    def q_learning(self):
        return 0