# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import pandas as pd 

p1, p2, p3, p4 = sym.symbols('p1 p2 p3 p4')
R, T, S, P = sym.symbols('R T S P')

f0 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f1 =  (-P*p2 + P - R*p2*p4 + R*p4 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p4 - T*p3*p4 + T*p3)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
f2 =  (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p4 + S*p2*p4 - S*p4 - T*p4)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
f3 =  (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p3 + R*p3*p4 - R*p4 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p4 + T*p3*p4 - T*p3)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
f4 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f5 =  (-P*p2*p3 + P*p3 - R*p2*p3 + R*p3 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
f6 =  (P*p1*p3 - P*p3 - R*p3*p4 + S*p2*p4 - S*p4 - T*p3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
f7 =  (P*p1*p3 - P*p3 - R*p3 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
f8 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f9 =  (P*p1*p2 - P*p1 - P*p2 + P - R*p2*p4 + R*p4 + S*p1*p2 - S*p1 - S*p2 + S - T*p1*p3 + T*p3)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
f10 =  (P*p1*p3 - P*p1 - P*p3 + P + R*p2*p4 - S*p1*p4 + S*p4 - T*p1*p4 + T*p4)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
f11 =  -(P*p1*p3 - P*p1 - P*p3 + P + R*p2*p3 - R*p3*p4 + R*p4 - S*p1 + S - T*p1*p3 + T*p3)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
f12 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f13 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f14 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f15 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)

exprs = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

symbolic_table = np.zeros((len(exprs), len(exprs)), dtype=object)
# iterate all possible pairs
for i in range(len(exprs)):
    for j in range(i+1,len(exprs)):
        print(i,j)
        # make subtraction between pairs
        f_prev = exprs[i]
        f_succ = exprs[j]
        subtraction = f_prev - f_succ
        # reduction of fractions to a common denominator
        frac = sym.fraction(sym.together(subtraction))
        numerator = frac[0]
        numerator = numerator.expand(basic=True)
        denominator = frac[1]
        # get signs of denominator
        signs = []
        for i1 in range(2):
            for i2 in range(2):
                for i3 in range(2):
                    for i4 in range(2):
                        value = denominator.evalf(subs={p1: i1,p2: i2,p3: i3,p4: i4})
                        # print(value)
                        if ((value > 0.0001) and ('+' not in signs)):
                            signs = signs + ['+']
                        elif (value < -0.0001) and ('-' not in signs):
                            signs = signs + ['-']
                        #print(i1,i2,i3,i4,"%1.3f" % value)  
        if (signs[0] == '+'):
            result = numerator
        elif (signs[0] == '-'):
            result = -numerator
        # separate
        # result = sym.separatevars(result)
        symbolic_table[i][j] = result
        symbolic_table[j][i] = -result
df = pd.DataFrame(symbolic_table)
writer = pd.ExcelWriter('SymbolicSubstraction.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
# comp_0_3 = f0 - f3
# print(sym.together(comp_0_3))
# print('--------------------')
# comp_0_3 = (-(p2 - p4 - 1)*(P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p3 + R*p3*p4 - R*p4 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p4 + T*p3*p4 - T*p3) + 2*(P*p2 - P - T*p4)*(p1*p2 - p1*p4 - p2*p3 + p3*p4 - 1))/(2*(p2 - p4 - 1)*(p1*p2 - p1*p4 - p2*p3 + p3*p4 - 1))
# frac = sym.fraction(comp_0_3)
# numerator = frac[0]
# denominator = frac[1]
# print('--------------------')
# print(numerator)
# print(denominator)
# expr = p1*p4 - 2*p2 - p3*p4 + p3 + 2

# for i1 in range(2):
#     for i2 in range(2):
#         for i3 in range(2):
#             for i4 in range(2):
#                 value = expr.evalf(subs={p1: i1,p2: i2,p3: i3,p4: i4})
#                 print(i1,i2,i3,i4,"%1.3f" % value)
    
# result = (-(p2 - p4 - 1)*(-P*p2 + P - R*p2*p4 + R*p4 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p4 - T*p3*p4 + T*p3) + (P*p2 - P - T*p4)*(p1*p4 - 2*p2 - p3*p4 + p3 + 2))/((p2 - p4 - 1)*(p1*p4 - 2*p2 - p3*p4 + p3 + 2))

# comp_0_1 = (-(p2 - p4 - 1)*(-P*p2 + P - R*p2*p4 + R*p4 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p4 - T*p3*p4 + T*p3) + (P*p2 - P - T*p4)*(p1*p4 - 2*p2 - p3*p4 + p3 + 2))

# denominator is negative
# comp_0_1 = - comp_0_1
# comp_0_1 = sym.separatevars(comp_0_1)
# print(comp_0_1)
# comp_0_1 = (P*p1*p4 - P*p2 - P*p3*p4 + P*p3 - P*p4 + P + R*p2*p4 - R*p4**2 - R*p4 - S*p2*p4 + S*p2 + S*p4**2 - S - T*p1*p4 + T*p3*p4 - T*p3 + 2*T*p4)
# comp_0_1 = sym.simplify(comp_0_1)
# print(comp_0_1)

# value = comp_0_1.subs(R,-1).subs(S, -3).subs(T,0).subs(P,-2)
# print(value)


