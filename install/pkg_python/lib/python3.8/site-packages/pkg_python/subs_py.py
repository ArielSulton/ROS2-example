import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data, qos_profile_services_default
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('subs_py')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, qos_profile_services_default)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(MinimalSubscriber())
    MinimalSubscriber().destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()