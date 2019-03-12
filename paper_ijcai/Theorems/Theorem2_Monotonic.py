"""
   Theorem 2. Assume 0 <= pi <= 1 and that 0 < qi < 1, 
        and p != (1,1,0,0).
        When all other variables are fixed, 
        s_X is monotonic to p1. (same to p2,p3,p4,q1,...,q4) 
    
    
    The output of this program is 0. (it may take some time to get the result)
"""

import sympy as sym
p1 = sym.Symbol('p1')
p2 = sym.Symbol('p2')
p3 = sym.Symbol('p3')
p4 = sym.Symbol('p4')
q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q3 = sym.Symbol('q3')
q4 = sym.Symbol('q4')

R = sym.Symbol('R', constant = True)
S = sym.Symbol('S', constant = True)
T = sym.Symbol('T', constant = True)
P = sym.Symbol('P', constant = True)

D_SY = sym.Matrix( \
   [ [p1*q1-1, p1-1, q1-1, R],   \
    [p2*q3, p2-1, q3, T], \
    [p3*q2, p3, q2-1, S], \
    [p4*q4, p4, q4, P] ])

D_1 = sym.Matrix( \
   [ [p1*q1-1, p1-1, q1-1, 1],   \
    [p2*q3, p2-1, q3, 1], \
    [p3*q2, p3, q2-1, 1], \
    [p4*q4, p4, q4, 1] ])

up = sym.det(D_SY)
down = sym.det(D_1)

diff_up = sym.simplify(sym.diff(up,p1)*down - up * sym.diff(down, p1))
print(sym.simplify(sym.diff(diff_up,p1)))