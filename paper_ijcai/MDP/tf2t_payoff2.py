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
  for nextstate in states:
    NewAP = nextstate[3:5]
    if (NewAP == 'cc'):
      payoff = 3
    elif (NewAP == 'cd'):
      payoff = 0
    elif (NewAP == 'dc'):
      payoff = 5
    elif (NewAP == 'dd'):
      payoff = 1
    df.loc[prevstate, nextstate] = payoff
df1 = df
df2 = df
# save to file
writer = pd.ExcelWriter('payoff.xlsx')
df1.to_excel(writer,'A1=C')
df2.to_excel(writer,'A1=D')
writer.save()