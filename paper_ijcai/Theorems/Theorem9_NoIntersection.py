"""
    Theorem 9. There is no intersection between extortionate strategy 
        and MisTort strategy.
"""

import z3

q1, q2, q3, q4 = z3.Reals('q1 q2 q3 q4')
R, T, S, P = z3.Reals('R T S P')
# m for \phi, k for \chi
m,k = z3.Reals('m k')

s = z3.Solver()
# one-memory strategy q.
s.add(q1>=0,q1<=1)
s.add(q2>=0,q2<=1)
s.add(q3>=0,q3<=1)
s.add(q4>=0,q4<=1)

# mistort strategy.
s.add(q2 < (q1*(T-P)-(1+q4)*(T-R))/(R-P)) 
s.add(q3 == ((1-q1)*(P-S)+q4*(R-S))/(R-P))   

# extortionate strategy.
s.add(q1 == 1 - m*(k-1)*(R-P)/(P-S))
s.add(q2 == 1 - m*(1 + k*(T-P)/(P-S)))
s.add(q3 == m * (k + (T-P)/(P-S)))
s.add(q4 == 0)

# range of chi and phi
s.add(k>1)
s.add(m>0)
s.add(m<(P-S)/((P-S)+k*(T-P)))

# constraints of IPD.
s.add(T>R, R>P, P>S)
s.add(2*R > T+S) 

print(s.check())