# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import pandas as pd

# Definition
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

# Symbolic calculation of s_Y
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

s_Y = up/down

# save to numpy
result_table = np.zeros((16, 2), dtype=object)
index = 0

# print format vector to string
def sprint(vector):
    return '[' + ', '.join('%1.3f' % v for v in vector) + ']'

# calculate limits
NumToSign = {1:'-',0:'+'}
for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                sy = s_Y
                sy = sym.limit(sy,q1,i1,NumToSign[i1])
                sy = sym.limit(sy,q2,i2,NumToSign[i2])
                sy = sym.limit(sy,q3,i3,NumToSign[i3])
                sy = sym.limit(sy,q4,i4,NumToSign[i4])
                
                print(i1,i2,i3,i4,':',sy)
                result_table[index,0] = sprint([i1,i2,i3,i4])
                result_table[index,1] = str(sy)
                index = index + 1
                # print(sy)
                # print("%.3f" % sy.subs(R,3).subs(T,5).subs(P,1).subs(S,0).subs(p1,0.5).subs(p2,0.5).subs(p3,0.5).subs(p4,0.5))

# save to file
df = pd.DataFrame(result_table)
writer = pd.ExcelWriter('./data/Extremums.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
