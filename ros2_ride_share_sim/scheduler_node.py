#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class SchedulerNode(Node):
    def __init__(self):
        super().__init__('scheduler')
        self.sub = self.create_subscription(String, '/ride_requests', self.request_callback, 10)
        self.pub = self.create_publisher(String, '/assignments', 10)
        self.available_drivers = ["A", "B", "C"]

    def request_callback(self, msg):
        if not self.available_drivers:
            self.get_logger().warn("No drivers available!")
            return
        driver = random.choice(self.available_drivers)
        assign = String()
        assign.data = f"{msg.data} -> Assigned to Driver {driver}"
        self.pub.publish(assign)
        self.get_logger().info(assign.data)

def main(args=None):
    rclpy.init(args=args)
    node = SchedulerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
