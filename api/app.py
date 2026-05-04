from flask import Flask
from database import create_table
from routes import register_routes

app = Flask(__name__)

register_routes(app)

if __name__ == '__main__':
    create_table()
    app.run(debug=True) 