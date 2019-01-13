import pandas as pd
import numpy as np

action_profiles = ['cc','cd','dc','dd']

index = 0
states = []

for ap1 in action_profiles:
    for ap2 in action_profiles:
            states = states + [ap1+','+ap2]

'''
   TRANSITION FUNCTION   

   player 1 takes action c.
   player 2 takes action stochastic-tf2t.
       if player 1 defects for two rounds, then play c with probability 0.1
       otherwise play c with probability 0.9
'''
action = 'c'
df = pd.DataFrame(np.zeros(shape=(16, 16)), index = states, columns=states)
for prevstate in states:
    if prevstate[0] == 'd' and prevstate[3] == 'd':
        p2 = 0.1
    else:
        p2 = 0.9
    nextstate = prevstate[3:5] + ',' + action + 'c'
    df.loc[prevstate, nextstate] = p2
    nextstate = prevstate[3:5] + ',' + action + 'd'
    df.loc[prevstate, nextstate] = 1 - p2
df.to_excel('transition.xlsx', sheet_name = 'A1=C')
df1 = df

action = 'd'
df = pd.DataFrame(np.zeros(shape=(16, 16)), index = states, columns=states)
for prevstate in states:
    if prevstate[0] == 'd' and prevstate[3] == 'd':
        p2 = 0.1
    else:
        p2 = 0.9
    nextstate = prevstate[3:5] + ',' + action + 'c'
    df.loc[prevstate, nextstate] = p2
    nextstate = prevstate[3:5] + ',' + action + 'd'
    df.loc[prevstate, nextstate] = 1 - p2
df.to_excel('transition.xlsx', sheet_name = 'A1=D')
df2 = df

# save to file
writer = pd.ExcelWriter('transition.xlsx')
df1.to_excel(writer,'A1=C')
df2.to_excel(writer,'A1=D')
writer.save()