#!/usr/bin/python3

from my_controller.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.pub_cmdvel = self.create_publisher(Twist)
        self.create_timer(0.01, self.timer_callback)

    def timer_callback(self):
        print("Hello")
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
