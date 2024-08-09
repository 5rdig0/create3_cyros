from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='create3_procedures',
            namespace='Einstein',
            executable='arm',
            name='arm'
        ),
        Node(
            package='create3_image',
            namespace='Einstein',
            executable='webcam',
            name='webcam'
        ),
        Node(
            package='create3_image',
            namespace='Einstein',
            executable='server',
            name='server'
        ),
        Node(
            package='create3_teleop',
            namespace='Einstein',
            executable='teleop',
            name='teleop'
        ),
    ])