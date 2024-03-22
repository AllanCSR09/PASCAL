from tkinter import *
import numpy as np
import Simulacion
from tkinter import ttk
from tkinter import messagebox


class NodoCTE:
    def __init__(self, id_CTE, tupla_listas, px, py):

        self.dato = id_CTE
        self.tipo = "CTE"
        self.nombre = "CTE_"+str(id_CTE)
        self.posicionx = px
        self.posiciony = py
        self.tipoNetlist = "E"

        self.dx = None
        self.dy = None

        # Salida
        self.salida = None

        self.siguiente = None

        self.window = tupla_listas[1]
        self.mainWindow = tupla_listas[0]
        self.imagen = PhotoImage(file="CTE.png")

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

        self.tupla_listas = tupla_listas
        self.creandoLinea = None
        self.tipoCreandoLinea = None

        self.ventanaCerrada = True
        self.borrandoElemento = False

        # Variables ------------------------
        self.variable_constante = 1

    def dobleClickCTE(self, event):

        if self.ventanaCerrada:
            self.ventanaCerrada = False

            self.windowCTE = Toplevel(self.mainWindow)
            self.windowCTE.resizable(False, False)
            self.windowCTE.title(self.nombre)

            # -------------------- FRAME 1 --------------------

            self.frame1 = Frame(self.windowCTE, bg="#2C2C2C")
            self.frame2 = Frame(self.windowCTE, bg="white")
            self.frame3 = Frame(self.windowCTE, bg="white")


            self.imagen_ventana = PhotoImage(file="CTEv.png")
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

            Label(self.frame2, text="Constante", font=("Arial Rounded MT Bold", -18))\
                .grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)

            self.c = StringVar()

            if self.variable_constante is None:
                self.c.set("1")
            else:
                self.c.set(str(self.variable_constante))

            Label(self.frame2, text="Valor:").grid(row=1, column=0, sticky=W, padx=(20,0), pady=(0,20))
            ttk.Entry(self.frame2, width=22, textvariable=self.c).grid(row=1, column=1, sticky=W, padx=(0,20), pady=(0, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(self.frame3, text="Aceptar", width=8, command=lambda: self.cerrarVentanaCTE("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(self.frame3, text="Cancelar", width=8, command=lambda: self.cerrarVentanaCTE("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            self.frame1.pack(side=TOP, fill=BOTH)
            self.frame2.pack(side=TOP, fill=BOTH)
            self.frame3.pack(side=TOP, fill=BOTH)

            self.windowCTE.protocol("WM_DELETE_WINDOW", self.cerrarVentanaCTE)

            self.windowCTE.withdraw()
            self.windowCTE.update_idletasks()
            x = (self.windowCTE.winfo_screenwidth() - self.windowCTE.winfo_reqwidth()) / 2
            y = (self.windowCTE.winfo_screenheight() - self.windowCTE.winfo_reqheight()) / 2
            self.windowCTE.geometry("+%d+%d" % (x, y))

            self.windowCTE.deiconify()

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
            self.windowCTE.lift()

    def cerrarVentanaCTE(self, opcion="Cancelar"):

        if opcion == "Aceptar":

            try:

                constante = eval(self.c.get())

                if type(constante) is not int and type(constante) is not float:
                    raise Exception

                self.variable_constante = constante

                self.ventanaCerrada = True
                self.windowCTE.destroy()

            except Exception:
                messagebox.showerror("Error", "Valor de constante inválido")

                self.windowCTE.lift()

        else:
            self.ventanaCerrada = True
            self.windowCTE.destroy()

    def arrastrarCTE(self, event):

        # tamano_ventana_x = self.window.winfo_width() - 20
        # tamano_ventana_y = self.window.winfo_height() - 20
        #
        # if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20:
        #     self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
        #
        #     self.posicionx = event.x - self.dx
        #     self.posiciony = event.y - self.dy

        pass

    def clickIzquierdoCTE(self, event):
        self.dx = event.x - self.posicionx
        self.dy = event.y - self.posiciony

        if self.borrandoElemento:
            self.eliminarCTE()

        else:

            if 38 > self.dx > 28 and 6 > abs(self.dy):  # Salida CTE

                if self.creandoLinea is not None and self.salida is None and not self.tipoCreandoLinea:
                    tupla = (self.posicionx + 32, self.posiciony-1)
                    self.salida = self.creandoLinea
                    self.tupla_listas[2].ultimoNodo(self.creandoLinea, self.nombre, tupla)

                if self.creandoLinea is None and self.salida is None:
                    coord = [self.posicionx + 32, self.posiciony-1]
                    self.tupla_listas[2].agregar(self.tupla_listas, self.nombre, coord, True)  # Nueva Conexion
                    self.salida = self.creandoLinea

    def clickDerechoCTE(self, event):

        self.eliminarCTE()

    def eliminarCTE(self):

        if self.creandoLinea is None:
            self.window.delete(self.nombre)
            self.window.delete(self.labelNombre)
            self.window.delete(self.labelSalida1)
            self.window.unbind(self.nombre)

            if self.salida is not None:
                self.tupla_listas[2].eliminarConexion(self.salida)

            self.tupla_listas[7].remover(self.nombre)

    def enMovimientoCTE(self, event):

        tamano_ventana_x = self.window.winfo_width() - 20
        tamano_ventana_y = self.window.winfo_height() - 20

        if tamano_ventana_x > event.x > 20 and tamano_ventana_y > event.y > 20 and self.creandoLinea is None:
            self.window.move(self.nombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)
            self.window.move(self.labelNombre, event.x - self.posicionx - self.dx, event.y - self.posiciony - self.dy)

            # Movimiento de la Conexion
            # ----------------------------------

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
        self.estado_labelSalida1 = False

# --------------------------------------------
    def senal_nombres(self, lista_nombres):

        lista_nombres.append(self.nombre)

        return lista_nombres

    def senal_simulacion(self, n, ts, conexion):

        return float(self.variable_constante)

class ListaCTE:

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

        temp = NodoCTE(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickCTE)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarCTE)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoCTE)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoCTE)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoCTE) # 3 Windows/Unix
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

        temp = NodoCTE(item, tupla_listas, x, y)
        temp.siguiente = self.cabeza
        self.cabeza = temp

        temp.window.tag_bind(temp.nombre, "<Double-Button-1>", temp.dobleClickCTE)
        temp.window.tag_bind(temp.nombre, "<ButtonRelease-1>", temp.arrastrarCTE)
        temp.window.tag_bind(temp.nombre, "<Button-1>", temp.clickIzquierdoCTE)
        temp.window.tag_bind(temp.nombre, "<B1-Motion>", temp.enMovimientoCTE)
        temp.window.tag_bind(temp.nombre, "<Button-2>", temp.clickDerechoCTE)  # 3 Windows/Unix
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
