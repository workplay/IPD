"""
    Draw Figure 1 in the paper.
    It may take some time.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# print format vector to string
def sprint(vector):
    return '[' + ', '.join('%1.3f' % v for v in vector) + ']'

# two float number are equal give precision
def equals(a,b,precision=0.001):
    return(abs(a-b) < precision)

# calculate stationary vector according to Cramer's rule
def sVector_cal(p=[0.5,0.5,0.5,0.5],q=[0.5,0.5,0.5,0.5]):
    p = [0] + p
    q = [0] + q
    D = np.matrix( \
    [ [ p[1]-1, p[2]-1, p[3], p[4]],  \
      [ q[1]-1, q[3], q[2]-1, q[4]],  \
      [ p[1]*q[1]-1, p[2]*q[3], p[3]*q[2], p[4]*q[4] ], \
      [ 1, 1, 1, 1] ]);
    D1 = D.copy()
    D2 = D.copy()
    D3 = D.copy()
    D4 = D.copy()
    D1[:,0] = np.matrix([[0],[0],[0],[1]])
    D2[:,1] = np.matrix([[0],[0],[0],[1]])
    D3[:,2] = np.matrix([[0],[0],[0],[1]])
    D4[:,3] = np.matrix([[0],[0],[0],[1]])    
    detD = np.linalg.det(D)
    if (detD == 0):
        print("error, det(D) equals to zero.")
        return [-1,-1,-1,-1]
    v1 = np.linalg.det(D1) / detD
    v2 = np.linalg.det(D2) / detD
    v3 = np.linalg.det(D3) / detD
    v4 = np.linalg.det(D4) / detD
    return [v1,v2,v3,v4]

def avePayoff_cal(p,q):
    sVector = sVector_cal(p,q)
    payoff_p = np.dot(sVector,[3,0,5,1])
    payoff_q = np.dot(sVector,[3,5,0,1])
    return [payoff_p, payoff_q]

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