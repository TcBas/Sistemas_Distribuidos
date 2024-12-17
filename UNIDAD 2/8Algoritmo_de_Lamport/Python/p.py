import matplotlib.pyplot as plt

class LamportClock:
    def __init__(self, name):
        self.name = name
        self.clock = 0
        self.history = []

    def increment(self):
        """Incrementa el reloj y guarda el estado."""
        self.clock += 1
        self.history.append(self.clock)

    def send_message(self):
        """Envía un mensaje con el valor del reloj."""
        return self.clock

    def receive_message(self, received_clock):
        """Recibe un mensaje y ajusta el reloj si es necesario."""
        self.clock = max(self.clock, received_clock) + 1
        self.history.append(self.clock)

# Simulación
def main():
    proceso_A = LamportClock("A")
    proceso_B = LamportClock("B")

    # Registro de los relojes
    proceso_A.increment()
    mensaje_A = proceso_A.send_message()

    proceso_B.receive_message(mensaje_A)
    proceso_B.increment()

    mensaje_B = proceso_B.send_message()
    proceso_A.receive_message(mensaje_B)
    proceso_A.increment()
    proceso_B.increment()

    # Graficar
    plt.plot(proceso_A.history, label="Proceso A")
    plt.plot(proceso_B.history, label="Proceso B")
    plt.xlabel("Eventos")
    plt.ylabel("Reloj lógico")
    plt.title("Algoritmo de Lamport - Relojes Lógicos")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
