from tkinter import *
from tkinter import messagebox
import Simulacion
from tkinter import ttk

class NodoADC:
    def __init__(self, id_ADC, tupla_listas, px, py):

        self.dato = id_ADC
        self.tipo = "ADC"
        self.nombre = "ADC_"+str(id_ADC)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "A"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada = None
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="ADC.png")
