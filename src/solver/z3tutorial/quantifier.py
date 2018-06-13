# -*- coding: utf-8 -*-
from z3 import *
x,y = Reals('x y')
s = z3.Solver()
s.add(z3.ForAll([x],z3.Exists([y],x==y)))
result = s.check()
print(result)
print(s.model())