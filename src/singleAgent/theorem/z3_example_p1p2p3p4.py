# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd
import time

start_time = time.time()


p1, p2, p3, p4 = Reals('p1 p2 p3 p4')
R, T, S, P = Reals('R T S P')

 
df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()

s.add(T>R, R>P, P>S)
s.add(2*R > T+S)  # this constraint is not necessary.
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)


# s.add(p1 >= p2)
# have to satisfy some of them
s.add(p2 >= p4)
s.add(p4 >= p1)
s.add(p1 >= p3)

for i in range(1, df.shape[0]):
    s.push()
    # careful: read data frame
    f = eval(df.iat[0,i])
    # print(f<0)
    s.add(f < 0)
    result = s.check()
    if result == z3.sat:
        print(i,"sat")
    elif result == z3.unsat:
        print(i,"unsat")
    elif result == z3.unknown:
        print(i,"unknown")
    else:
        print("error check result")
    s.pop()
    
print("--- %s seconds ---" % (time.time() - start_time))