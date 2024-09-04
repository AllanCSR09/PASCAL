from tkinter import *
from tkinter import messagebox
import numpy as np
import Simulacion
from tkinter import ttk


class NodoPFT:
    def __init__(self, id_PFT, tupla_listas, px, py):

        self.dato = id_PFT
        self.tipo = "PFT"
        self.tipoPFT = "PFT_1x1"

        self.nombre = "PFT_" + str(id_PFT)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "T"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada_1 = None
        self.entrada_2 = None

        self.salida_1 = None
        self.salida_2 = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]

        if self.tipoPFT == "PFT_1x1":
            self.imagen = PhotoImage(file="PFT_1x1.png")
        if self.tipoPFT == "PFT_1x2":
            self.imagen = PhotoImage(file="PFT_1x2.png")
        if self.tipoPFT == "PFT_2x1":
            self.imagen = PhotoImage(file="PFT_2x1.png")
        if self.tipoPFT == "PFT_2x2":
            self.imagen = PhotoImage(file="PFT_2x2.png")

        self.icono = self.window.create_image(
            px, py, image=self.imagen, tags=self.nombre
        )
        self.label_con_nombre = self.nombre + "l"  # tag etiqueta con nombre

        self.labelNombre = self.window.create_text(
            self.posicionx,
            self.posiciony - 45,
            text=self.nombre,
            font=("Arial Rounded MT", -12, "bold"),
            tags=self.label_con_nombre,
        )

        # - - - - - -

        self.estado_labelSalida1 = False
        self.labelSalida1 = self.nombre + "s1"
        self.estado_labelSalida2 = False
        self.labelSalida2 = self.nombre + "s2"

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
        self.tipoPFT = "PFT_1x1"
        self.variable_orden = 1
        self.variable_orden2 = 1
        self.variable_f2 = 1
        self.variable_n = 1
        self.variable_m = 1
        self.variable_numerador = ["b2", "b1", "b0"]
        self.variable_denominador = ["a2", "a1", "a0"]
        self.variable_numerador2 = ["b2", "b1", "b0"]
        self.variable_denominador2 = ["a2", "a1", "a0"]

        print("La lista es de numerador 1 es:", self.variable_numerador)
        print("El orden de la función 1 es:", self.variable_orden)

        # Simulacion -----------------------
        self.ordenEcuacion = 2
        self.y_n = 0
        self.y_n_1 = 0
        self.y_n_2 = 0
        self.y_n_3 = 0

        self.x_n = 0
        self.x_n_1 = 0
        self.x_n_2 = 0
        self.x_n_3 = 0

    def dobleClickPFT(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowPFT = Toplevel(self.mainWindow)
            self.windowPFT.resizable(False, False)
            self.windowPFT.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowPFT, bg="#2C2C2C")
            self.frame2 = Frame(self.windowPFT, bg="white")
            self.frame3 = Frame(self.windowPFT, bg="white")

            self.imagen_ventana = PhotoImage(file="PFTv.png")
            self.imagen_ventana_label = Label(
                self.frame1,
                image=self.imagen_ventana,
                borderwidth=0,
                highlightthickness=0,
                bg="#2C2C2C",
                padx=0,
                pady=10,
            )

            self.imagen_ventana_label.image = self.imagen_ventana
            self.imagen_ventana_label.pack(side=LEFT, padx=10)

            Label(
                self.frame1,
                text=self.nombre,
                bg="#2C2C2C",
                fg="White",
                font=("Arial Rounded MT", -20),
            ).pack(side=LEFT)

            # -------------------- FRAME 2 --------------------

            Label(
                self.frame2,
                text="Planta de Función de transferencia",
                font=("Arial Rounded MT Bold", -18),
            ).grid(row=0, column=0, columnspan=3, sticky=W, padx=10, pady=10)

            self.imagen_bloque = PhotoImage(file="Diagrama_PFT_1x1.png")
            self.imagen_bloque_label = Label(
                self.frame2,
                image=self.imagen_bloque,
                borderwidth=0,
                highlightthickness=0,
                padx=0,
                pady=0,
            )
            self.imagen_bloque_label.image = self.imagen_bloque
            self.imagen_bloque_label.grid(
                row=1, column=0, columnspan=1, pady=(0, 10), padx=(20, 0)
            )

            self.imagen_funcion = PhotoImage(
                file="Ecuacion_Funcion_Transferencia_O1.png"
            )
            self.imagen_funcion_label = Label(
                self.frame2,
                image=self.imagen_funcion,
                borderwidth=0,
                highlightthickness=0,
                padx=0,
                pady=0,
            )
            self.imagen_funcion_label.image = self.imagen_funcion
            self.imagen_funcion_label.grid(row=1, column=1, columnspan=1, pady=(0, 10))

            self.orden = StringVar()
            self.orden2 = StringVar()

            if self.orden is None:
                self.orden.set("1")
            else:
                self.orden.set(str(self.variable_orden))

            self.cambiarDiagramaEcua(None)

            opciones_orden = ["1", "2"]

            Label(self.frame2, text="Orden FT1:").grid(
                row=2, column=0, sticky=W, padx=(20, 10)
            )
            ttk.OptionMenu(
                self.frame2,
                self.orden,
                None,
                *opciones_orden,
                command=self.cambiarDiagramaEcua,
            ).grid(row=2, column=0, sticky=E, padx=(0, 40))

            if self.orden2 is None:
                self.orden2.set("1")
            else:
                self.orden2.set(str(self.variable_orden2))

            self.cambiarDiagramaEcua(None)

            opciones_orden2 = ["1", "2"]

            Label(self.frame2, text="Orden FT2:").grid(
                row=3, column=0, sticky=W, padx=(20, 10)
            )
            self.o2 = ttk.OptionMenu(
                self.frame2,
                self.orden2,
                None,
                *opciones_orden2,
                command=self.cambiarDiagramaEcua,
            )
            self.o2.grid(row=3, column=0, sticky=E, padx=(0, 40))

            self.n = StringVar()
            self.m = StringVar()

            if self.variable_n is None:
                self.n.set("1")
            else:
                self.n.set(str(self.variable_n))

            if self.variable_m is None:
                self.m.set("1")
            else:
                self.m.set(str(self.variable_m))

            self.opciones_entrada = ["1", "2"]
            self.opciones_salida = ["1", "2"]

            Label(self.frame2, text="Entradas:").grid(row=2, column=1, sticky=W)
            ttk.OptionMenu(
                self.frame2,
                self.n,
                None,
                *self.opciones_entrada,
                command=self.cambiarDiagrama,
            ).grid(row=2, column=1, sticky=E, padx=(0, 80))

            Label(self.frame2, text="Salidas: ").grid(row=3, column=1, sticky=W)
            ttk.OptionMenu(
                self.frame2,
                self.m,
                None,
                *self.opciones_salida,
                command=self.cambiarDiagrama,
            ).grid(row=3, column=1, sticky=E, padx=(0, 80))

            self.numerador = StringVar()
            self.numerador2 = StringVar()
            self.denominador = StringVar()
            self.denominador2 = StringVar()

            Label(self.frame2, text="Función de transferencia 1:").grid(
                row=5, column=0, sticky=W, padx=(20, 0), pady=(10, 10)
            )

            if self.variable_numerador is None:
                self.numerador.set("[b3, b2, b1, b0]")
            else:
                num = "["
                for i in range(0, len(self.variable_numerador)):

                    if i == len(self.variable_numerador) - 1:
                        num = num + str(self.variable_numerador[i]) + "]"
                    else:
                        num = num + str(self.variable_numerador[i]) + ", "

                self.numerador.set(num)

            Label(self.frame2, text="Numerador:").grid(
                row=6, column=0, sticky=W, padx=(20, 0)
            )
            ttk.Entry(self.frame2, width=25, textvariable=self.numerador).grid(
                row=6, column=1, sticky=W, padx=(0, 20)
            )

            if self.variable_denominador is None:
                self.denominador.set("[a3, a2, a1, a0]")
            else:
                den = "["
                for i in range(0, len(self.variable_denominador)):

                    if i == len(self.variable_denominador) - 1:
                        den = den + str(self.variable_denominador[i]) + "]"
                    else:
                        den = den + str(self.variable_denominador[i]) + ", "

                self.denominador.set(den)

            Label(self.frame2, text="Denominador:").grid(
                row=7, column=0, sticky=W, padx=(20, 0), pady=(0, 0)
            )
            ttk.Entry(self.frame2, width=25, textvariable=self.denominador).grid(
                row=7, column=1, sticky=W, padx=(0, 20), pady=(0, 0)
            )

            Label(self.frame2, text="Función de transferencia 2:").grid(
                row=8, column=0, sticky=W, padx=(20, 0), pady=(10, 10)
            )

            if self.variable_numerador2 is None:
                self.numerador2.set("[b3, b2, b1, b0]")
            else:
                num2 = "["
                for i in range(0, len(self.variable_numerador2)):

                    if i == len(self.variable_numerador2) - 1:
                        num2 = num2 + str(self.variable_numerador2[i]) + "]"
                    else:
                        num2 = num2 + str(self.variable_numerador2[i]) + ", "

                self.numerador2.set(num2)

            Label(self.frame2, text="Numerador:").grid(
                row=9, column=0, sticky=W, padx=(20, 0)
            )
            self.entry_n2 = ttk.Entry(
                self.frame2, width=25, textvariable=self.numerador2
            )
            self.entry_n2.grid(row=9, column=1, sticky=W, padx=(0, 20))

            if self.variable_denominador2 is None:
                self.denominador2.set("[a3, a2, a1, a0]")
            else:
                den2 = "["
                for i in range(0, len(self.variable_denominador2)):

                    if i == len(self.variable_denominador2) - 1:
                        den2 = den2 + str(self.variable_denominador2[i]) + "]"
                    else:
                        den2 = den2 + str(self.variable_denominador2[i]) + ", "

                self.denominador2.set(den)

            Label(self.frame2, text="Denominador:").grid(
                row=10, column=0, sticky=W, padx=(20, 0), pady=(0, 0)
            )
            self.out_n2 = ttk.Entry(
                self.frame2, width=25, textvariable=self.denominador2
            )
            self.out_n2.grid(row=10, column=1, sticky=W, padx=(0, 20), pady=(0, 0))

            self.rt = IntVar()
            if self.tipoPFT == "PFT_1x1":
                self.rt.set(0)
            else:
                self.rt.set(1)

            self.cambiarDiagrama(None)
            # self.cambiarIcono()

            #     ttk.Checkbutton(
            #        self.frame2,
            #       text="Retroalimentacion",
            #      variable=self.rt,
            #     command=self.cambiarIcono,
            # ).grid(row=10, column=1, sticky=E, padx=(0, 20), pady=(0, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(
                self.frame3,
                text="Aceptar",
                command=lambda: self.cerrarVentanaPFT("Aceptar"),
            ).pack(side=RIGHT, padx=(10, 20), pady=(15, 10))
            ttk.Button(
                self.frame3,
                text="Cancelar",
                command=lambda: self.cerrarVentanaPFT("Cancelar"),
            ).pack(side=RIGHT, pady=(15, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowPFT.protocol("WM_DELETE_WINDOW", self.cerrarVentanaPFT)

            self.windowPFT.withdraw()
            self.windowPFT.update_idletasks()
            x = (
                self.windowPFT.winfo_screenwidth() - self.windowPFT.winfo_reqwidth()
            ) / 2
            y = (
                self.windowPFT.winfo_screenheight() - self.windowPFT.winfo_reqheight()
            ) / 2
            self.windowPFT.geometry("+%d+%d" % (x, y))

            self.windowPFT.deiconify()

            # Color
            s = ttk.Style()
            s.configure("Style.TRadiobutton", background="White", foreground="black")
            s1 = ttk.Style()
            s1.configure("Style2.TCheckbutton", background="White", foreground="black")
            for wid in self.frame2.winfo_children():
                if wid.winfo_class() == "Label":
                    wid.configure(bg="white")
                if wid.winfo_class() == "TRadiobutton":
                    wid.configure(style="Style.TRadiobutton")
                if wid.winfo_class() == "Message":
                    wid.configure(bg="white")
                if wid.winfo_class() == "TCheckbutton":
                    wid.configure(style="Style2.TCheckbutton")

        else:

            self.windowPFT.lift()

    def cerrarVentanaPFT(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            print("La lista de numerador 1 es:", self.numerador.get())
            print("El orden de la función 1 es:", int(self.orden.get()))
            error = 0
            orden = int(self.orden.get())
            orden2 = int(self.orden2.get())

            try:
                m = int(self.m.get())
                n = int(self.n.get())

                if n == 1 and m == 1:
                    print("Hasta aqui se completo el codigo 0")

                    valor_num = eval(self.numerador.get())

                    error = 1

                    valor_den = eval(self.denominador.get())

                    print("Hasta aqui se completo el codigo a")

                    if type(valor_num) is not list:
                        raise Exception

                    print("Hasta aqui se completo el codigo b")

                    error = 2

                    if len(valor_num) == 0 and orden == 1:
                        valor_num = [0, 0]

                    if len(valor_num) == 0 and orden == 2:
                        valor_num = [0, 0, 0]

                    for i in valor_num:

                        if type(i) is not int and type(i) is not float:
                            raise Exception

                    print("Hasta aqui se completo el codigo c")

                    error = 3

                    print("Hasta aqui se completo el codigo d")

                    if orden == 1:

                        if type(valor_den) is int or type(valor_den) is float:
                            valor_den = [valor_den]

                    print("Hasta aqui se completo el codigo e")

                    if type(valor_den) is not list:
                        raise Exception

                    print("Hasta aqui se completo el codigo f")

                    if len(valor_den) == 0 and orden == 1:
                        valor_den = [0]

                    print("Hasta aqui se completo el codigo g")

                    if len(valor_den) == 0 and orden == 2:
                        valor_den = [0, 0]

                    print("Hasta aqui se completo el codigo h")

                    for i in valor_den:

                        if type(i) is not int and type(i) is not float:
                            raise Exception

                    error = 4

                    print("Hasta aqui se completo el codigo i")

                    if orden == 1:
                        numerador = [0, 0]
                    else:
                        numerador = [0, 0, 0]

                    print("Hasta aqui se completo el codigo j")

                    for i in range(0, len(valor_num)):
                        numerador[-(i + 1)] = valor_num[-(i + 1)]

                    print("Hasta aqui se completo el codigo k")

                    valor_num = numerador

                    print("Hasta aqui se completo el codigo l")

                    error = 5
                    if orden == 1:
                        denominador = [0]
                    else:
                        denominador = [0, 0]

                    print("Hasta aqui se completo el codigo m")

                    for i in range(0, len(valor_den)):
                        denominador[-(i + 1)] = valor_den[-(i + 1)]

                    print("Hasta aqui se completo el codigo n")

                    valor_den = denominador

                    print("Hasta aqui se completo el codigo o")

                    if len(valor_num) > 3 and orden == 2:
                        raise Exception

                    print("Hasta aqui se completo el codigo p")

                    if len(valor_num) > 2 and orden == 1:
                        raise Exception

                    print("Hasta aqui se completo el codigo q")

                    if len(valor_den) > 2 and orden == 2:
                        raise Exception

                    print("Hasta aqui se completo el codigo r")

                    if len(valor_den) > 1 and orden == 1:
                        raise Exception

                    print("Hasta aqui se completo el codigo s")

                    print("Hasta aqui se completo el codigo 872")

                    self.variable_numerador = valor_num

                    print("Hasta aqui se completo el codigo 873")
                    self.variable_denominador = valor_den

                    print("Hasta aqui se completo el codigo 874")

                if n != 1 or m != 1:
                    error = 0

                    print("Hasta aqui se completo el codigo 02")

                    valor_num = eval(self.numerador.get())

                    error = 1

                    valor_den = eval(self.denominador.get())

                    print("Hasta aqui se completo el codigo a2")

                    if type(valor_num) is not list:
                        raise Exception

                    print("Hasta aqui se completo el codigo b2")

                    error = 2

                    if len(valor_num) == 0 and orden == 1:
                        valor_num = [0, 0]

                    if len(valor_num) == 0 and orden == 2:
                        valor_num = [0, 0, 0]

                    for i in valor_num:

                        if type(i) is not int and type(i) is not float:
                            raise Exception

                    print("Hasta aqui se completo el codigo c2")

                    error = 3

                    print("Hasta aqui se completo el codigo d2")

                    if orden == 1:

                        if type(valor_den) is int or type(valor_den) is float:
                            valor_den = [valor_den]

                    if type(valor_den) is not list:
                        raise Exception

                    if len(valor_den) == 0 and orden == 1:
                        valor_den = [0]

                    if len(valor_den) == 0 and orden == 2:
                        valor_den = [0, 0]

                    for i in valor_den:

                        if type(i) is not int and type(i) is not float:
                            raise Exception

                    error = 4

                    if orden == 1:
                        numerador = [0, 0]
                    else:
                        numerador = [0, 0, 0]

                    for i in range(0, len(valor_num)):
                        numerador[-(i + 1)] = valor_num[-(i + 1)]

                    valor_num = numerador

                    error = 5

                    if orden == 1:
                        denominador = [0]
                    else:
                        denominador = [0, 0]

                    for i in range(0, len(valor_den)):
                        denominador[-(i + 1)] = valor_den[-(i + 1)]

                    valor_den = denominador

                    if len(valor_num) > 3 and orden == 2:
                        raise Exception

                    if len(valor_num) > 2 and orden == 1:
                        raise Exception

                    if len(valor_den) > 2 and orden == 2:
                        raise Exception

                    if len(valor_den) > 1 and orden == 1:
                        raise Exception

                    # ------------------------- FT 2 --------------------------#

                    error = 6

                    print("Hasta aqui se completo el codigo 022")

                    valor_num2 = eval(self.numerador2.get())

                    error = 7

                    valor_den2 = eval(self.denominador2.get())

                    print("Hasta aqui se completo el codigo a22")

                    if type(valor_num2) is not list:
                        raise Exception

                    print("Hasta aqui se completo el codigo b22")

                    error = 8

                    if len(valor_num2) == 0 and orden2 == 1:
                        valor_num2 = [0, 0]

                    if len(valor_num2) == 0 and orden2 == 2:
                        valor_num2 = [0, 0, 0]

                    for i in valor_num2:

                        if type(i) is not int and type(i) is not float:
                            raise Exception

                    print("Hasta aqui se completo el codigo c22")

                    error = 9

                    print("Hasta aqui se completo el codigo d22")

                    if orden2 == 1:

                        if type(valor_den2) is int or type(valor_den2) is float:
                            valor_den2 = [valor_den2]

                    if type(valor_den2) is not list:
                        raise Exception

                    if len(valor_den2) == 0 and orden2 == 1:
                        valor_den2 = [0]

                    if len(valor_den2) == 0 and orden2 == 2:
                        valor_den2 = [0, 0]

                    for i in valor_den2:

                        if type(i) is not int and type(i) is not float:
                            raise Exception

                    error = 10

                    if orden2 == 1:
                        numerador2 = [0, 0]
                    else:
                        numerador2 = [0, 0, 0]

                    for i in range(0, len(valor_num2)):
                        numerador2[-(i + 1)] = valor_num2[-(i + 1)]

                    valor_num2 = numerador2

                    error = 11
                    if orden2 == 1:
                        denominador2 = [0]
                    else:
                        denominador2 = [0, 0]

                    for i in range(0, len(valor_den2)):
                        denominador2[-(i + 1)] = valor_den2[-(i + 1)]

                    valor_den2 = denominador2

                    if len(valor_num2) > 3 and orden2 == 2:
                        raise Exception

                    if len(valor_num2) > 2 and orden2 == 1:
                        raise Exception

                    if len(valor_den2) > 2 and orden2 == 2:
                        raise Exception

                    if len(valor_den2) > 1 and orden2 == 1:
                        raise Exception
                    print("Hasta aqui se completo el codigo 1872")

                    self.variable_numerador = valor_num

                    print("Hasta aqui se completo el codigo 1873")
                    self.variable_denominador = valor_den

                    print("Hasta aqui se completo el codigo 1874")
                    self.variable_numerador2 = valor_num2

                    print("Hasta aqui se completo el codigo 1875")
                    self.variable_denominador2 = valor_den2

                    print("Hasta aqui se completo el codigo 1876")

                print("Hasta aqui se completo el codigo 62")

                posicion = 45

                print("Hasta aqui se completo el codigo 82")

                if n == 1 and m == 1:
                    self.tipoPFT = "PFT_1x1"
                    self.imagen = PhotoImage(file="PFT_1x1.png")
                    self.window.itemconfig(self.nombre, image=self.imagen)
                    posicion = 45

                if n == 1 and m == 2:
                    self.tipoPFT = "PFT_1x2"
                    self.imagen = PhotoImage(file="PFT_1x2.png")
                    self.window.itemconfig(self.nombre, image=self.imagen)
                    posicion = 45

                if n == 2 and m == 1:
                    self.tipoPFT = "PFT_2x1"
                    self.imagen = PhotoImage(file="PFT_2x1.png")
                    self.window.itemconfig(self.nombre, image=self.imagen)
                    posicion = 45

                if n == 2 and m == 2:
                    self.tipoPFT = "PFT_2x2"
                    self.imagen = PhotoImage(file="PFT_2x2.png")
                    self.window.itemconfig(self.nombre, image=self.imagen)
                    posicion = 45

                self.tupla_listas[1].delete(self.label_con_nombre)
                self.labelNombre = self.window.create_text(
                    self.posicionx,
                    self.posiciony - posicion,
                    text=self.nombre,
                    font=("Arial Rounded MT", -12, "bold"),
                    tags=self.label_con_nombre,
                )

                # En caso de cambio en numero de entradas/salidas, eliminar conexiones.
                print("Hasta aqui se completo el codigo 672")
                if self.variable_n != n or self.variable_m != m:

                    self.variable_n = n
                    self.variable_m = m

                    if self.entrada_1 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_1)
                    if self.entrada_2 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_2)
                    if self.salida_1 is not None:
                        self.tupla_listas[2].eliminarConexion(self.salida_1)
                    if self.salida_2 is not None:
                        self.tupla_listas[2].eliminarConexion(self.salida_2)

                # -----------------------------

                print("Hasta aqui se completo el codigo 900")

                self.variable_orden = int(self.orden.get())
                self.variable_orden2 = int(self.orden2.get())

                self.ventanaCerrada = True
                self.windowPFT.destroy()

            except Exception:

                n = int(self.n.get())
                m = int(self.m.get())

                if error == 0:
                    messagebox.showerror(
                        "Error",
                        "Numerador FT1 inválido\nEl formato deben ser valores numéricos",
                    )

                if error == 1:
                    messagebox.showerror(
                        "Error",
                        "Denominador FT1 inválido\nEl formato deben ser con valores numéricos",
                    )

                if error == 2 and orden == 1:
                    messagebox.showerror(
                        "Error", "Numerador FT1 inválido\nEl formato debe ser: [b1, b0]"
                    )
                if error == 2 and orden == 2:
                    messagebox.showerror(
                        "Error",
                        "Numerador FT1 inválido\nEl formato debe ser: [b2, b1, b0]",
                    )
                if error == 3 and orden == 1:
                    messagebox.showerror(
                        "Error", "Denominador FT1 inválido\nEl formato debe ser: [a0]"
                    )
                if error == 3 and orden == 2:
                    messagebox.showerror(
                        "Error",
                        "Denominador FT1 inválido\nEl formato debe ser: [a1, a0]",
                    )
                if error == 4 and orden == 1:
                    messagebox.showerror(
                        "Error", "El grado del numerador FT1 debe ser igual a 1"
                    )
                if error == 4 and orden == 2:
                    messagebox.showerror(
                        "Error", "El grado del numerador FT1 debe ser igual a 2"
                    )
                if error == 5 and orden == 1:
                    messagebox.showerror(
                        "Error", "El grado del denominador FT1 debe ser igual a 1"
                    )
                if error == 5 and orden == 2:
                    messagebox.showerror(
                        "Error", "El grado del denominador FT1 debe ser igual a 2"
                    )

                # ------------------------------ ERRORES FT2 --------------------------#

                if error == 6:
                    messagebox.showerror(
                        "Error",
                        "Numerador FT2 inválido\nEl formato deben ser valores numéricos",
                    )

                if error == 7:
                    messagebox.showerror(
                        "Error",
                        "Denominador FT2 inválido\nEl formato deben ser valores numéricos",
                    )

                if error == 8 and orden2 == 1:
                    messagebox.showerror(
                        "Error", "Numerador FT2 inválido\nEl formato debe ser: [b1, b0]"
                    )
                if error == 8 and orden2 == 2:
                    messagebox.showerror(
                        "Error",
                        "Numerador FT2 inválido\nEl formato debe ser: [b2, b1, b0]",
                    )
                if error == 9 and orden2 == 1:
                    messagebox.showerror(
                        "Error", "Denominador FT2 inválido\nEl formato debe ser: [a0]"
                    )
                if error == 9 and orden2 == 2:
                    messagebox.showerror(
                        "Error",
                        "Denominador FT2 inválido\nEl formato debe ser: [a1, a0]",
                    )
                if error == 10 and orden2 == 1:
                    messagebox.showerror(
                        "Error", "El grado del numerador FT2 debe ser igual a 1"
                    )
                if error == 10 and orden2 == 2:
                    messagebox.showerror(
                        "Error", "El grado del numerador FT2 debe ser igual a 2"
                    )
                if error == 11 and orden2 == 1:
                    messagebox.showerror(
                        "Error", "El grado del denominador FT2 debe ser igual a 1"
                    )
                if error == 11 and orden2 == 2:
                    messagebox.showerror(
                        "Error", "El grado del denominador FT2 debe ser igual a 2"
                    )

                self.windowPFT.lift()
        else:
            self.ventanaCerrada = True
            self.windowPFT.destroy()

    def cambiarDiagramaEcua(self, value):

        orden = int(self.orden.get())

        if orden == 1:
            self.imagen_funcion = PhotoImage(file="Ecuacion_PFT.png")
        else:
            self.imagen_funcion = PhotoImage(file="Ecuacion_PFT.png")

        self.imagen_funcion_label.configure(image=self.imagen_funcion)
        self.imagen_funcion_label.image = self.imagen_funcion

    def cambiarDiagrama(self, value=None):

        n = int(self.n.get())
        m = int(self.m.get())

        if n == 2 or m == 2:
            if n == 1 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_1x1.png")

            if n == 1 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_1x2.png")

            if n == 2 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_2x1.png")

            if n == 2 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_2x2.png")

            self.entry_n2.config(state="normal")
            self.out_n2.config(state="normal")
            self.o2.config(state="normal")

            self.imagen_bloque_label.configure(image=self.imagen_bloque)
            self.imagen_bloque_label.image = self.imagen_bloque
        if n == 1 and m == 1:
            if n == 1 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_1x1.png")

            if n == 1 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_1x2.png")

            if n == 2 and m == 1:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_2x1.png")

            if n == 2 and m == 2:

                self.imagen_bloque = PhotoImage(file="Diagrama_PFT_2x2.png")

            self.entry_n2.config(state="disabled")
            self.out_n2.config(state="disabled")
            self.o2.config(state="disabled")

            self.imagen_bloque_label.configure(image=self.imagen_bloque)
            self.imagen_bloque_label.image = self.imagen_bloque

    """
    def cambiarIcono(self):

        if self.rt.get() == 1:
            self.imagen_bloque = PhotoImage(file="PFT_r.png")
        else:
            self.imagen_bloque = PhotoImage(file="Diagrama_PFT_1x1.png")

        self.imagen_bloque_label.configure(image=self.imagen_bloque)
        self.imagen_bloque_label.image = self.imagen_bloque
    """

    def arrastrarPFT(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoPFT(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarPFT()

        else:

            if self.ventanaCerrada is True:
                # -------------------------- 1 Salida --------------------------
                if self.tipoPFT == "PFT_1x1" or self.tipoPFT == "PFT_2x1":

                    if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida_1 RE

                        if (
                            self.creandoLinea is not None
                            and self.salida_1 is None
                            and not self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx + 32, self.posiciony - 1)
                            self.salida_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.salida_1 is None:
                            coord = [self.posicionx + 32, self.posiciony - 1]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, True
                            )  # Nueva Conexion
                            self.salida_1 = self.creandoLinea

                # -------------------------- 2 Salidas --------------------------
                if self.tipoPFT == "PFT_1x2" or self.tipoPFT == "PFT_2x2":

                    if 38 > self.dx > 28 and -19 < self.dy < -7:  # Salida_1 RE

                        if (
                            self.creandoLinea is not None
                            and self.salida_1 is None
                            and not self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx + 32, self.posiciony - 17)
                            self.salida_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.salida_1 is None:
                            coord = [self.posicionx + 32, self.posiciony - 17]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, True
                            )  # Nueva Conexion
                            self.salida_1 = self.creandoLinea

                    if 38 > self.dx > 28 and 19 > self.dy > 7:  # Salida_2 RE

                        if (
                            self.creandoLinea is not None
                            and self.salida_2 is None
                            and not self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx + 32, self.posiciony + 16)
                            self.salida_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.salida_2 is None:
                            coord = [self.posicionx + 32, self.posiciony + 16]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, True
                            )  # Nueva Conexion
                            self.salida_2 = self.creandoLinea

                # -------------------------- 1 Entrada --------------------------
                if self.tipoPFT == "PFT_1x1" or self.tipoPFT == "PFT_1x2":

                    if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada_1 RE

                        if (
                            self.creandoLinea is not None
                            and self.entrada_1 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony - 14)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 14]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and -6 < self.dy < 6:  # Entrada_2 RE

                        if (
                            self.creandoLinea is not None
                            and self.entrada_2 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony - 1)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony - 1]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )
                            self.entrada_2 = self.creandoLinea

                # -------------------------- 2 Entradas --------------------------
                if self.tipoPFT == "PFT_2x1" or self.tipoPFT == "PFT_2x2":

                    if -38 < self.dx < -28 and -25 < self.dy < -14:  # Entrada_1 PFT

                        if (
                            self.creandoLinea is not None
                            and self.entrada_1 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony - 18)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 18]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and 14 < self.dy < 25:  # Entrada_2 PFT

                        if (
                            self.creandoLinea is not None
                            and self.entrada_2 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony + 16)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony + 16]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )
                            self.entrada_2 = self.creandoLinea

                """
                # ----------------- SALIDA -----------------

                if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida PFT

                    if (
                        self.creandoLinea is not None
                        and self.salida is None
                        and not self.tipoCreandoLinea
                    ):
                        tupla = (self.posicionx + 32, self.posiciony - 1)
                        self.salida = self.creandoLinea
                        self.tupla_listas[2].ultimoNodo(
                            self.creandoLinea, self.nombre, tupla
                        )

                    if self.creandoLinea is None and self.salida is None:
                        coord = [self.posicionx + 32, self.posiciony - 1]
                        self.tupla_listas[2].agregar(
                            self.tupla_listas, self.nombre, coord, True
                        )  # Nueva Conexion
                        self.salida = self.creandoLinea

                # -------------------------- 1 Entrada --------------------------
                if self.tipoPFT == "PFT_1x1":

                    if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada PFT

                        if (
                            self.creandoLinea is not None
                            and self.entrada_1 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony - 1)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 1]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                # -------------------------- 2 Entradas --------------------------
                if self.tipoPFT == "PFT_2x1":

                    if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada_1 PFT

                        if (
                            self.creandoLinea is not None
                            and self.entrada_1 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony - 14)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 14]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and 19 > self.dy > 7:  # Entrada_2 PFT

                        if (
                            self.creandoLinea is not None
                            and self.entrada_2 is None
                            and self.tipoCreandoLinea
                        ):
                            tupla = (self.posicionx - 32, self.posiciony + 12)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(
                                self.creandoLinea, self.nombre, tupla
                            )

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony + 12]
                            self.tupla_listas[2].agregar(
                                self.tupla_listas, self.nombre, coord, False
                            )  # Nueva Conexion
                            self.entrada_2 = self.creandoLinea
                """

    def clickDerechoPFT(self, event):

        self.eliminarPFT()

    def eliminarPFT(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelEntrada2)
            self.window.delete(self.labelSalida1)
            self.window.delete(self.labelSalida2)
            self.window.unbind(self.nombre)

            if self.entrada_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_1)
            if self.entrada_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_2)
            if self.salida_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.salida_1)
            if self.salida_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.salida_2)

            self.tupla_listas[21].remover(self.nombre)

    def enMovimientoPFT(self, event):

        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        self.window.delete(self.labelSalida1)
        self.window.delete(self.labelSalida2)
        self.window.delete(self.labelEntrada1)
        self.window.delete(self.labelEntrada2)

        if (
            tamano_ventana_x > event.x > 20
            and tamano_ventana_y > event.y > 20
            and self.creandoLinea is None
        ):
            self.window.move(
                self.nombre,
                event.x - self.posicionx - self.dx,
                event.y - self.posiciony - self.dy,
            )
            self.window.move(
                self.labelNombre,
                event.x - self.posicionx - self.dx,
                event.y - self.posiciony - self.dy,
            )

            # Movimiento de la Conexion
            # ----------------------------------
            if (
                self.entrada_1 is not None
                and self.entrada_1 != self.salida_1
                and self.entrada_1 != self.salida_2
            ):
                self.tupla_listas[2].moverLinea(
                    self.entrada_1,
                    self.nombre,
                    event.x - self.posicionx - self.dx,
                    event.y - self.posiciony - self.dy,
                )

            if (
                self.entrada_2 is not None
                and self.entrada_2 != self.salida_1
                and self.entrada_2 != self.salida_2
            ):
                self.tupla_listas[2].moverLinea(
                    self.entrada_2,
                    self.nombre,
                    event.x - self.posicionx - self.dx,
                    event.y - self.posiciony - self.dy,
                )

            if self.salida_1 is not None:
                self.tupla_listas[2].moverLinea(
                    self.salida_1,
                    self.nombre,
                    event.x - self.posicionx - self.dx,
                    event.y - self.posiciony - self.dy,
                )

            if self.salida_2 is not None:
                self.tupla_listas[2].moverLinea(
                    self.salida_2,
                    self.nombre,
                    event.x - self.posicionx - self.dx,
                    event.y - self.posiciony - self.dy,
                )
            # ----------------------------------
            self.posicionx = event.x - self.dx
            self.posiciony = event.y - self.dy

    def sobreIcono(self, event):

        x_icono = event.x - self.posicionx
        y_icono = event.y - self.posiciony

        # -------------------------- 1 Salida --------------------------
        if self.tipoPFT == "PFT_1x1" or self.tipoPFT == "PFT_2x1":

            if 38 > x_icono > 28 and 6 > abs(y_icono):  # Salida_1 RE
                if not self.estado_labelSalida1:
                    self.window.create_text(
                        self.posicionx + 35,
                        self.posiciony + 20,
                        text="Salida 1",
                        font=("Arial Rounded MT", -10),
                        tags=self.labelSalida1,
                    )
                    self.estado_labelSalida1 = True
            else:
                self.window.delete(self.labelSalida1)
                self.estado_labelSalida1 = False

        # -------------------------- 2 Salidas --------------------------
        if self.tipoPFT == "PFT_1x2" or self.tipoPFT == "PFT_2x2":

            if 38 > x_icono > 28 and -19 < y_icono < -7:  # Salida_1 RE
                if not self.estado_labelSalida1:
                    self.window.create_text(
                        self.posicionx + 35,
                        self.posiciony + 7,
                        text="Salida 1",
                        font=("Arial Rounded MT", -10),
                        tags=self.labelSalida1,
                    )
                    self.estado_labelSalida1 = True

            elif 38 > x_icono > 28 and 19 > y_icono > 7:  # Salida_2 RE
                if not self.estado_labelSalida2:
                    self.window.create_text(
                        self.posicionx + 35,
                        self.posiciony + 33,
                        text="Salida 2",
                        font=("Arial Rounded MT", -10),
                        tags=self.labelSalida2,
                    )
                    self.estado_labelSalida2 = True

            else:
                self.window.delete(self.labelSalida1)
                self.window.delete(self.labelSalida2)
                self.estado_labelSalida1 = False
                self.estado_labelSalida2 = False

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

        self.estado_labelSalida1 = False
        self.estado_labelSalida2 = False
        self.estado_labelEntrada1 = False
        self.estado_labelEntrada2 = False

    # --------------------------------------------
    def senal_nombres(self, lista_nombres):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada_1 is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
            sim_entrada1.senal_nombres(lista_nombres)

        if self.tipoPFT == "PFT_2x1":

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                sim_entrada2.senal_nombres(lista_nombres)

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

        num = self.variable_numerador
        den = self.variable_denominador

        # Orden 1
        # num = [b1, b0]
        # den = [a0]

        # Orden 2
        # num = [b2, b1, b0]
        # den = [a1, a0]

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.tipoPFT == "PFT_1x1":

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = float(sim_entrada1.senal_simulacion(n, ts, self.entrada_1))
            else:
                ent1 = 0.0

            self.x_n = ent1

        else:

            if self.entrada_1 is not None:
                sim_entrada1 = a.obtenerBloqueConexion(self.entrada_1, self.nombre)
                ent1 = float(sim_entrada1.senal_simulacion(n, ts, self.entrada_1))

            else:
                ent1 = 0.0

            if self.entrada_2 is not None:
                sim_entrada2 = a.obtenerBloqueConexion(self.entrada_2, self.nombre)
                ent2 = float(sim_entrada2.senal_simulacion(n, ts, self.entrada_2))

            else:
                ent2 = 0.0

            self.x_n = ent1 - ent2

        # Grado 1
        # y(n) = -a0 * y(n - 1) + b1 * x(n) + b0 * x(n - 1)
        if self.variable_orden == 1:
            self.y_n = (
                -float(den[0]) * self.y_n_1
                + float(num[0]) * self.x_n
                + float(num[1]) * self.x_n_1
            )

            self.y_n_1 = self.y_n
            self.x_n_1 = self.x_n

        else:

            # Grado 2
            # y(n) = -a1 * y(n - 1) - a0 * y(n - 2) + b2 * x(n) + b1 * x(n - 1) + b0 * x(n - 2)

            self.y_n = (
                -float(den[0]) * self.y_n_1
                - float(den[1]) * self.y_n_2
                + float(num[0]) * self.x_n
                + float(num[1]) * self.x_n_1
                + float(num[2]) * self.x_n_2
            )

            if self.y_n > 1e20:
                self.y_n = 1e20

            if self.y_n < -1e20:
                self.y_n = -1e20

            self.y_n_2 = self.y_n_1
            self.y_n_1 = self.y_n

            self.x_n_2 = self.x_n_1
            self.x_n_1 = self.x_n

        return float(self.y_n)


