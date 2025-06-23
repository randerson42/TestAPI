from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "status": "received",
        "you_sent": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

