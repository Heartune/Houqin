import sqlite3
from datetime import datetime
import os

# Database file path
DB_PATH = 'flow_history.db'

def get_db_connection():
    """Create a connection to the SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create the flow_history table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flow_history (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME,
        current_count INTEGER
    )
    ''')
    
    conn.commit()
    conn.close()
    
def add_flow_history(current_count):
    """Add a new entry to the flow_history table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    timestamp = datetime.now().isoformat()
    cursor.execute(
        'INSERT INTO flow_history (timestamp, current_count) VALUES (?, ?)',
        (timestamp, current_count)
    )
    
    conn.commit()
    conn.close()
    return True
