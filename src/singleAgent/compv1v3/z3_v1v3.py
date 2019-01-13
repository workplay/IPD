# -*- coding: utf-8 -*-
from z3 import *
p1, p2, p3, p4 = Reals('p1 p2 p3 p4')

s = Solver()
s.add(p1>=0, p1<=1)
s.add(p2>=0, p2<=1)
s.add(p3>=0, p3<=1)
s.add(p4>=0, p4<=1)

s.add(p4>=0.5)
s.add(p2>=0.5)
s.add(p3+p4>=1)
s.add(p2+p3>=1)
s.add(p1+p4>=1)
s.add(p1+p2>=1)
s.add(p1+p3>=1)

# s.add(p1*p2 - p1*p4 + p2*p3 - p3*p4 + 2*p4 - 1 < 0)
# s.add(p1*p2 - p1*p4 + p3 + p4 - 1 < 0)
s.add(p1 + p2*p3 - p3*p4 + p4 - 1 < 0)
result = s.check()
if result == sat:
    print(s.model())
else:
    print("unsat")