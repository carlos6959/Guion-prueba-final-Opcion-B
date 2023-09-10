import consultar_api
import guardar_mongo
from dotenv import load_dotenv
import os

load_dotenv()
api_key =os.getenv("API_KEY")
connection_str = os.getenv("CONNECTION_STR")

try:
    response_dict = consultar_api.consult(api_key)
except:
    print("Error consultando la api...")
print(response_dict)

db_name = "bsas-clima"
collection_name = "clima"
try:
    guardar_mongo.save_mongo(response_dict,connection_str,db_name,collection_name)
except:
    print("error guardando en Mongo Atlas")