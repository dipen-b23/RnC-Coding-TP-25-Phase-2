import rclpy
from rclpy.node import Node
import random
from smart_home_interfaces.msg import Temperature

class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher_ = self.create_publisher(Temperature, 'room_temperature', 10)
        self.timer = self.create_timer(2.0, self.timer_callback) # Publish every 2 seconds
        self.get_logger().info('Temperature Sensor Node has started.')

    def timer_callback(self):
        msg = Temperature()
        # Simulate a fluctuating temperature around 25-31 degrees
        msg.temperature = round(random.uniform(24.0, 32.0), 1)
        msg.room = "Living Room"
        msg.stamp = self.get_clock().now().to_msg()
        
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.temperature}°C in {msg.room}")

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
