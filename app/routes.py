from flask import Blueprint, render_template, request, redirect, url_for
from app import mongo
from app.kafka_producer.send_log import send_log
from datetime import datetime

main = Blueprint('main', __name__)

@main.route("/")
def dashboard():
    logs_cursor = mongo.db.logs.find().sort("timestamp", -1).limit(100)
    logs = list(logs_cursor)  # <-- convert to list FIRST!

    # Now safely modify timestamps
    for log in logs:
        if isinstance(log['timestamp'], str):
            try:
                log['timestamp'] = datetime.fromisoformat(log['timestamp'])
            except ValueError:
                log['timestamp'] = None  # fallback if string is not in ISO format

    return render_template("dashboard.html", logs=logs)


@main.route("/send-log", methods=["POST"])
def send_log_route():
    log_data = {
        "timestamp": datetime.utcnow(),
        "service": request.form.get("service", "flask-app"),
        "severity": request.form.get("severity", "INFO"),
        "message": request.form.get("message", "Default test log message"),
    }
    send_log("logs", log_data)
    return redirect(url_for("main.dashboard"))
