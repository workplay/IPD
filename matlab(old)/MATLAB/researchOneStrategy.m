%Given one strategy p, enumerate all q.
%Visualize the results.
function researchOneStrategy(p)
% disp(p); 

%initialize results.
results = zeros(11*11*11*11,4);

for  q1=0:10
    for q2=0:10
        for q3=0:10
            for q4=0:10
                q=[q1/10.0,q2/10.0,q3/10.0,q4/10.0];
                [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
                
                %Store all results in one matrix.
                index=q1*11*11*11 + q2*11*11 + q3*11 + q4 + 1;
                results(index,:) = [v1,v2,v3,v4];
            end;
        end;
    end
end
%disp(results);


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
labels = num2str(label_set);


myTitle = sprintf('IPD. X=%s incremental=0.1',num2str(p,'%.1f,'));
figure('Name',myTitle,'NumberTitle','off');

scatter(results(:,2)',results(:,3)','.');
hold on;
scatter(boundary(:,2)',boundary(:,3)','+','r');
hold on;
x = boundary(:,2)';
y = boundary(:,3)';
k = convhull(x,y);
plot(x(k),y(k),'r-')
for i=1:size(k)
    text(x(k(i)),y(k(i)),strrep(labels(k(i),:),' ',''));
end;   
plot([0,0.5],[0,0.5],'g-');
axis([0,0.7,0,0.7]);
xlabel('v2');
ylabel('v3');

