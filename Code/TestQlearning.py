import qlearning
import random as rnd

def epsilon_greedy(qfunc, s, epsilon=0.1):
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

qlearning = qlearning.Qlearning()
qfunc, _ = qlearning.initialize_QandE()
actions = ['w', 'e', 's', 'n']
diff = 100000
gamma = 0.5
alpha = 0.1
sum_q = 0
cnt = 0
while diff > 1e-7:
    s = rnd.randint(1, 13)
    if s == 12:
        continue
    t = False
    while t == False:
        act = epsilon_greedy(qfunc, s)
        t, new_s, r = qlearning.transform(s, act)
        q_list = []
        for a in actions:
            key = str(new_s) + "_" + a
            q_list.append(qfunc[key])

        action_index = q_list.index(max(q_list))
        max_key = str(new_s) + "_" + actions[action_index]
        curr_key = str(s) + "_" + act

        qfunc[curr_key] += alpha * (r + gamma * qfunc[max_key] - qfunc[curr_key])

        s = new_s

    diff = abs(sum_q - sum(qfunc.values()))
    sum_q = sum(qfunc.values())

    cnt+=1
print(cnt)
best_policy = []
for i in range(1, 14):
    q_temp = []
    a_temp = []
    for k in qfunc.keys():
        if k.split('_')[0] == str(i):
            q_temp.append(qfunc[k])
            a_temp.append(k)
    indx = q_temp.index(max(q_temp))
    best_policy.append(a_temp[indx])

print(best_policy)

