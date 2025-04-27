realtime-logwatch/
├── app/
│   ├── __init__.py              # Flask app init
│   ├── routes.py                # Flask routes (dashboard, API)
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   ├── static/
│   │   └── style.css
│   └── utils/
│       └── alerts.py            # Email/SMS alert logic
├── kafka_consumer/
│   ├── consumer.py              # Kafka consumer that pushes logs to MongoDB + triggers alerts
├── kafka_producer/
│   └── producer.py              # Simulates log messages to Kafka
├── Dockerfile               ← for Flask app (root level)
├── Dockerfile.consumer      ← for Kafka consumer (root level)
├── docker-compose.yml       ← main orchestrator file (root level)
├── config.py                    # App configuration
├── .env                         # Secrets, Kafka URI, Mongo URI
├── run.py                       # Entry point to run Flask app
├── requirements.txt             # Python dependencies
└── README.md

# 🔎 Real-Time Log Monitoring & Alert System

A real-time log collection, processing, and visualization platform built using Flask, Kafka, MongoDB, and Docker. 

---

## 🚀 Features

- 📡 **Real-Time Log Ingestion** via Kafka
- 🧠 **Log Filtering and Alerting** by a Kafka Consumer
- 💾 **Log Storage** in MongoDB for durability
- 🌐 **Flask Web Dashboard** to view logs

---

run the docker -> 
docker compose down -v
docker compose up --build
