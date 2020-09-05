function filename = readFilename(listing, suffix)
[m, ~] = size(listing);
filename = zeros(m, 1);
for i = 1 : m
    filename(i) = str2double(strrep(listing(i).name, suffix, ''));
end
end