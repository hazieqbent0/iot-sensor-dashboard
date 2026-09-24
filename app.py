from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/api/sensor-data")
def sensor_data():
    return jsonify({
        "timestamp": time.time(),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2)
    })

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)