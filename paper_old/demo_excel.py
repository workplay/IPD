import sympy as sym
x = sym.Symbol('x')
y = x * sym.sin(x) + 2*x + 3
print(sym.diff(y,x))

