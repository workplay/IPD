# -*- coding: utf-8 -*-
from z3 import *
import sympy as sym

# check D1>=0 is satisfiable.
def checkDeterminant(det_D_1):
    print(det_D_1)
    p1, p2, p3, p4 = z3.Reals('p1 p2 p3 p4')
    q1, q2, q3, q4 = z3.Reals('q1 q2 q3 q4')
    s = z3.Solver()
    s.add(p1>=0,p1<1)
    s.add(p2>=0,p2<1)
    s.add(p3>0,p3<=1)
    s.add(p4>0,p4<=1)
    s.add(q1>0,q1<1)
    s.add(q2>0,q2<1)
    s.add(q3>0,q3<1)
    s.add(q4>0,q4<1)
    f = eval(det_D_1)
    s.add(f >= 0)
    result = s.check()
    print(result)

# calculate limitations of determinant
# Due to complexity, we cannot directly check D<=0
# According to monotocity, we check extremums.
def getLimit():
    p1 = sym.Symbol('p1')
    p2 = sym.Symbol('p2')
    p3 = sym.Symbol('p3')
    p4 = sym.Symbol('p4')
    q1 = sym.Symbol('q1')
    q2 = sym.Symbol('q2')
    q3 = sym.Symbol('q3')
    q4 = sym.Symbol('q4')    
    D_1 = sym.Matrix( \
       [ [p1*q1-1, p1-1, q1-1, 1],   \
        [p2*q3, p2-1, q3, 1], \
        [p3*q2, p3, q2-1, 1], \
        [p4*q4, p4, q4, 1] ])    
    det_D_1 = str(sym.det(D_1))    
    NumToSign = {1:'-',0:'+'}    
    for i1 in range(2):
        for i2 in range(2):
#   for i3 in range(2):
            for i4 in range(2):
                sy = det_D_1
                sy = sym.limit(sy,p1,i1,NumToSign[i1])
                sy = sym.limit(sy,p2,i2,NumToSign[i2])
#               sy = sym.limit(sy,q3,i3,NumToSign[i3])
                sy = sym.limit(sy,p4,i4,NumToSign[i4])
                #print(i1,i2,i4,':',sy)      
                checkDeterminant(str(sy))
                
def main():
    getLimit()
        
if __name__== "__main__":
    main()

