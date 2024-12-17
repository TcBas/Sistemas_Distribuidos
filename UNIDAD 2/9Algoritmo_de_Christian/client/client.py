import requests
import time

def sincronizar_reloj():
    # Paso 1: Cliente envía solicitud al servidor
    t1 = time.time()
    print(f"Cliente envió solicitud en t1 = {t1}")

    # Solicita la hora del servidor
    response = requests.get("http://server:5000/hora")
    servidor_hora = response.json()["hora"]

    # Paso 2: Calcula tiempo de recepción
    t2 = time.time()
    print(f"Cliente recibió respuesta en t2 = {t2}")

    # Calcular RTT y ajustar el reloj
    rtt = t2 - t1
    tiempo_estimado = servidor_hora + (rtt / 2)
    print(f"RTT: {rtt}, Hora ajustada: {tiempo_estimado}")

# Ejecutar sincronización
if __name__ == "__main__":
    sincronizar_reloj()
