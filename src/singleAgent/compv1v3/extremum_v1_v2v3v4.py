# -*- coding: utf-8 -*-
"""
   conclusion:
       play repeat.
"""

import sympy as sym
import numpy as np
import pandas as pd 

p1, p2, p3, p4 = sym.symbols('p1 p2 p3 p4')
# q1, q2, q3, q4 = sym.symbols('q1 q2 q3 q4')


for q1 in range(2):
    for q2 in range(2):
        for q3 in range(2):
            for q4 in range(2):
                D = sym.Matrix( [ [ p1-1, p2-1, p3, p4], [ q1-1, q3, q2-1, q4],  [ p1*q1-1, p2*q3, p3*q2, p4*q4 ], [ 1, 1, 1, 1] ]);
                D1 = D.copy()
                D2 = D.copy()
                D3 = D.copy()
                D4 = D.copy()
                D1[:,0] = [[0],[0],[0],[1]]
                D2[:,1] = [[0],[0],[0],[1]]
                D3[:,2] = [[0],[0],[0],[1]]
                D4[:,3] = [[0],[0],[0],[1]]
                sub = - sym.det(D1) + sym.det(D3) + sym.det(D2) + sym.det(D4)
                sub = sym.simplify(sub)
                print([q1,q2,q3,q4],sub)