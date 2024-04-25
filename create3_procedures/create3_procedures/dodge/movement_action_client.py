import rclpy
from rclpy.node import Node
import numpy as np
from rclpy.action import ActionClient
from irobot_create_msgs.action import RotateAngle
from irobot_create_msgs.action import DriveDistance
from irobot_create_msgs.action._drive_distance import DriveDistance_SendGoal
from irobot_create_msgs.action import DriveArc
from irobot_create_msgs.msg import LedColor
from irobot_create_msgs.msg import LightringLeds


class MovementActionClient(Node):

    def __init__(self):
        super().__init__('Movement_action_client')
        self._action_client = ActionClient(self, DriveDistance, 'drivedistance')

    def send_goal(self, action):
        goal_msg = DriveDistance.Goal()
        goal_msg.action = action
        self._action_client.wait_for_server()
        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)
    rad = 2*np.pi
    Procedure = [
        ((0.0, -0.5*rad)),
        ((0.3, 0.0*rad)),
        ((0.0, 0.5*rad)),
        ((0.6, 0.0*rad)),
        ((0.0, 0.5*rad)),
        ((0.3, 0.0*rad)),
        ((0.0, -0.5*rad))
    ]
    #ros2 action send_goal /navigate_to_position irobot_create_msgs/action/NavigateToPosition 
    #"{achieve_goal_heading: true,goal_pose:{pose:{position:{x: 0,y: 0,z: 0.0}, orientation:{x: 0.0,y: 0.0, z: 0.0, w: 1.0}}}}"
    action_client = MovementActionClient()
    future = action_client.send_goal(
        "{achieve_goal_heading: true,goal_pose:{pose:{position:{x: 0.0,y: 0.0,z: 0.0},orientation:{x: 0.0,y: 0.0,z: 0.0,w:1.0}}}}"
        )
    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()