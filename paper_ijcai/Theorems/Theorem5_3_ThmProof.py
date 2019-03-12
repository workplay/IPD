"""
    Theorem 5 is proved by three steps.
    1. Calculate all extrema and save it to file.
    2. Make pairwise subtraction.
    3. Prove it with z3.
"""
"""
    In this script, we prove Theorem 5 with z3.
    Refer README.md to install z3.
    We show that 
    F0 > Fi, i \in {0,1,2,3,5,6,7,9,10,11,15}
"""

import z3
import pandas as pd
import time

start_time = time.time()


q1, q2, q3, q4 = z3.Reals('q1 q2 q3 q4')
R, T, S, P = z3.Reals('R T S P')

 
df = pd.read_excel('./Subtraction.xlsx', sheet_name='Sheet1')
 
s = z3.Solver()

# constraints in IPD
s.add(T>R, R>P, P>S)
s.add(2*R > T+S)  
s.add(q1>0,q1<1)
s.add(q2>0,q2<1)
s.add(q3>0,q3<1)
s.add(q4>0,q4<1)
# constraints in thm5
s.add(q2 >= q4)
s.add(q4 >= q1)
s.add(q1 >= q3)

index = [0,1,2,3,5,6,7,9,10,11,15]

for i in index:
    if (i==0):
        continue;
    s.push()
    f = eval(df.iat[0,i])
    s.add(f <= 0)
    result = s.check()
    if result == z3.sat:
        print(i,"sat")
    elif result == z3.unsat:
        print(i,"unsat")
    elif result == z3.unknown:
        print(i,"unknown")
    else:
        print("error check result")
    s.pop()
    
print("--- %s seconds ---" % (time.time() - start_time))