function [timestamp1_sync, timestamp2_sync] = sync(timestamp1, timestamp2, tol)
[m, ~] = size(timestamp1);
[n, ~] = size(timestamp2);
last = 1;
index = 1;
for i = 1 : m
    for j = last : n
        if abs(timestamp1(i) - timestamp2(j)) < tol
            timestamp1_sync(index, 1) = timestamp1(i);
            timestamp2_sync(index, 1) = timestamp2(j);
            index = index + 1;
            last = j + 1;
            continue
        end
    end
end
end