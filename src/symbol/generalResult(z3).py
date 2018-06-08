# -*- coding: utf-8 -*-
from z3 import *
q1, q2, q3, q4 = Reals('q1 q2 q3 q4')
p1, p2, p3, p4 = Real('p1 p2 p3 p4')
R, T, S, P = Reals('R T S P')


0 0 0 0 : (P*p2 - P - T*p4)/(p2 - p4 - 1)
0 0 0 1 : (-P*p2 + P - R*p2*p4 + R*p4 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p4 - T*p3*p4 + T*p3)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
0 0 1 0 : (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p4 + S*p2*p4 - S*p4 - T*p4)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
0 0 1 1 : (P*p1*p2 - P*p2*p3 + P*p3 - P - R*p2*p3 + R*p3*p4 - R*p4 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p4 + T*p3*p4 - T*p3)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
0 1 0 0 : (P*p2 - P - T*p4)/(p2 - p4 - 1)
0 1 0 1 : (-P*p2*p3 + P*p3 - R*p2*p3 + R*p3 + S*p2*p4 - S*p2 - S*p4 + S + T*p1*p3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
0 1 1 0 : (P*p1*p3 - P*p3 - R*p3*p4 + S*p2*p4 - S*p4 - T*p3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
0 1 1 1 : (P*p1*p3 - P*p3 - R*p3 + S*p1*p2 - S*p1*p4 + S*p4 - S - T*p1*p3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
1 0 0 0 : (P*p2 - P - T*p4)/(p2 - p4 - 1)
1 0 0 1 : (P*p1*p2 - P*p1 - P*p2 + P - R*p2*p4 + R*p4 + S*p1*p2 - S*p1 - S*p2 + S - T*p1*p3 + T*p3)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
1 0 1 0 : (P*p1*p3 - P*p1 - P*p3 + P + R*p2*p4 - S*p1*p4 + S*p4 - T*p1*p4 + T*p4)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
1 0 1 1 : -(P*p1*p3 - P*p1 - P*p3 + P + R*p2*p3 - R*p3*p4 + R*p4 - S*p1 + S - T*p1*p3 + T*p3)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
1 1 0 0 : (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
1 1 0 1 : (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
1 1 1 0 : (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
1 1 1 1 : (-R*p3 + S*p1 - S)/(p1 - p3 - 1)
