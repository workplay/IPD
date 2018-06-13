# -*- coding: utf-8 -*-
# This file difines the pipeline to calculate a concrete example
#    1. Substitute [R,S,T,P] in general examples and get specific value.
#    2. Save the values to file
#    3. (Optional) Solve expressions according to these values.
import sympy as sym
from z3 import *
import pandas as pd
import numpy as np

_R = 3
_S = 0
_T = 5
_P = 1


p1 = sym.Symbol('p1')
p2 = sym.Symbol('p2')
p3 = sym.Symbol('p3')
p4 = sym.Symbol('p4')
R = sym.Symbol('R', constant = True)
S = sym.Symbol('S', constant = True)
T = sym.Symbol('T', constant = True)
P = sym.Symbol('P', constant = True)

df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
concrete_table = np.zeros((df.shape[0], df.shape[0]), dtype=object)

for i in range(0, df.shape[0]):
    for j in range(0,df.shape[0]):
        if (df.iat[i,j] == 0):
            continue
        f = eval(df.iat[i,j])
        if (f==0):
            continue
        result = f.subs([(R, _R), (S, _S), (T, _T), (P,_P)])
        concrete_table[i,j] = result
df_result = pd.DataFrame(concrete_table)
filename = "ConcreteSubstraction_%.0f%.0f%.0f%.0f.xlsx" %(_R,_S,_T,_P)
writer = pd.ExcelWriter(filename)
df_result.to_excel(writer,'Sheet1')
writer.save()