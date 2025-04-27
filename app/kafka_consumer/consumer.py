# kafka_consumer/consumer.py

from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from pymongo import MongoClient
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import time

load_dotenv()

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/logwatch")
client = MongoClient(mongo_uri)
db = client.get_default_database()

# Retry Kafka connection
while True:
    try:
        consumer = KafkaConsumer(
            'logs',
            bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP", "kafka:9092"),
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='logwatch-group'
        )
        print("Connected to Kafka successfully!")
        break
    except NoBrokersAvailable:
        print("Kafka not available yet. Retrying in 3 seconds...")
        time.sleep(3)

print("Consumer started. Listening for logs...")

# Start consuming
for message in consumer:
    log_data = message.value
    print(f"Received log: {log_data}")

    # Replace float timestamp with datetime
    if 'timestamp' in log_data and isinstance(log_data['timestamp'], (float, int)):
        log_data['timestamp'] = datetime.utcfromtimestamp(log_data['timestamp'])

    # Insert into MongoDB
    db.logs.insert_one(log_data)
