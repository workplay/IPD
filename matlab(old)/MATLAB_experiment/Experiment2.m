clear
% Prepare for all distributions.
strategies=[];
for  q1=0:10
    for q2=0:10
        for q3=0:10
            for q4=0:10
                q=[q1/10.0,q2/10.0,q3/10.0,q4/10.0];
%                [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q);
                strategies = [strategies;q];
            end
        end
    end
end

result = [];

for i=1 : 14640
    % get the number of invincible strategies
    col23 = strategies(:,2)+strategies(:,3);
    col23 = (col23<=1);
    col4 = (strategies(:,4)==0);
    col234 = col23 + col4;
    col234 = (col234 == 2);
    NumberOfInvincible=sum(col234);
    [NumberOfStrategy,width] = size(strategies);
    disp([NumberOfInvincible,NumberOfStrategy]);
    
    result = [result;[i,NumberOfInvincible/NumberOfStrategy,NumberOfInvincible,NumberOfStrategy]];
    
    % pick two strateties, let then play against each other.
    % the loser is eliminated.
    [NumberOfStrategy,width] = size(strategies);
    player1id = round(rand*NumberOfStrategy);
    if (player1id==0)
        player1id=1;
    end
    player1 = strategies(player1id,:);
    strategies(player1id,:)=[];

    [NumberOfStrategy,width] = size(strategies);
    player2id = round(rand*NumberOfStrategy);
    if (player2id==0)
        player2id=1;
    end
    player2 = strategies(player2id,:);
    strategies(player2id,:)=[];

    [v1,v2,v3,v4] = CalculateStationaryDistribution(player1,player2);
    if (v3>=v2)
        %player1 win
        strategies = [strategies;player1];
    else
        %player2 win
        strategies = [strategies;player2];
    end
end


data = result;
[AX,H1,H2] = plotyy(data(:,1),data(:,2),data(:,1),data(:,3),'plot');
set(get(AX(1),'ylabel'),'string', 'Percentage of Invincible Strategy','fontsize',16);
set(get(AX(2),'ylabel'),'string', 'The Number of Invincible Strategy','fontsize',16);
set(H2,'Marker' ,'.')
set(H1,'Marker' ,'.')
xlabel('round')
title('Percentage Of Invincible Strategies')

