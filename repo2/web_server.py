from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv


app = Flask(__name__)

# Configuro la conexión a mongodb
load_dotenv()
connection_str = os.getenv("CONNECTION_STR")
db_name = "bsas-clima"
collection_name = "clima"

client = MongoClient(connection_str)
db = client.get_database(db_name)
collection = db[collection_name]

@app.route('/')
def index():
    data = list(collection.find({}))
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)