# Industrial Data Monitoring System

## 📌 Overview

This project simulates a real industrial data monitoring system, integrating PLC data acquisition, backend processing, and web visualization.

It collects real-time data from a simulated Siemens PLC, processes it through a Python backend, stores it in a database, and provides a web interface for monitoring and analysis.

\---

## 🏗️ Architecture

```
PLC (PLCSIM)
    ↓
Collector (Snap7)
    ↓
Flask API
    ↓
SQLite Database
    ↓
Django Dashboard (Admin)
```

\---

## ⚙️ Technologies

* Python
* Flask (Data ingestion API)
* Django (Dashboard \& Admin)
* SQLite (Database)
* python-snap7 (PLC communication)
* Requests (HTTP communication)

\---

## 🚀 Features

### 🔌 Data Acquisition

* Reads real-time data from PLC (temperature, pressure, status)
* Uses Snap7 protocol for industrial communication

### 🧠 Backend Processing

* REST API for receiving data (`POST /data`)
* Data persistence in SQLite
* Alert detection (`GET /alerts`)

### 📊 Data Visualization

* Django Admin dashboard
* Real-time data inspection
* Filtering and search capabilities

### ⚠️ Alerts

* Triggered when:

  * temperature > 80
  * status = ERROR

\---

## 📁 Project Structure

```
monitoramento-industrial/
│
├── api/          # Flask API
├── collector/    # PLC data reader (Snap7)
├── dashboard/    # Django project
├── database/     # SQLite database
├── venv/         # Virtual environment
└── start.bat     # Start all services
```

\---

## ▶️ How to Run

### 1\. Install dependencies

```
pip install -r requirements.txt
```

\---

### 2\. Start all services

```
start.bat
```

This will start:

* Flask API (port 5000)
* PLC Collector
* Django Dashboard (port 8000)

\---

### 3\. Access the system

* API: http://127.0.0.1:5000
* Django Admin: http://127.0.0.1:8000/admin

\---

## 📡 API Endpoints

### POST /data

```json
{
  "temperature": 85,
  "pressure": 5.2,
  "status": "RUN"
}
```

\---

### GET /data

Returns all stored data

\---

### GET /alerts

Returns abnormal data based on rules:

* temperature > 80
* status = ERROR

\---

## 🔧 PLC Integration

* Simulated using Siemens PLCSIM Advanced
* Data read via Snap7 (S7 protocol)
* Requires:

  * Non-optimized DB
  * PUT/GET enabled

\---

## 🎯 Purpose

This project demonstrates:

* Integration between industrial automation and software systems
* Real-time data acquisition from PLCs
* Backend API development
* Data visualization using web frameworks

\---

## 🚀 Future Improvements

* Real-time dashboard (charts)
* WebSocket integration
* Authentication system enhancements
* Migration to PostgreSQL
* Containerization (Docker)

\---

