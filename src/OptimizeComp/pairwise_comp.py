# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd

# task: whether a strategy can be best response.
p1, p2, p3, p4 = Reals('p1 p2 p3 p4')
# R, T, S, P = Reals('R T S P')
R = -1
T = 0
S = -3
P = -2

df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()

s.add(T>R, R>P, P>S)
s.add(2*R > T+S)
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)

duplicates = [4, 8]

# compare one with all others
i = 6
for j in range(0, df.shape[0]):
    if (j != i) and (j not in duplicates):
        s.push()
        # careful: read data frame
        f = eval(df.iat[i,j])
        s.add(f >= 0)
        result = s.check()
        if result == z3.sat:
            print(i,"sat")
            print(s.model())
        elif result == z3.unsat:
            print(i,"unsat")
        elif result == z3.unknown:
            print(i,"unknown")
        else:
            print("error check result")
        s.pop()
    
