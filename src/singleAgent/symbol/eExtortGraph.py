8# -*- coding: utf-8 -*-
from utils import equals,sprint
from avepayoff import avePayoff_cal
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

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
def allresponse(q):
    # file = open(r'../../data/response8462.csv','w')
    result = []
    candidates = [ 0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98, 0.999 ]
    for p1 in candidates:
        for p2 in candidates:
            for p3 in candidates:
                for p4 in candidates:
                    if p1 == 1 and p2 ==1 and p3 == 0 and p4 == 0:
                        continue;
                    p=[p1,p2,p3,p4]
                    payoff = avePayoff_cal(p,q)
                    result = result + [payoff]
                    # record = sprint(q)+':'+str(payoff[0])+','+str(payoff[1])+'\n'
                    # print(record)
                    # file.write(record)
    # file.close()
    return result
        
def main():
    q = [0.9, 0.5, 0.2, 0.1]
    result = allresponse(q)  
    result = np.array(result)
    points = result
    
    # print(result)
    hull = ConvexHull(result)
    # print(hull)

    plt.xlabel("$s_X$")
    plt.ylabel("$s_Y$")

    plt.axis([1.5, 2.4, 0.5, 4])
    plt.plot(result[:,0], result[:,1], 'c.',  label="$(s_X,s_Y)$")
    
    for simplex in hull.simplices:
        lines = plt.plot(points[simplex, 0], points[simplex, 1], 'b-', linewidth = 2)
    
    p = [1,1,1,1]
    corner = avePayoff_cal(p,q)
    print(corner[0],corner[1])
    plt.plot(corner[0],corner[1], 'g^', markersize=14, label = "$p=(1,1,1,1)$")
    plt.legend()
    
    plt.show()
    
if __name__== "__main__":
    main()