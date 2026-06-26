
import rclpy
from rclpy.node import Node
from smart_home_interfaces.srv import TogglePlug

class SmartPlugNode(Node):
    def __init__(self):
        super().__init__('smart_plug_controller')
        self.srv = self.create_service(TogglePlug, 'toggle_smart_plug', self.handle_toggle_plug)
        self.plug_state = False  # False = OFF, True = ON
        self.get_logger().info('Smart Plug Controller Node has been started.')

    def handle_toggle_plug(self, request, response):
        if request.turn_on != self.plug_state:
            self.plug_state = request.turn_on
            state_str = "ON" if self.plug_state else "OFF"
            self.get_logger().info(f'⚡ Smart Plug state CHANGED to: {state_str}')
        else:
            state_str = "ON" if self.plug_state else "OFF"
            self.get_logger().info(f'Smart Plug is already {state_str}. No action needed.')

        response.success = True
        response.message = f'Plug status updated to {state_str}'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SmartPlugNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
