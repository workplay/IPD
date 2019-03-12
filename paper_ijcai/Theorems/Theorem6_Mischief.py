"""
    Theorem 6. Every pure strategy response to Mischief strategy 
    receives the same average payoff.

    We write all values in Extrema.xlsx to F, and solve it with z3.
"""

import z3

q1, q2, q3, q4 = z3.Reals('q1 q2 q3 q4')
R, T, S, P = z3.Reals('R T S P')

F0 = (-P*q2 + P + T*q4)/(-q2 + q4 + 1)
F1 = (-P*q2 + P - R*q2*q4 + R*q4 + S*q2*q4 - S*q2 - S*q4 + S + T*q1*q4 - T*q3*q4 + T*q3)/(q1*q4 - 2*q2 - q3*q4 + q3 + 2)
F2 = (-P*q1*q2 + P*q2*q3 - P*q3 + P + R*q2*q4 - S*q2*q4 + S*q4 + T*q4)/(-q1*q2 + q2*q3 - q3 + 2*q4 + 1)
F3 = (-P*q1*q2 + P*q2*q3 - P*q3 + P + R*q2*q3 - R*q3*q4 + R*q4 - S*q1*q2 + S*q1*q4 - S*q4 + S + T*q1*q4 - T*q3*q4 + T*q3)/(2*(-q1*q2 + q1*q4 + q2*q3 - q3*q4 + 1))
F4 = (-P*q2 + P + T*q4)/(-q2 + q4 + 1)
F5 = (-P*q2*q3 + P*q3 - R*q2*q3 + R*q3 + S*q2*q4 - S*q2 - S*q4 + S + T*q1*q3)/(q1*q3 - 2*q2*q3 + q2*q4 - q2 + 2*q3 - q4 + 1)
F6 = (-P*q1*q3 + P*q3 + R*q3*q4 - S*q2*q4 + S*q4 + T*q3*q4)/(-q1*q3 - q2*q4 + 2*q3*q4 + q3 + q4)
F7 = (-P*q1*q3 + P*q3 + R*q3 - S*q1*q2 + S*q1*q4 - S*q4 + S + T*q1*q3)/(-q1*q2 + q1*q4 + 2*q3 - q4 + 1)
F8 = (P*q2 - P - T*q4)/(q2 - q4 - 1)
F9 = (P*q1*q2 - P*q1 - P*q2 + P - R*q2*q4 + R*q4 + S*q1*q2 - S*q1 - S*q2 + S - T*q1*q3 + T*q3)/(2*q1*q2 - q1*q3 - 2*q1 - q2*q4 - 2*q2 + q3 + q4 + 2)
F10 = (P*q1*q3 - P*q1 - P*q3 + P + R*q2*q4 - S*q1*q4 + S*q4 - T*q1*q4 + T*q4)/(q1*q3 - 2*q1*q4 - q1 + q2*q4 - q3 + 2*q4 + 1)
F11 = (P*q1*q3 - P*q1 - P*q3 + P + R*q2*q3 - R*q3*q4 + R*q4 - S*q1 + S - T*q1*q3 + T*q3)/(-2*q1 + q2*q3 - q3*q4 + q4 + 2)
F12 = -1
F13 = (-R*q3 + S*q1 - S)/(q1 - q3 - 1)
F14 = (R*q3 - S*q1 + S)/(-q1 + q3 + 1)
F15 = (R*q3 - S*q1 + S)/(-q1 + q3 + 1)

F = [F0,F1,F2,F3,F5,F6,F7,F9,F10,F11,F15]

for expr1 in F:
    for expr2 in F:
        s = z3.Solver()
        s.set("timeout",60000)
        s.add(T>R, R>P, P>S)
        s.add(2*R > T+S)
        s.add(q1>0,q1<1)
        s.add(q2>0,q2<1)
        s.add(q3>0,q3<1)
        s.add(q4>0,q4<1)
        s.add(q2 == (q1*(T-P)-(1+q4)*(T-R))/(R-P)) 
        s.add(q3 == ((1-q1)*(P-S)+q4*(R-S))/(R-P))    
        s.add(expr1 != expr2)
        print(s.check())