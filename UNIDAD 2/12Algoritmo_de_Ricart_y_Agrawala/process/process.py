import time
import random
import sys
from time import sleep

class Process:
    def __init__(self, process_id, coordinator):
        self.process_id = process_id
        self.coordinator = coordinator

    def request_token(self):
        print(f"Process {self.process_id} is requesting the token.")
        self.coordinator.request_access(self.process_id)

    def access_critical_section(self):
        print(f"Process {self.process_id} is accessing the critical section.")
        time.sleep(random.randint(1, 3))  # Simula trabajar en la sección crítica
        print(f"Process {self.process_id} has finished using the critical section.")

    def run(self):
        while True:
            self.request_token()
            sleep(5)  # Simula esperar antes de solicitar nuevamente


if __name__ == "__main__":
    process_id = int(sys.argv[1])  # Toma el ID del proceso desde los argumentos
    coordinator = sys.argv[2]  # Coordenador sería algo como 'localhost:5000'
    process = Process(process_id, coordinator)
    process.run()
