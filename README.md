# LiDAR_Camera_Calibration_Preprocess

This repository contains MATLAB and Python tools to extract and synchronize point clouds and images from a rosbag for extrinsic calibration.

## 1. Prerequisites

1. ROS (tested on Kinetic and Melodic)
2. Python 2.X (tested on 2.7.17)
3. MATLAB (tested on 2020a and 2021b)

## 2. Data Extraction

### 2.1 Point Cloud

Use [pcl_ros](http://wiki.ros.org/pcl_ros) to extract point clouds from a rosbag:

```shell
rosrun pcl_ros bag_to_pcd <input_file.bag> <topic> <output_directory>
```

### 2.2 Image

1. Change the following lines in `config.ini`:

    ```ini
    ; Parameter Setup
    [DEFAULT]
    ; ; Change rosbag path here.
    ; bag_path = <your roabag path>
    ; ; Change image topic here.
    ; image_topic = <your image topic>
    ; ; Change image destination folder path here.
    ; image_path = <your image destination folder path>
    ; ; Change cropped image destination folder path here.
    ; cropped_path = <your cropped image destination folder path>
    ; ; Change cropped resolution from bottom here.
    ; cropped_resolution = <your cropped resolution from bottom>
    ```

2. Use `extract_image.py` to extract images from a rosbag (Python 2.X):

    ```shell
    python extract_image.py
    ```

3. Use `crop_image_bottom.py` to crop images from bottom (Python 2.X):

    ```shell
    python crop_image_bottom.py
    ```

## 3. Data Synchronization

1. Change the following lines in `main.m`:

    ```matlab
    %% Determine Folder Path
    path = "<your root folder path>"; % Change folder path here.
    path_img = strcat(path, "img/*.jpg"); % Place images       in ./img/ folder
    path_pcd = strcat(path, "pcd/*.pcd"); % Place point clouds in ./pcd/ folder
    ```

2. Run `main.m` to synchronize timestamps.
3. Check synchronized data in `./img_sync/` and `./pcd_sync/` respectively.

## 4. Extrinsic Calibration

After extracting and synchronizing data from the rosbag, use `CameraCalibrator` app in MATLAB to calculate the intrinsic of the camera. Later, use the method mentioned in the following paper[^1] to calibrate the extrinsic between LiDAR and camera.

[^1]: Xie S, Yang D, Jiang K, et al. Pixels and 3-D Points Alignment Method for the Fusion of Camera and LiDAR Data[J]. IEEE Transactions on Instrumentation and Measurement, 2019, 68(10): 3661-3676. [[LINK](https://ieeexplore.ieee.org/document/8565990)]

## 5. TODO

- [x] Read config file to get parameters.
- [x] Check and create destination folder.
- [x] Add progressbar.
- [ ] Use Python to extract both point cloud and image.
- [ ] Use Python to synchronize point cloud and image messages.
- [ ] Manually select images and corresponding point cloud.
- [ ] Release and maintain code for extrinsic calibration (All credit goes to the authors of the paper above).

## 6. Reference

1. [pcl_ros](http://wiki.ros.org/pcl_ros)
2. [ROS Answers](https://answers.ros.org/question/289937/subscribing-to-compressed-images-from-rosbag/)
3. [CSDN Blog](https://blog.csdn.net/loveSIYU/article/details/113830289)
4. [CSDN Blog](https://blog.csdn.net/memoryd/article/details/105174348)
5. [CSDN Blog](https://blog.csdn.net/qq_22059843/article/details/103018216)
6. [CSDN Blog](https://blog.csdn.net/yourgreatfather/article/details/87783906)
7. [Stack Overflow](https://stackoverflow.com/questions/39772424/how-to-effeciently-convert-ros-pointcloud2-to-pcl-point-cloud-and-visualize-it-i)
8. [Stack Overflow](https://stackoverflow.com/questions/59794926/saving-pointcloud-from-rosbag)
