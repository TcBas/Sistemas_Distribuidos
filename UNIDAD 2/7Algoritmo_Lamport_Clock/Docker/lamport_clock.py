import time
import random
import sys
import socket

class LamportClock:
    def __init__(self, process_id):
        self.time = 0
        self.process_id = process_id

    def send_message(self, other_process_ip, other_process_port):
        # Incrementa el reloj antes de enviar el mensaje
        self.time += 1
        message = f"Process {self.process_id} sending message at time {self.time}"
        print(message)
        
        # Configura el socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (other_process_ip, other_process_port))
        sock.close()

    def receive_message(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', 0))  # Enlaza al puerto aleatorio disponible
        print(f"Process {self.process_id} waiting for message...")
        data, addr = sock.recvfrom(1024)
        sock.close()
        
        # Ajusta el reloj cuando recibe un mensaje
        timestamp = int(data.decode().split(' ')[-1])
        self.time = max(self.time, timestamp) + 1
        print(f"Process {self.process_id} received message at time {self.time}")

def main(process_id, other_ip, other_port):
    clock = LamportClock(process_id)
    for i in range(5):  # 5 interacciones de mensajes
        time.sleep(random.uniform(0.5, 1.5))  # Simula un retardo entre las interacciones
        clock.send_message(other_ip, other_port)
        clock.receive_message()

if __name__ == "__main__":
    process_id = int(sys.argv[1])
    other_ip = sys.argv[2]
    other_port = int(sys.argv[3])
    main(process_id, other_ip, other_port)
