from tkinter import *
import Simulacion
from tkinter import ttk
from tkinter import messagebox



class NodoDER:
    def __init__(self, id_DER, tupla_listas, px, py):

        self.dato = id_DER
        self.tipo = "DER"
        self.nombre = "DER_"+str(id_DER)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "K"

        self.dx = None
        self.dy = None

        # Entrada y Salidas
        self.entrada = None
        self.salida_1 = None
        self.salida_2 = None

        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="DER.png")

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

        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

        # Simulacion -----------------------
        self.i_n_1 = 0
        self.i_n = 0
        self.e_n_1 = 0

        #Variables
        self.variable_frecuenciaNatural = 60
        self.variable_amortiguamientoRelativo = 0.85

    def dobleClickDER(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowDER = Toplevel(self.mainWindow)
            self.windowDER.resizable(False, False)
            self.windowDER.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowDER, bg="#2C2C2C")
            self.frame2 = Frame(self.windowDER, bg="white")
            self.frame3 = Frame(self.windowDER, bg="white")

            self.imagen_ventana = PhotoImage(file="DERv.png")
            self.imagen_ventana_label = Label(self.frame1,
                                              image=self.imagen_ventana,
                                              borderwidth=0,
                                              highlightthickness=0,
                                              bg="#2C2C2C",
                                              padx=0,
                                              pady=10)

            self.imagen_ventana_label.image = self.imagen_ventana
            self.imagen_ventana_label.pack(side=LEFT, padx=10)

            Label(self.frame1, text=self.nombre, bg="#2C2C2C", fg="White", font=("Arial Rounded MT", -20)).pack(side=LEFT)


            # -------------------- FRAME 2 --------------------

            parametros=Label(self.frame2, text="Parámetros", font=("Arial Rounded MT Bold", -18))
            parametros.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)

            self.frecuenciaNatural=StringVar()
            self.amortiguamientoRelativo=StringVar()

            if self.variable_frecuenciaNatural is None:
                self.frecuenciaNatural.set("60")
            else:
                self.frecuenciaNatural.set(str(self.variable_frecuenciaNatural))

            if self.variable_amortiguamientoRelativo is None:
                self.amortiguamientoRelativo.set("0.85")
            else:
                self.amortiguamientoRelativo.set(str(self.variable_amortiguamientoRelativo))

            wn = Label(self.frame2, text="Frecuencia natural (\u03C9n):")
            wn.grid(row=1, column=0, sticky=W, padx=(20, 0))
            
            entry_wn = ttk.Entry(self.frame2, width=18, textvariable=self.frecuenciaNatural)
            entry_wn.grid(row=1, column=1, sticky=W, padx=(0, 20))

            zeta = Label(self.frame2, text="Amortiguamiento relativo (\u03B6):")
            zeta.grid(row=2, column=0, sticky=W, padx=(20, 0), pady=(0, 20))

            entry_zeta = ttk.Entry(self.frame2, width=18, textvariable=self.amortiguamientoRelativo)
            entry_zeta.grid(row=2, column=1, sticky=W, padx=(0, 20), pady=(0, 20))


            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", width=8, command=lambda: self.cerrarVentanaDER("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", width=8, command=lambda: self.cerrarVentanaDER("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))


            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowDER.protocol("WM_DELETE_WINDOW", self.cerrarVentanaDER)

            self.windowDER.withdraw()
            self.windowDER.update_idletasks()
            x = (self.windowDER.winfo_screenwidth() - self.windowDER.winfo_reqwidth()) / 2
            y = (self.windowDER.winfo_screenheight() - self.windowDER.winfo_reqheight()) / 2
            self.windowDER.geometry("+%d+%d" % (x, y))

            self.windowDER.deiconify()

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
            self.windowDER.lift()

        #pass

    def cerrarVentanaDER(self, opcion="Cancelar"):
        #self.windowDER.destroy()
        #pass
        if opcion == "Aceptar":

            try:
                error = 1
                parametro_wn = eval(self.frecuenciaNatural.get())
                parametro_zeta = eval(self.amortiguamientoRelativo.get())

                if type(parametro_wn) is not int and type(parametro_wn) is not float:
                    raise Exception

                if type(parametro_zeta) is not int and type(parametro_zeta) is not float:
                    raise Exception

                error = 2
                if parametro_wn <= 0:
                    raise Exception

                error = 3
                if parametro_zeta < 0 or parametro_zeta > 1:
                    raise Exception

                self.variable_frecuenciaNatural = parametro_wn
                self.variable_amortiguamientoRelativo = parametro_zeta

                self.ventanaCerrada = True
                self.windowDER.destroy()

            except Exception:

                if error == 1:
                    messagebox.showerror("Error", "Parámetros inválidos")
                if error == 2:
                    messagebox.showerror("Error", "La frecuencia relativa debe ser positiva y mayor a 0")
                if error == 3:
                    messagebox.showerror("Error", "El amortiguamiento relativo debe ser un valor entre 0 y 1")

                self.windowDER.lift()
        else:
            self.ventanaCerrada = True
            self.windowDER.destroy()

    def arrastrarDER(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoDER(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarDER()

        else:

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada_1 DER

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx - 32, self.posiciony - 1)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 32, self.posiciony - 1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

            if 38 > self.dx > 28 and -19 < self.dy < -7:  # Salida_1 DER

                if self.creandoLinea is not None and self.salida_1 is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony - 13)
                    self.salida_1 = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida_1 is None:
                    coord = [self.posicionx + 32, self.posiciony - 13]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida_1 = self.creandoLinea

            if 38 > self.dx > 28 and 19 > self.dy > 7:  # Salida_2 DER

                if self.creandoLinea is not None and self.salida_2 is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony + 13)
                    self.salida_2 = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida_2 is None:
                    coord = [self.posicionx + 32, self.posiciony + 13]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida_2 = self.creandoLinea

    def clickDerechoDER(self, event):

        self.eliminarDER()

    def eliminarDER(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelEntrada1)
            self.window.delete(self.labelSalida1)
            self.window.unbind(self.nombre)

            if self.entrada is not None:
                self.tupla_listas[2].eliminarConexion(self.entrada)
            if self.salida_1 is not None:
                self.tupla_listas[2].eliminarConexion(self.salida_1)
            if self.salida_2 is not None:
                self.tupla_listas[2].eliminarConexion(self.salida_2)

            self.tupla_listas[18].remover(self.nombre)

    def enMovimientoDER(self, event):
        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------
            if self.entrada is not None and self.entrada != self.salida_1 and self.entrada != self.salida_2:
                self.tupla_listas[2].moverLinea(self.entrada, self.nombre,
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

        if 38 > x_icono > 28 and -19 < y_icono < -7:  # Salida_1 DER
            if not self.estado_labelSalida1:
                self.window.create_text(self.posicionx + 35,
                                        self.posiciony + 7,
                                        text="Salida 1",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelSalida1)
                self.estado_labelSalida1 = True

        elif 38 > x_icono > 28 and 19 > y_icono > 7:  # Salida_2 DER
            if not self.estado_labelSalida2:
                self.window.create_text(self.posicionx + 35,
                                        self.posiciony + 33,
                                        text="Salida 2",
                                        font=("Arial Rounded MT", -10),
                                        tags=self.labelSalida2)
                self.estado_labelSalida2 = True

        else:
            self.window.delete(self.labelSalida1)
            self.window.delete(self.labelSalida2)
            self.estado_labelSalida1 = False
            self.estado_labelSalida2 = False


        if -38 < x_icono < -28 and 6 > abs(y_icono):  # Entrada_1 DER
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

    def dentroDelIcono(self, event):
        # self.window.create_text(self.posicionx,
        #                         self.posiciony-51,
        #                         text=self.nombre,
        #                         font=("Arial Rounded MT", -12, "bold"),
        #                         tags=self.label_con_nombre)
        pass

    def afueraDelIcono(self, event):
        #  self.window.delete(self.label_con_nombre)
        self.window.delete(self.labelSalida1, self.labelSalida2, self.labelEntrada1)
        self.estado_labelSalida1 = False
        self.estado_labelEntrada1 = False
        self.estado_labelEntrada2 = False

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
            sim_entrada = a.obtenerBloqueConexion(self.entrada, self.nombre)
            ent1 = sim_entrada.senal_simulacion(n, ts, self.entrada)

        else:
            ent1 = 0

        if conexion == self.salida_1:
            return ent1

        if conexion == self.salida_2:
            return -ent1


class ListaDER:

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

        temp = NodoDER(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickDER)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarDER)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoDER)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoDER)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoDER) # 3 Windows/Unix
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

        temp = NodoDER(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickDER)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarDER)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoDER)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoDER)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoDER)  # 3 Windows/Unix
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
