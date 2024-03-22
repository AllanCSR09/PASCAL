from tkinter import *
from tkinter import messagebox
import Simulacion
from tkinter import ttk


class NodoFLT:
    def __init__(self, id_FLT, tupla_listas, px, py):

        self.dato = id_FLT
        self.tipo = "FLT"
        self.nombre = "FLT_"+str(id_FLT)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "J"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada = None
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="FLT.png")

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

        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

        # Variables ------------------------
        self.variable_a1 = 1
        self.variable_a2 = 1
        self.variable_b0 = 1
        self.variable_b1 = 1
        self.variable_b2 = 1

        # Simulacion -----------------------
        self.y_n = 0
        self.y_n_1 = 0
        self.y_n_2 = 0

        self.x_n = 0
        self.x_n_1 = 0
        self.x_n_2 = 0

    def dobleClickFLT(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowFLT = Toplevel(self.mainWindow)
            self.windowFLT.resizable(False, False)
            self.windowFLT.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowFLT, bg="#2C2C2C")
            self.frame2 = Frame(self.windowFLT, bg="white")
            self.frame3 = Frame(self.windowFLT, bg="white")

            self.imagen_ventana = PhotoImage(file="FLTv.png")
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

            Label(self.frame2, text="Filtro", font=("Arial Rounded MT Bold", -18)) \
                .grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)

            imagen_funcion = PhotoImage(file="EcuacionFLT.png")
            imagen_funcion_label = Label(self.frame2,
                                               image=imagen_funcion,
                                               borderwidth=0,
                                               highlightthickness=0,
                                               padx=0,
                                               pady=0)
            imagen_funcion_label.image = imagen_funcion
            imagen_funcion_label.grid(row=1, column=0, columnspan=2, pady=(0,10))

            self.a1 = StringVar()
            self.a2 = StringVar()
            self.b0 = StringVar()
            self.b1 = StringVar()
            self.b2 = StringVar()

            if self.variable_a1 is None:
                self.a1.set(1)
            else:
                self.a1.set(str(self.variable_a1))

            if self.variable_a2 is None:
                self.a2.set(1)
            else:
                self.a2.set(str(self.variable_a2))

            if self.variable_b0 is None:
                self.b0.set(1)
            else:
                self.b0.set(str(self.variable_b0))

            if self.variable_b1 is None:
                self.b1.set(1)
            else:
                self.b1.set(str(self.variable_b1))

            if self.variable_b2 is None:
                self.b2.set(1)
            else:
                self.b2.set(str(self.variable_b2))

            Label(self.frame2, text="a1:").grid(row=2, column=0, sticky=W, padx=(20, 0))
            ttk.Entry(self.frame2, width=25, textvariable=self.a1).grid(row=2, column=1, sticky=W, padx=(0, 20))

            Label(self.frame2, text="a2:").grid(row=3, column=0, sticky=W, padx=(20, 0))
            ttk.Entry(self.frame2, width=25, textvariable=self.a2).grid(row=3, column=1, sticky=W, padx=(0, 20))

            Label(self.frame2, text="b0:").grid(row=4, column=0, sticky=W, padx=(20, 0))
            ttk.Entry(self.frame2, width=25, textvariable=self.b0).grid(row=4, column=1, sticky=W, padx=(0, 20))

            Label(self.frame2, text="b1:").grid(row=5, column=0, sticky=W, padx=(20, 0))
            ttk.Entry(self.frame2, width=25, textvariable=self.b1).grid(row=5, column=1, sticky=W, padx=(0, 20))

            Label(self.frame2, text="b2:").grid(row=6, column=0, sticky=W, padx=(20, 0), pady=(0, 20))
            ttk.Entry(self.frame2, width=25, textvariable=self.b2)\
                .grid(row=6, column=1, sticky=W, padx=(0, 20), pady=(0,20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", command=lambda: self.cerrarVentanaFLT("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", command=lambda: self.cerrarVentanaFLT("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowFLT.protocol("WM_DELETE_WINDOW", self.cerrarVentanaFLT)

            self.windowFLT.withdraw()
            self.windowFLT.update_idletasks()
            x = (self.windowFLT.winfo_screenwidth() - self.windowFLT.winfo_reqwidth()) / 2
            y = (self.windowFLT.winfo_screenheight() - self.windowFLT.winfo_reqheight()) / 2
            self.windowFLT.geometry("+%d+%d" % (x, y))

            self.windowFLT.deiconify()

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

            self.windowFLT.lift()

    def cerrarVentanaFLT(self, opcion="Cancelar"):

        if opcion == "Aceptar":


            try:
                valor_a1 = eval(self.a1.get())
                valor_a2 = eval(self.a2.get())
                valor_b0 = eval(self.b0.get())
                valor_b1 = eval(self.b1.get())
                valor_b2 = eval(self.b2.get())

                if type(valor_a1) is not int and type(valor_a1) is not float:
                    raise Exception

                if type(valor_a2) is not int and type(valor_a2) is not float:
                    raise Exception

                if type(valor_b0) is not int and type(valor_b0) is not float:
                    raise Exception

                if type(valor_b1) is not int and type(valor_b1) is not float:
                    raise Exception

                if type(valor_b2) is not int and type(valor_b2) is not float:
                    raise Exception

                self.variable_a1 = valor_a1
                self.variable_a2 = valor_a2
                self.variable_b0 = valor_b0
                self.variable_b1 = valor_b1
                self.variable_b2 = valor_b2

                self.ventanaCerrada = True
                self.windowFLT.destroy()

            except Exception:

                messagebox.showerror("Error", "Coeficiente Inválido")
                self.windowFLT.lift()

        else:
            self.ventanaCerrada = True
            self.windowFLT.destroy()
        

    def arrastrarFLT(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoFLT(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarFLT()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida FLT

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada FLT

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx-32, self.posiciony-1)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

    def clickDerechoFLT(self, event):

        self.eliminarFLT()

    def eliminarFLT(self):

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

            self.tupla_listas[14].remover(self.nombre)

    def enMovimientoFLT(self, event):

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

            self.y_n = 0.0
            self.y_n_1 = 0.0
            self.y_n_2 = 0.0

            self.x_n = 0.0
            self.x_n_1 = 0.0
            self.x_n_2 = 0.0

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada, self.nombre)
            ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada)
        else:
            ent1 = 0.0

        if ent1 < -1e20:
            ent1 = -1e20

        if ent1 > 1e20:
            ent1 = 1e20

        self.x_n = ent1

        b2 = self.variable_b2
        b1 = self.variable_b1
        b0 = self.variable_b0

        a1 = self.variable_a1
        a2 = self.variable_a2

        self.y_n = b2 * self.x_n_2 + b1 * self.x_n_1 + b0 * self.x_n - a1 * self.y_n_1 - a2 * self.y_n_2

        self.y_n_2 = self.y_n_1
        self.y_n_1 = self.y_n

        self.x_n_2 = self.x_n_1
        self.x_n_1 = self.x_n

        return float(self.y_n)


class ListaFLT:

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

        temp = NodoFLT(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickFLT)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarFLT)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoFLT)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoFLT)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoFLT) # 3 Windows/Unix
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

        temp = NodoFLT(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickFLT)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarFLT)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoFLT)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoFLT)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoFLT)  # 3 Windows/Unix
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
