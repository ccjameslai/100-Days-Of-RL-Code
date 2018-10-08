import Sarsa
import random as rnd

sarsa = Sarsa.sarsa()
Q, E = sarsa.initialize_QandE()
gamma = 0.5
alpha = 0.1
cnt = 0
sum_Q = 0
delta_q = 10000
while delta_q > 1e-7 or cnt == 500:
    s = rnd.randint(1, 13)
    if s == 12:
        continue
    a = sarsa.epsilon_greedy(Q, s)
    t = False
    while t == False:
        t, new_s, r = sarsa.transform(s, a)
        new_a = sarsa.epsilon_greedy(Q, new_s)

        key = str(s) + "_" + str(a)
        new_key = str(new_s) + "_" + str(new_a)
        delta = r + gamma * Q[new_key] - Q[key]
        Q[key] += alpha * delta

        s = new_s
        a = new_a

    delta_q = abs(sum(Q.values()) - sum_Q)
    sum_Q = sum(Q.values())
    cnt+=1

best_policy = []
for s in range(1, 14):
    if s == 12:
        continue
    policy = []
    keys = []
    for k in Q.keys():
        if str(s) == k.split('_')[0]:
            policy.append(Q[k])
            keys.append(k)
    best_policy.append(keys[policy.index(max(policy))])

print(best_policy)
