import requests

def consult(api_key,print=False):
    '''
    Argumentos:
        - api_key
        - region_code: código de la región en la que consultar los países. SAM para sudamérica
        - print: True/False para imprimir la respuesta a la consulta
    '''

    # region_code="SAM"
    # url = f"http://dataservice.accuweather.com/locations/v1/countries/{region_code}?apikey={api_key}" #endpoint paises
    
    url = f"http://dataservice.accuweather.com/locations/v1/127702?apikey={api_key}" #endpoint clima actual en Machala,Ecuador


    response = requests.post(url)

    response_dict = response.json()
    if print:
        print(response_dict)
        print(response_dict[0].keys())
    #La response de la api es una lista de diccionarios, cada uno con las claves ID, LocalizedName e EnglishName
    return response_dict