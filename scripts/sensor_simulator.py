import random
import time
import requests
from datetime import datetime

# API endpoint
API_URL = "http://localhost:5000/api/sensor"

def generate_mock_data():
    """Generate mock sensor data"""
    mock_data = {
        "sensor_id": "A1",
        "direction": random.choice(["in", "out"]),
        "timestamp": datetime.now().isoformat()
    }
    return mock_data

def send_data_to_api(data):
    """Send mock data to the API"""
    try:
        response = requests.post(API_URL, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to API: {e}")
        return None

def run_simulator(interval=0.5):
    """Run the simulator continuously"""
    print(f"Starting sensor simulator. Sending data every {interval} seconds to {API_URL}")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            mock_data = generate_mock_data()
            print(f"Generated: {mock_data}")
            
            result = send_data_to_api(mock_data)
            if result:
                print(f"API response: Current count = {result.get('current_count', 'N/A')}")
            
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Simulator stopped")

if __name__ == "__main__":
    run_simulator()
