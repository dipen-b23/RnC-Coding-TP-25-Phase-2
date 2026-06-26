
import rclpy
from rclpy.node import Node
import random
from smart_home_interfaces.msg import RoomTemp

class TemperatureSensorNode(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher_ = self.create_publisher(RoomTemp, 'room_temperature', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.current_temp = 24.0
        self.get_logger().info('Temperature Sensor Node has been started.')

    def timer_callback(self):
        self.current_temp += random.uniform(-0.4, 0.6)
        msg = RoomTemp()
        msg.temperature = self.current_temp
        msg.room_name = "Living Room"
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.temperature:.2f}°C in {msg.room_name}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
