function pickFile(oldpath, newpath, filename, suffix)
mkdir(newpath)
[m, ~] = size(filename);
for i = 1 : m
    copyfile(strcat(oldpath, strcat(num2str(filename(i)), suffix)), ...
        newpath);
end
end