from tkinter import *
from tkinter import messagebox
import Simulacion
from tkinter import ttk

class NodoPWM:
    def __init__(self, id_PWM, tupla_listas, px, py):

        self.dato = id_PWM
        self.tipo = "PWM"
        self.nombre = "PWM_"+str(id_PWM)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "C"

        self.dx = None
        self.dy = None

        # Entrada y Salida
        self.entrada = None
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="PWM.png")

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
        self.variable_periodo = 500
        self.variable_tipo = 0
        self.variable_amplitud = 1
        self.variable_zona_muerta = 0
        self.variable_limite_superior = 5
        self.variable_limite_inferior = -5

    def dobleClickPWM(self, event):


        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowPWM = Toplevel(self.mainWindow)
            self.windowPWM.resizable(False, False)
            self.windowPWM.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowPWM, bg="#2C2C2C")
            self.frame2 = Frame(self.windowPWM, bg="white")
            self.frame3 = Frame(self.windowPWM, bg="white")

            self.imagen_ventana = PhotoImage(file="PWMv.png")
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

            tipo = Label(self.frame2, text="Tipo", font=("Arial Rounded MT Bold", -18))
            tipo.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)

            self.v = IntVar()
            self.t = IntVar()
            self.a = StringVar()
            self.limite_superior = StringVar()
            self.limite_inferior = StringVar()
            self.zona_muerta = IntVar()

            if self.variable_tipo is None:
                self.v.set(1)
            else:
                self.v.set(self.variable_tipo + 1)

            if self.variable_periodo is None:
                self.t.set(10)
            else:
                self.t.set(str(self.variable_periodo))

            if self.variable_amplitud is None:
                self.a.set(1)
            else:
                self.a.set(str(self.variable_amplitud))

            if self.variable_zona_muerta is None:
                self.zona_muerta.set(0)
            else:
                self.zona_muerta.set(self.variable_zona_muerta)
            
            if self.variable_limite_superior is None:
                self.limite_superior.set(5)
            else:
                self.limite_superior.set(self.variable_limite_superior)

            if self.variable_limite_inferior is None:
                self.limite_inferior.set(-5)
            else:
                self.limite_inferior.set(self.variable_limite_inferior)

            

            ttk.Radiobutton(self.frame2, text="Estándar", variable=self.v, value=1)\
                .grid(row=1, column=0,sticky=W, padx=20)
            ttk.Radiobutton(self.frame2, text="RC", variable=self.v, value=2)\
                .grid(row=2, column=0, sticky=W, padx=20)
            ttk.Radiobutton(self.frame2, text="Oneshot", variable=self.v, value=3) \
                .grid(row=3, column=0, sticky=W, padx=20, pady=(0, 10))

            
            # limites = Label(self.frame2, text="Límites", font=("Arial Rounded MT Bold", -18))
            # limites.grid(row=4, column=0, columnspan=2, sticky=W, padx=10, pady=10)

            dead_zone = ttk.Checkbutton(self.frame2, text="Corrección de zona muerta", variable=self.zona_muerta)
            dead_zone.grid(row=4, column=0, sticky=W)

            Superior = Label(self.frame2, text="Límite superior:")
            Superior.grid(row=5, column=0, sticky=W, padx=(20, 0))
            
            entry_Superior = ttk.Entry(self.frame2, width=10, textvariable=self.limite_superior)
            entry_Superior.grid(row=5, column=1, sticky=W, padx=(0, 20))

            Inferior = Label(self.frame2, text="Límite inferior:")
            Inferior.grid(row=6, column=0, sticky=W, padx=(20, 0), pady=(0, 20))

            entry_Inferior = ttk.Entry(self.frame2, width=10, textvariable=self.limite_inferior)
            entry_Inferior.grid(row=6, column=1, sticky=W, padx=(0, 20), pady=(0, 20))


            Label(self.frame2, text="Periodo (us):").grid(row=7, column=0, sticky=W, padx=10)
            ttk.Entry(self.frame2, width=10, textvariable=self.t).grid(row=7, column=1, sticky=W, padx=(0,20))

            Label(self.frame2, text="Amplitud:").grid(row=8, column=0, sticky=W, padx=10, pady=(0, 10))
            ttk.Entry(self.frame2, width=10, textvariable=self.a).grid(row=8, column=1, sticky=W, pady=(0, 10), padx=(0, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", width=8, command=lambda: self.cerrarVentanaPWM("Aceptar"))\
                .pack(side=RIGHT, padx=(10, 20),pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", width=8, command=lambda: self.cerrarVentanaPWM("Cancelar"))\
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowPWM.protocol("WM_DELETE_WINDOW", self.cerrarVentanaPWM)

            self.windowPWM.withdraw()
            self.windowPWM.update_idletasks()
            x = (self.windowPWM.winfo_screenwidth() - self.windowPWM.winfo_reqwidth()) / 2
            y = (self.windowPWM.winfo_screenheight() - self.windowPWM.winfo_reqheight()) / 2
            self.windowPWM.geometry("+%d+%d" % (x, y))

            self.windowPWM.deiconify()

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
            self.windowPWM.lift()


    def cerrarVentanaPWM(self, opcion="Cancelar"):

        if opcion == "Aceptar":
            error = 1
            try:
                valor = self.t.get()
                if valor < 0:
                    raise Exception

                error = 2

                amplitud = eval(self.a.get())

                if type(amplitud) is not int and type(amplitud) is not float:
                    raise Exception

                error = 3
                zona = self.zona_muerta.get()
                if zona == 0:
                    self.variable_zona_muerta = zona
                    self.variable_limite_superior = 5
                    self.variable_limite_inferior = -5
                else:
                    limite_s = eval(self.limite_superior.get())
                    limite_i = eval(self.limite_inferior.get())

                    if type(limite_s) is not int and type(limite_s) is not float:
                        raise Exception

                    if type(limite_i) is not int and type(limite_i) is not float:
                        raise Exception

                    error = 4
                    if limite_s <= limite_i:
                        raise Exception

                    self.variable_limite_superior = limite_s
                    self.variable_limite_inferior = limite_i

                self.variable_amplitud = amplitud
                self.variable_periodo = self.t.get()
                self.variable_tipo = self.v.get() - 1
                self.variable_zona_muerta = zona
                self.ventanaCerrada = True
                self.windowPWM.destroy()

            except Exception:
                if error == 1:
                    messagebox.showerror("Error", "Periodo inválido")
                if error == 2:
                    messagebox.showerror("Error", "Amplitud inválida")
                if error == 3:
                    messagebox.showerror("Error", "Límite inválido")
                else:
                    messagebox.showerror("Error", "Límite superior debe ser mayor al límite inferior")

                self.windowPWM.lift()
        else:
            self.ventanaCerrada = True
            self.windowPWM.destroy()

    def arrastrarPWM(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoPWM(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarPWM()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida PWM

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

            if -38 < self.dx < -28 and 6 > abs(self.dy):  # Entrada PWM

                if self.creandoLinea is not None and self.entrada is None and self.tipoCreandoLinea:
                    tupla = (self.posicionx-32, self.posiciony-1)
                    self.entrada = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.entrada is None:
                    coord = [self.posicionx - 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, False)  # Nueva Conexion
                    self.entrada = self.creandoLinea

    def clickDerechoPWM(self, event):

        self.eliminarPWM()

    def eliminarPWM(self):

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

            self.tupla_listas[5].remover(self.nombre)

    def enMovimientoPWM(self, event):

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
            return sim_entrada1.senal_simulacion(n, ts, self.entrada)

        else:
            return 0

class ListaPWM:

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

        temp = NodoPWM(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickPWM)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarPWM)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoPWM)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoPWM)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoPWM) # 3 Windows/Unix
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

        temp = NodoPWM(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickPWM)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarPWM)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoPWM)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoPWM)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoPWM)  # 3 Windows/Unix
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
