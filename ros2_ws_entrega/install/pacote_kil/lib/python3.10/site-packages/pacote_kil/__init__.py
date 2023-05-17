# Importando bibliotecas
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from time import sleep
import math

# Criando lista de coordenadas (variável global)
coordenadas = []

# Criando classe TurtleController
class TurtleController(Node):
    
    # Método construtor
    def __init__(self, coordenadas):
        super().__init__('subscriber_node')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        self.local = 0
        self.point_list = coordenadas
        self.condicao = True
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.listener_callback,
            qos_profile=4)
        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=self.publisher_callback)
        
    # Método para receber as coordenadas
    def listener_callback(self, msg):
            self.x = msg.pose.pose.position.x
            self.y = msg.pose.pose.position.y
            orientation = msg.pose.pose.orientation
            _,_,self.theta = euler_from_quaternion([orientation.x,orientation.y,orientation.z,orientation.w])
            #self.get_logger().info(f"x={self.x:3f}, y={self.y:3f}")
            
    # Método para publicar as coordenadas
    def publisher_callback(self):
        posicao = Point()
        msg = Twist()
        if self.condicao == True:
            resposta = input("Deseja iniciar a trajetória? (y/n): ")
            if resposta == 'y':
                valor_coord = float(input("Digite a coordenada: "))
                valor_giro = int(input("Digite o valor do angulo em graus: "))
                if valor_giro != 0:
                    msg.angular.z = math.radians(valor_giro)
                    self.publisher.publish(msg)
                    sleep(2)
                    msg.angular.z = 0.0
                    self.publisher.publish(msg)
                self.point_list.append(valor_coord)
                self.condicao = False
            else:
                self.condicao = True
                self.angulo = False
                
        posicao.x = self.point_list[self.local]
        caminho_x = posicao.x - self.x
        
        if self.x <=  posicao.x and caminho_x >= 0.2:
            msg.linear.x = 0.5
        elif self.x >=  posicao.x and caminho_x <= 0.2:
            msg.linear.x = -0.5
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.local = 0 if (len(self.point_list) == self.local + 1) else (self.local + 1)
            self.condicao = True
        print(f'Coordenada atual: {round(self.x, 2)} -- Faltando para chegar:{round(caminho_x, 2)}')
        self.publisher.publish(msg)
        
# Função principal
def hello_world(args=None):
    rclpy.init(args=args)
    subscriber_node = TurtleController(coordenadas)
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    hello_world()