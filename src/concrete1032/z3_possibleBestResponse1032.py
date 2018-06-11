# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd

# task: whether a strategy can be best response.
p1, p2, p3, p4 = Reals('p1 p2 p3 p4')


df = pd.read_excel('SymbolicSubstraction1032.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()

s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)

duplicates = [4, 8]

# compare one with all others
for i in range(6,7):
    if (i in duplicates):
        continue
    s.push()
    for j in range(0, df.shape[0]):
        if (j != i) and (j not in duplicates):
        # careful: read data frame
            f = eval(df.iat[i,j])
            s.add(f > 0)
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
    