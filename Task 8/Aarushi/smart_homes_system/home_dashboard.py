import rclpy
from rclpy.node import Node
from smart_home_interfaces.msg import TempReading
from smart_home_interfaces.srv import SetPlugState


class HomeDashboard(Node):

    def __init__(self):
        super().__init__('home_dashboard')
        self.subscription = self.create_subscription(
            TempReading, 'temperature', self.temperature_callback, 10)
        self.client = self.create_client(SetPlugState, 'set_plug_state')

        self.high_threshold = 27.0
        self.low_threshold = 20.0
        self.plug_currently_on = False

    def temperature_callback(self, msg):
        self.get_logger().info(
            '%s: %.2f C' % (msg.room_name, msg.temperature))

        if msg.temperature > self.high_threshold and not self.plug_currently_on:
            self.send_plug_request(True)
        elif msg.temperature < self.low_threshold and self.plug_currently_on:
            self.send_plug_request(False)

    def send_plug_request(self, turn_on):
        if not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('set_plug_state service not available')
            return

        request = SetPlugState.Request()
        request.turn_on = turn_on

        future = self.client.call_async(request)
        future.add_done_callback(self.plug_response_callback)

    def plug_response_callback(self, future):
        response = future.result()
        self.plug_currently_on = (response.curr_state == 'ON')
        self.get_logger().info(response.msg)


def main(args=None):
    rclpy.init(args=args)
    home_dashboard = HomeDashboard()
    rclpy.spin(home_dashboard)
    home_dashboard.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
