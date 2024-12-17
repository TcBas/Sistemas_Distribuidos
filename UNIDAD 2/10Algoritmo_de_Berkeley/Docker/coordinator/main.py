from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Simular el reloj del coordinador
coordinator_time = time.time()

@app.route('/sync', methods=['POST'])
def sync_time():
    times = request.json['times']
    times.append(coordinator_time)
    
    # Calcular el tiempo promedio
    average_time = sum(times) / len(times)
    
    # Calcular ajustes para cada nodo
    adjustments = [average_time - t for t in times]
    return jsonify({"adjustments": adjustments[:-1]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
