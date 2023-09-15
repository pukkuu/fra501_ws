#!/usr/bin/python3

# from my_controller.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
import math

class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.pub_cmdvel = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_subscription(Point, "/mouse_position", self.mouse_position_callback, 10)
        self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.create_timer(0.01, self.timer_callback)
        self.target = [0.0, 0.0, 0.0]
        self.current_pose = [0.0, 0.0, 0.0]
        self.target_theta = [0.0, 0.0]
        self.theta = [0.0, 0.0]

    def pose_callback(self, msg):
        self.current_pose[0] = msg.x
        self.current_pose[1] = msg.y
        self.current_pose[2] = msg.theta


    def mouse_position_callback(self, msg):
        self.target[0] = msg.x
        self.target[1] = msg.y
        self.target[2] = msg.z
        print(self.target)

    def cmd_vel(self, vx, w):
        cmd_vel = Twist()
        cmd_vel.linear.x = vx
        cmd_vel.angular.z= w
        self.pub_cmdvel.publish(cmd_vel)

    def timer_callback(self):
        dy = self.target[1] - self.current_pose[1]
        dx = self.target[0] - self.current_pose[0]

        self.theta[0] = self.current_pose[2]
        if self.theta[0] - self.theta[1] > math.pi:
            self.theta[0] = self.theta[0] - (2 * math.pi)
        elif self.theta[0] - self.theta[1] < -math.pi:
            self.theta[0] = self.theta[0] + (2 * math.pi)
        self.theta[1] = self.theta[0]
            
        self.target_theta[0] = math.atan2(dy, dx)
        if self.target_theta[0] - self.target_theta[1] > math.pi:
            self.target_theta[0] = self.target_theta[0] - (2 * math.pi)
        elif self.target_theta[0] - self.target_theta[1] < -math.pi:
            self.target_theta[0] = self.target_theta[0] + (2 * math.pi)
        self.target_theta[1] = self.target_theta[0]

        distance_error = math.sqrt(pow(dx, 2) + pow(dy, 2))
        theta_error = self.target_theta[0] - self.theta[0]

        vel_x = 2.5 * distance_error
        w_z = 5 * theta_error

        if (abs(dx) < 0.001 and abs(dy) < 0.001):
            self.cmd_vel(0.0, 0.0)
        else:
            self.cmd_vel(vel_x, w_z)


def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()