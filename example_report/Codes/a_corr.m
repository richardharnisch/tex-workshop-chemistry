function res = auto_correlation(y, n)
    N = length(y)-n;
    y = y - mean(y);
    temp = y(end-N+1:end)'*y(end-N-n+1:end-n);
    res = temp/N;
end
