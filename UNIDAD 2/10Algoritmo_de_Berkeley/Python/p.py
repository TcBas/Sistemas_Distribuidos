import random
import time

class Node:
    def __init__(self, node_id, clock_time):
        self.node_id = node_id
        self.clock_time = clock_time  # Tiempo inicial del reloj del nodo

    def send_time(self):
        return self.clock_time

    def adjust_clock(self, offset):
        self.clock_time += offset

def berkeley_algorithm(nodes):
    # Paso 1: El nodo coordinador inicia el proceso
    coordinator = nodes[0]
    coordinator_time = coordinator.send_time()
    print(f"Coordinador inicial: Nodo {coordinator.node_id}, Hora: {coordinator_time:.2f}")
    
    # Paso 2: Los demás nodos envían sus tiempos al coordinador
    times = [node.send_time() for node in nodes]
    print(f"Tiempos recibidos de los nodos: {times}")
    
    # Paso 3: El coordinador calcula el promedio ajustado
    average_time = sum(times) / len(times)
    offsets = [average_time - t for t in times]
    print(f"Tiempo promedio calculado: {average_time:.2f}")
    print(f"Offsets calculados para cada nodo: {offsets}")
    
    # Paso 4: El coordinador informa los ajustes a cada nodo
    for node, offset in zip(nodes, offsets):
        node.adjust_clock(offset)
    
    print("Tiempos ajustados de los nodos:")
    for node in nodes:
        print(f"Nodo {node.node_id}, Hora ajustada: {node.clock_time:.2f}")

# Crear nodos con tiempos iniciales desincronizados
random.seed(42)  # Fijar la semilla para reproducibilidad
nodes = [Node(node_id=i, clock_time=random.uniform(100, 200)) for i in range(5)]

# Ejecutar el algoritmo de Berkeley
berkeley_algorithm(nodes)
