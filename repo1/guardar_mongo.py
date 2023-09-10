import pymongo
import sys

def save_mongo(document_list,connection_str,db_name,collection_name):
    '''
    Argumentos:
        - document_list: lista con documentos a insertar
        - connection_str: connection_str para conexión a Mongo Atlas
        - db_name: nombre de la database
        - collection_name: nombre de la collection
    '''
    try:
        client = pymongo.MongoClient(connection_str)
    except pymongo.errors.ConfigurationError:
        print("Connection string inválida")
        sys.exit(1)

    db = client[db_name]

    my_collection = db[collection_name]

  
    # borrar la collection si ya existe
    try:
     my_collection.drop()  
    except pymongo.errors.OperationFailure:
        print("Error de autenticación")
        sys.exit(1)


    try: 
        if isinstance(document_list,dict):
            my_collection.insert_one(document_list)
        else:
            my_collection.insert_many(document_list)
    except pymongo.errors.OperationFailure:
        print("Error en la inserción")
        sys.exit(1)
    else:
        print("Se insertaron exitosamente los documentos")