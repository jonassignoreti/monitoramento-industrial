import requests
import random
import time

URL = "http://127.0.0.1:5000/data"

def generate_data():
    return {
        "temperature": round(random.uniform(20.0, 100.0), 2),
        "pressure": round(random.uniform(1.0, 10.0), 2),
        "status": random.choice(["RUN", "STOP", "ERROR"])
    }

while True:
    data =  generate_data()
    
    try:
        response = requests.post(URL, json=data)
        
        print("Sent:", data, "| Status:", response.status_code)
    except Exception as e:
        print("Error:", e)
    
    time.sleep(2)