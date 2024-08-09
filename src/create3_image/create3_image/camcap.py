import cv2 as cv
import pyrealsense2 as rs
import numpy as np 

class DepthCamera:
    def __init__(self):
        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
        self.pipeline.start(config)

    def get_frame(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        if not depth_frame or not color_frame:
            return False, None, None
        return True, depth_image, color_image

dc = DepthCamera()
i = 0

def draw_circle(event,x,y,flags,param):
    cv.putText(rgb, str(int(depth[y, x]/10)) + " cm", (x,y), 1, 1.5, (0, 255, 0), 1, 1)
    cv.putText(rgb, str(str(int(hsv[y, x][0])) + ", "+ str(int(hsv[y, x][1])) + ", " + str(int(hsv[y, x][2]))), (x,y+30), 1, 1.5, (0, 255, 0), 1, 1)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

def detect(mask):
    size = 10
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(size,size))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    contours, h = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(rgb, contours, -1, (0, 255, 0), 2, 1, offset = (2,2), hierarchy = h, maxLevel= 0)
    for cnt in contours:
        moment = cv.moments(cnt)
        if moment["m00"] != 0:
            cx, cy = int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"])
            cv.putText(rgb, str(int(depth[cy, cx]/10)) + " cm", (cx,cy), 1, 1.5, (0, 255, 0), 1, 1)

while True:
    ret, depth, rgb = dc.get_frame()
    min, max = np.min(depth), np.max(np.where(depth < 6000))
    depth = cv.medianBlur(depth, 5)
    depth_interp = np.interp(depth, [min, max], [0, 255]).astype(np.uint8)
    depth_color = cv.applyColorMap(depth_interp, cv.COLORMAP_AUTUMN)

    hsv = cv.cvtColor(rgb, cv.COLOR_BGR2HSV)
    #Blue
    maskb = cv.inRange(hsv, (80, 180, 150), (120, 255, 220))
    #Orange
    masko = cv.inRange(hsv, (0, 150, 150), (50, 240, 255))
    #Pink
    maskp1 = cv.inRange(hsv, (0, 100, 140), (30, 150, 255))
    maskp2 = cv.inRange(hsv, (150, 100, 200), (200, 170, 255))
    maskp = cv.bitwise_or(maskp1, maskp2)

    detect(maskb)
    detect(masko)
    detect(maskp)

    key = cv.waitKey(1)
    print("Running")
    # cv.imshow('image',rgb)
    # cv.imshow("depth",depth_color)
    if cv.waitKey(1) == ord('q'): break
    # if key == ord('s'):
    #     cv.imwrite("{}rgb.png".format(i),rgb)
    #     cv.imwrite("{}depth.png".format(i),depth)
    #     i+=1

cv.destroyAllWindows()

