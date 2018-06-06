# -*- coding: utf-8 -*-
from z3 import *

print("Tutorial 1")
x = Int('x')
y = Int('y')
n = x + y >= 3
print("num args: ", n.num_args())
print("children: ", n.children())
print("1st child:", n.arg(0))
print("2nd child:", n.arg(1))
print("operator: ", n.decl())
print("op name:  ", n.decl().name())

print("Tutorial 2")
x = Real('x')
y = Real('y')
solve(x**2 + y**2 > 3, x**3 + y < 5)

print("Tutorial 3")
x = Real('x')
y = Real('y')
solve(x**2 + y**2 == 3, x**3 == 2)
set_option(precision=30)
print("Solving, and displaying result with 30 decimal places")
solve(x**2 + y**2 == 3, x**3 == 2)
solve(x+y==2)

print("Tutorial 4")
print(1/3)  #python 0.333333
print(RealVal(1)/3)  # z3, 1/3
print(Q(1,3))        # z3, 1/3

x = Real('x')
print(x + 1/3)          # python, x+0.333333 
print(x + Q(1,3))       # z3, x+1/3
print(x + "1/3")        # z3, x+1/3
print(x + 0.25)         # x + 1/4

print("Tutorial 5")
x = Real('x')
solve(3*x == 1)

set_option(rational_to_decimal=True)
solve(3*x == 1)

set_option(precision=3)
solve(3*x == 1)

print("Tutorial 6")
x = Real('x')
solve(x > 4, x < 0)
