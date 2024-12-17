from flask import Flask, request, jsonify

app = Flask(__name__)

token_available = True
queue = []

@app.route('/request_token', methods=['POST'])
def request_token():
    global token_available
    process_name = request.json['name']
    if token_available:
        token_available = False
        return jsonify({"message": f"{process_name} has received the token."})
    else:
        queue.append(process_name)
        return jsonify({"message": f"{process_name} added to the queue."})

@app.route('/release_token', methods=['POST'])
def release_token():
    global token_available
    if queue:
        next_process = queue.pop(0)
        return jsonify({"message": f"Token passed to {next_process}."})
    else:
        token_available = True
        return jsonify({"message": "Token is now available."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
