# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd

p1, p2, p3, p4 = Reals('p1 p2 p3 p4')
R, T, S, P = Reals('R T S P')
 
df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()

# s.set('timeout',10000)

s.add(T>R, R>P, P>S)
s.add(2*R > T+S)  # this constraint is not necessary.
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)

f_1_0 = eval(df.iat[1,0]) # unsat
# f_1_1 = eval(df.iat[1,1])
f_1_2 = eval(df.iat[1,2]) # timeout
f_1_3 = eval(df.iat[1,3]) # unsat
# f_1_4 = eval(df.iat[1,4])
f_1_5 = eval(df.iat[1,5]) # unsat
f_1_6 = eval(df.iat[1,6]) # timeout
f_1_7 = eval(df.iat[1,7]) # timeout
# f_1_8 = eval(df.iat[1,8])
f_1_9 = eval(df.iat[1,9]) # unsat
f_1_10 = eval(df.iat[1,10]) # timeout
f_1_11 = eval(df.iat[1,11]) # timeout
f_1_12 = eval(df.iat[1,12]) # unsat


#condition = z3.And(f_1_0 >= 0, f_1_2 >= 0, f_1_3 >= 0, f_1_5 >= 0, f_1_6 >= 0, f_1_7 >= 0, f_1_9 >= 0, f_1_10 >= 0, f_1_11 >= 0, f_1_12 >= 0)
expr = z3.ForAll([p1,p2,p3,p4],z3.Exists([R,S,T,P], f_1_2 < 0 ))

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



# for i in range(1, df.shape[0]):
#     s.push()
#     # careful: read data frame
#     f = eval(df.iat[0,i])
#     # print(f<0)
#     s.add(f < 0)
#     result = s.check()
#     if result == z3.sat:
#         print(i,"sat")
#     elif result == z3.unsat:
#         print(i,"unsat")
#     elif result == z3.unknown:
#         print(i,"unknown")
#     else:
#         print("error check result")
#     s.pop()
