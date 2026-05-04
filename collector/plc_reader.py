from snap7 import Client
import struct
import requests
import time

URL = "http://127.0.0.1:5000/data"

client = Client()

client.connect('192.168.0.65', 0, 1)

while True:
    data = client.db_read(1, 0, 10)
    
    temperature = struct.unpack('>f', data[0:4])[0]
    pressure    = struct.unpack('>f', data[4:8])[0]
    status      = int.from_bytes(data[8:10], 'big')
    
    payload = {
        "temperature": temperature,
        "pressure": pressure,
        "status": "RUN" if status == 0 else "ERROR"
    }
    
    try:
        response = requests.post(URL, json=payload)
        print("Sent:", data, "| Status:", response.status_code)
    except Exception as e:
        print("Error:", e)

    print(f"Temp: {temperature:.2f} | Press: {pressure:.2f} | Status: {payload['status']}")

    time.sleep(1)