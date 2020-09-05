function copyFile(path, timestamp_img_sync, timestamp_pcd_sync)
path_img_sync = "./img_sync/";
path_pcd_sync = "./pcd_sync/";
[~, ~, ~] = mkdir(path_img_sync);
[~, ~, ~] = mkdir(path_pcd_sync);
[m, ~] = size(timestamp_img_sync);
for i = 1 : m
    img = strcat(path, strcat("img/", strcat(num2str(timestamp_img_sync(i, 1), '%6f'), ".jpg")));
    [status_1, message_1, messageId_1] = copyfile(img, path_img_sync, 'f');
    if status_1 == 0
        fprintf("Image      %s not found!\n", strcat(num2str(timestamp_img_sync(i, 1), 16), ".jpg"));
    end
    pcd = strcat(path, strcat("pcd/", strcat(num2str(timestamp_pcd_sync(i, 1), '%6f'), strcat("000", ".pcd"))));
    [status_2, message_2, messageId_2] = copyfile(pcd, path_pcd_sync, 'f');
    if status_2 == 0
        fprintf("Pointcloud %s not found!\n", strcat(num2str(timestamp_pcd_sync(i, 1), 16), strcat("000", ".pcd")));
    end
end
end