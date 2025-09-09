from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='ros2_ride_share_sim',
             executable='scheduler_node.py',
             output='screen'),
        Node(package='ros2_ride_share_sim',
             executable='driver_node.py',
             arguments=['A'],
             output='screen'),
        Node(package='ros2_ride_share_sim',
             executable='driver_node.py',
             arguments=['B'],
             output='screen'),
        Node(package='ros2_ride_share_sim',
             executable='rider_node.py',
             arguments=['1'],
             output='screen'),
        Node(package='ros2_ride_share_sim',
             executable='rider_node.py',
             arguments=['2'],
             output='screen'),
    ])
