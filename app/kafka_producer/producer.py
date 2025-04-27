from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda m: json.dumps(m).encode("utf-8"),
)

services = ["auth", "orders", "payments", "inventory"]
severities = ["INFO", "WARNING", "ERROR", "CRITICAL"]

while True:
    log = {
        "timestamp": time.time(),
        "service": random.choice(services),
        "severity": random.choices(severities, weights=[70, 15, 10, 5])[0],
        "message": "Random log message"
    }
    producer.send("logs", log)
    time.sleep(1)
