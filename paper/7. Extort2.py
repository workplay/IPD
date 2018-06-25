# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd
import time

start_time = time.time()

p1, p2, p3, p4 = Reals('p1 p2 p3 p4')
R, T, S, P = z3.Reals('R T S P')

k = 2 # k for chi
m = Real('m') # m for phi
 
p1 = 1 - m*(k-1)*(R-P)/(P-S)
p2 = 1 - m*(1 + k*(T-P)/(P-S))
p3 = m * (k + (T-P)/(P-S))
p4 = 0

df = pd.read_excel('./data/SymbolicSubstraction.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()

s.add(T>R, R>P, P>S)
s.add(2*R > T+S)  # this constraint is not necessary.
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
# Previous we have assumed p4=0
# s.add(p4>0,p4<1) 

# range of chi and phi
s.add(k>1)
s.add(m>0)
s.add(m<(P-S)/((P-S)+k*(T-P)))

# compare formula 12 with all others
check_index = 12

# for i in range(0, df.shape[0]):
for i in range(0, df.shape[0]):
    s.push()
    # careful: read data frame
    
    if (df.iat[check_index,i]==0):
        continue
    f = eval(df.iat[check_index,i])
    # print(f<0)
    s.add(f < 0)
    result = s.check()
    # print(s)
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
    
print("--- %s seconds ---" % (time.time() - start_time))