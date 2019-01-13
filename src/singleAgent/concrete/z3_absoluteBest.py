# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd
from utils import *

# task: whether a strategy can be best response.
p1, p2, p3, p4 = z3.Reals('p1 p2 p3 p4')

[R,S,T,P]=[-1,-3,0,-2]
fileName = utils.getFileName(R,S,T,P)
df1 = pd.read_excel(fileName, sheet_name='Sheet1')

[R,S,T,P]=[3,0,5,1]
fileName = utils.getFileName(R,S,T,P)
df2 = pd.read_excel(fileName, sheet_name='Sheet1')
 
s = z3.Solver()
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)

duplicates = [4, 8]

i = 5
# compare one with all others

for j in range(0, df1.shape[0]):
    if (j != i) and (j not in duplicates):  
        s.push()
        f = eval(df1.iat[i,j])
        g = eval(df2.iat[i,j])        
        #print(i,j,f.subs([(p1, 1/2), (p2, 1/2), (p3, 1/2), (p4, 1/2)]))
        # print(i,j,f)
        s.add(f < 0)
        s.add(g < 0)
        result = s.check()
        if result == z3.sat:
            print(i,j,"sat")
            print(s.model())
        elif result == z3.unsat:
            print(i,j,"unsat")
        elif result == z3.unknown:
            print(i,j,"unknown")
        else:
            print("error check result")
        s.pop()
    