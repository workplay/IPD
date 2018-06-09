%This function calculates the final distribution of strategy p vs. q
function [v1,v2,v3,v4] = CalculateStationaryDistribution(p,q)
    debug = 0;
    adjustment = 1;
    if (adjustment)
        %deal with edge cases
        epsilon = 0.0000;
        p(p == 0) = epsilon;
        p(p == 1) = 1-epsilon;
        q(q == 0) = epsilon;
        q(q == 1) = 1-epsilon;
    end;
    D  =    [p(1)-1, p(2)-1, p(3), p(4);
            q(1)-1, q(3), q(2)-1, q(4); 
            p(1)*q(1)-1, p(2)*q(3), p(3)*q(2), p(4)*q(4);
            1, 1, 1, 1];
    %disp(D);
    if (debug)
        disp(D);
    end;
    
    D1 = D;
    D2 = D;
    D3 = D;
    D4 = D;
    
    D1(:,1) = [0;0;0;1];
    D2(:,2) = [0;0;0;1];
    D3(:,3) = [0;0;0;1];
    D4(:,4) = [0;0;0;1];
    
    if (debug)
        disp(D1);
    end;
    
    v1 = det(D1)/det(D);
    v2 = det(D2)/det(D);
    v3 = det(D3)/det(D);
    v4 = det(D4)/det(D);
 
    
    if (debug)
        disp([v1,v2,v3,v4]);
    end;
end