# -*- coding: utf-8 -*-
import sympy as sym
import sys

def bestResponse(p1,p2,p3,p4):
    f0   =  -(2*p2 - 2)/(p2 - p4 - 1)
    f1   =  -(2*p2*p4 - 5*p2 - 2*p4 + 5)/(p1*p4 - 2*p2 - p3*p4 + p3 + 2)
    f2   =  -(2*p1*p2 - 2*p2*p3 + 2*p2*p4 + 2*p3 - 3*p4 - 2)/(p1*p2 - p2*p3 + p3 - 2*p4 - 1)
    f3   =  -(5*p1*p2 - 3*p1*p4 - 3*p2*p3 + p3*p4 + 2*p3 + 2*p4 - 5)/(2*p1*p2 - 2*p1*p4 - 2*p2*p3 + 2*p3*p4 - 2)
    f4   =  -(2*p2 - 2)/(p2 - p4 - 1)
    f5   =  (3*p2*p3 - 3*p2*p4 + 3*p2 - 3*p3 + 3*p4 - 3)/(p1*p3 - 2*p2*p3 + p2*p4 - p2 + 2*p3 - p4 + 1)
    f6   =  -(2*p1*p3 + 3*p2*p4 - p3*p4 - 2*p3 - 3*p4)/(p1*p3 + p2*p4 - 2*p3*p4 - p3 - p4)
    f7   =  -(3*p1*p2 + 2*p1*p3 - 3*p1*p4 - 3*p3 + 3*p4 - 3)/(p1*p2 - p1*p4 - 2*p3 + p4 - 1)
    f8   =  -(2*p2 - 2)/(p2 - p4 - 1)
    f9   =  -(5*p1*p2 - 5*p1 - p2*p4 - 5*p2 + p4 + 5)/(2*p1*p2 - p1*p3 - 2*p1 - p2*p4 - 2*p2 + p3 + p4 + 2)
    f10   =  -(2*p1*p3 - 3*p1*p4 - 2*p1 + p2*p4 - 2*p3 + 3*p4 + 2)/(p1*p3 - 2*p1*p4 - p1 + p2*p4 - p3 + 2*p4 + 1)
    f11   =  (2*p1*p3 - 5*p1 + p2*p3 - p3*p4 - 2*p3 + p4 + 5)/(2*p1 - p2*p3 + p3*p4 - p4 - 2)
    f12   =  -(3*p1 - p3 - 3)/(p1 - p3 - 1)
    f13   =  -(3*p1 - p3 - 3)/(p1 - p3 - 1)
    f14   =  -(3*p1 - p3 - 3)/(p1 - p3 - 1)
    f15   =  -(3*p1 - p3 - 3)/(p1 - p3 - 1)
    scores = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]
    m = max(scores)
    indexes = [i for i, j in enumerate(scores) if j == m]
    return indexes

def sprint(vector):
    return '[' + ','.join('%d' % v for v in vector) + ']'

def main():    
    # sys.stdout = open(r'../../data/bestResponses.txt','wt')
    result = []
    candidates = []
    # candidates = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999]
    for p1 in candidates:
        for p2 in candidates:
            for p3 in candidates:
                for p4 in candidates:
                    index = bestResponse(p1,p2,p3,p4)
                    for i in index:
                        if (i not in result):
                            result = result + [i]
                    print(p1,p2,p3,p4, sprint(index))
    index = bestResponse(p1 = 3/4, p2 = 3/8, p3 = 1/2, p4 = 1/8)
    print(index)
    
if __name__== "__main__":
    main()
