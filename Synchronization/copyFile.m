function copyFile(path, timestamp_img_sync, timestamp_pcd_sync)
path_img_sync = "./img_sync/";
path_pcd_sync = "./pcd_sync/";
[~, ~, ~] = mkdir(path_img_sync);
[~, ~, ~] = mkdir(path_pcd_sync);
[m, ~] = size(timestamp_img_sync);
for i = 1 : m
    img = strcat(path, strcat("img/", strcat(num2str(timestamp_img_sync(i, 1), '%.9f'), ".jpg")));
    [status_1, ~, ~] = copyfile(img, strcat(path_img_sync, strcat(num2str(i, '%06d'), ".jpg")), 'f');
    if status_1 == 0
        fprintf("Image      %s not found!\n", strcat(num2str(timestamp_img_sync(i, 1), '%.9f'), ".jpg"));
    end
    pcd = strcat(path, strcat("pcd/", strcat(num2str(timestamp_pcd_sync(i, 1), '%.9f'), ".pcd")));
    [status_2, ~, ~] = copyfile(pcd, strcat(path_pcd_sync, strcat(num2str(i, '%06d'), ".pcd")), 'f');
    if status_2 == 0
        fprintf("Pointcloud %s not found!\n", strcat(num2str(timestamp_pcd_sync(i, 1), '%.9f'), ".pcd"));
    end
end
end