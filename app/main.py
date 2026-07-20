from flask import jsonify, render_template
from . import create_app
import os

config_name = os.getenv("FLASK_ENV", "default")
app = create_app(config_name)

@app.route("/")
def index():
    return render_template('index.html', environment=config_name)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/api/v1/status")
def status():
    return jsonify({
        "service": "DevSecOps Flask App",
        "version": "1.0.0",
        "environment": config_name
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
