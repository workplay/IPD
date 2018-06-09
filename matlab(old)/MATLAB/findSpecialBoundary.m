% enumerate all strategies of p
% find special boundaries

for p1=0:10
    for p2=0:10
        for p3=0:10
            for p4=0:10
                p=[p1/10.0,p2/10.0,p3/10.0,p4/10.0];
                vertex = getBoundary(p);
                if (~normalBoundary(vertex))
                    disp(p);
                end;
            end;
        end;
    end;
end;