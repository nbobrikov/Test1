from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с фронтенда

# Данные для передачи на фронтенд
def get_report_data():
    return {
        "actual_data": {
            "file_name": "отчет_2025.xlsx",
            "sheet_name": "данные_сентябрь"
        },
        "business_plan": {
            "file_name": "бизнес_план_2025.xlsx",
            "sheet_name": "основные_показатели"
        },
        "parameters": {
            "report_date": "29-09-2025",
            "frequency": "месяц",
            "periods": 12,
            "report_folder": "/отчеты/2025",
            "conversion_period": 30,
            "include_forecast": True
        },
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# API endpoint для получения данных
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(get_report_data())

# Обслуживаем статические файлы (ваш index.html)
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
