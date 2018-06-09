function maxRound = getConvergentRound(p,q)
% p1 = 11/13;
% p2 = 1/2;
% p3 = 7/26;
% p4 = 0;
% q1=0.3;
% q2=0.4;
% q3=0.5;
% q4=0.6;

p1 = p(1);
p2 = p(2);
p3 = p(3);
p4 = p(4);
q1 = q(1);
q2 = q(2);
q3 = q(3);
q4 = q(4);

% v=[0.25,0.25,0.25,0.25];
v = [0,0,0,1];

M = [ p1*q1, p1*(1-q1), (1-p1)*q1, (1-p1)*(1-q1);
    p2*q3, p2*(1-q3), (1-p2)*q3, (1-p2)*(1-q3);
    p3*q2, p3*(1-q2), (1-p3)*q2, (1-p3)*(1-q2);
    p4*q4, p4*(1-q4), (1-p4)*q4, (1-p4)*(1-q4)];

for i=0:10000
    previous=v;
    v = v*M;
    %v=round(v.*(10000))./(10^10000);    
    v=round(v,4);
    %disp(i);
    %disp(v);
    if (v==previous)
        break;
    end
end

disp(i);
maxRound = i;         
          
   