from tkinter import *
from tkinter import messagebox
import Simulacion
from tkinter import ttk


class NodoQDEC:
    def __init__(self, id_QDEC, tupla_listas, px, py):

        self.dato = id_QDEC
        self.tipo = "QDEC"
        self.nombre = "QDEC_"+str(id_QDEC)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "H"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada = None
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="QDEC.png")

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
        self.variable_tamano_contador = 3
        self.variable_tiempo_muestreo = 20
        self.variable_ganancia = 1

    def dobleClickQDEC(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowQDEC = Toplevel(self.mainWindow)
            self.windowQDEC.resizable(False, False)
            self.windowQDEC.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowQDEC, bg="#2C2C2C")
            self.frame2 = Frame(self.windowQDEC, bg="white")
            self.frame3 = Frame(self.windowQDEC, bg="white")

            self.imagen_ventana = PhotoImage(file="QDECv.png")
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

            Label(self.frame2, text="Tamaño del contador", font=("Arial Rounded MT Bold", -18)).grid(row=0,
                                                                                       column=0,
                                                                                       columnspan=2,
                                                                                       sticky=W,
                                                                                       padx=10,
                                                                                       pady=10)

            self.v = IntVar()
            self.g = StringVar()
            self.t = StringVar()

            if self.variable_tamano_contador is None:
                self.v.set(3)
            else:
                self.v.set(self.variable_tamano_contador)

            if self.variable_ganancia is None:
                self.g.set(1)
            else:
                self.g.set(str(self.variable_ganancia))

            if self.variable_tiempo_muestreo is None:
                self.t.set(20)
            else:
                self.t.set(str(self.variable_tiempo_muestreo))

            ttk.Radiobutton(self.frame2, text="8 bits", variable=self.v, value=1, state='disabled')\
                .grid(row=1, column=0, sticky=W, padx=20)
            Label(self.frame2, text="[-128 , +127]").grid(row=1, column=1, sticky=W, padx=(0,20))

            ttk.Radiobutton(self.frame2, text="16 bits", variable=self.v, value=2, state='disabled')\
                .grid(row=2, column=0, sticky=W, padx=20)
            Label(self.frame2, text="[-32'768 , +32'767]").grid(row=2, column=1, sticky=W, padx=(0,20))

            ttk.Radiobutton(self.frame2, text="32 bits", variable=self.v, value=3)\
                .grid(row=3, column=0, sticky=W, padx=20)
            Label(self.frame2, text="[-2'147'483'648 , +2'147'483'647]").grid(row=3, column=1, sticky=W, padx=(0,20))

            Label(self.frame2, text="Tiempo de muestreo (ms):").grid(row=4, column=0, sticky=W, padx=20, pady=(10,0))
            ttk.Entry(self.frame2, width=15, textvariable=self.t).grid(row=4, column=1, sticky=W, padx=(0, 20), pady=(10,0))

            Label(self.frame2, text="Ganancia:").grid(row=5, column=0, sticky=W, padx=20)
            ttk.Entry(self.frame2, width=15, textvariable=self.g).grid(row=5, column=1, sticky=W, padx=(0, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", command=lambda: self.cerrarVentanaQDEC("Aceptar"))\
                .pack(side=RIGHT, padx=(10, 20),pady=10)
            ttk.Button(self.frame3, text="Cancelar", command=lambda: self.cerrarVentanaQDEC("Cancelar"))\
                .pack(side=RIGHT, pady=10)

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowQDEC.protocol("WM_DELETE_WINDOW", self.cerrarVentanaQDEC)

            self.windowQDEC.withdraw()
            self.windowQDEC.update_idletasks()
            x = (self.windowQDEC.winfo_screenwidth() - self.windowQDEC.winfo_reqwidth()) / 2
            y = (self.windowQDEC.winfo_screenheight() - self.windowQDEC.winfo_reqheight()) / 2
            self.windowQDEC.geometry("+%d+%d" % (x, y))

            self.windowQDEC.deiconify()

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
            self.windowQDEC.lift()

    def cerrarVentanaQDEC(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            error = 1
            try:

                tmuestreo = eval(self.t.get())

                if type(tmuestreo) is not int and type(tmuestreo) is not float:
                    raise Exception

                error = 2

                ganancia = eval(self.g.get())

                if type(ganancia) is not int and type(ganancia) is not float:
                    raise Exception

                if tmuestreo < 1:
                    tmuestreo = 1

                self.variable_ganancia = ganancia
                self.variable_tiempo_muestreo = int(tmuestreo)
                self.variable_tamano_contador = self.v.get()
                self.ventanaCerrada = True
                self.windowQDEC.destroy()

            except Exception:

                if error == 1:
                    messagebox.showerror("Error", "Tiempo de muestreo inválido")
                else:
                    messagebox.showerror("Error", "Ganancia inválida")

                self.windowQDEC.lift()

        else:
            self.ventanaCerrada = True
            self.windowQDEC.destroy()

    def arrastrarQDEC(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoQDEC(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarQDEC()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida QDEC

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada QDEC

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx-32, self.posiciony-1)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

    def clickDerechoQDEC(self, event):

        self.eliminarQDEC()

    def eliminarQDEC(self):

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

            self.tupla_listas[10].remover(self.nombre)

    def enMovimientoQDEC(self, event):

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

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada, self.nombre)
            return sim_entrada1.senal_simulacion(n, ts, self.entrada) * self.variable_ganancia

        else:
            return 0


class ListaQDEC:

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

        temp = NodoQDEC(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickQDEC)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarQDEC)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoQDEC)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoQDEC)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoQDEC) # 3 Windows/Unix
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

        temp = NodoQDEC(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickQDEC)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarQDEC)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoQDEC)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoQDEC)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoQDEC)  # 3 Windows/Unix
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
