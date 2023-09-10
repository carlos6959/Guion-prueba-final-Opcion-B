# Prueba Final Opcion B
# CARLOS SOLORZANO RAMON
# Web server
***
## Instalación

1. Crear un virtual environment:
    ```
    python -m venv venv_repo2
    ```
    Activarlo (Windows):
    ```
    venv_repo2\Scripts\activate
    ```
2. Instalar requerimientos:
    ```
    pip install -r requirements.txt
    ```
3. Ejecutar `main.py`

***
## Descripción del proyecto
Una vez ejecutado el código del repositorio 1, se obtiene una colección en Mongo Atlas.
El repositorio 2 busca generar un servidor web con Flask que lee dicha colección y muestra su contenido en el browser. Una vez ejecutado `main.py`, se levanta el servidor en el puerto 5000 (http://localhost:5000) y se muestran los datos del clima.
