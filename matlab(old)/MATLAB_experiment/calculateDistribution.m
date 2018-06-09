A=[];
B=[];
p = [0.1,0.2,0.3,0.4];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.1,0.4,0.3,0.5];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.3,0.5,0.6,0.4];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.3,0.8,0.2,0.7];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.5,0.4,0.6,0.1];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.5,0.8,0.6,0.3];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.7,0.5,0.4,0.3];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

p = [0.8,0.6,0.4,0.5];
[group,one] = GroupAndOne(p);
A=[A;group'];
B=[B;one'];

disp(A);
disp(B);

 Distribution = A\B;

 disp(Distribution);

 p = [0.8,0.6,0.4,0.5];
 [group,one] = GroupAndOne(p);
% disp('------------')
% disp(Distribution * group);
% disp(one);