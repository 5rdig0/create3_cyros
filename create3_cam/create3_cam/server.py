#!/usr/bin/env python3
import rclpy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import signal, sys
from threading import Thread, Event
from flask import Flask, render_template, Response

frame = None # Global variable frame (the holy image)
bridge = CvBridge()
event = Event()

def on_image(msg):
    global frame
    cv_image = cv2.cvtColor(bridge.imgmsg_to_cv2(msg, msg.encoding), cv2.COLOR_BGR2RGB)
    frame = cv2.imencode(".jpg",cv_image)[1].tobytes()
    event.set()

rclpy.init(args=None)
node = rclpy.create_node('Show_image_python')
Thread(target=lambda:node).start() # Starting the Thread with a target in the node
subscription = node.create_subscription(Image,"/Einstein/cam", on_image, 10) # Creating the Subscribe node
app = Flask(__name__) # Initializing the Flask application

def get_frame():
    rclpy.spin_once(node)
    event.wait()
    event.clear()
    return frame

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed(): 
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def signal_handler(signal, frame):
    rclpy.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler) # Calls the 'signal_handler' and finish the actual signal (like a Ctrl + C)
 
def main(args=None): app.run(host='0.0.0.0', port=8080 ,debug=True)

if __name__ == '__main__': main()