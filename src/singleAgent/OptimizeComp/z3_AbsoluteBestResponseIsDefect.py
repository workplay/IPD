# -*- coding: utf-8 -*-
from z3 import *
# import pandas as pd

p1, p2, p3, p4 = Reals('p1 p2 p3 p4')
R, T, S, P = Reals('R T S P')
 
# read substractions from an external file.
# df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()
# s.set('timeout',10000)

#s.add(T>R, R>P, P>S)
c1=And([T>R, R>P, P>S])
#s.add(2*R > T+S)  
c2=And(2*R > T+S)  
#s.add(p1>0,p1<1)
c3=And(p1>0,p1<1)
#s.add(p2>0,p2<1)
c4=And(p2>0,p2<1)
#s.add(p3>0,p3<1)
c5=And(p3>0,p3<1)
#s.add(p4>0,p4<1)
c6=And(p4>0,p4<1)

# f_i_j is loaded from external file
# f_i_j means fi - fj
# f_i_j is the substraction of fi and fi
# it has been optimized - remove fraction and expand.
f_1_0 = P*p1*p2*p4 - P*p1*p4 - P*p2**2 - P*p2*p3*p4 + P*p2*p3 - P*p2*p4 + 2*P*p2 + P*p3*p4 - P*p3 + P*p4 - P + R*p2**2*p4 - R*p2*p4**2 - 2*R*p2*p4 + R*p4**2 + R*p4 - S*p2**2*p4 + S*p2**2 + S*p2*p4**2 + S*p2*p4 - 2*S*p2 - S*p4**2 + S - T*p1*p2*p4 + T*p1*p4 + T*p2*p3*p4 - T*p2*p3 + 2*T*p2*p4 - T*p3*p4 + T*p3 - 2*T*p4 # unsat
# f_1_1 = eval(df.iat[1,1])
# f_1_2 = eval(df.iat[1,2]) # timeout
# f_1_3 = eval(df.iat[1,3]) # unsat
# f_1_4 = eval(df.iat[1,4])
# f_1_5 = eval(df.iat[1,5]) # unsat
# f_1_6 = eval(df.iat[1,6]) # timeout
# f_1_7 = eval(df.iat[1,7]) # timeout
# f_1_8 = eval(df.iat[1,8])
# f_1_9 = eval(df.iat[1,9]) # unsat
# f_1_10 = eval(df.iat[1,10]) # timeout
# f_1_11 = eval(df.iat[1,11]) # timeout
# f_1_12 = eval(df.iat[1,12]) # unsat

expr = z3.ForAll([p1,p2,p3,p4],Implies(And([c3,c4,c5,c6]), z3.Exists([R,S,T,P], And([c1,c2,f_1_0 < 0]))))
s.add(expr)

result = s.check()
if result == z3.sat:
    print("sat")
    print(s.model())
elif result == z3.unsat:
    print("unsat")
elif result == z3.unknown:
    print("unknown")
else:
    print("error check result")


