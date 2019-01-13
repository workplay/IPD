# -*- coding: utf-8 -*-
from StationaryVector import sVector_cal
import numpy as np

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

def avePayoff_cal(p,q):
    sVector = sVector_cal(p,q)
    payoff_p = np.dot(sVector,[3,0,5,1])
    payoff_q = np.dot(sVector,[3,5,0,1])
    return [payoff_p, payoff_q]

def main():
    print(avePayoff_cal([0.9, 0.5, 0.2, 0.1],[0.9, 0.5, 0.2, 0.1]))
  
if __name__== "__main__":
    main()
