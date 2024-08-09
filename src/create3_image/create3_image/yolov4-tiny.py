import rclpy
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge

bridge = CvBridge()
video = cv.VideoCapture(0)
video.set(cv.CAP_PROP_FRAME_WIDTH, 800)
video.set(cv.CAP_PROP_FRAME_HEIGHT, 450)
cam_pub = None

net = cv.dnn.readNet("/home/cyros/yolo-test/yolov4-tiny.weights", "/home/cyros/yolo-test/yolov4-tiny.cfg")
model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)
classes = []
with open("/home/cyros/yolo-test/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

def on_image_detect():
    global cam_pub
    global classes
    global model
    frame = video.read()[1]
    frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]
        color = [0, 255, 0]
        cv.putText(frame, class_name, (x, y - 10), cv.FONT_HERSHEY_PLAIN, 3, color, 2)
        cv.rectangle(frame, (x, y), (x + w, y + h), color, 3)
    msg = bridge.cv2_to_imgmsg(frame)
    cam_pub.publish(msg)
 
def main(args=None): 
    global cam_pub
    rclpy.init(args=None)
    cam = rclpy.create_node('cam')
    cam_pub = cam.create_publisher(Image,"/Einstein/cam", 1)
    cam.create_timer(0.033, on_image_detect)
    while True: rclpy.spin(cam)

if __name__ == '__main__': main()
