from tkinter import *
from tkinter import messagebox
import Simulacion
from tkinter import ttk


class NodoSCOPE:
    def __init__(self, id_SCOPE, tupla_listas, px, py):

        self.dato = id_SCOPE
        self.tipo = "SCOPE"
        self.nombre = "SCOPE_"+str(id_SCOPE)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "P"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada = None
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="SCOPE.png")

        self.icono = self.window.create_image(px, py, image=self.imagen, tags=self.nombre)
        self.label_con_nombre = self.nombre + "l"  # tag etiqueta con nombre

        self.labelNombre = self.window.create_text(self.posicionx,
                                                   self.posiciony-45,
                                                   text=self.nombre,
                                                   font=("Arial Rounded MT", -12, "bold"),
                                                   tags=self.label_con_nombre)

        self.window.tag_bind(self.label_con_nombre, "<Double-Button-1>", self.dobleClickTexto)

        # - - - - - -

        self.estado_labelSalida1 = False
        self.labelSalida1 = self.nombre + "s1"

        self.estado_labelEntrada1 = False
        self.labelEntrada1 = self.nombre + "e1"

        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

        # Variables ------------------------
        self.variable_nombre_bloque = self.nombre
        self.variable_mostrar_ocultar = 1

        # Simulacion -----------------------
        self.simulacion_datos = []
        self.simulacion_tiempo = []

    def dobleClickTexto(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowSCOPE = Toplevel(self.mainWindow)
            self.windowSCOPE.resizable(False, False)
            self.windowSCOPE.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowSCOPE, bg="#2C2C2C")
            self.frame2 = Frame(self.windowSCOPE, bg="white")
            self.frame3 = Frame(self.windowSCOPE, bg="white")


            self.imagen_ventana = PhotoImage(file="SCOPEv.png")
            self.imagen_ventana_label = Label(self.frame1,
                                              image=self.imagen_ventana,
                                              borderwidth=0,
                                              highlightthickness=0,
                                              bg="#2C2C2C",
                                              padx=0,
                                              pady=10)

            self.imagen_ventana_label.image = self.imagen_ventana
            self.imagen_ventana_label.pack(side=LEFT, padx=10)

            Label(self.frame1, text=self.nombre, bg="#2C2C2C", fg="White",
                  font=("Arial Rounded MT", -20)).pack(side=LEFT)

            # -------------------- FRAME 2 --------------------



            self.c = StringVar()

            if self.variable_nombre_bloque is None:
                self.c.set("PLANTA")
            else:
                self.c.set(str(self.variable_nombre_bloque))

            Label(self.frame2, text="Nombre:").grid(row=1, column=0, sticky=W, padx=(20,0), pady=(20, 0))
            ttk.Entry(self.frame2, width=22, textvariable=self.c).grid(row=1, column=1, sticky=W, padx=(0,20), pady=(20, 0))

            self.mostrar_ocultar = IntVar()
            if self.variable_mostrar_ocultar == 1:
                self.mostrar_ocultar.set(1)
            else:
                self.mostrar_ocultar.set(0)

            ttk.Checkbutton(self.frame2, text="Mostrar / Ocultar", variable=self.mostrar_ocultar) \
                .grid(row=2, column=1, sticky=E, padx=(0, 20), pady=(0, 10))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", width=8, command=lambda: self.cerrarVentanaSCOPE("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", width=8, command=lambda: self.cerrarVentanaSCOPE("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowSCOPE.protocol("WM_DELETE_WINDOW", self.cerrarVentanaSCOPE)

            self.windowSCOPE.withdraw()
            self.windowSCOPE.update_idletasks()
            x = (self.windowSCOPE.winfo_screenwidth() - self.windowSCOPE.winfo_reqwidth()) / 2
            y = (self.windowSCOPE.winfo_screenheight() - self.windowSCOPE.winfo_reqheight()) / 2
            self.windowSCOPE.geometry("+%d+%d" % (x, y))

            self.windowSCOPE.deiconify()

            # Color
            s = ttk.Style()
            s.configure('Style.TRadiobutton',
                        background="White",
                        foreground='black')
            s1 = ttk.Style()
            s1.configure('Style2.TCheckbutton',
                         background="White",
                         foreground='black')
            for wid in self.frame2.winfo_children():
                if wid.winfo_class() == 'Label':
                    wid.configure(bg="white")
                if wid.winfo_class() == 'TRadiobutton':
                    wid.configure(style='Style.TRadiobutton')
                if wid.winfo_class() == 'Message':
                    wid.configure(bg='white')
                if wid.winfo_class() == 'TCheckbutton':
                    wid.configure(style='Style2.TCheckbutton')

        else:
            self.windowSCOPE.lift()

    def dobleClickSCOPE(self, event):

        import matplotlib.pyplot as plt

        plt.figure(self.nombre)
        plt.plot(self.simulacion_tiempo, self.simulacion_datos, label=self.variable_nombre_bloque)
        plt.legend()
        plt.show(block=False)

    def cerrarVentanaSCOPE(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            try:

                error = 1
                nombre = self.c.get()

                if nombre == "":
                    nombre = self.nombre

                estado = True
                for i in nombre:
                    if i != " ":
                        estado = False

                    if i == "/":
                        error = 2
                        raise Exception

                if len(nombre) > 25:
                    error = 3
                    raise Exception

                if estado:
                    nombre = self.nombre

                self.tupla_listas[1].delete(self.label_con_nombre)

                self.labelNombre = self.window.create_text(self.posicionx,
                                                           self.posiciony - 45,
                                                           text=nombre,
                                                           font=("Arial Rounded MT", -12, "bold"),
                                                           tags=self.label_con_nombre)

                self.window.tag_bind(self.label_con_nombre, "<Double-Button-1>", self.dobleClickTexto)

                self.variable_nombre_bloque = nombre
                self.variable_mostrar_ocultar = self.mostrar_ocultar.get()

                self.ventanaCerrada = True
                self.windowSCOPE.destroy()

            except Exception:

                if error == 1:
                    messagebox.showerror("Error", "Nombre inválido")
                if error == 2:
                    messagebox.showerror("Error", "Nombre inválido. El nombre no puede contener el carácter \"/\"")
                if error == 3:
                    messagebox.showerror("Error", "Nombre inválido. El nombre debe contener como máximo 25 caracteres")

                self.windowSCOPE.lift()

        else:
            self.ventanaCerrada = True
            self.windowSCOPE.destroy()

    def arrastrarSCOPE(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoSCOPE(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarSCOPE()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida SCOPE

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada SCOPE

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx-32, self.posiciony-1)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

    def clickDerechoSCOPE(self, event):

        self.eliminarSCOPE()

    def eliminarSCOPE(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelSalida1)
            self.window.unbind(self.nombre)

            if self.entrada is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada)
            if self.salida is not None:
                self.tupla_listas[2].eliminarConexion(self.salida)

            self.tupla_listas[15].remover(self.nombre)

    def enMovimientoSCOPE(self, event):

        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------
            if self.entrada is not None and self.entrada != self.salida:
                self.tupla_listas[2].moverLinea(self.entrada, self.nombre,
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
        y_icono = abs(event.y - self.posiciony)
        if -38 < x_icono < -28 and 6 > y_icono:

            if not self.estado_labelEntrada1:
                self.window.create_text(self.posicionx-38,
                                        self.posiciony+20,
                                        text="Entrada 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelEntrada1)
                self.estado_labelEntrada1 = True

        elif 38 > x_icono > 28 and 6 > y_icono:

            if not self.estado_labelSalida1:
                self.window.create_text(self.posicionx+38,
                                        self.posiciony+20,
                                        text="Salida 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelSalida1)
                self.estado_labelSalida1 = True
        else:
            self.window.delete(self.labelSalida1, self.labelEntrada1)
            self.estado_labelSalida1 = False
            self.estado_labelEntrada1 = False

    def dentroDelIcono(self, event):
        # self.window.create_text(self.posicionx,
        #                         self.posiciony-51,
        #                         text=self.nombre,
        #                         font=("Arial Rounded MT", -12, "bold"),
        #                         tags=self.label_con_nombre)
        pass

    def afueraDelIcono(self, event):
        #  self.window.delete(self.label_con_nombre)
        self.window.delete(self.labelSalida1, self.labelEntrada1)
        self.estado_labelSalida1 = False
        self.estado_labelEntrada1 = False

# --------------------------------------------
    def senal_nombres(self, lista_nombres):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada, self.nombre)
            sim_entrada1.senal_nombres(lista_nombres).append(self.nombre)
            return lista_nombres
        else:
            lista_nombres.append(self.nombre)
            return lista_nombres

    def senal_simulacion(self, n, ts, conexion):

        if n == 0:
            self.simulacion_datos = []
            self.simulacion_tiempo = []

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada, self.nombre)
            ent1 = float(sim_entrada1.senal_simulacion(n, ts, self.entrada))

            if ent1 < -1e20:
                ent1 = -1e20

            if ent1 > 1e20:
                ent1 = 1e20

            self.simulacion_datos.append(ent1)
            self.simulacion_tiempo.append(ts)

            return ent1
        else:

            self.simulacion_datos.append(0)
            self.simulacion_tiempo.append(ts)
            return 0


class ListaSCOPE:

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

        temp = NodoSCOPE(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickSCOPE)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarSCOPE)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoSCOPE)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoSCOPE)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoSCOPE) # 3 Windows/Unix
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

        temp = NodoSCOPE(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickSCOPE)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarSCOPE)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoSCOPE)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoSCOPE)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoSCOPE)  # 3 Windows/Unix
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
