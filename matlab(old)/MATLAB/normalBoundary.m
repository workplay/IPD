% Normal Boundary
% Must contain 1111,0111,0101,0001,0000,1010
% Cannot contain 1011,1100,1001,0110,0010,0011
% Input: A set of boundarys
% Output: a logical, 1 for normal boundary, 0 otherwise
function normal = normalBoundary(boundary)
    %suppose it is normal
    normal = 1;
    
    % must contain one of always defect strategies
    all_defect = [0,0,0,0; 0,1,0,0; 1,0,0,0];
    tmp = ismember(all_defect, boundary, 'rows');
    normal = normal & (sum(tmp) > 0);
    
    % must contain one of always cooperate strategies
    all_cooperate = [1,1,1,1; 1,1,1,0; 1,1,0,1];
    tmp = ismember(all_cooperate, boundary, 'rows');
    normal = normal & (sum(tmp) > 0);
    
    % must contain all boundary strategies.
    % they are:
    % 0001, 0101, 0111, 1010
    necessary_boundary = [0,0,0,1; 0,1,0,1; 0,1,1,1; 1,0,1,0];
    tmp = ismember(necessary_boundary, boundary, 'rows');
    normal = normal & (sum(tmp) == 4);
    
    % mustn't contain other strategies.
    % they are:
    % 0010, 0011, 0110, 1001, 1100, 1011
    inside_points = [0,0,1,0; 0,0,1,1; 0,1,1,0; 1,0,0,1; 1,1,0,0; 1,0,1,1];
    tmp = ismember(inside_points, boundary, 'rows');
    normal = normal & (sum(tmp) == 0);
    
    % disp(normal);
end


