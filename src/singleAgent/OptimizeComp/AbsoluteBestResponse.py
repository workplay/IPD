# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd
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
    # print(indexes)
    # TODO: check if indexes are absolute best response before return it.
    indexes = absoluteList(p1,p2,p3,p4, indexes)
    return indexes

# given p1,p2,p3,p4 and possible best responses
# check whether or not, they are abosolute
# return a subset of indexes of best responses.
def absoluteList(p1,p2,p3,p4, indexes):
    ablist = []
    for index in indexes:
        if absoluteBest(p1,p2,p3,p4,index):
            ablist = ablist + [index]
    return ablist

def absoluteBest(_p1,_p2,_p3,_p4,index):
    duplicates = [4, 8, 13, 14, 15]
    if index in duplicates:
        return False
    # compare index with all others.
    R, T, S, P = z3.Reals('R T S P')
    p1, p2, p3, p4 = z3.Reals('p1 p2 p3 p4')
    s = z3.Solver()
    s.set('timeout',10000)
    s.add(T>R, R>P, P>S)
    # s.add(2*R > T+S)
    s.add(p1 == _p1)
    s.add(p2 == _p2)
    s.add(p3 == _p3)
    s.add(p4 == _p4)
    for j in range(0, df.shape[0]):
        s.push()
        if (j == index) or (j in duplicates):
            continue;
        f = eval(df.iat[index,j])
        s.add(f < 0)
        result = s.check()
        if result == z3.sat:
            # print("sat")
            s.pop()
            return False
        elif result == z3.unsat:
            s.pop()
        elif result == z3.unknown:
            print("unknown",p1,p2,p3,p4,index)
            s.pop()
            return False
        else:
            print("error check result")
            s.pop()
            return False
    return True

def sprint(vector):
    return '[' + ','.join('%d' % v for v in vector) + ']'

def main():    
    # sys.stdout = open(r'../../data/absoluteBestResponses_without2R.txt','wt')
    global df
    df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
    #candidates = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999]
    candidates = []
    for p1 in candidates:
        for p2 in candidates:
            for p3 in candidates:
                for p4 in candidates:
                    index = bestResponse(p1,p2,p3,p4)
                    print(p1,p2,p3,p4, sprint(index))
    index = bestResponse(0.999, 0.001, 0.001, 0.001)
    print(index)
    
if __name__== "__main__":
    main()
