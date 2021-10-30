# -*- coding:utf-8 -*-

import os
import sys
import subprocess
import yaml
import configparser
import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError


def readConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    global output_path
    global bag_path
    global image_topic
    output_path = config['DEFAULT']['output_path']
    bag_path = config['DEFAULT']['bag_path']
    image_topic = config['DEFAULT']['image_topic']


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print "Destination folder %s created!" % (output_path)
    else:
        print "Destination folder %s exists!" % (output_path)


def status(length, percent):
    sys.stdout.write('\x1B[2K')  # Erase entire current line
    sys.stdout.write('\x1B[0E')  # Move to the beginning of the current line
    progress = "Progress: ["
    for i in range(0, length):
        if i < length * percent:
            progress += '='
        else:
            progress += ' '
    progress += "] " + str(round(percent * 100.0, 2)) + "%"
    sys.stdout.write(progress)
    sys.stdout.flush()


class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        readConfig()
        mkdir(output_path)
        info_dict = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_path], stdout=subprocess.PIPE).communicate()[0])
        duration = info_dict['duration']
        start_time = info_dict['start']
        with rosbag.Bag(bag_path, 'r') as bag:
            print "Extraction process started!"
            for topic, msg, t in bag.read_messages():
                if topic == image_topic:
                    if "compressed" in image_topic:
                        try:
                            cv_image = self.bridge.compressed_imgmsg_to_cv2(msg)  # *For sensor_msgs/CompressedImage
                        except CvBridgeError as e:
                            print e
                    else:
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")  # *For sensor_msgs/Image
                        except CvBridgeError as e:
                            print e
                    # !Timestamps MUST HAVE 6 decimal places.
                    timestr = "%.6f" % (msg.header.stamp.to_sec())
                    image_name = timestr + ".jpg"
                    cv2.imwrite(output_path + image_name, cv_image)
                    percent = (t.to_sec() - start_time) / duration
                    status(40, percent)
        status(40, 1)
        print "\nImages extracted successfully!"
        print "Exiting......"


if __name__ == '__main__':
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
