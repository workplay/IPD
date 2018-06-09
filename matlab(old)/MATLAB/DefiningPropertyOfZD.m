A = [3,3,1; 0,5,1; 5,0,1];
B = [-1;-1;1];
parameters = A\B;
disp(parameters);

syms p1 p2 p3; 
alpha = p1 - 0.6*p2 - 0.4*p3 - 0.4;
beta = p1 - 0.4*p2 - 0.6*p3 - 0.6;
gamma = (-5) * p1 + 3*p2 + 3*p3 +2;


disp([alpha,beta,gamma]);
disp(alpha+beta+gamma);