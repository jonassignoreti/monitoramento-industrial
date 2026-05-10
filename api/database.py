import sqlite3

def connect():
    return sqlite3.connect('../database/database.db')

def create_table():
    conn = connect()
    cursor = conn.cursor()
     
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            pressure REAL,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

def insert_data(temperature, pressure, status):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO sensor_data (temperature, pressure, status)
    VALUES (?, ?, ?)
    """, (temperature, pressure, status))
    
    conn.commit()
    conn.close()

def get_all_data():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM sensor_data")
    rows = cursor.fetchall()
    
    conn.close()
    
    return rows

def get_alerts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM sensor_data
        WHERE temperature > 80 OR status = 'ERROR' OR status = 'COMM_ERROR'
        """)
    rows = cursor.fetchall()
    conn.close()
    
    return rows