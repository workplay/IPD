chi = 3;
phi_max = 1/ (4*chi + 1);
p = Extortionate(phi_max/2,chi);

chi = 5;
phi_max = 1/ (4*chi + 1);
q = Extortionate(phi_max/2,chi);

p=[11/13,1/2,7/26,0];
q=[11/13,1/2,7/26,0];

disp(p);
disp(q);

[v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
disp([v1,v2,v3,v4]);