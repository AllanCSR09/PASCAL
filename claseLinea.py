from tkinter import *


class NodoLinea:
    def __init__(self, id_Linea, tupla_listas, bloqueInicio, nodosLinea):

        self.dato = id_Linea
        self.tipo = "Linea"
        self.nombre = "Linea_"+str(id_Linea)

        self.nodos = nodosLinea
        self.nodos_a_dibujar = nodosLinea

        self.bloqueInicio = bloqueInicio  # Salida
        self.bloqueFin = None  # Entrada

        self.dx = None
        self.dy = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]

        self.tupla_listas = tupla_listas  # Contiene informacion de todas las listas

        # Prueba
        self.creandoLinea = None
        self.tipoCreandoLinea = None
        # True -> Desde Salida hacia Entrada
        # False -> Desde Entrada hacia Salida

        self.pruebaCambio = True
        self.cancelarConexion = False

        self.borrandoElemento = False

    def creandoConexion(self):

        for i in range(2, len(self.tupla_listas)):
            actual = self.tupla_listas[i].cabeza

            while actual is not None:
                actual.creandoLinea = self.nombre
                actual.tipoCreandoLinea = self.tipoCreandoLinea
                actual = actual.siguiente

    def noCreandoConexion(self):

        for i in range(2, len(self.tupla_listas)):
            actual = self.tupla_listas[i].cabeza

            while actual is not None:
                actual.creandoLinea = None
                actual.tipoCreandoLinea = None
                if actual.nombre == self.bloqueInicio and self.cancelarConexion:

                    if actual.tipo == "PID":
                        if actual.entrada1 == self.nombre: actual.entrada1 = None
                        if actual.entrada2 == self.nombre: actual.entrada2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "RE":
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.entrada_3 == self.nombre: actual.entrada_3 = None
                        if actual.entrada_4 == self.nombre: actual.entrada_4 = None
                        if actual.entrada_5 == self.nombre: actual.entrada_5 = None
                        if actual.entrada_6 == self.nombre: actual.entrada_6 = None
                        if actual.entrada_7 == self.nombre: actual.entrada_7 = None

                        if actual.salida_1 == self.nombre: actual.salida_1 = None
                        if actual.salida_2 == self.nombre: actual.salida_2 = None

                    elif actual.tipo == "CTE":
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "FT":
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "STEP":
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "TRAPECIO":
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "DER":
                        if actual.entrada == self.nombre: actual.entrada = None

                        if actual.salida_1 == self.nombre: actual.salida_1 = None
                        if actual.salida_2 == self.nombre: actual.salida_2 = None

                    elif actual.tipo == "SUM":
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "REST":
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "SALP":
                        if actual.salida == self.nombre: actual.salida = None

                    elif actual.tipo == "ENTP":
                        if actual.entrada == self.nombre: actual.entrada = None

                    else:
                        if actual.entrada == self.nombre: actual.entrada = None
                        if actual.salida == self.nombre: actual.salida = None

                actual = actual.siguiente

    def pintarLinea(self, event):
        # !!!
        # mx = canvas.canvasx(event.x)
        # canvasobject = self.window.find_overlapping(event.x-3, event.y-3, event.x+3, event.y+3)

        # if len(canvasobject) == 2:
        #     t = self.window.gettags(canvasobject[1])
        #     print(t[0])
        #     r = self.tupla_listas[3].obtenerCoordenadas(t[0])
        #     print(r)

        #  (a,b) o--------------o (c,d)
        a = self.nodos[len(self.nodos) - 2]
        b = self.nodos[len(self.nodos) - 1]
        c = event.x
        d = event.y

        if self.pruebaCambio:
            self.nodos_a_dibujar = self.nodos + [c, b, c, d]
        else:
            self.nodos_a_dibujar = self.nodos + [a, d, c, d]

        self.window.delete(self.nombre)
        self.window.create_line(self.nodos_a_dibujar, width=3, tags=self.nombre, joinstyle=ROUND, arrow=LAST)
        self.window.tag_lower(self.nombre)  # tag_raise , tag_lower = send to back

    def cancelar(self, event):

        self.window.unbind("<Leave>")  # 3 Windows/Unix

        self.cancelarConexion = True
        self.window.delete(self.nombre)
        self.window.unbind("<Motion>")
        self.window.unbind(self.nombre)
        self.mainWindow.unbind("<Escape>")
        self.mainWindow.unbind("<space>")
        self.noCreandoConexion()
        self.tupla_listas[2].remover(self.dato)

    def dobleClickLinea(self, event):
        pass

    def soltarLinea(self, event):
        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy
        pass

    def clickIzquierdoLinea(self, event):
        # x, y = self.window.winfo_pointerxy()
        # ids = self.window.find_overlapping(x, y, x, y)
        # print(event.widget.find_withtag("current"))

        if self.borrandoElemento:
            self.eliminarConexion()

        if self.creandoLinea == self.nombre:

            if len(self.nodos) > 3:

                self.nodos = self.nodos_a_dibujar

                tamano = len(self.nodos)
                if self.nodos[tamano-4] == self.nodos[tamano-6] == self.nodos[tamano-8]:
                    del self.nodos[tamano-6:tamano-4]
                elif self.nodos[tamano-3] == self.nodos[tamano-5] == self.nodos[tamano-7]:
                    del self.nodos[tamano-6:tamano-4]
            else:
                self.nodos = self.nodos_a_dibujar

    def prueba(self, event):
        if len(self.nodos) > 2:
            self.pruebaCambio = not self.pruebaCambio  # Forma de la conexion

    def clickDerechoLinea(self, event):

        self.eliminarConexion()

    def eliminarConexion(self):

        if self.creandoLinea is None:

            for i in range(3, len(self.tupla_listas)):
                actual = self.tupla_listas[i].cabeza

                while actual is not None:

                    if i == 4:  # Caso PID
                        if actual.entrada1 == self.nombre: actual.entrada1 = None
                        if actual.entrada2 == self.nombre: actual.entrada2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 6:  # Caso RE

                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.entrada_3 == self.nombre: actual.entrada_3 = None
                        if actual.entrada_4 == self.nombre: actual.entrada_4 = None
                        if actual.entrada_5 == self.nombre: actual.entrada_5 = None
                        if actual.entrada_6 == self.nombre: actual.entrada_6 = None
                        if actual.entrada_7 == self.nombre: actual.entrada_7 = None

                        if actual.salida_1 == self.nombre: actual.salida_1 = None
                        if actual.salida_2 == self.nombre: actual.salida_2 = None

                    elif i == 7:  # Caso CTE
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 8:  # Caso FT
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 11:  # Caso ENTP
                        if actual.entrada == self.nombre: actual.entrada = None

                    elif i == 12:  # Caso SALP
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 16:  # Caso STEP
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 17:  # Caso TRAPECIO
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 18:  # Case DER
                        if actual.entrada == self.nombre: actual.entrada = None
                        if actual.salida_1 == self.nombre: actual.salida_1 = None
                        if actual.salida_2 == self.nombre: actual.salida_2 = None

                    elif i == 19:  # Caso SUM
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    elif i == 20:  # Caso REST
                        if actual.entrada_1 == self.nombre: actual.entrada_1 = None
                        if actual.entrada_2 == self.nombre: actual.entrada_2 = None
                        if actual.salida == self.nombre: actual.salida = None

                    else:
                        if actual.entrada == self.nombre: actual.entrada = None
                        if actual.salida == self.nombre: actual.salida = None

                    actual = actual.siguiente

            self.window.delete(self.nombre)
            self.window.unbind(self.nombre)
            self.tupla_listas[2].remover(self.dato)

    def enMovimientoLinea(self, event):
        pass

    def salirLinea(self, event):  # Borrar circulos en los nodos
        self.window.delete(self.nombre+"c")


