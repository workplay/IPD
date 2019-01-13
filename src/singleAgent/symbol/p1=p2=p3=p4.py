# -*- coding: utf-8 -*-
import sympy as sym
p = sym.Symbol('p')
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

D = sym.Matrix( \
    [ [ p-1, p-1, p, p],  \
      [ q1-1, q3, q2-1, q4],  \
      [ p*q1-1, p*q3, p*q2, p*q4 ], \
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

up = R*sym.det(D1) + T * sym.det(D2) + S * sym.det(D3) + P * sym.det(D4)
down = sym.det(D)
result = up/down

NumToSign = {1:'-',0:'+'}

for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                sy = result
                sy = sym.limit(sy,q1,i1,NumToSign[i1])
                sy = sym.limit(sy,q2,i2,NumToSign[i2])
                sy = sym.limit(sy,q3,i3,NumToSign[i3])
                sy = sym.limit(sy,q4,i4,NumToSign[i4])
                # print(i1,i2,i3,i4,':',sy,':',sy.subs(R,3).subs(T,5).subs(P,1).subs(S,0),":" "%.3f" % sy.subs(R,3).subs(T,5).subs(P,1).subs(S,0).subs(p,0.5))
                print(sy)
