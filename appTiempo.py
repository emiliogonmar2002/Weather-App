#Emilio González Martínez 06-05-2020
#Weather App

from tkinter import *
import requests


#Funciones

def clima_json(ciudad):
    API_key = "a606a607b32ac275421f5ddca332cad5"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID" : API_key, "q" : ciudad,  "units": "metric"}
    response = requests.get(URL, params = parametros)
    clima = response.json()

    mostrarRespuesta(clima)

    #print(clima["name"])
    #print(clima["weather"][0]["description"])
    #print(clima["main"]["temp"])

def mostrarRespuesta(clima):
    nombre_ciudad = clima["name"]
    desc = clima["weather"][0]["description"]
    temp = clima["main"]["temp"]

    ciudad["text"] = nombre_ciudad.capitalize()
    temperatura["text"] = str(round(temp)).capitalize() + "°C"
    descripcion["text"] = desc.capitalize()


#Configuración de la ventana
ventana = Tk()
ventana.geometry("300x550")
ventana.title("WeatherApp")
ventana["bg"] = "#F2FFD8"

#Cuadro de entrada de texto
texto_ciudad = Entry(ventana, font = ("Georgia",15,"normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

#Boton de Clima
obtener_clima = Button(ventana, text = "Get Weather",font = ("Tahoma",10,"normal"), command = lambda: clima_json(texto_ciudad.get()))
obtener_clima.pack(padx=30,pady=10)
obtener_clima["border"] = "1"
obtener_clima["bg"] = "light goldenrod"

#Resultados
ciudad = Label(font = ("Verdana",20,"normal"))
ciudad.pack(padx=30,pady=10)
ciudad["bg"] = "#F2FFD8"

temperatura = Label(font = ("Impact",70,"bold"))
temperatura.pack(padx=30,pady=10)
temperatura["bg"] = "#F2FFD8"

descripcion = Label(font = ("Times",15,"underline","italic"))
descripcion.pack(padx=30,pady=0)
descripcion["bg"] = "#F2FFD8"




ventana.mainloop()

#API
#a606a607b32ac275421f5ddca332cad5
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}