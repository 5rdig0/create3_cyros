import rclpy
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge

bridge = CvBridge()
video = cv.VideoCapture(0)
video.set(cv.CAP_PROP_FRAME_WIDTH, 800)
video.set(cv.CAP_PROP_FRAME_HEIGHT, 450)
cam_pub = None

def on_image_detect():
    global cam_pub
    frame = video.read()[1]
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV_FULL)
    frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)
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