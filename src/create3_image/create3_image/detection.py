#!/usr/bin/env python3
import rclpy
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge
import numpy as np

rgb = None
depth = None
frame = None 
bridge = CvBridge()

def on_imagec(msg):
    global rgb
    global contours_filtered
    cv_image = bridge.imgmsg_to_cv2(msg, msg.encoding)
    rgb = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)

def detect(mask, img):
    global depth
    size = 10
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(size,size))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    mask = cv.erode(mask, cv.getStructuringElement(cv.MORPH_RECT,(size*2,size*2)))
    contours, h = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 2, 1)
    for cnt in contours:
        moment = cv.moments(cnt)
        if moment["m00"] != 0:
            if cv.contourArea(cnt) > 2000:
                mask = np.zeros_like(depth)
                cv.drawContours(mask,[cnt],-1,255,-1)
                mask = cv.bitwise_and(depth, mask)
                points = np.transpose(np.nonzero(mask))
                min, max, mean = int(np.min(points))/10, int(np.max(points))/10, int(np.mean(points))/10
                cx, cy = int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"])
                cv.putText(img, "min" + str(min) + " cm", (cx,cy), 1, 1.5, (0, 255, 0), 1, 1)
                cv.putText(img, "max" + str(max) + " cm", (cx,cy+30), 1, 1.5, (0, 255, 0), 1, 1)
                cv.putText(img, "mean" + str(mean) + " cm", (cx,cy+60), 1, 1.5, (0, 255, 0), 1, 1)

def on_imaged(msg):
    global frame
    global depth
    global rgb
    global contours_filtered
    depth = bridge.imgmsg_to_cv2(msg, msg.encoding)
    depth = cv.medianBlur(depth, 5)
    min_t, max_t = np.min(depth), np.max(np.where(depth < 8000))
    depth_interp = np.interp(depth, [min_t, max_t], [0, 255]).astype(np.uint8)
    depth_color = cv.applyColorMap(depth_interp, cv.COLORMAP_AUTUMN)

    #cv.ellipse(depth_color, cnt, -1, (255, 0, 0), 2, 1)

    hsv = cv.cvtColor(rgb, cv.COLOR_BGR2HSV)
    #Blue
    maskb = cv.inRange(hsv, (80, 80, 80), (180, 255, 255))
    #Orange
    masko = cv.inRange(hsv, (15, 80, 80), (50, 255, 255))
    #Pink
    maskp1 = cv.inRange(hsv, (0, 80, 80), (30, 255, 255))
    maskp2 = cv.inRange(hsv, (220, 80, 80), (255, 255, 255))
    maskp = cv.bitwise_or(maskp1, maskp2)

    detect(maskb, rgb)
    detect(masko, rgb)
    detect(maskp, rgb)


    frame = rgb

def on_image_detect():
    global frame
    global depth
    global rgb
    global pub_detect
    msg = Image()
    msg = bridge.cv2_to_imgmsg(frame)
    pub_detect.publish(msg)
 
def main(args=None): 
    rclpy.init(args=None)
    global pub_detect
    nodergb = rclpy.create_node('rs_color')
    nodergb.create_subscription(Image,"/Einstein_rs/color/image_raw", on_imagec, 1)

    noded = rclpy.create_node('rsd_depth')
    noded.create_subscription(Image,"/Einstein_rs/depth/image_rect_raw", on_imaged, 1)

    nodedetect = rclpy.create_node('rs_detect')
    pub_detect = nodergb.create_publisher(Image,"/Einstein_rs/detect/obstacles", 1)
    nodedetect.create_timer(0.01, on_image_detect)

    while True:
        rclpy.spin_once(nodergb)
        rclpy.spin_once(noded)
        rclpy.spin_once(nodedetect)
if __name__ == '__main__': main()