# app/kafka_producer/send_log.py
from kafka import KafkaProducer
from kafka.errors import KafkaError, NoBrokersAvailable
import json
import os
import time
from datetime import datetime

producer = None  # Start with no producer

# Custom JSON encoder to handle datetime objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to string
        return super().default(obj)

def get_producer():
    global producer
    if producer is None:
        retries = 5
        while retries > 0:
            try:
                producer = KafkaProducer(
                    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP", "kafka:9092"),
                    value_serializer=lambda v: json.dumps(v, cls=CustomJSONEncoder).encode("utf-8"),
                )
                break
            except NoBrokersAvailable as e:
                retries -= 1
                print(f"Kafka broker not available yet, retries left: {retries}")
                time.sleep(2)
        if producer is None:
            raise Exception("Failed to connect to Kafka after retries")
    return producer

def send_log(topic, value):
    p = get_producer()
    try:
        p.send(topic, value)
        p.flush()
    except KafkaError as e:
        print(f"Failed to send log to Kafka: {e}")
