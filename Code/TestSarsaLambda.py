import Sarsa
import random as rnd
import ActionPolicy

ap = ActionPolicy.Action_Policy()
sarsa = Sarsa.sarsa()
Q, E = sarsa.initialize_QandE()
gamma = 0.5
alpha = 0.1
lamda = 0.2
acts = ['w', 'e', 's', 'n']
cnt = 0
sum_Q = 0
delta_q = 10000

while cnt <= 1000 and delta_q > 1e-7:
    s = rnd.randint(1, 13)
    if s == 12:
        continue
    a = ap.epsilon_greedy(Q, s)
    t = False
    while t == False:
        t, new_s, r = sarsa.transform(s, a)
        new_a = ap.epsilon_greedy(Q, new_s)
        delta = sarsa.update_delta_with_lambda(s, new_s, a, new_a, r, Q)
        E[str(s) + "_" + a] += 1

        for st in range(1, 14):
            for at in acts:
                Q = sarsa.get_Qvalue_with_lambda(st, at, delta, Q, E)
                E[str(st) + "_" + at] *= gamma * lamda

        s = new_s
        a = new_a

    E = sarsa.initial_eligibility_trace(E)

    delta_q = abs(sum(Q.values()) - sum_Q)
    sum_Q = sum(Q.values())
    cnt += 1
print('iteration times: ', cnt)

best_policy = ap.get_best_policy(Q)
print(best_policy)