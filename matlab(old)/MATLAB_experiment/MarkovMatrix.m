 p1 = 11/13;
 p2 = 1/2;
 p3 = 7/26;
 p4 = 0;
    

q1=0.3;
q2=0.4;
q3=0.5;
q4=0.6;

  v=[0,1,0,0];
 
                    M = [ p1*q1, p1*(1-q1), (1-p1)*q1, (1-p1)*(1-q1);
                        p2*q3, p2*(1-q3), (1-p2)*q3, (1-p2)*(1-q3);
                        p3*q2, p3*(1-q2), (1-p3)*q2, (1-p3)*(1-q2);
                        p4*q4, p4*(1-q4), (1-p4)*q4, (1-p4)*(1-q4)];

                    %disp(det(M));
                    %disp(det(M-eye(4,4)));

                  
                    
                    for i=0:10000
                        v = v*M;
                        disp(v);
                    end;

         
          
   