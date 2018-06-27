# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import pandas as pd 

R, T, S, P = sym.symbols('R T S P')
chi, phi = sym.symbols('chi phi')
p1 = 1 - phi*(chi-1)*(R-P)/(P-S)
# p2 = 1 - phi*(1 + chi*(T-P)/(P-S))
# p3 = phi * (chi + (T-P)/(P-S))
p4 = 0

E_p2 = (p1*(T-P)-(1+p4)*(T-R))/(R-P) 
E_p3 = ((1-p1)*(P-S)+p4*(R-S))/(R-P)
print(E_p2)
print(E_p3)