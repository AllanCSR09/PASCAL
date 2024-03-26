from ast import Pass
from logging import RootLogger
from logging.handlers import TimedRotatingFileHandler
from re import M
from textwrap import fill
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tokenize import String
from tracemalloc import stop
from turtle import title, width
from typing import Protocol
from warnings import catch_warnings
import weakref
from PIL import ImageTk, Image    #Biblioteca para manejo de imágenes en Tkinter
from tkinter import messagebox
from claseADC import ListaADC
from clasePID import ListaPID
from clasePWM import ListaPWM
from claseRE import ListaRE
from claseCTE import ListaCTE
from claseFT import ListaFT
from claseSAT import ListaSAT
from claseQDEC import ListaQDEC
from claseENTP import ListaENTP
from claseSALP import ListaSALP
from claseDAC import ListaDAC
from claseFLT import ListaFLT
from claseSCOPE import ListaSCOPE
from claseSTEP import ListaSTEP
from claseTRAPECIO import ListaTRAPECIO
from claseLinea import ListaLinea
from claseDER import ListaDER
from claseSUM import ListaSUM
from claseREST import ListaREST
from tkinter import filedialog
import GuardarArchivo
import Simulacion
import AbrirArchivo
import Netlist
import time
import serial
from time import sleep
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
from matplotlib.figure import Figure
from tkinter.messagebox import askyesno
import serial.tools.list_ports
#from VentanaPrincipal import Aplicacion
#import VentanaPrincipal.Aplicacion as andrewindow
#AQUI PROBÉ EL CONTROL DE VERSIONES
#AQUI PROBÉ EL NUEVO BRANCH
#Temas


tema="White"
tema2="Gray"
letras="Black"

#Características por defecto de la ventana root
root = tk.Tk()
root.title("Plataforma Acelerada de Sistemas de Control Automático en Laboratorio")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.configure(bg=tema)
# root.eval('tk::PlaceWindow . center')

root.geometry("1085x655")
root.update_idletasks()

#Temas
global tema_Principal
global tema_Secundario
global tema_Barra
global Letras

tema_Principal=StringVar()
#tema_Principal.set("#003366")
tema_Principal.set("#2C2C2C")
tema_Secundario=StringVar()
tema_Secundario.set("#B0E3E6")
tema_Barra=StringVar()
tema_Barra.set("#EFEFEF")
Letras=StringVar()
Letras.set("#003366")
Resolucion=StringVar()
Resolucion.set("1085x655")
theme=StringVar()
theme.set("dark")


#Botones de la barra de herramientas para todas las pantallas
#Botón atrás
abrir_ATRAS = Image.open("Atras.png")
abrir_ATRAS = abrir_ATRAS.resize((25, 25), Image.ANTIALIAS)
global img_ATRAS
img_ATRAS = ImageTk.PhotoImage(abrir_ATRAS)

#Botón Revertir
abrir_REVERTIR = Image.open("Revertir.png")
abrir_REVERTIR = abrir_REVERTIR.resize((25, 25), Image.ANTIALIAS)
global img_REVERTIR
img_REVERTIR = ImageTk.PhotoImage(abrir_REVERTIR)

#Botón Rehacer
abrir_REHACER = Image.open("Rehacer.png")
abrir_REHACER = abrir_REHACER.resize((25, 25), Image.ANTIALIAS)
global img_REHACER
img_REHACER = ImageTk.PhotoImage(abrir_REHACER)

#Botón Información
abrir_INFORMA = Image.open("Informa.png")
abrir_INFORMA = abrir_INFORMA.resize((25, 25), Image.ANTIALIAS)
global img_INFORMA
img_INFORMA = ImageTk.PhotoImage(abrir_INFORMA)

#Botón de borrar
abrir_BORRAR = Image.open("icono_borrar.png")
abrir_BORRAR = abrir_BORRAR.resize((25, 25), Image.ANTIALIAS)
global img_BORRAR
img_BORRAR = ImageTk.PhotoImage(abrir_BORRAR)

#Botón de simulación
abrir_SIM = Image.open("SIM.png")
abrir_SIM = abrir_SIM.resize((25, 25), Image.ANTIALIAS)
global img_SIM
img_SIM = ImageTk.PhotoImage(abrir_SIM)

#Botón de ejecutar
abrir_RUN = Image.open("Run.png")
abrir_RUN = abrir_RUN.resize((25, 25), Image.ANTIALIAS)
global img_RUN
img_RUN = ImageTk.PhotoImage(abrir_RUN)

#Botón de detener
abrir_STOP = Image.open("Stop.png")
abrir_STOP = abrir_STOP.resize((25, 25), Image.ANTIALIAS)
global img_STOP
img_STOP = ImageTk.PhotoImage(abrir_STOP)

#Botón de transferir
abrir_TRANSFER = Image.open("Transferir.png")
abrir_TRANSFER = abrir_TRANSFER.resize((30, 25), Image.ANTIALIAS)
global img_TRANSFER
img_TRANSFER = ImageTk.PhotoImage(abrir_TRANSFER)

#Boton de Acerca de
abrir_ACERCA = Image.open("Acercade.png")
abrir_ACERCA = abrir_ACERCA.resize((30,25), Image.ANTIALIAS)
global img_ACERCA
img_ACERCA = ImageTk.PhotoImage(abrir_ACERCA)


#Funciones de hover (puntero sobre objeto) para todas las pantallas
def inButtonBack(event):
    status_bar.configure(text="ATRÁS")

def inButtonBack2(event):
    status_bar2.configure(text="ATRÁS")
        
def inButtonRevert(event):
    status_bar.configure(text="DESHACER")

def inButtonRevert2(event):
    status_bar2.configure(text="DESHACER")

def inButtonRedo(event):
    status_bar.configure(text="REHACER")

def inButtonRedo2(event):
    status_bar2.configure(text="REHACER")

def inButtonInformation(event):
    status_bar.configure(text="INFORMACIÓN")

def inButtonInformation2(event):
    status_bar2.configure(text="INFORMACIÓN")

def inButtonErase(event):
    status_bar.configure(text="BORRAR")
    
def inButtonErase2(event):
    status_bar2.configure(text="BORRAR")

def inButtonSimulate(event):
    status_bar.configure(text="SIMULAR")
    
def inButtonSimulate2(event):
    status_bar2.configure(text="SIMULAR")

def inButtonRun(event):
    status_bar.configure(text="RUN")
    
def inButtonRun2(event):
    status_bar2.configure(text="RUN")

def inButtonStop(event):
    status_bar.configure(text="STOP")
    
def inButtonStop2(event):
    status_bar2.configure(text="STOP")

def inButtonAcerca(event):
    status_bar.configure(text="ACERCA DE")
    
def inButtonAcerca2(event):
    status_bar2.configure(text="ACERCA DE")

def inButtonTransfer(event):
    status_bar.configure(text="TRANSMITIR")

def inButtonTransfer2(event):
    status_bar2.configure(text="TRANSMITIR")

def inButtonGuardar(event):
    status_bar.configure(text="GUARDAR")

def inButtonAbrir(event):
    status_bar.configure(text="ABRIR")

def inButtonConfiguracion(event):
    status_bar.configure(text="CONFIGURACIÓN")

def inButtonADC(event):
    status_bar.configure(text="CONVERTIDOR ANALÓGICO-DIGITAL")

def inButtonPID(event):
    status_bar.configure(text="PID")

def inButtonPWM(event):
    status_bar.configure(text="MODULACIÓN POR ANCHO DE PULSOS")

def inButtonRE(event):
    status_bar.configure(text="REALIMENTACIÓN DE ESTADOS")  

def inButtonCTE(event):
    status_bar.configure(text="CONSTANTE")     

def inButtonFT(event):
    status_bar.configure(text="FUNCIÓN DE TRANSFERENCIA")

def inButtonSAT(event):
    status_bar.configure(text="SATURADOR")

def inButtonQDEC(event):
    status_bar.configure(text="DECODIFICADOR DE CUADRATURA")

def inButtonDAC(event):
    status_bar.configure(text="CONVERTIDOR DIGITAL-ANALÓGICO")

def inButtonFLT(event):
    status_bar.configure(text="FILTRO")

def inButtonSALP(event):
    status_bar.configure(text="Salida de la Planta")

def inButtonENTP(event):
    status_bar.configure(text="Entrada a la Planta")

def outButton(event):
    status_bar.configure(text="")
    
def outButton2(event):
    status_bar2.configure(text="")

def outButtonInStructureScreen(event):
    status_bar.configure(text=directorio)



##########Pantalla de Inicio##########
def inicio():

    #Funciones de la Pantalla de Inicio
    #loginWindow(): Una función que crea una ventana de ingreso para para el usuario 
    def loginWindow(): 
        button_START.configure(state=DISABLED)
        #credentials(): Revisa las credenciales ingresadas para determinar si los datos son válidos o inválidos
        def credentials():
            usuario=username.get()
            contraseña=password.get()
            
            if usuario=='' or contraseña=='':
                message.set("Respuesta inválida")
            else:
                if usuario=="profesor" and contraseña=="admin":
                    message.set("Acceso otorgado")
                    principal()
                    loginScreen.destroy()

                if usuario=="estudiante" and contraseña=="estudiante":
                    message.set("Acceso otorgado")
                    principal()
                    loginScreen.destroy()

                else:
                    message.set("¡¡¡Usuario o contraseña equivocados!!!")



        #cierre(): Si el usuario intenta cerrar la ventana de ingreso, aparece un mensaje de confirmación. Si acepta, se cierra la aplicación.
        def cierre():
            if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
                root.destroy()


        loginScreen = Toplevel()
        loginScreen.lift()
        loginScreen.title("Ventana de ingreso")
        loginScreen.geometry("300x250")

        global message
        global username
        global password

        username = StringVar()
        password = StringVar()
        message = StringVar()

        instruction = Label(loginScreen,width="300", text="Ingrese sus credenciales", bg="black",fg="white")
        instruction.pack()
        
        label_Username = Label(loginScreen, text="Usuario * ")
        label_Username.place(x=20,y=40)
        
        entry_Username = Entry(loginScreen, textvariable=username)
        entry_Username.place(x=90,y=42)
        
        label_password = Label(loginScreen, text="Contraseña * ")
        label_password.place(x=20,y=80)
        
        entry_password = Entry(loginScreen, textvariable=password ,show="*")
        entry_password.place(x=90,y=82)
        
        response = Label(loginScreen, text="",textvariable=message)
        response.place(x=95,y=100)
        
        button_LOG = Button(loginScreen, text="Login", width=10, height=1, bg="#003366", fg="#B0E3E6", command=credentials)
        button_LOG.place(x=105,y=130)

        loginScreen.protocol("WM_DELETE_WINDOW", cierre)

    
    #Resized(event): Una función para cambiar el tamaño de la imagen de fondo de la pantalla de inicio para que se adapte al tamaño
    #que el usuario decida
    def resized(event):
        global canvas_img
        global img_inicio
        img_inicio_new = Image.open("fondoinicio2.png").resize((event.width, event.height), Image.ANTIALIAS)
        #img_inicio_new=img_inicio_new.resize((event.width, event.height), Image.ANTIALIAS)
        img_inicio = ImageTk.PhotoImage(img_inicio_new)
        canvaInicio.itemconfig(canvas_img, image=img_inicio)


    #Frame de la Pantalla de Inicio
    global frm_inicio
    frm_inicio = Frame(root, bg=tema)
    frm_inicio.pack(fill="both", expand=True)
    frm_inicio.columnconfigure(0, weight=1)
    frm_inicio.columnconfigure(1, weight=1)


    #Canvas para la imagen de fondo de la Pantalla de Inicio
    canvaInicio=Canvas(frm_inicio)
    canvaInicio.pack(fill="both", expand=True)
    canvaInicio.bind("<Configure>", resized)

    imagenFondo = Image.open("fondoinicio2.png")
    imagenFondo = imagenFondo.resize((1085, 655), Image.ANTIALIAS)
    global img_inicio
    img_inicio = ImageTk.PhotoImage(imagenFondo)
    
    global canvas_img
    canvas_img = canvaInicio.create_image(0,0, image=img_inicio, anchor="nw")

    
    #Botones de la Pantalla de Inicio
    button_START = Button(frm_inicio, text="Comenzar", font=("TkDefaultFont", 20), bg="#B0E3E6", fg="#003366", command=loginWindow)
    button_START_window = canvaInicio.create_window(150, 550, window=button_START)
    button_EXIT = Button(frm_inicio, text="Salir", font=("TkDefaultFont", 20), bg="#B0E3E6", fg="#003366", command=root.destroy)
    button_EXIT_window= canvaInicio.create_window(350, 550, window=button_EXIT)


    


