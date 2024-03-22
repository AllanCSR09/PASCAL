import xml.etree.ElementTree as ET
from tkinter import *


class NuevoArchivo():

    def __init__(self, lista, directorio): #, obj_principal):
        
        self.lista = lista

        error = True
        try:
            tree = ET.parse(directorio)
            root = tree.getroot()
            error = False

        except Exception:
            pass

        if error is False:

            # ----------------------- Configuracion -----------------------
            for child in root.iter('Configuracion'):

                for child2 in child.iter('Dispositivo'):
                    #obj_principal.variable_nombre_dispositivo = child2.text
                    variable_nombre_dispositivo = child2.text

                for child2 in child.iter('Velocidad'):
                    #obj_principal.variable_velocidad = abs(int(child2.text))
                    variable_velocidad = abs(int(child2.text))

                for child2 in child.iter('Tiempo_Muestreo'):
                    #obj_principal.variable_tiempo_muestreo = abs(int(child2.text))
                    variable_tiempo_muestreo = abs(int(child2.text))

                for child2 in child.iter('Numero_Muestras'):
                    #obj_principal.variable_numero_muestras = abs(int(child2.text))
                    variable_numero_muestras = abs(int(child2.text))

            # ----------------------- Linea -----------------------
            for child in root.iter('Linea'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Bloque_Inicio'):
                    bloqueInicio = child2.text

                for child2 in child.iter('Bloque_Fin'):
                    bloqueFin = child2.text

                for child2 in child.iter('Nodos'):
                    nodos = eval(child2.text)

                temp = lista[2].abrirArchivo(lista, nombre, bloqueInicio, nodos)
                temp.bloqueFin = bloqueFin

            # ----------------------- ADC -----------------------
            for child in root.iter('ADC'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[3].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Rango'):
                    temp.variable_rango = int(child2.text)

                for child2 in child.iter('Variable_Tiempo_Muestreo'):
                    temp.variable_tiempo_muestreo = int(child2.text)

                for child2 in child.iter('Variable_Ganancia'):
                    temp.variable_ganancia = eval(child2.text)

            # ----------------------- PID -----------------------
            for child in root.iter('PID'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[4].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada1 = child2.text

                for child2 in child.iter('Entrada_2'):
                    temp.entrada2 = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Tipo_Pid'):
                    temp.variable_tipo_pid = int(child2.text)

                for child2 in child.iter('Variable_Parametro_P'):
                    temp.variable_parametro_p = eval(child2.text)

                for child2 in child.iter('Variable_Parametro_I'):
                    temp.variable_parametro_i = eval(child2.text)

                for child2 in child.iter('Variable_Parametro_D'):
                    temp.variable_parametro_d = eval(child2.text)

                for child2 in child.iter('Variable_Parametro_C'):
                    temp.variable_parametro_c = eval(child2.text)

                for child2 in child.iter('Variable_Parametro_B'):
                    temp.variable_parametro_b = eval(child2.text)

                for child2 in child.iter('Variable_Parametro_N'):
                    temp.variable_parametro_n = eval(child2.text)

                for child2 in child.iter('Variable_Metodo_Integrador'):
                    temp.variable_metodo_integrador = child2.text

                for child2 in child.iter('Variable_Metodo_Filtro'):
                    temp.variable_metodo_filtro = child2.text

                for child2 in child.iter('Variable_Tiempo_Muestreo'):
                    temp.variable_tiempo_muestreo = int(child2.text)

                for child2 in child.iter('Variable_Tipo_Saturador'):
                    temp.variable_tipo_saturador = int(child2.text)

                for child2 in child.iter('Variable_Limite_Superior'):
                    temp.variable_limite_superior = eval(child2.text)

                for child2 in child.iter('Variable_Limite_Inferior'):
                    temp.variable_limite_inferior = eval(child2.text)

            # ----------------------- PWM -----------------------
            for child in root.iter('PWM'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[5].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Tipo'):
                    temp.variable_tipo = int(child2.text)

                for child2 in child.iter('Variable_Periodo'):
                    temp.variable_periodo = int(child2.text)

                for child2 in child.iter('Variable_Amplitud'):
                    temp.variable_amplitud = eval(child2.text)

            # ----------------------- RE -----------------------
            for child in root.iter('RE'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[6].abrirArchivo(lista, nombre, x, y)

                tipo_retroalimentacion = 1

                for child2 in child.iter('Variable_Tipo'):
                    tipo_retroalimentacion = int(child2.text)

                for child2 in child.iter('Tipo_RE'):
                    tipoRE = child2.text
                    temp.tipoRE = tipoRE
                    posicion = 45

                    if tipo_retroalimentacion == 1:

                        if tipoRE == "RE_1x1":
                            temp.imagen = PhotoImage(file="RE_1x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_1x2":
                            temp.imagen = PhotoImage(file="RE_1x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_2x1":
                            temp.imagen = PhotoImage(file="RE_2x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_2x2":
                            temp.imagen = PhotoImage(file="RE_2x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_3x1":
                            temp.imagen = PhotoImage(file="RE_3x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 52

                        if tipoRE == "RE_3x2":
                            temp.imagen = PhotoImage(file="RE_3x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 52

                        if tipoRE == "RE_4x1":
                            temp.imagen = PhotoImage(file="RE_4x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 58

                        if tipoRE == "RE_4x2":
                            temp.imagen = PhotoImage(file="RE_4x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 58

                    if tipo_retroalimentacion == 2:

                        if tipoRE == "RE_1x1":
                            temp.imagen = PhotoImage(file="REI_1x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_1x2":
                            temp.imagen = PhotoImage(file="REI_1x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_2x1":
                            temp.imagen = PhotoImage(file="REI_2x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_2x2":
                            temp.imagen = PhotoImage(file="REI_2x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 45

                        if tipoRE == "RE_3x1":
                            temp.imagen = PhotoImage(file="REI_3x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 52

                        if tipoRE == "RE_3x2":
                            temp.imagen = PhotoImage(file="REI_3x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 52

                        if tipoRE == "RE_4x1":
                            temp.imagen = PhotoImage(file="REI_4x1.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 58

                        if tipoRE == "RE_4x2":
                            temp.imagen = PhotoImage(file="REI_4x2.png")
                            temp.window.itemconfig(temp.nombre, image=temp.imagen)
                            posicion = 58

                    lista[1].delete(temp.label_con_nombre)
                    temp.labelNombre = temp.window.create_text(temp.posicionx,
                                                               temp.posiciony - posicion,
                                                               text=temp.nombre,
                                                               font=("Arial Rounded MT", -12, "bold"),
                                                               tags=temp.label_con_nombre)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada_1 = child2.text

                for child2 in child.iter('Entrada_2'):
                    temp.entrada_2 = child2.text

                for child2 in child.iter('Entrada_3'):
                    temp.entrada_3 = child2.text

                for child2 in child.iter('Entrada_4'):
                    temp.entrada_4 = child2.text

                for child2 in child.iter('Entrada_5'):
                    temp.entrada_5 = child2.text

                for child2 in child.iter('Entrada_6'):
                    temp.entrada_6 = child2.text

                for child2 in child.iter('Entrada_7'):
                    temp.entrada_7 = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida_1 = child2.text

                for child2 in child.iter('Salida_2'):
                    temp.salida_2 = child2.text

                for child2 in child.iter('Variable_Tipo'):
                    temp.variable_tipo = int(child2.text)

                for child2 in child.iter('Variable_N'):
                    temp.variable_n = int(child2.text)

                for child2 in child.iter('Variable_M'):
                    temp.variable_m = int(child2.text)

                for child2 in child.iter('Variable_Y1'):
                    temp.variable_matriz_y1 = child2.text

                for child2 in child.iter('Variable_Y2'):
                    temp.variable_matriz_y2 = child2.text

                for child2 in child.iter('Variable_K0'):
                    temp.variable_k0 = eval(child2.text)

                for child2 in child.iter('Variable_Matriz_K'):
                    temp.variable_matriz_k = child2.text

                for child2 in child.iter('Variable_Matriz_Ki'):
                    temp.variable_matriz_ki = child2.text

            # ----------------------- CTE -----------------------
            for child in root.iter('CTE'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[7].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Constante'):
                    temp.variable_constante = eval(child2.text)

            # ----------------------- FT -----------------------
            for child in root.iter('FT'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[8].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Tipo_FT'):
                    tipoFT = child2.text
                    temp.tipoFT = tipoFT

                    if tipoFT == "FT_1x1":
                        temp.imagen = PhotoImage(file="FT.png")
                        temp.window.itemconfig(temp.nombre, image=temp.imagen)

                    if tipoFT == "FT_2x1":
                        temp.imagen = PhotoImage(file="FT_r.png")
                        temp.window.itemconfig(temp.nombre, image=temp.imagen)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada_1 = child2.text

                for child2 in child.iter('Entrada_2'):
                    temp.entrada_2 = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Orden'):
                    temp.variable_orden = int(child2.text)

                for child2 in child.iter('Variable_Numerador'):
                    temp.variable_numerador = eval(child2.text)

                for child2 in child.iter('Variable_Denominador'):
                    temp.variable_denominador = eval(child2.text)

            # ----------------------- SAT -----------------------
            for child in root.iter('SAT'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[9].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Limite_Superior'):
                    temp.variable_limite_superior = eval(child2.text)

                for child2 in child.iter('Variable_Limite_Inferior'):
                    temp.variable_limite_inferior = eval(child2.text)

            # ----------------------- QDEC -----------------------
            for child in root.iter('QDEC'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[10].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Tamano_Contador'):
                    temp.variable_tamano_contador = int(child2.text)

                for child2 in child.iter('Variable_Tiempo_Muestreo'):
                    temp.variable_tiempo_muestreo = int(child2.text)

                for child2 in child.iter('Variable_Ganancia'):
                    temp.variable_ganancia = eval(child2.text)

            # ----------------------- ENTP -----------------------
            for child in root.iter('ENTP'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[11].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Variable_Nombre_Bloque'):

                    if child2.text is not None:
                        temp.variable_nombre_bloque = child2.text
                    else:
                        temp.variable_nombre_bloque = ""

                    temp.tupla_listas[1].delete(temp.label_con_nombre)

                    temp.labelNombre = temp.window.create_text(temp.posicionx + 6,
                                                               temp.posiciony - 32,
                                                               text=temp.variable_nombre_bloque,
                                                               font=("Arial Rounded MT", -12, "bold"),
                                                               tags=temp.label_con_nombre)

            # ----------------------- SALP -----------------------
            for child in root.iter('SALP'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[12].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Nombre_Bloque'):

                    if child2.text is not None:
                        temp.variable_nombre_bloque = child2.text
                    else:
                        temp.variable_nombre_bloque = ""

                    temp.tupla_listas[1].delete(temp.label_con_nombre)

                    temp.labelNombre = temp.window.create_text(temp.posicionx - 6,
                                                               temp.posiciony - 32,
                                                               text=temp.variable_nombre_bloque,
                                                               font=("Arial Rounded MT", -12, "bold"),
                                                               tags=temp.label_con_nombre)

            # ----------------------- DAC -----------------------
            for child in root.iter('DAC'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[13].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Rango'):
                    temp.variable_rango = int(child2.text)

                for child2 in child.iter('Variable_Tiempo_Muestreo'):
                    temp.variable_tiempo_muestreo = int(child2.text)

                for child2 in child.iter('Variable_Ganancia'):
                    temp.variable_ganancia = eval(child2.text)

            # ----------------------- FLT -----------------------
            for child in root.iter('FLT'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[14].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_A1'):
                    temp.variable_a1 = eval(child2.text)

                for child2 in child.iter('Variable_A2'):
                    temp.variable_a2 = eval(child2.text)

                for child2 in child.iter('Variable_B0'):
                    temp.variable_b0 = eval(child2.text)

                for child2 in child.iter('Variable_B1'):
                    temp.variable_b1 = eval(child2.text)

                for child2 in child.iter('Variable_B2'):
                    temp.variable_b2 = eval(child2.text)

            # ----------------------- SCOPE -----------------------
            for child in root.iter('SCOPE'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[15].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Nombre_Bloque'):
                    temp.variable_nombre_bloque = child2.text

                    temp.tupla_listas[1].delete(temp.label_con_nombre)

                    temp.labelNombre = temp.window.create_text(temp.posicionx,
                                                               temp.posiciony - 45,
                                                               text=temp.variable_nombre_bloque,
                                                               font=("Arial Rounded MT", -12, "bold"),
                                                               tags=temp.label_con_nombre)
                    temp.window.tag_bind(temp.label_con_nombre, "<Double-Button-1>", temp.dobleClickTexto)

            # ----------------------- STEP -----------------------
            for child in root.iter('STEP'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[16].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Escalon'):
                    temp.variable_escalon = eval(child2.text)

                for child2 in child.iter('Variable_Valor_Inicial'):
                    temp.variable_valor_inicial = eval(child2.text)

                for child2 in child.iter('Variable_Valor_Final'):
                    temp.variable_valor_final = eval(child2.text)

            # ----------------------- TRAPECIO -----------------------
            for child in root.iter('TRAPECIO'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[17].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

                for child2 in child.iter('Variable_Amplitud'):
                    temp.variable_amplitud = eval(child2.text)

                for child2 in child.iter('Variable_Tiempo_Inicio'):
                    temp.variable_tiempo_inicio = eval(child2.text)

                for child2 in child.iter('Variable_Tiempo_Rampa'):
                    temp.variable_tiempo_rampa = eval(child2.text)

                for child2 in child.iter('Variable_Tiempo_Alto'):
                    temp.variable_tiempo_alto = eval(child2.text)

            # ----------------------- DER -----------------------
            for child in root.iter('DER'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[18].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida_1 = child2.text

                for child2 in child.iter('Salida_2'):
                    temp.salida_2 = child2.text

            # ----------------------- SUM -----------------------
            for child in root.iter('SUM'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[19].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada_1 = child2.text

                for child2 in child.iter('Entrada_2'):
                    temp.entrada_2 = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

            # ----------------------- REST -----------------------
            for child in root.iter('REST'):

                for child2 in child.iter('Nombre'):
                    nombre = child2.text

                for child2 in child.iter('Posicion_X'):
                    x = int(child2.text)

                for child2 in child.iter('Posicion_Y'):
                    y = int(child2.text)

                temp = lista[20].abrirArchivo(lista, nombre, x, y)

                for child2 in child.iter('Entrada_1'):
                    temp.entrada_1 = child2.text

                for child2 in child.iter('Entrada_2'):
                    temp.entrada_2 = child2.text

                for child2 in child.iter('Salida_1'):
                    temp.salida = child2.text

