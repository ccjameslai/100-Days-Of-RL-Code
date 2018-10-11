import qlearning
import random as rnd
import ActionPolicy


ap = ActionPolicy.Action_Policy()
qlearning = qlearning.Qlearning()
qfunc, _ = qlearning.initialize_QandE()

terminal_state = 12
diff = 100000
sum_q = 0
cnt = 0

while diff > 1e-7:
    s = rnd.randint(1, 13)
    if s == terminal_state:
        continue

    t = False
    while t == False:
        act = ap.epsilon_greedy(qfunc, s)
        t, new_s, r = qlearning.transform(s, act)

        qfunc = qlearning.get_Qvalue(s, new_s, act, r, qfunc)

        s = new_s

    diff = abs(sum_q - sum(qfunc.values()))
    sum_q = sum(qfunc.values())

    cnt += 1
print('iteration times: ', cnt)

best_policy = ap.get_best_policy(qfunc)
print(best_policy)

