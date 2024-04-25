import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

import time
import numpy as np
from rclpy.action import ActionClient
from irobot_create_msgs.action import RotateAngle
from irobot_create_msgs.action import DriveDistance
from irobot_create_msgs.action._drive_distance import DriveDistance_SendGoal
from irobot_create_msgs.action import DriveArc
from irobot_create_msgs.msg import LedColor
from irobot_create_msgs.msg import LightringLeds

class MovementActionServer(Node):

    def __init__(self):
        super().__init__('movement_action_server')
        self._action_server = ActionServer(
            self,
            DriveDistance,
            'movement',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = DriveDistance.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = DriveDistance.Result()
        result.sequence = feedback_msg.partial_sequence
        return result


def main(args=None):
    rclpy.init(args=args)

    movement_action_server = MovementActionServer()

    rclpy.spin(movement_action_server)


if __name__ == '__main__':
    main()