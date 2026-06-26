import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class SmartPlugController(Node):
    def __init__(self):
        super().__init__('smart_plug_controller')
        self.srv = self.create_service(SetBool, 'plug_control', self.handle_plug_control)
        self.plug_status = False # False = OFF, True = ON
        self.get_logger().info('Smart Plug Controller Service Server is ready.')

    def handle_plug_control(self, request, response):
        if request.data == self.plug_status:
            response.success = True
            status_str = "ON" if self.plug_status else "OFF"
            response.message = f"Plug is already {status_str}."
        else:
            self.plug_status = request.data
            status_str = "ON" if self.plug_status else "OFF"
            response.success = True
            response.message = f"Successfully turned the plug {status_str}."
            self.get_logger().info(f"STATUS CHANGE: Smart Plug turned {status_str}")
            
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SmartPlugController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
