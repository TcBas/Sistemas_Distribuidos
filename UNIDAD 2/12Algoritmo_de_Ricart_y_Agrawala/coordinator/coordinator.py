import time
import random
import sys
from time import sleep

class Coordinator:
    def __init__(self, process_count):
        self.process_count = process_count
        self.requests = [False] * process_count
        self.timestamp = [0] * process_count
        self.granted = [False] * process_count

    def request_access(self, process_id):
        self.timestamp[process_id] = random.randint(1, 100)  # Simula la hora del reloj lógico
        self.requests[process_id] = True
        print(f"Process {process_id} is requesting the critical section at timestamp {self.timestamp[process_id]}")

        # Proceso de aprobación, puede ser bloqueante o con espera
        self.grant_access(process_id)

    def grant_access(self, requesting_process_id):
        for i in range(self.process_count):
            if self.requests[i] and self.timestamp[i] < self.timestamp[requesting_process_id]:
                print(f"Process {i} has granted access to process {requesting_process_id}")
                self.granted[requesting_process_id] = True

    def release_access(self, process_id):
        self.requests[process_id] = False
        self.granted[process_id] = False
        print(f"Process {process_id} has finished using the critical section and released access.")

    def run(self):
        while True:
            # Aquí podrías agregar lógica de espera y otras condiciones
            time.sleep(2)


if __name__ == "__main__":
    coordinator = Coordinator(process_count=5)
    coordinator.run()