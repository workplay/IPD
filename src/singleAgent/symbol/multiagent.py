# -*- coding: utf-8 -*-
import avepayoff
   

q = [0.9, 0.5, 0.2, 0.1]
# u = [0.4, 0.8, 0.2, 0.6]
u = [0.4, 0.8, 0.2, 0.6]
pi = 0.9

candidates = [0, 1]
result = []
maxpayoff = -1
maxindex = -1
for p1 in candidates:
    for p2 in candidates:
        for p3 in candidates:
            for p4 in candidates:
                if p1 == 1 and p2 ==1 and p3 == 0 and p4 == 0:
                    continue;
                p=[p1,p2,p3,p4]
                payoff = pi * avePayoff_cal(p,q)[0] + (1-pi) * avePayoff_cal(p,u)[0]
                if (payoff > maxpayoff):
                    maxpayoff = payoff
                    maxindex = p
                print(p,payoff)
 
print('-------max payoff in deterministic strategies-------------')               
print(maxindex, maxpayoff)



candidates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
result = []
maxpayoff = -1
maxindex = -1
for p1 in candidates:
    for p2 in candidates:
        for p3 in candidates:
            for p4 in candidates:
                if p1 == 1 and p2 ==1 and p3 == 0 and p4 == 0:
                    continue;
                p=[p1,p2,p3,p4]
                payoff = pi * avePayoff_cal(p,q)[0] + (1-pi) * avePayoff_cal(p,u)[0]
                if (payoff > maxpayoff):
                    maxpayoff = payoff
                    maxindex = p
                # print(p,payoff)
 
print('-------max payoff in all strategies-------------')               
print(maxindex, maxpayoff)


