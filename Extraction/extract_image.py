# coding:utf-8

import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

output_path = '/home/zhangxl/data/img/' # 存放图片的位置
bag_path = '/home/zhangxl/data/WYH/2020-09-02-11-46-46.bag' # 存放bag的位置
image_topic = '/right_usb_cam/image_raw/compressed' # 图像的topic


class ImageCreator():

    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag(bag_path, 'r') as bag:  # 要读取的bag文件；
            for topic, msg, t in bag.read_messages():
                if topic == image_topic:  # 图像的topic；
                    try:
                        # cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8") # raw
                        cv_image = self.bridge.compressed_imgmsg_to_cv2(
                            msg)  # compressed
                    except CvBridgeError as e:
                        print e
                    timestr = "%.6f" % msg.header.stamp.to_sec()
                    # %.6f表示小数点后带有6位，可根据精确度需要修改；
                    image_name = timestr + ".jpg"  # 图像命名：时间戳.jpg
                    cv2.imwrite(output_path + image_name, cv_image)  # 保存；


if __name__ == '__main__':

    # rospy.init_node(PKG)

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
