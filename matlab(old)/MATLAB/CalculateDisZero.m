for p1=0:1
    for p2=0:1
        for p3=0:1
            for p4=0:1
                for q1=0:1
                    for q2=0:1
                        for q3=0:1
                            for q4=0:1
                                p1=0.5;
                                p2=0.5;
                                p3=0.5;
                                p4=0.5;
                                p=[p1,p2,p3,p4];
                                q=[q1,q2,q3,q4];
                                D  =    [p(1)-1, p(2)-1, p(3), p(4);
                                        q(1)-1, q(3), q(2)-1, q(4); 
                                        p(1)*q(1)-1, p(2)*q(3), p(3)*q(2), p(4)*q(4);
                                        1, 1, 1, 1];
                                if (det(D) == 0)
                                    fprintf("%d : (%d, %d, %d, %d)-(%d, %d, %d, %d)\n",det(D),p,q);
                                end
                            end
                        end
                    end
                end
            end
        end
    end
end
                       