##########Menu Principal##########
def principal():
        
    #Funciones del Menú Principal
    
    #info_PRINCIPAL(): Funcion que despliega una ventana con la información guía del Menú Principal al presionar el botón INFORMACIÓN
    def info_PRINCIPAL():
        help_PRINCIPAL = Toplevel()
        help_PRINCIPAL.columnconfigure(0, weight=1)
        help_PRINCIPAL.rowconfigure(1, weight=1)
            
        #Nombre de la Ventana
        help_PRINCIPAL.title("Ventana de información")

        #Titulo de la Ventana 
        titulo=Label(help_PRINCIPAL, text="Información del Menú Principal", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
        titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        informacion_PRINCIPAL = Text(help_PRINCIPAL, width=500, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        informacion_PRINCIPAL.grid(row=1, column=0, sticky="ns")

        text_PRINCIPAL="""Está en la Pantalla del Menú Principal.\nSe le presentan dos opciones para seleccionar:\nEXPERIMENTOS y CONFIGURACIÓN\n\nSeleccione la opción de EXPERIMENTOS si desea acceder a los experimentos disponibles en el Labotarorio de Control Automático. Si lo que busca es iniciar uno de estos experimentos, esta opción es la indicada.\n\nSeleccione la opción CONFIGURACIÓN si desea configurar un aspecto general de la aplicación, tal como el tema.\n\nLa barra de herramientas es la barra que se encuentra debajo del título de la pantalla. En el lado derecho de esta barra puede observar el nombre de los botones posicionados a la izquierda de la misma barra al colocar el puntero sobre ellos. Algunos de estos botones estan habilitados y deshabilitados dependiendo de la pantalla en la que se encuentre. Para el caso del menú principal, el estado de los botones es el siguiente:\n\nATRAS(Deshabilitado):Cuando es presionado, este botón permite regresar a la pantalla anterior.\n\nDESHACER(Deshabilitado):Cuando es presionado, este botón deshace la última acción realizada por el usuario.\n\nREHACER(Deshabilitado): Cuando es presionado, este botón rehace la última acción deshecha por el usuario.\n\nINFORMACIÓN(Habilitado):Cuando es presionado, este botón abre una ventana con información guía de la pantalla para el usuario.\n\nBORRAR(Deshabilitado): Cuando es presionado, este botón permite eliminar elementos de la estructura de un experimento.\n\nSIMULACIÓN(Deshabilitado):Cuando es presionado, este botón simula una estructura de experimento.\n\nTRANSMITIR(Deshabilitado): Cuando es presionado, este botón envía la información de la estructura de un experimento al hardware.\n\nRUN(Deshabilitado): Cuando es presionado, este botón inicia la ejecución de un experimento.\n\nSTOP(Deshabilitado): Cuando es presionado, este botón detiene la ejecución de un experimento.\n\nACERCA DE(Habilitado): Cuando es presionado, este botón despliega una ventana secundaria con información general de PASCAL. """
        informacion_PRINCIPAL.insert(tk.END, text_PRINCIPAL)
        informacion_PRINCIPAL.config(state=DISABLED)

        scrollWindow=Scrollbar(help_PRINCIPAL)
        scrollWindow.grid(row=1, column=1, sticky="ns")
        scrollWindow.config(command=informacion_PRINCIPAL.yview)
        informacion_PRINCIPAL.config(yscrollcommand=scrollWindow.set)
            
        help_PRINCIPAL.geometry("500x500")
        help_PRINCIPAL.resizable(width=False, height=False)

    def about_PASCAL():
        aboutIt = Toplevel()
        aboutIt.columnconfigure(0, weight=1)
        aboutIt.rowconfigure(0, weight=1)
        
        #Nombre de la ventana
        aboutIt.title("Ventana acerca de PASCAL")
        abrir_ABOUT = Image.open("aboutPASCAL.png")
        global img_about
        img_about = ImageTk.PhotoImage(abrir_ABOUT)

        sobre = Label(aboutIt, image=img_about)
        sobre.grid(row=0, column=0)

        aboutIt.resizable(width=False, height=False)


    if tema_Principal.get()=="#2C2C2C":
        imagen1="Experimentos.png"
        imagen2="Configuración.png"
    else:
        imagen1="Experimentos2.png"
        imagen2="Configuración2.png"
    
    raw_plantas = Image.open(imagen1)
    raw_plantas = raw_plantas.resize((250, 250), Image.ANTIALIAS)
    global img_plantas
    img_plantas = ImageTk.PhotoImage(raw_plantas)
        
    raw_config = Image.open(imagen2)
    raw_config = raw_config.resize((250, 250), Image.ANTIALIAS)
    global img_config
    img_config = ImageTk.PhotoImage(raw_config)
    
    #Frame
    frm_inicio.destroy()

    global frm_principal    
    frm_principal = Frame(root, width=800, height=600, bg=tema_Principal.get())
    frm_principal.pack(fill="both", expand=True)
    frm_principal.columnconfigure(0, weight=1)
    frm_principal.columnconfigure(1, weight=1)


    #Titulo de la Pantalla
    mensaje=Label(frm_principal, text="Menú Principal", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=2, sticky="ew")


    #Barra de Menú
    frm_barra=LabelFrame(frm_principal, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0,64))

    frm_barra.columnconfigure(0, weight=1)

    global status_bar
    status_bar=Label(frm_barra, text="", font=("TkDefaultFont", 10, "bold"), anchor=W, fg="#003366")
    status_bar.grid(row=0, column=0, sticky="ew")

    #Botones de la barra de Menú
    back = Button(frm_barra, image=img_ATRAS, borderwidth=0, state=DISABLED)
    back.grid(row = 0, column = 1, sticky=tk.E, padx=10)
    back.bind("<Enter>", inButtonBack)
    back.bind("<Leave>", outButton)

    revert = Button(frm_barra, image=img_REVERTIR, borderwidth=0, state=DISABLED)
    revert.grid(row = 0, column = 2, sticky=tk.E, padx=10)
    revert.bind("<Enter>", inButtonRevert)
    revert.bind("<Leave>", outButton)

    redo = Button(frm_barra, image=img_REHACER, borderwidth=0, state=DISABLED)
    redo.grid(row = 0, column = 3, sticky=tk.E, padx=10)
    redo.bind("<Enter>", inButtonRedo)
    redo.bind("<Leave>", outButton)

    information = Button(frm_barra, image=img_INFORMA, borderwidth=0, command=info_PRINCIPAL)
    information.grid(row = 0, column = 4, sticky=tk.E, padx=10)
    information.bind("<Enter>", inButtonInformation)
    information.bind("<Leave>", outButton)

    erase = Button(frm_barra, image=img_BORRAR, borderwidth=0, state=DISABLED)
    erase.grid(row = 0, column = 5, sticky=tk.E, padx=10)
    erase.bind("<Enter>", inButtonErase)
    erase.bind("<Leave>", outButton)

    simulate = Button(frm_barra, image=img_SIM, borderwidth=0, state=DISABLED)
    simulate.grid(row = 0, column = 6, sticky=tk.E, padx=10)
    simulate.bind("<Enter>", inButtonSimulate)
    simulate.bind("<Leave>", outButton)

    transfer = Button(frm_barra, image=img_TRANSFER, borderwidth=0, state=DISABLED)
    transfer.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer.bind("<Enter>", inButtonTransfer)
    transfer.bind("<Leave>", outButton)

    running = Button(frm_barra, image=img_RUN, borderwidth=0, state=DISABLED)
    running.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running.bind("<Enter>", inButtonRun)
    running.bind("<Leave>", outButton)

    stopping = Button(frm_barra, image=img_STOP, borderwidth=0, state=DISABLED)
    stopping.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping.bind("<Enter>", inButtonStop)
    stopping.bind("<Leave>", outButton)

    about = Button(frm_barra, image=img_ACERCA, borderwidth=0, command=about_PASCAL)
    about.grid(row = 0, column = 10, sticky=tk.E, padx=10)
    about.bind("<Enter>", inButtonAcerca)
    about.bind("<Leave>", outButton)

        
    #Botones de la pantalla de Menu Principal
    plantas=Button(frm_principal, image=img_plantas, height=250, width=250, command=experiments)
    plantas.grid(row=2, column=0)
    plantastxt=Label(frm_principal, text="Experimentos", font=("TkDefaultFont", 20), bg=tema_Principal.get(), fg=tema_Secundario.get())
    plantastxt.grid(row=3, column=0, pady=(25,0))

    configuracion=Button(frm_principal, image=img_config, height=250, width=250, command=config)
    configuracion.grid(row=2, column=1)
    configtxt=Label(frm_principal, text="Configuración", font=("TkDefaultFont", 20), bg=tema_Principal.get(), fg=tema_Secundario.get())
    configtxt.grid(row=3, column=1, pady=(25,0))




#########Pantalla de Configuración###########################################################################################################################3
def config():

    #Regreso al Menu Principal
    def configtoprincipal():
        frm_config.destroy()
        principal()

    #Información de la pantalla de configuración
    def info_CONFIG():
        help_CONFIG = Toplevel()
        help_CONFIG.columnconfigure(0, weight=1)
        help_CONFIG.rowconfigure(1, weight=1)
            
        #Nombre de la Ventana
        help_CONFIG.title("Ventana de información")

        #Titulo de la Ventana 
        titulo=Label(help_CONFIG, text="Información de la Pantalla de Configuración", font=("TkDefaultFont", 15), bg=tema_Secundario.get())
        titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        #Información de la pantalla
        informacion_CONFIG = Text(help_CONFIG, width=500, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        informacion_CONFIG.grid(row=1, column=0, sticky="ns")

        text_CONFIG="""Está en la Pantalla de Configuración.\nEn esta pantalla puede configurar características de PASCAL, entre ellas temas y otras que se implementen en versiones futuras:\n\nRESOLUCIÓN: Puede escoger entre tres resoluciones en pixeles para la pantalla de PASCAL: 1085x655 (por defecto)\n1366x768\n1920x1080\n\nTEMA:\nPuede escoger entre dos temas segun sus preferencias:\nOscuro (por defecto)\nClaro \n\nEn la sección de puerto de comunicación puede visualizar los puertos disponibles para comunicarse con la unidad de hardware al presionar el botón "Mostrar".\n\nLa barra de herramientas es la barra que se encuentra debajo del título de la pantalla. En el lado derecho de esta barra puede observar el nombre de los botones posicionados a la izquierda de la misma barra al colocar el puntero sobre ellos. Algunos de estos botones estan habilitados y deshabilitados dependiendo de la pantalla en la que se encuentre. Para el caso dela Pantalla de Configuración, el estado de los botones es el siguiente:\n\nATRAS(Habilitado):Cuando es presionado, este botón permite regresar a la pantalla anterior.\n\nDESHACER(Deshabilitado):Cuando es presionado, este botón deshace la última acción realizada por el usuario.\n\nREHACER(Deshabilitado): Cuando es presionado, este botón rehace la última acción deshecha por el usuario.\n\nINFORMACIÓN(Habilitado):Cuando es presionado, este botón abre una ventana con información guía de la pantalla para el usuario.\n\nBORRAR(Deshabilitado): Cuando es presionado, este botón permite eliminar elementos de la estructura de un experimento.\n\nSIMULACIÓN(Deshabilitado):Cuando es presionado, este botón simula una estructura de experimento.\n\nTRANSMITIR(Deshabilitado): Cuando es presionado, este botón envía la información de la estructura de un experimento al hardware.\n\nRUN(Deshabilitado): Cuando es presionado, este botón inicia la ejecución de un experimento.\n\nSTOP(Deshabilitado): Cuando es presionado, este botón detiene la ejecución de un experimento.n\n\nACERCA DE(Habilitado): Cuando es presionado, este botón despliega una ventana secundaria con información general de PASCAL. """
        informacion_CONFIG.insert(tk.END, text_CONFIG)
        informacion_CONFIG.config(state=DISABLED)

        scrollWindow=Scrollbar(help_CONFIG)
        scrollWindow.grid(row=1, column=1, sticky="ns")
        scrollWindow.config(command=informacion_CONFIG.yview)
        informacion_CONFIG.config(yscrollcommand=scrollWindow.set)
            
        help_CONFIG.geometry("500x500")
        help_CONFIG.resizable(width=False, height=False)

    def about_PASCAL():
        aboutIt = Toplevel()
        aboutIt.columnconfigure(0, weight=1)
        aboutIt.rowconfigure(0, weight=1)
        
        #Nombre de la ventana
        aboutIt.title("Ventana acerca de PASCAL")
        abrir_ABOUT = Image.open("aboutPASCAL.png")
        global img_about
        img_about = ImageTk.PhotoImage(abrir_ABOUT)

        sobre = Label(aboutIt, image=img_about)
        sobre.grid(row=0, column=0)

        aboutIt.resizable(width=False, height=False)


     #Función para cambiar el tema
    def cambiar_tema(x):
        if x=="light":
            tema_Principal.set("#E5E4E2")
            tema_Secundario.set("#003366")
            Letras.set("White")
            theme.set("light")
            frm_config.destroy()
            config()
        else:
            tema_Principal.set("#2C2C2C")
            tema_Secundario.set("#B0E3E6")
            Letras.set("#003366")
            theme.set("dark")
            frm_config.destroy()
            config()

    def cambiar_resolucion(r):
        root.geometry(r)
        frm_config.destroy()
        config()

    def ver_puertos():
        ports = serial.tools.list_ports.comports()
        for oneport in ports:
            port = Label (lbfrm_comm, text=oneport, font=("TkDefaultFont", 10), bg=tema_Principal.get(), fg=tema_Secundario.get())
            port.grid(row=ports.index(oneport), column=0)

    frm_principal.destroy()

    global frm_config        
    frm_config = Frame(root, bg=tema_Principal.get())
    frm_config.pack(fill="both", expand=True)
    frm_config.columnconfigure(0, weight=1)
    frm_config.columnconfigure(1, weight=1)
    frm_config.rowconfigure(5, weight=1)

    mensaje=Label(frm_config, text="Pantalla de Configuración", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=2, sticky="ew")

                
    #Barra de Menú
    frm_barra=Frame(frm_config, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0,32))

    frm_barra.columnconfigure(0, weight=1)

    global status_bar
    status_bar=Label(frm_barra, text="", font=("TkDefaultFont", 10, "bold"), anchor=W, fg="#003366")
    status_bar.grid(row=0, column=0, sticky="ew")

    #Botones de la barra de Menú
    back = Button(frm_barra, image=img_ATRAS, borderwidth=0, command=configtoprincipal)
    back.grid(row = 0, column = 1, sticky=tk.E, padx=10)
    back.bind("<Enter>", inButtonBack)
    back.bind("<Leave>", outButton)

    revert = Button(frm_barra, image=img_REVERTIR, borderwidth=0, state=DISABLED)
    revert.grid(row = 0, column = 2, sticky=tk.E, padx=10)
    revert.bind("<Enter>", inButtonRevert)
    revert.bind("<Leave>", outButton)

    redo = Button(frm_barra, image=img_REHACER, borderwidth=0, state=DISABLED)
    redo.grid(row = 0, column = 3, sticky=tk.E, padx=10)
    redo.bind("<Enter>", inButtonRedo)
    redo.bind("<Leave>", outButton)

    information = Button(frm_barra, image=img_INFORMA, borderwidth=0, command=info_CONFIG)
    information.grid(row = 0, column = 4, sticky=tk.E, padx=10)
    information.bind("<Enter>", inButtonInformation)
    information.bind("<Leave>", outButton)

    erase = Button(frm_barra, image=img_BORRAR, borderwidth=0, state=DISABLED)
    erase.grid(row = 0, column = 5, sticky=tk.E, padx=10)
    erase.bind("<Enter>", inButtonErase)
    erase.bind("<Leave>", outButton)

    simulate = Button(frm_barra, image=img_SIM, borderwidth=0, state=DISABLED)
    simulate.grid(row = 0, column = 6, sticky=tk.E, padx=10)
    simulate.bind("<Enter>", inButtonSimulate)
    simulate.bind("<Leave>", outButton)

    transfer = Button(frm_barra, image=img_TRANSFER, borderwidth=0, state=DISABLED)
    transfer.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer.bind("<Enter>", inButtonTransfer)
    transfer.bind("<Leave>", outButton)

    running = Button(frm_barra, image=img_RUN, borderwidth=0, state=DISABLED)
    running.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running.bind("<Enter>", inButtonRun)
    running.bind("<Leave>", outButton)

    stopping = Button(frm_barra, image=img_STOP, borderwidth=0, state=DISABLED)
    stopping.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping.bind("<Enter>", inButtonStop)
    stopping.bind("<Leave>", outButton)

    about = Button(frm_barra, image=img_ACERCA, borderwidth=0, command=about_PASCAL)
    about.grid(row = 0, column = 10, sticky=tk.E, padx=10)
    about.bind("<Enter>", inButtonAcerca)
    about.bind("<Leave>", outButton)


    lbfrm_resolucion = LabelFrame(frm_config, text="Resolución", padx=25, pady=25, font=("TkDefaultFont", 15, "bold"), bg=tema_Principal.get(), fg=tema_Secundario.get())
    lbfrm_resolucion.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)
    lbfrm_resolucion.columnconfigure(3, weight=1)
        
    resolucion1085x655 = Radiobutton(lbfrm_resolucion, text="1085x655", variable=Resolucion, value="1085x655", font=("TkDefaultFont", 15), bg=tema_Principal.get(), fg=tema_Secundario.get())
    resolucion1085x655.grid(row=0, column=0, padx=25)

    resolucion1366x768 = Radiobutton(lbfrm_resolucion, text="1366x768", variable=Resolucion, value="1366x768", font=("TkDefaultFont", 15), bg=tema_Principal.get(), fg=tema_Secundario.get())
    resolucion1366x768.grid(row=0, column=1, padx=25)

    resolucion1920x1080= Radiobutton(lbfrm_resolucion, text="1920x1080", variable=Resolucion, value="1920x1080", font=("TkDefaultFont", 15), bg=tema_Principal.get(), fg=tema_Secundario.get())
    resolucion1920x1080.grid(row=0, column=2, padx=25)

    aplicarresolucion=Button(lbfrm_resolucion, text="Aplicar", font=("TkDefaultFont", 15), fg=tema_Principal.get(), bg=tema_Secundario.get(), command=lambda:cambiar_resolucion(Resolucion.get()))
    aplicarresolucion.grid(row=0, column=4, padx=25, sticky="E")


    lbfrm_tema = LabelFrame(frm_config, text="Tema", padx=25, pady=25, font=("TkDefaultFont", 15, "bold"), bg=tema_Principal.get(), fg=tema_Secundario.get())
    lbfrm_tema.grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)
    lbfrm_tema.columnconfigure(2, weight=1)

    temalight = Radiobutton(lbfrm_tema, text="Claro", variable=theme, value="light", font=("TkDefaultFont", 15), bg=tema_Principal.get(), fg=tema_Secundario.get())
    temalight.grid(row=0, column=0, padx=25)

    temadark = Radiobutton(lbfrm_tema, text="Oscuro", variable=theme, value="dark", font=("TkDefaultFont", 15), bg=tema_Principal.get(), fg=tema_Secundario.get())
    temadark.grid(row=0, column=1, padx=25)

    aplicartema=Button(lbfrm_tema, text="Aplicar", font=("TkDefaultFont", 15), command=lambda:cambiar_tema(theme.get()), fg=tema_Principal.get(), bg=tema_Secundario.get())
    aplicartema.grid(row=0, column=2, sticky="E", padx=25)


    lbfrm_comm = LabelFrame(frm_config, text="Puertos de comunicación", padx=25, pady=25, font=("TkDefaultFont", 15, "bold"), bg=tema_Principal.get(), fg=tema_Secundario.get())
    lbfrm_comm.grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)
    lbfrm_comm.columnconfigure(1, weight=1)

    aplicarpuerto=Button(lbfrm_comm, text="Mostrar", font=("TkDefaultFont", 15), fg=tema_Principal.get(), bg=tema_Secundario.get(), command=ver_puertos)
    aplicarpuerto.grid(row=0, column=1, sticky="E", padx=25)


    configsave=Button(frm_config, text="Menú principal", font=("TkDefaultFont", 15), bg=tema_Principal.get(), fg=tema_Secundario.get(), command=configtoprincipal)
    configsave.grid(row=5, column=0, columnspan=2)


