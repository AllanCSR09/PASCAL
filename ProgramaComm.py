from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import time
from time import sleep
import serial
import serial.tools.list_ports
import pandas as pd
from pandasTable import Table



#Configuracion de la ventana root
root = tk.Tk()
root.title("Plataforma Acelerada de Sistemas de Control Automático en Laboratorio")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.geometry("1085x655")


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


#Funciones de hover (puntero sobre objeto) para todas las pantallas
def inButtonBack(event):
    status_bar.configure(text="ATRÁS")
        
def inButtonRevert(event):
    status_bar.configure(text="DESHACER")

def inButtonRedo(event):
    status_bar.configure(text="REHACER")

def inButtonInformation(event):
    status_bar.configure(text="INFORMACIÓN")

def inButtonErase(event):
    status_bar.configure(text="BORRAR")

def inButtonSimulate(event):
    status_bar.configure(text="SIMULAR")

def inButtonRun(event):
    status_bar.configure(text="RUN")

def inButtonStop(event):
    status_bar.configure(text="STOP")

def inButtonTransfer(event):
    status_bar.configure(text="TRANSFERIR")

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



def expProgress():

    # def show_data(x):
    #     if x=="Recibidos":
           

    #     if x=="Tabla":
            

    def animacionBloques():
        #for i in range (5):
        while (True):
            for j in range(10):
                
                #Hacer el bloque celeste
                squareON=Label(frm_progressBar, bg=tema_Secundario.get(), width=2, height=1)
                squareON.grid(row=0, column=j, padx=2)
                sleep(0.2)
                frm_progressBar.update()

                #Hacer el bloque azul
                squareOFF=Label(frm_progressBar, bg=Letras.get(), width=2, height=1)
                squareOFF.grid(row=0, column=j, padx=2)


    def executing():
        frm_progressBar.update()
        animacionBloques()


    # def recibirDatos():
    #     puerto="COM1"
    #     baudios=115200
    #     dispositivo = serial.Serial(puerto, baudios)
    #     time.sleep(1)

    #     while True:
    #         # valor = dispositivo.readline()
    #         # decode_valor = valor.decode("ascii")
    #         # print(decode_valor)

    #         if dispositivo.isOpen() and dispositivo.in_waiting:
    #             recentPacket=dispositivo.readline()
    #             recentPacketString=recentPacket.decode("utf").rstrip("\n")
    #             Label(dataFrame, text=recentPacketString).pack()
    #         else:
    #             break

    def recibirDatos():
        archivo=open("TextoPrueba.txt", "r")
        #Tabla=pd.DataFrame()

        #Creamos un vector donde guardaremos los titulos o encabezados de la tabla.
        global Titulos
        Titulos =[]
        encabezado=True


        vectorFloat=[]
        
        
        while True:
            linea = archivo.readlines()
            vectorString = linea.split(",")
            if encabezado:
                Titulos = vectorString[elemento]
                encabezado=False
            else:
                for elemento in range(0, len(vectorString)-1):
                    vectorFloat[elemento] = float(vectorString[elemento])




    global frm_ejecutando       
    frm_ejecutando= Frame(root, bg=tema_Principal.get())
    frm_ejecutando.pack(fill="both", expand=True)
    frm_ejecutando.columnconfigure(0, weight=1)
    frm_ejecutando.columnconfigure(1, weight=1)
    frm_ejecutando.rowconfigure(2, weight=1)
    frm_ejecutando.rowconfigure(3, weight=1)
    #frm_ejecutando.columnconfigure(2, weight=1)
    # frm_experimentos.columnconfigure(3, weight=1)

    puertos=serial.tools.list_ports.comports()


    mensaje=Label(frm_ejecutando, text="Pantalla de experimento en progreso", font=("TkDefaultFont", 15), bg=tema_Secundario.get(), fg=Letras.get())
    mensaje.grid(row=0, column=0, columnspan=3, sticky="ew")

    #Barra de Menú
    frm_barra=Frame(frm_ejecutando, bg=tema_Barra.get())
    frm_barra.grid(row=1, column=0, columnspa=3, sticky="ew", pady=(0,32))

    frm_barra.columnconfigure(0, weight=1)
    frm_barra.columnconfigure(1, weight=1)

    global status_bar
    status_bar=Label(frm_barra, text="", font=("TkDefaultFont", 10, "bold"), anchor=W, fg=Letras.get())
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

    information = Button(frm_barra, image=img_INFORMA, borderwidth=0, state=DISABLED)
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

    transfer = Button(frm_barra, image=img_TRANSFER, borderwidth=0, command=executing)#state=DISABLED)
    transfer.grid(row = 0, column = 7, sticky=tk.E, padx=10)
    transfer.bind("<Enter>", inButtonTransfer)
    transfer.bind("<Leave>", outButton)

    running = Button(frm_barra, image=img_RUN, borderwidth=0, command=recibirDatos)#, command=executing)
    running.grid(row = 0, column = 8, sticky=tk.E, padx=10)
    running.bind("<Enter>", inButtonRun)
    running.bind("<Leave>", outButton)

    stopping = Button(frm_barra, image=img_STOP, borderwidth=0, state=DISABLED)
    stopping.grid(row = 0, column = 9, sticky=tk.E, padx=10)
    stopping.bind("<Enter>", inButtonStop)
    stopping.bind("<Leave>", outButton)

    # frm_capturados=LabelFrame(frm_ejecutando, text="Datos capturados", width=1085, height=300)
    # frm_capturados.grid(row=1, column=0, columnspan=2)
    # frm_capturados.grid_propagate(False)

    #Importando la imagen que representa a la planta
    abrir_PLANTA = Image.open("PlantaIP.png")
    abrir_PLANTA = abrir_PLANTA.resize((150, 150), Image.ANTIALIAS)
    global img_PLANTA
    img_PLANTA = ImageTk.PhotoImage(abrir_PLANTA)

    #Importando la imagen que representa a PASCAL
    abrir_PASCAL = Image.open("PASCALPC.png")
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

    for oneport in puertos:
        commButton=Button(frm_commpic, text=oneport)
        commButton.grid(row=puertos.index(oneport), column=0)

    chip=Label(frm_commpic, image=img_PLANTA, bg=tema_Principal.get())
    chip.grid(row=0, column=0)

    frm_progressBar=Frame(frm_commpic, bg=tema_Principal.get())# width=200, height=300, bg=tema_Principal.get())
    frm_progressBar.grid(row=0, column=1)
    #frm_progressBar.grid_propagate(False)
    #frm_progressBar.rowconfigure(0, weight=1)

    for i in range(10):
        frm_progressBar.columnconfigure(i, weight=1)
        square=Label(frm_progressBar, bg=Letras.get(), width=2, height=1)
        square.grid(row=0, column=i, padx=2)

    pc=Label(frm_commpic, image=img_PASCAL, bg=tema_Principal.get())
    pc.grid(row=0, column=2)

    frm_visualizaciones = LabelFrame(frm_ejecutando, text="Datos", width=500, height=300, bg=tema_Principal.get())
    frm_visualizaciones.grid(row=2, column=1)
    frm_visualizaciones.grid_propagate(False)
    frm_visualizaciones.rowconfigure(1, weight=1)

    frm_btn_data=Frame(frm_visualizaciones, width=500)
    frm_btn_data.grid(row=0, column=0, sticky=W)
    #frm_btn_data.grid_propagate(False)
    # frm_btn_data.columnconfigure(0, weight=1)
    # frm_btn_data.columnconfigure(1, weight=1)
    # frm_btn_data.columnconfigure(2, weight=1)

    btn_datosEnviados=Button(frm_btn_data, text="Datos Enviados")
    btn_datosEnviados.grid(row=0, column=0)

    btn_datosRecibidos=Button(frm_btn_data, text="Datos Recibidos", command=show_data("Recibidos"))
    btn_datosRecibidos.grid(row=0, column=1)

    btn_tabla=Button(frm_btn_data, text="Tabla", command=show_data("Tabla"))
    btn_tabla.grid(row=0, column=2)

    frm_data=Frame(frm_visualizaciones, width=500, height=300, bg=tema_Principal.get())
    frm_data.grid(row=1, column=0)
    frm_data.grid_propagate(False)

    frm_data.columnconfigure(0, weight=1)
    frm_data.rowconfigure(0, weight=1)


    dataCanvas=Canvas(frm_data, width=475, height=300)
    dataCanvas.grid(row=0, column=0)
    dataCanvas.grid_propagate(False)

    vsb=Scrollbar(frm_data, orient=VERTICAL, command=dataCanvas.yview)
    vsb.grid(row=0, column=1, sticky="ns")
    dataCanvas.config(yscrollcommand=vsb.set)

    dataFrame=Frame(dataCanvas, width=475, height=300)
    dataCanvas.create_window((0,0), window=dataFrame, anchor="nw")


    frm_graph=LabelFrame(frm_ejecutando, text="Gráfico", width=300, height=300)
    frm_graph.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(30,0))
    frm_graph.grid_propagate(False)

        



expProgress()
root.mainloop()
    