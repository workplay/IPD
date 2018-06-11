# -*- coding: utf-8 -*-
from utils import equals,sprint
from avepayoff import avePayoff_cal

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
def allresponse(p):
    file = open(r'../../data/response8462.csv','w')
    result = []
    candidates = candvector()
    for q1 in candidates:
        for q2 in candidates:
            for q3 in candidates:
                for q4 in candidates:
                    q=[q1,q2,q3,q4]
                    payoff = avePayoff_cal(p,q)
                    record = sprint(q)+':'+str(payoff[1])+'\n'
                    # print(record)
                    file.write(record)
    file.close()
    return result
        
def main():
    result = allresponse([0.8,0.4,0.6,0.2])
if __name__== "__main__":
    main()
