from tkinter import *
from tkinter import messagebox
import numpy as np
import time
import math


class Simulacion():

    def __init__(self):

        self.lista = None
        self.tiempo_muestreo = 20
        self.numero_muestras = 1000

    def listas(self, lista):

        self.lista = lista

    def tiempoMuestreo(self, tiempo, muestras):

        self.tiempo_muestreo = tiempo
        self.numero_muestras = muestras

    def inicioSimulacion(self):

        listaRaizArbol = []

        for i in range(3, len(self.lista)):

            actual = self.lista[i].cabeza

            while actual is not None:

                if actual.tipo == "ADC":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "DAC":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "FLT":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "FT":

                    if actual.salida is None:
                        if actual.entrada_1 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_2 is not None:
                            listaRaizArbol.append(actual.nombre)

                if actual.tipo == "PID":
                    if actual.salida is None:
                        if actual.entrada1 is not None or actual.entrada2 is not None:
                            listaRaizArbol.append(actual.nombre)

                if actual.tipo == "PWM":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "QDEC":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "RE":

                    if actual.salida_1 is None and actual.salida_2 is None:
                        if actual.entrada_1 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_2 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_3 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_4 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_5 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_6 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_7 is not None:
                            listaRaizArbol.append(actual.nombre)

                if actual.tipo == "SAT":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "SCOPE":
                    if actual.salida is None and actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                if actual.tipo == "DER":

                    if actual.salida_1 is None and actual.salida_2 is None:
                        if actual.entrada is not None:
                            listaRaizArbol.append(actual.nombre)

                if actual.tipo == "SUM":

                    if actual.salida is None:
                        if actual.entrada_1 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_2 is not None:
                            listaRaizArbol.append(actual.nombre)

                if actual.tipo == "REST":

                    if actual.salida is None:
                        if actual.entrada_1 is not None:
                            listaRaizArbol.append(actual.nombre)
                        elif actual.entrada_2 is not None:
                            listaRaizArbol.append(actual.nombre)

                if actual.tipo == "ENTP":
                    if actual.entrada is not None: listaRaizArbol.append(actual.nombre)

                actual = actual.siguiente

        self.obtenerVectoresDatos(listaRaizArbol)

    def buscarConexion(self, nombre, nombre_bloque):

        actual = self.lista[2].cabeza
        encontrado = False

        if nombre is None:
            return None

        while actual != None and not encontrado:
            if actual.nombre == nombre:
                encontrado = True
                return self.buscarBloque(actual.bloqueFin)

            else:
                actual = actual.siguiente

        return None

    def buscarBloque(self, nombre):
        tipo = ""
        for i in nombre:
            if i == "_":
                break
            else:
                tipo = tipo + i

        actual = None

        if tipo == "Linea": actual = self.lista[2].cabeza
        if tipo == "ADC": actual = self.lista[3].cabeza
        if tipo == "PID": actual = self.lista[4].cabeza
        if tipo == "PWM": actual = self.lista[5].cabeza
        if tipo == "RE": actual = self.lista[6].cabeza
        if tipo == "CTE": actual = self.lista[7].cabeza
        if tipo == "FT": actual = self.lista[8].cabeza
        if tipo == "SAT": actual = self.lista[9].cabeza
        if tipo == "QDEC": actual = self.lista[10].cabeza
        if tipo == "ENTP": actual = self.lista[11].cabeza
        if tipo == "SALP": actual = self.lista[12].cabeza
        if tipo == "DAC": actual = self.lista[13].cabeza
        if tipo == "FLT": actual = self.lista[14].cabeza
        if tipo == "SCOPE": actual = self.lista[15].cabeza
        if tipo == "STEP": actual = self.lista[16].cabeza
        if tipo == "TRAPECIO": actual = self.lista[17].cabeza
        if tipo == "DER": actual = self.lista[18].cabeza
        if tipo == "SUM": actual = self.lista[19].cabeza
        if tipo == "REST": actual = self.lista[20].cabeza

        while actual is not None:
            if actual.nombre == nombre:
                return actual

            actual = actual.siguiente

        print("El bloque en la entrada no existe")
        return None

    def obtenerBloqueConexion(self, nombreConexion, nombre):

        if nombreConexion is None:
            return None

        a = self.buscarBloque(nombreConexion)

        if a.bloqueInicio == nombre:
            return self.buscarBloque(a.bloqueFin)

        if a.bloqueFin == nombre:
            return self.buscarBloque(a.bloqueInicio)

    def tipoBloque(self, nombre):

        tipo = ""
        for i in nombre:
            if i == "_":
                break
            else:
                tipo = tipo + i

        return tipo

    def obtenerVectoresDatos(self, elementos):

        listaSistemas = []

        for i in elementos:
            actual = self.buscarBloque(i)
            listaBloques = actual.senal_nombres([])
            listaSistemas.append(listaBloques)

        if listaSistemas == []:
            return None

        muestras = self.numero_muestras
        t_muestreo = self.tiempo_muestreo/1000  # 20 ms
        t = []

        for i in range(0, muestras):
            t.append(i*t_muestreo)

        # Recorrido del Arbol
        for i in elementos:

            for n in range(0, muestras):
                actual = self.buscarBloque(i)
                ts = n * t_muestreo
                actual.senal_simulacion(n, ts, None)

        # ----------------------

        lista_b = []

        for i in listaSistemas:
            lista_b.append([])

        for i in range(0, len(lista_b)):
            listaSistemas[i] = set(listaSistemas[i])
            lista_b[i] = set(listaSistemas[i])

        x = 0
        y = 0
        p = 0

        while p < math.factorial(len(listaSistemas)) + 20:

            if lista_b[x] & lista_b[y] != set() and x != y:

                for i in lista_b[y]:
                    lista_b[x].add(i)

                if x != y:
                    del lista_b[y]
                    if x >= len(lista_b):
                        x = len(lista_b) - 1
            y += 1

            if y >= len(lista_b):
                y = 0
                x = x + 1
                if x >= len(lista_b):
                    x = 0
            p += 1

        lista_c = []  # Lista con SCOPES a graficar

        for i in range(0, len(lista_b)):
            lista_c.append([])
            lista_b[i] = list(lista_b[i])
            for m in range(0, len(lista_b[i])):

                actual = self.buscarBloque(lista_b[i][m])

                if actual.tipo == "SCOPE":

                    if actual.variable_mostrar_ocultar == 1:
                        lista_c[i].append(lista_b[i][m])

        # Grafica -------------------------------------

        import matplotlib.pyplot as plt

        d = 1
        plt.close()

        for i in lista_c:

            if i != []:
                plt.figure(d)
                for m in i:
                    actual = self.buscarBloque(m)
                    plt.plot(actual.simulacion_tiempo, actual.simulacion_datos, label=actual.variable_nombre_bloque)
                    plt.legend()

                d = d + 1

        plt.show(block=False)
