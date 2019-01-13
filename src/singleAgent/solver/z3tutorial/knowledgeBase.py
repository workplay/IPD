# -*- coding: utf-8 -*-
from z3 import *

s = Solver()
[x,y] = z3.Reals('x y')
s.add(x>y)
s.add(x<0)
s.add(y>0)

result = s.check()
if (result == z3.sat):
    print(s.model())
if result == z3.sat:
	print("sat")
	print(s.model())
elif result == z3.unsat:
	print("unsat")
elif result == z3.unknown:
    print("unknown")