# -*- coding: utf-8 -*-
from z3 import *

x = Int('x')
y = Int('y')

s = Solver()
print(s)

s.add(x > 10, y == x + 2)
print(s)
print("Solving constraints in the solver s ...")
print(s.check())
print(s.model())

print("Create a new scope...")
s.push()
s.add(y < 11)
print(s)
print("Solving updated set of constraints...")
print(s.check())

print("Restoring state...")
s.pop()
print(s)
print("Solving restored set of constraints...")
print(s.check())

#  Recall that Z3 can solve nonlinear polynomial constraints, 
#  but 2**x is not a polynomial.
x = Real('x')
s = Solver()
s.add(2**x == 3)
print(s.check())

print('--------------------')
x = Real('x')
y = Real('y')
s = Solver()
s.add(x > 1, y > 1, Or(x + y > 3, x - y < 2))
print("asserted constraints...")
for c in s.assertions():
    print(c)

print(s.check())
print("statistics for the last check method...")
# print(s.statistics())
# Traversing statistics
# for k, v in s.statistics():
#    print("%s : %s" % (k, v))


print('--------------------')
x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
print(s.check())

print(s.model())
m = s.model()
print("x = %s" % m[x])

print("traversing model...")
for d in m.decls():
    print("%s = %s" % (d.name(), m[d]))

print('--------------------')
x, y, z = Reals('x y z')
solver = Solver()
f1 = x > 1
f2 = x < 2
solver.add(f1,f2)
print(solver.check())
print(solver.model())
print(solver)

