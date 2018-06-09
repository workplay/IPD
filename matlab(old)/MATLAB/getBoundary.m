% Given one strategy p, enumerate all q.
% Get all vertexes of that boundary.
% No duplicated results in the return value.
function vertex = getBoundary(p)
% disp(p); 

% boundary made by reactive strategies
boundary = zeros(2*2*2*2,4);
label_set = zeros(2*2*2*2,4);
for q1=0:1
    for q2=0:1
        for q3=0:1
            for q4=0:1
                q=[q1,q2,q3,q4];
                index = q1*2*2*2 + q2*2*2 + q3*2 + q4 +1;
                label_set(index,:) = q;
                [cc,cd,dc,dd] = CalculateStationaryDistribution(p,q);
                boundary(index,:) = [cc,cd,dc,dd];
            end;
        end;
    end;
end;

% make labels here.
labels = label_set;

vertex = [];
x = boundary(:,2)';
y = boundary(:,3)';
k = convhull(x,y);
for i=1:size(k)
    vertex = [vertex;labels(k(i),:)];
end;   

vertex = unique(vertex,'rows');
% disp(vertex)



