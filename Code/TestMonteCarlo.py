import random as rnd
import MonteCarloMethod
import copy
import numpy as np

def Test_gen_randompi_sample():
    mc = MonteCarloMethod.MonteCarlo()
    s, a, r = mc.gen_randompi_sample(50)
    print(s, a, r)

#Test_gen_randompi_sample()

def Test_mc_policy_evaluation():
    mc = MonteCarloMethod.MonteCarlo()
    s, a, r = mc.gen_randompi_sample(50)
    vfunc = mc.mc_policy_evaluation(0.5, s, a, r)
    print(vfunc)

#Test_mc_policy_evaluation()

def Test_epsilon_greedy():
    qf = {'1_e':100, '1_w':23, '1_n':66, '1_s':78}
    e_greedy_a = MonteCarloMethod.epsilon_greedy(qf, 1, 0.1)
    print(e_greedy_a)

#Test_epsilon_greedy()

def Test_mc_for_Q():
    mc = MonteCarloMethod.MonteCarlo()
    q = mc.mc_for_Q(100, 0.1)
    print(q)

#Test_mc_for_Q()

def Test_mc():
    mc = MonteCarloMethod.MonteCarlo()

    iter_num = 500
    epsilon = 0.1
    qfunc = mc.mc_for_Q(iter_num, epsilon)

    start_position = 4
    state_flow = mc.mc(start_position, qfunc)

    print(state_flow)

#Test_mc()

def poly_func(state, theta):
    #x = [state ** 6, state ** 5, state ** 4, state ** 3, state ** 2, state ** 1, 1]
    #x = [state ** 4, state ** 3, state ** 2, state ** 1, 1]
    x = [state ** 3, state ** 2, state ** 1, 1]
    #x = [state ** 2, state ** 1, 1]
    return np.array(theta).dot(np.array(x))

def gd_poly_func(state):
    #x = [state ** 6, state ** 5, state ** 4, state ** 3, state ** 2, state ** 1, 1]
    #x = [state ** 4, state ** 3, state ** 2, state ** 1, 1]
    x = [state ** 3, state ** 2, state ** 1, 1]
    #x = [state ** 2, state ** 1, 1]
    return x

def rbf(state, theta):


def Testgradiant_based_policy_evaluation():
    mc = MonteCarloMethod.MonteCarlo()

    v_func = mc.gradiant_based_policy_evaluation(poly_func, gd_poly_func)
    print(v_func)

Testgradiant_based_policy_evaluation()

