import rclpy
from rclpy.node import Node


class AgvFmsControl(Node):

    def __init__(self):
        super().__init__('agv_fms_control')
        self.get_logger().info('agv_fms_control node started')


def main(args=None):
    rclpy.init(args=args)
    node = AgvFmsControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()