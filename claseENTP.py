from tkinter import *
from tkinter import messagebox
import Simulacion
import numpy as np
from tkinter import ttk


class NodoENTP:
    def __init__(self, id_ENTP, tupla_listas, px, py):

        self.dato = id_ENTP
        self.tipo = "ENTP"
        self.nombre = "ENTP_"+str(id_ENTP)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "N"

        self.dx = None
        self.dy = None

        # Entrada
        self.entrada = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="ENTP.png")

        self.icono = self.window.create_image(px, py, image=self.imagen, tags=self.nombre)
        self.label_con_nombre = self.nombre + "l"  # tag etiqueta con nombre

        self.labelNombre = self.window.create_text(self.posicionx+6,
                                                   self.posiciony-32,
                                                   text="PLANTA",
                                                   font=("Arial Rounded MT", -12, "bold"),
                                                   tags=self.label_con_nombre)

        # - - - - - -

        self.estado_labelEntrada1 = False
        self.labelEntrada1 = self.nombre + "e1"

        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

        # Variables ------------------------
        self.variable_nombre_bloque = "PLANTA"

        # Simulacion -----------------------
        self.tipoPlanta = "BallAndBeam"

        self.y_n = 0
        self.y_n_1 = 0
        self.y_n_2 = 0
        self.x_n = 0
        self.x_n_1 = 0
        self.x_n_2 = 0

        self.matriz_x_n = 0
        self.matriz_x_n_1 = 0
        self.ex1_n = 0
        self.ex1_n_1 = 0
        self.ex2_n = 0
        self.ex2_n_1 = 0

    def dobleClickENTP(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowENTP = Toplevel(self.mainWindow)
            self.windowENTP.resizable(False, False)
            self.windowENTP.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowENTP, bg="#2C2C2C")
            self.frame2 = Frame(self.windowENTP, bg="white")
            self.frame3 = Frame(self.windowENTP, bg="white")


            self.imagen_ventana = PhotoImage(file="ENTP.png")
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

            Label(self.frame2, text="Nombre:").grid(row=1, column=0, sticky=W, padx=(20,0), pady=(20,20))
            ttk.Entry(self.frame2, width=22, textvariable=self.c).grid(row=1, column=1, sticky=W, padx=(0,20), pady=(20, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", width=8, command=lambda: self.cerrarVentanaENTP("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", width=8, command=lambda: self.cerrarVentanaENTP("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowENTP.protocol("WM_DELETE_WINDOW", self.cerrarVentanaENTP)

            self.windowENTP.withdraw()
            self.windowENTP.update_idletasks()
            x = (self.windowENTP.winfo_screenwidth() - self.windowENTP.winfo_reqwidth()) / 2
            y = (self.windowENTP.winfo_screenheight() - self.windowENTP.winfo_reqheight()) / 2
            self.windowENTP.geometry("+%d+%d" % (x, y))

            self.windowENTP.deiconify()

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
            self.windowENTP.lift()

    def cerrarVentanaENTP(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            try:

                error = 1
                nombre = self.c.get()

                for i in nombre:
                    if i == "/":
                        error = 2
                        raise Exception

                if len(nombre) > 25:
                    error = 3
                    raise Exception

                self.tupla_listas[1].delete(self.label_con_nombre)

                self.labelNombre = self.window.create_text(self.posicionx + 6,
                                                           self.posiciony - 32,
                                                           text=nombre,
                                                           font=("Arial Rounded MT", -12, "bold"),
                                                           tags=self.label_con_nombre)

                self.variable_nombre_bloque = nombre

                self.ventanaCerrada = True
                self.windowENTP.destroy()

            except Exception:

                if error == 1:
                    messagebox.showerror("Error", "Nombre inválido")
                if error == 2:
                    messagebox.showerror("Error", "Nombre inválido. El nombre no puede contener el carácter \"/\"")
                if error == 3:
                    messagebox.showerror("Error", "Nombre inválido. El nombre debe contener como máximo 25 caracteres")

                self.windowENTP.lift()

        else:
            self.ventanaCerrada = True
            self.windowENTP.destroy()

    def arrastrarENTP(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoENTP(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarENTP()

        else:

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada ENTP

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 30, self.posiciony)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 30, self.posiciony]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

    def clickDerechoENTP(self, event):

        self.eliminarENTP()

    def eliminarENTP(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.unbind(self.nombre)

            if self.entrada is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada)

            self.tupla_listas[11].remover(self.nombre)

    def enMovimientoENTP(self, event):

        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------
            if self.entrada is not None:
                self.tupla_listas[2].moverLinea(self.entrada, self.nombre,
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
                self.window.create_text(self.posicionx-33,
                                        self.posiciony+20,
                                        text="Entrada 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelEntrada1)
                self.estado_labelEntrada1 = True

        else:
            self.window.delete(self.labelEntrada1)
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
        self.window.delete(self.labelEntrada1)
        self.estado_labelEntrada1 = False

# --------------------------------------------
    def senal_nombres(self, lista_nombres):

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada, self.nombre)
            sim_entrada1.senal_nombres(lista_nombres).append(self.nombre)

        return lista_nombres

    def senal_simulacion(self, n, ts, conexion):

        if n == 0:
            self.y_n = 0
            self.y_n_1 = 0
            self.y_n_2 = 0
            self.x_n = 0
            self.x_n_1 = 0
            self.x_n_2 = 0

            self.ex1_n = 0
            self.ex1_n_1 = 0
            self.ex2_n = 0
            self.ex2_n_1 = 0

            self.matriz_x = 0

        a = Simulacion.Simulacion()
        a.listas(self.tupla_listas)

        if self.entrada is not None:
            sim_entrada1 = a.obtenerBloqueConexion(self.entrada, self.nombre)
            ent1 = sim_entrada1.senal_simulacion(n, ts, self.entrada)
        else:
            ent1 = 0

        self.x_n = ent1

        # y(n) = 2*y(n-1) - y*(n-2) + 0.00000525*x(n) + 0.0000105*x(n-1) + 0.00000525*x(n-2)  Ts=0.01
        self.y_n = 2 * self.y_n_1 - self.y_n_2 + 0.00000525 * self.x_n + 0.0000105 * self.x_n_1 + 0.00000525 * self.x_n_2

        if self.variable_nombre_bloque == "Ball&Beam_20":

            self.y_n = 2 * self.y_n_1 - self.y_n_2 + 0.000021 * self.x_n + 0.000042 * self.x_n_1 + 0.000021 * self.x_n_2

        self.x_n_2 = self.x_n_1
        self.x_n_1 = self.x_n

        self.y_n_2 = self.y_n_1
        self.y_n_1 = self.y_n

        # ------------------------------------------------------
        self.matriz_x_n = np.matrix([[self.ex1_n], [self.ex2_n]])

        # Ts = 0.01
        ad = np.matrix([[1, 0.01], [0, 1]])
        bd = np.matrix([[1.05e-05 * ent1], [0.0021 * ent1]])
        cd = np.matrix([[1, 0]])

        if self.variable_nombre_bloque == "Ball&Beam_20":
            # Ts = 0.02
            ad = np.matrix([[1, 0.02], [0, 1]])
            bd = np.matrix([[4.2e-05 * ent1], [0.0042 * ent1]])
            cd = np.matrix([[1, 0]])

        self.matriz_x_n_1 = ad.dot(self.matriz_x_n) + bd

        self.ex1_n = self.matriz_x_n_1.item(0)
        self.ex2_n = self.matriz_x_n_1.item(1)

        self.actualizarSalidaPlanta()

    def actualizarSalidaPlanta(self):

        actual = self.tupla_listas[12].cabeza

        while actual is not None:

            if actual.variable_nombre_bloque == "." + self.variable_nombre_bloque:

                actual.y_n = self.x_n
                actual = actual.siguiente

            elif actual.variable_nombre_bloque == self.variable_nombre_bloque + ".X1":

                actual.y_n = self.ex1_n
                actual = actual.siguiente
            
            elif actual.variable_nombre_bloque == self.variable_nombre_bloque + ".X2":

                actual.y_n = self.ex2_n
                actual = actual.siguiente
                
            else:
                
                actual.y_n = self.y_n
                actual = actual.siguiente

        actual = self.tupla_listas[6].cabeza

        while actual is not None:

            actual.y_n = self.y_n
            actual = actual.siguiente


class ListaENTP:

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

        temp = NodoENTP(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickENTP)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarENTP)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoENTP)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoENTP)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoENTP) # 3 Windows/Unix
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

        temp = NodoENTP(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickENTP)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarENTP)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoENTP)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoENTP)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoENTP)  # 3 Windows/Unix
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
