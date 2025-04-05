import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloSubscriber(Node):
    def __init__(self):
        #name of the node
        super().__init__("subscriber")

        #create subscription to the topic 'hello_topic' to receive the messages
        self.subscriber=self.create_subscription(String,"hello_topic",self.subscriber_callback,10) 
        
    #callback function to process the incoming messages
    def subscriber_callback(self,msg):
        self.get_logger().info(f'Received Message : "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = HelloSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()