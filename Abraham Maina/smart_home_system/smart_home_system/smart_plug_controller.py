import rclpy
from rclpy.node import Node
from smart_home_interfaces.srv import SmartPlugControl


class SmartPlugController(Node):

    def __init__(self):
        super().__init__('smart_plug_controller')
        self.plug_state = 'OFF'
        self.srv_ = self.create_service(SmartPlugControl, 'smart_plug_control', self.handle_request)
        self.get_logger().info('Smart Plug Controller ready. Initial state: OFF')

    def handle_request(self, request, response):
        self.plug_state = request.action

        response.success = True
        response.message = f'Plug turned {self.plug_state} (triggered by {request.temperature}°C)'

        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = SmartPlugController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
