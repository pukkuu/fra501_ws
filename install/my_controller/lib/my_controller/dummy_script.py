#!/usr/bin/python3

# from my_controller.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
from my_controller_interfaces.srv import SetTarget
import math

class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.pub_cmdvel = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_subscription(Point, "/mouse_position", self.mouse_position_callback, 10)
        self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.spawn_pizza_client = self.create_client(GivePosition, "spawn_pizza")
        self.eat_pizza_client = self.create_client(Empty, "turtle1/eat")
        self.create_service(SetTarget, "my_controller/p2p_eat", self.p2p_eat_callback)
        self.create_timer(0.01, self.timer_callback)
        self.target = [0.0, 0.0]
        self.current_pose = [0.0, 0.0, 0.0]
        self.enable_controller = False
        self.Kp_dis = 2.5
        self.Kp_ori = 5

    def p2p_eat_callback(self, request, response):
        if self.enable_controller == True:
            response.result = False
        else:
            self.target = [request.target.x, request.target.y]
            self.spawn_pizza(self.target)
            self.enable_controller = True
            response.result = True
        return response

    def spawn_pizza(self, position):
        position_request = GivePosition.Request()
        position_request.x = position[0]
        position_request.y = position[1]
        self.spawn_pizza_client.call_async(position_request)

    def pose_callback(self, msg):
        self.current_pose[0] = msg.x
        self.current_pose[1] = msg.y
        self.current_pose[2] = msg.theta

    def mouse_position_callback(self, msg):
        self.target[0] = msg.x
        self.target[1] = msg.y
        self.spawn_pizza([msg.x, msg.y])
        self.enable_controller = True

    def cmd_vel(self, vx, w):
        cmd_vel = Twist()
        cmd_vel.linear.x = vx
        cmd_vel.angular.z= w
        self.pub_cmdvel.publish(cmd_vel)

    def timer_callback(self):
        if self.enable_controller:
            dy = self.target[1] - self.current_pose[1]
            dx = self.target[0] - self.current_pose[0]

            e_dis = math.hypot(dx, dy)
            e_ori = math.atan2(dy, dx) - self.current_pose[2]
            e_ori = math.atan2(math.sin(e_ori), math.cos(e_ori))

            u_dis = self.Kp_dis * e_dis
            u_ori = self.Kp_ori * e_ori

            if (abs(dx) < 0.1 and abs(dy) < 0.1):
                self.cmd_vel(0.0, 0.0)
                self.eat_pizza_client.call_async(Empty.Request())
                self.enable_controller = False
            else:
                self.cmd_vel(u_dis, u_ori)


def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()