clear;
result=[];
for  q1=0:100
 %   for q2=0:10
 %       for q3=0:10
 %           for q4=0:10
                p=[0.5,0.6,0.7,0.4];
                %q=[q1/10.0,q2/10.0,q3/10.0,q4/10.0];
                q=[0.5,q1/100.0,0.01,0];
                r = getConvergentRound(p,q);
                if (r<20)
                    result=[result;[q1/100.0,r]];
                end
                disp(q); 
                %Store all results in one matrix.
                % index=q1*11*11*11 + q2*11*11 + q3*11 + q4 + 1;
  %          end
  %      end
  %  end
end
scatter(result(:,1)',result(:,2)','r','.');