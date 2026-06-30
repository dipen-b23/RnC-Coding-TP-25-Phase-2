import rclpy
from rclpy.node import Node
from smart_home_interfaces.msg import RoomTemperature
import random


class TemperatureSensor(Node):

    def __init__(self):
        super().__init__('temperature_sensor')

        self.declare_parameter('room_name', 'Living Room')
        self.room_name = self.get_parameter('room_name').value

        self.publisher_ = self.create_publisher(RoomTemperature, 'room_temperature', 10)
        self.timer_ = self.create_timer(1.0, self.publish_temperature)

    def publish_temperature(self):
        msg = RoomTemperature()
        msg.room_name = self.room_name
        msg.temperature = round(random.uniform(18.0, 32.0), 1)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.room_name} -> {msg.temperature}°C')


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
