function [timestamp1_sync, timestamp2_sync] = sync2(timestamp1, timestamp2, tol)
[m, ~] = size(timestamp1);
[n, ~] = size(timestamp2);
index = 1;
last_index = 1;
for i = 1 : m
    [ind, err] = findnearest(timestamp1(i, 1), timestamp2(last_index : n, 1));
    if err < tol
        timestamp1_sync(index, 1) = timestamp1(i, 1);
        timestamp2_sync(index, 1) = timestamp2(last_index + ind - 1, 1);
%         fprintf('%f \n%f \n',timestamp1(i, 1), timestamp2(last_index + ind - 1, 1))
        index = index + 1;
        last_index = last_index + ind;
    else
        continue
    end
end