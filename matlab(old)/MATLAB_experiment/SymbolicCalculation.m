% make all parameters symbols
syms p1 p2 p3 p4 q1 q2 q3 q4;
% Represent matrix and determinants
A = [p1-1,p2-1,p3,p4;...
    q1-1,q2,q3-1,q4;...
    p1*q1-1,p2*q2,p3*q3,p4*q4;...
    1,1,1,1];
B = [0;0;0;1];
D = A;
D1 = A;
D1(:,1) = B;
% Get numerator and denominator.
f = det(D1);
g = det(D);
N = diff(f,p1)*g - f*diff(g,p1);
% Show result.
disp(diff(N,p1));