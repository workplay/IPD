# -*- coding: utf-8 -*-

# Concrete Values
p1 = 0.9
p4 = 0.1
R = 3
S = 0
T = 5
P = 1


# Equalizer p2 p3
Ep2 = (p1*(T-P)-(1+p4)*(T-R))/(R-P) 
Ep3 = ((1-p1)*(P-S)+p4*(R-S))/(R-P) 

print(Ep2)
print(Ep3)
print("--------------")

p2 = 0.5
p3 = Ep3

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

exprs = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]

for expr in exprs:
    print(expr)