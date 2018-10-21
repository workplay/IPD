# -*- coding: utf-8 -*-
from z3 import *
import pandas as pd
import sys

# Give Concrete values to R,S,T,P
def bestResponse(p1,p2,p3,p4,R=-1,S=-3,T=0,P=-2):
    # load expression of extremums
    df = pd.read_excel('./data/Extremums.xlsx', sheet_name='Sheet1')
    scores = []
    for i in range(df.shape[0]):
        scores = scores + [eval(df.iat[i,1])]
    # print(scores)
    m = max(scores)
    indexes = [i for i, j in enumerate(scores) if j == m]
    # check if indexes are absolute best response before return it.
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
    s.add(2*R > T+S)
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
    sys.stdout = open('./data/absoluteBestResponses.txt','wt')
    global df
    df = pd.read_excel('./data/SymbolicSubstraction.xlsx', sheet_name='Sheet1')
    candidates = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999]

    for p1 in candidates:
        for p2 in candidates:
            for p3 in candidates:
                for p4 in candidates:
                    index = bestResponse(p1,p2,p3,p4)
                    print(p1,p2,p3,p4, sprint(index))
    
    
if __name__== "__main__":
    main()
