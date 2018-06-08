# -*- coding: utf-8 -*-
# Given p and q, generate markov matrix

def markovmatrix(p,q):
    # prefix, let index starts from 1.
    p = [0] + p
    q = [0] + q
    M = [ [ p[1]*q[1], p[1]*(1-q[1]), (1-p[1])*q[1], (1-p[1])*(1-q[1])], \
          [ p[2]*q[3], p[2]*(1-q[3]), (1-p[2])*q[3], (1-p[2])*(1-q[3])], \
          [ p[3]*q[2], p[3]*(1-q[2]), (1-p[3])*q[2], (1-p[3])*(1-q[2])], \
          [ p[4]*q[4], p[4]*(1-q[4]), (1-p[4])*q[4], (1-p[4])*(1-q[4])] ]
    return M
    
def main():
    print(markovmatrix([0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5]))
  
if __name__== "__main__":
    main()
