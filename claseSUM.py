from tkinter import *
import Simulacion


class NodoSUM:
    def __init__(self, id_SUM, tupla_listas, px, py):

        self.dato = id_SUM
        self.tipo = "SUM"
        self.nombre = "SUM_"+str(id_SUM)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "L"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada_1 = None
        self.entrada_2 = None

        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="SUM.png")

        self.icono = self.window.create_image(px, py, image=self.imagen, tags=self.nombre)
        self.label_con_nombre = self.nombre + "l"  # tag etiqueta con nombre

        self.labelNombre = self.window.create_text(self.posicionx,
                                                   self.posiciony-45,
                                                   text=self.nombre,
                                                   font=("Arial Rounded MT", -12, "bold"),
                                                   tags=self.label_con_nombre)

        # - - - - - -

        self.estado_labelSalida1 = False
        self.labelSalida1 = self.nombre + "s1"

        self.estado_labelEntrada1 = False
        self.labelEntrada1 = self.nombre + "e1"

        self.estado_labelEntrada2 = False
        self.labelEntrada2 = self.nombre + "e2"


        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

    def arrastrarSUM(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoSUM(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarSUM()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida SUM

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada1 SUM

                if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 32, self.posiciony-14)
                    self.entrada_1 = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada_1 is None:
                    coord = [self.posicionx - 32, self.posiciony-14]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada_1 = self.creandoLinea

            if -38 < self.dx < -28 and 19 > self.dy > 7:  # Entrada2 SUM

                if self.creandoLinea is not None and self.entrada_2 is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 32, self.posiciony+12)
                    self.entrada_2 = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada_2 is None:
                    coord = [self.posicionx - 32, self.posiciony+12]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada_2 = self.creandoLinea

    def clickDerechoSUM(self, event):

        self.eliminarSUM()

    def eliminarSUM(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelEntrada2)
            self.window.delete(self.labelSalida1)
            self.window.unbind(self.nombre)

            if self.entrada_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_1)
            if self.entrada_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_2)
            if self.salida is not None:
                self.tupla_listas[2].eliminarConexion(self.salida)

            self.tupla_listas[19].remover(self.nombre)

    def enMovimientoSUM(self, event):
        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------
            if self.entrada_1 is not None and self.entrada_1 != self.salida:
                self.tupla_listas[2].moverLinea(self.entrada_1, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_2 is not None and self.entrada_2 != self.salida:
                self.tupla_listas[2].moverLinea(self.entrada_2, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.salida is not None:
                self.tupla_listas[2].moverLinea(self.salida, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)
            # ----------------------------------
            self.posicionx = event.x - self.dx
            self.posiciony = event.y - self.dy

    def sobreIcono(self, event):

        x_icono = event.x - self.posicionx
        y_icono = event.y - self.posiciony

        if -38 < x_icono < -28 and -19 < y_icono < -7:
            if not self.estado_labelEntrada1:
                self.window.create_text(self.posicionx-38,
                                        self.posiciony+5,
                                        text="Entrada 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelEntrada1)
                self.estado_labelEntrada1 = True

        elif -38 < x_icono < -28 and 19 > y_icono > 7:
            if not self.estado_labelEntrada2:
                self.window.create_text(self.posicionx-38,
                                        self.posiciony+35,
                                        text="Entrada 2",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelEntrada2)
                self.estado_labelEntrada2 = True

        elif 38 > x_icono > 28 and 6 > abs(y_icono):
            if not self.estado_labelSalida1:
                self.window.create_text(self.posicionx+38,
                                        self.posiciony+20,
                                        text="Salida 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelSalida1)
                self.estado_labelSalida1 = True
        else:
            self.window.delete(self.labelSalida1, self.labelEntrada1, self.labelEntrada2)
            self.estado_labelSalida1 = False
            self.estado_labelEntrada1 = False
            self.estado_labelEntrada2 = False

    def dentroDelIcono(self, event):
        # self.window.create_text(self.posicionx,
        #                         self.posiciony-51,
        #                         text=self.nombre,
        #                         font=("Arial Rounded MT", -12, "bold"),
        #                         tags=self.label_con_nombre)
        pass

    def afueraDelIcono(self, event):
        #  self.window.delete(self.label_con_nombre)
        self.window.delete(self.labelSalida1, self.labelEntrada1, self.labelEntrada2)
        self.estado_labelSalida1 = False
        self.estado_labelEntrada1 = False
        self.estado_labelEntrada2 = False

# --------------------------------------------
    def senal_nombres(self, lista_nombres):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada_1 is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
            sim_entrada1.senal_nombres(lista_nombres)

        if self.entrada_2 is not None:
            sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
            sim_entrada2.senal_nombres(lista_nombres)

        lista_nombres.append(self.nombre)

        return lista_nombres

    def senal_simulacion(self, n, ts, conexion):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada_1 is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
            ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)
        else:
            ent1 = 0.0

        if self.entrada_2 is not None:
            sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
            ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada_2)
        else:
            ent2 = 0.0

        return ent1 + ent2


class ListaSUM:

    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self, tupla_listas, x, y):

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

        temp = NodoSUM(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarSUM)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoSUM)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoSUM)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoSUM) # 3 Windows/Unix
        temp.window.tag_bind(temp.nombre, "<Motion>", temp.sobreIcono)
        temp.window.tag_bind(temp.nombre, "<Enter>", temp.dentroDelIcono)
        temp.window.tag_bind(temp.nombre, "<Leave>", temp.afueraDelIcono)

    def abrirArchivo(self, tupla_listas, nombre, x, y):

        n = 0
        for i in nombre:
            if i == "_":
                n = n + 1
                break
            n = n + 1

        item = int(nombre[n:])

        temp = NodoSUM(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarSUM)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoSUM)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoSUM)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoSUM)  # 3 Windows/Unix
        temp.window.tag_bind(temp.nombre, "<Motion>", temp.sobreIcono)
        temp.window.tag_bind(temp.nombre, "<Enter>", temp.dentroDelIcono)
        temp.window.tag_bind(temp.nombre, "<Leave>", temp.afueraDelIcono)

        return temp

    def vaciarLista(self):
        self.cabeza = None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente

        return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False

        while actual != None and not encontrado:
            if actual.dato == item:
                encontrado = True
            else:
                actual = actual.siguiente

        return encontrado

    def remover(self, nombre):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.nombre == nombre:
                encontrado = True
            else:
                previo = actual
                actual = actual.siguiente

        if previo == None:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente

    def obtenerCoordenadas(self, nombre):
        actual = self.cabeza
        encontrado = False

        while actual!= None and not encontrado:
            if actual.nombre == nombre:
                coordenadas = (actual.posicionx, actual.posiciony)
                encontrado = True
                return coordenadas
            else:
                actual = actual.siguiente
        return None
