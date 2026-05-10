from flask import Flask, request, jsonify
from database import insert_data, get_all_data, get_alerts
from services import format_data, format_alerts

def register_routes(app):
    @app.route('/data', methods=['POST'])
    def receive_data():
        data = request.json
        
        if not data:
            return jsonify({"Error": "Invalid JSON"}), 400
        
        temperature = data.get('temperature')
        pressure = data.get('pressure')
        status = data.get('status')
        
        if 'temperature' not in data or 'pressure' not in data or 'status' not in data:
            return jsonify({"Error": "Missing fields"}), 400
        
        if temperature is not None and not isinstance(temperature, (int, float)):
            return jsonify({"Error": "Temperature must be a number"}), 400
        
        if pressure is not None and not isinstance(pressure, (int, float)):
            return jsonify({"Error": "Pressure must be a number"}), 400
        
        if not isinstance(status, str):
            return jsonify({"Error": "Status must be a string"}), 400
        
        insert_data(temperature, pressure, status)
        
        return jsonify({
            "Message": "Data received",
            "Data": data
        })
        
    @app.route('/data', methods=['GET'])
    def list_data():
        rows = get_all_data()
        
        data_list = format_data(rows)
        
        return jsonify(data_list)

    @app.route('/alerts', methods=['GET'])
    def list_alerts():
        rows = get_alerts()

        alert_list = format_alerts(rows)

        return jsonify(alert_list)