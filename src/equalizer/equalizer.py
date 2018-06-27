# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import pandas as pd 

p1, p4 = sym.symbols('p1 p4')
R, T, S, P = sym.symbols('R T S P')
# p2, p3 = sym.symbols('p2 p3')
p2 = (p1*(T-P)-(1+p4)*(T-R))/(R-P) 
p3 = ((1-p1)*(P-S)+p4*(R-S))/(R-P)

print(p2+p3)

# load expression of extremums
# df = pd.read_excel('Extremums.xlsx', sheet_name='Sheet1')
# exprs = []
# for i in range(df.shape[0]):
#     exprs = exprs + [eval(df.iat[i,1])]   
# for f in exprs:
#     print(sym.simplify(f))  


df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
for i in range(df.shape[0]):
    for j in range(df.shape[0]):
        if df.iat[i,j] == 0:
            print(i,j,0)
            continue
        f = eval(df.iat[i,j])
        print(i,j,sym.simplify(f))