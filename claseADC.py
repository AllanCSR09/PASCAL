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
        self.variable_rango = 7
        self.variable_tiempo_muestreo = 20
        self.variable_ganancia = 1

    def dobleClickADC(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowADC = Toplevel(self.mainWindow)
            self.windowADC.resizable(False, False)
            self.windowADC.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowADC, bg="#2C2C2C")
            self.frame2 = Frame(self.windowADC, bg="white")
            self.frame3 = Frame(self.windowADC, bg="white")

            self.imagen_ventana = PhotoImage(file="ADCv.png")
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

            Label(self.frame2, text="Rango", font=("Arial Rounded MT Bold", -18)).grid(row=0,
                                                                                       column=0,
                                                                                       columnspan=2,
                                                                                       sticky=W,
                                                                                       padx=10,
                                                                                       pady=10)

            # self.frame2.create_line(20,40, 280, 40, width=3, fill="#EFEFEF")

            self.v = IntVar()

            if self.variable_rango is None:
                self.v.set(8)
            else:
                self.v.set(self.variable_rango + 1)

            ttk.Radiobutton(self.frame2, text="\u00b1 10V", variable=self.v, value=8)\
                .grid(row=1, column=0, sticky=W, padx=25)
            ttk.Radiobutton(self.frame2, text="\u00b1 5V", variable=self.v, value=7)\
                .grid(row=2, column=0, sticky=W, padx=25)
            ttk.Radiobutton(self.frame2, text="\u00b1 2V", variable=self.v, value=6)\
                .grid(row=3, column=0, sticky=W, padx=25)
            ttk.Radiobutton(self.frame2, text="\u00b1 1V", variable=self.v, value=5)\
                .grid(row=4, column=0, sticky=W, padx=25, pady=(0, 10))

            ttk.Radiobutton(self.frame2, text="+10V", variable=self.v, value=4).\
                grid(row=1, column=1, sticky=W, padx=25)
            ttk.Radiobutton(self.frame2, text="+5V", variable=self.v, value=3).\
                grid(row=2, column=1, sticky=W, padx=25)
            ttk.Radiobutton(self.frame2, text="+2V", variable=self.v, value=2).\
                grid(row=3, column=1, sticky=W, padx=25)
            ttk.Radiobutton(self.frame2, text="+1V", variable=self.v, value=1).\
                grid(row=4, column=1, sticky=W, padx=25, pady=(0, 10))

            self.t = IntVar()
            self.g = StringVar()

            if self.variable_tiempo_muestreo is None:
                self.t.set(10)
            else:
                self.t.set(str(self.variable_tiempo_muestreo))

            if self.variable_ganancia is None:
                self.g.set(1)
            else:
                self.g.set(str(self.variable_ganancia))

            Message(self.frame2, text="Tiempo de muestreo (ms)").grid(row=5, column=0, sticky=W, padx=10)
            ttk.Entry(self.frame2, width=14, textvariable=self.t).grid(row=5, column=1, sticky=W, rowspan=1)

            Label(self.frame2, text="Ganancia:").grid(row=6, column=0, sticky=W, padx=10, pady=(0, 10))
            ttk.Entry(self.frame2, width=14, textvariable=self.g).grid(row=6, column=1, sticky=W, padx=(0, 20), pady=(0, 10))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", width=8, command=lambda: self.cerrarVentanaADC("Aceptar"))\
                .pack(side=RIGHT, padx=(10, 20),pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", width=8, command=lambda: self.cerrarVentanaADC("Cancelar"))\
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowADC.protocol("WM_DELETE_WINDOW", self.cerrarVentanaADC)

            self.windowADC.withdraw()
            self.windowADC.update_idletasks()
            x = (self.windowADC.winfo_screenwidth() - self.windowADC.winfo_reqwidth()) / 2
            y = (self.windowADC.winfo_screenheight() - self.windowADC.winfo_reqheight()) / 2
            self.windowADC.geometry("+%d+%d" % (x, y))

            self.windowADC.deiconify()

            s = ttk.Style()
            s.configure('Style.TRadiobutton',
                        background="White",
                        foreground='black')
            for wid in self.frame2.winfo_children():
                if wid.winfo_class() == 'Label':
                    wid.configure(bg="white")
                if wid.winfo_class() == 'TRadiobutton':
                    wid.configure(style='Style.TRadiobutton')
                if wid.winfo_class() == 'Message':
                    wid.configure(bg='white')
        else:
            self.windowADC.lift()


    def cerrarVentanaADC(self, opcion="Cancelar"):

        if opcion == "Aceptar":
            error = 1
            try:
                valor = self.t.get()
                if valor < 0:
                    raise Exception

                error = 2

                ganancia = eval(self.g.get())

                if type(ganancia) is not int and type(ganancia) is not float:
                    raise Exception

                self.variable_tiempo_muestreo = self.t.get()
                self.variable_ganancia = ganancia
                self.variable_rango = self.v.get() - 1
                self.ventanaCerrada = True
                self.windowADC.destroy()

            except Exception:
                if error == 1:
                    messagebox.showerror("Error", "Tiempo de muestreo inválido")
                else:
                    messagebox.showerror("Error", "Ganancia inválida")

                self.windowADC.lift()
        else:
            self.ventanaCerrada = True
            self.windowADC.destroy()

    def arrastrarADC(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoADC(self, event):

        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarADC()

        else:
            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida ADC

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony - 1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada ADC

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 32, self.posiciony - 1)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

    def clickDerechoADC(self, event):

        self.eliminarADC()

    def eliminarADC(self):

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

            self.tupla_listas[3].remover(self.nombre)

    def enMovimientoADC(self, event):

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


class ListaADC:

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

        temp = NodoADC(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickADC)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarADC)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoADC)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoADC)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoADC)  # 3 Windows/Unix
        temp.window.tag_bind(temp.nombre, "<Motion>", temp.sobreIcono)
        temp.window.tag_bind(temp.nombre, "<Enter>", temp.dentroDelIcono)
        temp.window.tag_bind(temp.nombre, "<Leave>", temp.afueraDelIcono)

# -----------------------------------------------------
    def abrirArchivo(self, tupla_listas, nombre, x, y):

        n = 0
        for i in nombre:
            if i == "_":
                n = n + 1
                break
            n = n + 1

        item = int(nombre[n:])

        temp = NodoADC(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickADC)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarADC)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoADC)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoADC)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoADC)  # 3 Windows/Unix
        temp.window.tag_bind(temp.nombre, "<Motion>", temp.sobreIcono)
        temp.window.tag_bind(temp.nombre, "<Enter>", temp.dentroDelIcono)
        temp.window.tag_bind(temp.nombre, "<Leave>", temp.afueraDelIcono)

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
