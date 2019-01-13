# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def calStationaryVector(p,q):
    [p1,p2,p3,p4] = p
    [q1,q2,q3,q4] = q
    D = sym.Matrix( \
                   [ [ p1-1, p2-1, p3, p4],  \
                    [ q1-1, q3, q2-1, q4],  \
                    [ p1*q1-1, p2*q3, p3*q2, p4*q4 ], \
                    [ 1, 1, 1, 1] ]);
    D1 = D.copy()
    D2 = D.copy()
    D3 = D.copy()
    D4 = D.copy()
    D1[:,0] = [[0],[0],[0],[1]]
    D2[:,1] = [[0],[0],[0],[1]]
    D3[:,2] = [[0],[0],[0],[1]]
    D4[:,3] = [[0],[0],[0],[1]]
    v1 = sym.det(D1)/sym.det(D)
    v2 = sym.det(D2)/sym.det(D)
    v3 = sym.det(D3)/sym.det(D)
    v4 = sym.det(D4)/sym.det(D)
    return [v1,v2,v3,v4]

# two float number are equal give precision
def equals(a,b,precision=0.001):
    return(abs(a-b) < precision)


# generate possible strategies of q with increment of 0.1
def candvector():
    epsilon = 0.001
    vector = []
    for v in range(0,11):
        v = v/10.0
        if (equals(v, 0.0)):
            v = v + epsilon
        if (equals(v, 1.0)):
            v = v - epsilon
        vector = vector + [v]
    return vector    

# calculate best response to strategy p
def allstationary(p):
    result = []
    # candidates = candvector()
    candidates = [0.001, 0.5, 0.999]
    for q1 in candidates:
        for q2 in candidates:
            for q3 in candidates:
                for q4 in candidates:
                    q=[q1,q2,q3,q4]
                    # print(calStationaryVector(p,q))
                    result = result + [calStationaryVector(p,q)]
    return result

def printgraph(result):
        # print(result)
    result = np.array(result)
    result = result[:,[0,2]]
    hull = ConvexHull(result)
    # print(hull)
    plt.xlabel("$v_1$")
    plt.ylabel("$v_3$")
    plt.axis([0, 1, 0, 1])
    plt.plot(result[:,0], result[:,1], 'b.')
    plt.plot([0,1])
    for simplex in hull.simplices:
        lines = plt.plot(result[simplex, 0], result[simplex, 1], 'r-', linewidth = 4)
    plt.legend()
    plt.show()

def main():
    p = [0.3,0.7,0.8,0.8]
    result = allstationary(p)
    printgraph(result)
    # print(result)
    
if __name__== "__main__":
    main()