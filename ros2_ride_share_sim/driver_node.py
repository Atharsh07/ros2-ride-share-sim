#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class DriverNode(Node):
    def __init__(self, driver_id):
        super().__init__(f"driver_{driver_id}")
        self.sub = self.create_subscription(String, '/assignments', self.assignment_callback, 10)
        self.driver_id = driver_id

    def assignment_callback(self, msg):
        self.get_logger().info(f"Driver {self.driver_id} assigned: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    import sys
    driver_id = sys.argv[1] if len(sys.argv) > 1 else "Y"
    node = DriverNode(driver_id)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
