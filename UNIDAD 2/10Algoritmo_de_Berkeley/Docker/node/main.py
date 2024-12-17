from flask import Flask, jsonify
import requests
import time
import threading

app = Flask(__name__)

# Simular el reloj del nodo
node_time = time.time()

@app.route('/time', methods=['GET'])
def get_time():
    return jsonify({"time": node_time})

def sync_with_coordinator():
    global node_time
    while True:
        # Simular petición al coordinador
        coordinator_url = "http://coordinator:5000/sync"
        
        # Obtener los tiempos de otros nodos
        times = [node_time]
        try:
            response = requests.post(coordinator_url, json={"times": times})
            adjustments = response.json()['adjustments']
            node_time += adjustments[0]
        except Exception as e:
            print("Error en la sincronización:", e)
        time.sleep(10)  # Sincronización cada 10 segundos

if __name__ == "__main__":
    threading.Thread(target=sync_with_coordinator).start()
    app.run(host="0.0.0.0", port=5000)
