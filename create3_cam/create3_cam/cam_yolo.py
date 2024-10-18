#!/usr/bin/env python3
import cv2
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main(args=None): 
    rclpy.init(args=None)
    node = rclpy.create_node('Show_image_python')
    subscription = node.create_publisher(Image,"/Einstein/cam", 1) # Creating the Subscribe node
    net = cv2.dnn.readNet("src/create3_cam/create3_cam/dnn_model/yolov4-tiny.weights", "src/create3_cam/create3_cam/dnn_model/yolov4-tiny.cfg")
    myModel = cv2.dnn_DetectionModel(net)   
    myModel.setInputParams(size=(320,320), scale=1/255)
    bridge = bridge = CvBridge()
    classes = []
    with  open("src/create3_cam/create3_cam/dnn_model/classes.txt", "r") as f:
        for class_name in f.readlines():
            class_name = class_name.replace("\n", "")
            classes.append(class_name.strip()) 

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 540)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    while True:
        ret, frame = cap.read()
        (class_ids, score, bboxes) = myModel.detect(frame)
        for class_id, score, bbox in zip(class_ids, score, bboxes):
            x, y, w, h = bbox
            cv2.putText(frame, classes[class_id], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        msg = Image()
        msg = bridge.cv2_to_imgmsg(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), encoding='rgb8')
        subscription.publish(msg)

if __name__ == '__main__': main()