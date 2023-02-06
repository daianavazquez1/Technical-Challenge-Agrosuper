import requests
import json
import pickle

#Params para consulta de carnes   
url_carnes = 'http://f11.cl:8090/getCarnesRealProyeccion'
data_carnes ={
  "auth": {
    "username": "devsafio",
    "token": "tokentokentokenABC"
  },
  "query": {
    "initial_date": {
      "month": 1,
      "year": 2020
    },
    "end_date": {
      "month": 12,
      "year": 2025
    }
  }
}

#Params para consulta de obtenerVariaciones y editorSemanal
url_obtenerVariaciones = "http://f11.cl:8090/obtenerVariaciones"
url_editorSemanal = "http://f11.cl:8090/editorSemanal"

data_variaciones_editor = {"auth": {
    "username": "devsafio",
    "token": "tokentokentokenABC"
  }}

#Params para consulta de probarVariable
url_probarVariable = 'http://f11.cl:8090/probarVariable'
data_probarVariable = {
  "auth": {
    "username": "devsafio",
    "token": "tokentokentokenABC"
  },
  "var_name": "variableA",
  "value_test": 0
}

#Params para consulta de editorVariable
url_editorVariable = 'http://f11.cl:8090/editorVariables'
data_editorVariable= {
  "auth": {
    "username": "devsafio",
    "token": "tokentokentokenABC"
  },
  "var_name": "variableA"
}

#Funcion para obtener la informacion de cada endpoint
def generar_request(url, data):
    data = json.dumps(data)
    response = requests.post(url, data=data)
    if response.status_code == 200:
        response = response.json()
    return response

#Procedimiento para realizar la llamada, y guardar la información en archivos .pkl
#info_general = generar_request(url_carnes, data_carnes)
#real = info_general['real']
#proyectado = info_general['proyectado']

"""with open('carnes_real.pkl', "wb") as carnesreal_pickle:
        pickle.dump(real, carnesreal_pickle)
        print("El archivo1 se guardo satisfacctoriamente.")

with open('carnes_proyectado.pkl', "wb") as carnesproyectado_pickle:
        pickle.dump(proyectado, carnesproyectado_pickle)
        print("El archivo1.2 se guardo satisfacctoriamente.")"""

#Una vez realizada la operacion lo comento para que no se guarde la cantidad de veces que activo el codigo

"""info_editor = generar_request(url_editorSemanal, data_variaciones_editor)
info_editor = info_editor['data']

with open('editor_semanal.pkl', "wb") as editorsemanal_pickle:
        pickle.dump(info_editor, editorsemanal_pickle)
        print("El archivo3 se guardo satisfacctoriamente.")


info_variaciones = generar_request(url_obtenerVariaciones, data_variaciones_editor)
info_variaciones = info_variaciones['data']

with open('obtenervariaciones.pkl', "wb") as obtenervariaciones_pickle:
        pickle.dump(info_variaciones, obtenervariaciones_pickle)
        print("El archivo4 se guardo satisfacctoriamente.")


info_variables = generar_request(url_probarVariable, data_probarVariable)
info_variables = info_variables['data']

with open('probarVariable.pkl', "wb") as probarVariable_pickle:
        pickle.dump(info_variables, probarVariable_pickle)
        print("El archivo5 se guardo satisfacctoriamente.")

        
info_editorVariable = generar_request(url_editorVariable, data_editorVariable)
info_editorVariable = info_editorVariable['data']

with open('editorVariable.pkl', "wb") as editorVariable_pickle:
        pickle.dump(info_editorVariable, editorVariable_pickle)
        print("El archivo6 se guardo satisfacctoriamente.")"""



#Intento fallido de: Creo dos funciones, una para guardar un archivo .pkl que tenga la info de los dics obtenidos por consulta, y otro para abrirlo, luego de esto no seria necesario continuar con las consultas y asi evitar que me de un error por alcanzar el maximo de consultas.
#Se evita eliminar el codigo con la finalidad de retomar el proceso en un futuro cercano, sepa comprender. A solucionar: lograr pasar el nombre del parametro 'nombre_lista', para que el nombre del archivo.pkl sea costumizable.
"""def pickle_guardar(nombre_lista, nombre_archivo):
    with open(str(nombre_lista)+'.pkl', "wb") as nombre_archivo:
        pickle.dump(nombre_lista, nombre_archivo)
        print("El archivo se guardo satisfacctoriamente.")

def pickle_abrir(example_dict):
    pickle_in = open("dict.pickle","rb")
    example_dict = pickle.load(pickle_in)"""