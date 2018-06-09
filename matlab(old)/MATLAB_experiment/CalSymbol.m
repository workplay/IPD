for v1=0:1
    for v2=0:1
        for v3=0:1

syms p1 p2 p3 p4 q1 q2 q3 q4
D2 = [p1-1 , 0 , p3  , 0 ; 
  q1-1 , 0 ,q2-1 , q4 ;
  p1*q1-1 , 0 , p3*q2 , 0 ;
  1 , 1 , 1 , 1];
%disp(D2);
%disp(det(D2));
D3 =  [p1-1 , p2-1 , 0  , 0;
  q1-1 , q3   , 0  , q4 ;
  p1*q1-1 , p2*q3 , 0 , 0 ;
  1 , 1 , 1 , 1];
%disp(D3);
%disp(det(D3));

disp(subs(((p1*p3 - p1 + p1*p2)*q1 + (p3 - p1*p3)*q2 + (p2-p1*p2)*q3-p3-p2 + 1),[q1,q2,q3],[v1,v2,v3]));
        end;
    end;
end;