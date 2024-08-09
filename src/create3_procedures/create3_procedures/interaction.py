import RPi.GPIO as GPIO
from time import sleep
from create3_msgs.msg import Armcontrol
import rclpy

class Servos(object):   
    def setup(self, pin, frequency, speed_min, speed_max, retracted, grab, release, dutycycle_min, dutycycle_max):
        self.pos = 0
        self.pin = pin
        self.frequency = frequency
        self.speed_min = speed_min
        self.speed_max = speed_max
        self.dutycycle_start = (dutycycle_min + dutycycle_max)/2
        self.dutycycle_min = dutycycle_min
        self.dutycycle_max = dutycycle_max
        self.retracted = retracted
        self.grab_box = grab
        self.grab_ball = self.grab_box
        self.grab_cilinder = self.grab_ball
        self.release_box = release
        self.release_ball = self.release_box
        self.release_cilinder = self.release_ball
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, self.frequency)
        self.servo.start(0)

    def angle_to_percent(self, angle) :
        if angle > 90 or angle < -90 :return False
        ratio = (self.dutycycle_max - self.dutycycle_min)/180 #Calcul ratio from angle to percent
        angle_as_percent = angle * ratio
        return self.dutycycle_start + angle_as_percent

    def move(self, angle):
        self.pos = angle
        self.servo.ChangeDutyCycle(self.angle_to_percent(self.pos))
        ratio = (self.speed_max - self.speed_min)/180
        sleep(self.speed_min + ratio*(abs(self.pos - angle)))

    def pega_cubo(self):
        self.move(self.grab_box)

    def pega_bola(self):
        self.move(self.grab_ball)

    def pega_cilindro(self):
        self.move(self.grab_cilinder)

    def solta_cubo(self):
        self.move(self.release_box)

    def solta_bola(self):
        self.move(self.release_ball)

    def solta_cilindro(self):
        self.move(self.release_cilinder)

    def retrai(self): self.move(self.retracted)

class Commands(object):
    def grab_box(self):
        self.retract()
        sleep(0.5)
        elbow.pega_cubo()
        wrist.pega_cubo()
        claw.pega_cubo()
        sleep(0.5)
        self.retract()

    def grab_cilinder(self):
        claw.pega_bola()
        elbow.pega_bola()
        wrist.pega_bola()

    def grab_ball(self):
        claw.pega_cilindro()
        elbow.pega_cilindro()
        wrist.pega_cilindro()

    def retract(self):
        claw.retrai()
        elbow.retrai()
        wrist.retrai()

class Callbacks(object):

    def claw_control(data):
        angle = data.pos
        time = data.time
        speed = data.speed
        if time: wrist.move(angle, time)
        if speed: wrist.move(angle, speed)

    def wrist_control(data):
        angle = data.pos
        time = data.time
        speed = data.speed
        if time: wrist.move(angle, time)
        if speed: wrist.move(angle, speed)

    def elbow_control(data):
        angle = data.pos
        time = data.time
        speed = data.speed
        if time: wrist.move(angle, time)
        if speed: wrist.move(angle, speed)

    def command_control(data):
        command = data.command
        if command == "grab_box": commands.grab_box()
        if command == "release_box": commands.release_box()
        if command == "grab_ball": commands.grab_box()
        if command == "release_ball": commands.grab_box()
        if command == "grab_cilinder": commands.grab_box()
        if command == "release_cilinder": commands.grab_box()

commands = Commands()
callbacks = Callbacks()

def main(args = None):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    rclpy.init()
    claw = Servos()
    claw.setup(pin = 13, frequency = 50,
               dutycycle_start = 1.5, dutycycle_min = 1, dutycycle_max = 2,
               retracted = 0, grab = -15, release = 15)
    wrist = Servos()
    wrist.setup(pin = 11, frequency = 50,
                dutycycle_start = 1.5, dutycycle_min = 1, dutycycle_max = 2, 
                retracted = 45, grab = 25, release = 25)
    elbow = Servos()
    elbow.setup(pin = 15, frequency = 50,
                dutycycle_start = 1.5, dutycycle_min = 1, dutycycle_max = 2,
                retracted = 60, grab = -30, release = -30)

    commands = Commands()
    callbacks = Callbacks()

    arm_control = rclpy.create_node("arm_control")
    arm_control.create_subscription(Armcontrol, "Einstein/arm/command", callbacks.command_control,1)
    arm_control.create_subscription(Armcontrol, "Einstein/arm/claw", callbacks.claw_control,1)
    arm_control.create_subscription(Armcontrol, "Einstein/arm/wrist", callbacks.wrist_control,1)
    arm_control.create_subscription(Armcontrol, "Einstein/arm/elbow", callbacks.elbow_control,1)
    rclpy.spin(arm_control)

#if __name__ == '__main__': main()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

claw = Servos()
claw.setup(pin = 13, frequency = 50, speed_min = 0.1, speed_max = 0.25,
           dutycycle_min = 1.5, dutycycle_max = 7,
           retracted = 0, grab = -30, release = 45)
wrist = Servos()
wrist.setup(pin = 15, frequency = 50,  speed_min = 0.3, speed_max = 1,
            dutycycle_min = 2.3, dutycycle_max = 12.2,
            retracted = 60, grab = 15, release = 15)
elbow = Servos()
elbow.setup(pin = 11, frequency = 50,  speed_min = 0.3, speed_max = 1,
            dutycycle_min = 2, dutycycle_max = 12,
            retracted = 55, grab = -70, release = 55)

commands.grab_box()

commands.grab_box()

GPIO.cleanup((11,13,15))