#########Función para la pantalla de selección de experimentos####################################################################################################
def experiments():

    #Regreso al Menu Principal
    def experimentstoprincipal():
        frm_experimentos.destroy()
        principal()

    #Información de la pantalla Experimentos
    def info_EXPERIMENTS():
        help_EXPERIMENTS = Toplevel()
        help_EXPERIMENTS.columnconfigure(0, weight=1)
        help_EXPERIMENTS.rowconfigure(1, weight=1)
        
        #Nombre de la Ventana
        help_EXPERIMENTS.title("Ventana de información")

        #Titulo de la Ventana 
        titulo=Label(help_EXPERIMENTS, text="Información de la Pantalla de selección de experimentos", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
        titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        #Información de la pantalla
        informacion_EXPERIMENTS = Text(help_EXPERIMENTS, width=500, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        informacion_EXPERIMENTS.grid(row=1, column=0, sticky="ns")

        text_CONFIG="""Está en la Pantalla de selección de experimentos.\nEn esta pantalla puede seleccionar la planta con la que desea realizar un experimento de laboratorio con solo presionar sobre la imagen o nombre de la planta. Una vez seleccione uno de los experimentos, se abrirá la Ventana de experimento seleccionado, la cual contiene información general del sistema y las opciones para empezar el experimento, editar la información o cerrar esta ventana.\n\nLas credenciales de estudiante tienen acceso a iniciar un experimento ya existente en la Pantalla de selección de esperimentos, no pueden crear uno nuevo. Además, en la Ventana de experimento seleccionado, la opción para editar la descripción está deshabilitada.\n\nLas credenciales de profesor equivalen a las credenciales de administrador, lo cual les permite crear nuevos archivos. También pueden editar la descripción de los experimentos en la Ventana de experimento seleccionado.\n\nLa barra de herramientas es la barra que se encuentra debajo del título de la pantalla. En el lado derecho de esta barra puede observar el nombre de los botones posicionados a la izquierda de la misma barra al colocar el puntero sobre ellos. Algunos de estos botones estan habilitados y deshabilitados dependiendo de la pantalla en la que se encuentre. Para el caso de la Pantalla de selección de experimento, el estado de los botones es el siguiente:\n\nATRAS(Habilitado):Cuando es presionado, este botón permite regresar a la pantalla anterior.\n\nDESHACER(Deshabilitado):Cuando es presionado, este botón deshace la última acción realizada por el usuario.\n\nREHACER(Deshabilitado): Cuando es presionado, este botón rehace la última acción deshecha por el usuario.\n\nINFORMACIÓN(Habilitado):Cuando es presionado, este botón abre una ventana con información guía de la pantalla para el usuario.\n\nBORRAR(Deshabilitado): Cuando es presionado, este botón permite eliminar elementos de la estructura de un experimento.\n\nSIMULACIÓN(Deshabilitado):Cuando es presionado, este botón simula una estructura de experimento.\n\nTRANSMITIR(Deshabilitado): Cuando es presionado, este botón envía la información de la estructura de un experimento al hardware.\n\nRUN(Deshabilitado): Cuando es presionado, este botón inicia la ejecución de un experimento.\n\nSTOP(Deshabilitado): Cuando es presionado, este botón detiene la ejecución de un experimento.\n\nACERCA DE(Habilitado): Cuando es presionado, este botón despliega una ventana secundaria con información general de PASCAL. """
        informacion_EXPERIMENTS.insert(tk.END, text_CONFIG)
        informacion_EXPERIMENTS.config(state=DISABLED)

        scrollWindow=Scrollbar(help_EXPERIMENTS)
        scrollWindow.grid(row=1, column=1, sticky="ns")
        scrollWindow.config(command=informacion_EXPERIMENTS.yview)
        informacion_EXPERIMENTS.config(yscrollcommand=scrollWindow.set)
            
        help_EXPERIMENTS.geometry("500x500")
        help_EXPERIMENTS.resizable(width=False, height=False)


     #Función para la ventana de experimento seleccionado
    def systeminfo(planta):

        def openFile():
            #estructura()
            global sistema
            global trigger
            sistema=planta
            trigger=1
            estructura()

        
        def guardarDescripcion():
            escribir_archivo.write(descripcion_Experimento.get(1.0, END))
            escribir_archivo.close()
            descripcion_Experimento.config(state=DISABLED)
            btn_editar.configure(text="Editar", command=editarDescripcion)

        
        def editarDescripcion():
            global escribir_archivo
            escribir_archivo=open(archivo, "w")
            descripcion_Experimento.config(state=NORMAL)
            btn_editar.configure(text="Guardar", command=guardarDescripcion)


        global info
        info = Toplevel()
        info.geometry("600x600")
        info.resizable(width=False, height=False)
        info.configure(bg=tema_Principal.get())
        info.columnconfigure(0, weight=1)
        info.columnconfigure(1, weight=1)
            
        #Nombre de la Ventana
        info.title("Ventana de experimento seleccionado")
        global folder
        global cargarImagen
        global text_Experimento
        global descripcion_Experimento
        global ruta

        if (planta=="HELI2DOF"):
            #Titulo de la Ventana 
            titulo=Label(info, text="Helicóptero con dos grados de libertad", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
            titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

            #Ilustración del experimento
            abrirImagen = Image.open("Heli2DOF2.jpg")
            abrirImagen = abrirImagen.resize((300, 300), Image.ANTIALIAS)
            cargarImagen = ImageTk.PhotoImage(abrirImagen)

            #Descripción del experimento
            archivo="Heli2DOF.txt"
            abrir_archivo=open(archivo, "r")
            text_Experimento=abrir_archivo.read()
            abrir_archivo.close()

            #Abrir carpeta
            ruta="Experimentos\HELI2DOF"
            


        if (planta=="PAMH"):
            #Titulo de la Ventana 
            titulo=Label(info, text="Péndulo amortiguado a hélice", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
            titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

            #Ilustración del experimento
            abrirImagen = Image.open("Pamh.jpg")
            abrirImagen = abrirImagen.resize((300, 300), Image.ANTIALIAS)
            cargarImagen = ImageTk.PhotoImage(abrirImagen)

            #Descripción del experimento
            archivo="PAMH.txt"
            abrir_archivo=open(archivo, "r")
            text_Experimento=abrir_archivo.read()
            abrir_archivo.close()

            #Abrir carpeta
            ruta="Experimentos\PAMH"

        if (planta=="BALL&BEAM"):
            #Titulo de la Ventana 
            titulo=Label(info, text="Ball and Beam", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
            titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

            #Ilustración del experimento
            abrirImagen = Image.open("Ball&Beam.jpg")
            abrirImagen = abrirImagen.resize((300, 300), Image.ANTIALIAS)
            cargarImagen = ImageTk.PhotoImage(abrirImagen)

            #Descripción del experimento
            archivo="BALL&BEAM.txt"
            abrir_archivo=open(archivo, "r")
            text_Experimento=abrir_archivo.read()
            abrir_archivo.close()

            #Abrir carpeta
            ruta="Experimentos\BALL&BEAM"

        if (planta=="GRUA"):
            #Titulo de la Ventana 
            titulo=Label(info, text="Grúa", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
            titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

            #Ilustración del experimento
            abrirImagen = Image.open("Grua.jpg")
            abrirImagen = abrirImagen.resize((450, 300), Image.ANTIALIAS)
            cargarImagen = ImageTk.PhotoImage(abrirImagen)

            #Descripción del experimento
            archivo="GRUA.txt"
            abrir_archivo=open(archivo, "r")
            text_Experimento=abrir_archivo.read()
            abrir_archivo.close()

            #Abrir carpeta
            ruta="Experimentos\GRUA"

        if planta=="MOTORCD":
            #Titulo de la Ventana 
            titulo=Label(info, text="Motor CD", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
            titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

            #Ilustración del experimento
            abrirImagen = Image.open("MotorCD.jpg")
            abrirImagen = abrirImagen.resize((300, 300), Image.ANTIALIAS)
            cargarImagen = ImageTk.PhotoImage(abrirImagen)

            #Descripción del experimento
            archivo="MotorCD.txt"
            abrir_archivo=open(archivo, "r")
            text_Experimento=abrir_archivo.read()
            abrir_archivo.close()

            #Abrir carpeta
            ruta="Experimentos\MOTORCD"

        if planta=="Otro":
            #Titulo de la Ventana 
            titulo=Label(info, text="Otro experimento", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
            titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

            #Ilustración del experimento
            abrirImagen = Image.open("Otro.png")
            abrirImagen = abrirImagen.resize((300, 300), Image.ANTIALIAS)
            cargarImagen = ImageTk.PhotoImage(abrirImagen)

            #Descripción del experimento
            archivo="Otro.txt"
            abrir_archivo=open(archivo, "r")
            text_Experimento=abrir_archivo.read()
            abrir_archivo.close()

            #Abrir carpeta
            ruta="Experimentos"


        ilustracion=Label(info, image=cargarImagen)
        ilustracion.grid_propagate(0)
        ilustracion.grid(row=1, column=0, sticky=W)#columnspan=2, sticky=W)
        

        #Botones
        frm_buttons = Frame(info, bg=tema_Principal.get())
        frm_buttons.grid(row = 1, column = 1)
            
        btn_iniciar = Button(frm_buttons, text = "Nuevo", command=estructura, width=15, bg=tema_Secundario.get(), fg=Letras.get())
        btn_iniciar.grid(row = 0, column = 0, pady = 20)

        btn_abrir = Button(frm_buttons, text = "Abrir", command=openFile, width=15, bg=tema_Secundario.get(), fg=Letras.get())
        btn_abrir.grid(row=1, column=0, pady = 20)#, pady=10, padx=10)

        btn_editar = Button(frm_buttons, text = "Editar", command=editarDescripcion ,width=15, bg=tema_Secundario.get(), fg=Letras.get())
        btn_editar.grid(row = 2, column = 0, pady = 20)#, pady = 10, padx = 10)

        btn_cerrar = Button(frm_buttons, text = "Cerrar", command = info.destroy, width=15, bg=tema_Secundario.get(), fg=Letras.get())
        btn_cerrar.grid(row = 3, column = 0, pady = 20)#, pady = 10, padx = 10)

        if username.get()=="estudiante":
            btn_iniciar.config(state=DISABLED)
            btn_editar.config(state=DISABLED)

        #Información del experimento
        frm_description = LabelFrame(info, text = "Descripción", width = 600, bg=tema_Principal.get(), fg=tema_Secundario.get())
        frm_description.grid(row =2, column = 0, columnspan = 2)
        frm_description.columnconfigure(0, weight=1)

        descripcion_Experimento=Text(frm_description, width=600, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        descripcion_Experimento.grid(row=0, column=0, sticky="ns")

        descripcion_Experimento.insert(tk.END, text_Experimento)
        descripcion_Experimento.config(state=DISABLED)

    def about_PASCAL():
        aboutIt = Toplevel()
        aboutIt.columnconfigure(0, weight=1)
        aboutIt.rowconfigure(0, weight=1)
        
        #Nombre de la ventana
        aboutIt.title("Ventana acerca de PASCAL")
        abrir_ABOUT = Image.open("aboutPASCAL.png")
        global img_about
        img_about = ImageTk.PhotoImage(abrir_ABOUT)

        sobre = Label(aboutIt, image=img_about)
        sobre.grid(row=0, column=0)

        aboutIt.resizable(width=False, height=False)


    frm_principal.destroy()

    global frm_experimentos        
    frm_experimentos= Frame(root, bg=tema_Principal.get())
    frm_experimentos.pack(fill="both", expand=True)
    frm_experimentos.columnconfigure(0, weight=1)
    frm_experimentos.columnconfigure(1, weight=1)
    frm_experimentos.columnconfigure(2, weight=1)
    frm_experimentos.columnconfigure(3, weight=1)

    mensaje=Label(frm_experimentos, text="Pantalla de selección de experimento", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=4, sticky="ew")

    #Barra de Menú
    frm_barra=Frame(frm_experimentos, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0,64))

    frm_barra.columnconfigure(0, weight=1)

    global status_bar
    status_bar=Label(frm_barra, text="", font=("TkDefaultFont", 10, "bold"), anchor=W, fg="#003366")
    status_bar.grid(row=0, column=0, sticky="ew")

    #Botones de la barra de Menú
    back = Button(frm_barra, image=img_ATRAS, borderwidth=0, command=experimentstoprincipal)
    back.grid(row = 0, column = 1, sticky=tk.E, padx=10)
    back.bind("<Enter>", inButtonBack)
    back.bind("<Leave>", outButton)

    revert = Button(frm_barra, image=img_REVERTIR, borderwidth=0, state=DISABLED)
    revert.grid(row = 0, column = 2, sticky=tk.E, padx=10)
    revert.bind("<Enter>", inButtonRevert)
    revert.bind("<Leave>", outButton)

    redo = Button(frm_barra, image=img_REHACER, borderwidth=0, state=DISABLED)
    redo.grid(row = 0, column = 3, sticky=tk.E, padx=10)
    redo.bind("<Enter>", inButtonRedo)
    redo.bind("<Leave>", outButton)

    information = Button(frm_barra, image=img_INFORMA, borderwidth=0, command=info_EXPERIMENTS)
    information.grid(row = 0, column = 4, sticky=tk.E, padx=10)
    information.bind("<Enter>", inButtonInformation)
    information.bind("<Leave>", outButton)

    erase = Button(frm_barra, image=img_BORRAR, borderwidth=0, state=DISABLED)
    erase.grid(row = 0, column = 5, sticky=tk.E, padx=10)
    erase.bind("<Enter>", inButtonErase)
    erase.bind("<Leave>", outButton)

    simulate = Button(frm_barra, image=img_SIM, borderwidth=0, state=DISABLED)
    simulate.grid(row = 0, column = 6, sticky=tk.E, padx=10)
    simulate.bind("<Enter>", inButtonSimulate)
    simulate.bind("<Leave>", outButton)

    transfer = Button(frm_barra, image=img_TRANSFER, borderwidth=0, state=DISABLED)
    transfer.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer.bind("<Enter>", inButtonTransfer)
    transfer.bind("<Leave>", outButton)

    running = Button(frm_barra, image=img_RUN, borderwidth=0, state=DISABLED)
    running.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running.bind("<Enter>", inButtonRun)
    running.bind("<Leave>", outButton)

    stopping = Button(frm_barra, image=img_STOP, borderwidth=0, state=DISABLED)
    stopping.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping.bind("<Enter>", inButtonStop)
    stopping.bind("<Leave>", outButton)

    about = Button(frm_barra, image=img_ACERCA, borderwidth=0, command=about_PASCAL)
    about.grid(row = 0, column = 10, sticky=tk.E, padx=10)
    about.bind("<Enter>", inButtonAcerca)
    about.bind("<Leave>", outButton)



    #Heli2DOF
    raw_heli = Image.open("Heli2DOF2.jpg")
    raw_heli = raw_heli.resize((150, 150), Image.ANTIALIAS)
    global img_heli
    img_heli = ImageTk.PhotoImage(raw_heli)

    # heli_pic = Label(frm_experimentos, image = img_heli)
    # heli_pic.grid(row = 2, column = 0)

    heli_pic = Button(frm_experimentos, image = img_heli, command=lambda:systeminfo("HELI2DOF"))
    heli_pic.grid(row = 2, column = 0)

    heli_exp = Button(frm_experimentos, text= "Heli2DOF", font=("TkDefaultFont", 10, "bold"), command=lambda:systeminfo("HELI2DOF"), bg=tema_Secundario.get(), fg=Letras.get())
    heli_exp.grid(row = 3, column = 0, pady=(5,64))

            
    #PAMH
    raw_pamh = Image.open("Pamh.jpg")
    raw_pamh = raw_pamh.resize((150,150), Image.ANTIALIAS)
    global img_pamh
    img_pamh = ImageTk.PhotoImage(raw_pamh)

    # pamh_pic = Label(frm_experimentos, image = img_pamh)
    # pamh_pic.grid(row = 2, column = 1)

    pamh_pic = Button(frm_experimentos, image = img_pamh, command=lambda:systeminfo("PAMH"))
    pamh_pic.grid(row = 2, column = 1)

    pamh_exp=Button(frm_experimentos, text = "PAMH", font=("TkDefaultFont", 10, "bold"), command=lambda:systeminfo("PAMH"), bg=tema_Secundario.get(), fg=Letras.get())
    pamh_exp.grid(row = 3, column = 1, pady=(5,64))


    #Ball&Beam
    raw_bb = Image.open("Ball&Beam.jpg")
    raw_bb = raw_bb.resize((200,150), Image.ANTIALIAS)
    global img_bb
    img_bb = ImageTk.PhotoImage(raw_bb)

    # bb_pic = Label(frm_experimentos, image = img_bb)
    # bb_pic.grid(row = 2, column = 2)

    bb_pic = Button(frm_experimentos, image = img_bb, command=lambda:systeminfo("BALL&BEAM"))
    bb_pic.grid(row = 2, column = 2)
            
    bb_exp = Button(frm_experimentos, text = "Ball&Beam", font=("TkDefaultFont", 10, "bold"), command=lambda:systeminfo("BALL&BEAM"), bg=tema_Secundario.get(), fg=Letras.get())
    bb_exp.grid(row = 3, column = 2, pady=(5,64))


    #Grua
    raw_grua = Image.open("Grua.jpg")
    raw_grua = raw_grua.resize((200,150), Image.ANTIALIAS)
    global img_grua
    img_grua = ImageTk.PhotoImage(raw_grua)

    # grua_pic = Label(frm_experimentos, image = img_grua)
    # grua_pic.grid(row = 2, column = 3)

    grua_pic = Button(frm_experimentos, image = img_grua, command=lambda:systeminfo("GRUA"))
    grua_pic.grid(row = 2, column = 3)
            
    grua_exp = Button(frm_experimentos, text = "Grúa", font=("TkDefaultFont", 10, "bold"), command=lambda:systeminfo("GRUA"), bg=tema_Secundario.get(), fg=Letras.get())
    grua_exp.grid(row = 3, column = 3, pady=(5,64))


    #MotorCD
    raw_motor = Image.open("MotorCD.jpg")
    raw_motor = raw_motor.resize((150,150), Image.ANTIALIAS)
    global img_motor
    img_motor = ImageTk.PhotoImage(raw_motor)

    # motor_pic = Label(frm_experimentos, image = img_motor)
    # motor_pic.grid(row = 4, column = 0)

    motor_pic = Button(frm_experimentos, image = img_motor, command=lambda:systeminfo("MOTORCD"))
    motor_pic.grid(row = 4, column = 0)
            
    motor_exp = Button(frm_experimentos, text = "Motor CD", font=("TkDefaultFont", 10, "bold"), command=lambda:systeminfo("MOTORCD"), bg=tema_Secundario.get(), fg=Letras.get())
    motor_exp.grid(row = 5, column = 0, pady=(5,64))


    #Nuevos experimentos
    raw_otro = Image.open("Otro.png")
    raw_otro = raw_otro.resize((150,150), Image.ANTIALIAS)
    global img_otro
    img_otro = ImageTk.PhotoImage(raw_otro)

    # otro_pic = Label(frm_experimentos, image = img_otro, bg=tema_Principal.get())
    # otro_pic.grid(row = 4, column = 1)

    otro_pic = Button(frm_experimentos, image = img_otro, command=lambda:systeminfo("Otro"))
    otro_pic.grid(row = 4, column = 1)
            
    otro_exp = Button(frm_experimentos, text = "Otro", font=("TkDefaultFont", 10, "bold"), command=lambda:systeminfo("Otro"), bg=tema_Secundario.get(), fg=Letras.get())
    otro_exp.grid(row = 5, column = 1, pady=(5,64))


##########Función para la pantalla de estructura de experimento#########################################################
def estructura():

    global trigger
    #Función estructuratoexperimentos(): Una función para regresar a la pantalla de experimentos cuando se presiona el botón de ATRÁS en
    #la pantalla de la estructura de experimento. El frame frm_estructura debe destruirse para poder ser reemplazado por el frame
    #frm_experimentos
    def estructuratoexperimentos():
        frm_estructura.destroy()
        experiments()
    
    

    #Función guardarArchivo(): Una función para guardar un archivo (nuevo o existente) cuando el botón GUARDAR es presionado. Se tiene 
    # los siguientes casos:

    # 1. Cuando la variable "directorio" es "Laboratorio de Control Automático - Archivo Nuevo", se trata de un archivo nuevo. Al
    # presionar GUARDAR, se abre la ventana para nombrar el archivo nuevo a guardar con extensión xml en una ruta a escoger. La variable 
    # "nuevoDirectorio" va a tener como valor la ruta donde se guarde este archivo, y su valor será asignado a la variable "directorio".

    # 2. Cuando la variable "directorio" no es "Laboratorio de Control Automático - Archivo Nuevo", se trata de un archivo que se ha 
    #abierto, y la variable "directorio" tiene asignada la ruta del archivo. Al presionar GUARDAR, se guardan los cambios sin alterar
    #el nombre o la ruta del archivo, por lo que la variable "directorio" no cambia.

    #Si la variable nuevoDirectorio tiene un valor, significa que el archivo se ha guardado previamente, por lo que al presionar
    #GUARDAR se guardan los cambios realizados. Una vez se ha guardado, si se presiona CERRAR, la aplicación se cerrara con la función
    # root.destroy(). Por otro lado, si el archivo no se ha guardado y hay cambios, se ejecuta la función cerrarAplicación() para desplegar
    # una ventana que pregunta si se desea guardar el archivo antes de salir.

    def guardarArchivo(event, opcion=False):
        global directorio
        
        if directorio == "Laboratorio de Control Automático - Archivo Nuevo":
            nuevoDirectorio = filedialog.asksaveasfilename(initialfile="Untitled-1", defaultextension=".xml")
        else:
            nuevoDirectorio = directorio

        if nuevoDirectorio != "":
            GuardarArchivo.NuevoArchivo(tupla_listas, nuevoDirectorio,
                                        variable_nombre_dispositivo,
                                        variable_tiempo_muestreo,
                                        variable_numero_muestras,
                                        variable_velocidad)
            directorio = nuevoDirectorio

            status_bar.configure(text=directorio)
            return 0

        if opcion:

            if nuevoDirectorio == "":
                cerrarAplicacion()

            else:
                root.destroy()

        return 1



    #Función guardarArchivoComo(): Independientemente de si el archivo se ha guardado antes o es nuevo, al presionar click derecho en el
    #botón GUARDAR, se abre la ventana para guardar el archivo como. La variable "nuevoDirectorio" almacenará la ruta donde se guarde el 
    #archivo, y le asignará ese valor a la variable "directorio"
    def guardarArchivoComo(event):
        global directorio
        nuevoDirectorio = filedialog.asksaveasfilename(initialfile="Untitled-1", defaultextension=".xml")
        
        if nuevoDirectorio != "":
            GuardarArchivo.NuevoArchivo(tupla_listas, directorio,
                                        variable_nombre_dispositivo,
                                        variable_tiempo_muestreo,
                                        variable_numero_muestras,
                                        variable_velocidad)
            directorio = nuevoDirectorio
            status_bar.configure(text=directorio)



    #Funcion cerrarAplicacion(): Es una función que se ejecuta cuando se va a cerrar la ventana de la aplicación y se ha detectado cambios sin 
    # guardar en el archivo con el que se trabaja. La función hace que se despliegue una ventana con un mensaje preguntando si se desea guardar
    # los cambios efectuados en el archivo actual. Si el usuario responde que si, se ejecuta la función guardarArchivo(), y si responde que no,
    # se ejecuta la función root.destroy para salir de la aplicación
    def cerrarAplicacion():
        global cambiosArchivo
        if cambiosArchivo is True:
            opcion = messagebox.askyesnocancel("Laboratorio de Control Automático | TEC", "¿Desea guardar los cambios?")
            if opcion is True:
                a = guardarArchivo(None, True)
                if a == 0:
                    root.destroy()
            if opcion is False:
                root.destroy()

        else:
            root.destroy()



    #Función abrirArchivo(): Una función para abrir un archivo creado previamente. Al presionar ABRIR, si hay cambios realizados en un archivo 
    #abierto con anterioridad, se despliega una ventana para preguntar si se desean guardar los cambios en el archivo actual. Si el usuario
    #selecciona "No", se pierden los cambios efectuados y aparece la ventana para seleccionar el archivo a abrir. La variable "nuevoDirectorio"
    # se actualiza a la ruta del archivo que se abre, y le asigna ese valor a la variable "directorio" 
    def abrirArchivo(event):

        global cambiosArchivo
        global directorio
        if cambiosArchivo:

            opcion = messagebox.askyesnocancel("Laboratorio de Control Automático | TEC", "¿Desea guardar los cambios?")

            if opcion is None:
                return None

            if opcion is True:
                a = guardarArchivo(None, False)
                if a == 1:
                    return None

        cambiosArchivo = True

        nuevoDirectorio = filedialog.askopenfilename(filetypes=[("XML", "*.xml")])

        if nuevoDirectorio != "":

            ventana_principal.delete(ALL)
            for i in range(2, len(tupla_listas)):

                tupla_listas[i].vaciarLista()

            AbrirArchivo.NuevoArchivo(tupla_listas, nuevoDirectorio)
            directorio = nuevoDirectorio
            status_bar.configure(text=directorio)


    def abrirDesdeSystem():
        global directorio
        global trigger
        nuevoDirectorio = filedialog.askopenfilename(initialdir=ruta, filetypes=[("XML", "*.xml")])

        if not nuevoDirectorio:
            directorio = "Laboratorio de Control Automático - Archivo Nuevo"

        else:
            AbrirArchivo.NuevoArchivo(tupla_listas, nuevoDirectorio)
            directorio = nuevoDirectorio
            #trigger=0
        
        status_bar.configure(text=directorio)
        trigger=0



    #Función configuracionArchivo(): Esta función se ejecuta al presionar el botón de CONFIGURACIÓN. Lo que hace es abrir una ventana
    #auxiliar para configurar la comunicación entre la app y la placa de hardware del laboratorio, la velocidad de la comunicación, el
    #tiempo de muestreo del experimento y el número de muestras que se desean tomar. 
    def configuracionArchivo(event):

        global ventanaCerrada
        if ventanaCerrada:
            ventanaCerrada = False
            global windowConfig
            windowConfig = Toplevel()
            windowConfig.resizable(False, False)
            windowConfig.title("Configuración")

            # -------------------- FRAME 1 --------------------

            frame1 = Frame(windowConfig, bg="#2C2C2C")
            frame2 = Frame(windowConfig, bg="white")
            frame3 = Frame(windowConfig, bg="white")

            imagen_ventana = PhotoImage(file="Icono_Configuracion.png")
            imagen_ventana_label = Label(frame1, image=imagen_ventana, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=10)

            imagen_ventana_label.image = imagen_ventana
            imagen_ventana_label.pack(side=LEFT, padx=10)

            Label(frame1, text="Configuración", bg="#2C2C2C", fg="White", font=("Arial Rounded MT", -20)).pack(side=LEFT)

            # -------------------- FRAME 2 --------------------

            Label(frame2, text="Comunicación Serie", font=("Arial Rounded MT Bold", -18)) \
                .grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)
            

            global variable_nombre_dispositivo
            global variable_velocidad
            global variable_tiempo_muestreo
            global variable_numero_muestras

            global nombre_dispositivo 
            nombre_dispositivo = StringVar()
            global velocidad
            velocidad = IntVar()
            global tiempoMuestreo
            tiempoMuestreo = StringVar()
            global numeroMuestras
            numeroMuestras = StringVar()

            if variable_nombre_dispositivo is None:
                nombre_dispositivo.set("")
            else:
                nombre_dispositivo.set(str(variable_nombre_dispositivo))

            if variable_velocidad is None:
                velocidad.set(115200)
            else:
                velocidad.set(variable_velocidad)

            if variable_nombre_dispositivo is None:
                tiempoMuestreo.set("20")
            else:
                tiempoMuestreo.set(str(variable_tiempo_muestreo))

            if variable_numero_muestras is None:
                numeroMuestras.set("1000")
            else:
                numeroMuestras.set(str(variable_numero_muestras))

            Label(frame2, text="Puerto:").grid(row=1, column=0, sticky=W, padx=(20,0), pady=(0,0))
            ttk.Entry(frame2, width=30, textvariable=nombre_dispositivo)\
                .grid(row=1, column=1, sticky=W, padx=(0,20), pady=(0,0))

            Label(frame2, text="Velocidad:").grid(row=2, column=0, sticky=W, padx=(20, 0), pady=(0, 0))
            ttk.Entry(frame2, width=30, textvariable=velocidad) \
                .grid(row=2, column=1, sticky=W, padx=(0, 20), pady=(0, 0))

            Label(frame2, text="Simulación", font=("Arial Rounded MT Bold", -18)) \
                .grid(row=3, column=0, sticky=W, columnspan=2, padx=10, pady=10)

            Label(frame2, text="Tiempo de muestreo (ms):").grid(row=4, column=0, sticky=W, padx=(20, 0), pady=(0, 0))
            ttk.Entry(frame2, width=30, textvariable=tiempoMuestreo) \
                .grid(row=4, column=1, sticky=W, padx=(0, 20), pady=(0, 0))

            Label(frame2, text="Número de muestras:").grid(row=5, column=0, sticky=W, padx=(20, 0), pady=(0, 20))
            ttk.Entry(frame2, width=30, textvariable=numeroMuestras) \
                .grid(row=5, column=1, sticky=W, padx=(0, 20), pady=(0, 20))

            # -------------------- FRAME 3 --------------------
            ttk.Button(frame3, text="Aceptar", command=lambda: cerrarVentanaConfiguracion("Aceptar")) \
                .pack(side=RIGHT, padx=(10, 20), pady=(0, 10))
            ttk.Button(frame3, text="Cancelar", command=lambda: cerrarVentanaConfiguracion("Cancelar")) \
                .pack(side=RIGHT, pady=(0, 10))

            frame1.pack(side=TOP, fill=BOTH)
            frame2.pack(side=TOP, fill=BOTH)
            frame3.pack(side=TOP, fill=BOTH)

            windowConfig.protocol("WM_DELETE_WINDOW", cerrarVentanaConfiguracion)

            windowConfig.withdraw()
            windowConfig.update_idletasks()
            x = (windowConfig.winfo_screenwidth() - windowConfig.winfo_reqwidth()) / 2
            y = (windowConfig.winfo_screenheight() - windowConfig.winfo_reqheight()) / 2
            windowConfig.geometry("+%d+%d" % (x, y))

            windowConfig.deiconify()

            # Color
            s = ttk.Style()
            s.configure('Style.TRadiobutton', background="White", foreground='black')
            s1 = ttk.Style()
            s1.configure('Style2.TCheckbutton', background="White", foreground='black')
            for wid in frame2.winfo_children():
                if wid.winfo_class() == 'Label':
                    wid.configure(bg="white")
                if wid.winfo_class() == 'TRadiobutton':
                    wid.configure(style='Style.TRadiobutton')
                if wid.winfo_class() == 'Message':
                    wid.configure(bg='white')
                if wid.winfo_class() == 'TCheckbutton':
                    wid.configure(style='Style2.TCheckbutton')

        else:
            windowConfig.lift()


    #Función cerrarVentanaConfiguracion(): La ventana de configuración tiene dos opciones para salir de ella. Si se selecciona "Aceptar",
    #se guardan los valores ingresados para los parametros de dispositivo, velocidad, tiempo de muestreo y numero de muestras. Por otro lado,
    #si se selecciona "Cancelar", se cierra la ventana con los valores predeterminados o previamente configurados para los parámetros
    #mencionados. 
    def cerrarVentanaConfiguracion(opcion="cancelar"):
        global ventanaCerrada
        global nombre_dispositivo
        global velocidad
        global tiempoMuestreo
        global numeroMuestras

        global variable_velocidad
        global variable_tiempo_muestreo
        global variable_numero_muestras
        global variable_nombre_dispositivo

        if opcion == "Aceptar":

            try:

                velocidad = int(velocidad.get())
                velocidad = abs(velocidad)

                if velocidad == 0:
                    velocidad = 9600

                ts = eval(tiempoMuestreo.get())

                if type(ts) is not int and type(ts) is not float:
                    raise Exception

                muestras = eval(numeroMuestras.get())

                if type(muestras) is not int and type(muestras) is not float:
                    raise Exception

                if muestras > 5000:
                    muestras = 5000

                if muestras < -5000:
                    muestras = 5000

                variable_velocidad = velocidad
                variable_tiempo_muestreo = abs(int(ts))
                variable_numero_muestras = abs(int(muestras))

                variable_nombre_dispositivo = nombre_dispositivo.get()

                ventanaCerrada = True
                windowConfig.destroy()

            except Exception:
                messagebox.showerror("Error", "Parámetro Inválido")

        else:
            ventanaCerrada = True
            windowConfig.destroy()


    #Función coordenadasIcono(): Una función que registra las pocisicones del icono luego de haber sido presionado con click izquierdo. 
    #Mientras el icono es desplazado, la función arrastrarIcono se esta ejecutando.
    def coordenadasIcono(event, icono):
        global posicion_x
        global posicion_y
        global px
        global py
        global iconoNuevo
        global imagen

        dx = event.x
        dy = event.y

        posicion_x = frm_workspace.winfo_pointerx() - frm_workspace.winfo_rootx() - dx
        posicion_y = frm_workspace.winfo_pointery() - frm_workspace.winfo_rooty() - dy

        if icono == "ADC": imagen = PhotoImage(file="ADCn.png")
        if icono == "PID": imagen = PhotoImage(file="PIDn.png")
        if icono == "PWM": imagen = PhotoImage(file="PWMn.png")
        if icono == "RE": imagen = PhotoImage(file="REn.png")
        if icono == "CTE": imagen = PhotoImage(file="CTEn.png")
        if icono == "FT": imagen = PhotoImage(file="FTn.png")
        if icono == "SAT": imagen = PhotoImage(file="SATn.png")
        if icono == "QDEC": imagen = PhotoImage(file="QDECn.png")
        if icono == "DAC": imagen = PhotoImage(file="DACn.png")
        if icono == "FLT": imagen = PhotoImage(file="FLTn.png")
        if icono == "DER": imagen = PhotoImage(file="DERn.png")
        if icono == "SUM": imagen = PhotoImage(file="SUMn.png")
        if icono == "REST": imagen = PhotoImage(file="RESTn.png")
        if icono == "SCOPE": imagen = PhotoImage(file="SCOPEn.png")
        if icono == "STEP": imagen = PhotoImage(file="STEPn.png")
        if icono == "TRAPECIO": imagen = PhotoImage(file="TRAPECIOn.png")
        if icono == "SALP": imagen = PhotoImage(file="SALPn.png")
        if icono == "ENTP": imagen = PhotoImage(file="ENTPn.png")

        
        px = posicion_x+dx-185
        py = posicion_y+dy#-35
        iconoNuevo = ventana_principal.create_image(px, py, image=imagen)

    
    #Función arrastarIcono(): Una función que va calculando la nueva posición de iconoNuevo mientras es desplazado en ventana_principal.
    # 
    def arrastrarIcono(event):
        global iconoNuevo
        global px
        global py
        global imagen
        
        x = ventana_principal.winfo_pointerx() - ventana_principal.winfo_rootx()
        y = ventana_principal.winfo_pointery() - ventana_principal.winfo_rooty()

        ventana_principal.move(iconoNuevo, x-px, y-py)
        px = x
        py = y
    

    #Función nuevoModulo(): Una función que permite agregar más modulos a ventana_prinicpal, y también limita la cantidad de cada tipo de
    #modulo que puede ser colocado en este espacio de trabajo. 
    def nuevoModulo(event, lista):

        global iconoNuevo
        global posicion_x
        global posicion_y
        global cambiosArchivo
        global imagen

        ventana_principal.delete(iconoNuevo)

        tamano_ventana_x = ventana_principal.winfo_width() - 20
        tamano_ventana_y = ventana_principal.winfo_height() - 20

        coordenada_x = event.x - (185-posicion_x)
        coordenada_y = event.y + (posicion_y)# - 35)

        if tamano_ventana_x > coordenada_x > 20 and tamano_ventana_y > coordenada_y > 20:
            cambiosArchivo = True

            if lista == lista_ADC:
                if lista.tamano() < 2:  # Máximo número de ADC
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_DAC:
                if lista.tamano() < 2:  # Máximo número de DAC
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_PWM:
                if lista.tamano() < 3:  # Máximo número de PWM
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_QDEC:
                if lista.tamano() < 3:  # Máximo número de QDEC
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_PID:
                if lista.tamano() < 4:  # Máximo número de PID
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_RE:
                if lista.tamano() < 1:  # Máximo número de RE
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_FT:
                if lista.tamano() < 4:  # Máximo número de FT
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_FLT:
                if lista.tamano() < 2:  # Máximo número de FT
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_DER:
                if lista.tamano() < 2:  # Máximo número de DER
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_SUM:
                if lista.tamano() < 3:  # Máximo número de SUM
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            elif lista == lista_REST:
                if lista.tamano() < 3:  # Máximo número de REST
                    lista.agregar(tupla_listas, coordenada_x, coordenada_y)

            else:
                lista.agregar(tupla_listas, coordenada_x, coordenada_y)



    def cambiarIconos(event):
        global pagina

        if pagina:

            icono_1 = PhotoImage(file="SCOPE_sideBar.png")
            icon_1.configure(image=icono_1)
            icon_1.image = icono_1
            icon_1.unbind("<Button-1>")
            icon_1.unbind("<B1-Motion>")
            icon_1.unbind("<ButtonRelease-1>")
            icon_1.bind("<Button-1>", lambda event: coordenadasIcono(event, "SCOPE"))
            icon_1.bind("<B1-Motion>", arrastrarIcono)
            icon_1.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_SCOPE))

            icono_2 = PhotoImage(file="STEP_sideBar.png")
            icon_2.configure(image=icono_2)
            icon_2.image = icono_2
            icon_2.unbind("<Button-1>")
            icon_2.unbind("<B1-Motion>")
            icon_2.unbind("<ButtonRelease-1>")
            icon_2.bind("<Button-1>", lambda event: coordenadasIcono(event, "STEP"))
            icon_2.bind("<B1-Motion>", arrastrarIcono)
            icon_2.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_STEP))

            icono_3 = PhotoImage(file="TRAPECIO_sideBar.png")
            icon_3.configure(image=icono_3)
            icon_3.image = icono_3
            icon_3.unbind("<Button-1>")
            icon_3.unbind("<B1-Motion>")
            icon_3.unbind("<ButtonRelease-1>")
            icon_3.bind("<Button-1>", lambda event: coordenadasIcono(event, "TRAPECIO"))
            icon_3.bind("<B1-Motion>", arrastrarIcono)
            icon_3.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_TRAPECIO))

            icono_4 = PhotoImage(file="DER_sideBar.png")
            icon_4.configure(image=icono_4)
            icon_4.image = icono_4
            icon_4.unbind("<Button-1>")
            icon_4.unbind("<B1-Motion>")
            icon_4.unbind("<ButtonRelease-1>")
            icon_4.bind("<Button-1>", lambda event: coordenadasIcono(event, "DER"))
            icon_4.bind("<B1-Motion>", arrastrarIcono)
            icon_4.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_DER))

            icono_5 = PhotoImage(file="SUM_sideBar.png")
            icon_5.configure(image=icono_5)
            icon_5.image = icono_5
            icon_5.unbind("<Button-1>")
            icon_5.unbind("<B1-Motion>")
            icon_5.unbind("<ButtonRelease-1>")
            icon_5.bind("<Button-1>", lambda event: coordenadasIcono(event, "SUM"))
            icon_5.bind("<B1-Motion>", arrastrarIcono)
            icon_5.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_SUM))

            icono_6 = PhotoImage(file="REST_sideBar.png")
            icon_6.configure(image=icono_6)
            icon_6.image = icono_6
            icon_6.unbind("<Button-1>")
            icon_6.unbind("<B1-Motion>")
            icon_6.unbind("<ButtonRelease-1>")
            icon_6.bind("<Button-1>", lambda event: coordenadasIcono(event, "REST"))
            icon_6.bind("<B1-Motion>", arrastrarIcono)
            icon_6.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_REST))

            icono_7 = PhotoImage(file="Fondo.png")
            icon_7.configure(image=icono_7, cursor='arrow')
            icon_7.image = icono_7
            icon_7.unbind("<Button-1>")
            icon_7.unbind("<B1-Motion>")
            icon_7.unbind("<ButtonRelease-1>")

            icono_8 = PhotoImage(file="Fondo.png")
            icon_8.configure(image=icono_8, cursor='arrow')
            icon_8.image = icono_8
            icon_8.unbind("<Button-1>")
            icon_8.unbind("<B1-Motion>")
            icon_8.unbind("<ButtonRelease-1>")

            icono_9 = PhotoImage(file="Fondo.png")
            icon_9.configure(image=icono_9, cursor='arrow')
            icon_9.image = icono_9
            icon_9.unbind("<Button-1>")
            icon_9.unbind("<B1-Motion>")
            icon_9.unbind("<ButtonRelease-1>")

            icono_10 = PhotoImage(file="Fondo.png")
            icon_10.configure(image=icono_10, cursor='arrow')
            icon_10.image = icono_10
            icon_10.unbind("<Button-1>")
            icon_10.unbind("<B1-Motion>")
            icon_10.unbind("<ButtonRelease-1>")

        if not pagina:

            icono_1 = PhotoImage(file="ADC_sideBar.png")
            icon_1.configure(image=icono_1)
            icon_1.image = icono_1
            icon_1.unbind("<Button-1>")
            icon_1.unbind("<B1-Motion>")
            icon_1.unbind("<ButtonRelease-1>")
            icon_1.bind("<Button-1>", lambda event: coordenadasIcono(event, "ADC"))
            icon_1.bind("<B1-Motion>", arrastrarIcono)
            icon_1.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_ADC))

            icono_2 = PhotoImage(file="PID_sideBar.png")
            icon_2.configure(image=icono_2)
            icon_2.image = icono_2
            icon_2.unbind("<Button-1>")
            icon_2.unbind("<B1-Motion>")
            icon_2.unbind("<ButtonRelease-1>")
            icon_2.bind("<Button-1>", lambda event: coordenadasIcono(event, "PID"))
            icon_2.bind("<B1-Motion>", arrastrarIcono)
            icon_2.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_PID))

            icono_3 = PhotoImage(file="PWM_sideBar.png")
            icon_3.configure(image=icono_3)
            icon_3.image = icono_3
            icon_3.unbind("<Button-1>")
            icon_3.unbind("<B1-Motion>")
            icon_3.unbind("<ButtonRelease-1>")
            icon_3.bind("<Button-1>", lambda event: coordenadasIcono(event, "PWM"))
            icon_3.bind("<B1-Motion>", arrastrarIcono)
            icon_3.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_PWM))

            icono_4 = PhotoImage(file="RE_sideBar.png")
            icon_4.configure(image=icono_4)
            icon_4.image = icono_4
            icon_4.unbind("<Button-1>")
            icon_4.unbind("<B1-Motion>")
            icon_4.unbind("<ButtonRelease-1>")
            icon_4.bind("<Button-1>", lambda event: coordenadasIcono(event, "RE"))
            icon_4.bind("<B1-Motion>", arrastrarIcono)
            icon_4.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_RE))

            icono_5 = PhotoImage(file="CTE_sideBar.png")
            icon_5.configure(image=icono_5)
            icon_5.image = icono_5
            icon_5.unbind("<Button-1>")
            icon_5.unbind("<B1-Motion>")
            icon_5.unbind("<ButtonRelease-1>")
            icon_5.bind("<Button-1>", lambda event: coordenadasIcono(event, "CTE"))
            icon_5.bind("<B1-Motion>", arrastrarIcono)
            icon_5.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_CTE))

            icono_6 = PhotoImage(file="FT_sideBar.png")
            icon_6.configure(image=icono_6)
            icon_6.image = icono_6
            icon_6.unbind("<Button-1>")
            icon_6.unbind("<B1-Motion>")
            icon_6.unbind("<ButtonRelease-1>")
            icon_6.bind("<Button-1>", lambda event: coordenadasIcono(event, "FT"))
            icon_6.bind("<B1-Motion>", arrastrarIcono)
            icon_6.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_FT))

            icono_7 = PhotoImage(file="SAT_sideBar.png")
            icon_7.configure(image=icono_7)
            icon_7.image = icono_7
            icon_7.unbind("<Button-1>")
            icon_7.unbind("<B1-Motion>")
            icon_7.unbind("<ButtonRelease-1>")
            icon_7.bind("<Button-1>", lambda event: coordenadasIcono(event, "SAT"))
            icon_7.bind("<B1-Motion>", arrastrarIcono)
            icon_7.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_SAT))

            icono_8 = PhotoImage(file="QDEC_sideBar.png")
            icon_8.configure(image=icono_8)
            icon_8.image = icono_8
            icon_8.unbind("<Button-1>")
            icon_8.unbind("<B1-Motion>")
            icon_8.unbind("<ButtonRelease-1>")
            icon_8.bind("<Button-1>", lambda event: coordenadasIcono(event, "QDEC"))
            icon_8.bind("<B1-Motion>", arrastrarIcono)
            icon_8.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_QDEC))

            icono_9 = PhotoImage(file="DAC_sideBar.png")
            icon_9.configure(image=icono_9)
            icon_9.image = icono_9
            icon_9.unbind("<Button-1>")
            icon_9.unbind("<B1-Motion>")
            icon_9.unbind("<ButtonRelease-1>")
            icon_9.bind("<Button-1>", lambda event: coordenadasIcono(event, "DAC"))
            icon_9.bind("<B1-Motion>", arrastrarIcono)
            icon_9.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_DAC))

            icono_10 = PhotoImage(file="FLT_sideBar.png")
            icon_10.configure(image=icono_10)
            icon_10.image = icono_10
            icon_10.unbind("<Button-1>")
            icon_10.unbind("<B1-Motion>")
            icon_10.unbind("<ButtonRelease-1>")
            icon_10.bind("<Button-1>", lambda event: coordenadasIcono(event, "FLT"))
            icon_10.bind("<B1-Motion>", arrastrarIcono)
            icon_10.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_FLT))

        pagina = not pagina


    def simulacion(event):

        global estadoBorrar

        if estadoBorrar:
            cancelar_Borrar(None)

        a = Simulacion.Simulacion()
        a.listas(tupla_listas)
        a.tiempoMuestreo(variable_tiempo_muestreo, variable_numero_muestras)
        a.inicioSimulacion()

    def borrar(event):
        global estadoBorrar
        global directorio
        if estadoBorrar:
            back.configure(state=ACTIVE)
            revert.configure(state=ACTIVE)
            redo.configure(state=ACTIVE)
            information.configure(state=ACTIVE)
            erase.configure(bg=tema_Barra.get())
            simulate.configure(state=ACTIVE)
            transfer.configure(state=ACTIVE)

            for i in range(2, len(tupla_listas)):
                actual = tupla_listas[i].cabeza

                while actual is not None:
                    actual.borrandoElemento = False
                    actual = actual.siguiente

        else:
            back.configure(state=DISABLED)
            revert.configure(state=DISABLED)
            redo.configure(state=DISABLED)
            information.configure(state=DISABLED)
            erase.configure(bg=tema_Principal.get())
            simulate.configure(state=DISABLED)
            transfer.configure(state=DISABLED)

            for i in range(2, len(tupla_listas)):
                actual = tupla_listas[i].cabeza

                while actual is not None:
                    actual.borrandoElemento = True
                    actual = actual.siguiente

        estadoBorrar = not estadoBorrar

    def cancelar_Borrar(event):
        global estadoBorrar

        back.configure(state=ACTIVE)
        revert.configure(state=ACTIVE)
        redo.configure(state=ACTIVE)
        information.configure(state=ACTIVE)
        erase.configure(bg=tema_Barra.get())
        simulate.configure(state=ACTIVE)
        transfer.configure(state=ACTIVE)
        estadoBorrar = False

        for i in range(2, len(tupla_listas)):
            actual = tupla_listas[i].cabeza

            while actual is not None:
                actual.borrandoElemento = False
                actual = actual.siguiente

    def comunicacion(event):
        global estadoBorrar
        global variable_nombre_dispositivo
        global variable_velocidad
        #global lectura
        global mensajeEnviado
        mensajeEnviado=""
        
        confirmacion=askyesno(title="Ventana de confirmación", message="La estructura de experimento está a punto de transmitirse. Asegúrese de que la planta se encuentra en reposo antes de proceder.\n¿Desea continuar?")
        if confirmacion:
            if estadoBorrar:
                cancelar_Borrar(None)

            if lista_Linea.tamano() > 0:

                a = Netlist.Netlist()
                a.listas(tupla_listas)
                a.generarNetlist()

                try:

                    archivo = "Protocolo_Comunicacion.txt"
                    puerto = variable_nombre_dispositivo
                    velocidad = variable_velocidad

                    with open(archivo) as fp:

                        trama = 'S'

                        dispositivo = serial.Serial(puerto, velocidad, timeout=0.1)
                        time.sleep(2)


                        while trama:

                            dispositivo.write(trama.strip().encode())

                            lectura = dispositivo.readline()
                            

                            if lectura:

                                lectura = lectura.rstrip('\n'.encode()).decode()
                                mensajeEnviado=mensajeEnviado + lectura

                                if lectura == "S":
                                    pass

                                elif lectura == "E":
                                    messagebox.showerror("Error", "Error en la comunicación")
                                    dispositivo.close()
                                    return None
                                elif lectura == "ERR":
                                    messagebox.showerror("Error", "Error en la comunicación")
                                    dispositivo.close()
                                    return None

                            trama = fp.readline()

                        dispositivo.close()
                        
                        messagebox.showinfo("", "La transmisión de datos ha sido exitosa")
                        expProgreso()

                except Exception:
                    messagebox.showerror("Error", "Error en la comunicación")

    #Información de la pantalla de configuración
    def info_STRUCT():
        help_STRUCT = Toplevel()
        help_STRUCT.columnconfigure(0, weight=1)
        help_STRUCT.rowconfigure(1, weight=1)
            
        #Nombre de la Ventana
        help_STRUCT.title("Ventana de información")

        #Titulo de la Ventana 
        titulo=Label(help_STRUCT, text="Información de la Pantalla de estructura de experimento", font=("TkDefaultFont", 15), bg=tema_Secundario.get())
        titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        #Información de la pantalla
        informacion_STRUCT = Text(help_STRUCT, width=500, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        informacion_STRUCT.grid(row=1, column=0, sticky="ns")

        text_STRUCT="""Está en la Pantalla de estructura de experimento.\nEn esta pantalla puede construir o abrir una estructura de experimento para utilizar en el experimento. Tiene a sus disposición las opciones para abrir y guardar un archivo con extensión xml, asi como configurar la comunicación para transmitir su experimento al sistema fisico o planta. Además, cuenta con varios módulos de control automático configurables para que se adapten al experimento que le interesa. \n\nPasos para transmitir un experimento a la planta: \n1.Construya o cargue la estructura del experimento que necesita.\n2.Ajuste los parámatros de los módulos de acuerdo a sus necesidades.\n3.Configure el puerto, velocidad, numero de muestras y tiempo de muestreo en el botón "CONFIGURACIÓN\n4.Presione el botón "TRANSMITIR" en la barra de herramientas y espere al mensaje del resultado de la transmisión.  \n\nLa barra de herramientas es la barra que se encuentra debajo del título de la pantalla. En el lado derecho de esta barra puede observar el nombre de los botones posicionados a la izquierda de la misma barra al colocar el puntero sobre ellos. Algunos de estos botones estan habilitados y deshabilitados dependiendo de la pantalla en la que se encuentre. Para el caso de la Pantalla de estructura de experimento, el estado de los botones es el siguiente:\n\nATRAS(Habilitado):Cuando es presionado, este botón permite regresar a la pantalla anterior.\n\nDESHACER(Deshabilitado):Cuando es presionado, este botón deshace la última acción realizada por el usuario.\n\nREHACER(Deshabilitado): Cuando es presionado, este botón rehace la última acción deshecha por el usuario.\n\nINFORMACIÓN(Habilitado):Cuando es presionado, este botón abre una ventana con información guía de la pantalla para el usuario.\n\nBORRAR(Habilitado): Cuando es presionado, este botón permite eliminar elementos de la estructura de un experimento.\n\nSIMULACIÓN(Habilitado):Cuando es presionado, este botón simula una estructura de experimento.\n\nTRANSMITIR(Habilitado): Cuando es presionado, este botón envía la información de la estructura de un experimento al hardware.\n\nRUN(Deshabilitado): Cuando es presionado, este botón inicia la ejecución de un experimento.\n\nSTOP(Deshabilitado): Cuando es presionado, este botón detiene la ejecución de un experimento.\n\nACERCA DE(Habilitado): Cuando es presionado, este botón despliega una ventana secundaria con información general de PASCAL. """
        informacion_STRUCT.insert(tk.END, text_STRUCT)
        informacion_STRUCT.config(state=DISABLED)

        scrollWindow=Scrollbar(help_STRUCT)
        scrollWindow.grid(row=1, column=1, sticky="ns")
        scrollWindow.config(command=informacion_STRUCT.yview)
        informacion_STRUCT.config(yscrollcommand=scrollWindow.set)
            
        help_STRUCT.geometry("500x500")
        help_STRUCT.resizable(width=False, height=False)

    def about_PASCAL():
        aboutIt = Toplevel()
        aboutIt.columnconfigure(0, weight=1)
        aboutIt.rowconfigure(0, weight=1)
        
        #Nombre de la ventana
        aboutIt.title("Ventana acerca de PASCAL")
        abrir_ABOUT = Image.open("aboutPASCAL.png")
        global img_about
        img_about = ImageTk.PhotoImage(abrir_ABOUT)

        sobre = Label(aboutIt, image=img_about)
        sobre.grid(row=0, column=0)

        aboutIt.resizable(width=False, height=False)


    #Pantalla de estructura de experimentos
    frm_experimentos.destroy()
    info.destroy()

    global frm_estructura       
    frm_estructura = Frame(root)#, bg=tema)
    frm_estructura.pack(fill="both", expand=True)
    frm_estructura.columnconfigure(0, weight=1)
    frm_estructura.columnconfigure(1, weight=1)
    frm_estructura.rowconfigure(2, weight=1)

    root.protocol("WM_DELETE_WINDOW", cerrarAplicacion)

    mensaje=Label(frm_estructura, text="Pantalla de Estructura de Experimento", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=2, sticky="ew")

                
    #Barra de Menú
    frm_barra=Frame(frm_estructura, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspan=2, sticky="ew")#, pady=(0,32))
    frm_barra.bind("<Button-1>", cancelar_Borrar)

    frm_barra.columnconfigure(0, weight=1)

    global status_bar
    status_bar=Label(frm_barra, text="Laboratorio de Control Automático - Archivo Nuevo", font=("TkDefaultFont", 10, "bold"), anchor=W, fg="#003366")
    status_bar.grid(row=0, column=0, sticky="ew")
    #status_bar.grid_propagate(False)
    status_bar.bind("<Button-1>", cancelar_Borrar)

    #Botones de la barra de Menú
    back = Button(frm_barra, image=img_ATRAS, borderwidth=0, command=estructuratoexperimentos)
    back.grid(row = 0, column = 1, sticky=tk.E, padx=10)
    back.bind("<Enter>", inButtonBack)
    back.bind("<Leave>", outButtonInStructureScreen)

    revert = Button(frm_barra, image=img_REVERTIR, borderwidth=0)
    revert.grid(row = 0, column = 2, sticky=tk.E, padx=10)
    revert.bind("<Enter>", inButtonRevert)
    revert.bind("<Leave>", outButtonInStructureScreen)

    redo = Button(frm_barra, image=img_REHACER, borderwidth=0)
    redo.grid(row = 0, column = 3, sticky=tk.E, padx=10)
    redo.bind("<Enter>", inButtonRedo)
    redo.bind("<Leave>", outButtonInStructureScreen)

    information = Button(frm_barra, image=img_INFORMA, borderwidth=0, command=info_STRUCT)
    information.grid(row = 0, column = 4, sticky=tk.E, padx=10)
    information.bind("<Enter>", inButtonInformation)
    information.bind("<Leave>", outButtonInStructureScreen)

    erase = Button(frm_barra, image=img_BORRAR, borderwidth=0)#, command=borrar)
    erase.grid(row = 0, column = 5, sticky=tk.E, padx=10)
    erase.bind("<ButtonRelease-1>", borrar)
    erase.bind("<Enter>", inButtonErase)
    erase.bind("<Leave>", outButtonInStructureScreen)

    simulate = Button(frm_barra, image=img_SIM, borderwidth=0)
    simulate.grid(row = 0, column = 6, sticky=tk.E, padx=10)
    simulate.bind("<Enter>", inButtonSimulate)
    simulate.bind("<Leave>", outButtonInStructureScreen)
    simulate.bind("<ButtonRelease-1>", simulacion)

    transfer = Button(frm_barra, image=img_TRANSFER, borderwidth=0)
    transfer.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer.bind("<Enter>", inButtonTransfer)
    transfer.bind("<Leave>", outButtonInStructureScreen)
    transfer.bind("<ButtonRelease-1>", comunicacion)

    running = Button(frm_barra, image=img_RUN, borderwidth=0, state=DISABLED)
    running.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running.bind("<Enter>", inButtonRun)
    running.bind("<Leave>", outButtonInStructureScreen)

    stopping = Button(frm_barra, image=img_STOP, borderwidth=0, state=DISABLED)
    stopping.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping.bind("<Enter>", inButtonStop)
    stopping.bind("<Leave>", outButtonInStructureScreen)

    about = Button(frm_barra, image=img_ACERCA, borderwidth=0, command=about_PASCAL)
    about.grid(row = 0, column = 10, sticky=tk.E, padx=10)
    about.bind("<Enter>", inButtonAcerca)
    about.bind("<Leave>", outButton)


    frm_workspace=Frame(frm_estructura)
    frm_workspace.grid(row=2, column=0, columnspan=2, sticky="nsew")
    frm_workspace.grid_propagate(False)

    sideBar = Frame(frm_workspace, width=185, height=500, bg="#2C2C2C")
    sideBar.pack(side=LEFT, fill=Y)
    sideBar.pack_propagate(False)  # Evita que el frame se ajuste al tamaño del label
    sideBar.grid_propagate(False)
    sideBar.bind("<Enter>", cancelar_Borrar)
   
    ventana_principal = Canvas(frm_workspace, width=900, height=620, bg="white")
    ventana_principal.pack(side=TOP, fill=BOTH, expand=True)


    # Creacion de listas de los modulos ---------------------
    lista_ADC = ListaADC()
    lista_PID = ListaPID()
    lista_PWM = ListaPWM()
    lista_RE = ListaRE()
    lista_CTE = ListaCTE()
    lista_FT = ListaFT()
    lista_SAT = ListaSAT()
    lista_QDEC = ListaQDEC()
    lista_Linea = ListaLinea()
    lista_ENTP = ListaENTP()
    lista_SALP = ListaSALP()
    lista_DAC = ListaDAC()
    lista_FLT = ListaFLT()
    lista_SCOPE = ListaSCOPE()
    lista_STEP = ListaSTEP()
    lista_TRAPECIO = ListaTRAPECIO()
    lista_DER = ListaDER()
    lista_SUM = ListaSUM()
    lista_REST = ListaREST()

    tupla_listas = (frm_estructura,              # [0]
        ventana_principal,    # [1]
        lista_Linea,          # [2]
        lista_ADC,            # [3]
        lista_PID,            # [4]
        lista_PWM,            # [5]
        lista_RE,             # [6]
        lista_CTE,            # [7]
        lista_FT,             # [8]
        lista_SAT,            # [9]
        lista_QDEC,           # [10]
        lista_ENTP,           # [11]
        lista_SALP,           # [12]
        lista_DAC,            # [13]
        lista_FLT,            # [14]
        lista_SCOPE,          # [15]
        lista_STEP,           # [16]
        lista_TRAPECIO,       # [17]
        lista_DER,            # [18]
        lista_SUM,            # [19]
        lista_REST)           # [20]

    global cambiosArchivo
    cambiosArchivo = False

    global estadoBorrar
    estadoBorrar=False

    #Dirección del archivo
    global directorio
    directorio = "Laboratorio de Control Automático - Archivo Nuevo"
    estadoDirectorio = False

    global ventanaCerrada
    ventanaCerrada = True

    global variable_nombre_dispositivo
    variable_nombre_dispositivo = "COM1"

    global variable_velocidad
    variable_velocidad = 115200

    global variable_tiempo_muestreo
    variable_tiempo_muestreo = 20

    global variable_numero_muestras
    variable_numero_muestras = 1000



    # Layout del Side Bar --------------------------------

    # Frame Icono Guardar Abrir
    frame1 = Frame(sideBar, width=185, height=50, bg="#2C2C2C")
    frame1.pack_propagate(False)
    frame1.grid(row=0, column=0, columnspan=2)

    # Icono Abrir
    imagen_Abrir = PhotoImage(file="Icono_Abrir.png")
    icon_Abrir = Label(frame1, image=imagen_Abrir, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_Abrir.image = imagen_Abrir
    icon_Abrir.pack(side=RIGHT, padx=(0,19))
    icon_Abrir.bind("<ButtonRelease-1>", abrirArchivo)
    icon_Abrir.bind("<Enter>", inButtonAbrir)
    icon_Abrir.bind("<Leave>", outButtonInStructureScreen)

    # Icono Guardar
    imagen_Guardar = PhotoImage(file="Icono_Guardar.png")
    icon_Guardar = Label(frame1, image=imagen_Guardar, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_Guardar.image = imagen_Guardar
    icon_Guardar.pack(side=RIGHT, padx=19)
    icon_Guardar.bind("<ButtonRelease-1>", guardarArchivo)
    icon_Guardar.bind("<Enter>", inButtonGuardar)
    icon_Guardar.bind("<Leave>", outButtonInStructureScreen)
    icon_Guardar.bind("<Button-3>", guardarArchivoComo)

    # Icono Configuracion
    imagen_Configuracion = PhotoImage(file="Icono_Configuracion.png")
    icon_Configuracion = Label(frame1, image=imagen_Configuracion, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_Configuracion.image = imagen_Configuracion
    icon_Configuracion.pack(side=RIGHT)
    icon_Configuracion.bind("<ButtonRelease-1>", configuracionArchivo)
    icon_Configuracion.bind("<Enter>", inButtonConfiguracion)
    icon_Configuracion.bind("<Leave>", outButtonInStructureScreen)

    # Frame Texto Módulos
    frame2 = Frame(sideBar, width=185, height=35, bg="#2C2C2C")
    frame2.pack_propagate(False)
    frame2.grid(row=1, column=0, columnspan=2)

    # Texto Módulos
    Label(frame2, text="Módulos", bg="#2C2C2C", fg="White", font=("Arial Rounded MT", -20)) \
        .pack(side=LEFT, padx=13)

    # Icono Flechas Modulos (cambiar Pagina)
    imagen_Flechas_Modulos = PhotoImage(file="Flecha_Modulos.png")
    imagen_Flechas_Modulos_Label = Label(frame2, image=imagen_Flechas_Modulos, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    imagen_Flechas_Modulos_Label.image = imagen_Flechas_Modulos
    imagen_Flechas_Modulos_Label.pack(side=RIGHT, padx=19)

    global pagina
    pagina = True
    imagen_Flechas_Modulos_Label.bind("<Button-1>", cambiarIconos)


    # Icono ADC
    icono_1 = PhotoImage(file="ADC_sideBar.png")
    icon_1 = Label(sideBar, image=icono_1, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_1.image = icono_1
    icon_1.grid(row=3, column=0, padx=19, pady=(0,19))
    icon_1.bind("<Enter>", inButtonADC)
    icon_1.bind("<Leave>", outButtonInStructureScreen)
    icon_1.bind("<Button-1>", lambda event: coordenadasIcono(event, "ADC"))
    icon_1.bind("<B1-Motion>", arrastrarIcono)
    icon_1.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_ADC))

    # Icono PID
    icono_2 = PhotoImage(file="PID_sideBar.png")
    icon_2 = Label(sideBar, image=icono_2, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_2.image = icono_2
    icon_2.grid(row=3, column=1, padx=(0,19), pady=(0,19))
    icon_2.bind("<Enter>", inButtonPID)
    icon_2.bind("<Leave>", outButtonInStructureScreen)
    icon_2.bind("<Button-1>", lambda event: coordenadasIcono(event, "PID"))
    icon_2.bind("<B1-Motion>", arrastrarIcono)
    icon_2.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_PID))

    # Icono PWM
    icono_3 = PhotoImage(file="PWM_sideBar.png")
    icon_3 = Label(sideBar, image=icono_3, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_3.image = icono_3
    icon_3.grid(row=4, column=0, padx=19, pady=(0,19))
    icon_3.bind("<Enter>", inButtonPWM)
    icon_3.bind("<Leave>", outButtonInStructureScreen)
    icon_3.bind("<Button-1>", lambda event: coordenadasIcono(event, "PWM"))
    icon_3.bind("<B1-Motion>", arrastrarIcono)
    icon_3.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_PWM))

    # Icono RE
    icono_4 = PhotoImage(file="RE_sideBar.png")
    icon_4 = Label(sideBar, image=icono_4, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_4.image = icono_4
    icon_4.grid(row=4, column=1, padx=(0,19), pady=(0,19))
    icon_4.bind("<Enter>", inButtonRE)
    icon_4.bind("<Leave>", outButtonInStructureScreen)
    icon_4.bind("<Button-1>", lambda event: coordenadasIcono(event, "RE"))
    icon_4.bind("<B1-Motion>", arrastrarIcono)
    icon_4.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_RE))

    # Icono CTE
    icono_5 = PhotoImage(file="CTE_sideBar.png")
    icon_5 = Label(sideBar, image=icono_5, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_5.image = icono_5
    icon_5.grid(row=5, column=0, padx=19, pady=(0,19))
    icon_5.bind("<Enter>", inButtonCTE)
    icon_5.bind("<Leave>", outButtonInStructureScreen)
    icon_5.bind("<Button-1>", lambda event: coordenadasIcono(event, "CTE"))
    icon_5.bind("<B1-Motion>", arrastrarIcono)
    icon_5.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_CTE))

    # Icono FT
    icono_6 = PhotoImage(file="FT_sideBar.png")
    icon_6 = Label(sideBar, image=icono_6, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_6.image = icono_6
    icon_6.grid(row=5, column=1, padx=(0,19), pady=(0,19))
    icon_6.bind("<Enter>", inButtonFT)
    icon_6.bind("<Leave>", outButtonInStructureScreen)
    icon_6.bind("<Button-1>", lambda event: coordenadasIcono(event, "FT"))
    icon_6.bind("<B1-Motion>", arrastrarIcono)
    icon_6.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_FT))

    # Icono SAT
    icono_7 = PhotoImage(file="SAT_sideBar.png")
    icon_7 = Label(sideBar, image=icono_7, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_7.image = icono_7
    icon_7.grid(row=6, column=0, padx=19, pady=(0,19))
    icon_7.bind("<Enter>", inButtonSAT)
    icon_7.bind("<Leave>", outButtonInStructureScreen)
    icon_7.bind("<Button-1>", lambda event: coordenadasIcono(event, "SAT"))
    icon_7.bind("<B1-Motion>", arrastrarIcono)
    icon_7.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_SAT))


    # Icono QDec
    icono_8 = PhotoImage(file="QDEC_sideBar.png")
    icon_8 = Label(sideBar, image=icono_8, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_8.image = icono_8
    icon_8.grid(row=6, column=1, padx=(0,19), pady=(0,19))
    icon_8.bind("<Enter>", inButtonQDEC)
    icon_8.bind("<Leave>", outButtonInStructureScreen)
    icon_8.bind("<Button-1>", lambda event: coordenadasIcono(event, "QDEC"))
    icon_8.bind("<B1-Motion>", arrastrarIcono)
    icon_8.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_QDEC))

    # Icono DAC
    icono_9 = PhotoImage(file="DAC_sideBar.png")
    icon_9 = Label(sideBar, image=icono_9, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_9.image = icono_9
    icon_9.grid(row=7, column=0, padx=19, pady=(0, 15))
    icon_9.bind("<Enter>", inButtonDAC)
    icon_9.bind("<Leave>", outButtonInStructureScreen)
    icon_9.bind("<Button-1>", lambda event: coordenadasIcono(event, "DAC"))
    icon_9.bind("<B1-Motion>", arrastrarIcono)
    icon_9.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_DAC))

    # Icono FLT
    icono_10 = PhotoImage(file="FLT_sideBar.png")
    icon_10 = Label(sideBar, image=icono_10, borderwidth=0, highlightthickness=0, bg="#2C2C2C", padx=0, pady=0)
    icon_10.image = icono_10
    icon_10.grid(row=7, column=1, padx=(0, 19), pady=(0, 15))
    icon_10.bind("<Enter>", inButtonFLT)
    icon_10.bind("<Leave>", outButtonInStructureScreen)
    icon_10.bind("<Button-1>", lambda event: coordenadasIcono(event, "FLT"))
    icon_10.bind("<B1-Motion>", arrastrarIcono)
    icon_10.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_FLT))

    # Texto Entrada/Salida
    Label(sideBar, text="Entrada / Salida", bg="#2C2C2C", fg="White", font=("Arial Rounded MT", -20))\
        .grid(row=8, column=0, columnspan=2, padx=13, sticky=W)

    # Barra Horizontal
    imagen_Barra = PhotoImage(file="barra_sideBar.png")
    imagen_Barra2_Label = Label(sideBar, image=imagen_Barra, borderwidth=0, highlightthickness=0, padx=0, pady=0)
    imagen_Barra2_Label.image = imagen_Barra
    imagen_Barra2_Label.grid(row=9, column=0, columnspan=2, pady=(0,19))

    # Icono SALP
    icono_SALP = PhotoImage(file="SALP_sideBar.png")
    icon_SALP = Label(sideBar, bg="#2C2C2C", image=icono_SALP, borderwidth=0, highlightthickness=0, padx=0, pady=0)
    icon_SALP.image = icono_SALP
    icon_SALP.grid(row=10, column=0, padx=19, pady=(0,19))
    icon_SALP.bind("<Enter>", inButtonSALP)
    icon_SALP.bind("<Leave>", outButtonInStructureScreen)
    icon_SALP.bind("<Button-1>", lambda event: coordenadasIcono(event, "SALP"))
    icon_SALP.bind("<B1-Motion>", arrastrarIcono)
    icon_SALP.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_SALP))
    

    #Icono ENTP
    icono_ENTP = PhotoImage(file="ENTP_sideBar.png")
    icon_ENTP = Label(sideBar, bg="#2C2C2C", image=icono_ENTP, borderwidth=0, highlightthickness=0, padx=0, pady=0)
    icon_ENTP.image = icono_ENTP
    icon_ENTP.grid(row=10, column=1, padx=(0, 19), pady=(0, 19))
    icon_ENTP.bind("<Enter>", inButtonENTP)
    icon_ENTP.bind("<Leave>", outButtonInStructureScreen)
    icon_ENTP.bind("<Button-1>", lambda event: coordenadasIcono(event, "ENTP"))
    icon_ENTP.bind("<B1-Motion>", arrastrarIcono)
    icon_ENTP.bind("<ButtonRelease-1>", lambda event: nuevoModulo(event, lista_ENTP))

    global trigger 
    if trigger==1:
        abrirDesdeSystem()
       

