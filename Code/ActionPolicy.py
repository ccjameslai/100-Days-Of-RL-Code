import random as rnd

class Action_Policy():
    def __init__(self, alpha=0.1, epsilon=0.1, gamma=0.5):
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon

    def epsilon_greedy(self, qfunc, state):
        action = ['e', 's', 'w', 'n']
        pi = 1 - self.epsilon + float(self.epsilon / len(action))
        temp = 0.0
        max_a = ''
        for a in action:
            if temp < qfunc[str(state) + "_" + a]:
                temp = qfunc[str(state) + "_" + a]
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