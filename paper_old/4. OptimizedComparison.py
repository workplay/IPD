# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import pandas as pd 

p1, p2, p3, p4 = sym.symbols('p1 p2 p3 p4')
R, T, S, P = sym.symbols('R T S P')

# load expression of extremums
df = pd.read_excel('./data/Extremums.xlsx', sheet_name='Sheet1')
exprs = []
for i in range(df.shape[0]):
    exprs = exprs + [eval(df.iat[i,1])]

symbolic_table = np.zeros((len(exprs), len(exprs)), dtype=object)

# iterate all possible pairs
for i in range(len(exprs)):
    for j in range(i+1,len(exprs)):
        # print(i,j)
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
        # print(signs, denominator)
        # separate
        # result = sym.separatevars(result)
        symbolic_table[i][j] = result
        symbolic_table[j][i] = -result

# save to file
df = pd.DataFrame(symbolic_table)
writer = pd.ExcelWriter('./data/SymbolicSubstraction.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
