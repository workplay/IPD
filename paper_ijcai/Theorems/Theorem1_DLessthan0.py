"""
    Theorem 1: 
        Assume 0 <= pi <= 1 and that 0 < qi < 1, 
        and p != (1,1,0,0).
        Then D(p,q,1) < 0.
        
    The program output all extreme values and unsat.
"""

import z3
import sympy as sym

def checkDeterminant(det_D_1):
    print(det_D_1)
    """
        z3 symbol declaration.
    """
    p1, p2, p3, p4 = z3.Reals('p1 p2 p3 p4')
    q1, q2, q3, q4 = z3.Reals('q1 q2 q3 q4')
    """
        solve with refutation.
           f >= 0 ?  If no, then we get f<0.
    """
    s = z3.Solver()
    # s.add(p1>=0,p1<1)
    # s.add(p2>=0,p2<1)
    s.add(p3>0,p3<=1)
    # s.add(p4>0,p4<=1)
    s.add(q1>0,q1<1)
    s.add(q2>0,q2<1)
    s.add(q3>0,q3<1)
    s.add(q4>0,q4<1)
    f = eval(det_D_1)
    s.add(f >= 0)
    result = s.check()
    print(result)

# calculate limitations of determinant
# Due to complexity, we cannot directly check D<=0
# According to monotocity, we check extremums.
def getLimit():
    """
        Symbol declaration.
    """
    p1 = sym.Symbol('p1')
    p2 = sym.Symbol('p2')
    p3 = sym.Symbol('p3')
    p4 = sym.Symbol('p4')
    q1 = sym.Symbol('q1')
    q2 = sym.Symbol('q2')
    q3 = sym.Symbol('q3')
    q4 = sym.Symbol('q4') 
    

    """
        Get all expressions of extrema.
        Let p1, p2, p4 be 0 or 1.
        Then check whether it can be 0 or not.
        
        In this example we assume 0<p3<1, 
        we can also assume p1, p2, p4 in the same way.
    """
    for p1 in range(2):
        for p2 in range(2):
            #   for i3 in range(2):
            for p4 in range(2):
                D_1 = sym.Matrix( \
                    [[p1*q1-1, p1-1, q1-1, 1],   \
                     [p2*q3, p2-1, q3, 1], \
                     [p3*q2, p3, q2-1, 1], \
                     [p4*q4, p4, q4, 1] ])    
                det_D_1 = str(sym.det(D_1))
                """
                    Check whether a extreme value can be 0 with z3.
                """
                checkDeterminant(str(det_D_1))
                
def main():
    getLimit()
        
if __name__== "__main__":
    main()

