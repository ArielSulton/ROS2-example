import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data, qos_profile_services_default
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('pubs_py')
        self.publisher = self.create_publisher(String, 'topic', qos_profile_services_default)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(MinimalPublisher())
    MinimalPublisher().destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()