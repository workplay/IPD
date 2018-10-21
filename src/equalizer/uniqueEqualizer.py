# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from z3 import *
import sys

p1, p2, p3, p4 = Reals('p1 p2 p3 p4')
R, T, S, P = Reals('R T S P')

f0 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f1 =  (-P*p2 + P - R*p2*p4 + R*p4 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p4 - T*p3*p4 + T*p3)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
f2 =  (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p4 + S*p2*p4 - S*p4 - T*p4)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
f3 =  (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p3 + R*p3*p4 - R*p4 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p4 + T*p3*p4 - T*p3)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
f4 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f5 =  (-P*p2*p3 + P*p3 - R*p2*p3 + R*p3 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
f6 =  (P*p1*p3 - P*p3 - R*p3*p4 + S*p2*p4 - S*p4 - T*p3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
f7 =  (P*p1*p3 - P*p3 - R*p3 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
f8 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f9 =  (P*p1*p2 - P*p1 - P*p2 + P - R*p2*p4 + R*p4 + S*p1*p2 - S*p1 - S*p2 + S - T*p1*p3 + T*p3)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
f10 =  (P*p1*p3 - P*p1 - P*p3 + P + R*p2*p4 - S*p1*p4 + S*p4 - T*p1*p4 + T*p4)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
f11 =  -(P*p1*p3 - P*p1 - P*p3 + P + R*p2*p3 - R*p3*p4 + R*p4 - S*p1 + S - T*p1*p3 + T*p3)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
f12 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f13 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f14 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f15 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)

exprs = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]

# check for greatest
# check_index = 0
# comp_list = [10, 11]

s = z3.Solver()
s.set("timeout",60000)
s.add(T>R, R>P, P>S)
s.add(2*R > T+S)
s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)
s.add(f0 == f15)
s.add(f1 < f2)
print(s.check())
