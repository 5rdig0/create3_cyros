from piservo import Servo
import time


myservo = Servo(27,0,180,1.5,7,50)

myservo.write(90)
time.sleep(1)
myservo.write(0)
time.sleep(1)
myservo.stop()

