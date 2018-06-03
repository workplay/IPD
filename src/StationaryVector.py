from MarkovMatrix import markovmatrix
from utils import pprint
import numpy as np

# initial vector converge to stationary according to Markov matrix
def sVector_converge(p=[0.5,0.5,0.5,0.5],q=[0.5,0.5,0.5,0.5],v0=[0.9,0,0.1,0],debug = False): 
    M = markovmatrix(p,q)
    for i in range(100):
        if (debug):
            print('[' + ', '.join('%1.3f' % v for v in v0) + ']')
        v0 = np.dot(v0, M)
    return v0

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

def main():
    pprint(sVector_cal(p=[0.7,0.2,0.3,0.4], q=[0.5,0.6,0.7,0.8]))
    pprint(sVector_converge(p=[0.7,0.2,0.3,0.4], q=[0.5,0.6,0.7,0.8]))
  
if __name__== "__main__":
    main()