def expProgreso():
    
    global animacionBloques
    def animacionBloques():
        global frm_progressBar
        global transmision
        #for i in range (5):
        while (True):
            if transmision==True:
                for j in range(10):
                    
                    #Hacer el bloque celeste
                    squareON=Label(frm_progressBar, bg=tema_Secundario.get(), width=2, height=1)
                    squareON.grid(row=0, column=j, padx=2)
                    sleep(0.2)
                    frm_progressBar.update()

                    #Hacer el bloque azul
                    squareOFF=Label(frm_progressBar, bg=Letras.get(), width=2, height=1)
                    squareOFF.grid(row=0, column=j, padx=2)
            else:
                #time.stop(2)
                break

    global start_Stopwatch
    def start_Stopwatch():
        global Timing
        if not Timing:
            threading.Thread(target=update_stopwatch).start()
            Timing=True

    def graphIt(i):
        global x_vals
        global y_vals
        global Titulos
        global encabezado
        global buffer
        vector_datos=buffer.split(",")
        if vector_datos[0]!="":
            if encabezado:
                Titulos=vector_datos
                encabezado=False
            else:
                x_vals.append(float(vector_datos[0]))
                y_vals.append(float(vector_datos[1]))
                xyAxes= plt.gcf().get_axes()
                xyAxes.cla()
                xyAxes.plot(x_vals, y_vals)
        else:
            Titulos=vector_datos
        vector_datos=[]



    global stop_stopwatch
    def stop_stopwatch():
        global Timing
        if Timing:
            stopwatch.after_cancel(update_time)
            Timing=False

    global update_stopwatch
    def update_stopwatch():
        global hours, minutes, seconds
        seconds+=1
        if seconds==60:
            minutes+=1
            seconds=0
        if minutes==60:
            hours+=1
            minutes=0
        str_hours=f"{hours}" if hours > 9 else f"0{hours}"
        str_minutes=f"{minutes}" if minutes > 9 else f"0{minutes}"
        str_seconds=f"{seconds}" if seconds > 9 else f"0{seconds}"
        stopwatch.configure(text = str_hours + ":" + str_minutes + ":" + str_seconds)
        global update_time
        update_time = stopwatch.after(1000, update_stopwatch)


    def executing():
        running2.config(state=DISABLED)
        frm_progressBar.update()
        global animacionBloques
        global recibirDatos
        global start_Stopwatch
        global transmision
        global lienzo
        global dataFrame
        transmision=True
        global Timing
        Timing=False
        confirmacion = askyesno(title="Ventana de confirmación", message="¿Desea comenzar la ejecución del experimento?")
        if confirmacion:
            threading.Thread(target=animacionBloques).start()
            threading.Thread(target=start_Stopwatch).start()
            threading.Thread(target=recibirDatos).start()
        
    global recibirDatos
    def recibirDatos():
        global variable_nombre_dispositivo
        global variable_velocidad
        global dispositivo
        global transmision
        global buffer
        global variable_tiempo_muestreo
        global catch_data
        global lienzo
        global dataFrame
        puerto = variable_nombre_dispositivo   #Puerto
        velocidad = variable_velocidad         #Baudrate
        archivo = open("Datos_Recibidos.txt", "w")
        #executing()
        trama = 'R'                            #"R" se envía a la planta para que comience la ejecución del experimento
        buffer = ""
        #with serial.Serial(puerto, velocidad, timeout=0.1) as dispositivo:      #Se abre la conexión al dispositivo en el puerto
        dispositivo=serial.Serial(puerto, velocidad, timeout=0.1)
        dispositivo.write(trama.strip().encode())                           #Se escribe "R" en el dispositivo (comienza experimento)
        while True:
            if transmision:
                aByte = dispositivo.read(1)
                if aByte == b"\r":    
                    archivo.write(buffer)
                    archivo.write("\n")
                    Data=buffer + "\n"
                    catch_data.insert(tk.END, Data)
                    catch_data.see(tk.END)
                    catch_data.update()
                    buffer = ""
                    continue
                else:
                    buffer += aByte.decode()
            else:
                break                               
        

    def stop():
        stopping2.configure(state=DISABLED)
        global transmision
        transmision=False
        global dispositivo
        threading.Thread(target=close_port).start()
        threading.Thread(target=stop_stopwatch).start()

    global close_port
    def close_port():
        global dispositivo
        global transmision
        global ventanaEnviados
        global sent
        if not transmision:
            trama = 'T'
            dispositivo.write(trama.strip().encode())
            dispositivo.close()
        time.sleep(3)
        messagebox.showinfo("", "El experimento ha finalizado")
        if sent:
            ventanaEnviados.destroy()
        ventanaRecibidos.destroy()
        expFinalizado()


    def ocultar_Recibidos():
        ventanaRecibidos.withdraw()

    def ver_Enviados():
        def cerrarEnviados():
            global sent
            ventanaEnviados.destroy()
            sent=False

        global mensajeEnviado
        global ventanaEnviados
        global sent
        ventanaEnviados = Toplevel()
        ventanaEnviados.title("Ventana de datos Enviados")
        ventanaEnviados.geometry("500x500")
        ventanaEnviados.resizable(width=False, height=False)
        ventanaEnviados.columnconfigure(0, weight=1)
        ventanaEnviados.rowconfigure(1, weight=1)
        ventanaEnviados.protocol('WM_DELETE_WINDOW', cerrarEnviados)

        titulo=Label(ventanaEnviados, text="Ventana de datos enviados", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
        titulo.grid(row=0, column=0, sticky="ew")
        
        datos=Text(ventanaEnviados, width=500, wrap=WORD, bg=tema_Principal.get(), fg=tema_Secundario.get())
        datos.grid(row=1, column=0, sticky="ns")
        #enviado=mensajeEnviado
        datos.insert(tk.END, mensajeEnviado)
        datos.config(state=DISABLED)
        sent=True

    def ver_Recibidos():
        ventanaRecibidos.deiconify()

    def info_INPROGRESS():
        help_INPROGRESS = Toplevel()
        help_INPROGRESS.columnconfigure(0, weight=1)
        help_INPROGRESS.rowconfigure(1, weight=1)
            
        #Nombre de la Ventana
        help_INPROGRESS.title("Ventana de información")

        #Titulo de la Ventana 
        titulo=Label(help_INPROGRESS, text="Información de la Pantalla de experimento en progreso", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
        titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        informacion_INPROGRESS = Text(help_INPROGRESS, width=500, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        informacion_INPROGRESS.grid(row=1, column=0, sticky="ns")

        text_INPROGRESS="""Está en la Pantalla de experimento en progreso.\nYa ha transmitido una estructura de esperimento a la planta, por lo que ahora puede iniciar la ejecución del experimento al presionar el botón "RUN" en la barra de herramientas. \n\nSi así lo desea, antes de ejecutar el experimento puede presionar el botón "Ver datos enviados" para consultar el mensaje transmitido desde PASCAL. Por otro lado, el botón "Ver datos recibidos" despliega una ventana donde se puede visualizar los datos capturados por PASCAL durante la ejecución de un experimento,\n\nCuando inicie la ejecución del experimento, la barra entre los iconos del chip y la computadora comenzara a mostrar una animación mientras que el cronometro debajo de esta iniciará la cuenta del tiempo. Para finalizar un experimento, presione el botón "STOP" en la barra de herramientas y espere al mensaje que confirma que el experimento se ha detenido\n\nLa barra de herramientas es la barra que se encuentra debajo del título de la pantalla. En el lado derecho de esta barra puede observar el nombre de los botones posicionados a la izquierda de la misma barra al colocar el puntero sobre ellos. Algunos de estos botones estan habilitados y deshabilitados dependiendo de la pantalla en la que se encuentre. Para el caso de la Pantalla de experimento en progreso, el estado de los botones es el siguiente:\n\nATRAS(Habilitado):Cuando es presionado, este botón permite regresar a la pantalla anterior.\n\nDESHACER(Deshabilitado):Cuando es presionado, este botón deshace la última acción realizada por el usuario.\n\nREHACER(Deshabilitado): Cuando es presionado, este botón rehace la última acción deshecha por el usuario.\n\nINFORMACIÓN(Habilitado):Cuando es presionado, este botón abre una ventana con información guía de la pantalla para el usuario.\n\nBORRAR(Deshabilitado): Cuando es presionado, este botón permite eliminar elementos de la estructura de un experimento.\n\nSIMULACIÓN(Deshabilitado):Cuando es presionado, este botón simula una estructura de experimento.\n\nTRANSMITIR(Deshabilitado): Cuando es presionado, este botón envía la información de la estructura de un experimento al hardware.\n\nRUN(Habilitado): Cuando es presionado, este botón inicia la ejecución de un experimento.\n\nSTOP(Habilitado): Cuando es presionado, este botón detiene la ejecución de un experimento.\n\nACERCA DE(Habilitado): Cuando es presionado, este botón despliega una ventana secundaria con información general de PASCAL. """
        informacion_INPROGRESS.insert(tk.END, text_INPROGRESS)
        informacion_INPROGRESS.config(state=DISABLED)

        scrollWindow=Scrollbar(help_INPROGRESS)
        scrollWindow.grid(row=1, column=1, sticky="ns")
        scrollWindow.config(command=informacion_INPROGRESS.yview)
        informacion_INPROGRESS.config(yscrollcommand=scrollWindow.set)
            
        help_INPROGRESS.geometry("500x500")
        help_INPROGRESS.resizable(width=False, height=False)

    def about_PASCAL():
        aboutIt = Toplevel()
        aboutIt.columnconfigure(0, weight=1)
        aboutIt.rowconfigure(0, weight=1)
        
        #Nombre de la ventana
        aboutIt.title("Ventana acerca de PASCAL")
        abrir_ABOUT = Image.open("aboutPASCAL.png")
        global img_about
        img_about = ImageTk.PhotoImage(abrir_ABOUT)

        sobre = Label(aboutIt, image=img_about)
        sobre.grid(row=0, column=0)

        aboutIt.resizable(width=False, height=False)

    def progressToStructure():
        salir = askyesno(title='Ventana de confirmación', message='El experimento será cancelado. ¿Esta seguro que desea regresar?')
        if salir:
            root.deiconify()
            branch.destroy()

    def endSalir():
        salir = askyesno(title='Ventana de confirmación', message='El experimento será cancelado. ¿Esta seguro que desea salir de PASCAL?')
        if salir:
            root.destroy()
            branch.destroy()

    global branch
    branch = Toplevel()
    branch.lift()
    # branch.attributes('-topmost', 'true')
    branch.title("Plataforma acelerada de sistemas de control automático en laboratorio")
    branch.columnconfigure(0, weight=1)
    branch.columnconfigure(1, weight=1)
    branch.configure(bg=tema)
    branch.geometry("1085x655")

    root.withdraw()
    branch.protocol('WM_DELETE_WINDOW', endSalir)

    global catching
    catching=False

    global sent
    sent=False

    global frm_ejecutando       
    frm_ejecutando= Frame(branch, bg=tema_Principal.get())
    frm_ejecutando.pack(fill="both", expand=True)
    frm_ejecutando.columnconfigure(0, weight=1)
    frm_ejecutando.columnconfigure(1, weight=1)
    frm_ejecutando.rowconfigure(2, weight=1)
    frm_ejecutando.rowconfigure(3, weight=1)
 
    mensaje=Label(frm_ejecutando, text="Pantalla de experimento en progreso", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=3, sticky="ew")

    #Barra de Menú
    frm_barra=Frame(frm_ejecutando, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspa=3, sticky="ew", pady=(0,32))

    frm_barra.columnconfigure(0, weight=1)

    global status_bar2
    status_bar2=Label(frm_barra, text="", font=("TkDefaultFont", 10, "bold"), anchor=W, fg="#003366")
    status_bar2.grid(row=0, column=0, sticky="ew")

    #Botones de la barra de Menú
    back2 = Button(frm_barra, image=img_ATRAS, borderwidth=0, command=progressToStructure)
    back2.grid(row = 0, column = 1, sticky=tk.E, padx=10)
    back2.bind("<Enter>", inButtonBack2)
    back2.bind("<Leave>", outButton2)

    revert2 = Button(frm_barra, image=img_REVERTIR, borderwidth=0, state=DISABLED)
    revert2.grid(row = 0, column = 2, sticky=tk.E, padx=10)
    revert2.bind("<Enter>", inButtonRevert2)
    revert2.bind("<Leave>", outButton2)

    redo2 = Button(frm_barra, image=img_REHACER, borderwidth=0, state=DISABLED)
    redo2.grid(row = 0, column = 3, sticky=tk.E, padx=10)
    redo2.bind("<Enter>", inButtonRedo2)
    redo2.bind("<Leave>", outButton2)

    information2 = Button(frm_barra, image=img_INFORMA, borderwidth=0, command=info_INPROGRESS)
    information2.grid(row = 0, column = 4, sticky=tk.E, padx=10)
    information2.bind("<Enter>", inButtonInformation2)
    information2.bind("<Leave>", outButton2)

    erase2 = Button(frm_barra, image=img_BORRAR, borderwidth=0, state=DISABLED)
    erase2.grid(row = 0, column = 5, sticky=tk.E, padx=10)
    erase2.bind("<Enter>", inButtonErase2)
    erase2.bind("<Leave>", outButton2)

    simulate2 = Button(frm_barra, image=img_SIM, borderwidth=0, state=DISABLED)
    simulate2.grid(row = 0, column = 6, sticky=tk.E, padx=10)
    simulate2.bind("<Enter>", inButtonSimulate2)
    simulate2.bind("<Leave>", outButton2)

    transfer2 = Button(frm_barra, image=img_TRANSFER, borderwidth=0, state=DISABLED)
    transfer2.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer2.bind("<Enter>", inButtonTransfer2)
    transfer2.bind("<Leave>", outButton2)

    running2 = Button(frm_barra, image=img_RUN, borderwidth=0, command=executing)
    running2.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running2.bind("<Enter>", inButtonRun2)
    running2.bind("<Leave>", outButton2)

    stopping2 = Button(frm_barra, image=img_STOP, borderwidth=0, command=stop)
    stopping2.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping2.bind("<Enter>", inButtonStop2)
    stopping2.bind("<Leave>", outButton2)

    about2 = Button(frm_barra, image=img_ACERCA, borderwidth=0, command=about_PASCAL)
    about2.grid(row = 0, column = 10, sticky=tk.E, padx=10)
    about2.bind("<Enter>", inButtonAcerca2)
    about2.bind("<Leave>", outButton2)


    #Importando la imagen que representa a la planta
    if tema_Principal.get()=="#2C2C2C":
        imagenPlanta="PlantaIP.png"
        imagenChip="PASCALPC.png"
        imagenEnviada="verEnviado.png"
        imagenRecibida="verRecibido.png"
    else:
        imagenPlanta="PlantaIP2.png"
        imagenChip="PASCALPC2.png"
        imagenEnviada="verEnviado2.png"
        imagenRecibida="verRecibido2.png"

    abrir_PLANTA = Image.open(imagenPlanta)
    abrir_PLANTA = abrir_PLANTA.resize((150, 150), Image.ANTIALIAS)
    global img_PLANTA
    img_PLANTA = ImageTk.PhotoImage(abrir_PLANTA)

    #Importando la imagen que representa a PASCAL
    abrir_PASCAL = Image.open(imagenChip)
    abrir_PASCAL = abrir_PASCAL.resize((150, 150), Image.ANTIALIAS)
    global img_PASCAL
    img_PASCAL = ImageTk.PhotoImage(abrir_PASCAL)


    frm_commpic=Frame(frm_ejecutando, width=550, height=300, bg=tema_Principal.get())
    frm_commpic.grid(row=2, column=0)
    frm_commpic.grid_propagate(False)
    frm_commpic.columnconfigure(0, weight=0)
    frm_commpic.columnconfigure(1, weight=0)
    frm_commpic.columnconfigure(2, weight=0)
    frm_commpic.rowconfigure(0, weight=1)

    chip=Label(frm_commpic, image=img_PLANTA, bg=tema_Principal.get())
    chip.grid(row=0, column=0)

    global frm_progressBar
    frm_progressBar=Frame(frm_commpic, bg=tema_Principal.get())# width=200, height=300, bg=tema_Principal.get())
    frm_progressBar.grid(row=0, column=1)

    for i in range(10):
        frm_progressBar.columnconfigure(i, weight=1)
        square=Label(frm_progressBar, bg=Letras.get(), width=2, height=1)
        square.grid(row=0, column=i, padx=2)

    pc=Label(frm_commpic, image=img_PASCAL, bg=tema_Principal.get())
    pc.grid(row=0, column=2)

    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    global Timing
    Timing = False
    stopwatch=Label(frm_commpic, text="00:00:00", font=("Arial", 30), bg=tema_Principal.get(), fg=tema_Secundario.get())
    stopwatch.grid(row=1, column=1)
    global transmision
    transmision=False

    global frm_data
    frm_data=Frame(frm_ejecutando, width=500, height=300, bg=tema_Principal.get())
    frm_data.grid(row=2, column=1)
    frm_data.grid_propagate(False)
    frm_data.columnconfigure(0, weight=1)
    frm_data.rowconfigure(0, weight=1)
    frm_data.rowconfigure(1, weight=1)

    abrir_ENVIADOS = Image.open(imagenEnviada)
    abrir_ENVIADOS = abrir_ENVIADOS.resize((150, 50), Image.ANTIALIAS)
    global img_ENVIADOS
    img_ENVIADOS = ImageTk.PhotoImage(abrir_ENVIADOS)

    abrir_RECIBIDOS = Image.open(imagenRecibida)
    abrir_RECIBIDOS = abrir_RECIBIDOS.resize((150, 50), Image.ANTIALIAS)
    global img_RECIBIDOS
    img_RECIBIDOS = ImageTk.PhotoImage(abrir_RECIBIDOS)

    btn_datosEnviados=Button(frm_data, image=img_ENVIADOS, bg=tema_Principal.get(), borderwidth=0, command=ver_Enviados)
    btn_datosEnviados.grid(row=0, column=0, pady=25)

    btn_datosRecibidos=Button(frm_data, image=img_RECIBIDOS, bg=tema_Principal.get(), borderwidth=0, command=ver_Recibidos)
    btn_datosRecibidos.grid(row=1, column=0)

    frm_graph=Frame(frm_ejecutando, width=300, height=300)#LabelFrame(frm_ejecutando, text="Gráfico", width=300, height=300)
    frm_graph.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(30,0))
    frm_graph.grid_propagate(False)

    ventanaRecibidos = Toplevel()
    ventanaRecibidos.withdraw()
    ventanaRecibidos.title("Ventana de datos recibidos")
    ventanaRecibidos.geometry("500x500")
    ventanaRecibidos.resizable(width=False, height=False)
    ventanaRecibidos.columnconfigure(0, weight=1)
    ventanaRecibidos.rowconfigure(1, weight=1)

    ventanaRecibidos.protocol('WM_DELETE_WINDOW', ocultar_Recibidos)

    titulo=Label(ventanaRecibidos, text="Ventana de datos capturados", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

    global catch_data
    catch_data=Text(ventanaRecibidos, width=500, wrap=WORD, bg=tema_Principal.get(), fg=tema_Secundario.get())
    catch_data.grid(row=1, column=0, sticky="ns")
    
    vsb=Scrollbar(ventanaRecibidos)
    vsb.grid(row=1, column=1, sticky="ns")
    vsb.config(command=catch_data.yview)
    catch_data.config(yscrollcommand=vsb.set)


def expFinalizado():

    def actualizarGrafico():
        global Titulos
        global variableX, variableY, variableY2
        global tabla
        global grafico
        figura = Figure(figsize=(7,5), dpi=100)
        ax = figura.add_subplot(111)

        tabla.plot(x=variableX.get(), y=variableY.get(), ax=ax, grid=True)
        if variableY2.get()!="None":
            tabla.plot(x=variableX.get(), y=variableY2.get(), ax=ax, grid=True)
    
        if not grafico:
            canvas_Graph = FigureCanvasTkAgg(figura, master=frm_grafico)
            canvas_Graph.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            toolbar_Graph = NavigationToolbar2Tk(canvas_Graph)#, frm_grafico)
            canvas_Graph._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
            grafico=True
        else:
            for widget in frm_grafico.winfo_children():
                widget.destroy()
            canvas_Graph = FigureCanvasTkAgg(figura, master=frm_grafico)
            canvas_Graph.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            toolbar_Graph = NavigationToolbar2Tk(canvas_Graph)
            canvas_Graph._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
            grafico=True

    def export_CSV():
        global tabla
        path = filedialog.asksaveasfilename(initialfile="Untitled-1", defaultextension=".csv")
        tabla.to_csv(path, index=False)
       

    def finalSalir():
        salir = askyesno(title='Ventana de confirmación', message='Los datos del experimento se perderán si no se han guardado. ¿Esta seguro que desea salir de la Pantalla de experimento finalizado?')
        if salir:
            root.deiconify()
            branch.destroy()

    def endSalir():
        salir = askyesno(title='Ventana de confirmación', message='Los datos del experimento se perderán si no se han guardado. ¿Esta seguro que desea salir de PASCAL?')
        if salir:
            branch.destroy()
            root.destroy()

    def about_PASCAL():
        aboutIt = Toplevel()
        aboutIt.columnconfigure(0, weight=1)
        aboutIt.rowconfigure(0, weight=1)
        
        #Nombre de la ventana
        aboutIt.title("Ventana acerca de PASCAL")
        abrir_ABOUT = Image.open("aboutPASCAL.png")
        global img_about
        img_about = ImageTk.PhotoImage(abrir_ABOUT)

        sobre = Label(aboutIt, image=img_about)
        sobre.grid(row=0, column=0)

        aboutIt.resizable(width=False, height=False)

    #Información de la pantalla de configuración
    def info_END():
        help_END = Toplevel()
        help_END.columnconfigure(0, weight=1)
        help_END.rowconfigure(1, weight=1)
            
        #Nombre de la Ventana
        help_END.title("Ventana de información")

        #Titulo de la Ventana 
        titulo=Label(help_END, text="Información de la Pantalla de experimento finalizado", font=("TkDefaultFont", 15), bg=tema_Secundario.get())
        titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        #Información de la pantalla
        informacion_STRUCT = Text(help_END, width=500, wrap=WORD, fg=tema_Secundario.get(), bg=tema_Principal.get())
        informacion_STRUCT.grid(row=1, column=0, sticky="ns")

        text_STRUCT="""Está en la Pantalla de experimento finalizado.\nEn esta pantalla puede generar un gráfico al elegir una variable para graficar en el eje X y hasta dos variables en el eje Y por medio de los menús desplegables. Una vez se han seleccionado las variables de interés, se presiona el botón "Graficar" para generar el gráfico de estas. \n\nCon la opción "Exportar CSV" se pueden exportar los datos capturados durante la ejecución del experimento como un archivo CSV. Es posible elegir un directorio y un nombre para el archivo CSV. \n\nPara regresar a la Pantalla de estructura de experimento, seleccione la opción "Estructura de experimento". Si desea salir de PASCAL, cierre la ventana del programa.\n\nLa barra de herramientas es la barra que se encuentra debajo del título de la pantalla. En el lado derecho de esta barra puede observar el nombre de los botones posicionados a la izquierda de la misma barra al colocar el puntero sobre ellos. Algunos de estos botones estan habilitados y deshabilitados dependiendo de la pantalla en la que se encuentre. Para el caso de la Pantalla de experimento finalizado, el estado de los botones es el siguiente:\n\nATRAS(Deshabilitado):Cuando es presionado, este botón permite regresar a la pantalla anterior.\n\nDESHACER(Deshabilitado):Cuando es presionado, este botón deshace la última acción realizada por el usuario.\n\nREHACER(Deshabilitado): Cuando es presionado, este botón rehace la última acción deshecha por el usuario.\n\nINFORMACIÓN(Habilitado):Cuando es presionado, este botón abre una ventana con información guía de la pantalla para el usuario.\n\nBORRAR(Deshabilitado): Cuando es presionado, este botón permite eliminar elementos de la estructura de un experimento.\n\nSIMULACIÓN(Desabilitado):Cuando es presionado, este botón simula una estructura de experimento.\n\nTRANSMITIR(Deshabilitado): Cuando es presionado, este botón envía la información de la estructura de un experimento al hardware.\n\nRUN(Deshabilitado): Cuando es presionado, este botón inicia la ejecución de un experimento.\n\nSTOP(Deshabilitado): Cuando es presionado, este botón detiene la ejecución de un experimento.\n\nACERCA DE(Habilitado): Cuando es presionado, este botón despliega una ventana secundaria con información general de PASCAL. """
        informacion_STRUCT.insert(tk.END, text_STRUCT)
        informacion_STRUCT.config(state=DISABLED)

        scrollWindow=Scrollbar(help_END)
        scrollWindow.grid(row=1, column=1, sticky="ns")
        scrollWindow.config(command=informacion_STRUCT.yview)
        informacion_STRUCT.config(yscrollcommand=scrollWindow.set)
            
        help_END.geometry("500x500")
        help_END.resizable(width=False, height=False)



    branch.lift()
    frm_ejecutando.destroy()

    branch.protocol('WM_DELETE_WINDOW', endSalir)

    global frm_fin      
    frm_fin= Frame(branch, bg=tema_Principal.get())
    frm_fin.pack(fill="both", expand=True)
    frm_fin.columnconfigure(1, weight=1)
 
    mensaje=Label(frm_fin, text="Pantalla de experimento finalizado", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=2, sticky="ew")

    #Barra de Menú
    frm_barra=Frame(frm_fin, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0,32))

    frm_barra.columnconfigure(0, weight=1)

    global status_bar2
    status_bar2=Label(frm_barra, text="", font=("TkDefaultFont", 10, "bold"), anchor=W, fg="#003366")
    status_bar2.grid(row=0, column=0, sticky="ew")

    #Botones de la barra de Menú
    back2 = Button(frm_barra, image=img_ATRAS, borderwidth=0, state=DISABLED)
    back2.grid(row = 0, column = 1, sticky=tk.E, padx=10)
    back2.bind("<Enter>", inButtonBack2)
    back2.bind("<Leave>", outButton2)

    revert2 = Button(frm_barra, image=img_REVERTIR, borderwidth=0, state=DISABLED)
    revert2.grid(row = 0, column = 2, sticky=tk.E, padx=10)
    revert2.bind("<Enter>", inButtonRevert2)
    revert2.bind("<Leave>", outButton2)

    redo2 = Button(frm_barra, image=img_REHACER, borderwidth=0, state=DISABLED)
    redo2.grid(row = 0, column = 3, sticky=tk.E, padx=10)
    redo2.bind("<Enter>", inButtonRedo2)
    redo2.bind("<Leave>", outButton2)

    information2 = Button(frm_barra, image=img_INFORMA, borderwidth=0, command=info_END)
    information2.grid(row = 0, column = 4, sticky=tk.E, padx=10)
    information2.bind("<Enter>", inButtonInformation2)
    information2.bind("<Leave>", outButton2)

    erase2 = Button(frm_barra, image=img_BORRAR, borderwidth=0, state=DISABLED)
    erase2.grid(row = 0, column = 5, sticky=tk.E, padx=10)
    erase2.bind("<Enter>", inButtonErase2)
    erase2.bind("<Leave>", outButton2)

    simulate2 = Button(frm_barra, image=img_SIM, borderwidth=0, state=DISABLED)
    simulate2.grid(row = 0, column = 6, sticky=tk.E, padx=10)
    simulate2.bind("<Enter>", inButtonSimulate2)
    simulate2.bind("<Leave>", outButton2)

    transfer2 = Button(frm_barra, image=img_TRANSFER, borderwidth=0, state=DISABLED)
    transfer2.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer2.bind("<Enter>", inButtonTransfer2)
    transfer2.bind("<Leave>", outButton2)

    running2 = Button(frm_barra, image=img_RUN, borderwidth=0, state=DISABLED)#, command=threading.Thread(target=executing).start())
    running2.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running2.bind("<Enter>", inButtonRun2)
    running2.bind("<Leave>", outButton2)

    stopping2 = Button(frm_barra, image=img_STOP, borderwidth=0, state=DISABLED)#, command=threading.Thread(target=stop).start())
    stopping2.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping2.bind("<Enter>", inButtonStop2)
    stopping2.bind("<Leave>", outButton2)

    about2 = Button(frm_barra, image=img_ACERCA, borderwidth=0, command=about_PASCAL)
    about2.grid(row = 0, column = 10, sticky=tk.E, padx=10)
    about2.bind("<Enter>", inButtonAcerca2)
    about2.bind("<Leave>", outButton2)

    archivo=open("Datos_Recibidos.txt", "r")

    #Creamos un vector donde guardaremos los titulos o encabezados de la tabla.
    global Titulos
    Titulos =[]
    encabezado=True
    matrix=[]

    while True:
        linea=archivo.readline()
        if not linea:
            break
        if linea=="" or linea=="\n":
            continue
        if linea[0]==",":
            continue
        else:
            vectorlineastr=linea.split(",")
            vectorlineastr[len(vectorlineastr)-1]=vectorlineastr[len(vectorlineastr)-1].replace("\n", "")
            if encabezado:
                Titulos=vectorlineastr
                encabezado=False
            else:
                vectorlineafloat=[]
                for elemento in range(0, len(vectorlineastr)):
                    vectorlineafloat.append(float(vectorlineastr[elemento]))
                matrix.append(vectorlineafloat)

    global tabla
    tabla=pd.DataFrame(matrix, columns=Titulos)

    frm_variables = Frame(frm_fin, bg=tema_Principal.get(), width=300, height=550)
    frm_variables.grid(row=2, column=0)
    frm_variables.grid_propagate(False)
    frm_variables.columnconfigure(0, weight=1)

    global variableX, variableY, variableY2
    global grafico
    grafico=False
    variableX=StringVar()
    variableY=StringVar()
    variableY2=StringVar()
    variableX.set(Titulos[0])
    variableY.set(Titulos[1])
    variableY2.set("None")

    LabelX=Label(frm_variables, text="Graficar en X:", font=("TkDefaultFont", 10), bg=tema_Principal.get(), fg=tema_Secundario.get())
    LabelX.grid(row=0, column=0, pady=25)

    LabelY=Label(frm_variables, text="Graficar en Y:", font=("TkDefaultFont", 10), bg=tema_Principal.get(), fg=tema_Secundario.get())
    LabelY.grid(row=1, column=0, pady=25)

    LabelY2=Label(frm_variables, text="Graficar en Y:", font=("TkDefaultFont", 10), bg=tema_Principal.get(), fg=tema_Secundario.get())
    LabelY2.grid(row=2, column=0, pady=25)

    menuX=OptionMenu(frm_variables, variableX, *Titulos)
    menuX.grid(row=0, column=1, pady=25)
    menuX.config(bg=tema_Secundario.get(), fg=Letras.get())

    menuY=OptionMenu(frm_variables, variableY, *Titulos)
    menuY.grid(row=1, column=1, pady=25)
    menuY.config(bg=tema_Secundario.get(), fg=Letras.get())

    menuY2=OptionMenu(frm_variables, variableY2, *Titulos)
    menuY2.grid(row=2, column=1, pady=25)
    menuY2.config(bg=tema_Secundario.get(), fg=Letras.get())

    button_graph=Button(frm_variables, text="Graficar", font=("TkDefaultFont",10, "bold"), bg=tema_Principal.get(), fg=tema_Secundario.get(), command=actualizarGrafico)
    button_graph.grid(row=3, column=0, columnspan=2, pady=(25, 15))

    button_csv=Button(frm_variables, text="Exportar CSV", font=("TkDefaultFont",10, "bold"), bg=tema_Principal.get(), fg=tema_Secundario.get(), command=export_CSV)
    button_csv.grid(row=4, column=0, columnspan=2, pady=15)

    button_Exit=Button(frm_variables, text="Estructura de experimento", font=("TkDefaultFont",10, "bold"), bg=tema_Principal.get(), fg=tema_Secundario.get(), command=finalSalir)
    button_Exit.grid(row=5, column=0, columnspan=2, pady=15)


    frm_grafico=Frame(frm_fin, bg=tema_Secundario.get(), width=700, height=550)
    frm_grafico.grid(row=2, column=1)
    frm_grafico.grid_propagate(False)



inicio() #Ejecuta la funcion de la pantalla de inicio

root.mainloop()