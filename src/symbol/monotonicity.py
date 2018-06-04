# -*- coding: utf-8 -*-
import sympy as sym
p1 = sym.Symbol('p1')
p2 = sym.Symbol('p2')
p3 = sym.Symbol('p3')
p4 = sym.Symbol('p4')
q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q3 = sym.Symbol('q3')
q4 = sym.Symbol('q4')

x = sym.Symbol('x')
y = sym.Symbol('y')
a = sym.Symbol('a')
b = sym.Symbol('b')

R = sym.Symbol('R', constant = True)
S = sym.Symbol('S', constant = True)
T = sym.Symbol('T', constant = True)
P = sym.Symbol('P', constant = True)

D = sym.Matrix(([[x, y], [a, b]]))
D[:,1] = [[1],[1]]

D = sym.Matrix( \
    [ [ p1-1, p2-1, p3, p4],  \
      [ q1-1, q3, q2-1, q4],  \
      [ p1*q1-1, p2*q3, p3*q2, p4*q4 ], \
      [ 1, 1, 1, 1] ]);
D1 = D.copy()
D2 = D.copy()
D3 = D.copy()
D4 = D.copy()

D1[:,0] = [[0],[0],[0],[1]]
D2[:,1] = [[0],[0],[0],[1]]
D3[:,2] = [[0],[0],[0],[1]]
D4[:,3] = [[0],[0],[0],[1]]

v1 = sym.det(D1)/sym.det(D)
v2 = sym.det(D2)/sym.det(D)
v3 = sym.det(D3)/sym.det(D)
v4 = sym.det(D4)/sym.det(D)

up = 3*sym.det(D1) + 5 * sym.det(D2) + 0 * sym.det(D3) + 1 * sym.det(D4)
down = sym.det(D)

diff_up = sym.diff(up,p1)*down - up * sym.diff(down, p1)
diff_down = down**2
print(sym.diff(diff_up,p1))