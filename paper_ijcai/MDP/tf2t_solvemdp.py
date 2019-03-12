# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import mdptoolbox

r1 = pd.read_excel('payoff.xlsx',sheet_name='A1=C')
r2 = pd.read_excel('payoff.xlsx',sheet_name='A1=D')
R = np.array([r1.values, r2.values])

t1 = pd.read_excel('transition.xlsx',sheet_name='A1=C')
t2 = pd.read_excel('transition.xlsx',sheet_name='A1=D')
P = np.array([t1.values, t2.values])

print(R)
# print(P)
# print(P.shape)
# print(R)
# print(R.shape)
mdptoolbox.util.checkSquareStochastic(P[1])


rvi = mdptoolbox.mdp.RelativeValueIteration(P, R)
rvi.run()
print(rvi.average_reward)

p = rvi.policy

action_profiles = ['cc','cd','dc','dd']

index = 0
states = []
for ap1 in action_profiles:
    for ap2 in action_profiles:
            states = states + [ap1+','+ap2]

result =  [states] + [p]
print(result)
