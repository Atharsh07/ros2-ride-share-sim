#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random, time

class RiderNode(Node):
    def __init__(self, rider_id):
        super().__init__(f"rider_{rider_id}")
        self.publisher = self.create_publisher(String, '/ride_requests', 10)
        self.timer = self.create_timer(5.0, self.request_ride)  # every 5 sec
        self.rider_id = rider_id

    def request_ride(self):
        msg = String()
        msg.data = f"Rider {self.rider_id} requests ride at loc {random.randint(0,10)}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Sent: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    import sys
    rider_id = sys.argv[1] if len(sys.argv) > 1 else "X"
    node = RiderNode(rider_id)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
