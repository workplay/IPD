% Visualize the linear relationship
% when one of p_i and q_i changes
p=[0.3,0.4,0.5,0.6];

% Play against (q_1, 0.3, 0.5,0.7)
results = zeros(11,4);
for  q1=0:10
    q=[q1/10.0, 0.3, 0.5, 0.7];
    [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
    index = q1+1;
    results(index,:) = [v1,v2,v3,v4];
end
disp(results);

% Play against (q_1, 0.8, 0.5,0.7)
results2 = zeros(11,4);
for  q1=0:10
    q=[q1/10.0, 0.8, 0.5, 0.7];
    [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
    index = q1+1;
    results2(index,:) = [v1,v2,v3,v4];
end
disp(results2);

% Play against (q_1, 1, 0, 1)
results3 = zeros(11,4);
for  q1=0:10
    q=[q1/10.0, 1, 0, 1];
    [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
    index = q1+1;
    results3(index,:) = [v1,v2,v3,v4];
end
disp(results3);

% Play against (q_1, 0, 1, 0)
results4 = zeros(11,4);
for  q1=0:10
    q=[q1/10.0, 1, 1, 1];
    [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
    index = q1+1;
    results4(index,:) = [v1,v2,v3,v4];
end
disp(results4);


% Exception: (0, 0, 0, q1)
results5 = zeros(11,4);
for  q1=0:10
    q=[0, 0, 0, q1/10.0];
    [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
    index = q1+1;
    results5(index,:) = [v1,v2,v3,v4];
end
disp(results5);

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

scatter(results2(:,2)',results2(:,3)','.','g');
hold on;

scatter(results3(:,2)',results3(:,3)','*','b');
hold on;

scatter(results4(:,2)',results4(:,3)','*','g');
hold on;

scatter(results5(:,2)',results5(:,3)','*','h');
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
xlabel('v2');
ylabel('v3');
legend('(q_1, 0.3, 0.5,0.7)','(q_1, 0.8, 0.5,0.7)',...
    '(q_1, 1, 0, 1)','(q_1, 0, 1, 0)','(0, 0, 0, q1)');