class ListaLinea:

    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self, tupla_listas, bloqueInicio, coordenadasNodos, tipoLinea):

        # tipoLinea: True -> Creando desde salida del bloque - False -> desde entrada

        actual = self.cabeza
        done = False
        if actual is None:
            item = 0
        else:

            item = 0

            while not done:
                if self.buscar(item) is True:
                    item = item + 1
                else:
                    done = True

        temp = NodoLinea(item, tupla_listas, bloqueInicio, coordenadasNodos)
        temp.tipoCreandoLinea = tipoLinea
        temp.siguiente = self.cabeza
        self.cabeza = temp
        temp.creandoConexion()
        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickLinea)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.soltarLinea)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoLinea)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoLinea)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoLinea)
        temp.window.bind("<Leave>", temp.cancelar)  # 3 Windows/Unix

        # Unbind teclado
        temp.window.bind("<Motion>", temp.pintarLinea)
        temp.mainWindow.bind("<Escape>", temp.cancelar)
        temp.mainWindow.bind("<space>", temp.prueba)

        temp.window.tag_bind(temp.nombre, "<Leave>", temp.salirLinea)

# -----------------------------------------------------
    def abrirArchivo(self, tupla_listas, nombre, bloqueInicio, coordenadasNodos):

        n = 0
        for i in nombre:
            if i == "_":
                n = n + 1
                break
            n = n + 1

        item = int(nombre[n:])

        temp = NodoLinea(item, tupla_listas, bloqueInicio, coordenadasNodos)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickLinea)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.soltarLinea)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoLinea)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoLinea)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoLinea)

        temp.window.create_line(coordenadasNodos, width=3, tags=temp.nombre, joinstyle=ROUND)
        temp.window.tag_lower(temp.nombre)
        temp.noCreandoConexion()

        return temp

