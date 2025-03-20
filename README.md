# Houqin System

A campus facilities and logistics management system designed to streamline administrative services within educational institutions.

## Phase 1: Framework Setup & Mock Data Development

This initial phase focuses on building the system skeleton, implementing mock sensor data generation, and storage.

### Tech Stack

- **Frontend**: Vue.js + Vite + VChart (Simple Charts)
- **Backend**: Python Flask + SQLite
- **Data Simulation**: Python Scripts for Mock Sensor Data
- **Real-Time Communication**: HTTP Polling

### Getting Started

#### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```
   The backend will run on http://localhost:5000

#### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```
   The frontend will run on http://localhost:3000

#### Running the Mock Sensor Simulator

1. Make sure the Flask backend is running

2. Run the sensor simulator script:
   ```
   cd scripts
   python sensor_simulator.py
   ```
   This will generate random "in" and "out" events and send them to the backend API.

### System Architecture

- **Mock Data Generator**: Simulates sensor data for people entering and exiting
- **In-Memory Counter**: Tracks the current count of people
- **SQLite Database**: Stores historical flow data
- **API Endpoints**:
  - `GET /api/realtime`: Returns current count from memory
  - `POST /api/sensor`: Receives mock data, updates counter, and logs to DB
