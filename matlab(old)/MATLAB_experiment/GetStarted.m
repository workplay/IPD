%This program is to pick up the basic grammers of MATLAB.
p = [0.5,0.5,0.5,0.5];
q = [1,2,3,4];
fprintf('%.2f ',p .* q);
fprintf('\n');

%replace 0 with NaN
A = [1 2 0 -4 5 0 0 6];
A(A == 0) = NaN;
disp(A);

