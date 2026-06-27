import rclpy
from rclpy.node import Node
from smart_home_interfaces.srv import SetPlugState


class SmartPlugController(Node):

    def __init__(self):
        super().__init__('smart_plug_controller')
        self.srv = self.create_service(SetPlugState, 'set_plug_state', self.set_plug_state_callback)
        self.plug_state = 'OFF'

    def set_plug_state_callback(self, request, response):
        if request.turn_on:
            self.plug_state = 'ON'
        else:
            self.plug_state = 'OFF'

        response.success = True
        response.curr_state = self.plug_state
        response.msg = 'Plug turned %s' % self.plug_state

        self.get_logger().info('Plug state changed to: %s' % self.plug_state)
        return response


def main(args=None):
    rclpy.init(args=args)
    smart_plug_controller = SmartPlugController()
    rclpy.spin(smart_plug_controller)
    smart_plug_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
