def format_data(rows):
    data_list = []
    
    for row in rows:
        data_list.append({
            "id": row[0],
            "temperature": row[1],
            "pressure": row[2],
            "status": row[3],
            "timestamp": row[4]
        })
    
    return data_list

def format_alerts(rows):
    alert_list = []
    
    for row in rows:
        alert_list.append({
            "id": row[0],
            "temperature": row[1],
            "pressure": row[2],
            "status": row[3],
            "timestamp": row[4]
        })
    
    return alert_list