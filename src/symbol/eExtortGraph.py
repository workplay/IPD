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
def allresponse(p):
    # file = open(r'../../data/response8462.csv','w')
    result = []
    candidates = candvector()
    for q1 in candidates:
        for q2 in candidates:
            for q3 in candidates:
                for q4 in candidates:
                    q=[q1,q2,q3,q4]
                    payoff = avePayoff_cal(p,q)
                    result = result + [payoff]
                    # record = sprint(q)+':'+str(payoff[0])+','+str(payoff[1])+'\n'
                    # print(record)
                    # file.write(record)
    # file.close()
    return result
        
def main():
    p = [0.9, 0.5, 0.2, 0.1]
    result = allresponse(p)
    result = np.array(result)
    points = result
    
    # print(result)
    hull = ConvexHull(result)
    # print(hull)

    plt.xlabel("$s_X$")
    plt.ylabel("$s_Y$")

    plt.axis([0.5, 4, 1.4, 2.3])
    plt.plot(result[:,0], result[:,1], 'b.', label="$(s_X,s_Y)$")
    
    for simplex in hull.simplices:
        lines = plt.plot(points[simplex, 0], points[simplex, 1], 'r-', linewidth = 4)
    
    q = [1,1,1,1]
    corner = avePayoff_cal(p,q)
    print(corner[0],corner[1])
    plt.plot(corner[0],corner[1], 'g^', markersize=14, label = "$q=(1,1,1,1)$")
    plt.legend()
    
    plt.show()
    
if __name__== "__main__":
    main()