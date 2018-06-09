clear;
for  q1=0:100
 %   for q2=0:10
 %       for q3=0:10
 %           for q4=0:10
                p=[0.5,0.6,0.7,0.4];
                %q=[q1/10.0,q2/10.0,q3/10.0,q4/10.0];
                q=[q1/100.0,0.1,0.8,0];
                r = getConvergentRound(p,q);
                
                disp(q); 
                %Store all results in one matrix.
                % index=q1*11*11*11 + q2*11*11 + q3*11 + q4 + 1;
  %          end
  %      end
  %  end
end