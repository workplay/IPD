data = resultExtort5720;
scatter(data(:,1),data(:,2),'.');
hold on
scatter(data(:,1),data(:,3),'.');
hold on
scatter(data(:,1),data(:,4),'.');
hold on
scatter(data(:,1),data(:,5),'.');
xlabel('round')
ylabel('percentage')
title('ABM, p=Extortionate, q=(0.5,0.7,0.2,0)')
legend('v1','v2','v3','v4')