# -*- coding: utf-8 -*-
import sympy as sym

# p1, p2, p3, p4 = Reals('p1 p2 p3 p4')

# R = 3
# S = 0
# T = 5
# P = 1
R,S,T,P = sym.symbols('R S T P')

k = sym.symbols('k') # k for chi, m for phi


m = sym.symbols('m')

p1 = 1 - m*(k-1)*(R-P)/(P-S)
# p2 = 1 - m*(1 + k*(T-P)/(P-S))
# p3 = m * (k + (T-P)/(P-S))
p4 = 0

p3 = ((1-p1)*(P-S)+p4*(R-S))/(R-P)

print(p3)