class ListaPFT:

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

        temp = NodoPFT(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickPFT)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarPFT)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoPFT)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoPFT)
        temp.window.tag_bind(
            temp.nombre, "<Button-2>", temp.clickDerechoPFT
        )  # 3 Windows/Unix
        temp.window.tag_bind(temp.nombre, "<Motion>", temp.sobreIcono)
        temp.window.tag_bind(temp.nombre, "<Enter>", temp.dentroDelIcono)
        temp.window.tag_bind(temp.nombre, "<Leave>", temp.afueraDelIcono)
    
    def inspeccionar_nodo_PFT(self):
        if self.cabeza is not None:
            print(self.cabeza.__dict__)
        else:
            print("La lista está vacía")
    
    def imprimir_lista_PFT(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Elemento {actual.item}: x = {actual.x}, y = {actual.y}, tupla = {actual.tupla_listas}")
            actual = actual.siguiente

    def abrirArchivo(self, tupla_listas, nombre, x, y):

        n = 0
        for i in nombre:
            if i == "_":
                n = n + 1
                break
            n = n + 1

        item = int(nombre[n:])

        temp = NodoPFT(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickPFT)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarPFT)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoPFT)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoPFT)
        temp.window.tag_bind(
            temp.nombre, "<Button-2>", temp.clickDerechoPFT
        )  # 3 Windows/Unix
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

        while actual != None and not encontrado:
            if actual.nombre == nombre:
                coordenadas = (actual.posicionx, actual.posiciony)
                encontrado = True
                return coordenadas
            else:
                actual = actual.siguiente
        return None
