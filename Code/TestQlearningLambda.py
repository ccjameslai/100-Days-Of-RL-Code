import qlearning
import random as rnd
import ActionPolicy


policy = ActionPolicy.Action_Policy()

q_learning = qlearning.Qlearning()
Q, E = q_learning.initialize_QandE()
actions = ['w', 'e', 's', 'n']

gamma = 0.5
alpha = 0.1
lamda = 0.2
delta = 0

batch = 500
cnt = 0
while cnt <= batch:
    init_s = rnd.randint(1, 13)
    init_a = policy.epsilon_greedy(Q, init_s)

    t = False
    while t == False:
        t, new_s, r = q_learning.transform(init_s, init_a)
        max_Q = 0.0001
        max_a = actions[rnd.randint(0, 3)]
        for i in range(len(actions)):
            if max_Q <= Q[str(new_s) + "_" + actions[i]]:
                max_Q = Q[str(new_s) + "_" + actions[i]]
                max_a = actions[i]

        delta = r + gamma * max_Q - Q[str(init_s) + "_" + init_a]
        E[str(init_s) + "_" + init_a] += 1

        for s in range(1, 14):
            for a in actions:
                Q[str(s) + "_" + a] += alpha * delta * E[str(s) + "_" + a]

                if a == max_a:
                    E[str(s) + "_" + a] *= gamma * lamda
                else:
                    E[str(s) + "_" + a] = 0

        init_s = new_s
        init_a = max_a

    cnt += 1

best_policy = policy.get_best_policy(Q)
print(best_policy)
