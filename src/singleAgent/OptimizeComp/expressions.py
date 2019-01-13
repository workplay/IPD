# -*- coding: utf-8 -*-
import sympy as sym

p1, p2, p3, p4 = sym.symbols('p1 p2 p3 p4')
R, T, S, P = sym.symbols('R T S P')

f0 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f1 =  (-P*p2 + P - R*p2*p4 + R*p4 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p4 - T*p3*p4 + T*p3)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
f2 =  (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p4 + S*p2*p4 - S*p4 - T*p4)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
f3 =  (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p3 + R*p3*p4 - R*p4 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p4 + T*p3*p4 - T*p3)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
# f4 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f5 =  (-P*p2*p3 + P*p3 - R*p2*p3 + R*p3 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
f6 =  (P*p1*p3 - P*p3 - R*p3*p4 + S*p2*p4 - S*p4 - T*p3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
f7 =  (P*p1*p3 - P*p3 - R*p3 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
# f8 =  (P*p2 - P - T*p4)/(p2 - p4 - 1)
f9 =  (P*p1*p2 - P*p1 - P*p2 + P - R*p2*p4 + R*p4 + S*p1*p2 - S*p1 - S*p2 + S - T*p1*p3 + T*p3)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
f10 =  (P*p1*p3 - P*p1 - P*p3 + P + R*p2*p4 - S*p1*p4 + S*p4 - T*p1*p4 + T*p4)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
f11 =  -(P*p1*p3 - P*p1 - P*p3 + P + R*p2*p3 - R*p3*p4 + R*p4 - S*p1 + S - T*p1*p3 + T*p3)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
# f12 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
# f13 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
# f14 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
f15 =  (-R*p3 + S*p1 - S)/(p1 - p3 - 1)

exprs = [f0, f1, f2, f3, f5, f6, f7, f9, f10, f11, f15]
result = s.check()
        if result == z3.sat:
            print(i,"sat")
            print(s.model())
        elif result == z3.unsat:
            print(i,"unsat")
        elif result == z3.unknown:
            print(i,"unknown")
        else:
            print("error check result")
        s.pop()
