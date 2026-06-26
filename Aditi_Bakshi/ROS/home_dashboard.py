import rclpy
from rclpy.node import Node
from smart_home_interfaces.msg import Temperature
from std_srvs.srv import SetBool

class HomeDashboard(Node):
    def __init__(self):
        super().__init__('home_dashboard')
        self.subscription = self.create_subscription(
            Temperature, 'room_temperature', self.listener_callback, 10)
        
        self.client = self.create_client(SetBool, 'plug_control')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for Smart Plug service to become available...')
            
        self.current_plug_state = None # Keep track of local target state
        self.get_logger().info('Home Dashboard Node has started.')

    def listener_callback(self, msg):
        self.get_logger().info(f"Dashboard Feed -> Room: {msg.room} | Temp: {msg.temperature}°C")
        
        # Rule Evaluation
        if msg.temperature > 28.0 and self.current_plug_state != True:
            self.get_logger().warn(f"High temperature detected ({msg.temperature}°C)! Triggering Smart Plug ON...")
            self.call_plug_service(True)
        elif msg.temperature < 26.0 and self.current_plug_state != False:
            self.get_logger().info(f"Cool temperature detected ({msg.temperature}°C). Turning Smart Plug OFF...")
            self.call_plug_service(False)

    def call_plug_service(self, state):
        request = SetBool.Request()
        request.data = state
        self.current_plug_state = state # Optimistically update state tracking
        
        future = self.client.call_async(request)
        future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Service Response: {response.message}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = HomeDashboard()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
