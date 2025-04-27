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

A real-time log collection, processing, and visualization platform built using Flask, Kafka, MongoDB, and Docker. This system simulates production-grade log monitoring tools like ELK Stack (Elasticsearch + Logstash + Kibana), but is lightweight and tailored for Python environments.

---

## 🚀 Features

- 📡 **Real-Time Log Ingestion** via Kafka
- 🧠 **Log Filtering and Alerting** by a Kafka Consumer
- 💾 **Log Storage** in MongoDB for durability
- 🌐 **Flask Web Dashboard** to view logs
- 🔔 Optional alerts via email, Slack, or other integrations
- 🔄 Real-time log updates with **Flask-SocketIO**
- 🐳 Fully containerized with **Docker Compose**

---

## 🛠 Tech Stack

| Layer                  | Technology            | Purpose                             |
|------------------------|-----------------------|-------------------------------------|
| Web Framework          | Flask                 | Backend API and web dashboard       |
| WSGI Server            | Gunicorn              | Production-ready web server         |
| Streaming Platform     | Apache Kafka          | Log pipeline                        |
| Kafka Integration      | kafka-python          | Kafka Producer & Consumer API       |
| Database               | MongoDB               | Persistent log storage              |
| DB Integration         | Flask-PyMongo         | Flask ↔ MongoDB                     |
| Environment Config     | python-dotenv         | Manage app secrets & configs        |
| HTTP Client            | requests              | External API calls                  |
| Real-time Frontend     | Flask-SocketIO        | Real-time log updates in dashboard  |
| Containerization       | Docker + Docker Compose| Consistent development & deployment |

---

run the docker -> 
docker compose down -v
docker compose up --build
