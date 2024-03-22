import numpy as np


class Netlist():

    def __init__(self):

        self.lista = None
        # self.directorio = "/Users/usuario/Desktop/Protocolo_Comunicacion.txt"
        self.directorio = "Protocolo_Comunicacion.txt"
        self.file = open(self.directorio, "w")

    def listas(self, lista):

        self.lista = lista

    def generarNetlist(self):

        self.file.write("MOD\n")

        for i in range(3, len(self.lista)):

            if self.lista[i].tamano() != 0:

                actual = self.lista[i].cabeza
                
                self.file.write(actual.tipoNetlist + ",")
                self.file.write(str(self.lista[i].tamano()) + "\n")

        self.file.write("CON\n")
        # ADC / ID-ADC / ID_Parametro / <Parametro> /

        for i in range(3, len(self.lista)):

            if self.lista[i].tamano() != 0:
                actual = self.lista[i].cabeza

                while actual is not None:

                    if actual.tipo == "ADC":

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", actual.variable_rango)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_tiempo_muestreo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02", actual.variable_ganancia)

                    if actual.tipo == "PID":

                        variable = None
                        
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", int(actual.variable_tipo_pid) - 1)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_parametro_p)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02", actual.variable_parametro_i)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "03", actual.variable_parametro_d)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "04", actual.variable_parametro_c)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "05", actual.variable_parametro_b)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "06", actual.variable_parametro_n)

                        if actual.variable_metodo_integrador == "Backward Euler": variable = 1
                        if actual.variable_metodo_integrador == "Forward Euler": variable = 2
                        if actual.variable_metodo_integrador == "Trapezoidal": variable = 3

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "07", variable)

                        if actual.variable_metodo_filtro == "Backward Euler": variable = 1
                        if actual.variable_metodo_filtro == "Forward Euler": variable = 2
                        if actual.variable_metodo_filtro == "Trapezoidal": variable = 3

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "08", variable)

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "09", actual.variable_tiempo_muestreo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "10", actual.variable_tipo_saturador)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "11", actual.variable_limite_inferior)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "12", actual.variable_limite_superior)

                    if actual.tipo == "PWM":
                        
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", actual.variable_tipo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_periodo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02", actual.variable_amplitud)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "03", actual.variable_zona_muerta)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "04", actual.variable_limite_inferior)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "05", actual.variable_limite_superior)

                    if actual.tipo == "RE":
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", actual.variable_tipo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_n)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02", actual.variable_m)

                        m = np.matrix(actual.variable_matriz_k)
                        variable = []

                        if m.shape == (1, 1) or m.shape == (2, 1):
                            variable.append("[")
                            variable.append(str(float(m[0, 0])))

                        elif m.shape == (1, 2) or m.shape == (2, 2):
                            variable.append("[")
                            variable.append(str(float(m[0, 0])))
                            variable.append(",")
                            variable.append(str(float(m[0, 1])))

                        elif m.shape == (1, 3) or m.shape == (2, 3):
                            variable.append("[")
                            variable.append(str(float(m[0, 0])))
                            variable.append(",")
                            variable.append(str(float(m[0, 1])))
                            variable.append(",")
                            variable.append(str(float(m[0, 2])))

                        elif m.shape == (1, 4) or m.shape == (2, 4):
                            variable.append("[")
                            variable.append(str(float(m[0, 0])))
                            variable.append(",")
                            variable.append(str(float(m[0, 1])))
                            variable.append(",")
                            variable.append(str(float(m[0, 2])))
                            variable.append(",")
                            variable.append(str(float(m[0, 3])))

                        if m.shape == (2, 1):
                            variable.append(";")
                            variable.append(str(float(m[1, 0])))

                        elif m.shape == (2, 2):
                            variable.append(";")
                            variable.append(str(float(m[1, 0])))
                            variable.append(",")
                            variable.append(str(float(m[1, 1])))

                        elif m.shape == (2, 3):
                            variable.append(";")
                            variable.append(str(float(m[1, 0])))
                            variable.append(",")
                            variable.append(str(float(m[1, 1])))
                            variable.append(",")
                            variable.append(str(float(m[1, 2])))

                        elif m.shape == (2, 4):
                            variable.append(";")
                            variable.append(str(float(m[1, 0])))
                            variable.append(",")
                            variable.append(str(float(m[1, 1])))
                            variable.append(",")
                            variable.append(str(float(m[1, 2])))
                            variable.append(",")
                            variable.append(str(float(m[1, 3])))

                        variable.append("]")
                        variable = "".join(variable)

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "04", variable)

                        if actual.variable_tipo == 1:
                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "03", actual.variable_k0)

                        else:

                            m_ki = np.matrix(actual.variable_matriz_ki)
                            variable = []

                            if m_ki.shape == (1, 1):
                                variable.append("[")
                                variable.append(str(float(m_ki[0, 0])))
                                variable.append("]")

                            elif m_ki.shape == (2, 2):
                                variable.append("[")
                                variable.append(str(float(m_ki[0, 0])))
                                variable.append(",")
                                variable.append(str(float(m_ki[0, 1])))
                                variable.append(";")
                                variable.append(str(float(m_ki[1, 0])))
                                variable.append(",")
                                variable.append(str(float(m_ki[1, 1])))
                                variable.append("]")

                            variable = "".join(variable)

                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "05", variable)
                            

                        if actual.variable_matriz_y1 == "x1": variable = 1
                        if actual.variable_matriz_y1 == "x2": variable = 2
                        if actual.variable_matriz_y1 == "x3": variable = 3
                        if actual.variable_matriz_y1 == "x4": variable = 4

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "06", variable)

                        if actual.variable_matriz_y2 == "x1": variable = 1
                        if actual.variable_matriz_y2 == "x2": variable = 2
                        if actual.variable_matriz_y2 == "x3": variable = 3
                        if actual.variable_matriz_y2 == "x4": variable = 4

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "07", variable)

                        if actual.variable_tipo == 2:
                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "08", actual.variable_tipo_saturador)
                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "09", actual.variable_limite_inferior)
                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "10", actual.variable_limite_superior)

                    if actual.tipo == "CTE":

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00",  actual.variable_constante)

                    if actual.tipo == "FT":

                        if actual.tipoFT == "FT_1x1":
                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", "0")
                        else:
                            self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", "1")

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01",  actual.variable_orden)

                        variable = str(actual.variable_numerador)
                        variable = list(variable)

                        posicion = []
                        for i in range(0, len(variable)):
                            if variable[i] == " ":
                                posicion.append(i)

                        if posicion != []:

                            posicion.reverse()

                            for i in posicion:

                                del variable[i]

                        variable = "".join(variable)

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02",  variable)

                        variable = str(actual.variable_denominador)
                        variable = list(variable)

                        posicion = []
                        for i in range(0, len(variable)):
                            if variable[i] == " ":
                                posicion.append(i)

                        if posicion != []:

                            posicion.reverse()

                            for i in posicion:
                                del variable[i]

                        variable = "".join(variable)

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "03",  variable)

                    if actual.tipo == "SAT":

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00",  actual.variable_limite_inferior)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01",  actual.variable_limite_superior)

                    if actual.tipo == "QDEC":

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00",  actual.variable_tiempo_muestreo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01",  actual.variable_ganancia)

                    if actual.tipo == "ENTP":
                        nombre = ""
                        index = 0
                        for c in actual.variable_nombre_bloque:

                            if index > 11:  # Nombre a transferir debe ser maximo de 12 caracteres
                                break
                            index += 1
                            nombre = nombre + c
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", nombre)

                    if actual.tipo == "SALP":
                        nombre = ""
                        index = 0
                        for c in actual.variable_nombre_bloque:

                            if index > 11:  # Nombre a transferir debe ser maximo de 12 caracteres
                                break
                            index += 1
                            nombre = nombre + c
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", nombre)

                    if actual.tipo == "DAC":

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00",  actual.variable_rango)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01",  actual.variable_tiempo_muestreo)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02",  actual.variable_ganancia)

                    if actual.tipo == "FLT":

                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00",  actual.variable_a1)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01",  actual.variable_a2)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02",  actual.variable_b0)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "03",  actual.variable_b1)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "04",  actual.variable_b2)

                    if actual.tipo == "SCOPE":

                        nombre = ""
                        index = 0
                        for c in actual.variable_nombre_bloque:

                            if index > 11: # Nombre a transferir debe ser maximo de 12 caracteres
                                break
                            index += 1
                            nombre = nombre + c
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", nombre)

                    if actual.tipo == "STEP":
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", actual.variable_escalon)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_valor_inicial)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02", actual.variable_valor_final)

                    if actual.tipo == "TRAPECIO":
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", actual.variable_amplitud)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_tiempo_inicio)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "02", actual.variable_tiempo_rampa)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "03", actual.variable_tiempo_alto)

                    if actual.tipo == "DER":
                        #pass
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "00", actual.variable_frecuenciaNatural)
                        self.imprimirConfig(actual.tipoNetlist, actual.dato, "01", actual.variable_amortiguamientoRelativo)

                    if actual.tipo == "SUM":
                        pass

                    if actual.tipo == "REST":
                        pass

                    actual = actual.siguiente

        self.file.write("NET\n")

        actual = self.lista[2].cabeza

        while actual is not None:

            bInicio = self.buscarBloque(actual.bloqueInicio)
            bFin = self.buscarBloque(actual.bloqueFin)

            self.file.write(str(bInicio.tipoNetlist) + ",")
            self.file.write(str(bInicio.dato) + ",")

            tipo_bInicio = bInicio.tipo

            # Bloque Inicio de la conexion
            if tipo_bInicio == "ADC": self.file.write("1,")
            if tipo_bInicio == "PID": self.file.write("1,")
            if tipo_bInicio == "PWM": self.file.write("1,")

            if tipo_bInicio == "RE":

                if bInicio.salida_1 == actual.nombre: self.file.write("1,")
                if bInicio.salida_2 == actual.nombre: self.file.write("2,")

            if tipo_bInicio == "CTE": self.file.write("1,")
            if tipo_bInicio == "FT": self.file.write("1,")
            if tipo_bInicio == "SAT": self.file.write("1,")
            if tipo_bInicio == "QDEC": self.file.write("1,")
            if tipo_bInicio == "SALP": self.file.write("1,")
            if tipo_bInicio == "DAC": self.file.write("1,")
            if tipo_bInicio == "FLT": self.file.write("1,")
            if tipo_bInicio == "SCOPE": self.file.write("1,")
            if tipo_bInicio == "STEP": self.file.write("1,")
            if tipo_bInicio == "TRAPECIO": self.file.write("1,")

            if tipo_bInicio == "DER":

                if bInicio.salida_1 == actual.nombre: self.file.write("1,")
                if bInicio.salida_2 == actual.nombre: self.file.write("2,")

            if tipo_bInicio == "SUM": self.file.write("1,")
            if tipo_bInicio == "REST": self.file.write("1,")

            self.file.write(str(bFin.tipoNetlist) + ",")
            self.file.write(str(bFin.dato) + ",")

            tipo_bFin = bFin.tipo

            if tipo_bFin == "ADC": self.file.write("1")
            if tipo_bFin == "PID":

                if bFin.entrada1 == actual.nombre: self.file.write("1")
                if bFin.entrada2 == actual.nombre: self.file.write("2")

            if tipo_bFin == "PWM": self.file.write("1")

            if tipo_bFin == "RE":

                if bFin.entrada_1 == actual.nombre: self.file.write("1")
                if bFin.entrada_2 == actual.nombre: self.file.write("2")
                if bFin.entrada_3 == actual.nombre: self.file.write("3")
                if bFin.entrada_4 == actual.nombre: self.file.write("4")
                if bFin.entrada_5 == actual.nombre: self.file.write("5")
                if bFin.entrada_6 == actual.nombre: self.file.write("6")
                if bFin.entrada_7 == actual.nombre: self.file.write("7")

            if tipo_bFin == "FT":

                if bFin.entrada_1 == actual.nombre: self.file.write("1")
                if bFin.entrada_2 == actual.nombre: self.file.write("2")

            if tipo_bFin == "SAT": self.file.write("1")
            if tipo_bFin == "QDEC": self.file.write("1")
            if tipo_bFin == "ENTP": self.file.write("1")
            if tipo_bFin == "DAC": self.file.write("1")
            if tipo_bFin == "FLT": self.file.write("1")
            if tipo_bFin == "SCOPE": self.file.write("1")
            if tipo_bFin == "STEP": self.file.write("1")
            if tipo_bFin == "TRAPECIO": self.file.write("1")
            if tipo_bFin == "DER": self.file.write("1")

            if tipo_bFin == "SUM":

                if bFin.entrada_1 == actual.nombre: self.file.write("1")
                if bFin.entrada_2 == actual.nombre: self.file.write("2")

            if tipo_bFin == "REST":

                if bFin.entrada_1 == actual.nombre: self.file.write("1")
                if bFin.entrada_2 == actual.nombre: self.file.write("2")

            self.file.write("\n")
            actual = actual.siguiente

        self.file.write("END")
        self.file.close()

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

    def imprimirConfig(self, tipo, dato, numero, variable):

        self.file.write(str(tipo)+"/")
        self.file.write(str(dato)+"/")
        self.file.write(str(numero)+"/")
        self.file.write(str(variable)+"/\n")
