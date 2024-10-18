#!/usr/bin/env python3
import cv2
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main(args=None): 
    rclpy.init(args=None)
    node = rclpy.create_node('Show_image_python')
    subscription = node.create_publisher(Image,"/Einstein/cam", 1) # Creating the Subscribe node
    bridge = bridge = CvBridge()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 540)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    while True:
        ret, frame = cap.read()
        msg = Image()
        msg = bridge.cv2_to_imgmsg(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), encoding='rgb8')
        subscription.publish(msg)
if __name__ == '__main__': main()