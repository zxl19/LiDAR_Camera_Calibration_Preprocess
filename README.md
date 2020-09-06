# LiDAR_Camera_Calibration_Preprocess

This repository contains MATLAB and Python tools to extract and synchronize pointclouds and images from a rosbag for extrinsic calibration.

## Data Extraction

### Pointcloud

Use `pcl_ros` to extract pointclouds from a rosbag:

```shell
rosrun pcl_ros bag_to_pcd <bag_path> <pointcloud_topic> <folder_path>
```

### Image

Use `extract_image.py` to extract images from a rosbag:

```shell
python extract_images.py
```

## Data Synchronization

Run `main.m` to synchronize timestamps.

## Extrinsic Calibration

After extracting and synchronizing data from the rosbag, use `CameraCalibrator` app in MATLAB to calculate the intrinsic of the camera. Later, use the method mentioned in the following paper to calibrate the extrinsic between LiDAR and camera.

[1]. Xie S, Yang D, Jiang K, et al. Pixels and 3-D Points Alignment Method for the Fusion of Camera and LiDAR Data[J]. IEEE Transactions on Instrumentation and Measurement, 2019, 68(10): 3661-3676. [[LINK](https://ieeexplore.ieee.org/document/8565990)]

## Reference

1. [ROS Answers](https://answers.ros.org/question/289937/subscribing-to-compressed-images-from-rosbag/)
2. [CSDN Blog](https://blog.csdn.net/yinxingtianxia/java/article/details/80266849)