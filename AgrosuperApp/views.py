from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import pickle


# Funciones para visualizar templates
def login(request):
    return render(request, "registration\login.html")

@login_required
def index(request):
    return render(request, "index.html")

def salir(request):
    logout(request)
    return redirect('/')

def carnes(request):
    return render(request, "carnes.html")


# Vistas para API
#Toda la info de los endpoint ya fueron obtenidos en el archivo getinfo, y guardados como archivos.pkl, ahora me dispongo a leerlo y evaluar el contenido para renderizarlo en los html.

class DatosCarnes(TemplateView):
    template_name = 'carnes.html'

    def crear_data(diccionario, concepto, columna):
        lista = []
        for dicc in diccionario:
            for clave in dicc:
                if dicc[clave] == concepto:
                    lista.append(dicc[columna])
        return lista

    with open('carnes_real.pkl', 'rb') as real_carnes:
        real = pickle.load(real_carnes)

    with open('carnes_proyectado.pkl', 'rb') as proyectado_carnes:
        proyectado = pickle.load(proyectado_carnes)
        
    
    data_ingreso_real_usdm = crear_data(real, 'INGRESO', 'resultado_USDM')
    data_ingreso_proyectado_usdm = crear_data(proyectado, 'INGRESO', 'resultado_USDM')

    def pasar(self, request):
        return render(request, self.template_name, {'data_ingreso_real_usdm'}, {'data_ingreso_proyectado_usdm'})

def editorSemanal(request):
    with open('editor_semanal.pkl', 'rb') as editor_semanal:
        editor_semanal = pickle.load(editor_semanal)
            
    return render(request, 'editor.html', {"diccionarios": editor_semanal})
    """def crear_tablehead(lista):
        claves = []
        for dicc in lista[0]:
            claves.append(dicc)
        return claves
    nombre_columnas = crear_tablehead(editor_semanal)
    print(nombre_columnas)"""

"""def crearPDF(request):
    env = Enviroment(loader = FileSystemLoader("../templates"))
    template = env.get
    pdfkit.from_string(html,)"""

def obtenerVariaciones(request):
    with open('obtenervariaciones.pkl', 'rb') as variaciones:
        variaciones = pickle.load(variaciones)
    return render(request, 'variaciones.html', {"variaciones": variaciones})

def EditaryProbarVariable(request):
    with open('editorVariable.pkl', 'rb') as editarV:
        editarV = pickle.load(editarV)

    with open('probarVariable.pkl', 'rb') as probarV:
        probarV = pickle.load(probarV)

    return render(request, 'editarVariable.html')
    """, {"dato_grafico": editarV}, {"dato_tabla": probarV}"""