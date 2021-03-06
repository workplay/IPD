# -*- coding: utf-8 -*-

import sympy as sym

p1, p4 = sym.symbols('p1 p4')
# p1 = 0.9
# p4 = 0

R = 3
S = 0
T = 5
P = 1

# p2, p3 = sym.symbols('p2 p3')
p2 = (p1*(T-P)-(1+p4)*(T-R))/(R-P) 
p3 = ((1-p1)*(P-S)+p4*(R-S))/(R-P)

print("p2=")
print(p2)
print("p3=")
print(p3)