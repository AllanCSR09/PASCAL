from tkinter import *
import Simulacion
from tkinter import ttk
from tkinter import messagebox

class NodoPID:
    def __init__(self, id_PID, tupla_listas, px, py):

        self.dato = id_PID
        self.tipo = "PID"
        self.nombre = "PID_"+str(id_PID)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "B"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada1 = None
        self.entrada2 = None

        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="PID.png")

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

        # Variables ------------------------
        self.variable_tipo_pid = 1

        self.variable_parametro_p = 1
        self.variable_parametro_i = 0
        self.variable_parametro_d = 0
        self.variable_parametro_c = 1
        self.variable_parametro_b = 1
        self.variable_parametro_n = 1

        self.variable_metodo_integrador = "Forward Euler"
        self.variable_metodo_filtro = "Forward Euler"
        self.variable_tiempo_muestreo = 10

        self.variable_tipo_saturador = 0
        self.variable_limite_inferior = -5
        self.variable_limite_superior = 5

        # Simulacion -----------------------
        self.i_n_1 = 0
        self.i_n = 0
        self.e_n_1 = 0
        self.e_n = 0
        self.d_n = 0
        self.d_n_1 = 0
        self.p_n = 0
        self.pid = 0
        self.x_n = 0
        self.y_n = 0
        self.y_n_2 = 0
        self.y_n_1 = 0
        self.x_n_2 = 0
        self.x_n_1 = 0

    def dobleClickPID(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowPID = Toplevel(self.mainWindow)
            self.windowPID.resizable(False, False)
            self.windowPID.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowPID, bg="#2C2C2C")
            self.frame2 = Frame(self.windowPID, bg="white")
            self.frame3 = Frame(self.windowPID, bg="white")

            self.imagen_ventana = PhotoImage(file="PIDv.png")
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

            Label(self.frame2, text="Control", font=("Arial Rounded MT Bold", -18))\
                .grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

            self.v = IntVar()

            if self.variable_tipo_pid is None:
                self.v.set(1)
            else:
                self.v.set(self.variable_tipo_pid)

            self.imagen_diagrama = PhotoImage(file="PID_diagrama.png")
            self.imagen_diagrama_label = Label(self.frame2,
                                               image=self.imagen_diagrama,
                                               borderwidth=0,
                                               highlightthickness=0,
                                               padx=0,
                                               pady=0)
            self.imagen_diagrama_label.image = self.imagen_diagrama
            self.imagen_diagrama_label.grid(row=1, column=1, columnspan=4, rowspan=3, padx=(0, 20))

            ttk.Radiobutton(self.frame2, text="PID", variable=self.v, value=1, command=self.cambiarDiagrama) \
                .grid(row=1, column=0, sticky=W, padx=20)
            ttk.Radiobutton(self.frame2, text="I_PD", variable=self.v, value=2, command=self.cambiarDiagrama) \
                .grid(row=2, column=0, sticky=W, padx=20)
            ttk.Radiobutton(self.frame2, text="PI_D", variable=self.v, value=3, command=self.cambiarDiagrama) \
                .grid(row=3, column=0, sticky=W, padx=20)

            Label(self.frame2, text="Parámetros", font=("Arial Rounded MT Bold", -18))\
                .grid(row=4, column=0, sticky=W, columnspan=4, padx=10, pady=10)

            self.p = StringVar()
            self.i = StringVar()
            self.d = StringVar()
            self.c = StringVar()
            self.b = StringVar()
            self.n = StringVar()
            self.t = IntVar()
            self.saturador = IntVar()
            self.ls = StringVar()
            self.li = StringVar()
            self.metodo_integrador = StringVar()
            self.metodo_filtro = StringVar()

            self.cambiarDiagrama()

            if self.variable_parametro_p is None: self.p.set(1)
            else: self.p.set(self.variable_parametro_p)

            if self.variable_parametro_i is None: self.i.set(0)
            else: self.i.set(self.variable_parametro_i)

            if self.variable_parametro_d is None: self.d.set(0)
            else: self.d.set(self.variable_parametro_d)

            if self.variable_parametro_c is None: self.c.set(1)
            else: self.c.set(self.variable_parametro_c)

            if self.variable_parametro_b is None: self.b.set(1)
            else: self.b.set(self.variable_parametro_b)

            if self.variable_parametro_n is None: self.n.set(1)
            else: self.n.set(self.variable_parametro_n)

            if self.variable_tiempo_muestreo is None: self.t.set(10)
            else: self.t.set(self.variable_tiempo_muestreo)

            if self.variable_metodo_integrador is None:
                self.metodo_integrador.set('Forward Euler')
            else:
                self.metodo_integrador.set(self.variable_metodo_integrador)

            if self.variable_metodo_filtro is None:
                self.metodo_filtro.set('Forward Euler')
            else:
                self.metodo_filtro.set(self.variable_metodo_filtro)

            if self.variable_tipo_saturador is None:
                self.saturador.set(0)

            else:
                self.saturador.set(self.variable_tipo_saturador)

            if self.variable_limite_superior is None:
                self.ls.set(5)
            else:
                self.ls.set(self.variable_limite_superior)

            if self.variable_limite_inferior is None:
                self.li.set(-5)
            else:
                self.li.set(self.variable_limite_inferior)


            Label(self.frame2, text="Proporcional (P):").grid(row=5, column=0, sticky=W, padx=(20,0))
            ttk.Entry(self.frame2, width=15, textvariable=self.p).grid(row=5, column=1, sticky=W, padx=(0, 20))

            Label(self.frame2, text="Integral (I):").grid(row=6, column=0, sticky=W, padx=(20,0))
            ttk.Entry(self.frame2, width=15, textvariable=self.i).grid(row=6, column=1, sticky=W, padx=(0,20))

            Label(self.frame2, text="Derivativo (D):").grid(row=7, column=0, sticky=W, padx=(20,0), pady=(0,20))
            ttk.Entry(self.frame2, width=15, textvariable=self.d).grid(row=7, column=1, sticky=W, padx=(0,20), pady=(0,20))

            Label(self.frame2, text="Coeficiente Filtro (N):").grid(row=5, column=2, sticky=W, padx=(0,20))
            ttk.Entry(self.frame2, width=15, textvariable=self.n).grid(row=5, column=3, sticky=W, padx=(0,20))

            Label(self.frame2, text="Setpoint weight (b):").grid(row=6, column=2, sticky=W, padx=(0,20))
            ttk.Entry(self.frame2, width=15, textvariable=self.b, state='disabled').grid(row=6, column=3, sticky=W, padx=(0,20))

            Label(self.frame2, text="Setpoint weight (c):").grid(row=7, column=2, sticky=W, pady=(0,20), padx=(0,20))
            ttk.Entry(self.frame2, width=15, textvariable=self.c, state='disabled').grid(row=7, column=3, sticky=W, pady=(0,20), padx=(0,20))

            Label(self.frame2, text="Método Integrador:").grid(row=8, column=0, sticky=W, padx=(20,0))
            Label(self.frame2, text="Método Filtro:").grid(row=9, column=0, sticky=W, padx=(20,0))

            Label(self.frame2, text="Tiempo de muestreo (ms):").grid(row=10, column=0, sticky=W, padx=(20, 0))
            ttk.Entry(self.frame2, width=15, textvariable=self.t).grid(row=10, column=1, sticky=W)

            opciones = ['Forward Euler', 'Backward Euler', 'Trapezoidal']

            a = ttk.OptionMenu(self.frame2, self.metodo_integrador, None, *opciones, command=self.cambiarEcuacion)
            a.grid(row=8, column=1, sticky=W)
            a.config(width=13)

            b = ttk.OptionMenu(self.frame2, self.metodo_filtro, None, *opciones, command=self.cambiarEcuacion)
            b.grid(row=9, column=1, sticky=W)
            b.config(width=13)

            ttk.Checkbutton(self.frame2, text="Saturador", variable=self.saturador).grid(row=8, column=2, sticky=W)

            Label(self.frame2, text="Límite Superior:").grid(row=9, column=2, sticky=W, padx=(0, 20))
            ttk.Entry(self.frame2, width=15, textvariable=self.ls).grid(row=9, column=3, sticky=W, padx=(0, 20))

            Label(self.frame2, text="Límite Inferior:").grid(row=10, column=2, sticky=W, padx=(0, 20))
            ttk.Entry(self.frame2, width=15, textvariable=self.li).grid(row=10, column=3, sticky=W, padx=(0, 20))

            self.imagen_ecuacion = PhotoImage(file="Ecuacion_FF.png")
            self.imagen_ecuacion_label = Label(self.frame2,
                                              image=self.imagen_ecuacion,
                                              borderwidth=0,
                                              highlightthickness=0,
                                              padx=0,
                                              pady=0)
            self.imagen_ecuacion_label.image = self.imagen_ecuacion
            self.imagen_ecuacion_label.grid(row=12, column=0, columnspan=4, rowspan=1, padx=(0,20), pady=10)

            self.cambiarEcuacion(None)

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", command=lambda: self.cerrarVentanaPID("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", command=lambda: self.cerrarVentanaPID("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowPID.protocol("WM_DELETE_WINDOW", self.cerrarVentanaPID)

            self.windowPID.withdraw()
            self.windowPID.update_idletasks()
            x = (self.windowPID.winfo_screenwidth() - self.windowPID.winfo_reqwidth()) / 2
            y = (self.windowPID.winfo_screenheight() - self.windowPID.winfo_reqheight()) / 2
            self.windowPID.geometry("+%d+%d" % (x, y))

            self.windowPID.deiconify()

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
            self.windowPID.lift()

    def cerrarVentanaPID(self, opcion="Cancelar"):

        if opcion == "Aceptar":
            try:
                error = 1

                constante = eval(self.p.get())
                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                constante = eval(self.i.get())
                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                constante = eval(self.d.get())
                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                constante = eval(self.c.get())
                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                constante = eval(self.b.get())
                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                constante = eval(self.n.get())
                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                error = 2
                constante = self.t.get()

                error = 3

                tipo = self.saturador.get()


                if tipo == 0:

                    self.variable_tipo_saturador = tipo
                    self.variable_limite_superior = 5
                    self.variable_limite_inferior = -5

                else:

                    lsuperior = eval(self.ls.get())
                    if type(lsuperior) is not int and type(lsuperior) is not float:
                        raise Exception

                    error = 4

                    linferior = eval(self.li.get())
                    if type(linferior) is not int and type(linferior) is not float:
                        raise Exception

                    error = 5
                    if lsuperior <= linferior:
                        raise Exception

                    self.variable_limite_superior = lsuperior
                    self.variable_limite_inferior = linferior

                self.variable_tipo_saturador = tipo
                self.variable_tiempo_muestreo = constante
                self.variable_tipo_pid = self.v.get()

                self.variable_parametro_p = eval(self.p.get())
                self.variable_parametro_i = eval(self.i.get())
                self.variable_parametro_d = eval(self.d.get())
                self.variable_parametro_c = eval(self.c.get())
                self.variable_parametro_b = eval(self.b.get())
                self.variable_parametro_n = eval(self.n.get())

                self.variable_metodo_integrador = self.metodo_integrador.get()
                self.variable_metodo_filtro = self.metodo_filtro.get()

                self.ventanaCerrada = True
                self.windowPID.destroy()

            except Exception:

                if error == 1:
                    messagebox.showerror("Error", "Parámetro inválido")

                if error == 2:
                    messagebox.showerror("Error", "Tiempo de muestreo inválido")

                if error == 3:
                    messagebox.showerror("Error", "Límite superior inválido")

                if error == 4:
                    messagebox.showerror("Error", "Límite inferior inválido")

                if error == 5:
                    messagebox.showerror("Error", "Límite superior debe ser mayor al límite inferior")

                self.windowPID.lift()
        else:
            self.ventanaCerrada = True
            self.windowPID.destroy()

    def cambiarDiagrama(self):

        if self.v.get() == 1:
            self.imagen_diagrama = PhotoImage(file="PID_diagrama.png")
            self.c.set(1)
            self.b.set(1)

        if self.v.get() == 2:
            self.imagen_diagrama = PhotoImage(file="I_PD_diagrama.png")
            self.c.set(0)
            self.b.set(0)

        if self.v.get() == 3:
            self.imagen_diagrama = PhotoImage(file="PI_D_diagrama.png")
            self.c.set(0)
            self.b.set(1)

        self.imagen_diagrama_label.configure(image=self.imagen_diagrama)
        self.imagen_diagrama_label.image = self.imagen_diagrama

    def cambiarEcuacion(self, value):

        metodo_i = self.metodo_integrador.get()
        metodo_f = self.metodo_filtro.get()

        if metodo_i == "Forward Euler" and metodo_f == "Forward Euler":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_FF.png")

        if metodo_i == "Forward Euler" and metodo_f == "Backward Euler":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_FB.png")

        if metodo_i == "Forward Euler" and metodo_f == "Trapezoidal":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_FT.png")

        if metodo_i == "Backward Euler" and metodo_f == "Forward Euler":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_BF.png")

        if metodo_i == "Backward Euler" and metodo_f == "Backward Euler":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_BB.png")

        if metodo_i == "Backward Euler" and metodo_f == "Trapezoidal":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_BT.png")

        if metodo_i == "Trapezoidal" and metodo_f == "Forward Euler":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_TF.png")

        if metodo_i == "Trapezoidal" and metodo_f == "Backward Euler":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_TB.png")

        if metodo_i == "Trapezoidal" and metodo_f == "Trapezoidal":
            self.imagen_ecuacion = PhotoImage(file="Ecuacion_TT.png")


        self.imagen_ecuacion_label.configure(image=self.imagen_ecuacion)
        self.imagen_ecuacion_label.image = self.imagen_ecuacion

    def arrastrarPID(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoPID(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarPID()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida PID

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada1 PID

                if self.creandoLinea is not None and self.entrada1 is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 32, self.posiciony-14)
                    self.entrada1 = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada1 is None:
                    coord = [self.posicionx - 32, self.posiciony-14]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada1 = self.creandoLinea

            if -38 < self.dx < -28 and 19 > self.dy > 7:  # Entrada2 PID

                if self.creandoLinea is not None and self.entrada2 is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 32, self.posiciony+12)
                    self.entrada2 = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada2 is None:
                    coord = [self.posicionx - 32, self.posiciony+12]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada2 = self.creandoLinea

    def clickDerechoPID(self, event):

        self.eliminarPID()

    def eliminarPID(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelEntrada2)
            self.window.delete(self.labelSalida1)
            self.window.unbind(self.nombre)

            if self.entrada1 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada1)
            if self.entrada2 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada2)
            if self.salida is not None:
                self.tupla_listas[2].eliminarConexion(self.salida)

            self.tupla_listas[4].remover(self.nombre)

    def enMovimientoPID(self, event):
        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------
            if self.entrada1 is not None and self.entrada1 != self.salida:
                self.tupla_listas[2].moverLinea(self.entrada1, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada2 is not None and self.entrada2 != self.salida:
                self.tupla_listas[2].moverLinea(self.entrada2, self.nombre,
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

        if self.entrada1 is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada1, self.nombre)
            sim_entrada1.senal_nombres(lista_nombres)

        if self.entrada2 is not None:
            sim_entrada2 = a.obtenerBloqueConexion(self.entrada2, self.nombre)
            sim_entrada2.senal_nombres(lista_nombres)

        lista_nombres.append(self.nombre)

        return lista_nombres

    def senal_simulacion(self, n, ts, conexion):

        if n == 0:
            self.i_n_1 = 0
            self.i_n = 0
            self.e_n_1 = 0
            self.e_n = 0
            self.d_n = 0
            self.d_n_1 = 0
            self.p_n = 0
            self.y_n = 0
            self.y_n_1 = 0
            self.pid = 0
            self.i_pd = 0
            self.pi_d = 0

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        ent1 = 0.0
        ent2 = 0.0

        if self.entrada1 is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada1, self.nombre)
            ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada1)
        else:
            ent1 = 0.0

        if self.entrada2 is not None:
            sim_entrada2 = a.obtenerBloqueConexion(self.entrada2, self.nombre)
            ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada2)
        else:
            ent2 = 0.0

        self.e_n = ent1 - ent2
        self.y_n = ent2

        ts = self.variable_tiempo_muestreo / 1000

        # BORRAR -------------------------
        if self.variable_parametro_n == 9999:
            if n == 0:

                self.y_n = 0
                self.y_n_1 = 0
                self.y_n_2 = 0
                self.x_n = 0
                self.x_n_1 = 0
                self.x_n_2 = 0

            kp = self.variable_parametro_p
            kd = self.variable_parametro_d
            ki = self.variable_parametro_i

            a = 2 * kp * ts + ki * ts * ts + 4 * kd
            b = 2 * ki * ts * ts - 8 * kd
            c = 4 * kd + ki * ts * ts - 2 * kp * ts
            self.x_n = self.e_n
            self.y_n = self.y_n_2 + a / (2 * ts) * self.x_n + b / (2 * ts) * self.x_n_1 + c / (2 * ts) * self.x_n_2

            self.y_n_2 = self.y_n_1
            self.y_n_1 = self.y_n
            self.x_n_2 = self.x_n_1
            self.x_n_1 = self.x_n

            return self.y_n

        n = self.variable_parametro_n
        d = self.variable_parametro_d

        if self.variable_tipo_pid == 1:  # PID

            # Control Proporcional

            self.p_n = self.variable_parametro_p * self.e_n

            # Control Integral

            if self.variable_metodo_integrador == "Backward Euler":
                self.i_n = self.e_n * self.variable_parametro_i * ts + self.i_n_1

            if self.variable_metodo_integrador == "Forward Euler":
                self.i_n = self.e_n_1 * self.variable_parametro_i * ts + self.i_n_1

            if self.variable_metodo_integrador == "Trapezoidal":
                self.i_n = ((self.e_n + self.e_n_1) / 2) * self.variable_parametro_i * ts + self.i_n_1

            # Control Derivativo

            if self.variable_metodo_filtro == "Backward Euler":
                self.d_n = d*n*(self.e_n-self.e_n_1)/(1+n*ts)+self.d_n_1/(1+n*ts)

            if self.variable_metodo_filtro == "Forward Euler":
                self.d_n = d * n * (self.e_n - self.e_n_1) - self.d_n_1 * (n * ts - 1)

            if self.variable_metodo_filtro == "Trapezoidal":
                self.d_n = (d * n * (self.e_n - self.e_n_1) + (2 - n * ts) * self.d_n_1) / (2 + n * ts)
            
            self.pid = self.p_n + self.i_n + self.d_n

            self.e_n_1 = self.e_n
            self.d_n_1 = self.d_n
            self.i_n_1 = self.i_n
            return self.pid

        if self.variable_tipo_pid == 2:  # I_PD

            # Control Proporcional

            self.p_n = self.variable_parametro_p * self.y_n

            # Control Integral

            if self.variable_metodo_integrador == "Backward Euler":
                self.i_n = self.e_n * self.variable_parametro_i * ts + self.i_n_1

            if self.variable_metodo_integrador == "Forward Euler":
                self.i_n = self.e_n_1 * self.variable_parametro_i * ts + self.i_n_1

            if self.variable_metodo_integrador == "Trapezoidal":
                self.i_n = ((self.e_n + self.e_n_1) / 2) * self.variable_parametro_i * ts + self.i_n_1

            # Control Derivativo

            if self.variable_metodo_filtro == "Backward Euler":
                self.d_n = d * n * (self.y_n - self.y_n_1) / (1 + n * ts) + self.d_n_1 / (1 + n * ts)

            if self.variable_metodo_filtro == "Forward Euler":
                self.d_n = d * n * (self.y_n - self.y_n_1) - self.d_n_1 * (n * ts - 1)

            if self.variable_metodo_filtro == "Trapezoidal":
                self.d_n = (d * n * (self.y_n - self.y_n_1) + (2 - n * ts) * self.d_n_1) / (2 + n * ts)

            self.i_pd = self.i_n - self.p_n - self.d_n

            self.e_n_1 = self.e_n
            self.y_n_1 = self.y_n
            self.d_n_1 = self.d_n
            self.i_n_1 = self.i_n
            return self.i_pd

        if self.variable_tipo_pid == 3:  # PI_D

            # Control Proporcional

            self.p_n = self.variable_parametro_p * self.e_n

            # Control Integral

            if self.variable_metodo_integrador == "Backward Euler":
                self.i_n = self.e_n * self.variable_parametro_i * ts + self.i_n_1

            if self.variable_metodo_integrador == "Forward Euler":
                self.i_n = self.e_n_1 * self.variable_parametro_i * ts + self.i_n_1

            if self.variable_metodo_integrador == "Trapezoidal":
                self.i_n = ((self.e_n + self.e_n_1) / 2) * self.variable_parametro_i * ts + self.i_n_1

            # Control Derivativo

            if self.variable_metodo_filtro == "Backward Euler":
                self.d_n = d * n * (self.y_n - self.y_n_1) / (1 + n * ts) + self.d_n_1 / (1 + n * ts)

            if self.variable_metodo_filtro == "Forward Euler":
                self.d_n = d * n * (self.y_n - self.y_n_1) - self.d_n_1 * (n * ts - 1)

            if self.variable_metodo_filtro == "Trapezoidal":
                self.d_n = (d * n * (self.y_n - self.y_n_1) + (2 - n * ts) * self.d_n_1) / (2 + n * ts)

            self.pi_d = self.p_n + self.i_n - self.d_n

            self.e_n_1 = self.e_n
            self.y_n_1 = self.y_n
            self.d_n_1 = self.d_n
            self.i_n_1 = self.i_n
            return self.pi_d

        return 0


class ListaPID:

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

        temp = NodoPID(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickPID)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarPID)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoPID)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoPID)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoPID) # 3 Windows/Unix
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

        temp = NodoPID(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickPID)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarPID)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoPID)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoPID)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoPID)  # 3 Windows/Unix
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
