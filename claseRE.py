from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import Simulacion

class NodoRE:
    def __init__(self, id_RE, tupla_listas, px, py):

        self.dato = id_RE
        self.tipo = "RE"
        self.tipoRE = "RE_1x1"

        self.nombre = "RE_"+str(id_RE)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "D"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada_1 = None
        self.entrada_2 = None
        self.entrada_3 = None
        self.entrada_4 = None
        self.entrada_5 = None
        self.entrada_6 = None
        self.entrada_7 = None

        self.salida_1 = None
        self.salida_2 = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]

        if self.tipoRE == "RE_1x1": self.imagen = PhotoImage(file="RE_1x1.png")
        if self.tipoRE == "RE_1x2": self.imagen = PhotoImage(file="RE_1x2.png")
        if self.tipoRE == "RE_2x1": self.imagen = PhotoImage(file="RE_2x1.png")
        if self.tipoRE == "RE_2x2": self.imagen = PhotoImage(file="RE_2x2.png")
        if self.tipoRE == "RE_3x1": self.imagen = PhotoImage(file="RE_3x1.png")
        if self.tipoRE == "RE_3x2": self.imagen = PhotoImage(file="RE_3x2.png")
        if self.tipoRE == "RE_4x1": self.imagen = PhotoImage(file="RE_4x1.png")
        if self.tipoRE == "RE_4x2": self.imagen = PhotoImage(file="RE_4x2.png")

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
        self.estado_labelSalida2 = False
        self.labelSalida2 = self.nombre + "s2"

        self.estado_labelEntrada1 = False
        self.labelEntrada1 = self.nombre + "e1"
        self.estado_labelEntrada2 = False
        self.labelEntrada2 = self.nombre + "e2"
        self.estado_labelEntrada3 = False
        self.labelEntrada3 = self.nombre + "e3"
        self.estado_labelEntrada4 = False
        self.labelEntrada4 = self.nombre + "e4"
        self.estado_labelEntrada4 = False
        self.labelEntrada5 = self.nombre + "e5"
        self.estado_labelEntrada4 = False
        self.labelEntrada6 = self.nombre + "e6"
        self.estado_labelEntrada4 = False
        self.labelEntrada7 = self.nombre + "e7"

        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

        # Variables ------------------------
        self.variable_tipo = 1
        self.variable_n = 1
        self.variable_m = 1

        self.variable_k0 = 1
        self.variable_matriz_k = "[1.0]"
        self.variable_matriz_ki = ""
        self.variable_matriz_y1 = 'x1'
        self.variable_matriz_y2 = 'x1'
        self.variable_tipo_saturador = 0
        self.variable_limite_superior = 5
        self.variable_limite_inferior = -5

        # Simulacion -----------------------
        self.y_n = 0
        self.u1_n = 0
        self.u1_n_1 = 0
        self.u2_n = 0
        self.u2_n_1 = 0
        self.x_n = 0
        self.x_n_1 = 0

    def dobleClickRE(self, event):

        if self.ventanaCerrada and self.creandoLinea is None:
            self.ventanaCerrada = False

            self.windowRE = Toplevel(self.mainWindow)
            self.windowRE.resizable(False, False)
            self.windowRE.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowRE, bg="#2C2C2C")
            self.frame2 = Frame(self.windowRE, bg="white")
            self.frame3 = Frame(self.windowRE, bg="white")
            self.frame4 = Frame(self.windowRE, bg="white")

            self.imagen_ventana = PhotoImage(file="REv.png")
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

            Label(self.frame2, text="Retroalimentación de Estados", font=("Arial Rounded MT Bold", -18)) \
                .grid(row=1, column=0, columnspan=3, sticky=W, padx=10, pady=(15, 0))

            self.imagen_diagrama_bloques = PhotoImage(file="Diagrama_Bloques_RE.png")
            self.imagen_diagrama_bloques_label = Label(self.frame2,
                                             image=self.imagen_diagrama_bloques,
                                             borderwidth=0,
                                             highlightthickness=0,
                                             padx=0)
            self.imagen_diagrama_bloques_label.image = self.imagen_diagrama_bloques
            self.imagen_diagrama_bloques_label.grid(row=15, column=0, columnspan=5, rowspan=1, pady=20, padx=0)

            self.imagen_bloque = PhotoImage(file="Diagrama_RE_1x1.png")
            self.imagen_bloque_label = Label(self.frame2,
                                             image=self.imagen_bloque,
                                             borderwidth=0,
                                             highlightthickness=0,
                                             padx=0)
            self.imagen_bloque_label.image = self.imagen_bloque
            self.imagen_bloque_label.grid(row=3, column=0, columnspan=5, rowspan=1, pady=(5, 15))

            self.v = IntVar()

            if self.variable_tipo is None:
                self.v.set(1)
            else:
                self.v.set(self.variable_tipo)

            ttk.Radiobutton(self.frame2, text="RE", variable=self.v, value=1, command=self.cambiarDiagrama) \
                .grid(row=6, column=0, sticky=W, padx=(20, 0))
            ttk.Radiobutton(self.frame2, text="REI", variable=self.v, value=2, command=self.cambiarDiagrama) \
                .grid(row=7, column=0, sticky=W, padx=(20, 0))

            self.n = StringVar()
            self.m = StringVar()

            self.matriz_y1 = StringVar()
            self.matriz_y2 = StringVar()


            if self.variable_n is None:
                self.n.set("1")
            else:
                self.n.set(str(self.variable_n))

            if self.variable_m is None:
                self.m.set("1")
            else:
                self.m.set(str(self.variable_m))

            if self.variable_matriz_y1 is None:
                self.matriz_y1.set("x1")
            else:
                self.matriz_y1.set(str(self.variable_matriz_y1))

            if self.variable_matriz_y2 is None:
                self.matriz_y2.set("x2")
            else:
                self.matriz_y2.set(str(self.variable_matriz_y2))

            

            self.opciones_entrada = ['1', '2', '3', '4']
            self.opciones_salida = ['1', '2']
            self.opciones_entradas_u = ['1', '2']

            Label(self.frame2, text="Estados:").grid(row=6, column=1, sticky=E)
            ttk.OptionMenu(self.frame2, self.n, None, *self.opciones_entrada, command=self.cambiarDiagrama) \
                .grid(row=6, column=2, sticky=W)

            Label(self.frame2, text="Salidas: ").grid(row=7, column=1, sticky=E)
            ttk.OptionMenu(self.frame2, self.m, None, *self.opciones_salida, command=self.cambiarDiagrama) \
                .grid(row=7, column=2, sticky=W)

            opciones_y1y2 = ['x1', 'x2', 'x3', 'x4']

            Label(self.frame2, text="Salida y1:").grid(row=6, column=3, sticky=W)
            ttk.OptionMenu(self.frame2, self.matriz_y1, None, *opciones_y1y2).grid(row=6, column=4, sticky=W, padx=(0, 20))

            Label(self.frame2, text="Salida y2:") \
                .grid(row=7, column=3, sticky=W)
            ttk.OptionMenu(self.frame2, self.matriz_y2, None, *opciones_y1y2) \
                .grid(row=7, column=4, sticky=W, padx=(0, 20))

            self.k0 = StringVar()
            self.k = StringVar()
            self.ki = StringVar()

            if self.variable_k0 is None:
                self.k0.set("1")
            else:
                self.k0.set(self.variable_k0)

            if self.variable_matriz_k is None:
                self.k.set("[ k0 k1 k2 k3 ]")
            else:
                self.k.set(self.variable_matriz_k)

            if self.variable_matriz_ki is None:
                self.ki.set("")
            else:
                self.ki.set(self.variable_matriz_ki)

            Label(self.frame2, text="K0:").grid(row=9, column=0, sticky=W, padx=(20, 0), pady=(5, 0))
            self.entry_k0 = ttk.Entry(self.frame2, width=35, textvariable=self.k0)
            self.entry_k0.grid(row=9, column=1, columnspan=4, sticky=W, padx=(0, 20), pady=(5, 0))

            Label(self.frame2, text="Matriz K:").grid(row=10, column=0, sticky=W, padx=(20, 0), pady=(0,0))
            ttk.Entry(self.frame2, width=35, textvariable=self.k)\
                .grid(row=10, column=1, columnspan=4, sticky=W, padx=(0, 20), pady=(0,0))

            Label(self.frame2, text="Matriz Ki:").grid(row=11, column=0, sticky=W, padx=(20, 0), pady=(0, 0))
            self.entry_ki = ttk.Entry(self.frame2, width=35, textvariable=self.ki)
            self.entry_ki.grid(row=11, column=1, columnspan=4, sticky=W, padx=(0, 20), pady=(0, 0))

            self.saturador = IntVar()
            self.limite_superior = StringVar()
            self.limite_inferior = StringVar()

            if self.variable_tipo_saturador is None:
                self.saturador.set(0)
            else:
                self.saturador.set(self.variable_tipo_saturador)

            if self.variable_limite_superior is None:
                self.limite_superior.set(5)
            else:
                self.limite_superior.set(self.variable_limite_superior)

            if self.variable_limite_inferior is None:
                self.limite_inferior.set(-5)
            else:
                self.limite_inferior.set(self.variable_limite_inferior)

            self.saturator = ttk.Checkbutton(self.frame2, text="Saturador", variable=self.saturador)
            self.saturator.grid(row=12, column=0, sticky=W)

            Superior = Label(self.frame2, text="Límite superior:")
            Superior.grid(row=13, column=0, sticky=W, padx=(20, 0))
            
            self.entry_Superior = ttk.Entry(self.frame2, width=18, textvariable=self.limite_superior)
            self.entry_Superior.grid(row=13, column=1, sticky=W, padx=(0, 20))

            Inferior = Label(self.frame2, text="Límite inferior:")
            Inferior.grid(row=14, column=0, sticky=W, padx=(20, 0), pady=(0, 20))

            self.entry_Inferior = ttk.Entry(self.frame2, width=18, textvariable=self.limite_inferior)
            self.entry_Inferior.grid(row=14, column=1, sticky=W, padx=(0, 20), pady=(0, 20))

            self.cambiarDiagrama(None)

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", command=lambda: self.cerrarVentanaRE("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", command=lambda: self.cerrarVentanaRE("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowRE.protocol("WM_DELETE_WINDOW", self.cerrarVentanaRE)

            self.windowRE.withdraw()
            self.windowRE.update_idletasks()
            x = (self.windowRE.winfo_screenwidth() - self.windowRE.winfo_reqwidth()) / 2
            y = (self.windowRE.winfo_screenheight() - self.windowRE.winfo_reqheight()) / 2
            self.windowRE.geometry("+%d+%d" % (x, y))

            self.windowRE.deiconify()

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

            if self.creandoLinea is None:
                self.windowRE.lift()

    def cerrarVentanaRE(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            error = 0

            try:
                t = self.v.get()

                if t == 1:

                    valor_k0 = eval(self.k0.get())

                    if type(valor_k0) is not int and type(valor_k0) is not float:
                        raise Exception
                else:

                    valor_k0 = "1"

                error = 1

                matriz_k = np.matrix(self.k.get())

                m = int(self.m.get())
                n = int(self.n.get())

                y1 = self.matriz_y1.get()
                y2 = self.matriz_y2.get()

                dimensiones_k = matriz_k.shape

                if dimensiones_k != (m, n):
                    raise Exception

                error = 2

                if n == 1 and y1 != "x1":
                    raise Exception

                if n == 2 and y1 not in ["x1", "x2"]:
                    raise Exception

                if n == 3 and y1 not in ["x1", "x2", "x3"]:
                    raise Exception

                if n == 4 and y1 not in ["x1", "x2", "x3", "x4"]:
                    raise Exception

                error = 3

                if n == 1 and m == 2 and y2 != "x1":
                    raise Exception

                if n == 2 and m == 2 and y2 not in ["x1", "x2"]:
                    raise Exception

                if n == 3 and m == 2 and y2 not in ["x1", "x2", "x3"]:
                    raise Exception

                if n == 4 and m == 2 and y2 not in ["x1", "x2", "x3", "x4"]:
                    raise Exception

                error = 4

                if t == 2:

                    matriz_ki = np.matrix(self.ki.get())

                    dimensiones_ki = matriz_ki.shape

                    if t == 2 and dimensiones_ki != (m, m):
                        raise Exception
                else:
                    matriz_ki = np.matrix("")

                error = 5

                posicion = 45

                if t == 1:

                    if n == 1 and m == 1:
                        self.tipoRE = "RE_1x1"
                        self.imagen = PhotoImage(file="RE_1x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 1 and m == 2:
                        self.tipoRE = "RE_1x2"
                        self.imagen = PhotoImage(file="RE_1x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 2 and m == 1:
                        self.tipoRE = "RE_2x1"
                        self.imagen = PhotoImage(file="RE_2x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 2 and m == 2:
                        self.tipoRE = "RE_2x2"
                        self.imagen = PhotoImage(file="RE_2x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 3 and m == 1:
                        self.tipoRE = "RE_3x1"
                        self.imagen = PhotoImage(file="RE_3x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 52

                    if n == 3 and m == 2:
                        self.tipoRE = "RE_3x2"
                        self.imagen = PhotoImage(file="RE_3x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 52

                    if n == 4 and m == 1:
                        self.tipoRE = "RE_4x1"
                        self.imagen = PhotoImage(file="RE_4x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 58

                    if n == 4 and m == 2:
                        self.tipoRE = "RE_4x2"
                        self.imagen = PhotoImage(file="RE_4x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 58

                    self.tupla_listas[1].delete(self.label_con_nombre)
                    self.labelNombre = self.window.create_text(self.posicionx,
                                                               self.posiciony - posicion,
                                                               text=self.nombre,
                                                               font=("Arial Rounded MT", -12, "bold"),
                                                               tags=self.label_con_nombre)

                else:

                    if n == 1 and m == 1:
                        self.tipoRE = "RE_1x1"
                        self.imagen = PhotoImage(file="REI_1x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 1 and m == 2:
                        self.tipoRE = "RE_1x2"
                        self.imagen = PhotoImage(file="REI_1x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 2 and m == 1:
                        self.tipoRE = "RE_2x1"
                        self.imagen = PhotoImage(file="REI_2x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 2 and m == 2:
                        self.tipoRE = "RE_2x2"
                        self.imagen = PhotoImage(file="REI_2x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 45

                    if n == 3 and m == 1:
                        self.tipoRE = "RE_3x1"
                        self.imagen = PhotoImage(file="REI_3x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 52

                    if n == 3 and m == 2:
                        self.tipoRE = "RE_3x2"
                        self.imagen = PhotoImage(file="REI_3x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 52

                    if n == 4 and m == 1:
                        self.tipoRE = "RE_4x1"
                        self.imagen = PhotoImage(file="REI_4x1.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 58

                    if n == 4 and m == 2:
                        self.tipoRE = "RE_4x2"
                        self.imagen = PhotoImage(file="REI_4x2.png")
                        self.window.itemconfig(self.nombre, image=self.imagen)
                        posicion = 58

                    self.tupla_listas[1].delete(self.label_con_nombre)
                    self.labelNombre = self.window.create_text(self.posicionx,
                                                               self.posiciony - posicion,
                                                               text=self.nombre,
                                                               font=("Arial Rounded MT", -12, "bold"),
                                                               tags=self.label_con_nombre)

                # En caso de cambio en numero de entradas/salidas, eliminar conexiones.

                if self.variable_n != n or self.variable_m != m:

                    self.variable_n = n
                    self.variable_m = m

                    if self.entrada_1 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_1)
                    if self.entrada_2 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_2)
                    if self.entrada_3 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_3)
                    if self.entrada_4 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_4)
                    if self.entrada_5 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_5)
                    if self.entrada_6 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_6)
                    if self.entrada_7 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_7)

                    if self.salida_1 is not None:
                        self.tupla_listas[2].eliminarConexion(self.salida_1)
                    if self.salida_2 is not None:
                        self.tupla_listas[2].eliminarConexion(self.salida_2)

                # -----------------------------

                m_k = np.matrix(matriz_k)
                variable = []

                if m_k.shape == (1, 1) or m_k.shape == (2, 1):
                    variable.append("[")
                    variable.append(str(float(m_k[0, 0])))

                elif m_k.shape == (1, 2) or m_k.shape == (2, 2):
                    variable.append("[")
                    variable.append(str(float(m_k[0, 0])))
                    variable.append(", ")
                    variable.append(str(float(m_k[0, 1])))

                elif m_k.shape == (1, 3) or m_k.shape == (2, 3):
                    variable.append("[")
                    variable.append(str(float(m_k[0, 0])))
                    variable.append(", ")
                    variable.append(str(float(m_k[0, 1])))
                    variable.append(", ")
                    variable.append(str(float(m_k[0, 2])))

                elif m_k.shape == (1, 4) or m_k.shape == (2, 4):
                    variable.append("[")
                    variable.append(str(float(m_k[0, 0])))
                    variable.append(", ")
                    variable.append(str(float(m_k[0, 1])))
                    variable.append(", ")
                    variable.append(str(float(m_k[0, 2])))
                    variable.append(", ")
                    variable.append(str(float(m_k[0, 3])))

                if m_k.shape == (2, 1):
                    variable.append(" ; ")
                    variable.append(str(float(m_k[1, 0])))

                elif m_k.shape == (2, 2):
                    variable.append(" ; ")
                    variable.append(str(float(m_k[1, 0])))
                    variable.append(", ")
                    variable.append(str(float(m_k[1, 1])))

                elif m_k.shape == (2, 3):
                    variable.append(" ; ")
                    variable.append(str(float(m_k[1, 0])))
                    variable.append(", ")
                    variable.append(str(float(m_k[1, 1])))
                    variable.append(", ")
                    variable.append(str(float(m_k[1, 2])))

                elif m_k.shape == (2, 4):
                    variable.append(" ; ")
                    variable.append(str(float(m_k[1, 0])))
                    variable.append(", ")
                    variable.append(str(float(m_k[1, 1])))
                    variable.append(", ")
                    variable.append(str(float(m_k[1, 2])))
                    variable.append(", ")
                    variable.append(str(float(m_k[1, 3])))

                variable.append("]")
                matriz_k = "".join(variable)

                # -----------------------------

                m_ki = np.matrix(matriz_ki)
                variable = []

                if t == 1:
                    matriz_ki = ""

                else:

                    if m_ki.shape == (1, 1):
                        variable.append("[")
                        variable.append(str(float(m_ki[0, 0])))
                        variable.append("]")

                    elif m_ki.shape == (2, 2):
                        variable.append("[")
                        variable.append(str(float(m_ki[0, 0])))
                        variable.append(", ")
                        variable.append(str(float(m_ki[0, 1])))
                        variable.append(" ; ")
                        variable.append(str(float(m_ki[1, 0])))
                        variable.append(", ")
                        variable.append(str(float(m_ki[1, 1])))
                        variable.append("]")

                    matriz_ki = "".join(variable)

                error = 6
                tipo = self.saturador.get()
                if tipo == 0:
                    self.variable_zona_muerta = tipo
                    self.variable_limite_superior = 5
                    self.variable_limite_inferior = -5
                else:
                    limite_s = eval(self.limite_superior.get())
                    limite_i = eval(self.limite_inferior.get())

                    if type(limite_s) is not int and type(limite_s) is not float:
                        raise Exception

                    if type(limite_i) is not int and type(limite_i) is not float:
                        raise Exception

                    error = 7
                    if limite_s <= limite_i:
                        raise Exception

                    self.variable_limite_superior = limite_s
                    self.variable_limite_inferior = limite_i
                # limite_s = eval(self.limite_superior.get())
                # limite_i = eval(self.limite_inferior.get())

                # if type(limite_s) is not int and type(limite_s) is not float:
                #     raise Exception

                # if type(limite_i) is not int and type(limite_i) is not float:
                #     raise Exception

                # error = 7
                # if limite_s <= limite_i:
                #     raise Exception

                self.variable_tipo = t
                self.variable_tipo_saturador = tipo
                self.variable_k0 = valor_k0
                self.variable_matriz_y1 = y1
                self.variable_matriz_y2 = y2

                self.variable_matriz_k = matriz_k
                self.variable_matriz_ki = matriz_ki

                # self.variable_limite_superior = limite_s
                # self.variable_limite_inferior = limite_i

                self.ventanaCerrada = True
                self.windowRE.destroy()

            except Exception:

                n = int(self.n.get())
                m = int(self.m.get())

                if error == 0:
                    messagebox.showerror("Error", "Parámetro K0 inválido")

                if error == 1:

                    if m == 1:

                        if n == 1:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 1x1\n"
                                                          "[k11]")

                        if n == 2:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 1x2 \n"
                                                          "[k11 k12]")

                        if n == 3:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 1x3 \n"
                                                          "[k11 k12 k13]")

                        if n == 4:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 1x4 \n"
                                                          "[k11 k12 k13 k14]")

                    if m == 2:

                        if n == 1:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 2x1\n"
                                                          "[k11 ; k21]")

                        if n == 2:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 2x2 \n"
                                                          "[k11 k12 ; k21 k22]")

                        if n == 3:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 2x3 \n"
                                                          "[k11 k12 k13 ; k21 k22 k23]")

                        if n == 4:
                            messagebox.showerror("Error", "Matriz K inválida\n"
                                                          "Dimensiones: 2x4 \n"
                                                          "[k11 k12 k13 k14 ; k21 k22 k23 k24]")

                if error == 2:

                    messagebox.showerror("Error", "Salida y1 inválida")

                if error == 3:

                    messagebox.showerror("Error", "Salida y2 inválida")

                if error == 4:

                    if m == 1:

                        messagebox.showerror("Error", "Matriz Ki inválida\n"
                                                      "Dimensiones: 1x1 \n"
                                                      "[k11]")

                    if m == 2:

                        messagebox.showerror("Error", "Matriz Ki inválida\n"
                                                      "Dimensiones: 2x2 \n"
                                                      "[k11 k12 ; k21 k22]")

                if error == 6:
                    messagebox.showerror("Error", "Límite inválido")

                if error == 7:
                    messagebox.showerror("Error", "Límite superior debe ser mayor al límite inferior")

                self.windowRE.lift()

        else:
            self.ventanaCerrada = True
            self.windowRE.destroy()

    def cambiarDiagrama(self, value=None):

        n = int(self.n.get())
        m = int(self.m.get())
        t = self.v.get()

        if t == 1:
            if n == 1 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_1x1.png")

            if n == 1 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_1x2.png")

            if n == 2 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_2x1.png")

            if n == 2 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_2x2.png")

            if n == 3 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_3x1.png")

            if n == 3 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_3x2.png")

            if n == 4 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_4x1.png")

            if n == 4 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_RE_4x2.png")

            self.entry_ki.config(state='disabled')
            self.entry_k0.config(state='normal')
            self.saturator.config(state="disabled")
            self.entry_Superior.config(state="disabled")
            self.entry_Inferior.config(state="disabled")

            self.imagen_diagrama_bloques = PhotoImage(file="Diagrama_Bloques_RE.png")
            self.imagen_diagrama_bloques_label.configure(image=self.imagen_diagrama_bloques)
            self.imagen_diagrama_bloques_label.image = self.imagen_diagrama_bloques

        if t == 2:
            if n == 1 and m == 1:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_1x1.png")

            if n == 1 and m == 2:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_1x2.png")

            if n == 2 and m == 1:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_2x1.png")

            if n == 2 and m == 2:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_2x2.png")

            if n == 3 and m == 1:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_3x1.png")

            if n == 3 and m == 2:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_3x2.png")

            if n == 4 and m == 1:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_4x1.png")

            if n == 4 and m == 2:
                self.imagen_bloque = PhotoImage(file="Diagrama_REI_4x2.png")

            self.entry_ki.config(state='normal')
            self.entry_k0.config(state='disabled')
            self.saturator.config(state="normal")
            self.entry_Superior.config(state="normal")
            self.entry_Inferior.config(state="normal")
            self.imagen_diagrama_bloques = PhotoImage(file="Diagrama_Bloques_REI.png")
            self.imagen_diagrama_bloques_label.configure(image=self.imagen_diagrama_bloques)
            self.imagen_diagrama_bloques_label.image = self.imagen_diagrama_bloques

        self.imagen_bloque_label.configure(image=self.imagen_bloque)
        self.imagen_bloque_label.image = self.imagen_bloque

    def arrastrarRE(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoRE(self, event):

        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarRE()

        else:

            if self.ventanaCerrada is True:

                # -------------------------- 1 Salida --------------------------
                if self.tipoRE == "RE_1x1" or self.tipoRE == "RE_2x1" or self.tipoRE == "RE_3x1" or self.tipoRE == "RE_4x1":

                    if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida_1 RE

                        if self.creandoLinea is not None and self.salida_1 is None and not self.tipoCreandoLinea:
                            tupla = (self.posicionx + 32, self.posiciony - 1)
                            self.salida_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.salida_1 is None:
                            coord = [self.posicionx + 32, self.posiciony - 1]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         True)  # Nueva Conexion
                            self.salida_1 = self.creandoLinea

                # -------------------------- 2 Salidas --------------------------
                if self.tipoRE == "RE_1x2" or self.tipoRE == "RE_2x2" or self.tipoRE == "RE_3x2" or self.tipoRE == "RE_4x2":

                    if 38 > self.dx > 28 and -19 < self.dy < -7:  # Salida_1 RE

                        if self.creandoLinea is not None and self.salida_1 is None and not self.tipoCreandoLinea:
                            tupla = (self.posicionx + 32, self.posiciony - 13)
                            self.salida_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.salida_1 is None:
                            coord = [self.posicionx + 32, self.posiciony - 13]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         True)  # Nueva Conexion
                            self.salida_1 = self.creandoLinea

                    if 38 > self.dx > 28 and 19 > self.dy > 7:  # Salida_2 RE

                        if self.creandoLinea is not None and self.salida_2 is None and not self.tipoCreandoLinea:
                            tupla = (self.posicionx + 32, self.posiciony + 13)
                            self.salida_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.salida_2 is None:
                            coord = [self.posicionx + 32, self.posiciony + 13]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         True)  # Nueva Conexion
                            self.salida_2 = self.creandoLinea

                # -------------------------- 1 Entrada --------------------------
                if self.tipoRE == "RE_1x1" or self.tipoRE == "RE_1x2":

                    if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada_1 RE

                        if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 14)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 14]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and -6 < self.dy < 6:  # Entrada_2 RE

                        if self.creandoLinea is not None and self.entrada_2 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 1)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony - 1]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_2 = self.creandoLinea

                    if -38 < self.dx < -28 and 7 < self.dy < 19:  # Entrada_3 RE

                        if self.creandoLinea is not None and self.entrada_3 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 12)
                            self.entrada_3 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_3 is None:
                            coord = [self.posicionx - 32, self.posiciony + 12]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         False)  # Nueva Conexion
                            self.entrada_3 = self.creandoLinea

                # -------------------------- 2 Entradas --------------------------
                if self.tipoRE == "RE_2x1" or self.tipoRE == "RE_2x2":

                    if -38 < self.dx < -28 and -25 < self.dy < -14:  # Entrada_1 RE

                        if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx-32, self.posiciony - 20)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 20]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and -12 < self.dy < -1:  # Entrada_2 RE

                        if self.creandoLinea is not None and self.entrada_2 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx-32, self.posiciony - 7)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony - 7]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                            self.entrada_2 = self.creandoLinea

                    if -38 < self.dx < -28 and 1 < self.dy < 12:  # Entrada_3 RE

                        if self.creandoLinea is not None and self.entrada_3 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx-32, self.posiciony + 6)
                            self.entrada_3 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_3 is None:
                            coord = [self.posicionx - 32, self.posiciony + 6]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                            self.entrada_3 = self.creandoLinea

                    if -38 < self.dx < -28 and 14 < self.dy < 25:  # Entrada_4 RE

                        if self.creandoLinea is not None and self.entrada_4 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx-32, self.posiciony + 19)
                            self.entrada_4 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_4 is None:
                            coord = [self.posicionx - 32, self.posiciony + 19]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_4 = self.creandoLinea

                # -------------------------- 3 Entradas --------------------------
                if self.tipoRE == "RE_3x1" or self.tipoRE == "RE_3x2":

                    if -38 < self.dx < -28 and -32 < self.dy < -20:  # Entrada_1 RE

                        if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 27)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 27]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         False)  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada_2 RE

                        if self.creandoLinea is not None and self.entrada_2 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 14)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony - 14]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         False)  # Nueva Conexion
                            self.entrada_2 = self.creandoLinea

                    if -38 < self.dx < -28 and -6 < self.dy < 6:  # Entrada_3 RE

                        if self.creandoLinea is not None and self.entrada_3 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 1)
                            self.entrada_3 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_3 is None:
                            coord = [self.posicionx - 32, self.posiciony - 1]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         False)  # Nueva Conexion
                            self.entrada_3 = self.creandoLinea

                    if -38 < self.dx < -28 and 7 < self.dy < 19:  # Entrada_4 RE

                        if self.creandoLinea is not None and self.entrada_4 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 12)
                            self.entrada_4 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_4 is None:
                            coord = [self.posicionx - 32, self.posiciony + 12]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord,
                                                         False)  # Nueva Conexion
                            self.entrada_4 = self.creandoLinea

                    if -38 < self.dx < -28 and 20 < self.dy < 32:  # Entrada_5 RE

                        if self.creandoLinea is not None and self.entrada_5 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 25)
                            self.entrada_5 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_5 is None:
                            coord = [self.posicionx - 32, self.posiciony + 25]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_5 = self.creandoLinea

                # -------------------------- 4 Entradas --------------------------
                if self.tipoRE == "RE_4x1" or self.tipoRE == "RE_4x2":

                    if -38 < self.dx < -28 and -38 < self.dy < -27:  # Entrada_1 RE

                        if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 33)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 33]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and -25 < self.dy < -14:  # Entrada_2 RE

                        if self.creandoLinea is not None and self.entrada_2 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 20)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony - 20]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_2 = self.creandoLinea

                    if -38 < self.dx < -28 and -12 < self.dy < -1:  # Entrada_3 RE

                        if self.creandoLinea is not None and self.entrada_3 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 7)
                            self.entrada_3 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_3 is None:
                            coord = [self.posicionx - 32, self.posiciony - 7]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_3 = self.creandoLinea

                    if -38 < self.dx < -28 and 1 < self.dy < 12:  # Entrada_4 RE

                        if self.creandoLinea is not None and self.entrada_4 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 6)
                            self.entrada_4 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_4 is None:
                            coord = [self.posicionx - 32, self.posiciony + 6]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_4 = self.creandoLinea

                    if -38 < self.dx < -28 and 14 < self.dy < 25:  # Entrada_5 RE

                        if self.creandoLinea is not None and self.entrada_5 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 19)
                            self.entrada_5 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_5 is None:
                            coord = [self.posicionx - 32, self.posiciony + 19]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_5 = self.creandoLinea

                    if -38 < self.dx < -28 and 27 < self.dy < 38:  # Entrada_6 RE

                        if self.creandoLinea is not None and self.entrada_6 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 32)
                            self.entrada_6 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_6 is None:
                            coord = [self.posicionx - 32, self.posiciony + 32]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)
                            self.entrada_6 = self.creandoLinea


    def clickDerechoRE(self, event):

        self.eliminarRE()

    def eliminarRE(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelEntrada2)
            self.window.delete(self.labelEntrada3)
            self.window.delete(self.labelEntrada4)
            self.window.delete(self.labelEntrada5)
            self.window.delete(self.labelEntrada6)
            self.window.delete(self.labelEntrada7)
            self.window.delete(self.labelSalida1)
            self.window.delete(self.labelSalida2)
            self.window.unbind(self.nombre)

            if self.entrada_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_1)
            if self.entrada_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_2)
            if self.entrada_3 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_3)
            if self.entrada_4 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_4)
            if self.entrada_5 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_5)
            if self.entrada_6 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_6)
            if self.entrada_7 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_7)

            if self.salida_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.salida_1)
            if self.salida_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.salida_2)

            self.tupla_listas[6].remover(self.nombre)

    def enMovimientoRE(self, event):

        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        self.window.delete(self.labelSalida1)
        self.window.delete(self.labelSalida2)
        self.window.delete(self.labelEntrada1)
        self.window.delete(self.labelEntrada2)
        self.window.delete(self.labelEntrada3)
        self.window.delete(self.labelEntrada4)
        self.window.delete(self.labelEntrada5)
        self.window.delete(self.labelEntrada6)
        self.window.delete(self.labelEntrada7)

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------
            if self.entrada_1 is not None and self.entrada_1 != self.salida_1 and self.entrada_1 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_1, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_2 is not None and self.entrada_2 != self.salida_1 and self.entrada_2 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_2, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_3 is not None and self.entrada_3 != self.salida_1 and self.entrada_3 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_3, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_4 is not None and self.entrada_4 != self.salida_1 and self.entrada_4 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_4, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_5 is not None and self.entrada_5 != self.salida_1 and self.entrada_5 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_5, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_6 is not None and self.entrada_6 != self.salida_1 and self.entrada_6 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_6, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.entrada_7 is not None and self.entrada_7 != self.salida_1 and self.entrada_7 != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada_7, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.salida_1 is not None:
                self.tupla_listas[2].moverLinea(self.salida_1, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            if self.salida_2 is not None:
                self.tupla_listas[2].moverLinea(self.salida_2, self.nombre,
                                                event.x-self.posicionx-self.dx,
                                                event.y-self.posiciony-self.dy)

            # ----------------------------------
            self.posicionx = event.x - self.dx
            self.posiciony = event.y - self.dy

    def sobreIcono(self, event):

        x_icono = event.x - self.posicionx
        y_icono = event.y - self.posiciony


        # -------------------------- 1 Salida --------------------------
        if self.tipoRE == "RE_1x1" or self.tipoRE == "RE_2x1" or self.tipoRE == "RE_3x1" or self.tipoRE == "RE_4x1":

            if 38 > x_icono > 28 and 6 > abs(y_icono):  # Salida_1 RE
                if not self.estado_labelSalida1:
                    self.window.create_text(self.posicionx+35,
                                            self.posiciony+20,
                                            text="Salida 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelSalida1)
                    self.estado_labelSalida1 = True
            else:
                self.window.delete(self.labelSalida1)
                self.estado_labelSalida1 = False

        # -------------------------- 2 Salidas --------------------------
        if self.tipoRE == "RE_1x2" or self.tipoRE == "RE_2x2" or self.tipoRE == "RE_3x2" or self.tipoRE == "RE_4x2":

            if 38 > x_icono > 28 and -19 < y_icono < -7:  # Salida_1 RE
                if not self.estado_labelSalida1:
                    self.window.create_text(self.posicionx+35,
                                            self.posiciony+7,
                                            text="Salida 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelSalida1)
                    self.estado_labelSalida1 = True

            elif 38 > x_icono > 28 and 19 > y_icono > 7:  # Salida_2 RE
                if not self.estado_labelSalida2:
                    self.window.create_text(self.posicionx+35,
                                            self.posiciony+33,
                                            text="Salida 2",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelSalida2)
                    self.estado_labelSalida2 = True

            else:
                self.window.delete(self.labelSalida1)
                self.window.delete(self.labelSalida2)
                self.estado_labelSalida1 = False
                self.estado_labelSalida2 = False
        '''
        # -------------------------- 1 Entrada --------------------------
        if self.tipoRE == "RE_1x1" or self.tipoRE == "RE_1x2":

            if -38 < x_icono < -28 and 6 > abs(y_icono):  # Entrada_1 RE
                if not self.estado_labelEntrada1:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+20,
                                            text="Entrada 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada1)
                    self.estado_labelEntrada1 = True

            else:
                self.window.delete(self.labelEntrada1)
                self.estado_labelEntrada1 = False

        # -------------------------- 2 Entradas --------------------------
        if self.tipoRE == "RE_2x1" or self.tipoRE == "RE_2x2":

            if -38 < x_icono < -28 and -19 < y_icono < -7:  # Entrada_1 RE
                if not self.estado_labelEntrada1:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+7,
                                            text="Entrada 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada1)
                    self.estado_labelEntrada1 = True

            elif -38 < x_icono < -28 and 19 > y_icono > 7:  # Entrada_2 RE
                if not self.estado_labelEntrada2:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+33,
                                            text="Entrada 2",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada2)
                    self.estado_labelEntrada2 = True
            else:
                self.window.delete(self.labelEntrada1, self.labelEntrada2)
                self.estado_labelEntrada1 = False
                self.estado_labelEntrada2 = False


        # -------------------------- 3 Entradas --------------------------
        if self.tipoRE == "RE_3x1" or self.tipoRE == "RE_3x2":

            if -38 < x_icono < -28 and -19 < y_icono < -7:  # Entrada_1 RE
                if not self.estado_labelEntrada1:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+7,
                                            text="Entrada 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada1)
                    self.estado_labelEntrada1 = True

            elif -38 < x_icono < -28 and 6 > abs(y_icono):  # Entrada_2 RE
                if not self.estado_labelEntrada2:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+20,
                                            text="Entrada 2",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada2)
                    self.estado_labelEntrada2 = True

            elif -38 < x_icono < -28 and 19 > y_icono > 7:  # Entrada_3 RE
                if not self.estado_labelEntrada3:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+33,
                                            text="Entrada 3",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada2)
                    self.estado_labelEntrada3 = True

            else:
                self.window.delete(self.labelEntrada1, self.labelEntrada2)
                self.window.delete(self.labelEntrada3)
                self.estado_labelEntrada1 = False
                self.estado_labelEntrada2 = False
                self.estado_labelEntrada3 = False

        # -------------------------- 4 Entradas --------------------------
        if self.tipoRE == "RE_4x1" or self.tipoRE == "RE_4x2":

            if -38 < x_icono < -28 and -25 < y_icono < -14:  # Entrada_1 RE
                if not self.estado_labelEntrada1:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+1,
                                            text="Entrada 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada1)
                    self.estado_labelEntrada1 = True

            elif -38 < x_icono < -28 and -12 < y_icono < -1:  # Entrada_2 RE
                if not self.estado_labelEntrada2:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+14,
                                            text="Entrada 2",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada2)
                    self.estado_labelEntrada2 = True

            elif -38 < x_icono < -28 and 12 > y_icono > 1:  # Entrada_3 RE
                if not self.estado_labelEntrada3:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+27,
                                            text="Entrada 3",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada2)
                    self.estado_labelEntrada3 = True

            elif -38 < x_icono < -28 and 25 > y_icono > 14:  # Entrada_4 RE
                if not self.estado_labelEntrada4:
                    self.window.create_text(self.posicionx-35,
                                            self.posiciony+40,
                                            text="Entrada 4",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada4)
                    self.estado_labelEntrada4 = True

            else:

                self.window.delete(self.labelEntrada1, self.labelEntrada2)
                self.window.delete(self.labelEntrada3, self.labelEntrada4)

                self.estado_labelEntrada1 = False
                self.estado_labelEntrada2 = False
                self.estado_labelEntrada3 = False
                self.estado_labelEntrada4 = False
        '''

    def dentroDelIcono(self, event):
        # self.window.create_text(self.posicionx,
        #                         self.posiciony-51,
        #                         text=self.nombre,
        #                         font=("Arial Rounded MT", -12, "bold"),
        #                         tags=self.label_con_nombre)
        pass

    def afueraDelIcono(self, event):
        self.window.delete(self.labelSalida1, self.labelSalida2)
        self.window.delete(self.labelEntrada1, self.labelEntrada2)
        self.window.delete(self.labelEntrada3, self.labelEntrada4)

        self.estado_labelSalida1 = False
        self.estado_labelSalida2 = False
        self.estado_labelEntrada1 = False
        self.estado_labelEntrada2 = False
        self.estado_labelEntrada3 = False
        self.estado_labelEntrada4 = False
# --------------------------------------------

    def senal_nombres(self, lista_nombres):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.tipoRE == "RE_1x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_1x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_2x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            if self.entrada_5 is not None:
                sim_entrada5 = a.obtenerBloqueConexion(self.entrada_5, self.nombre)
                sim_entrada5.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_2x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            if self.entrada_5 is not None:
                sim_entrada5 = a.obtenerBloqueConexion(self.entrada_5, self.nombre)
                sim_entrada5.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_3x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            if self.entrada_5 is not None:
                sim_entrada5 = a.obtenerBloqueConexion(self.entrada_5, self.nombre)
                sim_entrada5.senal_nombres(lista_nombres)

            if self.entrada_6 is not None:
                sim_entrada6 = a.obtenerBloqueConexion(self.entrada_6, self.nombre)
                sim_entrada6.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_3x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            if self.entrada_5 is not None:
                sim_entrada5 = a.obtenerBloqueConexion(self.entrada_5, self.nombre)
                sim_entrada5.senal_nombres(lista_nombres)

            if self.entrada_6 is not None:
                sim_entrada6 = a.obtenerBloqueConexion(self.entrada_6, self.nombre)
                sim_entrada6.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_4x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            if self.entrada_5 is not None:
                sim_entrada5 = a.obtenerBloqueConexion(self.entrada_5, self.nombre)
                sim_entrada5.senal_nombres(lista_nombres)

            if self.entrada_6 is not None:
                sim_entrada6 = a.obtenerBloqueConexion(self.entrada_6, self.nombre)
                sim_entrada6.senal_nombres(lista_nombres)

            if self.entrada_7 is not None:
                sim_entrada7 = a.obtenerBloqueConexion(self.entrada_7, self.nombre)
                sim_entrada7.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        if self.tipoRE == "RE_4x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                sim_entrada1.senal_nombres(lista_nombres)

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                sim_entrada3.senal_nombres(lista_nombres)

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                sim_entrada4.senal_nombres(lista_nombres)

            if self.entrada_5 is not None:
                sim_entrada5 = a.obtenerBloqueConexion(self.entrada_5, self.nombre)
                sim_entrada5.senal_nombres(lista_nombres)

            if self.entrada_6 is not None:
                sim_entrada6 = a.obtenerBloqueConexion(self.entrada_6, self.nombre)
                sim_entrada6.senal_nombres(lista_nombres)

            if self.entrada_7 is not None:
                sim_entrada7 = a.obtenerBloqueConexion(self.entrada_7, self.nombre)
                sim_entrada7.senal_nombres(lista_nombres)

            lista_nombres.append(self.nombre)
            return lista_nombres

        return None

    def senal_simulacion(self, n, ts, conexion):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if n == 0:

            self.y_n = 0
            self.u1_n = 0
            self.u1_n_1 = 0
            self.u2_n = 0
            self.u2_n_1 = 0
            self.x_n = 0
            self.x_n_1 = 0

        if self.tipoRE == "RE_1x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)

            else:
                ent1 = 0

            return ent1

        if self.tipoRE == "RE_1x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)

            else:
                ent1 = 0

            if conexion == self.salida_1:
                return ent1

            if conexion == self.salida_2:
                return -ent1

        if self.tipoRE == "RE_2x1":

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

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                ent3 = sim_entrada3.senal_simulacion(n, ts, self.entrada_3)

            else:
                ent3 = 0.0

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                ent4 = sim_entrada4.senal_simulacion(n, ts, self.entrada_4)

            else:
                ent4 = 0.0

            if self.variable_tipo == 1:  # RE

                matriz_x = np.array([[ent3], [ent4]])

                matriz_k = np.matrix(self.variable_matriz_k)

                u1 = ent1 * self.variable_k0

                u2 = matriz_k.dot(matriz_x)
                u2 = u2.item(0)

                u = u1 - u2

                return u

            if self.variable_tipo == 2:  # REI

                self.x_n = ent1 - self.y_n  # self.y_n -> Salida de la Planta

                matriz_ki = np.matrix(self.variable_matriz_ki)
                ki = matriz_ki.item(0)
                ts = 0.02

                self.u1_n = self.u1_n_1 + ki * ts * self.x_n_1

                matriz_x = np.array([[ent3], [ent4]])
                matriz_k = np.matrix(self.variable_matriz_k)

                self.u2_n = matriz_k.dot(matriz_x)
                self.u2_n = self.u2_n.item(0)

                u = self.u1_n - self.u2_n

                self.x_n_1 = self.x_n
                self.u1_n_1 = self.u1_n

                return u

            else:

                return 0

        if self.tipoRE == "RE_2x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)
            else:
                ent1 = 0

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada_2)
            else: ent2 = 0

            if conexion == self.salida_1:
                return ent1 - ent2

            if conexion == self.salida_2:
                return ent1 + ent2

        if self.tipoRE == "RE_3x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)

            else:
                ent1 = 0

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada_2)
            else:
                ent2 = 0

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                ent3 = sim_entrada3.senal_simulacion(n, ts, self.entrada_3)
            else:
                ent3 = 0

            return ent1 - ent2 - ent3

        if self.tipoRE == "RE_3x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)
            else:
                ent1 = 0

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada_2)
            else:
                ent2 = 0

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                ent3 = sim_entrada3.senal_simulacion(n, ts, self.entrada_3)
            else:
                ent3 = 0

            if conexion == self.salida_1:
                return ent1 - ent2 - ent3

            if conexion == self.salida_2:
                return ent1 + ent2 + ent3

        if self.tipoRE == "RE_4x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)
            else:
                ent1 = 0

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada_2)
            else:
                ent2 = 0

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                ent3 = sim_entrada3.senal_simulacion(n, ts, self.entrada_3)
            else:
                ent3 = 0

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                ent4 = sim_entrada4.senal_simulacion(n, ts, self.entrada_4)
            else:
                ent4 = 0

            return ent1 - ent2 - ent3 - ent4

        if self.tipoRE == "RE_4x2":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada_1)
            else:
                ent1 = 0

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                ent2 = sim_entrada2.senal_simulacion(n, ts, self.entrada_2)
            else:
                ent2 = 0

            if self.entrada_3 is not None:
                sim_entrada3 = a.obtenerBloqueConexion(self.entrada_3, self.nombre)
                ent3 = sim_entrada3.senal_simulacion(n, ts, self.entrada_3)
            else:
                ent3 = 0

            if self.entrada_4 is not None:
                sim_entrada4 = a.obtenerBloqueConexion(self.entrada_4, self.nombre)
                ent4 = sim_entrada4.senal_simulacion(n, ts, self.entrada_4)
            else:
                ent4 = 0

            if conexion == self.salida_1:
                return ent1 - ent2 - ent3 - ent4

            if conexion == self.salida_2:
                return ent1 + ent2 + ent3 + ent4


class ListaRE:

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

        temp = NodoRE(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickRE)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarRE)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoRE)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoRE)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoRE)  # 3 Windows/Unix
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

        temp = NodoRE(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickRE)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarRE)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoRE)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoRE)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoRE)  # 3 Windows/Unix
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
