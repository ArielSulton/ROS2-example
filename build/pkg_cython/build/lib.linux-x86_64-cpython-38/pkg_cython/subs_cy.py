import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('subs_cy')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(MinimalSubscriber())
    MinimalSubscriber().destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()