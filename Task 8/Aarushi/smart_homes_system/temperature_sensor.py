import rclpy
from rclpy.node import Node
from smart_home_interfaces.msg import TempReading
import random


class TemperatureSensor(Node):

    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher_ = self.create_publisher(TempReading, 'temperature', 10)
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = TempReading()
        msg.room_name = 'Living Room'
        msg.temperature = random.uniform(18.0, 32.0)
        msg.stamp = self.get_clock().now().to_msg()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%.2f" C' % msg.temperature)


def main(args=None):
    rclpy.init(args=args)
    temperature_sensor = TemperatureSensor()
    rclpy.spin(temperature_sensor)
    temperature_sensor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
