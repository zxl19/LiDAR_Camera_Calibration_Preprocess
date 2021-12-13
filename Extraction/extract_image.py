# -*- coding:utf-8 -*-

import configparser
import subprocess
import yaml
import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
from mkdir import mkdir
from status import status


config = configparser.ConfigParser()
config.read('config.ini')
bag_path = config['DEFAULT']['bag_path']
image_topic = config['DEFAULT']['image_topic']
image_path = config['DEFAULT']['image_path']


class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        info_dict = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_path], stdout=subprocess.PIPE).communicate()[0])
        duration = info_dict['duration']
        start_time = info_dict['start']
        mkdir(image_path)
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
                    # !Timestamps MUST HAVE 9 decimal places.
                    timestr = "%.9f" % (msg.header.stamp.to_sec())
                    image_name = timestr + ".jpg"
                    cv2.imwrite(image_path + image_name, cv_image)
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
