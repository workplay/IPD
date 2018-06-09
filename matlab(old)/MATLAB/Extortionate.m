function p=Extortionate(fi,chi)
R=3;
S=0;
T=5;
P=1;
p1 = 1-fi*(chi-1)*(R-P)/(P-S);
p2 = 1-fi*(1 + chi*(T-P)/(P-S));
p3 = fi * (chi + (T-P)/(P-S));
p4 = 0;
p=[p1,p2,p3,p4];
end