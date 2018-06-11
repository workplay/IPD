from z3 import *
import pandas as pd

p1, p2, p3, p4 = Reals('p1 p2 p3 p4')

# compare this with all others
f6   =  -(2*p1*p3 + 3*p2*p4 - p3*p4 - 2*p3 - 3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
    
f0   =  -(2*p2 - 2)/(p2 - p4 - 1)
f1   =  -(2*p2*p4 - 5*p2 - 2*p4 + 5)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
f2   =  -(2*p1*p2 - 2*p2*p3 + 2*p2*p4 + 2*p3 - 3*p4 - 2)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
f3   =  -(5*p1*p2 - 3*p1*p4 - 3*p2*p3 + p3*p4 + 2*p3 + 2*p4 - 5)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
f5   =  (3*p2*p3 - 3*p2*p4 + 3*p2 - 3*p3 + 3*p4 - 3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
f7   =  -(3*p1*p2 + 2*p1*p3 - 3*p1*p4 - 3*p3 + 3*p4 - 3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
f9   =  -(5*p1*p2 - 5*p1 - p2*p4 - 5*p2 + p4 + 5)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
f10   =  -(2*p1*p3 - 3*p1*p4 - 2*p1 + p2*p4 - 2*p3 + 3*p4 + 2)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
f11   =  (2*p1*p3 - 5*p1 + p2*p3 - p3*p4 - 2*p3 + p4 + 5)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
f12   =  -(3*p1 - p3 - 3)/(p1 - p3 - 1)

exprs = [f0, f1, f2, f3, f5, f7, f9, f10, f11, f12]

s = z3.Solver()
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)
for expr in exprs:
    s.add(f6 >= expr)
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
