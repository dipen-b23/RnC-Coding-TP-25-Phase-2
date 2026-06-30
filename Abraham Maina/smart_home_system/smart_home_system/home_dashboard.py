import rclpy
from rclpy.node import Node
from smart_home_interfaces.msg import RoomTemperature
from smart_home_interfaces.srv import SmartPlugControl


class HomeDashboard(Node):

    def __init__(self):
        super().__init__('home_dashboard')

        self.declare_parameter('threshold', 26.0)
        self.threshold = self.get_parameter('threshold').value

        self.plug_state = 'OFF'

        self.subscription_ = self.create_subscription(
            RoomTemperature, 'room_temperature', self.temperature_callback, 10)

        self.client_ = self.create_client(SmartPlugControl, 'smart_plug_control')

    def temperature_callback(self, msg):
        self.get_logger().info(f'Dashboard received: {msg.room_name} -> {msg.temperature}°C')

        if msg.temperature > self.threshold and self.plug_state != 'ON':
            self.call_plug_service('ON', msg.temperature)
        elif msg.temperature <= self.threshold and self.plug_state != 'OFF':
            self.call_plug_service('OFF', msg.temperature)

    def call_plug_service(self, action, temperature):
        if not self.client_.service_is_ready():
            self.get_logger().warn('Smart plug service not available yet')
            return

        request = SmartPlugControl.Request()
        request.action = action
        request.temperature = temperature

        future = self.client_.call_async(request)
        future.add_done_callback(self.service_response_callback)
        self.plug_state = action

    def service_response_callback(self, future):
        response = future.result()
        self.get_logger().info(f'Service response: {response.message}')


def main(args=None):
    rclpy.init(args=args)
    node = HomeDashboard()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
