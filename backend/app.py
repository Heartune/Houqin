from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime
import os

# Import service modules
from services.memory_counter import get_current_count, update_counter
from database import init_db, add_flow_history

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the database
init_db()

@app.route('/api/realtime', methods=['GET'])
def get_realtime_count():
    """Return the current count from memory"""
    return jsonify({'current_count': get_current_count()})

@app.route('/api/sensor', methods=['POST'])
def receive_sensor_data():
    """Receive sensor data, update counter, and log to DB"""
    data = request.json
    
    if not data or 'direction' not in data:
        return jsonify({'error': 'Invalid data format'}), 400
        
    # Update the in-memory counter
    direction = data['direction']
    update_counter(direction)
    
    # Log the current count to the database
    current_count = get_current_count()
    add_flow_history(current_count)
    
    return jsonify({'success': True, 'current_count': current_count})

if __name__ == '__main__':
    app.run(debug=True)
