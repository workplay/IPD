# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from z3 import *
import sympy as sym

p1, p2, p3, p4 = z3.Reals('p1 p2 p3 p4')    
q1, q2, q3, q4 = z3.Reals('q1 q2 q3 q4')

D = p1*p2*q1*q2 - p1*p2*q1*q4 - p1*p2*q1 - p1*p2*q2*q3 + p1*p2*q3*q4 + p1*p2*q3 - p1*p3*q1*q3 + p1*p3*q1*q4 + p1*p3*q2*q3 - p1*p3*q2*q4 - p1*p4*q1*q2 + p1*p4*q1*q3 + p1*p4*q1 + p1*p4*q2*q4 - p1*p4*q3*q4 - p1*p4*q4 - p1*q1*q2 + p1*q1*q4 + p1*q1 - p2*p3*q1*q2 + p2*p3*q1*q3 + p2*p3*q2*q4 + p2*p3*q2 - p2*p3*q3*q4 - p2*p3*q3 - p2*p4*q1*q3 + p2*p4*q1*q4 + p2*p4*q2*q3 - p2*p4*q2*q4 + p2*q2*q3 - p2*q2 - p2*q3*q4 - p2*q3 + p2*q4 + p2 + p3*p4*q1*q2 - p3*p4*q1*q4 - p3*p4*q2*q3 - p3*p4*q2 + p3*p4*q3*q4 + p3*p4*q4 + p3*q1*q2 - p3*q2*q3 - p3*q2 + p3*q3 - p3*q4 - p4*q1*q4 + p4*q2 + p4*q3*q4 - p4*q3 + p4*q4 - p4 + q2 - q4 - 1   

s = z3.Solver()
s.add(p1>=0,p1<1)
s.add(p2>=0,p2<=1)
s.add(p3>=0,p3<=1)
s.add(p4>=0,p4<=1)
s.add(q1>0,q1<1)
s.add(q2>0,q2<1)
s.add(q3>0,q3<1)
s.add(q4>0,q4<1)
s.add(D == 0)
result = s.check()
if (result==z3.sat):
    print(s.model())
if (result==z3.unsat):
    print('unsat')



