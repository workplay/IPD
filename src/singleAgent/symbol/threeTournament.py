# -*- coding: utf-8 -*-
import avepayoff as ap
import pandas as pd
import numpy as np
q1 = [0.9,0.5,0.2,0.1]
q2 = [0.9,0.9,0.9,0.9]

df = pd.DataFrame(columns=['p','q1' ,'score1', 'q2', 'score2', 'score'])
index = 0
candidates = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999]
for p1 in candidates:
    for p2 in candidates:
        for p3 in candidates:
            for p4 in candidates:
                p=[p1,p2,p3,p4]
                score1 = ap.avePayoff_cal(p,q1)[0] 
                score2 = ap.avePayoff_cal(p,q2)[0]
                score = 0.9 * score1 + 0.1 * score2
                df.loc[index] = [p, q1, score1, q2, score2, score]
                index += 1
                print(p, score)
df.to_excel('tournament.xlsx')

