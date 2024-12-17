import random
import time

class LamportClock:
    def __init__(self):
        # Inicializamos el reloj con valor 0
        self.clock = 0

    def increment(self):
        # Incrementamos el reloj local
        self.clock += 1
        return self.clock

    def receive_message(self, other_clock):
        # Al recibir un mensaje, actualizamos el reloj a max(clock_local, clock_other) + 1
        self.clock = max(self.clock, other_clock) + 1
        return self.clock

    def send_message(self):
        # Cuando un proceso envía un mensaje, incrementa su reloj
        return self.increment()

    def __str__(self):
        # Función para mostrar el reloj de Lamport
        return f'Reloj Lamport: {self.clock}'


def simulate_event():
    # Creamos dos instancias del reloj de Lamport (para dos procesos)
    process_A = LamportClock()
    process_B = LamportClock()

    # Simulación de un evento en el que ambos procesos envían y reciben mensajes
    print(f"Inicializando proceso A: {process_A}")
    print(f"Inicializando proceso B: {process_B}")
    
    # Proceso A envía un mensaje a B
    print(f"\nProceso A envía mensaje a B: {process_A.send_message()}")
    time.sleep(random.uniform(0.5, 1.5))  # Simula un pequeño retraso
    
    # Proceso B recibe el mensaje de A
    print(f"Proceso B recibe mensaje de A y actualiza su reloj: {process_B.receive_message(process_A.clock)}")
    
    # Proceso B responde a A
    print(f"\nProceso B envía mensaje a A: {process_B.send_message()}")
    time.sleep(random.uniform(0.5, 1.5))  # Simula un pequeño retraso

    # Proceso A recibe el mensaje de B
    print(f"Proceso A recibe mensaje de B y actualiza su reloj: {process_A.receive_message(process_B.clock)}")
    
    print(f"\nEstado final de los procesos:\n{process_A}\n{process_B}")


if __name__ == '__main__':
    simulate_event()
