close all
clear
clc
format long
%% Determine Folder Path
path = "../../data/"; % Change root folder path here.
path_img = strcat(path, "img/*.jpg"); % Place images       in ./img/ folder
path_pcd = strcat(path, "pcd/*.pcd"); % Place point clouds in ./pcd/ folder
%% List Folder Contents
listing_img = dir(path_img);
listing_pcd = dir(path_pcd);
%% Read Filenames
timestamp_img = readFilename(listing_img, ".jpg");
timestamp_pcd = readFilename(listing_pcd, ".pcd");
%% Synchronize Timestamps
tol = 0.001; % Change tolerance here.
[timestamp_img_sync, timestamp_pcd_sync] = sync2(timestamp_img, timestamp_pcd, tol);
%% Print Sychronized Timestamp Pairs
[m, ~] = size(timestamp_img_sync);
fileID = fopen("filename_sync.txt",'w+');
for i = 1 : m
    fprintf("--------------------%06d--------------------\n",i);
    fprintf("Camera timestamp: %.9f\n",timestamp_img_sync(i, 1));
    fprintf("Lidar  timestamp: %.9f\n",timestamp_pcd_sync(i, 1));
    fprintf(fileID, "--------------------%06d--------------------\n",i);
    fprintf(fileID, "Camera timestamp: %.9f\n",timestamp_img_sync(i, 1));
    fprintf(fileID, "Lidar  timestamp: %.9f\n",timestamp_pcd_sync(i, 1));
end
fclose(fileID);
%% Copy Synchronized Files
copyFile(path, timestamp_img_sync, timestamp_pcd_sync);