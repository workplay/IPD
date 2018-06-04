# -*- coding: utf-8 -*-
from StationaryVector import sVector_cal
import numpy as np

def avePayoff_cal(p,q):
    sVector = sVector_cal(p,q)
    payoff_p = np.dot(sVector,[3,0,5,1])
    payoff_q = np.dot(sVector,[3,5,0,1])
    return [payoff_p, payoff_q]

def main():
    print(avePayoff_cal([0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5]))
  
if __name__== "__main__":
    main()
