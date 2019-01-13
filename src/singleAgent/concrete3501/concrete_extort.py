# -*- coding: utf-8 -*-
import sympy as sym

# p1, p2, p3, p4 = Reals('p1 p2 p3 p4')

R = 3
S = 0
T = 5
P = 1

# k = sym.symbols('k') # k for chi, m for phi
k=2

# m = sym.symbols('m')
m = 0.05

p1 = 1 - m*(k-1)*(R-P)/(P-S)
p2 = 1 - m*(1 + k*(T-P)/(P-S))
p3 = m * (k + (T-P)/(P-S))
p4 = 0

print(p1)
print(p2)
print(p3)
print(p4)