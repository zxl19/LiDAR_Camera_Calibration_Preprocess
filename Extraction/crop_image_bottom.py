# -*- coding:utf-8 -*-

import os
import configparser
import cv2
from mkdir import mkdir
from status import status


# *Read config file
config = configparser.ConfigParser()
config.read('config.ini')
image_path = config['DEFAULT']['image_path']
cropped_path = config['DEFAULT']['cropped_path']
cropped_resolution = config['DEFAULT'].getint('cropped_resolution')


# *Read and crop images
image_list = os.listdir(image_path)
image_list.sort()
mkdir(cropped_path)
N = len(image_list)
n = 0
print "Cropping process started!"
for image_name in image_list:
    image = cv2.imread(image_path + image_name)
    image = image[:-cropped_resolution, :, :]
    cv2.imwrite(cropped_path + image_name, image)
    n = n + 1
    status(40, float(n) / N)
status(40, 1)
print "\nImages cropped successfully!"
print "Exiting......"
