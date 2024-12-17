from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/hora", methods=["GET"])
def hora_servidor():
    # Devuelve la hora actual del servidor
    return jsonify({"hora": time.time()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
