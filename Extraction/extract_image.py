# -*- coding:utf-8 -*-

import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

# Change image destination folder path here.
output_path = '/home/zhangxl/data/img/'
# Change rosbag path here.
bag_path = '/home/zhangxl/data/WYH/2020-09-02-11-46-46.bag'
# Change image topic here.
image_topic = '/right_usb_cam/image_raw/compressed'


class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag(bag_path, 'r') as bag:
            for topic, msg, t in bag.read_messages():
                if topic == image_topic:
                    try:
                        # cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8") # For /image/raw
                        cv_image = self.bridge.compressed_imgmsg_to_cv2(
                            msg)  # For /image/compressed
                    except CvBridgeError as e:
                        print e
                    # Timestamps HAVE to be 9 decimal places
                    timestr = "%.9f" % msg.header.stamp.to_sec()
                    image_name = timestr + ".jpg"
                    cv2.imwrite(output_path + image_name, cv_image)


if __name__ == '__main__':
    # rospy.init_node(PKG)
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
