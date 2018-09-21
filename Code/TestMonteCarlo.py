import random as rnd
import MonteCarloMethod

mc = MonteCarloMethod.MonteCarlo()

s, a, r = mc.gen_randompi_sample(50)

mc.mc(0.5, s, a, r)
