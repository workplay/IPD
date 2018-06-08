# -*- coding: utf-8 -*-
from z3 import *
q1, q2, q3, q4 = Reals('q1 q2 q3 q4')
p = Real('p')
R, T, S, P = Reals('R T S P')

f0  = -P*p + P + T*p
f1  = (P*p - P + R*p**2 - R*p - S*p**2 + 2*S*p - S - T*p)/(p - 2)
f2  = (-P*p + P + R*p**2 - S*p**2 + S*p + T*p)/(p + 1)
f3  = -P*p/2 + P/2 + R*p/2 - S*p/2 + S/2 + T*p/2
f4  = -P*p + P + T*p
f5  = -P*p**2 + P*p - R*p**2 + R*p + S*p**2 - 2*S*p + S + T*p**2
f6  = -P*p/2 + P/2 + R*p/2 - S*p/2 + S/2 + T*p/2
f7  = -(P*p**2 - P*p - R*p + S*p - S - T*p**2)/(p + 1)
f8  = -P*p + P + T*p
f9  = -P*p/2 + P/2 + R*p/2 - S*p/2 + S/2 + T*p/2
f10 = P*p**2 - 2*P*p + P + R*p**2 - S*p**2 + S*p - T*p**2 + T*p
f11 = -(P*p**2 - 2*P*p + P + R*p - S*p + S - T*p**2 + T*p)/(p - 2)
f12 = R*p - S*p + S
f13 = R*p - S*p + S
f14 = R*p - S*p + S
f15 = R*p - S*p + S

exprs = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]

# check for greatest
check_index = 0

s = Solver()
s.add(T>R, R>P, P>S)
s.add(2*R > T+S)
s.add(p>0, p<1)
s.add(q1>0,q1<1)
s.add(q2>0,q2<1)
s.add(q3>0,q3<1)
s.add(q4>0,q4<1)
for i in range(len(exprs)):
    if (i == check_index):
        continue
    s.push()
    s.add(exprs[check_index] < exprs[i])
    result = s.check()
    if result == sat:
        print(i,s.model())
    else:
        print(i,"unsat",s)
    s.pop()