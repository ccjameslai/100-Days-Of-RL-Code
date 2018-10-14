import random as rnd
import ActionPolicy

'''
Value function would converge as using greedy as action policy.

But it would not converge in stochastic action policy.
'''


def transform(state, action):
    state_action = [[1, 1, 2, 4, 5, 5, 7, 7, 9, 10, 10, 12, 12],
                   [2, 3, 3, 4, 6, 6, 8, 8, 9, 11, 12, 12, 13],
                   [4, 2, 5, 7, 5, 9, 10, 11, 13, 10, 11, 12, 13],
                   [1, 2, 3, 1, 3, 6, 4, 8, 6, 7, 8, 12, 9]]  # W,E,S,N

    actions = ['w', 'e', 's', 'n']

    new_state = state_action[actions.index(action)][state - 1]

    terminal = False
    if new_state == 12:
        terminal = True

    if new_state == 12:
        reward = 100
    else:
        reward = -1

    return terminal, new_state, reward

def vfunction_with_TD_lambda():
    states = [i + 1 for i in range(13)]
    actions = ['w', 'e', 's', 'n']
    gamma = 0.5
    alpha = 0.5
    lmda = 0.6
    vfunc = {}
    e = {}
    ap = ActionPolicy.Action_Policy()

    for s in states:
        vfunc[s] = 0.0
        e[s] = 0.0

    num_of_episode = 0
    diff = 1000
    sum_v = 0
    while num_of_episode <= 1000 and diff > 1e-7:
        s = rnd.randint(1, len(states))
        t = False
        while t == False:
            #a = actions[rnd.randint(0, 3)]
            a = ap.greedy(vfunc, s)

            t, new_s, r = transform(s, a)
            delta = r + gamma * vfunc[new_s] - vfunc[s]
            e[s] += 1

            for st in states:
                vfunc[st] += alpha * delta * e[st]
                e[st] *= gamma * lmda

            s = new_s

        num_of_episode += 1

        diff = abs(sum(vfunc.values()) - sum_v)
        #print('diff', diff)
        #print('number of episode', num_of_episode)
        sum_v = sum(vfunc.values())

    print([round(v, 3) for v in vfunc.values()])
    return vfunc

ap = ActionPolicy.Action_Policy()
vfunc = vfunction_with_TD_lambda()
initial_state = rnd.randint(1, 13)
print('initial state', initial_state)
state_flow = []
action_flow = []
t = False
while t == False:
    if initial_state == 12:
        break
    action = ap.greedy(vfunc, initial_state)
    _, new_s, _ = transform(initial_state, action)
    state_flow.append(new_s)
    action_flow.append(action)
    initial_state = new_s

print('state flow', state_flow)
print('action flow', action_flow)