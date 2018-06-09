# -*- coding: utf-8 -*-
import sympy as sym
from sympy import together, collect, simplify

p1 = sym.Symbol('p1')
p2 = sym.Symbol('p2')
p3 = sym.Symbol('p3')
p4 = sym.Symbol('p4')

f0  = -(2*p2 - 2)/(p2 - p4 - 1)
f15 = -(3*p1 - p3 - 3)/(p1 - p3 - 1)
exp = f0 - f15
# print(together(exp))

up = p1*p2 - 3*p1*p4 - p1 + p2*p3 - p2 + p3*p4 - p3 + 3*p4 + 1

print(together(up))