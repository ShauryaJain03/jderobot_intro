import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class HelloPublisher(Node):
    def __init__(self):
        #name of the node
        super().__init__("publisher")

        #publish the message in String format to the topic 'hello_topic'
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        timer_period = 1.0 

        #publish the message every 1 second
        self.timer = self.create_timer(timer_period, self.timer_callback)

    #define the callback function which will be executed every 1 second
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello! ROS2 is fun'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Transmitted Message : "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = HelloPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()