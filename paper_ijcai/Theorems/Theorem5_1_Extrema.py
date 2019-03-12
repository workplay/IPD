"""
    Theorem 5 is proved by three steps.
    1. Calculate all extrema and save it to file.
    2. Make pairwise subtraction.
    3. Prove it with z3.
"""
"""
    In this script, we calculate all extrema. 
                (Same as Theorem4_Equivalent.py).
    And then save the result to './Extrema.xlsx'.
"""


import sympy as sym
import numpy as np
import pandas as pd

# print format vector to string
def sprint(vector):
    return '[' + ', '.join('%1.3f' % v for v in vector) + ']'

q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q3 = sym.Symbol('q3')
q4 = sym.Symbol('q4')

R = sym.Symbol('R', constant = True)
S = sym.Symbol('S', constant = True)
T = sym.Symbol('T', constant = True)
P = sym.Symbol('P', constant = True)

# save to numpy
result_table = np.zeros((16, 2), dtype=object)
index = 0

for p1 in range(2):
    for p2 in range(2):
        for p3 in range(2):
            for p4 in range(2):
                if (p1==1 and p2==1 and p3==0 and p4==0):
                    result_table[index,0] = sprint([p1,p2,p3,p4])
                    result_table[index,1] = '-1'
                    index = index + 1
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
                result_table[index,0] = sprint([p1,p2,p3,p4])
                result_table[index,1] = str(s_X)
                index = index + 1
                
# save to file
df = pd.DataFrame(result_table)
writer = pd.ExcelWriter('./Extrema.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