# -----------------------------------------------------

    def vaciarLista(self):
        self.cabeza = None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente

        return contador

    def buscar(self, item):
        actual = self.cabeza
        encontrado = False

        while actual != None and not encontrado:
            if actual.dato == item:
                encontrado = True
            else:
                actual = actual.siguiente

        return encontrado

    def invertirNodos(self, nodos):

        c = []
        d = []
        tamano = len(nodos)
        for i in range(0, tamano, 2):
            c.append(nodos[i])
            d.append(nodos[i + 1])

        c = list(reversed(c))
        d = list(reversed(d))

        n = []
        tamano = len(c)

        for i in range(0, tamano):
            n.append(c[i])
            n.append(d[i])

        return n

    def remover(self, item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.dato == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.siguiente

        if previo == None:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente

    def ultimoNodo(self, nombreLinea, nombre, coordenadas):
        actual = self.cabeza
        encontrado = False

        while actual != None and not encontrado:
            if actual.nombre == nombreLinea:
                encontrado = True
                actual.bloqueFin = nombre
                # (a,b) o------------o (c,d)

                tamano = len(actual.nodos)

                a = actual.nodos[tamano - 2]
                b = actual.nodos[tamano - 1]
                c = coordenadas[0]
                d = coordenadas[1]

                if tamano == 2:
                    q = int((a + c) / 2)
                    nodos = [q, b, q, d, c, d]
                elif c < a and actual.tipoCreandoLinea:
                    nodos = [c - 30, b, c - 30, d, c, d]
                elif c > a and not actual.tipoCreandoLinea:
                    nodos = [c + 30, b, c + 30, d, c, d]

                else:
                    nodos = [a, d, c, d]

                actual.nodos = actual.nodos + nodos

                if not actual.tipoCreandoLinea:
                    actual.nodos = self.invertirNodos(actual.nodos)
                    actual.bloqueInicio, actual.bloqueFin = actual.bloqueFin, actual.bloqueInicio

                if tamano > 3:
                    tamano = len(actual.nodos)
                    if actual.nodos[tamano - 4] == actual.nodos[tamano - 6] == actual.nodos[tamano - 8]:
                        del actual.nodos[tamano - 6:tamano - 4]
                    elif actual.nodos[tamano - 3] == actual.nodos[tamano - 5] == actual.nodos[tamano - 7]:
                        del actual.nodos[tamano - 6:tamano - 4]

                actual.window.delete(actual.nombre)
                actual.window.create_line(actual.nodos, width=3, tags=actual.nombre, joinstyle=ROUND)
                actual.window.tag_lower(actual.nombre)
                actual.window.unbind("<Motion>")
                actual.window.unbind("<Leave>")
                actual.noCreandoConexion()
                actual.mainWindow.unbind("<space>")
                actual.mainWindow.unbind("<Escape>")

            else:
                actual = actual.siguiente

    def obtenerEntradaYSalidas(self, nombre, entrada_salida):
        actual = self.cabeza
        encontrado = False

        while actual != None and not encontrado:
            if actual.nombre == nombre:
                if entrada_salida == "entrada":
                    return actual.bloqueFin
                if entrada_salida == "salida":
                    return actual.bloqueInicio

                encontrado = True
            else:
                actual = actual.siguiente

    def moverLinea(self, linea, bloque, dx, dy):
        actual = self.cabeza
        encontrado = False
        while actual is not None and not encontrado:

            if actual.nombre == linea:
                encontrado = True

                if bloque == actual.bloqueInicio:
                    # mover primeras dos coordenadas
                    actual.nodos[0:2] = [actual.nodos[0]+dx, actual.nodos[1]+dy]
                    actual.nodos[3] = actual.nodos[3]+dy

                    actual.window.delete(actual.nombre)
                    actual.window.create_line(actual.nodos, width=3, tags=actual.nombre, joinstyle=ROUND)
                    actual.window.tag_lower(actual.nombre)

                if bloque == actual.bloqueFin:
                    # mover ultimas dos coordenadas
                    tamano = len(actual.nodos)
                    actual.nodos[tamano-2:] = [actual.nodos[tamano-2] + dx, actual.nodos[tamano-1] + dy]
                    actual.nodos[tamano-3] = actual.nodos[tamano-3] + dy

                    actual.window.delete(actual.nombre)
                    actual.window.create_line(actual.nodos, width=3, tags=actual.nombre, joinstyle=ROUND)
                    actual.window.tag_lower(actual.nombre)

            else:
                actual = actual.siguiente

    def eliminarConexion(self, conexion):
        actual = self.cabeza
        encontrado = False

        while not encontrado and actual is not None:

            if actual.nombre == conexion:
                encontrado = True

                actual.eliminarConexion()

            actual = actual.siguiente
