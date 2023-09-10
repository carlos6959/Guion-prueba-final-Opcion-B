# Prueba Final Opcion B
# CARLOS SOLORZANO RAMON
***
## Instalación

1. Crear un virtual environment:
    ```
    python -m venv venv_repo1
    ```
    Activarlo (Windows):
    ```
    venv_repo1\Scripts\activate
    ```
2. Instalar requerimientos:
    ```
    pip install -r requirements.txt
    ```
3. Ejecutar `main.py`

***
## Descripción del proyecto
#### Parte 1
Se busca consultar la API de [AccuWeather](https://www.accuweather.com), que posee datos climáticos de todo el mundo. Son varias APis distintas, dentro de las cuales hay una denominada [Current Conditions API](https://developer.accuweather.com/accuweather-current-conditions-api/apis), con información sobre el clima en distintas ciudades. Esta API será la utilizada para el proyecto.

Dentro de los distintos endpoints, hay uno llamado *Current conditions* que permite obtener el clima actual para una determinada región. Este será el endpoint a consultar para el proyecto.

La API requiere registrarse para obtener una API key con la que consultar los datos. Además, para este caso se necesita el código de la región, que se puede obtener a partir de [Locations API](https://developer.accuweather.com/accuweather-locations-api/apis). 

Para realizar las consultas a la API desde Python, se utilizará la librería `requests` (archivo `consultar_api.py`). En este archivo se realiza una consulta POST con el código de región, y se transforma la respuesta obtenida a formato JSON.

#### Parte 2
El siguiente paso consiste en almacenar los datos en una base de datos en la nube (archivo `guardar_mongo.py`), para lo cual se eligió Mongo Atlas. Los parámetros requeridos son la cadena de conexión al servidor y el nombre de la base de datos y la colección donde se guardarán los datos. Para la comunicación entre Python y Mongo se utiliza la librería `pymongo`.
