import Sarsa
import random as rnd
import ActionPolicy


ap = ActionPolicy.Action_Policy()
sarsa = Sarsa.sarsa()
Q, E = sarsa.initialize_QandE()
gamma = 0.5
alpha = 0.1
cnt = 0
sum_Q = 0
delta_q = 10000
while delta_q > 1e-7:
    s = rnd.randint(1, 13)
    if s == 12:
        continue
    a = ap.epsilon_greedy(Q, s)
    t = False
    while t == False:
        t, new_s, r = sarsa.transform(s, a)
        new_a = ap.epsilon_greedy(Q, new_s)
        Q = sarsa.get_Qvalue(s, new_s, a, new_a, r, Q)

        s = new_s
        a = new_a

    delta_q = abs(sum(Q.values()) - sum_Q)
    sum_Q = sum(Q.values())
    cnt += 1
print('iteration times: ', cnt)

best_policy = ap.get_best_policy(Q)
print(best_policy)
