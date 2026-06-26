
import rclpy
from rclpy.node import Node
from smart_home_interfaces.msg import RoomTemp
from smart_home_interfaces.srv import TogglePlug

class HomeDashboardNode(Node):
    def __init__(self):
        super().__init__('home_dashboard')
        
        self.subscription = self.create_subscription(
            RoomTemp,
            'room_temperature',
            self.listener_callback,
            10
        )
        
        self.client = self.create_client(TogglePlug, 'toggle_smart_plug')
        
        self.upper_threshold = 26.5
        self.lower_threshold = 24.5
        self.last_sent_state = None  
        
        self.get_logger().info(f'Dashboard online. Rules: ON > {self.upper_threshold}°C | OFF < {self.lower_threshold}°C')

    def listener_callback(self, msg):
        self.get_logger().info(f'📊 Dashboard Metric: {msg.temperature:.2f}°C [{msg.room_name}]')
        
        if msg.temperature > self.upper_threshold and self.last_sent_state != True:
            self.get_logger().warning(f'Threshold broken ({msg.temperature:.2f}°C)! Sending Request: Turn ON.')
            self.call_plug_service(True)
        elif msg.temperature < self.lower_threshold and self.last_sent_state != False:
            self.get_logger().info(f'Environment stabilized ({msg.temperature:.2f}°C). Sending Request: Turn OFF.')
            self.call_plug_service(False)

    def call_plug_service(self, turn_on):
        if not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error('Service backend unavailable!')
            return
        
        request = TogglePlug.Request()
        request.turn_on = turn_on
        
        future = self.client.call_async(request)
        future.add_done_callback(lambda fut: self.handle_service_response(fut, turn_on))

    def handle_service_response(self, future, intended_state):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(f'Acknowledge: {response.message}')
                self.last_sent_state = intended_state
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = HomeDashboardNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
