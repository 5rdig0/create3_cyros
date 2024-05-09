import rclpy
from rclpy.node import Node
import numpy as np
from rclpy.action import ActionClient
from irobot_create_msgs.action import RotateAngle
from irobot_create_msgs.action import DriveDistance
from irobot_create_msgs.action import DriveArc
from irobot_create_msgs.msg import IrIntensity
import rclpy.waitable

class TranslationActionClient(Node):
    def __init__(self):
        super().__init__('translation_action_client')
        self._action_client = ActionClient(self, DriveDistance, 'Einstein/drive_distance')
    def send_goal(self, action):
        goal_msg = DriveDistance.Goal()
        goal_msg._distance = action.distance
        goal_msg._max_translation_speed = action.max_translation_speed
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)      
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    def get_result_callback(self, future): rclpy.shutdown()

class RotationActionClient(Node):
    def __init__(self):
        super().__init__('rotation_action_client')
        self._action_client = ActionClient(self, RotateAngle, 'Einstein/rotate_angle')
    def send_goal(self, action):
        goal_msg = RotateAngle.Goal()
        goal_msg._angle = action.angle
        goal_msg._max_rotation_speed = action.max_rotation_speed
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)      
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    def get_result_callback(self, future): rclpy.shutdown()

class ArcActionClient(Node):
    def __init__(self):
        super().__init__('arc_action_client')
        self._action_client = ActionClient(self, DriveArc, 'Einstein/drive_arc')
    def send_goal(self, action):
        goal_msg = DriveArc.Goal()
        goal_msg._angle = action.angle
        goal_msg._radius = action.radius
        goal_msg._translate_direction = action.translate_direction
        goal_msg._max_translation_speed = action.max_translation_speed
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)      
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    def get_result_callback(self, future): rclpy.shutdown()
        

#ros2 topic echo /ir_intensity
class IRSub(Node):
    def __init__(self):
        super().__init__('Ir_subscriber_node')
        self.subs = self.create_subscription(
            IrIntensity, '/Einstein/ir_intensity',
            self.listener_callback, 10)
        self.subscription
    def listener_callback(self, msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rad = 2*np.pi
    Procedure = [
        ((0.0, 0.29*rad)),
        ((1.4, 0.0*rad)),
        ((0.0, 0.25*rad)),
        ((1.7, 0.0*rad)),
        ((0.0, 0.25*rad)),
        ((0.3, 0.0*rad))
    ]
     
    Square_dodge = [
        ((0.0, -0.25*rad)),
        ((0.4, 0.0*rad)),
        ((0.0, 0.25*rad)),
        ((0.8, 0.0*rad)),
        ((0.0, 0.25*rad)),
        ((0.4, 0.0*rad)),
        ((0.0, -0.25*rad))
    ]

    class rotation():
        def __init__(self):
            self.angle = str(Procedure[i][1])
            self.max_rotation_speed = 0.5
        def client(Procedure):
            action_client = RotationActionClient()
            rotation.angle = Procedure[1]
            rotation.max_rotation_speed = 0.9
            return(action_client)
        
    class translation():
        def __init__(self):
            self.distance = Procedure[i][0]
            self.max_translation_speed = 0.2
        def client(Procedure):
            action_client = TranslationActionClient()
            translation.distance = Procedure[0]
            translation.max_translation_speed = 0.3
            return(action_client)
        
    class arc():
        def __init__(self):
            self.angle = Procedure[i][1]
            self.radius = Procedure[i][0]     
            self.translate_direction = 1      
            self.max_translation_speed = 0.2    
        def client(Procedure):
            action_client = ArcActionClient()
            arc.angle = Procedure[1]
            arc.radius = Procedure[0] 
            arc.translate_direction = 1 
            arc.max_translation_speed = 0.3   
            return(action_client)   
           
    for i in range(len(Procedure)):
        rclpy.init(args=args)
        if Procedure[i][0] == 0.0: 
            action_client = rotation.client(Procedure[i])
            action_client.send_goal(rotation)
        elif Procedure[i][1] == 0.0: 
            action_client = translation.client(Procedure[i])
            action_client.send_goal(translation)
        else:
            action_client = arc.client(Procedure[i])
            action_client.send_goal(arc)
        rclpy.spin(action_client)
        print("Sucess in procedure",i+1)
if __name__ == '__main__': main()

