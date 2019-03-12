"""
    Compute all extreme values by letting pi = 0 or pi = 1.
    Some extreme values are the same.
        (0, 0, 0, 0) <-> (0, 1, 0, 0) <-> (1, 0, 0, 0)
        (1, 1, 0, 1) <-> (1, 1, 1, 0) <-> (1, 1, 1, 1)
"""
import sympy as sym

q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q3 = sym.Symbol('q3')
q4 = sym.Symbol('q4')

R = sym.Symbol('R', constant = True)
S = sym.Symbol('S', constant = True)
T = sym.Symbol('T', constant = True)
P = sym.Symbol('P', constant = True)

for p1 in range(2):
    for p2 in range(2):
        for p3 in range(2):
            for p4 in range(2):
                if (p1==1 and p2==1 and p3==0 and p4==0):
                    print([p1,p2,p3,p4])
                    continue;
                D_SX = sym.Matrix( \
                   [ [p1*q1-1, p1-1, q1-1, R],   \
                    [p2*q3, p2-1, q3, S], \
                    [p3*q2, p3, q2-1, T], \
                    [p4*q4, p4, q4, P] ])
                D_1 = sym.Matrix( \
                   [ [p1*q1-1, p1-1, q1-1, 1],   \
                    [p2*q3, p2-1, q3, 1], \
                    [p3*q2, p3, q2-1, 1], \
                    [p4*q4, p4, q4, 1] ])
                up = sym.simplify(sym.det(D_SX))
                down = sym.simplify(sym.det(D_1))
                s_X = sym.simplify(up/down)
                print([p1,p2,p3,p4],s_X)

