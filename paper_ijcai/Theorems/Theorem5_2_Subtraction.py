"""
    Theorem 5 is proved by three steps.
    1. Calculate all extrema and save it to file.
    2. Make pairwise subtraction.
    3. Prove it with z3.
"""
"""
    In this script, we make pairwise substraction among extreme values.
    And then save the result to Subtraction.xlsx.
    
    To avoid fractions, we use the trick D(p,q,1) < 0,
    so that the denominator can be removed.
"""
import sympy as sym
import numpy as np
import pandas as pd 

q1, q2, q3, q4 = sym.symbols('q1 q2 q3 q4')
R, T, S, P = sym.symbols('R T S P')

# load expression of extremums
df = pd.read_excel('./Extrema.xlsx', sheet_name='Sheet1')
exprs = []
for i in range(df.shape[0]):
    exprs = exprs + [eval(df.iat[i,1])]

symbolic_table = np.zeros((len(exprs), len(exprs)), dtype=object)

# iterate all possible pairs
for i in range(len(exprs)):
    for j in range(i+1,len(exprs)):
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
                        value = denominator.evalf(subs={q1: i1,q2: i2,q3: i3,q4: i4})
                        # print(value)
                        if ((value > 0.0001) and ('+' not in signs)):
                            signs = signs + ['+']
                        elif (value < -0.0001) and ('-' not in signs):
                            signs = signs + ['-']
        if (signs[0] == '+'):
            result = numerator
        elif (signs[0] == '-'):
            result = -numerator
        symbolic_table[i][j] = result
        symbolic_table[j][i] = -result

# save to file
df = pd.DataFrame(symbolic_table)
writer = pd.ExcelWriter('./Subtraction.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
