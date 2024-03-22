from tkinter import *
from tkinter import messagebox
import numpy as np
import Simulacion
from tkinter import ttk

class NodoFT:
    def __init__(self, id_FT, tupla_listas, px, py):

        self.dato = id_FT
        self.tipo = "FT"

        self.nombre = "FT_"+str(id_FT)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "F"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada_1 = None
        self.entrada_2 = None
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="FT.png")

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
        self.tipoFT = "FT_1x1"
        self.variable_orden = 2
        self.variable_numerador = [1, 2, 3]
        self.variable_denominador = [1, 2]

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

    def dobleClickFT(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowFT = Toplevel(self.mainWindow)
            self.windowFT.resizable(False, False)
            self.windowFT.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowFT, bg="#2C2C2C")
            self.frame2 = Frame(self.windowFT, bg="white")
            self.frame3 = Frame(self.windowFT, bg="white")

            self.imagen_ventana = PhotoImage(file="FTv.png")
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

            Label(self.frame2, text="Función de transferencia", font=("Arial Rounded MT Bold", -18)) \
                .grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)

            self.imagen_bloque = PhotoImage(file="FT.png")
            self.imagen_bloque_label = Label(self.frame2,
                                              image=self.imagen_bloque,
                                              borderwidth=0,
                                              highlightthickness=0,
                                              padx=0,
                                              pady=0)
            self.imagen_bloque_label.image = self.imagen_bloque
            self.imagen_bloque_label.grid(row=1, column=0, columnspan=1, pady=(0, 10), padx=(20, 0))

            self.imagen_funcion = PhotoImage(file="Ecuacion_Funcion_Transferencia_O1.png")
            self.imagen_funcion_label = Label(self.frame2,
                                               image=self.imagen_funcion,
                                               borderwidth=0,
                                               highlightthickness=0,
                                               padx=0,
                                               pady=0)
            self.imagen_funcion_label.image = self.imagen_funcion
            self.imagen_funcion_label.grid(row=1, column=1, columnspan=1, pady=(0,10))

            self.orden = StringVar()
            if self.orden is None:
                self.orden.set("1")
            else:
                self.orden.set(str(self.variable_orden))

            self.cambiarDiagrama(None)

            opciones_orden = ['1', '2']

            Label(self.frame2, text="Orden:").grid(row=2, column=0, sticky=W, padx=(20, 0))
            ttk.OptionMenu(self.frame2, self.orden, None, *opciones_orden, command=self.cambiarDiagrama) \
                .grid(row=2, column=1, sticky=W, pady=(0, 0))

            self.numerador = StringVar()

            if self.variable_numerador is None:
                self.numerador.set("[b3, b2, b1, b0]")
            else:
                num = "["
                for i in range(0,len(self.variable_numerador)):

                    if i == len(self.variable_numerador)-1:
                        num = num + str(self.variable_numerador[i]) + "]"
                    else:
                        num = num + str(self.variable_numerador[i]) + ", "

                self.numerador.set(num)


            Label(self.frame2, text="Numerador:").grid(row=3, column=0, sticky=W, padx=(20, 0))
            ttk.Entry(self.frame2, width=25, textvariable=self.numerador).grid(row=3, column=1, sticky=W,
                                                                                 padx=(0, 20))

            self.denominador = StringVar()

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

            Label(self.frame2, text="Denominador:").grid(row=4, column=0, sticky=W, padx=(20, 0), pady=(0, 0))
            ttk.Entry(self.frame2, width=25, textvariable=self.denominador) \
                .grid(row=4, column=1, sticky=W, padx=(0, 20), pady=(0, 0))

            self.rt = IntVar()
            if self.tipoFT == "FT_1x1":
                self.rt.set(0)
            else:
                self.rt.set(1)

            self.cambiarIcono()

            ttk.Checkbutton(self.frame2, text="Retroalimentacion", variable=self.rt, command=self.cambiarIcono)\
                .grid(row=5, column=1, sticky=E, padx=(0, 20), pady=(0, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", command=lambda: self.cerrarVentanaFT("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", command=lambda: self.cerrarVentanaFT("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowFT.protocol("WM_DELETE_WINDOW", self.cerrarVentanaFT)

            self.windowFT.withdraw()
            self.windowFT.update_idletasks()
            x = (self.windowFT.winfo_screenwidth() - self.windowFT.winfo_reqwidth()) / 2
            y = (self.windowFT.winfo_screenheight() - self.windowFT.winfo_reqheight()) / 2
            self.windowFT.geometry("+%d+%d" % (x, y))

            self.windowFT.deiconify()

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

            self.windowFT.lift()

    def cerrarVentanaFT(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            error = 1
            orden = int(self.orden.get())

            try:

                valor_num = eval(self.numerador.get())

                if type(valor_num) is not list:
                    raise Exception

                if len(valor_num) == 0 and orden == 1:
                    valor_num = [0, 0]

                if len(valor_num) == 0 and orden == 2:
                    valor_num = [0, 0, 0]

                for i in valor_num:

                    if type(i) is not int and type(i) is not float:
                        raise Exception

                error = 2
                valor_den = eval(self.denominador.get())

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

                error = 3

                if orden == 1: numerador = [0, 0]
                else: numerador = [0, 0, 0]

                for i in range(0, len(valor_num)):
                    numerador[-(i + 1)] = valor_num[-(i + 1)]

                valor_num = numerador

                error = 4
                if orden == 1: denominador = [0]
                else: denominador = [0, 0]

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

                if self.rt.get() == 1:

                    self.imagen = PhotoImage(file="FT_r.png")
                    self.window.itemconfig(self.nombre, image=self.imagen)

                else:
                    self.imagen = PhotoImage(file="FT.png")
                    self.window.itemconfig(self.nombre, image=self.imagen)

                if self.rt.get() == 1 and self.tipoFT != "FT_2x1":

                    self.tipoFT = "FT_2x1"
                    if self.entrada_1 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_1)
                    if self.entrada_2 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_2)

                if self.rt.get() == 0 and self.tipoFT != "FT_1x1":

                    self.tipoFT = "FT_1x1"
                    if self.entrada_1 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_1)
                    if self.entrada_2 is not None:
                        self.tupla_listas[2].eliminarConexion(self.entrada_2)

                self.variable_orden = int(self.orden.get())

                self.variable_numerador = valor_num
                self.variable_denominador = valor_den

                self.ventanaCerrada = True
                self.windowFT.destroy()

            except Exception:

                if error == 1 and orden == 1:
                    messagebox.showerror("Error", "Numerador inválido\nEl formato debe ser: [b1, b0]")
                if error == 1 and orden == 2:
                    messagebox.showerror("Error", "Numerador inválido\nEl formato debe ser: [b2, b1, b0]")
                if error == 2 and orden == 1:
                    messagebox.showerror("Error", "Denominador inválido\nEl formato debe ser: [a0]")
                if error == 2 and orden == 2:
                    messagebox.showerror("Error", "Denominador inválido\nEl formato debe ser: [a1, a0]")
                if error == 3 and orden == 1:
                    messagebox.showerror("Error", "El grado del numerador debe ser igual a 1")
                if error == 3 and orden == 2:
                    messagebox.showerror("Error", "El grado del numerador debe ser igual a 2")
                if error == 4 and orden == 1:
                    messagebox.showerror("Error", "El grado del denominador debe ser igual a 1")
                if error == 4 and orden == 2:
                    messagebox.showerror("Error", "El grado del denominador debe ser igual a 2")

                self.windowFT.lift()
        else:
            self.ventanaCerrada = True
            self.windowFT.destroy()

    def cambiarDiagrama(self, value):

        orden = int(self.orden.get())

        if orden == 1:
            self.imagen_funcion = PhotoImage(file="Ecuacion_Funcion_Transferencia_O1.png")
        else:
            self.imagen_funcion = PhotoImage(file="Ecuacion_Funcion_Transferencia_O2.png")

        self.imagen_funcion_label.configure(image=self.imagen_funcion)
        self.imagen_funcion_label.image = self.imagen_funcion

    def cambiarIcono(self):

        if self.rt.get() == 1:
            self.imagen_bloque = PhotoImage(file="FT_r.png")
        else:
            self.imagen_bloque = PhotoImage(file="FT.png")

        self.imagen_bloque_label.configure(image=self.imagen_bloque)
        self.imagen_bloque_label.image = self.imagen_bloque

    def arrastrarFT(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoFT(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarFT()

        else:

            if self.ventanaCerrada is True:

                # ----------------- SALIDA -----------------

                if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida FT

                    if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                        tupla = (self.posicionx + 32, self.posiciony-1)
                        self.salida = self.creandoLinea
                        self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                    if self.creandoLinea is None and self.salida is None:
                        coord = [self.posicionx + 32, self.posiciony-1]
                        self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                        self.salida = self.creandoLinea

                # -------------------------- 1 Entrada --------------------------
                if self.tipoFT == "FT_1x1":

                    if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada FT

                        if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx-32, self.posiciony-1)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony-1]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                # -------------------------- 2 Entradas --------------------------
                if self.tipoFT == "FT_2x1":

                    if -38 < self.dx < -28 and -19 < self.dy < -7:  # Entrada_1 FT

                        if self.creandoLinea is not None and self.entrada_1 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony - 14)
                            self.entrada_1 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_1 is None:
                            coord = [self.posicionx - 32, self.posiciony - 14]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                            self.entrada_1 = self.creandoLinea

                    if -38 < self.dx < -28 and 19 > self.dy > 7:  # Entrada_2 FT

                        if self.creandoLinea is not None and self.entrada_2 is None and self.tipoCreandoLinea:
                            tupla = (self.posicionx - 32, self.posiciony + 12)
                            self.entrada_2 = self.creandoLinea
                            self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                        if self.creandoLinea is None and self.entrada_2 is None:
                            coord = [self.posicionx - 32, self.posiciony + 12]
                            self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                            self.entrada_2 = self.creandoLinea


    def clickDerechoFT(self, event):

        self.eliminarFT()

    def eliminarFT(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelSalida1)
            self.window.unbind(self.nombre)

            if self.entrada_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_1)
            if self.entrada_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada_2)
            if self.salida is not None:
                self.tupla_listas[2].eliminarConexion(self.salida)

            self.tupla_listas[8].remover(self.nombre)

    def enMovimientoFT(self, event):

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

        if self.tipoFT == "FT_1x1":
            if -38 < x_icono < -28 and 6 > abs(y_icono):

                if not self.estado_labelEntrada1:
                    self.window.create_text(self.posicionx-38,
                                            self.posiciony+20,
                                            text="Entrada 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada1)
                    self.estado_labelEntrada1 = True
            else:
                self.window.delete(self.labelEntrada1)
                self.estado_labelEntrada1 = False

        # -------------------------- 2 Entradas --------------------------
        if self.tipoFT == "FT_2x1":

            if -38 < x_icono < -28 and -19 < y_icono < -7:  # Entrada_1 RE
                if not self.estado_labelEntrada1:
                    self.window.create_text(self.posicionx - 35,
                                            self.posiciony + 7,
                                            text="Entrada 1",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada1)
                    self.estado_labelEntrada1 = True

            elif -38 < x_icono < -28 and 19 > y_icono > 7:  # Entrada_2 RE
                if not self.estado_labelEntrada2:
                    self.window.create_text(self.posicionx - 35,
                                            self.posiciony + 33,
                                            text="Entrada 2",
                                            font=("Arial Rounded MT", -10),
                                            tags=self.labelEntrada2)
                    self.estado_labelEntrada2 = True
            else:
                self.window.delete(self.labelEntrada1, self.labelEntrada2)
                self.estado_labelEntrada1 = False
                self.estado_labelEntrada2 = False

        # -------------------------- Salida --------------------------
        if 38 > x_icono > 28 and 6 > y_icono:

            if not self.estado_labelSalida1:
                self.window.create_text(self.posicionx+38,
                                        self.posiciony+20,
                                        text="Salida 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelSalida1)
                self.estado_labelSalida1 = True
        else:
            self.window.delete(self.labelSalida1)
            self.estado_labelSalida1 = False

    def dentroDelIcono(self, event):
        # self.window.create_text(self.posicionx,
        #                         self.posiciony-51,
        #                         text=self.nombre,
        #                         font=("Arial Rounded MT", -12, "bold"),
        #                         tags=self.label_con_nombre)
        pass

    def afueraDelIcono(self, event):
        self.window.delete(self.labelSalida1)
        self.window.delete(self.labelEntrada1, self.labelEntrada2)

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

        if self.tipoFT == "FT_2x1":

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

        if self.tipoFT == "FT_1x1":

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
            self.y_n = -float(den[0]) * self.y_n_1 + float(num[0]) * self.x_n + float(num[1]) * self.x_n_1

            self.y_n_1 = self.y_n
            self.x_n_1 = self.x_n

        else:

            # Grado 2
            # y(n) = -a1 * y(n - 1) - a0 * y(n - 2) + b2 * x(n) + b1 * x(n - 1) + b0 * x(n - 2)

            self.y_n = -float(den[0]) * self.y_n_1 - float(den[1]) * self.y_n_2 + float(num[0]) * self.x_n + float(
                num[1]) * self.x_n_1 + float(num[2]) * self.x_n_2

            if self.y_n > 1e20:
                self.y_n = 1e20

            if self.y_n < -1e20:
                self.y_n = -1e20

            self.y_n_2 = self.y_n_1
            self.y_n_1 = self.y_n

            self.x_n_2 = self.x_n_1
            self.x_n_1 = self.x_n

        return float(self.y_n)


class ListaFT:

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

        temp = NodoFT(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickFT)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarFT)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoFT)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoFT)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoFT) # 3 Windows/Unix
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

        temp = NodoFT(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickFT)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarFT)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoFT)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoFT)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoFT)  # 3 Windows/Unix
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
