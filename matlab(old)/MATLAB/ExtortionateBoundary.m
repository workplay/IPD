function e = ExtortionateBoundary(vertex)
    e = (sum(vertex(:,3)<(vertex(:,2))) == 0);
end