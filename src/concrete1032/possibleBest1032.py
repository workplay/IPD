from z3 import *

p1, p2, p3, p4 = z3.Reals('p1 p2 p3 p4')

f0  = -(2*p2 - 2)/(p2 - p4 - 1)
f1  = -(2*p2*p4 - 5*p2 - 2*p4 + 5)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
f2  = -(2*p1*p2 - 2*p2*p3 + 2*p2*p4 + 2*p3 - 3*p4 - 2)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
f3  = -(5*p1*p2 - 3*p1*p4 - 3*p2*p3 + p3*p4 + 2*p3 + 2*p4 - 5)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
# f4  = -(2*p2 - 2)/(p2 - p4 - 1)
f5  = (3*p2*p3 - 3*p2*p4 + 3*p2 - 3*p3 + 3*p4 - 3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
f6  = -(2*p1*p3 + 3*p2*p4 - p3*p4 - 2*p3 - 3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
f7  = -(3*p1*p2 + 2*p1*p3 - 3*p1*p4 - 3*p3 + 3*p4 - 3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
# f8  = -(2*p2 - 2)/(p2 - p4 - 1)
f9  = -(5*p1*p2 - 5*p1 - p2*p4 - 5*p2 + p4 + 5)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
f10 = -(2*p1*p3 - 3*p1*p4 - 2*p1 + p2*p4 - 2*p3 + 3*p4 + 2)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
f11 = (2*p1*p3 - 5*p1 + p2*p3 - p3*p4 - 2*p3 + p4 + 5)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
# f12 = -(3*p1 - p3 - 3)/(p1 - p3 - 1)
# f13 = -(3*p1 - p3 - 3)/(p1 - p3 - 1)
# f14 = -(3*p1 - p3 - 3)/(p1 - p3 - 1)
f15 = -(3*p1 - p3 - 3)/(p1 - p3 - 1)


exprs = [f0, f1, f2, f3, f5, f6, f7, f9, f10, f11, f15]

s = z3.Solver()
s.set('timeout', 1200000) # 20 minutes

s.add(p1>0,p1<1)
s.add(p2>0,p2<1)
s.add(p3>0,p3<1)
s.add(p4>0,p4<1)

# pairwise comparison
for i in range(len(exprs)):
    s.push()
    for j in range(len(exprs)):
        s.add(exprs[i] >= exprs[j])
    result = s.check()
    if result == z3.sat:
        print(i,"sat")
        print(s.model())
    elif result == z3.unsat:
        print(i,"unsat")
    elif result == z3.unknown:
        print(i,"unknown")
    else:
        print(i,"error")
    s.pop()
